import type { UnifiedMeeting } from "../types/meeting";

export function getMeetingTitle(meeting: UnifiedMeeting): string {
    return (
        meeting.crm?.title ??
        meeting.calendar?.title ??
        "Untitled Meeting"
    );
}

export function getCompany(meeting: UnifiedMeeting): string {
    return (
        meeting.crm?.client_company ??
        "—"
    );
}

export function getMeetingDate(meeting: UnifiedMeeting): string {

    const start =
        meeting.crm?.start ??
        meeting.calendar?.start;

    if (!start) {
        return "—";
    }

    return new Date(start).toLocaleString();
}

export function getSource(meeting: UnifiedMeeting): string {

    if (meeting.crm && meeting.calendar) {
        return "CRM + Calendar";
    }

    if (meeting.crm) {
        return "CRM Only";
    }

    return "Calendar Only";
}

export function getConflictCount(
    meeting: UnifiedMeeting
): number {

    return Object.keys(
        meeting.conflicts ?? {}
    ).length;
}