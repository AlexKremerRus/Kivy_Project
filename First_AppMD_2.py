
from kivymd. app import MDApp
from kivymd.uix.label import MDLabel
class MainApp(MDApp):
    def build(self):
        self.icon = "/Users/alex/PycharmProjects/Kivy_Project/icon.ico"
        self.title = "Приложение на KivyMD"
        label = MDLabel (text="Привет от KivyMD и Python", halign="center")
        return label
if __name__ == '__main__':

    app = MainApp ()
    app.run ()