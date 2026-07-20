import type { UnifiedMeeting } from "../types/meeting";

type Props = {

    meeting: UnifiedMeeting;

};

function renderValue(value?: string) {

    return value || "Not available";

}

export default function MeetingDetails({

    meeting,

}: Props) {

    const crm = meeting.crm;

    const calendar = meeting.calendar;

    return (

        <div
            style={{
                marginTop: "2rem",
                border: "1px solid #ddd",
                padding: "1.5rem",
                borderRadius: "8px",
            }}
        >

            <h2>

                Meeting Details

            </h2>

            <div
                style={{
                    display: "flex",
                    gap: "3rem",
                }}
            >

                <div
                    style={{
                        flex: 1,
                    }}
                >

                    <h3>

                        CRM

                    </h3>

                    {

                        crm ? (

                            <>

                                <p>

                                    <strong>Title:</strong>{" "}

                                    {renderValue(crm.title)}

                                </p>

                                <p>

                                    <strong>Owner:</strong>{" "}

                                    {renderValue(crm.owner)}

                                </p>

                                <p>

                                    <strong>Company:</strong>{" "}

                                    {renderValue(crm.client_company)}

                                </p>

                                <p>

                                    <strong>Location:</strong>{" "}

                                    {renderValue(crm.location)}

                                </p>

                                <p>

                                    <strong>Status:</strong>{" "}

                                    {renderValue(crm.status)}

                                </p>

                                <p>

                                    <strong>Notes:</strong>{" "}

                                    {renderValue(crm.notes)}

                                </p>

                            </>

                        ) : (

                            <p>

                                No CRM record.

                            </p>

                        )

                    }

                </div>

                <div
                    style={{
                        flex: 1,
                    }}
                >

                    <h3>

                        Calendar

                    </h3>

                    {

                        calendar ? (

                            <>

                                <p>

                                    <strong>Title:</strong>{" "}

                                    {renderValue(calendar.title)}

                                </p>

                                <p>

                                    <strong>Owner:</strong>{" "}

                                    {renderValue(calendar.owner)}

                                </p>

                                <p>

                                    <strong>Location:</strong>{" "}

                                    {renderValue(calendar.location)}

                                </p>

                                <p>

                                    <strong>Status:</strong>{" "}

                                    {renderValue(calendar.status)}

                                </p>

                                <p>

                                    <strong>Description:</strong>{" "}

                                    {renderValue(calendar.notes)}

                                </p>

                            </>

                        ) : (

                            <p>

                                No Calendar record.

                            </p>

                        )

                    }

                </div>

            </div>

            <hr />

            <h3>

                Detected Conflicts

            </h3>

            {

                Object.keys(meeting.conflicts).length === 0

                ? (

                    <p>

                        ✅ No conflicts detected.

                    </p>

                )

                : (

                    Object.entries(meeting.conflicts).map(

                        ([field, values]) => (

                            <div
                                key={field}
                                style={{
                                    marginBottom: "1rem",
                                }}
                            >

                                <strong>

                                    ⚠ {field}

                                </strong>

                                <p>

                                    CRM:

                                    {" "}

                                    {values.crm}

                                </p>

                                <p>

                                    Calendar:

                                    {" "}

                                    {values.calendar}

                                </p>

                            </div>

                        )

                    )

                )

            }

        </div>

    );

}