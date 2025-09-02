from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class NoteTaker:
    """Collect meeting notes and persist them to disk."""

    path: Path
    notes: List[str] = field(default_factory=list)

    def add(self, note: str) -> None:
        self.notes.append(note)
        self.path.write_text("\n".join(self.notes), encoding="utf-8")

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"NoteTaker(path={self.path!r}, notes={self.notes!r})"
