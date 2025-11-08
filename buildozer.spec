[app]

# 应用名称
title = 虫害报告提取器

# 包名
package.name = pestreportextractor
package.domain = com.pestcontrol

# 主程序入口
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# ===== Android 14 (API 34) 回退配置 =====
# 这个配置针对 Android 14，尽管设备是 Android 16
# 这样做的目的是告诉 Android 16：
# "我只需要 Android 14 的功能"
# 可以绕过 Android 16 的某些新限制
#
# 版本号
version = 2.2

# 应用依赖 - 最小化配置
# 不指定版本号，让 buildozer 自动选择兼容的版本
requirements = python3,\
               kivy

# 图标和启动画面
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Android 配置
orientation = portrait
fullscreen = 0

# Android 权限 - 仅网络权限
android.permissions = INTERNET

# ===== 关键：降级到 Android 14 标准 =====
# API 版本配置 - 针对 Android 14（编译 API 34）
android.api = 34
# 最低支持 Android 5.0
android.minapi = 21
# 目标 Android 13
android.targetSdkVersion = 33

# 使用稳定的 NDK
android.ndk = 25b

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
