from app.models.meeting import meeting
from datetime import datetime
from app.utils.datetime_parser import parse_datetime, parse_iso_datetime


def normalize_crm(record: dict) -> meeting:
    pass


def normalize_calendar(record: dict) -> meeting:
    pass

    


def normalize_crm(record: dict) -> meeting:

    start = None

    if record["meeting_date"] and record["meeting_time"]:

        start = parse_datetime(
            record["meeting_date"],
            record["meeting_time"]
        )

    return meeting(
        source="crm",
        source_id=record["crm_id"],

        title=record["subject"],

        client_name=record["client_name"],
        client_company=record["client_company"],

        owner=record["relationship_owner"],

        start=start,

        location=record["location"],

        status=record["status"],

        notes=record["notes"]
    )

def normalize_calendar(record: dict) -> meeting:

    if record["start_time"]:
        start = parse_iso_datetime(
        record["start_time"]
        )

    return meeting(
        source="calendar",
        source_id=record["event_id"],

        title=record["title"],

        client_name=None,
        client_company=None,

        owner=record["organizer"],

        start=start,

        location=record["location"],

        status=record["status"],

        notes=record["description"]
    )