Setting Up UV 

1. Install UV
Run the following command to install UV:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Initialize the Project
Use the uv init command to initialize your project:
```bash
uv init
```

Managing Python and the UV Environment
1. Pin Python Version
Pin the Python version to a specific version (e.g., 3.13) with the following command:
```bash
uv python pin 3.13
```

2. Add a Package to the UV Environment
To add a package (e.g., titanoboa) to your UV environment, use:
```bash
uv add titanoboa
```

3. Run the Python Application
Execute your Python script (e.g., basic_python.py) using:
```bash
uv run python basic_python.py
```

4. Sync the UV Environment
To sync the environment and ensure dependencies are up-to-date, run:
```bash
uv sync
```

Working with the Virtual Environment
1. Check the Virtual Environment
To display information about the virtual environment:
```bash
uv venv
```

2. Activate the Virtual Environment
Enter the virtual environment with:
```bash
source .venv/bin/activate
```

3. Exit the Virtual Environment
To exit the virtual environment, you can either:
    Close the terminal, or
    Run the following command:
```bash
deactivate
```
