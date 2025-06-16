from textual.screen import Screen
from textual.widgets import Header, Static, Footer
from textual.app import ComposeResult


class InitLessonScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Lesson: git init\n\nThis command initializes a new Git repository in your current directory.")
        yield Footer()
