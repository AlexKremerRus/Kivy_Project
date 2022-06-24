from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.title="App development with Kivy"
        self.icon="/Users/alex/PycharmProjects/Kivy_Project/icon1.ico"
        label=Label(text="hello from kivy and Python!")
        return label

if __name__=='__main__':
    app = MainApp()  # создание объекта (приложения app) на основе базового класса
    app.run()  # запуск приложения
