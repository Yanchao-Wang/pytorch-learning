#!/bin/bash

# 启动 Jupyter Notebook 的便捷脚本

echo "🚀 启动 Jupyter Notebook..."
echo ""
echo "📚 可用的教程和示例："
echo "  - /workspace/notebooks/            - 你的 Jupyter notebooks"
echo "  - /workspace/tutorials/d2l-zh/     - D2L 中文教程"
echo "  - /workspace/test_pytorch.ipynb    - PyTorch 基础示例"
echo ""
echo "🌐 Jupyter 将在以下地址启动："
echo "  - http://localhost:8888"
echo ""

# 检查 d2l 教程是否存在
if [ -d "/workspace/tutorials/d2l-zh" ]; then
    echo "✅ D2L 教程已就绪"
else
    echo "⚠️ D2L 教程未找到，正在下载..."
    mkdir -p /workspace/tutorials
    cd /workspace/tutorials
    wget https://zh-v2.d2l.ai/d2l-zh.zip
    unzip d2l-zh.zip
    rm d2l-zh.zip
    echo "✅ D2L 教程下载完成"
fi

echo ""
echo "启动 Jupyter Notebook..."

# 启动 Jupyter，允许外部访问
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root \
    --notebook-dir=/workspace \
    --ServerApp.token='' \
    --ServerApp.password='' \
    --ServerApp.allow_origin='*'
