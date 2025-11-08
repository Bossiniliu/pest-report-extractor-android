# Android 15 闪退调试指南

**设备**：三星 S25 Ultra (Android 15, One UI 8)
**问题**：APK 安装成功但立即闪退，无法设置权限
**更新时间**：2025-11-08

---

## 🔴 症状分析

```
安装成功 → 打开应用 → 立即闪退
         ↓
     无法进入 UI
     无法设置权限
     无法获取日志
```

---

## 🔍 第一步：获取 logcat 日志（最关键）

这将告诉我们**具体在哪里崩溃**，是否与 Kivy、Python 还是某个库有关。

### 快速命令

```bash
# 1️⃣ 确保手机连接
adb devices

# 2️⃣ 清空日志
adb logcat -c

# 3️⃣ 卸载旧版本
adb uninstall com.pestcontrol.pestreportextractor

# 4️⃣ 安装 APK
adb install -r pestreportextractor-*.apk

# 5️⃣ 立即打开应用，同时在另一个终端运行：
adb logcat > /tmp/android_crash.log 2>&1 &

# 6️⃣ 在手机上点击应用图标，等待闪退
# 7️⃣ 关闭 logcat 进程
pkill -f "adb logcat"

# 8️⃣ 查看完整日志
cat /tmp/android_crash.log | grep -E "python|kivy|crash|error|exception|fatal|ANR" -i
```

### 详细日志查看

```bash
# 查看完整日志
cat /tmp/android_crash.log

# 仅查看错误相关行
cat /tmp/android_crash.log | grep -E "E/|FATAL|ERROR|Exception"

# 查看 Python/Kivy 相关日志
cat /tmp/android_crash.log | grep -iE "python|kivy|pyjnius"

# 查看应用启动日志
cat /tmp/android_crash.log | grep "com.pestcontrol.pestreportextractor"
```

### 期望看到的日志关键词（根据问题类型）

| 关键词 | 问题 | 解决方案 |
|-------|------|---------|
| `ImportError: pdfplumber` | 库导入失败 | 检查库版本兼容性 |
| `ImportError: kivy` | Kivy 导入失败 | 更新 Kivy 版本 |
| `UnicodeDecodeError` | 编码问题 | 检查中文支持 |
| `Permission denied` | 权限问题 | 调整权限配置 |
| `Segmentation fault` | C 扩展库崩溃 | 重新编译依赖 |
| `ANR` | 应用无响应 | 优化性能 |
| `dlopen failed` | 库加载失败 | 检查架构匹配 |

---

## 🧪 第二步：测试 Kivy 基础功能

使用**超极简版本**验证 Kivy 是否能在 Android 15 上运行。

### 方案 A：使用已有的超极简版本

```bash
# 修改 buildozer.spec 使用最小化程序
cp android_minimal_test.py main.py

# 重新构建
buildozer android clean
buildozer android debug

# 测试 APK
adb install -r bin/*-debug.apk
adb logcat | grep -E "kivy|python|error" -i
```

### 方案 B：GitHub Actions 自动构建最小版本

编辑 `.github/workflows/build-apk.yml`，在 "准备主程序" 步骤改为：

```yaml
- name: 📝 准备主程序
  run: |
    # 使用最小化测试版本
    cp android_minimal_test.py main.py
    echo "✅ 已使用最小化版本"
```

推送代码，让 GitHub Actions 自动构建。

---

## ⚙️ 第三步：修改 buildozer.spec 优化配置

根据 logcat 日志结果，尝试以下优化。

### 问题诊断 → 解决方案

#### 问题：Kivy 库加载失败

```ini
[app]
# 尝试使用更稳定的 Kivy 版本
requirements = python3==3.9,kivy==2.1.0,...

[android]
# 降低 API 版本
android.api = 32
android.targetSdkVersion = 32
```

#### 问题：pdfplumber/pandas 编译失败

```ini
requirements = python3==3.9,kivy==2.2.1,\
               pdfplumber==0.8.0,\
               openpyxl==3.0.10,\
               pandas==1.3.5,\
               pillow==9.0.0
```

#### 问题：中文/编码支持

```ini
[app]
# 确保 UTF-8 支持
meta-data = org.kivy.android.meta-data

[android]
# 添加 ICU 库支持
android.gradle_dependencies = androidx.appcompat:appcompat:1.3.1
```

#### 问题：NDK 工具链版本

```ini
[android]
# 尝试更新的 NDK
android.ndk = 26b

# 或降低版本
android.ndk = 25
```

#### 问题：架构兼容性

```ini
[android]
# 仅编译 ARM64（S25 Ultra 是 ARM64 架构）
android.archs = arm64-v8a

# 或尝试降级
# android.archs = armeabi-v7a,arm64-v8a
```

---

## 🔧 第四步：逐步增加功能验证

一旦超极简版本可以运行，逐步添加功能，找出哪个库导致问题。

