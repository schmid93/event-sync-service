from app.models.meeting import Meeting
from datetime import datetime
from app.utils.datetime_parser import parse_datetime, parse_iso_datetime


def normalize_crm(record: dict) -> Meeting:
    pass


def normalize_calendar(record: dict) -> Meeting:
    pass

    


def normalize_crm(record: dict) -> Meeting:

    start = None

    if record["meeting_date"] and record["meeting_time"]:

        start = parse_datetime(
            record["meeting_date"],
            record["meeting_time"]
        )

    return Meeting(
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

def normalize_calendar(record: dict) -> Meeting:

    if record["start_time"]:
        start = parse_iso_datetime(
        record["start_time"]
        )

    return Meeting(
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