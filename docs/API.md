# API Documentation

## API 文档

### Functions 函数

#### `hello(name="World")`

A simple greeting function that returns a hello message.

一个简单的问候函数，返回问候消息。

**Parameters 参数:**
- `name` (str, optional): The name to greet. Default is "World".  
  要问候的名字。默认为 "World"。

**Returns 返回值:**
- `str`: A greeting message in the format "Hello, {name}!"  
  格式为 "Hello, {name}!" 的问候消息。

**Example 示例:**
```python
from src.main import hello

# Basic usage
message = hello()
print(message)  # Output: Hello, World!

# With a name
message = hello("Alice")
print(message)  # Output: Hello, Alice!

# With Chinese characters
message = hello("开发者")
print(message)  # Output: Hello, 开发者!
```

#### `main()`

Main function to run the application.

运行应用程序的主函数。

**Parameters 参数:**
- None 无

**Returns 返回值:**
- None 无

**Description 描述:**

This function demonstrates the usage of the hello function by printing greetings.

此函数通过打印问候语来演示 hello 函数的用法。
