"""
Tests for the main module.
主模块的测试。
"""
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import hello


def test_hello_default():
    """Test hello function with default parameter."""
    result = hello()
    assert result == "Hello, World!"
    assert isinstance(result, str)


def test_hello_with_name():
    """Test hello function with a custom name."""
    result = hello("Alice")
    assert result == "Hello, Alice!"


def test_hello_chinese():
    """Test hello function with Chinese characters."""
    result = hello("开发者")
    assert result == "Hello, 开发者!"


if __name__ == "__main__":
    print("Running tests...")
    test_hello_default()
    print("✓ test_hello_default passed")
    
    test_hello_with_name()
    print("✓ test_hello_with_name passed")
    
    test_hello_chinese()
    print("✓ test_hello_chinese passed")
    
    print("\nAll tests passed!")