### 步骤 1：Kivy UI 测试
```python
# 文件：test_kivy_ui.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='✅ Kivy UI 工作'))
        layout.add_widget(Button(text='测试按钮'))
        return layout

if __name__ == '__main__':
    TestApp().run()
```

### 步骤 2：加入 pdfplumber
```python
# 文件：test_with_pdf.py
import pdfplumber  # 测试导入
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='✅ pdfplumber 导入成功')

if __name__ == '__main__':
    TestApp().run()
```

### 步骤 3：加入 pandas
```python
# 文件：test_with_pandas.py
import pandas as pd  # 测试导入
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='✅ pandas 导入成功')

if __name__ == '__main__':
    TestApp().run()
```

### 步骤 4：加入 openpyxl
```python
# 文件：test_with_openpyxl.py
import openpyxl  # 测试导入
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='✅ openpyxl 导入成功')

if __name__ == '__main__':
    TestApp().run()
```

### 步骤 5：加入 jnius/Android API
```python
# 文件：test_with_android.py
from jnius import autoclass  # 测试 Android API
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            return Label(text='✅ Android API 可用')
        except Exception as e:
            return Label(text=f'❌ {e}')

if __name__ == '__main__':
    TestApp().run()
```

---

## 📊 构建测试矩阵

对每个版本在 GitHub Actions 构建并在 S25 Ultra 测试。

| 版本 | 内容 | 预期结果 | 实际结果 |
|-----|------|---------|---------|
| v1 | 超极简 (仅 Label) | ✅ 应该运行 | ? |
| v2 | +Kivy UI | ✅ 应该运行 | ? |
| v3 | +pdfplumber | ? | ? |
| v4 | +pandas | ? | ? |
| v5 | +openpyxl | ? | ? |
| v6 | +jnius | ? | ? |
| v7 | 完整版 | ❌ 当前失败 | ? |

---

## 🚀 快速实施方案

### 方案 1：使用 GitHub Actions + 最小化版本

1. **创建测试分支**
   ```bash
   git checkout -b debug/android15
   ```

2. **使用最小版本**
   ```bash
   cp android_minimal_test.py main.py
   git add main.py
   git commit -m "test: 使用超极简版本测试 Android 15 兼容性"
   git push origin debug/android15
   ```

3. **GitHub Actions 会自动构建**
   - 访问 Actions 页面查看进度
   - 下载 APK 在 S25 Ultra 上测试

4. **获取日志**
   ```bash
   adb logcat -c
   # 在手机上打开应用
   adb logcat | tee test_results.log
   ```

5. **分析日志并修改配置**
   - 根据错误调整 buildozer.spec
   - 推送更新
   - 重复测试

### 方案 2：本地调试 + Docker Buildozer

```bash
# 使用 Docker 构建（更稳定）
docker pull kivy/buildozer:latest

docker run --rm \
  -v "$(pwd):/app" \
  kivy/buildozer:latest \
  bash -c "cd /app && buildozer android clean && buildozer android debug"
```

---

## 📝 调试日志记录模板

每次测试时填写这个表格，帮助追踪问题。

```markdown
### 测试 #1
- **日期**：2025-11-08
- **版本**：android_minimal_test.py
- **buildozer.spec**：原始配置
- **结果**：✅ / ❌
- **logcat 关键行**：
  ```
  [粘贴错误信息]
  ```
- **分析**：
  - 问题：...
  - 下一步：...
```

---

## 💡 替代方案

如果 Kivy 无法解决，考虑以下框架：

### 1. **BeeWare**（推荐）
- 原生 Android 支持
- Python 友好
- 更好的兼容性

```bash
pip install briefcase
briefcase create android
briefcase build android
```

### 2. **Chaquopy**（最稳定）
- 直接在 Android Studio 中使用 Python
- 完整的 Android API 访问
- 生产级别稳定性

### 3. **PyDroid 3**（快速原型）
- 在线 IDE
- 无需构建流程
- 适合快速测试

---

## ✅ 检查清单

完成以下步骤以确保系统地诊断问题：

- [ ] 获取并分析完整的 logcat 日志
- [ ] 使用超极简版本测试基础 Kivy
- [ ] 逐步添加库，找出问题源头
- [ ] 记录每次测试的结果
- [ ] 根据日志修改 buildozer.spec
- [ ] 在 GitHub Actions 和本地都进行测试
- [ ] 如果 Kivy 无法解决，考虑替代框架

---

## 📞 获取帮助

提供以下信息以加速调试：

1. **完整 logcat 日志**（最重要）
2. **buildozer 构建日志**（check `.buildozer/android/platform/build-*/build.log`）
3. **S25 Ultra 手机设置截图**：
   - 开发者选项
   - 应用权限
   - Android 版本
4. **已尝试过的配置和结果**

---

**记住**：日志是最好的朋友。先获取日志，再做任何修改！🔍

