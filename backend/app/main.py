from fastapi import FastAPI

from app.services.loader import (
    load_calendar_events,
    load_crm_events
)

from app.services.normalizer import (
    normalize_calendar,
    normalize_crm
)

from app.services.reconciler import Reconciler

app = FastAPI()


@app.get("/meetings")
def meetings():

    crm = [
        normalize_crm(record)
        for record in load_crm_events()
    ]

    calendar = [
        normalize_calendar(record)
        for record in load_calendar_events()
    ]

    reconciler = Reconciler()

    return reconciler.reconcile(
        crm,
        calendar,
    )