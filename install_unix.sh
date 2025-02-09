#!/bin/bash

# 定义变量
BUILD_DIR="build"
EGG_INFO_DIR="pyfolio.egg-info"
BENCHMARKS_DIR=".benchmarks"

# 安装 requirements.txt 中的依赖
pip install -U -r requirements.txt

# 切换到上一级目录
cd ..

# 安装 bt_api_py 包
pip install -U --no-build-isolation ./bt_api_py

# 切换到 bt_api_py 目录
cd ./pyfolio

# 运行 backtrader 的测试用例，使用 4 个进程并行测试
pytest tests -n 4

# 删除中间构建和 egg-info 目录
echo "Deleting intermediate files..."
if [ -d "$BUILD_DIR" ]; then
    rm -rf "$BUILD_DIR"
    echo "Deleted $BUILD_DIR directory."
fi

if [ -d "$EGG_INFO_DIR" ]; then
    rm -rf "$EGG_INFO_DIR"
    echo "Deleted $EGG_INFO_DIR directory."
fi

# 删除 .benchmarks 目录
if [ -d "$BENCHMARKS_DIR" ]; then
    rm -rf "$BENCHMARKS_DIR"
    echo "Deleted $BENCHMARKS_DIR directory."
fi

# 删除所有 .log 文件
echo "Deleting all .log files..."
find . -type f -name "*.log" -exec rm -f {} \;
echo "All .log files deleted."



