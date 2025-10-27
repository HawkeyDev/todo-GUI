from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Static, Input
from textual.events import Key
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

class TodoApp(App):
    def __init__(self):
        super().__init__()
        self.tasks = load_tasks()
        self.typing = False  # True when typing a new task

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("📝 Terminal To-Do List | a=add d=delete space=toggle", id="title")
        self.table = DataTable(zebra_stripes=True)
        self.table.add_columns("Status", "Task")
        yield self.table
        self.input_box = Input(placeholder="Type task and press Enter...", visible=False)
        yield self.input_box
        yield Footer()

    def on_mount(self):
        self.load_table()
        self.table.cursor_type = "row"
        self.table.focus()

    def load_table(self):
        self.table.clear()
        for t in self.tasks:
            status = "✅" if t["done"] else "❌"
            self.table.add_row(status, t["task"])

    async def on_key(self, event: Key):
        if self.typing:
            return  # Ignore commands while typing

        key = event.key.lower()
        if key == "a":
            # Enter typing mode
            self.typing = True
            self.input_box.visible = True
            self.input_box.focus()
        elif key == "d" and
