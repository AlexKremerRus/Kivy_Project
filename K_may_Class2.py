from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


KV=""" 
BoxLayout:
    Button:
        text:"Button_2"
"""
class MainApp(BoxLayout):
    pass
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()