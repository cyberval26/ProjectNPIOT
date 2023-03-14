import firebase_admin
from firebase_admin import credentials, auth
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        try:
            user = auth.sign_in_with_email_and_password(self.email.text, self.password.text)
            print(user)
        except auth.AuthError as e:
            error_message = str(e.detail)
            self.show_error_dialog(error_message)

    def show_error_dialog(self, message):
        ok_button = MDFlatButton(text="OK", on_release=self.dismiss_dialog)
        self.dialog = MDDialog(title="Error", text=message, size_hint=(0.7, 1), buttons=[ok_button])
        self.dialog.open()

    def dismiss_dialog(self, obj):
        self.dialog.dismiss()
