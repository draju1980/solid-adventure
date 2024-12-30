Setting Up UV 

1. Install UV
Run the following command to install UV:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Initialize the Project
Use the uv init command to initialize your project:
```sh
uv init
```

Managing Python and the UV Environment
1. Pin Python Version
Pin the Python version to a specific version (e.g., 3.13) with the following command:
```sh
uv python pin 3.13
```

2. Add a Package to the UV Environment
To add a package (e.g., titanoboa) to your UV environment, use:
```sh
uv add titanoboa
uv add web3
```

3. Install vyper on UV Environment
To Install tool (e.g., vyper, pipx) to your UV environment, use:
```sh
uv tool install vyper
```

4. Run the Python Application
Execute your Python script (e.g., basic_python.py) using:
```sh
uv run python basic_python.py
```

5. Sync the UV Environment
To sync the environment and ensure dependencies are up-to-date, run:
```sh
uv sync
```

Working with the Virtual Environment
1. Check the Virtual Environment
To display information about the virtual environment:
```sh
uv venv
```

2. Activate the Virtual Environment
Enter the virtual environment with:
```sh
source .venv/bin/activate
```

3. Exit the Virtual Environment
To exit the virtual environment, you can either:
    Close the terminal, or
    Run the following command:
```sh
deactivate
```
