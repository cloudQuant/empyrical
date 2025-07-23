# GitHub Actions Workflows

本目录包含用于持续集成和部署的GitHub Actions工作流。

## 工作流文件

### 1. CI主工作流 (`ci.yml`)
- **触发条件**: 推送到master/main分支，PR，手动触发
- **测试矩阵**:
  - **操作系统**: Ubuntu (latest), Windows (latest), macOS (latest)
  - **Python版本**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **任务**:
  - `test`: 在所有平台和Python版本上运行完整测试套件
  - `test-summary`: 汇总测试结果
  - `coverage`: 代码覆盖率分析
  - `lint`: 代码质量检查
  - `build`: 构建和验证包

### 2. 调试工作流 (`debug.yml`) 
- **触发条件**: 手动触发或推送到debug-*分支
- **用途**: 详细诊断CI问题
- **特性**: 
  - 详细的系统信息输出
  - 目录结构展示
  - 逐步测试执行

### 3. 发布工作流 (`publish.yml`)
- **触发条件**: GitHub release或手动触发
- **用途**: 发布包到PyPI
- **特性**:
  - 可选先发布到Test PyPI
  - 自动构建和上传
  - 分发验证

## 测试覆盖

| 操作系统 | Python版本 | 状态 |
|---------|-----------|------|
| Ubuntu | 3.8 - 3.13 | ✅ |
| Windows | 3.8 - 3.13 | ✅ |
| macOS | 3.8 - 3.13 | ✅ |

## 本地测试

使用pytest运行测试：

```bash
# 运行所有测试
pytest tests/

# 运行特定测试文件
pytest tests/test_stats.py

# 运行特定测试
pytest tests/test_stats.py::test_sharpe_ratio

# 带覆盖率运行
pytest tests/ --cov=empyrical
```

## 故障排除

如果CI失败：

1. 查看GitHub Actions日志了解具体错误
2. 运行debug.yml工作流进行详细诊断
3. 检查测试文件路径是否正确
4. 验证依赖项兼容性

## 必需的密钥

要启用PyPI发布，需要在GitHub仓库中添加以下密钥：

1. 进入 Settings → Secrets and variables → Actions
2. 添加:
   - `PYPI_API_TOKEN`: PyPI API令牌
   - `TEST_PYPI_API_TOKEN`: Test PyPI API令牌（可选）