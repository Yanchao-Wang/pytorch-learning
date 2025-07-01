# PyTorch 开发容器模板

这是一个预配置的 PyTorch 开发环境，使用 VS Code 开发容器和 PyTorch 2.7.1。

## 🚀 快速开始

1. **克隆仓库**
   ```bash
   git clone <你的仓库URL>
   cd tem_pytorch
   ```

2. **在 VS Code 中打开**
   - 确保已安装 Docker Desktop 并运行
   - 安装 "Dev Containers" 扩展
   - 打开项目文件夹
   - 点击左下角的绿色按钮，选择 "Reopen in Container"

3. **测试环境**
   ```bash
   python test_pytorch.py
   ```

## � PyTorch 环境特性

- **PyTorch 2.7.1** - 最新版本的PyTorch
- **CPU优化** - 适合学习和开发，无需GPU
- **Jupyter支持** - 内置Jupyter Notebook支持
- **TensorBoard** - 可视化训练过程
- **完整工具链** - 包含所有PyTorch开发必需工具

## �📦 包含的工具和库

### 核心框架
- PyTorch 2.7.1
- torchvision
- torchaudio

### 开发工具
- Jupyter Notebook/Lab
- TensorBoard
- torchsummary (模型概览)

### 数据科学
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- pillow

## 🔧 自定义环境

- 修改 `.devcontainer/devcontainer.json` 来调整容器配置
- 修改 `requirements.txt` 来添加或移除 Python 包
- 修改 `.devcontainer/Dockerfile` 来更改PyTorch版本

## 📁 项目结构

```
.
├── .devcontainer/          # 开发容器配置
│   ├── devcontainer.json  # VS Code容器配置
│   └── Dockerfile         # Docker镜像定义
├── test_pytorch.py        # PyTorch环境测试脚本
├── requirements.txt       # Python依赖
└── README.md             # 项目说明
```

## 🎯 开发建议

1. **学习PyTorch**：从 `test_pytorch.py` 开始，了解基础操作
2. **创建模型**：在项目根目录创建你的训练脚本
3. **数据处理**：使用 `data/` 文件夹存放数据集
4. **模型保存**：使用 `models/` 文件夹保存训练好的模型
5. **实验记录**：使用TensorBoard记录训练过程

## 🚀 常用端口

- **8888**: Jupyter Notebook
- **6006**: TensorBoard

启动后可通过以下方式访问：
```bash
# 启动 Jupyter
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# 启动 TensorBoard  
tensorboard --logdir=./runs --host=0.0.0.0 --port=6006
```

---

� Happy PyTorch Coding!
