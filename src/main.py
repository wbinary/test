#!/usr/bin/env python3
"""
Main application entry point.
这是主应用程序入口点。
"""


def hello(name="World"):
    """
    A simple hello function.
    
    Args:
        name (str): The name to greet. Default is "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Main function to run the application."""
    print(hello())
    print(hello("开发者"))  # Developer in Chinese


if __name__ == "__main__":
    main()
