# === Stage 4: Редактирование записей ===
# Project: GuitarPractice
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

ALLOWED_FIELDS = {"title", "tempo", "duration", "level"}


@dataclass
class Exercise:
    id: int
    title: str
    tempo: int
    duration: float
    level: str
    created_at: str = field(default_factory=datetime.now, compare=False)


class ExerciseRepository:
    def __init__(self, path: Path) -> None:
        self._path = path
        self._exercises: dict[int, Exercise] = {}
        self._load()

    def _load(self) -> None:
        if self._path.exists():
            data = json.loads(self._path.read_text(encoding="utf-8"))
            for item in data.get("exercises", []):
                self._exercises[item["id"]] = Exercise(
                    id=item["id"],
                    title=item["title"],
                    tempo=item["tempo"],
                    duration=item["duration"],
                    level=item["level"],
                    created_at=item.get("created_at", ""),
                )

    def _save(self) -> None:
        payload = {"exercises": [vars(e) for e in self._exercises.values()]}
        self._path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def all(self) -> list[Exercise]:
        return list(self._exercises.values())

    def get(self, exercise_id: int) -> Optional[Exercise]:
        return self._exercises.get(exercise_id)


class ExerciseUpdater:
    def __init__(self, repository: ExerciseRepository) -> None:
        self._repository = repository

    def update(self, exercise_id: int, changes: dict[str, object]) -> Optional[Exercise]:
        exercise = self._repository.get(exercise_id)
        if exercise is None:
            return None

        filtered = {key: value for key, value in changes.items() if key in ALLOWED_FIELDS}
        if not filtered:
            return exercise

        for key, value in filtered.items():
            setattr(exercise, key, value)

        self._repository._save()
        return exercise
