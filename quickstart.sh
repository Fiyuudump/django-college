#!/bin/bash

# Step 1: Create virtual environment
echo "Creating virtual environment..."
py -m venv myenv

# Step 2: Activate the virtual environment depending on the OS
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows Git Bash or CMD
    # source myenv/Scripts/activate
    .\myenv\Scripts\activate
elif [[ "$OSTYPE" == "darwin" || "$OSTYPE" == "linux-gnu" ]]; then
    # macOS or Linux
    source myenv/bin/activate
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

# Step 3: Install dependencies
echo "Installing dependencies..."
pip install -r requirement.txt

# Step 4: Change directory to blog
cd blog || { echo "Directory 'blog' not found!"; exit 1; }

# Step 5: Apply database migrations
echo "Running migrations..."
py manage.py migrate

# Step 6: Create superuser
echo "Creating superuser..."
py manage.py createsuperuser
