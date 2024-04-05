from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.texinput import TextInput

class SayHello(App):
	def buld(Self):
		self.window = GridLayout()
		self.window.cols = 1
		self.window.size_hint = (0.6,0.7)
		self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

		self.window.add_widget(Image(source="https://th.bing.com/th/id/OIP.FpBTdmS425XMYJ6kJH-fVAHaHd?rs=1&pid=ImgDetMain"))
		self.greeting = label(
			text="What's your name?",
			font_size = 18,
			color = "#ffffff"
		)
		self.window.add_widget(self.greeting)

		self.user = TexInput(
			multiline=False,
			padding_y = (20,20),
			size_hint = (1, 0.5)
		)
		self.window.add_widget(self.user)
		self.button = Button(
			text="GREET",
			size_hint = (1,0.5),
			bold = True,
			background_color = "#00ffce", 
			background_normal = ""
		)
		self.button.bind(on_press=self.callback)
		self.window.add_widget(self.button)

	def callback(self, instance):
		self.greeting.text = "hello "+self.user.text + "!"



		return self.window

if __name__ == "__main__":
	SayHello().run()

