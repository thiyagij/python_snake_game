#!/bin/bash
# Setup script for Python Snake Game
# Works on Unix, Linux, macOS, and Windows (Git Bash/WSL)
#
# Usage: ./setup.sh
# Or: bash setup.sh

set -e  # Exit on error

echo "==================================="
echo "Python Snake Game Setup"
echo "==================================="
echo ""

# Function to check Python version
check_python_version() {
    local python_cmd=$1
    if command -v $python_cmd &> /dev/null; then
        local version=$($python_cmd --version 2>&1 | awk '{print $2}')
        local major=$(echo $version | cut -d. -f1)
        local minor=$(echo $version | cut -d. -f2)
        
        if [ "$major" -ge 3 ] && [ "$minor" -ge 8 ]; then
            echo "$python_cmd"
            return 0
        fi
    fi
    return 1
}

# Find suitable Python version
echo "Checking Python installation..."
PYTHON_CMD=""

if check_python_version "python3"; then
    PYTHON_CMD="python3"
elif check_python_version "python"; then
    PYTHON_CMD="python"
else
    echo "Error: Python 3.8 or higher is not installed."
    echo "Please install Python 3.8.1 or higher and try again."
    echo ""
    echo "Download from: https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python found: $($PYTHON_CMD --version)"
echo ""

# Check if virtual environment already exists
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping creation."
    echo "To recreate, delete the 'venv' directory first."
    echo ""
else
    # Create virtual environment
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        echo "Make sure you have python3-venv installed:"
        echo "  Ubuntu/Debian: sudo apt-get install python3-venv"
        echo "  Fedora/RHEL: sudo yum install python3-virtualenv"
        exit 1
    fi
    
    echo "✓ Virtual environment created successfully!"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    # Windows Git Bash
    source venv/Scripts/activate
else
    echo "Error: Could not find activation script."
    exit 1
fi

echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

echo "✓ pip upgraded"
echo ""

# Install requirements
echo "Installing requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install requirements."
        exit 1
    fi
    
    echo "✓ Requirements installed successfully!"
else
    echo "Warning: requirements.txt not found. Skipping dependencies."
fi

echo ""
echo "==================================="
echo "✓ Setup completed successfully!"
echo "==================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the game:"
echo "   python snake_game.py"
echo ""
echo "3. Run tests (optional):"
echo "   python test_game.py"
echo ""
echo "Game controls:"
echo "  ↑↓←→  Move"
echo "  P     Pause/Resume"
echo "  R     Restart"
echo "  Q     Quit"
echo ""
echo "Enjoy playing Snake! 🐍🎮"
