import { useEffect, useState } from "react";

import type { UnifiedMeeting } from "../types/meeting";

import { getMeetings } from "../api/meetings";

export function useMeetings() {

    const [meetings, setMeetings] = useState<UnifiedMeeting[]>([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        getMeetings()

            .then(setMeetings)

            .finally(() => setLoading(false));

    }, []);

    return {

        meetings,

        loading,

    };

}