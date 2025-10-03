# Thonny Installation Guide (Ubuntu)

Thonny is a beginner-friendly Python IDE. Follow these steps to install Thonny on Ubuntu.

## Installation

```bash
# Install Python3 if not already installed
sudo apt install python3

# Create the virtual environement
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install Thonny
pip install thonny
```

## After installation

To launch Thonny, run:

```bash
thonny
```

A window should open, click on "Let's go!" to start using Thonny.

## Leave the virtual environment

To exit the virtual environment, simply run:

```bash
deactivate
```

## More Information

- [Thonny Official Website](https://thonny.org/)
- [Ubuntu Documentation](https://ubuntu.com/)
