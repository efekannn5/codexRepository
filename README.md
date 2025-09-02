# Jarvis Prototype

This repository contains a minimal, extensible foundation for building a
voice-enabled assistant similar to "Jarvis".  The focus is on a clean
architecture so new capabilities can be added incrementally.

Beyond simple conversation, the assistant can tackle programming tasks by
generating code, executing unit tests, and iterating on failures
automatically.

## Components

- `speech.py` – microphone input via `SpeechRecognition` and spoken
  responses using `pyttsx3`.
- `conversation.py` – wraps OpenAI's ChatCompletion API for dialogue.
- `notes.py` – simple meeting note collection that writes to disk.
- `people.py` – lightweight in-memory database about people you meet.
- `jarvis.py` – orchestrates the modules into a single assistant.
- `code.py` – generate code via an LLM and verify it by running tests.
- `main.py` – example command-line entry point.

## Development

Install dependencies and run tests:

```bash
pip install -r requirements.txt
python -m pytest
```

Set the `OPENAI_API_KEY` environment variable to enable the conversation
module.
