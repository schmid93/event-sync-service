import type { UnifiedMeeting } from "../types/meeting";

import ConflictBadge from "./conflictBadge";
import MeetingDetails from "./meetingDetails";

import {
    getCompany,
    getConflictCount,
    getMeetingDate,
    getMeetingTitle,
    getSource,
} from "../utils/meetingHelpers";

type Props = {

    meeting: UnifiedMeeting;

    expanded: boolean;

    onToggle: () => void;

};

export default function MeetingRow({

    meeting,

    expanded,

    onToggle,

}: Props) {

    return (

        <>

            <tr

                onClick={onToggle}

                style={{
                    cursor: "pointer",
                    backgroundColor: expanded ? "#2b2b2b" : "transparent",
                    transition: "background-color 0.2s ease",
                    }}

            >

                <td>

                    {

                        expanded

                            ? "▼"

                            : "▶"

                    }

                </td>

                <td>

                    {getMeetingTitle(meeting)}

                </td>

                <td>

                    {getCompany(meeting)}

                </td>

                <td>

                    {getMeetingDate(meeting)}

                </td>

                <td>

                    {getSource(meeting)}

                </td>

                <td>

                    {meeting.match_score}

                </td>

                <td>

                    <ConflictBadge

                        conflicts={

                            getConflictCount(meeting)

                        }

                    />

                </td>

            </tr>

            {

                expanded && (

                    <tr>

                        <td

                            colSpan={7}

                            style={{

                                padding: "1rem",

                                backgroundColor: "#1f1f1f",

                            }}

                        >

                            <MeetingDetails

                                meeting={meeting}

                            />

                        </td>

                    </tr>

                )

            }

        </>

    );

}