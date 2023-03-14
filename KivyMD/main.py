from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (310,580)

class Main(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        # screen_manager.add_widget(Builder.load_file("home.kv"))
        # screen_manager.add_widget(Builder.load_file("profile.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager
        # label = Label(text='Hello, world!', font_name='Bpoppins')
        # return label

# Run the app in the emulator
if __name__ == '__main__':
    from kivy.config import Config
    Config.set('kivy', 'keyboard_mode', 'systemanddock')
    Config.set('kivy', 'keyboard_layout', 'numeric.json')
    Config.set('kivy', 'keyboard_provider', 'kivy')

    # from kivy.utils import platform
    # if platform == 'android':
    #     from android import mActivity
    #     mActivity.hide_navigation()

    Main().run()