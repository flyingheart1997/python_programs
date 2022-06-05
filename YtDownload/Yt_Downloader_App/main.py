import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
Window.size = (320, 600)


class WindowManager(ScreenManager):
    """A window that manage all the screen"""


class MessageScreen(Screen):
    """A screen that display all the history"""


class MainApp(MDApp):
    def build(self):
        """Initialize the application and return the root widget."""
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = 'Yt_Download'

        # storing the screen in a list
        screen = [
            MessageScreen(name='message')
        ]
        self.wm = WindowManager(transition=FadeTransition())
        for screen in screen:
            self.wm.add_widget(screen)
        return self.wm


if __name__ == '__main__':
    MainApp().run()
