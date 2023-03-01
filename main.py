from gtts import gTTS 
from playsound import playsound
import os

class mp3Creator:
    def __init__(self, text):
        self.text = text
        self.mp3 = gTTS(text=self.text)

    def create(self):
        self.mp3.save("mp3.mp3")

class Speaker:
    def __init__(self):
        self.cwd = os.getcwd()

    def speak(self):
        playsound(self.cwd + "\mp3.mp3")

    def speaktwice(self):
        playsound(self.cwd + "\mp3.mp3")
        playsound(self.cwd + "\mp3.mp3")


if __name__ == "__main__":
    mp3Creator("Hello World").create()
    Speaker().speaktwice()
    