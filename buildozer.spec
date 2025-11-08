[app]

# 应用名称
title = 虫害报告提取器

# 包名
package.name = pestreportextractor
package.domain = com.pestcontrol

# 主程序入口 - Flask Web 版本
source.dir = .
source.include_exts = py,png,jpg,html,css,js

# 版本号
version = 3.0

# 应用依赖 - Flask Web 版本（最小化）
requirements = python3,flask

# Bootstrap - 使用 sdl2 bootstrap 运行 Web 服务器
p4a.bootstrap = sdl2

# 图标和启动画面
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Android 配置
orientation = portrait
fullscreen = 0

# Android 权限 - 网络权限
android.permissions = INTERNET

# ===== Android 16 Web 版本配置 =====
# API 版本配置 - 编译 API 34
android.api = 34
# 最低支持 Android 7.0（API 24）
android.minapi = 24
# 目标 Android 13（API 33）
android.targetSdkVersion = 33

# 使用稳定的 NDK
android.ndk = 25b

# 仅编译 ARM64（Samsung S25 Ultra）
android.archs = arm64-v8a

# 接受许可证
android.accept_sdk_license = True

# Android 入口点 - 自定义 MainActivity（包装 PythonActivity）
android.entrypoint = com.pestcontrol.pestreportextractor.MainActivity

# 使用 Apache HTTP 库支持
android.uses_library = org.apache.http.legacy

# 跳过更新（加速构建）
android.skip_update = False

# 日志配置
log_level = 2
warn_on_root = 1

[buildozer]

# 日志级别
log_level = 2
warn_on_root = 1
