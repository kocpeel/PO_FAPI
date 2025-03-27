import pyttsx3
import subprocess

class Orator:
    def speak(self, text: str):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def record(self, text: str, output_file: str):
        subprocess.run(["arecord", "-f", "cd", output_file], input=text.encode())

    def read_from_file(self, source_file: str, output_file: str):
        with open(source_file, "r") as f:
            text = f.read()
        self.record(text, output_file)