from pathlib import Path
import json


DATA_DIR = Path(__file__).parent.parent / "data"


def load_json(filename: str):
    try:
        file_path = DATA_DIR / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        raise DataLoadingError(
            f"Unable to load {filename}"
        ) from e


def load_crm_events():
    return load_json("crm_events.json")


def load_calendar_events():
    return load_json("calendar_events.json")

    
class DataLoadingError(Exception):
    pass