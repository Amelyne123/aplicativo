from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout_principal = GridLayout(cols=2)
