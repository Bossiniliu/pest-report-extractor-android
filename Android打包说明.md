# 虫害报告提取器 - Android APK 打包说明

## 📱 项目概述

本文档详细介绍如何将虫害报告提取工具打包为 Android APK 文件，适用于安卓手机。

### ✨ 功能特点

- 🎨 **简洁界面** - 专为移动端优化的界面设计
- 📄 **PDF 提取** - 直接从手机上的 PDF 文件提取虫害数据
- 📊 **Excel 生成** - 自动生成带格式的 Excel 报告
- 📈 **数据分析** - 包含虫害类型统计和高危区域分析
- 💾 **本地保存** - 文件保存到手机 Documents/虫害报告 目录

---

## 🛠️ 打包环境要求

### 方式一：使用 Linux 服务器（推荐）

由于 macOS 不支持直接打包 Android APK，建议使用以下环境：

1. **Ubuntu 20.04/22.04** 系统（推荐）
2. **至少 8GB RAM**
3. **至少 20GB 可用磁盘空间**
4. **Python 3.8+**

### 方式二：使用 Docker（macOS 可用）

如果您使用 macOS，可以通过 Docker 容器来打包：

```bash
# 拉取 buildozer 镜像
docker pull kivy/buildozer

# 或者使用官方镜像
docker pull buildozer/buildozer:latest
```

---

## 📦 打包步骤

### 步骤 1：准备环境（Ubuntu）

```bash
# 更新系统
sudo apt update
sudo apt upgrade -y

# 安装基础依赖
sudo apt install -y \
    python3-pip \
    git \
    zip \
    unzip \
    openjdk-11-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev

# 安装 buildozer
pip3 install --upgrade buildozer

# 安装 Cython
pip3 install --upgrade Cython==0.29.33
```

### 步骤 2：上传项目文件

将以下文件上传到 Linux 服务器：

```
pest_report_extractor/
├── android_main.py          # Android 主程序
├── buildozer.spec          # 打包配置文件
└── README.md               # 说明文档（可选）
```

**重要：** 将 `android_main.py` 重命名为 `main.py`：

```bash
mv android_main.py main.py
```

### 步骤 3：修改配置（可选）

编辑 `buildozer.spec` 文件，根据需要修改：

```ini
# 应用名称
title = 虫害报告提取器

# 版本号
version = 2.0

# Android 最低版本（API 21 = Android 5.0）
android.minapi = 21

# Android 目标版本（API 33 = Android 13）
android.api = 33
```

### 步骤 4：开始打包

```bash
# 进入项目目录
cd pest_report_extractor

# 初始化 buildozer（首次运行）
buildozer init

# 开始打包 APK（debug 版本）
buildozer android debug

# 或打包 release 版本（需要签名）
# buildozer android release
```

**注意：** 首次打包需要下载 Android SDK、NDK 等工具，**大约需要 1-2 小时**。

### 步骤 5：查找生成的 APK

打包完成后，APK 文件位于：

```bash
bin/pestreportextractor-2.0-debug.apk
```

---

## 🐳 使用 Docker 打包（macOS 适用）

如果您使用 macOS，可以用 Docker 来打包：

```bash
# 1. 进入项目目录
cd "/Users/bossiniliu/Documents/Coding/Claude Code/Pest Report Extrator"

# 2. 重命名主程序
cp android_main.py main.py

# 3. 启动 Docker 容器并打包
docker run --rm -v "$PWD":/home/user/hostcwd kivy/buildozer android debug

# 4. 查找生成的 APK
ls -lh bin/
```

---

## 📱 安装到手机

### 方法 1：USB 传输

1. 将 APK 文件通过 USB 传输到手机
2. 在手机上找到 APK 文件
3. 点击安装（需要开启"允许安装未知来源应用"）

### 方法 2：ADB 安装

```bash
# 安装 ADB 工具
# macOS
brew install android-platform-tools

# 通过 ADB 安装
adb install bin/pestreportextractor-2.0-debug.apk
```

---

## 🎯 使用说明

### 应用权限

首次运行时，应用会请求以下权限：
- ✅ **读取存储** - 选择 PDF 文件
- ✅ **写入存储** - 保存 Excel 报告

