# === Stage 3: Хранилище в памяти ===
# Project: GuitarPractice
class Exercise:
    def __init__(self, name, tempo, duration, level):
        self.id = None
        self.name = name
        self.tempo = tempo
        self.duration = duration
        self.level = level

    def __repr__(self):
        return f"Exercise(id={self.id}, name={self.name}, tempo={self.tempo}, duration={self.duration}, level={self.level})"


class ExerciseStore:
    def __init__(self):
        self._exercises = {}
        self._counter = 0

    def add(self, name, tempo, duration, level):
        self._counter += 1
        exercise = Exercise(name, tempo, duration, level)
        exercise.id = self._counter
        self._exercises[exercise.id] = exercise
        return exercise

    def get(self, exercise_id):
        return self._exercises.get(exercise_id)

    def list(self):
        return list(self._exercises.values())
