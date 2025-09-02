"""High level orchestration for the Jarvis assistant."""

from __future__ import annotations

from pathlib import Path

from .speech import SpeechRecognizer, SpeechSynthesizer
from .conversation import ConversationAgent
from .notes import NoteTaker
from .people import PeopleDatabase
from .code import CodeAssistant


class Jarvis:
    def __init__(self, note_path: Path, system_prompt: str | None = None):
        self.speech_recognizer = SpeechRecognizer()
        self.speech_synthesizer = SpeechSynthesizer()
        self.conversation = ConversationAgent(system_prompt)
        self.notes = NoteTaker(note_path)
        self.people = PeopleDatabase()
        self.code = CodeAssistant()

    def run_once(self) -> None:
        """Listen, think, speak cycle for a single utterance."""
        text = self.speech_recognizer.listen()
        if not text:
            return
        response = self.conversation.reply(text)
        self.speech_synthesizer.say(response)
        self.notes.add(f"User: {text}\nJarvis: {response}")

    # ------------------------------------------------------------------
    def run_code_task(self, prompt: str, file_path: Path) -> str:
        """Generate code for ``prompt`` and ensure its tests pass."""
        return self.code.run_task(prompt, file_path)
