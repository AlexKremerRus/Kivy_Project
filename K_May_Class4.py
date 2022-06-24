from kivy.app import App
from kivy.lang import Builder

KV=""" 
<MyButton@Button>:
    font_size: '25sp'
    pos_hint: {'center_x':.5, 'center_y':.6}
    markup: True

BoxLayout:
    orientation:"vertical"
    MyButton:
        text:"Button_1"
    MyButton:
        text:"Button_2"
    MyButton:
        text:"Button_3"
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()