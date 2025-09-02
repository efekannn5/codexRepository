from pathlib import Path

from jarvis.code import CodeAssistant


def test_code_assistant_iterates(tmp_path: Path) -> None:
    """CodeAssistant should refine code until tests pass."""

    # Create a simple test suite expecting an add function
    test_file = tmp_path / "test_calc.py"
    test_file.write_text(
        "from calc import add\n\n\n" "def test_add():\n    assert add(1, 2) == 3\n",
        encoding="utf-8",
    )

    # Stub that returns faulty code first, then fixes it after receiving feedback
    def stub(prompt: str) -> str:
        if "Tests failed" in prompt:
            return "def add(a, b):\n    return a + b\n"
        return "def add(a, b)\n    return a + b\n"

    assistant = CodeAssistant(completion_fn=stub)
    file_path = tmp_path / "calc.py"
    output = assistant.run_task("implement add", file_path)

    assert "1 passed" in output
    assert "return a + b" in file_path.read_text(encoding="utf-8")
