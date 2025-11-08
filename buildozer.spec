[app]

# 应用名称
title = 虫害报告提取器

# 包名
package.name = pestreportextractor
package.domain = com.pestcontrol

# 主程序入口 - 使用最小化版本
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 指定主 Python 文件
p4a.entrypoint = android_main_minimal:main

# 版本号
version = 3.0

# 应用依赖 - 完全最小化（不使用 Kivy，改用系统原生 WebView）
requirements = python3

# 图标和启动画面
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Android 配置
orientation = portrait
fullscreen = 0

# Android 权限 - 仅网络权限
android.permissions = INTERNET

# ===== Android 16 优化配置 =====
# API 版本配置 - 编译 API 34
android.api = 34
# 最低支持 Android 6.0
android.minapi = 23
# 目标 Android 12 - 启用兼容性模式解决 Android 16 问题
android.targetSdkVersion = 31

# 使用稳定的 NDK
android.ndk = 25b

# 仅编译 ARM64（Samsung S25 Ultra）
android.archs = arm64-v8a

# 接受许可证
android.accept_sdk_license = True

# Android 入口点
android.entrypoint = org.kivy.android.PythonActivity

# 使用 Apache HTTP 库支持
android.uses_library = org.apache.http.legacy

# 禁用 OpenGL multisampling（可能导致线程问题）
android.gl_multisampling = False

# 跳过更新（加速构建）
android.skip_update = False

# 日志配置 - 启用详细日志以便诊断
log_level = 2
warn_on_root = 1

[buildozer]

# 日志级别
log_level = 2
warn_on_root = 1
