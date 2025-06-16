from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Footer, Button
from textual.containers import Vertical
from textual.screen import Screen


class MainMenuScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Welcome to the Git Tutorial! Select a lesson:", id="main-text")
        yield Vertical(
            Button("Git Init", id="init_lesson"),
            Button("Git Status", id="status_lesson"),
            Button("Git Add", id="add_lesson"),
            Button("Git Commit", id="commit_lesson"),
            Button("Git Log", id="log_lesson"),
            Button("Git Branch", id="branch_lesson"),
            Button("Git Checkout", id="checkout_lesson"),
            Button("Git Merge", id="merge_lesson"),
        )
        yield Footer()

    def on_button_pressed(self, event):
        self.app.push_screen(event.button.id)
