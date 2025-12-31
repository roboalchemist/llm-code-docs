# Source: https://rich.readthedocs.io/en/latest/live.html

[]

# Live Display[](#live-display "Link to this heading")

Progress bars and status indicators use a *live* display to animate parts of the terminal. You can build custom live displays with the [[`Live`]](reference/live.html#rich.live.Live "rich.live.Live") class.

For a demonstration of a live display, run the following command:

    python -m rich.live

Note

If you see ellipsis "...", this indicates that the terminal is not tall enough to show the full table.

## Basic usage[](#basic-usage "Link to this heading")

To create a live display, construct a [[`Live`]](reference/live.html#rich.live.Live "rich.live.Live") object with a renderable and use it as a context manager. The live display will persist for the duration of the context. You can update the renderable to update the display:

    import time

    from rich.live import Live
    from rich.table import Table

    table = Table()
    table.add_column("Row ID")
    table.add_column("Description")
    table.add_column("Level")

    with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
        for row in range(12):
            time.sleep(0.4)  # arbitrary delay
            # update the renderable internally
            table.add_row(f"", f"description ", "[red]ERROR")