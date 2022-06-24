from kivy.app import App
from kivy.lang import Builder

KV=""" 
BoxLayout:
    Button:
        text:"Button_1"
"""
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()