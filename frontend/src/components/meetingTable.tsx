import { useState } from "react";

import type { UnifiedMeeting } from "../types/meeting";

import MeetingRow from "./meetingRow";

type Props = {
    meetings: UnifiedMeeting[];
};

export default function MeetingTable({
    meetings,
}: Props) {

    const [expandedId, setExpandedId] = useState<string | null>(null);

    const getMeetingId = (meeting: UnifiedMeeting) =>
        meeting.crm?.source_id ??
        meeting.calendar?.source_id ??
        "";

    const toggleMeeting = (id: string) => {

        setExpandedId(current =>
            current === id ? null : id
        );

    };

    return (

        <table
            style={{
                width: "100%",
                borderCollapse: "collapse",
            }}
        >

            <thead>

                <tr>

                    <th></th>

                    <th>Title</th>

                    <th>Company</th>

                    <th>Date</th>

                    <th>Source</th>

                    <th>Score</th>

                    <th>Conflicts</th>

                </tr>

            </thead>

            <tbody>

                {

                    meetings.map(meeting => {

                        const id = getMeetingId(meeting);

                        return (

                            <MeetingRow

                                key={id}

                                meeting={meeting}

                                expanded={expandedId === id}

                                onToggle={() => toggleMeeting(id)}

                            />

                        );

                    })

                }

            </tbody>

        </table>

    );

}