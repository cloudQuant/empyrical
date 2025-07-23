# empyrical | 金融风险指标计算库

<p align="center">
    <img src="https://img.shields.io/badge/version-0.6.0-blueviolet.svg" alt="Version 0.6.0" style="margin-right: 10px;"/>
    <img src="https://img.shields.io/badge/platform-mac%7Clinux%7Cwin-yellow.svg" alt="Supported Platforms: Mac, Linux, and Windows" style="margin-right: 10px;"/>
    <img src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg" alt="Python Versions" style="margin-right: 10px;"/>
    <img src="https://img.shields.io/badge/license-Apache%202.0-orange" alt="License: Apache 2.0"/>
</p>

**[English](#english-version) | [中文](#chinese-version)**

---

<a name="english-version"></a>
## English

### Overview

Empyrical is a Python library for calculating common financial risk and performance metrics. Originally developed by Quantopian Inc., it provides a comprehensive toolkit for quantitative finance professionals and researchers to analyze investment returns, calculate risk metrics, and perform performance attribution.

### Features

- **Comprehensive Metrics**: Over 50 financial metrics including returns, risk, risk-adjusted returns, and market relationships
- **Rolling Calculations**: Rolling window versions of most metrics for time-series analysis
- **Flexible Input**: Supports pandas Series/DataFrame and numpy arrays
- **NaN Handling**: Robust handling of missing data throughout all calculations
- **Performance Attribution**: Factor-based performance decomposition
- **Period Flexibility**: Automatic period detection and support for daily, weekly, monthly, quarterly, and yearly data

### Installation

#### From Source (Recommended)

```bash
# For users in China
git clone https://gitee.com/yunjinqi/empyrical

# For international users
git clone https://github.com/cloudQuant/empyrical

cd empyrical

# Windows
install_win.bat

# Linux/macOS
sh install_unix.sh
```

#### pip install 

```bash
pip install -U git+https://github.com/cloudQuant/empyrical.git
```

### Quick Start

#### Basic Metrics

```python
import numpy as np
from empyrical import max_drawdown, sharpe_ratio, alpha_beta

# Sample returns data
returns = np.array([0.01, 0.02, 0.03, -0.4, -0.06, -0.02])
benchmark_returns = np.array([0.02, 0.02, 0.03, -0.35, -0.05, -0.01])

# Calculate max drawdown
mdd = max_drawdown(returns)
print(f"Max Drawdown: {mdd:.2%}")

# Calculate Sharpe ratio (assuming daily returns)
sharpe = sharpe_ratio(returns, risk_free=0.02/252)
print(f"Sharpe Ratio: {sharpe:.2f}")

# Calculate alpha and beta
alpha, beta = alpha_beta(returns, benchmark_returns)
print(f"Alpha: {alpha:.4f}, Beta: {beta:.2f}")
```

#### Rolling Metrics

```python
import pandas as pd
from empyrical import roll_sharpe_ratio, roll_max_drawdown

# Create time series data
dates = pd.date_range('2020-01-01', periods=100, freq='D')
returns = pd.Series(np.random.normal(0.001, 0.02, 100), index=dates)

# Calculate 30-day rolling Sharpe ratio
rolling_sharpe = roll_sharpe_ratio(returns, window=30)

# Calculate 30-day rolling max drawdown
rolling_mdd = roll_max_drawdown(returns, window=30)
```

#### Advanced Usage with DataFrames

```python
import pandas as pd
from empyrical import annual_return, annual_volatility, calmar_ratio

# Multiple strategy returns
strategies = pd.DataFrame({
    'Strategy_A': np.random.normal(0.001, 0.02, 252),
    'Strategy_B': np.random.normal(0.0015, 0.025, 252),
    'Strategy_C': np.random.normal(0.0008, 0.018, 252)
})

# Calculate metrics for all strategies at once
annual_returns = annual_return(strategies)
annual_vols = annual_volatility(strategies)
calmar_ratios = calmar_ratio(strategies)

print("Annual Returns:")
print(annual_returns)
print("\nAnnual Volatilities:")
print(annual_vols)
print("\nCalmar Ratios:")
print(calmar_ratios)
```

### Available Metrics

#### Return Metrics
- `simple_returns()` - Convert prices to returns
- `cum_returns()` - Cumulative returns
- `annual_return()` - Annualized mean return
- `cagr()` - Compound Annual Growth Rate
- `aggregate_returns()` - Aggregate returns to different frequencies

#### Risk Metrics
- `max_drawdown()` - Maximum peak-to-trough drawdown
- `annual_volatility()` - Annualized standard deviation
- `downside_risk()` - Downside deviation
- `value_at_risk()` - Value at Risk (VaR)
- `conditional_value_at_risk()` - Conditional VaR (CVaR/Expected Shortfall)

#### Risk-Adjusted Return Metrics
- `sharpe_ratio()` - Sharpe ratio
- `sortino_ratio()` - Sortino ratio
- `calmar_ratio()` - Calmar ratio
- `omega_ratio()` - Omega ratio

#### Market Relationship Metrics
- `alpha()`, `beta()` - Jensen's alpha and beta
- `up_capture()`, `down_capture()` - Capture ratios
- `tail_ratio()` - Tail ratio

#### Rolling Metrics
Most metrics have rolling versions prefixed with `roll_`:
- `roll_sharpe_ratio()`
- `roll_max_drawdown()`
- `roll_beta()`
- And many more...

### Period Constants

```python
from empyrical import DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY

# Use period constants for clarity
sharpe_daily = sharpe_ratio(returns, period=DAILY)
sharpe_monthly = sharpe_ratio(returns, period=MONTHLY)
```

### Testing

```bash
# Run all tests
pytest ./empyrical/tests -n 4

# Run specific test module
pytest ./empyrical/tests/test_stats.py

# Run specific test
pytest ./empyrical/tests/test_stats.py::test_sharpe_ratio
```

### Development

#### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/cloudQuant/empyrical
cd empyrical

# Create virtual environment (using conda)
conda create -n empyrical-dev python=3.11
conda activate empyrical-dev

# Install dependencies
pip install -U -r requirements.txt

# Install in development mode
pip install -e .
```

#### Testing Across Python Versions

```bash
# Unix/Linux/macOS
./test_python_versions_simple.sh

# Windows
test_python_versions_simple.bat
```

### Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Make your changes and add tests
4. Run tests to ensure everything works
5. Submit a pull request

### License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

Originally developed by Quantopian Inc. Currently maintained by the open-source community.

---

<a name="chinese-version"></a>
## 中文

### 概述

Empyrical 是一个用于计算常见金融风险和绩效指标的 Python 库。最初由 Quantopian Inc. 开发，它为量化金融专业人士和研究人员提供了一个全面的工具包，用于分析投资回报、计算风险指标和进行绩效归因。

### 特性

- **全面的指标**：超过 50 个金融指标，包括收益、风险、风险调整收益和市场关系指标
- **滚动计算**：大多数指标都有滚动窗口版本，用于时间序列分析
- **灵活的输入**：支持 pandas Series/DataFrame 和 numpy 数组
- **NaN 处理**：在所有计算中都能稳健地处理缺失数据
- **绩效归因**：基于因子的绩效分解
- **周期灵活性**：自动周期检测，支持日、周、月、季度和年度数据

### 安装

#### 从源码安装（推荐）

```bash
# 中国用户
git clone https://gitee.com/yunjinqi/empyrical

# 国际用户
git clone https://github.com/cloudQuant/empyrical

cd empyrical

# Windows 系统
install_win.bat

# Linux/macOS 系统
sh install_unix.sh
```

#### 从 PyPI 安装

```bash
pip install empyrical
```

### 快速开始

#### 基本指标

```python
import numpy as np
from empyrical import max_drawdown, sharpe_ratio, alpha_beta

# 示例收益数据
returns = np.array([0.01, 0.02, 0.03, -0.4, -0.06, -0.02])
benchmark_returns = np.array([0.02, 0.02, 0.03, -0.35, -0.05, -0.01])

# 计算最大回撤
mdd = max_drawdown(returns)
print(f"最大回撤: {mdd:.2%}")

# 计算夏普比率（假设为日收益）
sharpe = sharpe_ratio(returns, risk_free=0.02/252)
print(f"夏普比率: {sharpe:.2f}")

# 计算 alpha 和 beta
alpha, beta = alpha_beta(returns, benchmark_returns)
print(f"Alpha: {alpha:.4f}, Beta: {beta:.2f}")
```

#### 滚动指标

```python
import pandas as pd
from empyrical import roll_sharpe_ratio, roll_max_drawdown

# 创建时间序列数据
dates = pd.date_range('2020-01-01', periods=100, freq='D')
returns = pd.Series(np.random.normal(0.001, 0.02, 100), index=dates)

# 计算 30 天滚动夏普比率
rolling_sharpe = roll_sharpe_ratio(returns, window=30)

# 计算 30 天滚动最大回撤
rolling_mdd = roll_max_drawdown(returns, window=30)
```

#### DataFrame 高级用法

```python
import pandas as pd
from empyrical import annual_return, annual_volatility, calmar_ratio

# 多策略收益
strategies = pd.DataFrame({
    '策略_A': np.random.normal(0.001, 0.02, 252),
    '策略_B': np.random.normal(0.0015, 0.025, 252),
    '策略_C': np.random.normal(0.0008, 0.018, 252)
})

# 一次性计算所有策略的指标
annual_returns = annual_return(strategies)
annual_vols = annual_volatility(strategies)
calmar_ratios = calmar_ratio(strategies)

print("年化收益:")
print(annual_returns)
print("\n年化波动率:")
print(annual_vols)
print("\nCalmar 比率:")
print(calmar_ratios)
```

### 可用指标

#### 收益指标
- `simple_returns()` - 将价格转换为收益率
- `cum_returns()` - 累计收益
- `annual_return()` - 年化平均收益
- `cagr()` - 复合年增长率
- `aggregate_returns()` - 将收益聚合到不同频率

#### 风险指标
- `max_drawdown()` - 最大回撤
- `annual_volatility()` - 年化标准差
- `downside_risk()` - 下行风险
- `value_at_risk()` - 风险价值（VaR）
- `conditional_value_at_risk()` - 条件风险价值（CVaR/预期损失）

#### 风险调整收益指标
- `sharpe_ratio()` - 夏普比率
- `sortino_ratio()` - 索提诺比率
- `calmar_ratio()` - 卡玛比率
- `omega_ratio()` - 欧米茄比率

#### 市场关系指标
- `alpha()`, `beta()` - 詹森阿尔法和贝塔
- `up_capture()`, `down_capture()` - 捕获比率
- `tail_ratio()` - 尾部比率

#### 滚动指标
大多数指标都有以 `roll_` 为前缀的滚动版本：
- `roll_sharpe_ratio()`
- `roll_max_drawdown()`
- `roll_beta()`
- 以及更多...

### 周期常量

```python
from empyrical import DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY

# 使用周期常量以提高代码清晰度
sharpe_daily = sharpe_ratio(returns, period=DAILY)
sharpe_monthly = sharpe_ratio(returns, period=MONTHLY)
```

### 测试

```bash
# 运行所有测试
pytest ./empyrical/tests -n 4

# 运行特定测试模块
pytest ./empyrical/tests/test_stats.py

# 运行特定测试
pytest ./empyrical/tests/test_stats.py::test_sharpe_ratio
```

### 开发

#### 设置开发环境

```bash
# 克隆仓库
git clone https://gitee.com/yunjinqi/empyrical
cd empyrical

# 创建虚拟环境（使用 conda）
conda create -n empyrical-dev python=3.11
conda activate empyrical-dev

# 安装依赖
pip install -U -r requirements.txt

# 以开发模式安装
pip install -e .
```

#### 跨 Python 版本测试

```bash
# Unix/Linux/macOS
./test_python_versions_simple.sh

# Windows
test_python_versions_simple.bat
```

### 贡献

我们欢迎贡献！请按以下步骤操作：

1. Fork 仓库
2. 创建功能分支（`git checkout -b feature-name`）
3. 进行更改并添加测试
4. 运行测试确保一切正常
5. 提交 Pull Request

### 许可证

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

### 致谢

最初由 Quantopian Inc. 开发，目前由开源社区维护。