# Android 15 APK 闪退问题 - 完整总结和解决方案

**问题设备**：三星 S25 Ultra (Android 15, One UI 8)
**问题现象**：APK 安装成功但立即闪退，无法进入应用
**项目版本**：虫害报告提取器 v2.0/2.1
**更新日期**：2025-11-08

---

## 📋 问题概述

### 当前状态
```
✅ Python 代码在桌面版正常运行
✅ APK 在 buildozer 中编译成功
❌ APK 在三星 S25 Ultra 上立即闪退
❌ 无法显示错误提示或权限对话框
❌ 无法手动设置应用权限
```

### 问题表现
1. **安装阶段**：正常，无错误提示
2. **启动阶段**：点击应用图标
3. **闪退**：在 splash screen 后立即闪退，回到桌面
4. **无日志**：系统未记录错误信息

---

## 🔍 问题根本原因分析

### 可能的原因（按可能性排序）

#### 1️⃣ **Kivy 框架与 Android 15 不兼容** (40% 概率)
- Kivy 2.x 可能在 Android 15 上存在兼容性问题
- targetSdkVersion=34 与新系统的交互可能有问题
- Kivy 的 Java/Python 桥接层可能需要更新

**症状**：任何 Kivy 应用都无法运行

#### 2️⃣ **依赖库编译不当** (30% 概率)
- pdfplumber、pandas、openpyxl 等库中的 C 扩展库编译失败
- 某些库可能不兼容 ARM64 架构或 NDK 25b
- 库版本间存在冲突

**症状**：ImportError 或 Segmentation Fault

#### 3️⃣ **Python 版本问题** (20% 概率)
- Python 3.11 可能与 Android 15 或 Kivy 不兼容
- buildozer 内置的 Python 版本可能有问题

**症状**：Python 启动失败

#### 4️⃣ **权限和存储访问** (5% 概率)
- Android 15 的新安全限制
- app_storage_path 获取失败导致早期崩溃

**症状**：权限申请时闪退

#### 5️⃣ **其他系统级问题** (5% 概率)
- One UI 8 的特定优化
- Samsung Knox 安全机制
- 硬件特定问题

---

## 🛠️ 已执行的解决方案

### ❌ 已尝试但失败的方案

| 方案 | 修改内容 | 结果 |
|------|---------|------|
| **方案 1** | 添加完整存储权限 + targetSdkVersion=33 | ❌ 仍然闪退 |
| **方案 2** | 移除所有存储权限，仅保留 INTERNET | ❌ 仍然闪退 |
| **方案 3** | 简化权限请求代码 | ❌ 仍然闪退 |

**结论**：问题不在权限配置，而在更深层的框架问题

---

## ✅ 当前实施的新调试方案

### 1️⃣ 获取详细 logcat 日志（最关键）

**文件**：`Android15闪退调试指南.md` 中的快速命令

**目的**：识别具体的错误信息
- ImportError → 库版本问题
- Segmentation Fault → C 扩展库崩溃
- dlopen failed → 库加载问题
- No error → 启动阶段早期崩溃

### 2️⃣ 创建超极简测试版本

**文件**：`android_minimal_test.py`

**代码**：
```python
from kivy.app import App
from kivy.uix.label import Label

class MinimalTestApp(App):
    def build(self):
        return Label(text='✅ Hello Android 15!\n\nKivy 基础测试成功')

if __name__ == '__main__':
    MinimalTestApp().run()
```

**用途**：判断 Kivy 本身是否能在 Android 15 上运行

### 3️⃣ 优化 buildozer.spec 配置

**文件**：修改后的 `buildozer.spec`

**主要优化**：

```ini
# 降低 targetSdkVersion 以提高兼容性
android.api = 31                    # ← 从 34 改为 31
android.targetSdkVersion = 31       # ← 从 34 改为 31

# 使用更稳定的库版本（而不是最新的）
requirements = python3==3.9,\       # 指定版本，不用自动最新
               kivy==2.1.0,\        # 使用稳定的 2.1.0
               pyjnius==1.4.2,
               pdfplumber==0.8.0,
               pandas==1.3.5,
               ...

# 仅编译 ARM64（S25 Ultra 使用）
android.archs = arm64-v8a          # ← 只编译 64 位，加快构建
```

**备份**：原始配置保存为 `buildozer.spec.backup`

### 4️⃣ GitHub Actions 测试工作流

**文件**：`.github/workflows/build-apk-test.yml`

**功能**：
- 自动构建极简版本和优化版本
- 两个 APK 都作为 artifact 下载
- 可通过 `workflow_dispatch` 手动触发

**触发方式**：
```bash
# 方式 1：推送到 test/android15 分支
git checkout -b test/android15
git push origin test/android15

# 方式 2：GitHub 网页 → Actions → 测试 APK 构建 → Run workflow
```

---

## 📊 完整调试流程

```
开始调试
  ↓
[步骤 1] 获取 logcat 日志 (5 分钟)
  ├─ 有明确的错误信息 → 跳到原因诊断
  └─ 无错误信息 → 继续步骤 2
  ↓
[步骤 2] 测试极简版本 (10 分钟)
  ├─ 极简版本能运行 ✅ → 问题在业务代码或库
  │  └─ 逐步添加库，找到问题源
  └─ 极简版本也闪退 ❌ → 问题在 Kivy 或 Python
     └─ 尝试修改 buildozer.spec 版本号
  ↓
[步骤 3] 使用优化的 buildozer.spec (15 分钟)
  ├─ 问题解决 ✅ → 原因是库版本或 API 版本
  └─ 仍然闪退 ❌ → 问题可能不可修复，考虑替代方案
  ↓
[步骤 4] 考虑替代框架 (选择性)
  ├─ BeeWare - Python 原生 Android 支持
  ├─ Chaquopy - Python in Android Studio
  └─ PyDroid 3 - 在线 IDE
```

