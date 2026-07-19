export interface Meeting {

    source: string;

    source_id: string;

    title: string;

    client_name?: string;

    client_company?: string;

    owner: string;

    start: string;

    location?: string;

    status: string;

    notes?: string;
}

export interface UnifiedMeeting {

    crm?: Meeting;

    calendar?: Meeting;

    match_score: number;

    conflicts: Record<
        string,
        {
            crm: string;
            calendar: string;
        }
    >;
}