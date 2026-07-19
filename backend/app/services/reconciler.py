from typing import List, Set

from app.models.meeting import Meeting
from app.models.unified_meeting import UnifiedMeeting
from app.services.matcher import (
    calculate_match_score,
    MATCH_THRESHOLD,
)


class Reconciler:
    """
    Reconciles CRM and Calendar meetings into a unified list.

    Strategy (Greedy Matching):

    """

    def reconcile(
        self,
        crm_meetings: List[Meeting],      
        calendar_meetings: List[Meeting], 
    ) -> List[UnifiedMeeting]:            
        unified: List[UnifiedMeeting] = []          
        used_calendar_ids: Set[str] = set()

        for crm in crm_meetings:

            best_match = None
            best_score = 0

            for calendar in calendar_meetings:

                if calendar.source_id in used_calendar_ids:
                    continue

                score = calculate_match_score(crm, calendar)

                if score > best_score:
                    best_score = score
                    best_match = calendar

            # Match found
            if (
                best_match is not None
                and best_score >= MATCH_THRESHOLD
            ):

                used_calendar_ids.add(best_match.source_id)

                unified.append(
                    UnifiedMeeting(
                        crm=crm,
                        calendar=best_match,
                        match_score=best_score,
                    )
                )

            # CRM only
            else:

                unified.append(
                    UnifiedMeeting(
                        crm=crm,
                        calendar=None,
                        match_score=0,
                    )
                )

        # Remaining Calendar meetings
        for calendar in calendar_meetings:

            if calendar.source_id in used_calendar_ids:
                continue

            unified.append(
                UnifiedMeeting(
                    crm=None,
                    calendar=calendar,
                    match_score=0,
                )
            )

        return unified