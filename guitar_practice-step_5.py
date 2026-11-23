# === Stage 5: Удаление и восстановление ===
# Project: GuitarPractice
from datetime import datetime


class Exercise:
    def __init__(self, name, tempo, duration, level):
        self.id = None
        self.name = name
        self.tempo = tempo
        self.duration = duration
        self.level = level
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = datetime.now()
        return self

    def restore(self):
        self.deleted = False
        self.deleted_at = None
        return self

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "tempo": self.tempo,
            "duration": self.duration,
            "level": self.level,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at,
        }
        return data


class ExerciseStore:
    def __init__(self):
        self._exercises = {}
        self._counter = 0

    def create(self, name, tempo, duration, level):
        self._counter += 1
        exercise = Exercise(name, tempo, duration, level)
        exercise.id = self._counter
        self._exercises[exercise.id] = exercise
        return exercise

    def get(self, exercise_id):
        return self._exercises.get(exercise_id)

    def list_active(self):
        return [e for e in self._exercises.values() if not e.deleted]

    def list_deleted(self):
        return [
            e for e in self._exercises.values() if e.deleted
        ]

    def delete(self, exercise_id):
        exercise = self.get(exercise_id)
        if exercise is not None:
            exercise.soft_delete()
        return exercise is not None

    def restore(self, exercise_id):
        exercise = self.get(exercise_id)
        if exercise is not None:
            exercise.restore()
        return exercise is not None

    def remove(self, exercise_id):
        return self._exercises.pop(exercise_id, None) is not None

    def count_active(self):
        return len(self.list_active())

    def count_deleted(self):
        return len(self.list_deleted())
