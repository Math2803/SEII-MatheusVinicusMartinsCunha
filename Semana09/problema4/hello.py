import kivi
from kivy.app import App
from kivy.uxi.label import label

class MyApp():
	def build(self):
		return label(text="Hello World", font_size=72)

if __name__ == '__main__':
 	MyApp().run()