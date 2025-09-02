from pathlib import Path

from jarvis.jarvis import Jarvis


def main() -> None:
    jarvis = Jarvis(note_path=Path("notes.txt"), system_prompt="You are a helpful assistant.")
    print("Jarvis is listening. Press Ctrl+C to exit.")
    try:
        while True:
            jarvis.run_once()
    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()
