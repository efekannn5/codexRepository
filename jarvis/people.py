from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Person:
    name: str
    info: Dict[str, str] = field(default_factory=dict)


class PeopleDatabase:
    """Store information about people the assistant has met."""

    def __init__(self):
        self.people: Dict[str, Person] = {}

    def update_person(self, name: str, **info: str) -> None:
        person = self.people.setdefault(name, Person(name))
        person.info.update(info)

    def get_person(self, name: str) -> Person | None:
        return self.people.get(name)
