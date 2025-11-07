[app]

# 应用名称（显示在手机上的名称）
title = 虫害报告提取器

# 包名（唯一标识符）
package.name = pestreportextractor

# 包域名
package.domain = com.pestcontrol

# 主程序入口
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 版本号
version = 2.0

# 应用依赖
requirements = python3,kivy,pdfplumber,openpyxl,pandas,pillow,pycryptodome,charset-normalizer

# 图标和启动画面（可选，如果没有会使用默认）
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Android 配置
orientation = portrait
fullscreen = 0

# Android 权限
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# Android API 版本
android.api = 33
android.minapi = 21
android.ndk = 25b

# Android 架构
android.archs = arm64-v8a,armeabi-v7a

# 接受 Android SDK 许可证
android.accept_sdk_license = True

# Android 入口点
android.entrypoint = org.kivy.android.PythonActivity

# 跳过更新（加速构建）
android.skip_update = False

# Android ANT 路径
# android.ant_path = 

# 添加 Java 代码或库（如果需要）
# android.add_src = 

# 添加 Android AAR 库
# android.gradle_dependencies = 

# Android AAB 格式（Google Play 需要）
# android.release_artifact = aab
android.release_artifact = apk

# 日志级别
log_level = 2

# 警告
warn_on_root = 1

[buildozer]

# 日志级别（0 = 最少，2 = 最多）
log_level = 2

# 警告退出
warn_on_root = 1
