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
    CSS_PATH = None

    def __init__(self):
        super().__init__()
        self.tasks = load_tasks()
        self.adding = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("📝 To-Do List | [a]=Add  [space]=Toggle  [d]=Delete", id="title")
        self.table = DataTable(zebra_stripes=True)
        self.table.add_columns("Status", "Task")
        yield self.table

        self.input_box = Input(placeholder="Press 'a' to add a task...")
        yield self.input_box

        yield Footer()

    def on_mount(self):
        self.load_table()
        self.table.cursor_type = "row"
        self.table.focus()
        self.input_box.display = False  # Hide input initially

    def load_table(self):
        self.table.clear()
        for t in self.tasks:
            status = "[green]✅[/green]" if t["done"] else "[red]❌[/red]"
            self.table.add_row(status, t["task"])

    async def on_key(self, event: Key):
        # Ignore keys while typing a task
        if self.adding:
            return

        key = event.key.lower()

        if key == "a":
            # Enter add mode
            self.adding = True
            self.input_box.display = True
            self.input_box.placeholder = "Type a new task and press Enter..."
            self.input_box.value = ""
            self.input_box.focus()

        elif key == "space" and self.tasks and self.table.cursor_row is not None:
            # Toggle done/undone
            idx = self.table.cursor_row
            self.tasks[idx]["done"] = not self.tasks[idx]["done"]
            save_tasks(self.tasks)
            self.load_table()

        elif key == "d" and self.tasks and self.table.cursor_row is not None:
            # Delete selected task
            idx = self.table.cursor_row
            self.tasks.pop(idx)
            save_tasks(self.tasks)
            self.load_table()

    def on_input_submitted(self, event):
        if not self.adding:
            return

        task_text = event.value.strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            save_tasks(self.tasks)
            self.load_table()

        # Exit add mode
        self.adding = False
        self.input_box.display = False
        self.table.focus()


if __name__ == "__main__":
    TodoApp().run()
