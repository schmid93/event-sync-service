import type { UnifiedMeeting } from "../types/meeting";

export async function getMeetings(): Promise<UnifiedMeeting[]> {

    const response = await fetch(
        "http://127.0.0.1:8000/meetings"
    );

    if (!response.ok) {

        throw new Error("Unable to fetch meetings");

    }

    return response.json();
}