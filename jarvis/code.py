from __future__ import annotations

"""Utilities for generating and testing code snippets.

The :class:`CodeAssistant` can iteratively ask an LLM to produce code,
run tests, and feed failures back to the model until the tests pass.
This mirrors how a human developer might work when solving a task.
"""

from pathlib import Path
import subprocess
from typing import Callable, List


CompletionFn = Callable[[str], str]


class CodeAssistant:
    """Generate code with an LLM and verify it by running tests.

    Parameters
    ----------
    completion_fn:
        Function that takes the conversation history and returns new code.
        Defaults to a small wrapper around OpenAI's chat completion API.
    """

    def __init__(self, completion_fn: CompletionFn | None = None):
        self.completion_fn: CompletionFn = completion_fn or self._openai_completion

    # ------------------------------------------------------------------
    def _openai_completion(self, prompt: str) -> str:
        """Query OpenAI's chat completion API with the given prompt."""
        import openai

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()

    # ------------------------------------------------------------------
    def run_task(
        self,
        prompt: str,
        file_path: Path,
        test_cmd: List[str] | None = None,
        max_iters: int = 3,
    ) -> str:
        """Iteratively generate code until tests pass.

        Parameters
        ----------
        prompt:
            Description of the desired code.
        file_path:
            Where the generated code should be written.
        test_cmd:
            Command used to verify correctness.  Defaults to ``python -m pytest``
            executed in the directory containing ``file_path``.
        max_iters:
            Maximum number of attempts before giving up.

        Returns
        -------
        str
            Output of the successful test run.

        Raises
        ------
        RuntimeError
            If the tests fail ``max_iters`` times.
        """

        test_cmd = test_cmd or ["python", "-m", "pytest"]
        history = prompt
        for _ in range(max_iters):
            code = self.completion_fn(history)
            file_path.write_text(code, encoding="utf-8")
            result = subprocess.run(
                test_cmd,
                cwd=file_path.parent,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                return result.stdout
            # augment prompt with error feedback
            history += f"\n\nTests failed:\n{result.stderr}"
        raise RuntimeError("Failed to satisfy tests after multiple iterations")
