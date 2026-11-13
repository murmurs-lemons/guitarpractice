# === Stage 1: Каркас модуля ===
# Project: GuitarPractice
from dataclasses import dataclass, field
from typing import List, Optional
import random


@dataclass
class Exercise:
    name: str
    tempo: int
    duration: int
    level: str
    tags: List[str] = field(default_factory=list)


def make_demo_exercises(count: int = 5) -> List[Exercise]:
    templates = [
        ("Хроматическая гамма", 90, 30, "начальный"),
        ("Метроном-метроном", 120, 45, "средний"),
        ("Лендинг-арпеджио", 80, 60, "продвинутый"),
        ("Пентатоника-петля", 100, 30, "начальный"),
        ("Блюзовый рифф", 140, 90, "продвинутый"),
    ]
    exercises: List[Exercise] = []
    for i in range(count):
        template = templates[i % len(templates)]
        exercises.append(Exercise(
            name=template[0],
            tempo=template[1],
            duration=template[2],
            level=template[3],
            tags=[f"demo-{i}"],
        ))
    return exercises


def main() -> None:
    exercises = make_demo_exercises()
    for exercise in exercises:
        print(f"{exercise.name} | темп {exercise.tempo} | "
              f"длительность {exercise.duration} | уровень {exercise.level}")
    if not exercises:
        print("Демо-записей не создано.")


if __name__ == "__main__":
    main()
