# CI/CD Pipeline Documentation

This document describes the Continuous Integration and Continuous Deployment (CI/CD) pipeline for the Python Snake Game project.

## Overview

The CI/CD pipeline is implemented using GitHub Actions and runs automatically on every push and pull request to the `main` and `develop` branches.

## Pipeline Components

### 1. Linting (`lint` job)

**Purpose**: Ensures code quality and style consistency

- **Tool**: flake8
- **Runs on**: `ubuntu-latest`
- **Python version**: 3.11
- **Checks**:
  - Python syntax errors and undefined names (E9, F63, F7, F82)
  - Code complexity (max 10)
  - Line length (max 127 characters)

**How to run locally**:
```bash
pip install flake8
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### 2. Testing (`test` job)

**Purpose**: Validates functionality across multiple platforms and Python versions

- **Platforms**: Ubuntu, Windows, macOS
- **Python versions**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Tools**: pytest, pytest-cov
- **Coverage**: Generates code coverage reports

**Matrix Strategy**: Tests run on 15 different combinations (3 OS × 5 Python versions)

**How to run locally**:
```bash
pip install pytest pytest-cov
pytest test_game.py -v --cov=snake_game --cov-report=xml --cov-report=term
```

**Coverage Upload**: Coverage reports from Ubuntu + Python 3.11 are uploaded to Codecov

### 3. Build (`build` job)

**Purpose**: Creates distributable packages

- **Tool**: Poetry
- **Depends on**: `lint` and `test` jobs must pass
- **Outputs**:
  - Source distribution (`.tar.gz`)
  - Wheel distribution (`.whl`)
- **Artifact retention**: 30 days

**How to run locally**:
```bash
pip install poetry
poetry install --no-interaction
poetry build
```

**Artifacts**: Built packages are uploaded as GitHub Actions artifacts

### 4. Publish Package (`publish-package` job)

**Purpose**: Publishes packages to GitHub Packages

- **Trigger**: Only on push to `main` branch
- **Depends on**: `build` job must pass
- **Registry**: GitHub Packages (Maven format)
- **Authentication**: Uses `GITHUB_TOKEN`

**Note**: This job only runs on the main branch, not on pull requests.

### 5. Deploy Pages (`deploy-pages` job)

**Purpose**: Deploys documentation to GitHub Pages

- **Trigger**: Only on push to `main` branch
- **Depends on**: `lint` and `test` jobs must pass
- **Content**:
  - README.md → index.html
  - GAMEPLAY.md → gameplay.html
  - QUICKSTART.md → quickstart.html
  - Custom landing page with navigation

**GitHub Pages URL**: `https://<username>.github.io/python_snake_game/`

## Workflow Triggers

The pipeline runs on:

1. **Push** to `main` or `develop` branches
2. **Pull requests** targeting `main` or `develop` branches
3. **Manual trigger** via workflow_dispatch

## Required GitHub Settings

### Permissions

The workflow requires the following permissions (configured in the workflow file):

- `contents: write` - For committing changes
- `pages: write` - For deploying to GitHub Pages
- `id-token: write` - For GitHub Pages deployment
- `packages: write` - For publishing to GitHub Packages

### GitHub Secrets

For package publishing to work, configure these secrets:

**Optional Secrets** (for package publishing):
1. Go to repository Settings → Secrets and variables → Actions
2. Add the following secrets:
   - `PYPI_USERNAME` - Your PyPI username
   - `PYPI_PASSWORD` - Your PyPI password or token

**Note**: Package publishing will be skipped if secrets are not configured. All other pipeline jobs (lint, test, build, deploy docs) work without secrets.

### GitHub Pages Setup

To enable GitHub Pages deployment:

1. Go to repository Settings → Pages
2. Under "Build and deployment":
   - Source: GitHub Actions
3. Save changes

The documentation site will be automatically deployed on pushes to the main branch.

## Package Management with Poetry

### What is Poetry?

Poetry is a modern Python dependency management and packaging tool that provides:

