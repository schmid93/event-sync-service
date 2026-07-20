type Props = {

    conflicts: number;

};

export default function ConflictBadge({

    conflicts,

}: Props) {

    if (conflicts === 0)

        return <span>✅ None</span>;

    return (

        <span>

            ⚠ {conflicts}

        </span>

    );

}