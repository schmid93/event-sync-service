from datetime import timedelta

from app.models.unified_meeting import UnifiedMeeting


TIME_TOLERANCE_MINUTES = 15


class ConflictDetector:
    """
    Detects conflicts between CRM and Calendar records.
    """

    def detect(self, meeting: UnifiedMeeting) -> dict:

        conflicts = {}

        if meeting.crm is None or meeting.calendar is None:
            return conflicts

        self._compare_location(meeting, conflicts)
        self._compare_status(meeting, conflicts)
        self._compare_start_time(meeting, conflicts)

        return conflicts

    def _compare_location(
        self,
        meeting: UnifiedMeeting,
        conflicts: dict,
    ) -> None:

        crm_location = meeting.crm.location
        calendar_location = meeting.calendar.location

        if (
            crm_location
            and calendar_location
            and crm_location != calendar_location
        ):

            conflicts["location"] = {
                "crm": crm_location,
                "calendar": calendar_location,
            }

    def _compare_status(
        self,
        meeting: UnifiedMeeting,
        conflicts: dict,
    ) -> None:

        crm_status = meeting.crm.status
        calendar_status = meeting.calendar.status

        if (
            crm_status
            and calendar_status
            and crm_status != calendar_status
        ):

            conflicts["status"] = {
                "crm": crm_status,
                "calendar": calendar_status,
            }

    def _compare_start_time(
        self,
        meeting: UnifiedMeeting,
        conflicts: dict,
    ) -> None:

        crm_start = meeting.crm.start
        calendar_start = meeting.calendar.start

        if crm_start is None or calendar_start is None:
            return

        crm_start = self._to_naive(crm_start)
        calendar_start = self._to_naive(calendar_start)

        difference = abs(crm_start - calendar_start)

        if difference > timedelta(minutes=TIME_TOLERANCE_MINUTES):

            conflicts["start_time"] = {
                "crm": crm_start.isoformat(),
                "calendar": calendar_start.isoformat(),
            }

    @staticmethod
    def _to_naive(dt):

        if dt.tzinfo is not None:
            return dt.replace(tzinfo=None)

        return dt