### 使用流程

1. **打开应用** - 启动"虫害报告提取器"
2. **选择文件** - 点击"选择 PDF 文件"按钮
3. **浏览文件** - 在文件管理器中找到虫害报告 PDF
4. **开始处理** - 点击"开始处理"按钮
5. **等待完成** - 进度条显示处理进度
6. **查看结果** - 处理完成后查看保存位置

### 输出位置

生成的 Excel 文件保存在：
```
/storage/emulated/0/Documents/虫害报告/
虫害情况报告_YYYYMMDD_HHMMSS.xlsx
```

可以通过手机的"文件管理器" → "Documents" → "虫害报告"找到。

---

## ⚠️ 常见问题

### Q1: 打包失败，提示 "Command failed"

**解决方法：**
```bash
# 清理构建缓存
buildozer android clean

# 重新打包
buildozer android debug
```

### Q2: 打包时内存不足

**解决方法：**
- 增加服务器内存到至少 8GB
- 或在 `buildozer.spec` 中添加：
```ini
android.gradle_dependencies = 
```

### Q3: APK 安装后闪退

**可能原因：**
1. 缺少依赖库 - 检查 `buildozer.spec` 中的 requirements
2. 权限未授予 - 确保授予存储权限
3. Android 版本过低 - 最低需要 Android 5.0

**调试方法：**
```bash
# 连接手机查看日志
adb logcat | grep python
```

### Q4: 无法读取或保存文件

**解决方法：**
1. 在手机设置中手动授予存储权限
2. 对于 Android 11+，可能需要额外的文件访问权限

### Q5: macOS 无法打包 APK

**解决方法：**
使用 Docker 方式打包（见上文"使用 Docker 打包"部分）

---

## 🔧 高级配置

### 自定义应用图标

1. 准备一个 512x512 的 PNG 图标文件
2. 保存为 `icon.png`
3. 在 `buildozer.spec` 中取消注释：
```ini
icon.filename = %(source.dir)s/icon.png
```

### 自定义启动画面

1. 准备一个启动画面图片（推荐 1920x1080）
2. 保存为 `presplash.png`
3. 在 `buildozer.spec` 中取消注释：
```ini
presplash.filename = %(source.dir)s/presplash.png
```

### 签名 APK（发布版本）

```bash
# 1. 生成签名密钥
keytool -genkey -v -keystore my-release-key.keystore \
    -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# 2. 打包签名版本
buildozer android release

# 3. 签名 APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
    -keystore my-release-key.keystore \
    bin/pestreportextractor-2.0-release-unsigned.apk \
    my-key-alias

# 4. 对齐 APK
zipalign -v 4 \
    bin/pestreportextractor-2.0-release-unsigned.apk \
    bin/pestreportextractor-2.0-release.apk
```

---

## 📊 应用信息

| 项目 | 说明 |
|------|------|
| **应用名称** | 虫害报告提取器 |
| **包名** | com.pestcontrol.pestreportextractor |
| **版本** | 2.0 |
| **最低 Android 版本** | 5.0 (API 21) |
| **目标 Android 版本** | 13 (API 33) |
| **支持架构** | ARM64, ARMv7 |
| **APK 大小** | 约 40-60 MB |

---

## 📞 技术支持

### 文件结构

```
项目目录/
├── main.py                 # Android 主程序（从 android_main.py 重命名）
├── buildozer.spec         # 打包配置文件
├── Android打包说明.md      # 本文档
├── README.md              # 项目说明
└── bin/                   # 打包输出目录（自动生成）
    └── *.apk              # 生成的 APK 文件
```

### 依赖库版本

- Python: 3.8+
- Kivy: 最新版
- pdfplumber: 最新版
- openpyxl: 最新版
- pandas: 最新版

### 推荐开发环境

- **打包环境**: Ubuntu 22.04 LTS
- **测试设备**: Android 10+ 手机
- **开发工具**: VS Code + Python 扩展

---

## 🎉 完成

按照以上步骤，您应该能够成功打包出可在安卓手机上运行的 APK 文件。

**祝使用愉快！** 🐛📱✨
