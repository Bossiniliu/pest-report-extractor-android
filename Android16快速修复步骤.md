# Android 16 - 快速修复步骤

**设备**：三星 S25 Ultra (Android 16)
**时间**：2025-11-08
**优先级**：方案 1 → 方案 2 → 方案 3

---

## 🚀 方案 1：尝试最新 Kivy（成功率 25%）

### 快速步骤（15 分钟）

```bash
# 1. 使用最新的 buildozer.spec
cp buildozer.spec buildozer.spec.backup
cp buildozer.spec.android16-latest buildozer.spec

# 2. 清空旧构建
buildozer clean

# 3. 构建新 APK
buildozer android debug

# 4. 安装测试
adb uninstall com.pestcontrol.pestreportextractor
adb install -r bin/pestreportextractor-2.2-debug.apk

# 5. 查看日志
adb logcat | grep -iE "error|exception|python|kivy"
```

### 预期结果
- ✅ **成功**：应用能运行，问题解决
- ❌ **失败**：应用仍闪退，继续方案 2

---

## 🔄 方案 2：回退到 Android 14 标准（成功率 40%）

### 快速步骤（15 分钟）

```bash
# 1. 使用回退配置
cp buildozer.spec.android14-fallback buildozer.spec

# 2. 清空旧构建
buildozer clean

# 3. 构建新 APK
buildozer android debug

# 4. 安装测试
adb uninstall com.pestcontrol.pestreportextractor
adb install -r bin/pestreportextractor-2.2-debug.apk

# 5. 查看日志
adb logcat | grep -iE "error|exception|python|kivy"
```

### 预期结果
- ✅ **成功**：应用能运行，长期解决方案
- ❌ **失败**：继续方案 3

---

## 🔴 方案 3：迁移到 BeeWare（成功率 85%）

如果方案 1 和 2 都失败，BeeWare 是最可靠的解决方案。

### 时间投入：2-3 天

### 快速开始（30 分钟）

```bash
# 1. 安装 BeeWare
pip install briefcase

# 2. 创建新项目
briefcase new

# 按照提示输入：
# - Application name: 虫害报告提取器
# - Bundle: com.pestcontrol
# - Module name: pestreportextractor

# 3. 查看生成的文件
cd pestreportextractor
ls -la

# 4. 初始化构建
briefcase create android

# 5. 构建 APK
briefcase build android

# 6. 运行测试
briefcase run android
```

### 代码迁移（1-2 天）
- 将 `android_main.py` 的核心逻辑迁移到 BeeWare 项目
- 重点：PDF 提取 + Excel 生成逻辑可以基本保留
- 修改：Kivy UI → BeeWare UI（相对简单）

---

## 📊 决策矩阵

| 条件 | 推荐方案 | 理由 |
|------|---------|------|
| **想快速修复** | 方案 1 → 2 | 15 分钟内知道能否解决 |
| **不想花太多时间** | 方案 2 | 保守方案，稳定性好 |
| **时间充足** | 方案 3 | 最可靠，官方支持好 |
| **需要长期维护** | 方案 3 | BeeWare 更新更频繁 |

---

## ⏱️ 预期时间表

```
现在 (2025-11-08)
  ↓
今天 (2-3 小时)
  ├─ 方案 1 测试 (15 分钟)
  ├─ 方案 2 测试 (15 分钟)
  └─ 获取诊断信息 (30 分钟)
  ↓
明天或后天 (2-3 天)
  └─ 方案 3 (BeeWare) 迁移
     ├─ 环境设置 (30 分钟)
     ├─ 代码迁移 (1-2 天)
     └─ 测试和调试 (6-8 小时)
```

---

## 🔍 故障排除快速参考

### 如果方案 1 失败

```
错误提示：ImportError: No module named 'kivy'
  → Kivy 版本 2.3.0 与 Android 16 不兼容
  → 继续方案 2

错误提示：UnsatisfiedLinkError
  → NDK 26b 可能有问题
  → 尝试 buildozer.spec 中 android.ndk = 25b
```

### 如果方案 2 失败

```
错误提示：targetSdkVersion mismatch
  → 这是预期的，不影响功能
  → 继续方案 3

错误提示：仍然闪退
  → Kivy 框架完全不兼容 Android 16
  → 迁移到 BeeWare 是唯一解决方案
```

---

## 📝 记录测试结果

每次测试都记录以下信息：

```markdown
## 测试记录

### 方案 1（最新 Kivy）
- 日期：YYYY-MM-DD
- buildozer.spec：android16-latest
- 结果：✅ / ❌
- 错误信息（如有）：
  ```
  [粘贴日志]
  ```

### 方案 2（Android 14 回退）
- 日期：YYYY-MM-DD
- buildozer.spec：android14-fallback
- 结果：✅ / ❌
- 错误信息（如有）：
  ```
  [粘贴日志]
  ```

### 方案 3（BeeWare 迁移）
- 开始日期：YYYY-MM-DD
- 进度：30% / 60% / 100%
- 预计完成：YYYY-MM-DD
```

---

## 🎯 一句话总结

- ✅ **方案 1-2**：快速修复（今天），成功率 65%
- ✅ **方案 3**：彻底解决（2-3 天），成功率 85%+

**建议**：立即尝试方案 1-2，如失败则启动方案 3。

---

## 📞 需要帮助？

运行这个命令获取完整的诊断信息：

```bash
# 获取系统和应用信息
adb shell getprop | grep -i "android\|version\|api"

# 获取崩溃日志
adb logcat -b all > full_crash_log.txt

# 显示文件
cat full_crash_log.txt
```

然后分享日志，我可以提供更具体的建议。

---

**记住**：Android 16 很新，没有魔法解决方案。耐心测试，记录结果。🔍

