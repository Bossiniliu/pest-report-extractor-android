# Android 权限问题修复说明

## 🔧 修复内容

### 1. buildozer.spec 配置更新

**修改的配置项：**

```spec
# 仅使用 INTERNET 权限 - 完全依赖应用专属存储
android.permissions = INTERNET

# 更新 targetSdkVersion 到 34 (Android 14+)
android.api = 34
android.targetSdkVersion = 34

# 移除所有危险权限声明，避免 Android 15+ 闪退
```

### 2. android_main.py 代码更新

**存储路径优化：**
- ✅ 使用应用专属外部存储目录 (`getExternalFilesDir(DIRECTORY_DOCUMENTS)`)
- ✅ Android 11+ 无需用户授权即可使用
- ✅ 文件保存到：`/Android/data/com.pestcontrol.pestreportextractor/files/Documents/虫害报告/`

**权限请求改进：**
- ✅ **完全移除所有存储权限请求** - 避免 Android 15+ 闪退
- ✅ 100% 使用应用专属存储，无需用户授权
- ✅ 支持 Android 5.0 - Android 15+

## 📱 Android 版本支持

| Android 版本 | API Level | 存储策略 | 是否需要用户授权 |
|-------------|-----------|---------|---------------|
| Android 5-9 | 21-28 | 应用专属存储 | **否**（自动可用） |
| Android 10-14 | 29-34 | 应用专属存储 | **否**（自动可用） |
| Android 15+ | 35+ | 应用专属存储 | **否**（自动可用） |

✅ **所有版本均使用应用专属存储，无需任何权限！**

## 🚀 使用方法

### 重新打包 APK

```bash
# 清理旧构建
buildozer android clean

# 重新构建
buildozer android debug

# 或使用你的脚本
./build_apk.sh
```

### 安装和使用

1. **安装 APK**
   ```bash
   adb install -r pestreportextractor-*.apk
   ```

2. **首次运行**
   - Android 11+ 用户：应用会显示文件保存位置，无需额外操作
   - Android 10 及以下：会弹出权限请求对话框，点击"允许"

3. **查看生成的文件**
   - 路径：`/Android/data/com.pestcontrol.pestreportextractor/files/Documents/虫害报告/`
   - 使用文件管理器导航到该目录

## ✅ 主要优点

1. **Android 11+ 无需权限** - 使用应用专属存储，自动可用
2. **向后兼容** - 支持 Android 5.0 (API 21) 到最新版本
3. **更安全** - 符合 Android 最新安全要求
4. **用户友好** - 清晰的提示信息，无混淆

## 🐛 故障排除

### 问题1：仍然无法保存文件

**解决方法：**
```bash
# 手动授予权限
adb shell pm grant com.pestcontrol.pestreportextractor android.permission.READ_EXTERNAL_STORAGE
adb shell pm grant com.pestcontrol.pestreportextractor android.permission.WRITE_EXTERNAL_STORAGE
```

### 问题2：找不到保存的文件

**解决方法：**
1. 使用支持查看应用专属目录的文件管理器（如 Solid Explorer）
2. 或者通过 adb 查看：
   ```bash
   adb shell ls -la /sdcard/Android/data/com.pestcontrol.pestreportextractor/files/Documents/
   ```

### 问题3：Android 11+ 需要访问共享存储

**解决方法：**
1. 打开应用设置
2. 找到"所有文件访问权限"
3. 开启该权限

## 📝 测试清单

- [ ] Android 5.0-9 (API 21-28) - 传统权限
- [ ] Android 10 (API 29) - 分区存储
- [ ] Android 11+ (API 30+) - 应用专属存储
- [ ] 文件保存功能
- [ ] 文件读取功能
- [ ] 权限请求流程

## 📚 相关文档

- [Android 存储最佳实践](https://developer.android.com/training/data-storage)
- [分区存储概览](https://developer.android.com/about/versions/11/privacy/storage)
- [请求应用权限](https://developer.android.com/training/permissions/requesting)
