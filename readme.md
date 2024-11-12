# 小学数学练习题生成器

## 项目简介

这是一个用于生成小学数学练习题的工具，支持生成口算和竖式计算练习题。通过简单的界面配置，用户可以轻松生成适合自己需求的练习题，并可以直接打印出来供学生使用。

## 功能

- **口算练习题**：生成加法、减法、乘法和除法的口算题目。
- **竖式计算练习题**：生成加法、减法、乘法和除法的竖式计算题目。
- **自定义配置**：用户可以自定义题目数量、数值范围、得数限制等参数。
- **布局调整**：用户可以调整题目之间的间距、行距和每行的题目数量。

## 安装

### 环境要求

- Python 3.7 或更高版本
- Streamlit 1.24.1
- Pandas > 2.0
- Numpy <= 1.25.1

### 安装步骤

1. 克隆项目仓库：
   ```bash
   git clone https://github.com/gc313/kousuan.git
   cd kousuan
   ```
2. 安装依赖包：
  ```bash
  pip install -r requirements.txt
  ```
3. 运行项目：
  ```bash
  streamlit run main.py
  ```