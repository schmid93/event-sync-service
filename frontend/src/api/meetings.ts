import type { UnifiedMeeting } from "../types/meeting";

export async function getMeetings(): Promise<UnifiedMeeting[]> {

    const response = await fetch(
        "http://localhost:8000/meetings"
    );

    if (!response.ok) {

        throw new Error("Unable to fetch meetings");

    }

    return response.json();
}