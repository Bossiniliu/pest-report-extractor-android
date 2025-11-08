[app]

# 应用名称
title = 虫害报告提取器

# 包名
package.name = pestreportextractor
package.domain = com.pestcontrol

# BeeWare/Briefcase 项目配置
formal_name = 虫害报告提取器
description = 自动提取虫害情况的应用
source.dir = src

# 版本号
version = 3.0

# 应用依赖 - 仅使用 Toga（BeeWare 官方 UI 框架）
requirements = python3,toga

# 图标和启动画面
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Android 配置
orientation = portrait
fullscreen = 0

# Android 权限 - 仅网络权限
android.permissions = INTERNET

# ===== 针对 Android 16 的 BeeWare 配置 =====
# API 版本配置 - 编译 API 34，最小化兼容性问题
android.api = 34
# 最低支持 Android 7.0（API 24）
android.minapi = 24
# 目标 Android 12（API 31）- 启用兼容性模式
android.targetSdkVersion = 31

# 使用稳定的 NDK
android.ndk = 25b

# 仅编译 ARM64（Samsung S25 Ultra）
android.archs = arm64-v8a

# 接受许可证
android.accept_sdk_license = True

# Android 入口点 - Toga 使用
android.entrypoint = org.beeware.android.MainActivity

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

# BeeWare/Toga 配置
# Toga 是 BeeWare 的官方 UI 框架，相比 Kivy 更好地支持 Android 16
requirements = toga,toga-android

# 编译选项
android.gradle_dependencies = org.beeware.androidx:androidx-appcompat:1.6.1

# 权限列表
android.permissions = INTERNET

# Gradle 编译配置
android.gradle_options = org.gradle.jvmargs=-Xmx4096m
