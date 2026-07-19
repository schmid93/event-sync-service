from fastapi import FastAPI

from app.services.loader import (
    load_calendar_events,
    load_crm_events
)

from app.services.normalizer import (
    normalize_calendar,
    normalize_crm
)

app = FastAPI()


@app.get("/meetings/raw")
def meetings():

    crm = [
        normalize_crm(record)
        for record in load_crm_events()
    ]

    calendar = [
        normalize_calendar(record)
        for record in load_calendar_events()
    ]

    return {
        "crm": crm,
        "calendar": calendar
    }