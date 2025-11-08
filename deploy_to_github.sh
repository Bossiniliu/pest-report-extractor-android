#!/bin/bash
# 快速部署到 GitHub 并触发自动构建

set -e

echo "🚀 虫害报告提取器 - GitHub 部署脚本"
echo "===================================="
echo ""

# 检查是否已初始化 Git
if [ ! -d ".git" ]; then
    echo "📝 初始化 Git 仓库..."
    git init
    echo "✅ Git 仓库已初始化"
else
    echo "✅ Git 仓库已存在"
fi

echo ""
echo "📋 添加文件到 Git..."

# 添加所有必要文件
git add android_main.py
git add buildozer.spec
git add .github/
git add .gitignore
git add README_GITHUB.md
git add GitHub_Actions_使用指南.md
git add Android打包说明.md
git add 功能完整性确认.md
git add 快速打包指南.md

echo "✅ 文件已添加"

echo ""
echo "💾 提交更改..."
git commit -m "feat: 虫害报告提取器 Android 版本 v2.0

- 添加 Kivy 移动端界面
- 支持 PDF 自动提取
- 生成完整的 Excel 分析报告
- 配置 GitHub Actions 自动构建
- 包含虫害类型统计和高危区域分析" || echo "没有新的更改需要提交"

echo ""
echo "📝 下一步操作："
echo ""
echo "1. 创建 GitHub 仓库："
echo "   访问: https://github.com/new"
echo "   仓库名: pest-report-extractor-android"
echo "   类型: Public (公开，免费使用 Actions)"
echo ""
echo "2. 添加远程仓库（替换为您的用户名）："
echo "   git remote add origin https://github.com/您的用户名/pest-report-extractor-android.git"
echo ""
echo "3. 推送代码："
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. 查看构建进度："
echo "   https://github.com/您的用户名/pest-report-extractor-android/actions"
echo ""
echo "===================================="
echo "准备完成！按照上述步骤操作即可开始自动构建 APK"
echo ""
