#!/bin/bash
# 虫害报告提取器 - APK 快速打包脚本（macOS Docker 方式）

set -e  # 遇到错误立即退出

echo "🐛 虫害报告提取器 - APK 打包工具"
echo "=================================="
echo ""

# 检查 Docker 是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ 错误: 未检测到 Docker"
    echo "请先安装 Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "✅ 检测到 Docker"

# 检查 Docker 是否运行
if ! docker info &> /dev/null; then
    echo "❌ 错误: Docker 未运行"
    echo "请启动 Docker Desktop 后重试"
    exit 1
fi

echo "✅ Docker 正在运行"
echo ""

# 获取当前目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 检查必要文件
if [ ! -f "android_main.py" ]; then
    echo "❌ 错误: 找不到 android_main.py"
    exit 1
fi

if [ ! -f "buildozer.spec" ]; then
    echo "❌ 错误: 找不到 buildozer.spec"
    exit 1
fi

echo "✅ 文件检查通过"
echo ""

# 创建 main.py（Buildozer 需要）
echo "📝 准备主程序文件..."
cp android_main.py main.py
echo "✅ 已创建 main.py"
echo ""

# 提示用户
echo "⏳ 准备开始打包..."
echo "⚠️  注意："
echo "   - 首次打包需要下载约 1-2GB 的构建工具"
echo "   - 整个过程可能需要 1-2 小时"
echo "   - 请确保网络连接稳定"
echo ""

read -p "是否继续？(y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ 已取消打包"
    rm -f main.py
    exit 0
fi

echo ""
echo "🚀 开始打包..."
echo "=================================="
echo ""

# 拉取最新的 buildozer 镜像
echo "📦 拉取 Buildozer Docker 镜像..."
docker pull kivy/buildozer:latest

echo ""
echo "🔨 开始构建 APK..."
echo "   （这可能需要一段时间，请耐心等待）"
echo ""

# 运行 Docker 容器进行打包（禁用 root 警告）
docker run --rm -e BUILDOZER_WARN_ON_ROOT=0 -v "$SCRIPT_DIR":/home/user/hostcwd kivy/buildozer android debug

# 检查打包结果
if [ -f "bin/pestreportextractor-2.0-debug.apk" ]; then
    echo ""
    echo "=================================="
    echo "✅ 打包成功！"
    echo ""
    echo "📱 APK 文件位置:"
    echo "   $SCRIPT_DIR/bin/pestreportextractor-2.0-debug.apk"
    echo ""
    echo "📊 文件信息:"
    ls -lh bin/pestreportextractor-2.0-debug.apk
    echo ""
    echo "📋 下一步："
    echo "   1. 将 APK 文件传输到 Android 手机"
    echo "   2. 在手机上安装 APK"
    echo "   3. 授予存储权限"
    echo "   4. 开始使用！"
    echo ""
    echo "详细说明请查看: Android打包说明.md"
    echo "=================================="
else
    echo ""
    echo "❌ 打包失败"
    echo "请查看上方错误信息，或参考 Android打包说明.md"
    rm -f main.py
    exit 1
fi

# 清理临时文件
echo ""
echo "🧹 清理临时文件..."
rm -f main.py
echo "✅ 完成"
