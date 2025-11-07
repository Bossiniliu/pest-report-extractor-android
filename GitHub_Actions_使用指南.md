# 🚀 GitHub Actions 自动构建 APK 使用指南

## 📖 简介

已为您配置好 GitHub Actions 自动构建系统，可以在云端自动构建 Android APK，无需本地等待！

---

## 🎯 使用步骤

### 步骤 1：初始化 Git 仓库（如果还没有）

```bash
cd "/Users/bossiniliu/Documents/Coding/Claude Code/Pest Report Extrator"

# 初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: 虫害报告提取器 Android 版本"
```

### 步骤 2：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名称：`pest-report-extractor-android`
3. 选择 **Public**（公开仓库可免费使用 Actions）
4. 点击 "Create repository"

### 步骤 3：推送代码到 GitHub

```bash
# 添加远程仓库（替换为您的用户名）
git remote add origin https://github.com/您的用户名/pest-report-extractor-android.git

# 推送代码
git branch -M main
git push -u origin main
```

### 步骤 4：触发构建

**自动触发：**
- 推送代码后，GitHub Actions 会自动开始构建

**手动触发：**
1. 进入 GitHub 仓库页面
2. 点击 **Actions** 选项卡
3. 选择 "Build Android APK" 工作流
4. 点击 **Run workflow** → **Run workflow**

### 步骤 5：下载 APK

构建完成后（约 30-60 分钟）：

1. 进入 GitHub 仓库
2. 点击 **Actions** 选项卡
3. 点击最新的工作流运行
4. 滚动到底部 **Artifacts** 部分
5. 下载 `pestreportextractor-apk`

---

## 📊 构建时间

- **首次构建**：约 40-60 分钟
- **后续构建**：约 20-30 分钟（有缓存）

---

## 🔍 查看构建进度

1. 访问 `https://github.com/您的用户名/pest-report-extractor-android/actions`
2. 点击正在运行的工作流
3. 实时查看构建日志

---

## ✅ 优势

| 特性 | 本地 Docker | GitHub Actions |
|------|------------|----------------|
| 构建时间 | 1-2 小时 | 30-60 分钟 |
| 网络要求 | 高（下载 1-2GB） | 无 |
| 占用本地资源 | 是 | 否 |
| 自动化 | 否 | 是 |
| 稳定性 | 可能失败 | ⭐⭐⭐⭐⭐ |
| 成本 | 免费 | 免费 |

---

## 🛠️ 高级用法

### 创建 Release 版本

```bash
# 打标签
git tag -a v2.0 -m "虫害报告提取器 Android v2.0"

# 推送标签
git push origin v2.0
```

推送标签后，GitHub Actions 会自动：
1. 构建 APK
2. 创建 GitHub Release
3. 自动附加 APK 文件

---

## 📝 所需文件清单

已为您准备好所有必要文件：

- ✅ `android_main.py` - Android 主程序
- ✅ `buildozer.spec` - 构建配置
- ✅ `.github/workflows/build-apk.yml` - GitHub Actions 配置
- ✅ `README.md` - 项目说明
- ✅ `功能完整性确认.md` - 功能验证

---

## 🔧 故障排除

### Q: 构建失败了怎么办？

**A:** 
1. 进入 Actions 页面查看错误日志
2. 如果是依赖问题，检查 `buildozer.spec`
3. 如果是代码问题，修改 `android_main.py`
4. 重新推送代码，自动重新构建

### Q: 如何修改应用配置？

**A:** 编辑 `buildozer.spec` 文件：
- 修改应用名称：`title =`
- 修改版本号：`version =`
- 修改包名：`package.name =`
- 修改权限：`android.permissions =`

提交并推送后自动重新构建。

### Q: 私有仓库可以用吗？

**A:** 可以，但 GitHub Actions 分钟数有限制：
- 公开仓库：无限制
- 私有仓库：每月 2000 分钟（免费账户）

---

## 📱 安装 APK

1. 从 GitHub Actions 下载 APK
2. 通过 USB、云盘或邮件传到手机
3. 在手机上允许安装未知来源应用
4. 安装 APK
5. 授予存储权限
6. 开始使用！

---

## 🎉 完成！

现在您有了一个全自动的 APK 构建系统：
- ✅ 无需本地构建
- ✅ 稳定可靠
- ✅ 自动化
- ✅ 免费

每次修改代码并推送，GitHub 都会自动为您构建新的 APK！

---

**如有问题，请查看 GitHub Actions 日志或参考 `Android打包说明.md`**
