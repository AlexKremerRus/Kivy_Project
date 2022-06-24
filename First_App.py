'''
import kivy.app  # импорт фрейморка kivy
import kivy.uix.label

class MainApp(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text="hello from Kivy!")



app = MainApp(title="First App on kivy")  # создание объекта (приложения app) на основе базового класса
app.run()  # запуск приложения
'''

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(text="hello from Kivy!", halign="center")

app = MainApp( title = "First App on kivy" )  # создание объекта (приложения app) на основе базового класса
app.run()  # запуск приложения