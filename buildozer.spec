[app]

# 应用名称
title = 虫害报告提取器

# 包名
package.name = pestreportextractor
package.domain = com.pestcontrol

# 主程序入口
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# ===== Android 16 优化配置 =====
# 版本号
version = 2.2

# 应用依赖 - 使用最新版本针对 Android 16
# 注意：这些是最新可用的版本，应该提供最好的 Android 16 支持
requirements = python3==3.11,\
               kivy==2.3.0,\
               pyjnius==1.5.0,\
               pdfplumber==0.10.0,\
               openpyxl==3.11.0,\
               pandas==2.1.0,\
               pillow==10.0.0,\
               pycryptodome==3.18.0

# 图标和启动画面
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Android 配置
orientation = portrait
fullscreen = 0

# Android 权限 - 仅网络权限
android.permissions = INTERNET

# ===== Android 16 特定配置 =====
# API 版本配置（编译 API 36 - Android 16）
android.api = 36
# 最低支持 Android 11
android.minapi = 30
# 目标保持在 34 以兼容性为主
android.targetSdkVersion = 34

# 使用最新的 NDK
android.ndk = 26b

# 仅编译 ARM64（S25 Ultra）
android.archs = arm64-v8a

# 接受许可证
android.accept_sdk_license = True

# Android 入口点
android.entrypoint = org.kivy.android.PythonActivity

# 使用 Apache HTTP 库支持
android.uses_library = org.apache.http.legacy

# 跳过更新（加速构建）
android.skip_update = False

# 日志配置 - 启用详细日志以便诊断
log_level = 2
warn_on_root = 1

[buildozer]

# 日志级别
log_level = 2
warn_on_root = 1
