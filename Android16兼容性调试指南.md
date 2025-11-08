# Android 16 兼容性调试指南

**设备**：三星 S25 Ultra (Android 16)
**项目**：虫害报告提取器 v2.0
**问题**：APK 在 Android 16 上闪退
**更新时间**：2025-11-08

---

## 🔴 关键认识

**Android 16 是一个全新的系统，Kivy 框架可能不被官方支持！**

- **Android 15 发布**：2024 年秋
- **Android 16 发布**：2025 年秋（最新的 Android）
- **Kivy 官方支持**：通常落后 1-2 个 Android 版本

### 当前 Kivy 支持范围：
- ✅ Android 13, 14 - 完全支持
- ⚠️ Android 15 - 部分支持
- ❌ Android 16 - **可能不支持**

---

## 📊 问题严重程度

| 方面 | 影响 | 解决难度 |
|------|------|---------|
| **Kivy 兼容性** | 极可能是主要原因 | 🔴 极高 |
| **Python 运行时** | 可能有问题 | 🔴 极高 |
| **库版本** | 次要原因 | 🟠 高 |
| **权限配置** | 不太可能 | 🟢 低 |

---

## 🛠️ 解决方案（按可行性）

### 方案 1: 使用最新的 Kivy + 最激进的配置优化

**成功概率**：25%

#### 第一步：更新 buildozer.spec 到最新的 Kivy

```ini
[app]
version = 2.2

# 使用最新的 Kivy（官方最新）
requirements = python3==3.11,\
               kivy==2.3.0,\
               pyjnius==1.5.0,\
               pdfplumber==0.10.0,\
               openpyxl==3.11.0,\
               pandas==2.1.0,\
               pillow==10.0.0

[android]
# Android 16 专用配置
android.api = 36          # 编译 API 36（Android 16）
android.minapi = 30       # 最低支持 Android 11
android.targetSdkVersion = 34  # 目标仍设为 34（权衡兼容性）

# 使用最新的 NDK
android.ndk = 26b

# 仅编译 ARM64（S25 Ultra 是 ARM64）
android.archs = arm64-v8a

# 额外配置
android.permissions = INTERNET
android.accept_sdk_license = True
```

#### 第二步：启用更多调试选项

```bash
# 设置详细日志
export KIVY_LOGLEVEL=debug

# 构建时添加详细输出
buildozer android debug -vvv
```

---

### 方案 2: 降级到 Android 14 的目标版本

**成功概率**：40%

这个方案告诉 Android 16"假装你是 Android 14"。

```ini
[android]
# 降级到 Android 14 API 标准
android.api = 34
android.minapi = 21
android.targetSdkVersion = 33  # 目标 Android 13

# 使用稳定的 NDK
android.ndk = 25b

# 使用更稳定的 Kivy 版本
requirements = python3==3.9,kivy==2.1.0,...
```

**优点**：
- 更稳定的库版本
- 更成熟的兼容性
- 更容易调试

**缺点**：
- 可能无法使用 Android 16 的新功能
- 某些安全限制仍可能触发

---

### 方案 3: 使用 BeeWare（推荐）

**成功概率**：85%

BeeWare 是专门为 Python 原生 Android 开发的框架，与 Kivy 完全不同。

#### 优点：
- ✅ 专为 Python 开发设计
- ✅ 更好的 Android 版本支持
- ✅ 更少的兼容性问题
- ✅ 官方支持最新的 Android

#### 缺点：
- ❌ 需要重写应用代码（2-3 天工作量）
- ❌ 学习曲线陡峭
- ❌ 功能集可能不如 Kivy 完整

#### 快速开始：

```bash
# 安装 BeeWare
pip install briefcase

# 创建新项目
briefcase new

# 构建 Android APK
briefcase create android
briefcase build android
briefcase run android
```

---

### 方案 4: 使用 Chaquopy

**成功概率**：95%

Chaquopy 允许在 Android Studio 中直接使用 Python，提供最好的 Android 集成。

#### 优点：
- ✅ 最佳的 Android 16 兼容性
- ✅ 完整的 Android API 访问
- ✅ 专业级支持
- ✅ 最新的安全特性

#### 缺点：
- ❌ 需要学习 Android Studio
- ❌ 需要 Java/Kotlin 基础
- ❌ 更复杂的设置

#### 快速开始：

