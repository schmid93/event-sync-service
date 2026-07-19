from datetime import datetime


DATETIME_FORMATS = [

    "%Y-%m-%d %H:%M",

    "%m-%d/%Y %H:%M"

]


def parse_datetime(date: str, time: str):

    combined = f"{date} {time}"

    for fmt in DATETIME_FORMATS:

        try:
            return datetime.strptime(combined, fmt)

        except ValueError:
            pass

    raise ValueError(
        f"Unsupported datetime: {combined}"
    )

def parse_iso_datetime(date_string: str) -> datetime:
    return datetime.fromisoformat(
        date_string.replace("Z", "+00:00")
    )