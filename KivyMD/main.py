from kivy.core.text import LabelBase
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (310,580)

class Main(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager
    
    def on_start(self):
        self.login()
    
    def login(self, *args):
        # Get the "login" screen from the ScreenManager
        screen = screen_manager.get_screen("login")
        # Set the initial opacity of the "login" screen to 0
        screen.opacity = 0
        # Create an animation that will change the opacity of the "login" screen
        # from 0 to 1 over a duration of 2 seconds
        anim = Animation(opacity=1, duration=2)
        # Bind the "complete" event of the animation to a method that will set
        # the current screen to "login"
        anim.bind(on_complete=lambda *args: setattr(screen_manager, "current", "login"))
        # Start the animation
        anim.start(screen)
        
    # def build(self):
    #     screen_manager = ScreenManager()
    #     # screen_manager.add_widget(Builder.load_file("home.kv"))
    #     # screen_manager.add_widget(Builder.load_file("profile.kv"))
    #     screen_manager.add_widget(Builder.load_file("login.kv"))
    #     return screen_manager
    #     # label = Label(text='Hello, world!', font_name='Bpoppins')
    #     # return label

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