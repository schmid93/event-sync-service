from __future__ import annotations
from datetime import datetime, timedelta

from app.models.meeting import Meeting

# ---------------------------------------------------------------------
# Matching configuration
# ---------------------------------------------------------------------

SAME_DAY_SCORE = 30
SAME_TIME_SCORE = 25
SAME_OWNER_SCORE = 15
SAME_COMPANY_SCORE = 30

MATCH_THRESHOLD = 70


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def _to_naive(dt: datetime | None) -> datetime | None:
    """
    Convert timezone-aware datetimes into naive datetimes so they can
    be safely compared with naive datetimes.

    If the datetime is already naive or None, it is returned unchanged.
    """
    if dt is None:
        return None

    if dt.tzinfo is not None:
        return dt.replace(tzinfo=None)

    return dt


def _normalize_owner(owner: str) -> str:
    """
    Normalize owner names.

    Examples

    "Sarah Chen"
        -> "sarah chen"

    "sarah.chen@company.com"
        -> "sarah chen"
    """

    owner = owner.lower().strip()

    if "@" in owner:
        local = owner.split("@")[0]
        owner = local.replace(".", " ")

    return owner


# ---------------------------------------------------------------------
# Matching rules
# ---------------------------------------------------------------------

def same_day(crm: Meeting, calendar: Meeting) -> bool:
    """
    True if both meetings occur on the same calendar day.
    """

    crm_date = _to_naive(crm.start)
    calendar_date = _to_naive(calendar.start)

    if crm_date is None or calendar_date is None:
        return False

    return crm_date.date() == calendar_date.date()


def similar_time(
    crm: Meeting,
    calendar: Meeting,
    tolerance_minutes: int = 30,
) -> bool:
    """
    True if the meeting start times differ by no more than
    `tolerance_minutes`.
    """

    crm_date = _to_naive(crm.start)
    calendar_date = _to_naive(calendar.start)

    if crm_date is None or calendar_date is None:
        return False

    difference = abs(crm_date - calendar_date)

    return difference <= timedelta(minutes=tolerance_minutes)


def same_owner(crm: Meeting, calendar: Meeting) -> bool:
    """
    True if both records appear to refer to the same meeting owner.

    CRM stores a person's full name while Calendar stores an email.
    """

    if not crm.owner or not calendar.owner:
        return False

    return (
        _normalize_owner(crm.owner)
        ==
        _normalize_owner(calendar.owner)
    )


def company_matches(crm: Meeting, calendar: Meeting) -> bool:
    """
    Returns True when the CRM company name appears in the
    calendar title.

    This is intentionally a simple substring-based approach.
    It can later be replaced with fuzzy matching if needed.
    """

    if not crm.client_company:
        return False

    company = crm.client_company.lower().strip()
    title = (calendar.title or "").lower()

    if company in title:
        return True

    words = company.split()

    if not words:
        return False

    first_word = words[0]

    if len(first_word) > 3 and first_word in title:
        return True

    return False


# ---------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------

def calculate_match_score(
    crm: Meeting,
    calendar: Meeting,
) -> int:
    """
    Calculates a similarity score between two meetings.

    Maximum score: 100

        +30 Same day
        +25 Similar time
        +15 Same owner
        +30 Company mentioned in calendar title
    """

    score = 0

    if same_day(crm, calendar):
        score += SAME_DAY_SCORE

    if similar_time(crm, calendar):
        score += SAME_TIME_SCORE

    if same_owner(crm, calendar):
        score += SAME_OWNER_SCORE

    if company_matches(crm, calendar):
        score += SAME_COMPANY_SCORE

    return score


def is_match(
    crm: Meeting,
    calendar: Meeting,
) -> bool:
    """
    Returns True when the similarity score exceeds the
    configured threshold.
    """

    return calculate_match_score(
        crm,
        calendar,
    ) >= MATCH_THRESHOLD