#!/usr/bin/env python3
"""
Example usage of the project.
项目使用示例。
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import hello


def main():
    """Demonstrate various ways to use the hello function."""
    print("=== Example Usage 示例用法 ===\n")
    
    # Example 1: Default usage
    print("1. Default usage 默认用法:")
    print(f"   {hello()}\n")
    
    # Example 2: With a name
    print("2. With a name 使用名字:")
    print(f"   {hello('Alice')}\n")
    
    # Example 3: With Chinese name
    print("3. With Chinese name 使用中文名字:")
    print(f"   {hello('小明')}\n")
    
    # Example 4: Loop through names
    print("4. Multiple greetings 多个问候:")
    names = ["Bob", "Charlie", "张三", "李四"]
    for name in names:
        print(f"   {hello(name)}")


if __name__ == "__main__":
    main()
