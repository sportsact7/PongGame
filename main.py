# Stet 1 - Create the app
# Stet 2 - Create the game
# Stet 3 - Build the Game
# Stet 4 - Run the Game
from kivy.app import App
from kivy.uix.widget import Widget

# Stet 2 - Create the game
class PongGame(Widget):
    pass
# Stet 1 - Create the app
class PongApp(App):
    def build(self):
        return PongGame() # Stet 3 - Build the Game

# Stet 4 - Run the Game
PongApp().run()

