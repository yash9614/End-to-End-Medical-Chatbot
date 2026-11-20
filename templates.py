import os
from pathlib import Path

# Project root
project_name = "End to End Medical Chatbot"

# List of files and directories to create
list_of_files = [
    # Source package
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",

    # Data & research
    "data/.gitkeep",
    "research/.gitkeep",

    # Frontend
    "templates/chat.html",
    "static/style.css",

    # Core files
    "app.py",
    "store_index.py",
    "setup.py",
    "requirements.txt",
    ".env",
    ".gitignore",
    "Dockerfile",
    "README.md",

    # Optional CI/CD
    ".github/workflows/cicd.yaml",
]

def create_structure():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            print(f"Creating directory: {filedir}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
            print(f"Creating empty file: {filepath}")
        else:
            print(f"File already exists: {filepath}")

if __name__ == "__main__":
    create_structure()
    print("\n✅ Folder structure created successfully!")    