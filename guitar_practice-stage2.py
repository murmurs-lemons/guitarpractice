# === Stage 2: Проверка полей ===
# Project: GuitarPractice
from datetime import timedelta


def normalize_input(raw):
    if isinstance(raw, (int, float)) and isinstance(raw, str) is False:
        raise ValueError("введите значение в текстовом формате")
    text = str(raw).strip().lower()
    return text


def validate_name(raw):
    name = normalize_input(raw)
    if not name:
        raise ValueError("название не может быть пустым")
    if len(name) > 50:
        raise ValueError("название слишком длинное, не более 50 символов")
    if not name.replace(" ", "").replace("-", "").isalnum():
        raise ValueError("название может содержать только буквы, цифры, пробелы и дефисы")
    return name


def validate_tempo(raw):
    tempo = normalize_input(raw)
    if not tempo.isdigit():
        raise ValueError("темп должен быть целым положительным числом")
    tempo = int(tempo)
    if tempo < 30:
        raise ValueError("темп слишком мал, минимум 30 ударов в минуту")
    if tempo > 240:
        raise ValueError("темп слишком велик, максимум 240 ударов в минуту")
    return tempo


def validate_duration(raw):
    duration = normalize_input(raw)
    if duration not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        raise ValueError("длительность должна быть одной из 1, 2, 3, 4, 5, 6, 7 или 8 тактов")
    return int(duration)


def validate_level(raw):
    level = normalize_input(raw)
    if level not in ("beginner", "intermediate", "advanced"):
        raise ValueError("уровень должен быть одним из beginner, intermediate или advanced")
    return level


def validate_exercise(raw):
    if raw is None:
        raise ValueError("упражнение не может быть пустым")
    data = {
        "name": validate_name(raw.get("name")),
        "tempo": validate_tempo(raw.get("tempo")),
        "duration": validate_duration(raw.get("duration")),
        "level": validate_level(raw.get("level")),
    }
    return data


def format_duration_ticks(ticks):
    seconds = int(ticks / 4)
    minutes, remainder = divmod(seconds, 60)
    if minutes > 0:
        return f"{minutes} мин {remainder} сек"
    return f"{remainder} сек"


def build_exercise_summary(data):
    return (
        f"Упражнение «{data['name']}» — {data['level']}, {data['tempo']} BPM, "
        f"длительность {format_duration_ticks(data['duration'])}"
    )


def parse_exercise(raw):
    try:
        return validate_exercise(raw)
    except ValueError as error:
        raise error