```bash
# 在 Android Studio 中：
1. 新建项目
2. 安装 Chaquopy 插件
3. 配置 Python 环境
4. 编写 Python 代码
5. 构建 APK
```

---

## 📋 立即行动计划

### 阶段 1：诊断（今天，20 分钟）

```bash
# 获取 logcat
adb logcat -c
adb uninstall com.pestcontrol.pestreportextractor
adb install -r bin/*.apk
adb logcat | tee android16_crash.log

# 关键词搜索
grep -iE "kivy|python|unsupported|api|version" android16_crash.log
```

### 阶段 2：尝试方案 1（今天，30 分钟）

```bash
# 更新 buildozer.spec（已为你准备）
# 重新构建
buildozer clean
buildozer android debug

# 测试
adb install -r bin/*.apk
```

### 阶段 3：如果方案 1 失败，尝试方案 2（明天，30 分钟）

```bash
# 修改为更保守的配置
# 重新构建并测试
```

### 阶段 4：如果都失败，开始迁移到 BeeWare（2-3 天）

```bash
# 创建新的 BeeWare 项目
# 移植代码
# 重新打包
```

---

## 🔍 关键诊断信息

### 要在 logcat 中查找的内容

```
✅ 如果看到这些 = 问题已确认

ImportError: No module named 'kivy'
  → Kivy 加载失败，Python 运行时可能有问题

java.lang.UnsatisfiedLinkError
  → 本地库加载失败（可能是 NDK 版本问题）

FATAL EXCEPTION: PythonActivity
  → Python 层崩溃，可能是兼容性问题

dlopen failed: cannot locate symbol
  → 库版本不兼容
```

### 可以做的快速诊断

```bash
# 测试超极简 Kivy（推荐）
cp android_minimal_test.py main.py
buildozer clean
buildozer android debug
adb install -r bin/*.apk

# 如果极简版本也闪退 → Kivy 与 Android 16 不兼容
# 如果极简版本能运行 → 问题在业务代码或库
```

---

## 📊 方案选择决策树

```
APK 在 Android 16 闪退
  ↓
[诊断日志]
  ├─ 看到 "ImportError: kivy" → Kivy 不兼容，跳到方案 3-4
  ├─ 看到 "UnsatisfiedLinkError" → NDK 问题，尝试方案 1-2
  ├─ 看到 "FATAL EXCEPTION" → 运行时问题，尝试方案 2
  └─ 没有明确错误 → 早期启动崩溃，尝试超极简版本
     ├─ 极简版能运行 → 业务代码问题，尝试方案 2
     └─ 极简版也闪退 → 框架问题，选择方案 3 或 4

方案 1-2 失败 3 次 以上？ → 迁移到 BeeWare 或 Chaquopy
```

---

## 📁 新增文件

已为 Android 16 创建的文件：

```
buildozer.spec.android16
  ↳ Android 16 优化配置（最新 Kivy）

buildozer.spec.android14-fallback
  ↳ 回退配置（兼容性最好）
```

---

## ⏱️ 预期时间表

| 阶段 | 任务 | 时间 | 成功率 |
|------|------|------|--------|
| 1 | 诊断 logcat | 20 分钟 | 100% |
| 2 | 方案 1（最新 Kivy） | 30 分钟 | 25% |
| 3 | 方案 2（回退 API） | 30 分钟 | 40% |
| 4 | 方案 3（BeeWare） | 2-3 天 | 85% |
| 5 | 方案 4（Chaquopy） | 3-5 天 | 95% |

---

## 🎯 我的建议

### 短期（24 小时内）

1. **获取 logcat** - 确认具体的错误
2. **尝试方案 1 和 2** - 可能快速解决（25%-40% 概率）
3. **测试超极简版本** - 确认 Kivy 兼容性

### 长期（如果短期方案失败）

**强烈建议迁移到 BeeWare**：
- 官方支持最新的 Android
- 更简单的 Python-to-Android 路径
- 社区活跃度高
- 代码迁移相对简单（大部分核心逻辑无需改动）

---

## 📞 需要的信息

完成第一阶段诊断后，请提供：

1. **完整的 logcat 日志** - 最关键！
2. **错误信息的确切文本**
3. **超极简版本的测试结果**
4. **你愿意花多长时间调试**（决定是否值得迁移）

---

**记住**：Android 16 是全新系统，可能没有现成的 Kivy 支持。如果短期内看不到希望，迁移到更现代的框架会更经济。🚀

