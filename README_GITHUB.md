# 🐛 虫害报告提取器 - Android 版

[![Build APK](https://github.com/您的用户名/pest-report-extractor-android/actions/workflows/build-apk.yml/badge.svg)](https://github.com/您的用户名/pest-report-extractor-android/actions/workflows/build-apk.yml)

一个用于从虫害报告 PDF 自动提取数据并生成 Excel 分析报告的 Android 应用。

## ✨ 功能特点

- 📱 **移动端设计** - 简洁直观的手机界面
- 📄 **PDF 自动提取** - 智能识别虫害报告数据
- 📊 **Excel 报告生成** - 包含原始数据和分析报告
- 📈 **数据分析** - 虫害类型统计、建筑物分布、高危区域 TOP 10
- 💾 **本地存储** - 文件保存到手机 Documents 目录
- 🔒 **隐私保护** - 所有数据在本地处理

## 📱 应用界面

- 🐛 标题栏 - "虫害报告提取器 v2.0"
- 📁 选择按钮 - 浏览并选择 PDF 文件
- 🚀 处理按钮 - 开始提取和生成
- 📊 进度条 - 实时显示处理进度
- 📝 状态区 - 显示详细的操作信息

## 📊 生成的报告

生成的 Excel 文件包含两个工作表：

### 工作表 1：虫害分析
- 📈 数据概览（总记录数、虫害总数、平均密度、最大单点）
- 🦟 虫害类型统计（含占比）
- 🏢 建筑物统计（含占比）
- ⚠️ 高危区域 TOP 10（前三名高亮）

### 工作表 2：虫害情况
- 完整的原始数据表
- 包含建筑物、楼层、部门、监测点位、虫害类型、数量

## 🚀 快速开始

### 下载 APK

1. 进入 [Releases](https://github.com/您的用户名/pest-report-extractor-android/releases) 页面
2. 下载最新版本的 APK 文件
3. 传输到 Android 手机
4. 安装并授予存储权限

### 使用方法

1. 打开应用
2. 点击"选择 PDF 文件"
3. 选择虫害报告 PDF
4. 点击"开始处理"
5. 等待处理完成
6. 在 `Documents/虫害报告/` 查看生成的 Excel 文件

## 📋 系统要求

- **Android 版本**：5.0 (API 21) 及以上
- **存储空间**：至少 50 MB
- **权限**：读写外部存储

## 🔨 技术栈

- **Python 3.8+**
- **Kivy** - 跨平台 UI 框架
- **pdfplumber** - PDF 文本提取
- **openpyxl** - Excel 文件生成
- **pandas** - 数据分析
- **Buildozer** - Android 打包工具

## 📦 自动构建

本项目使用 GitHub Actions 自动构建 APK：

- ✅ 推送代码后自动构建
- ✅ 构建产物自动上传
- ✅ Release 自动发布

查看 [构建状态](https://github.com/您的用户名/pest-report-extractor-android/actions)

## 📝 开发

### 本地开发

```bash
# 克隆仓库
git clone https://github.com/您的用户名/pest-report-extractor-android.git
cd pest-report-extractor-android

# 安装依赖（桌面版测试）
pip install pdfplumber openpyxl pandas kivy

# 运行应用（桌面版）
python android_main.py
```

### 构建 APK

```bash
# 使用 Buildozer
cp android_main.py main.py
buildozer android debug
```

或者推送到 GitHub，让 Actions 自动构建。

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

如有问题，请查看：
- [使用指南](GitHub_Actions_使用指南.md)
- [打包说明](Android打包说明.md)
- [功能确认](功能完整性确认.md)

---

**版本：** 2.0  
**更新日期：** 2025-01-07
