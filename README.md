# Python 开发容器模板

这是一个预配置的 Python 开发环境，使用 VS Code 开发容器。

## 🚀 快速开始

1. **克隆仓库**
   ```bash
   git clone <你的仓库URL>
   cd <项目文件夹>
   ```

2. **在 VS Code 中打开**
   - 安装 "Dev Containers" 扩展
   - 打开项目文件夹
   - 点击左下角的绿色按钮，选择 "Reopen in Container"

3. **开始开发**
   ```bash
   python hello_world.py
   ```

## 📦 包含的工具

- Python 3.11+
- pip 包管理器
- 预安装的常用包：
  - matplotlib
  - numpy
  - pandas
  - 等等...

## 🔧 自定义环境

- 修改 `.devcontainer/devcontainer.json` 来调整容器配置
- 修改 `requirements.txt` 来添加或移除 Python 包

## 📁 项目结构

```
.
├── .devcontainer/          # 开发容器配置
├── hello_world.py         # 示例 Python 文件
├── requirements.txt       # Python 依赖
└── README.md             # 项目说明
```

## 🎯 使用建议

1. **新项目**：复制这个模板，修改 `requirements.txt`
2. **团队协作**：团队成员只需要 Docker 和 VS Code
3. **环境一致性**：所有人使用相同的开发环境

---

🐍 Happy Python Coding!
