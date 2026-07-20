
import MeetingTable from "./components/meetingTable";


import { useMeetings } from "./hooks/useMeeting";


function App() {

    const {

        meetings,

        loading,

    } = useMeetings();

    if (loading) {

        return <h2>Loading...</h2>;

    }

    return (

        <div style={{ padding: "2rem" }}>

            <h1>

                Event Sync Service

            </h1>

            <MeetingTable

                meetings={meetings}

            />

        </div>

    );

}

export default App;