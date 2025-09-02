"""Conversation logic using OpenAI's chat completion API.

This module is intentionally simple so it can be swapped out with other
models in the future.
"""

from __future__ import annotations

import os
from typing import List, Dict

import openai


class ConversationAgent:
    def __init__(self, system_prompt: str | None = None):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.messages: List[Dict[str, str]] = []
        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def reply(self, text: str) -> str:
        self.messages.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        message = response.choices[0].message["content"].strip()
        self.messages.append({"role": "assistant", "content": message})
        return message
