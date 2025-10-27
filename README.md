
# Todo Terminal UI

A modern **terminal-based To-Do app** built with [Textual](https://github.com/Textualize/textual) and [Rich](https://github.com/Textualize/rich).  
Easily add, complete, and manage your daily tasks — all inside your terminal with an interactive interface.

## Features
    • Clean and responsive **terminal GUI (TUI)**  
    • Add, toggle, and delete tasks instantly  
    • Auto-save to `tasks.json`  
    • Keyboard shortcuts for fast control  
    • Works cross-platform (Linux, macOS, Window

## 🖥️ Preview


This is the User Interface of the Todo Application with keyboard shortcuts.








When You press letter a in keyboard the input box popouts and lets you add tasks in the task menu.

## Installation

## 1️. Clone the repository
```bash
git clone https://github.com/HawkeyeDev/todo-terminal-UI.git
cd todo-terminal-UI
## 2️.Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Linux / macOS)
# or
venv\Scripts\activate     # (Windows)
## 3️.Install dependencies
pip install textual rich
 Usage
Run the app:
python todo_app.py
Then use:
Key	Action
a	Add a new task
Space	Toggle task done/undone
d	Delete selected task
↑ / ↓	Navigate tasks
q	Quit app

Data Storage
All tasks are saved automatically to a local file named:
tasks.json
Tech Stack
    • Python 3.10+
    • Textual – Terminal UI framework
    • Rich – Beautiful terminal formatting
 Author
@HawkeyeDev
If you like this project, ⭐ the repo!


