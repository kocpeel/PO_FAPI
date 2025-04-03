import pyttsx3
import speech_recognition as sr
import wave


class Orator:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        """Słowo wypowiedzenie"""
        self.engine.say(text)
        self.engine.runAndWait()

    def record(self, text, output_file):
        """Nagranie mowy"""
        self.engine.say(text)
        self.engine.runAndWait()

        wf = wave.open(output_file, 'wb')
        wf.setnchannels(1)  # Jedna kanałowa
        wf.setsampwidth(wf.getsampwidth())
        wf.setframerate(44100)

        microphone = sr.Microphone()
        audio = self.recognizer.record(microphone, duration=10)

        wf.writeframesraw(audio.get_raw_data())

        wf.close()

    def read_from_file(self, source_file, output_file):
        """Odczyt z pliku"""
        with wave.open(source_file, 'rb') as wav_file:
            data = wav_file.readframes(wav_file.getnframes())

        audio = sr.AudioData(data, wav_file.getnframes(), wav_file.getsampwidth())

        try:
            text = self.recognizer.recognize_google(audio)
            self.speak(f"Recognize word: {text}")

            # Zapisz rozpoznane słwo do pliku
            with open(output_file, 'w') as f:
                f.write(text)
        except sr.UnknownValueError:
            print("Can not recognize.")
        except sr.RequestError as e:
            print(f"Can not connect; {e}")