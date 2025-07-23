# GitHub Actions Workflows

This directory contains GitHub Actions workflows for continuous integration and deployment.

## Workflows

### 1. Tests (`tests.yml`)
- **Trigger**: Push to main branches, pull requests, and weekly schedule
- **Purpose**: Run comprehensive tests across multiple platforms and Python versions
- **Matrix**:
  - OS: Ubuntu, Windows, macOS
  - Python: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **Jobs**:
  - **test**: Run pytest on all platform/version combinations
  - **coverage**: Generate code coverage reports
  - **lint**: Code quality checks (flake8, black, isort)
  - **build**: Verify package builds correctly

### 2. Publish (`publish.yml`)
- **Trigger**: GitHub release or manual workflow dispatch
- **Purpose**: Publish package to PyPI
- **Features**:
  - Option to test on Test PyPI first
  - Automated build and upload
  - Distribution validation

## Setting up Secrets

To enable PyPI publishing, you need to add the following secrets to your GitHub repository:

1. Go to Settings → Secrets and variables → Actions
2. Add the following secrets:
   - `PYPI_API_TOKEN`: Your PyPI API token
   - `TEST_PYPI_API_TOKEN`: Your Test PyPI API token (optional)

## Local Testing

To test the workflows locally, you can use [act](https://github.com/nektos/act):

```bash
# Test the main workflow
act -j test

# Test with specific Python version
act -j test -P ubuntu-latest=python:3.11
```

## Workflow Status

The current status of the workflows is displayed in the main README.md file as badges.