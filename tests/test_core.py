from pathlib import Path

from jarvis.notes import NoteTaker
from jarvis.people import PeopleDatabase


def test_note_taker(tmp_path: Path) -> None:
    path = tmp_path / "notes.txt"
    nt = NoteTaker(path)
    nt.add("hello")
    nt.add("world")
    assert path.read_text(encoding="utf-8") == "hello\nworld"


def test_people_database() -> None:
    db = PeopleDatabase()
    db.update_person("Ayşe", role="manager")
    person = db.get_person("Ayşe")
    assert person is not None
    assert person.info["role"] == "manager"
