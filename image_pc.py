from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source= r'C:/Users/aluno.sesipaulista/Desktop/aplicativo/fotopc/Merida01.webp')
    
if __name__ == "__main__":
    MinhaApp().run()