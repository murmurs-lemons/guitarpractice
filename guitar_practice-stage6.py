# === Stage 6: Связанная сущность ===
# Project: GuitarPractice
from datetime import datetime
from typing import List, Dict, Any


class Session:
    def __init__(self, title: str, date: datetime = None):
        self.id = None
        self.title = title
        self.date = date or datetime.now()
        self.exercise_ids: List[str] = []

    def add_exercise(self, exercise_id: str) -> bool:
        if exercise_id in self.exercise_ids:
            return False
        self.exercise_ids.append(exercise_id)
        return True

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.isoformat(),
            'exercise_ids': list(self.exercise_ids),
        }


class SessionManager:
    def __init__(self):
        self._sessions: List[Session] = []
        self._counter = 0

    def add_session(self, title: str, exercise_ids: List[str] = None) -> Session:
        session = Session(title)
        for exercise_id in exercise_ids or []:
            session.add_exercise(exercise_id)
        self._sessions.append(session)
        self._counter += 1
        session.id = str(self._counter)
        return session

    def get_sessions(self) -> List[Session]:
        return list(self._sessions)
