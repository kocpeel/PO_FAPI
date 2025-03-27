import argparse
from ..src.orator import Orator


def main():
    parser = argparse.ArgumentParser(description="Orator CLI tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # orator <tekst_do_wypowiedzenia>
    speak_parser = subparsers.add_parser("speak", help="Speak the given text")
    speak_parser.add_argument("text", type=str, help="The text to be spoken")

    # orator <tekst_do_wypowiedzenia> -o <nazwa_pliku>
    record_parser = subparsers.add_parser("record", help="Record the spoken text")
    record_parser.add_argument("-o", "--output-file", type=str, required=True, help="Output file name")

    # orator -s <nazwa_pliku_tekstowego> -o <nazwa_pliku>
    read_file_parser = subparsers.add_parser("read", help="Read from a text file and record")
    read_file_parser.add_argument("-s", "--source-file", type=str, required=True, help="Source text file name")
    read_file_parser.add_argument("-o", "--output-file", type=str, required=True, help="Output file name")

    args = parser.parse_args()

    if args.command == "speak":
        Orator().speak(args.text)
    elif args.command == "record":
        Orator().record(args.text, args.output_file)
    elif args.command == "read":
        Orator().read_from_file(args.source_file, args.output_file)


if __name__ == "__main__":
    main()
