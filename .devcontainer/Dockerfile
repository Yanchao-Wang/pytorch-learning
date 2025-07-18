# 基于轻量级 Python 镜像，手动安装 PyTorch CPU 版本
FROM python:3.11-slim

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 设置工作目录
WORKDIR /workspace

# 安装系统依赖 (需要root权限)
RUN apt-get update && apt-get install -y \
    git \
    vim \
    curl \
    wget \
    build-essential \
    htop \
    tree \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 安装 PyTorch CPU 版本和其他常用包
RUN pip install --upgrade pip setuptools wheel && \
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install pandas matplotlib jupyterlab scikit-learn tensorboard torchsummary d2l

# 创建常用目录结构
RUN mkdir -p /workspace/{data,models,notebooks,scripts,runs,tutorials}

# 下载和安装 d2l 中文教程（使用WORKDIR确保目录存在）
WORKDIR /workspace/tutorials
RUN wget https://zh-v2.d2l.ai/d2l-zh.zip && \
    unzip d2l-zh.zip && \
    rm d2l-zh.zip && \
    echo "D2L 教程已下载到 /workspace/tutorials/d2l-zh"

# 重新设置回工作目录
WORKDIR /workspace

# 创建默认用户并设置权限
RUN useradd -m vscode && \
    chown -R vscode:vscode /workspace

# 切换到普通用户
USER vscode

# 设置默认命令
CMD ["bash"]


