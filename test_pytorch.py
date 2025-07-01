#!/usr/bin/env python3
"""
PyTorch CPU-only 测试脚本
"""

import torch
import torch.nn as nn
import numpy as np

def test_pytorch_installation():
    """测试PyTorch安装是否成功"""
    print("🔥 PyTorch 版本:", torch.__version__)
    print("💻 设备类型:", "CUDA" if torch.cuda.is_available() else "CPU")
    print("🎯 CPU核心数:", torch.get_num_threads())
    
    # 测试张量操作
    x = torch.rand(5, 3)
    y = torch.rand(5, 3)
    z = x + y
    
    print("\n📊 张量运算测试:")
    print("x shape:", x.shape)
    print("y shape:", y.shape) 
    print("z = x + y shape:", z.shape)
    print("z 前3行:")
    print(z[:3])

def test_simple_neural_network():
    """测试简单神经网络"""
    print("\n🧠 测试简单神经网络:")
    
    # 创建简单的线性网络
    model = nn.Sequential(
        nn.Linear(10, 5),
        nn.ReLU(),
        nn.Linear(5, 1)
    )
    
    # 生成随机输入
    x = torch.randn(32, 10)  # batch_size=32, features=10
    
    # 前向传播
    output = model(x)
    
    print(f"输入形状: {x.shape}")
    print(f"输出形状: {output.shape}")
    print(f"模型参数数量: {sum(p.numel() for p in model.parameters())}")

def test_autograd():
    """测试自动微分"""
    print("\n⚡ 测试自动微分:")
    
    x = torch.tensor([2.0], requires_grad=True)
    y = x ** 2 + 3 * x + 1
    
    # 反向传播
    y.backward()
    
    print(f"x = {x.item()}")
    print(f"y = x² + 3x + 1 = {y.item()}")
    print(f"dy/dx = 2x + 3 = {x.grad.item()}")

if __name__ == "__main__":
    print("🐍 开始 PyTorch CPU-only 测试...")
    print("=" * 50)
    
    try:
        test_pytorch_installation()
        test_simple_neural_network()
        test_autograd()
        
        print("\n" + "=" * 50)
        print("✅ 所有测试通过！PyTorch CPU版本运行正常！")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
