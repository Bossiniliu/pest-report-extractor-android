# Android 15 快速修复清单

**目标**：在三星 S25 Ultra (Android 15) 上运行 APK
**状态**：正在调试
**最后更新**：2025-11-08

---

## 🚀 快速修复步骤 (按优先级排列)

### ✅ 步骤 1：获取崩溃日志 (5 分钟) - **必做！**

```bash
# 清空日志
adb logcat -c

# 卸载旧版本
adb uninstall com.pestcontrol.pestreportextractor

# 安装新 APK
adb install -r bin/pestreportextractor-2.1-debug.apk

# 获取日志（在另一个终端）
adb logcat > crash.log 2>&1 &

# 在手机上点击应用
# 等待 10 秒闪退，然后 Ctrl+C 停止日志记录

# 查看错误
cat crash.log | grep -iE "error|exception|fatal|crash"
```

### ✅ 步骤 2：测试极简版本 (10 分钟)

如果步骤 1 无法诊断，测试超极简 Kivy：

```bash
# 构建极简版本
buildozer clean
cp android_minimal_test.py main.py
buildozer android debug

# 测试
adb install -r bin/*.apk
adb logcat | grep -iE "kivy|python|error"
```

**预期结果**：
- ✅ 如果极简版本可以运行 → 问题在后续的库（pdfplumber/pandas 等）
- ❌ 如果极简版本也崩溃 → 问题在 Kivy 框架本身

### ✅ 步骤 3：尝试优化配置 (5 分钟)

已修改的 `buildozer.spec` 包含：
- 降低 targetSdkVersion 从 34 → 31
- 固定库版本（Python 3.9, Kivy 2.1.0 等）
- 仅编译 ARM64 架构

```bash
# 使用新配置构建
buildozer clean
buildozer android debug

# 测试
adb install -r bin/*.apk
```

### ✅ 步骤 4：使用 GitHub Actions 构建测试版本 (2 分钟)

新增了 `.github/workflows/build-apk-test.yml` 用于构建两个版本：

1. **极简测试版** - 仅 Kivy UI
2. **优化版本** - 带优化的 buildozer.spec

```bash
# 推送到 test/android15 分支触发构建
git checkout -b test/android15
git add .
git commit -m "test: Android 15 调试版本"
git push origin test/android15

# 或在 GitHub Actions 页面手动触发 "测试 APK 构建"
```

---

## 📊 问题诊断流程图

```
APK 闪退
  ↓
[获取 logcat]
  ↓
  ├─ Python/Kivy ImportError → 库版本冲突
  │    └─ 解决：修改 buildozer.spec 中的库版本
  │
  ├─ Segmentation Fault → C 扩展库崩溃
  │    └─ 解决：使用纯 Python 库或降低版本
  │
  ├─ dlopen failed → 架构或库加载问题
  │    └─ 解决：仅编译 ARM64 或更新 NDK
  │
  ├─ Permission denied → 权限问题
  │    └─ 解决：检查 android.permissions 设置
  │
  ├─ No error (但仍然闪退) → 早期启动崩溃
  │    └─ 解决：测试极简版本，逐步添加功能
  │
  └─ 其他错误 → 查看 logcat 或提供日志
```

---

## 🔧 已修改的文件

| 文件 | 修改内容 | 用途 |
|-----|---------|------|
| **buildozer.spec** | ✅ 降低 API 版本、固定库版本、仅 ARM64 | 主要优化版本 |
| **android_minimal_test.py** | ✅ 新增超极简 Kivy 程序 | 基础测试 |
| **buildozer.spec.backup** | ✅ 备份原始配置 | 恢复用 |
| **.github/workflows/build-apk-test.yml** | ✅ 新增测试工作流 | GitHub 自动构建测试版本 |
| **Android15闪退调试指南.md** | ✅ 详细调试文档 | 完整参考 |

---

## 📝 关键配置说明

### buildozer.spec 优化版本

```ini
# 原始版本
python3,kivy,pyjnius,...

# 优化版本（更稳定）
python3==3.9,kivy==2.1.0,pyjnius==1.4.2,...

# 原始 targetSdkVersion
android.targetSdkVersion = 34

# 优化版本（兼容性更好）
android.targetSdkVersion = 31

# 原始架构
android.archs = arm64-v8a,armeabi-v7a

# 优化版本（仅 S25 Ultra）
android.archs = arm64-v8a
```

---

## 💡 常见问题速答

| 问题 | 答案 |
|-----|------|
| **APK 构建失败？** | 检查 `.buildozer/android/platform/build-*/build.log` |
| **APK 安装失败？** | 运行 `adb uninstall com.pestcontrol.pestreportextractor` 后重试 |
| **看不到应用图标？** | 应用闪退前未到达主屏幕。查看 logcat 日志。 |
| **权限弹窗出不来？** | 应用在权限请求前就已闪退。这是核心问题。 |
| **文件无法保存？** | 先解决闪退问题，这是后续问题。 |

---

## 🎯 预期测试结果

完成以上步骤后，你应该知道：

```markdown
[ ] 极简版本 (仅 Label) 是否能运行？
    - ✅ 是 → Kivy 可用，问题在后续库
    - ❌ 否 → Kivy 与 Android 15 不兼容

[ ] 原始版本 (完整 PDF 处理) 是否能运行？
    - ✅ 是 → 所有库兼容，万岁！
    - ❌ 否 → 需要进一步调试

[ ] 优化版本 (API 31 + 固定版本) 是否能运行？
    - ✅ 是 → 配置优化有效
    - ❌ 否 → 需要尝试其他框架
```

---

## 📞 下一步

1. **立即执行步骤 1** - 获取 logcat 日志
2. **分析日志中的错误** - 这将指导后续修复
3. **执行相应步骤** - 根据错误类型选择修复方案
4. **提交结果** - 记录测试结果，便于追踪

---

**记住**：日志是金钱！先获取日志再做任何修改。🔍

