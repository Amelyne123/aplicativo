from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        layout= BoxLayout()
        url = 'https://recreio.uol.com.br/media/_versions/disney/merida_valente_capa_widelg.jpg'
        image= AsyncImage(source=url)
        layout.add_widget(image)
        return layout 
        
if __name__ == "__main__":
    MinhaApp().run()
