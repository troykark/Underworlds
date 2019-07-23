from kivy.app import App
from kivy.uix.widget import Widget


class Overworld(Widget):
    pass


class OverworldApp(App):
    def build(self):
        return Overworld()


if __name__ == '__main__':
    OverworldApp().run()