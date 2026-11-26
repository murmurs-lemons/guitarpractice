# === Stage 7: Связи между сущностями ===
# Project: GuitarPractice
from datetime import datetime


class GuitarExercise:
    def __init__(self, name, tempo, duration, level):
        self.name = name
        self.tempo = tempo
        self.duration = duration
        self.level = level


class Session:
    def __init__(self, exercise, date, completed):
        self.exercise = exercise
        self.date = date
        self.completed = completed


class PracticeRepository:
    def __init__(self, sessions):
        self._sessions = list(sessions)

    def get_sessions_for(self, exercise):
        return [s for s in self._sessions if s.exercise is exercise]

    def get_sessions_for_name(self, exercise_name):
        return [s for s in self._sessions if s.exercise.name == exercise_name]

    def check_integrity(self, exercise):
        if exercise is None:
            return False
        sessions = self.get_sessions_for(exercise)
        for session in sessions:
            if session.exercise is not exercise:
                return False
            if session.exercise.name != exercise.name:
                return False
            if session.exercise.tempo != exercise.tempo:
                return False
            if session.exercise.duration != exercise.duration:
                return False
            if session.exercise.level != exercise.level:
                return False
        return True


def build_sessions_for_exercise(exercise, dates, completed_flags):
    sessions = []
    for idx, date in enumerate(dates):
        sessions.append(Session(exercise, date, completed_flags[idx]))
    return sessions


def main():
    exercise = GuitarExercise("Метроном", 90, 4, 1)
    dates = [datetime(2026, 1, 1), datetime(2026, 1, 2), datetime(2026, 1, 3)]
    completed = [True, False, True]

    sessions = build_sessions_for_exercise(exercise, dates, completed)
    repository = PracticeRepository(sessions)

    found = repository.get_sessions_for(exercise)
    print("Найдено занятий:", len(found))
    for session in found:
        print(session.date, session.completed)

    is_integrity = repository.check_integrity(exercise)
    print("Целостность связи:", is_integrity)


if __name__ == "__main__":
    main()
