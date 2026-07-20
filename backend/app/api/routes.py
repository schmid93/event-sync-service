from fastapi import APIRouter

from app.services.loader import (
    load_calendar_events,
    load_crm_events,
)

from app.services.normalizer import (
    normalize_calendar,
    normalize_crm,
)

from app.services.reconciler import Reconciler

router = APIRouter()

reconciler = Reconciler()


@router.get("/health")
def health():

    return {
        "status": "ok"
    }


@router.get("/meetings")
def get_meetings():

    crm_meetings = [
        normalize_crm(record)
        for record in load_crm_events()
    ]

    calendar_meetings = [
        normalize_calendar(record)
        for record in load_calendar_events()
    ]

    unified = reconciler.reconcile(
        crm_meetings,
        calendar_meetings,
    )

    unified.sort(
    key=lambda meeting: len(meeting.conflicts),
    reverse=True,
)

    return unified