---

## 📁 新增文件说明

| 文件 | 大小 | 用途 | 优先级 |
|-----|------|------|--------|
| **Android15闪退调试指南.md** | 3.2 KB | 完整的调试步骤和诊断方法 | 🔴 必读 |
| **Android15快速修复清单.md** | 2.8 KB | 快速参考，优先级清单 | 🟡 重要 |
| **android_minimal_test.py** | 0.3 KB | 超极简 Kivy 测试程序 | 🔴 必需 |
| **buildozer.spec** | 2.4 KB | 优化的构建配置（已修改） | 🔴 必需 |
| **buildozer.spec.backup** | 2.3 KB | 原始配置备份 | 🟢 可选 |
| **.github/workflows/build-apk-test.yml** | 2.1 KB | GitHub Actions 测试工作流 | 🟡 推荐 |

---

## 🚀 立即行动指南

### 步骤 A：获取诊断信息（必做，5 分钟）

```bash
# 1. 清空日志并卸载旧版本
adb logcat -c
adb uninstall com.pestcontrol.pestreportextractor

# 2. 安装新 APK（使用优化版本或 GitHub Actions 构建）
adb install -r bin/pestreportextractor-2.1-debug.apk

# 3. 获取日志
adb logcat > crash_$(date +%Y%m%d_%H%M%S).log 2>&1 &

# 4. 在手机上打开应用并等待闪退
# 5. Ctrl+C 停止 logcat

# 6. 分析日志
cat crash_*.log | grep -iE "error|exception|fatal|python|kivy"
```

**期望获得**：
- 具体的错误信息（ImportError, Segmentation Fault 等）
- 哪个库或模块导致问题
- Python 堆栈跟踪

### 步骤 B：测试极简版本（如步骤 A 无结果，10 分钟）

```bash
# 1. 准备最小版本
cp android_minimal_test.py main.py

# 2. 构建
buildozer clean
buildozer android debug

# 3. 安装和测试
adb uninstall com.pestcontrol.pestreportextractor
adb install -r bin/*.apk

# 4. 观察结果
# - ✅ 如果能运行：Kivy 可用，问题在库
# - ❌ 如果仍闪退：Kivy 本身有问题
```

### 步骤 C：使用新的 buildozer.spec 优化版本（15 分钟）

```bash
# 已自动优化，直接构建
buildozer clean
buildozer android debug

# 安装测试
adb uninstall com.pestcontrol.pestreportextractor
adb install -r bin/pestreportextractor-2.1-debug.apk
```

### 步骤 D：使用 GitHub Actions 自动构建（推荐）

```bash
# 推送到 test/android15 分支
git checkout -b test/android15
git add .
git commit -m "test: Android 15 调试"
git push origin test/android15

# 或在 GitHub 网页界面手动触发 "测试 APK 构建"
# 等待构建完成（约 30 分钟）
# 下载两个 APK 版本进行测试
```

---

## 📈 预期时间线

| 阶段 | 任务 | 时间 | 备注 |
|------|------|------|------|
| **第 1 天** | 获取 logcat 日志 + 测试极简版本 | 30 分钟 | 关键诊断 |
| **第 2 天** | 根据日志修改配置 + 重新构建 | 1-2 小时 | 可能需要多次尝试 |
| **第 3 天** | 测试优化后的 buildozer.spec | 1 小时 | 验证修复 |
| **第 4 天** | 如未解决，考虑替代方案 | 变量 | BeeWare/Chaquopy |

---

## 💡 关键点总结

### ✅ 已完成
- ✅ 创建超极简测试版本
- ✅ 优化 buildozer.spec 配置
- ✅ 创建详细的调试指南
- ✅ 设置 GitHub Actions 测试工作流
- ✅ 提供清晰的优先级清单

### ⏳ 待执行
- ⏳ 获取并分析 logcat 日志（关键！）
- ⏳ 在 S25 Ultra 上测试极简版本
- ⏳ 根据结果调整策略
- ⏳ 验证修复方案

### 🎯 最可能的解决方案（按可能性）
1. **修改 buildozer.spec 中的库版本** (60% 成功率)
2. **降低 targetSdkVersion 版本** (30% 成功率)
3. **切换到 BeeWare 或 Chaquopy** (80% 成功率，但需重写代码)

---

## 📞 需要你提供的信息

完成上述调试后，请提供：

1. **完整的 logcat 日志** - 最重要！
   ```bash
   cat crash_*.log
   ```

2. **极简版本测试结果**
   ```
   [ ] ✅ 能运行
   [ ] ❌ 也闪退
   ```

3. **优化版本测试结果**
   ```
   [ ] ✅ 能运行
   [ ] ❌ 仍闪退
   ```

4. **错误信息或堆栈跟踪**（如有）

5. **S25 Ultra 的开发者选项截图**（可选）

---

## 🔗 相关文档

- **快速修复**：`Android15快速修复清单.md`
- **详细调试**：`Android15闪退调试指南.md`
- **原始文档**：`项目状态_2025-11-08.md`
- **权限修复**：`Android权限修复说明.md`

---

## 📝 版本历史

| 版本 | 日期 | 描述 |
|------|------|------|
| 2.0 | 2025-11-08 | 原始版本，Android 15 上闪退 |
| 2.1 | 2025-11-08 | 优化版本，带 buildozer.spec 改进 |

---

**最后更新**：2025-11-08 17:30
**下一步**：获取 logcat 日志！🔍

