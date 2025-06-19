#!/bin/bash

# Step 1: Create virtual environment & Activate the virtual environment depending on the OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows Git Bash or CMD
    # source myenv/Scripts/activate
    echo "Creating virtual environment..."
    py -m venv myenv
    echo "Activating virtual environment..."
    .\myenv\Scripts\activate
elif [[ "$OSTYPE" == "darwin" || "$OSTYPE" == "linux-gnu" ]]; then
    # macOS or Linux
    echo "Creating virtual environment..."
    python3 -m venv myenv
    echo "Activating virtual environment..."
    source myenv/bin/activate
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

# Step 3: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Change directory to blog
cd blog || { echo "Directory 'blog' not found!"; exit 1; }

# Step 5: Apply database migrations and Create superuser
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows Git Bash or CMD
    echo "Creating superuser..."
    py .\manage.py migrate
    echo "Creating superuser..."
    py .\manage.py createsuperuser

elif [[ "$OSTYPE" == "darwin" || "$OSTYPE" == "linux-gnu" ]]; then
    # macOS or Linux
    echo "Creating superuser..."
    python3 ./manage.py migrate
    echo "Creating superuser..."
    python3 ./manage.py createsuperuser

else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi
