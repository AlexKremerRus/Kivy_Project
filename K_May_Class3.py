from kivy.app import App
from kivy.lang import Builder


KV=""" 
<MyBox@BoxLayout>
MyBox:
    Button:
        text:"Button_3"
"""
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()