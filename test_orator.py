import unittest
from .client.orator import Orator

#
class TestOrator(unittest.TestCase):

    def setUp(self):
        self.orator = Orator()

    def test_speak(self):
        text = "Testowy tekst do wypowiedzenia"
        result = self.orator.speak(text)
        self.assertEqual(result, f"Text '{text}' has been spoken")

    def test_record(self):
        output_file = "test_recording.wav"
        result = self.orator.record("Testowy tekst do nagrania", output_file)
        self.assertEqual(result, f"Text 'Testowy tekst do nagrania' has been recorded")

        import os
        self.assertTrue(os.path.exists(output_file))

    def test_read_from_file(self):
        source_file = "test_source.txt"
        output_file = "test_output.txt"

        with open(source_file, 'w') as f:
            f.write("Testowy tekst do odczytu")

        result = self.orator.read_from_file(source_file, output_file)

        import os
        self.assertTrue(os.path.exists(output_file))

        with open(output_file, 'r') as f:
            content = f.read()
        self.assertEqual(content.strip(), "Testowy tekst do odczytu")


if __name__ == '__main__':
    unittest.main()