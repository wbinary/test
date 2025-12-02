# Getting Started 快速开始

## Prerequisites 先决条件

- Python 3.6 or higher (Python 3.6 或更高版本)
- Git

## Installation 安装

1. **Clone the repository 克隆仓库**

   ```bash
   git clone https://github.com/wbinary/test.git
   cd test
   ```

2. **Run the main application 运行主应用程序**

   ```bash
   python src/main.py
   ```

3. **Run the examples 运行示例**

   ```bash
   python examples/example_usage.py
   ```

4. **Run the tests 运行测试**

   ```bash
   python tests/test_main.py
   ```

## Project Structure 项目结构

```
test/
├── src/                    # Source code 源代码
│   └── main.py            # Main application 主应用程序
├── tests/                 # Test files 测试文件
│   └── test_main.py       # Unit tests 单元测试
├── docs/                  # Documentation 文档
│   ├── API.md            # API documentation API文档
│   └── GETTING_STARTED.md # This file 本文件
├── examples/              # Example usage 示例用法
│   └── example_usage.py   # Usage examples 使用示例
├── .gitignore            # Git ignore patterns Git忽略模式
├── LICENSE               # MIT License MIT许可证
├── README.md             # Project overview 项目概述
└── CONTRIBUTING.md       # Contribution guidelines 贡献指南
```

## Basic Usage 基本用法

### Using the hello function 使用 hello 函数

```python
from src.main import hello

# Default greeting
print(hello())  # Output: Hello, World!

# Custom greeting
print(hello("Alice"))  # Output: Hello, Alice!

# Chinese greeting
print(hello("小明"))  # Output: Hello, 小明!
```

## Next Steps 下一步

1. Read the [API Documentation](API.md) for detailed function descriptions  
   阅读 [API 文档](API.md) 了解详细的函数描述

2. Check out the [examples](../examples/) for more usage patterns  
   查看 [示例](../examples/) 了解更多使用模式

3. See [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute  
   查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解如何贡献

## Troubleshooting 故障排除

### Import errors 导入错误

If you get import errors, make sure you're running the scripts from the project root directory:

如果遇到导入错误，请确保从项目根目录运行脚本：

```bash
# Run from project root
python src/main.py
python tests/test_main.py
python examples/example_usage.py
```

### Python version 错误

This project requires Python 3.6+. Check your version:

本项目需要 Python 3.6+。检查你的版本：

```bash
python --version
```
