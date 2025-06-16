from textual.app import App
from tui.main_screen import MainMenuScreen
from lessons.init_lesson import InitLessonScreen
from lessons.add_lesson import AddLessonScreen


class TutorialApp(App):
    CSS_PATH = None  # Set to your CSS file if you have one
    SCREENS = {
        "main_menu": MainMenuScreen,
        "init_lesson": InitLessonScreen,
        "add_lesson": AddLessonScreen,
    }

    def on_mount(self):
        self.push_screen("main_menu")


if __name__ == "__main__":
    app = TutorialApp()
    app.run()
