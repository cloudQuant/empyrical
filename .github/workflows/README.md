# GitHub Actions Workflows

This directory contains GitHub Actions workflows for continuous integration and deployment.

## Active Workflows

### 1. Main Test Suite (`tests.yml`)
- **Trigger**: Push/PR to master, main, develop branches
- **Purpose**: Comprehensive testing across multiple platforms and Python versions
- **Matrix**:
  - OS: Ubuntu, Windows, macOS  
  - Python: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 (excluding Python 3.13 on Windows)
- **Jobs**:
  - `test`: Full test suite on all platform/version combinations
  - `test-minimal`: Quick sanity check
  - `coverage`: Code coverage analysis
  - `lint`: Code quality checks
  - `build`: Package building and validation

### 2. Simple Test (`test-simple.yml`)
- **Trigger**: Push/PR to master, main, develop branches
- **Purpose**: Lightweight testing with minimal dependencies
- **Features**: Tests specific OS/Python combinations for quick feedback

### 3. Minimal Test (`test-minimal.yml`)
- **Trigger**: Push/PR to master, main, develop branches
- **Purpose**: Debug and identify specific issues
- **Features**: Detailed logging and step-by-step execution

### 4. Debug Workflow (`debug.yml`)
- **Trigger**: Manual (workflow_dispatch) or push to debug-ci branch
- **Purpose**: Detailed debugging when tests fail
- **Features**: Comprehensive system information and verbose output

### 5. Publish to PyPI (`publish.yml`)
- **Trigger**: GitHub release or manual workflow dispatch
- **Purpose**: Publish package to PyPI
- **Features**:
  - Option to test on Test PyPI first
  - Automated build and upload
  - Distribution validation

## Workflow Files Structure

```
.github/
├── workflows/
│   ├── tests.yml          # Main comprehensive test suite
│   ├── test-simple.yml    # Simple test with minimal deps
│   ├── test-minimal.yml   # Minimal test for debugging
│   ├── debug.yml          # Debug workflow
│   ├── publish.yml        # PyPI publishing
│   └── README.md          # This file
└── dependabot.yml         # Automated dependency updates
```

## Required Secrets

To enable PyPI publishing, add these secrets to your GitHub repository:

1. Go to Settings → Secrets and variables → Actions
2. Add:
   - `PYPI_API_TOKEN`: Your PyPI API token
   - `TEST_PYPI_API_TOKEN`: Your Test PyPI API token (optional)

## Local Testing

To test workflows locally using [act](https://github.com/nektos/act):

```bash
# Test the main workflow
act push -j test

# Test with specific Python version
act push -j test -P ubuntu-latest=python:3.11
```

## Troubleshooting

If workflows fail:

1. Check the `test-minimal.yml` workflow for detailed logs
2. Run the `debug.yml` workflow manually for comprehensive debugging
3. Review artifact uploads for test failures
4. Check dependency compatibility in `requirements.txt`