- Dependency resolution
- Virtual environment management
- Package building and publishing
- Lock file for reproducible builds

### Poetry Configuration Files

1. **`pyproject.toml`**: Project metadata and dependencies
   - Project name, version, description
   - Python version requirement (≥3.8.1)
   - Runtime dependencies (windows-curses for Windows)
   - Development dependencies (pytest, flake8, etc.)
   - Build system configuration
   - Tool-specific settings (pytest, flake8)

2. **`poetry.lock`**: Locked dependency versions
   - Ensures reproducible installations
   - Contains exact versions of all dependencies
   - Should be committed to version control

### Common Poetry Commands

```bash
# Install dependencies
poetry install

# Add a new dependency
poetry add <package-name>

# Add a development dependency
poetry add --group dev <package-name>

# Update dependencies
poetry update

# Build the package
poetry build

# Publish to a repository
poetry publish -r <repository-name>

# Run a command in the virtual environment
poetry run <command>

# Run the game using poetry
poetry run snake-game
```

### Script Entry Point

The game can be run using the poetry script entry point:

```bash
poetry run snake-game
```

This is configured in `pyproject.toml`:

```toml
[tool.poetry.scripts]
snake-game = "snake_game:main_wrapper"
```

## Local Development

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/thiyagij/python_snake_game.git
   cd python_snake_game
   ```

2. Install Poetry:
   ```bash
   pip install poetry
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

### Running Tests

```bash
# Run tests with poetry
poetry run pytest test_game.py -v

# Run with coverage
poetry run pytest test_game.py -v --cov=snake_game --cov-report=term

# Run the legacy test script
python test_game.py
```

### Running Linters

```bash
# Run flake8 with poetry
poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Full flake8 check
poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### Building the Package

```bash
# Build source and wheel distributions
poetry build

# Check the dist/ directory
ls -la dist/
```

### Running the Game

```bash
# Using poetry
poetry run snake-game

# Or directly with Python
python snake_game.py
```

## Continuous Integration Status

Check the status of the CI/CD pipeline:

- Go to the repository's Actions tab on GitHub
- View the latest workflow runs
- Click on a run to see detailed logs for each job

## Troubleshooting

### Failed Lint Job

If linting fails:

1. Check the error messages in the GitHub Actions log
2. Run flake8 locally to reproduce the issue
3. Fix the code style issues
4. Commit and push the changes

### Failed Test Job

If tests fail:

1. Check which platform/Python version failed
2. Run tests locally with the same Python version
3. Fix the failing tests
4. Ensure tests pass on all supported Python versions

### Failed Build Job

If the build fails:

1. Check the Poetry build output
2. Ensure `pyproject.toml` is valid
3. Run `poetry check` locally
4. Run `poetry build` locally to reproduce

### Failed Publish Job

If publishing fails:

1. Check GitHub Packages permissions
2. Ensure `GITHUB_TOKEN` has required permissions
3. Verify the package version is unique (not already published)

### Failed Pages Deploy

If GitHub Pages deployment fails:

1. Check GitHub Pages is enabled in repository settings
2. Verify the Pages permissions are correct
3. Check the deployment logs for specific errors

## Best Practices

1. **Always run tests locally** before pushing
2. **Use poetry** for dependency management
3. **Keep poetry.lock** in version control
4. **Run linters** before committing
5. **Write tests** for new features
6. **Update documentation** when adding features
7. **Check CI status** after pushing

## Future Enhancements

Potential improvements to the CI/CD pipeline:

- [ ] Add code coverage badges to README
- [ ] Add workflow status badges
- [ ] Implement automated version bumping
- [ ] Add changelog generation
- [ ] Implement semantic release
- [ ] Add performance benchmarking
- [ ] Add security scanning (e.g., Bandit, Safety)
- [ ] Add dependency update automation (e.g., Dependabot)

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [flake8 Documentation](https://flake8.pycqa.org/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Packages Documentation](https://docs.github.com/en/packages)
