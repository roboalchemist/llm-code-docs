# Source: https://typer.tiangolo.com/tutorial/parameter-types/datetime/

# DateTime[¶](#datetime "Permanent link")

You can specify a *CLI parameter* as a Python [`datetime`](https://docs.python.org/3/library/datetime.html).

Your function will receive a standard Python `datetime` object, and again, your editor will give you completion, etc.

Python 3.9+

Typer will accept any string from the following formats:

-   `%Y-%m-%d`
-   `%Y-%m-%dT%H:%M:%S`
-   `%Y-%m-%d %H:%M:%S`

Check it:

    $ python main.py --help

    Usage: main.py [OPTIONS] BIRTH:[%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]

    Arguments:
      BIRTH:[%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S][required]

    Options:
      --help                Show this message and exit.

    // Pass a datetime
    $ python main.py 1956-01-31T10:00:00

    Interesting day to be born: 1956-01-31 10:00:00
    Birth hour: 10

    // An invalid date
    $ python main.py july-19-1989

    Usage: main.py [OPTIONS] [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d%H:%M:%S]

    Error: Invalid value for 'BIRTH:[%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]': 'july-19-1989' does not match the formats '%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S'.

## Custom date format[¶](#custom-date-format "Permanent link")

You can also customize the formats received for the `datetime` with the `formats` parameter.

`formats` receives a list of strings with the date formats that would be passed to [datetime.strptime()](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime).

For example, let\'s imagine that you want to accept an ISO formatted datetime, but for some strange reason, you also want to accept a format with:

-   first the month
-   then the day
-   then the year
-   separated with \"`/`\"

\...It\'s a crazy example, but let\'s say you also needed that strange format:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    from datetime import datetime

    import typer

    app = typer.Typer()

    @app.command()
    def main(
        launch_date: datetime = typer.Argument(
            ..., formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"]
        ),
    ):
        print(f"Launch will be at: ")

    if __name__ == "__main__":
        app()

Tip

Notice the last string in `formats`: `"%m/%d/%Y"`.

Check it:

    // ISO dates work
    $ python main.py 1969-10-29

    Launch will be at: 1969-10-29 00:00:00

    // But the strange custom format also works
    $ python main.py 10/29/1969

    Launch will be at: 1969-10-29 00:00:00