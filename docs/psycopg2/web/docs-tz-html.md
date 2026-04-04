# Source: https://www.psycopg.org/docs/tz.html

Title: psycopg2.tz – tzinfo implementations for Psycopg 2 — Psycopg 2.9.11 documentation

URL Source: https://www.psycopg.org/docs/tz.html

Markdown Content:
Deprecated since version 2.9: The module will be dropped in psycopg 2.10. Use [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "(in Python v3.14)") instead.

This module holds two different tzinfo implementations that can be used as the `tzinfo` argument to [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") constructors, directly passed to Psycopg functions or used to set the [`cursor.tzinfo_factory`](https://www.psycopg.org/docs/cursor.html#cursor.tzinfo_factory "cursor.tzinfo_factory") attribute in cursors.

_class_ psycopg2.tz.FixedOffsetTimezone(_offset=None_, _name=None_)[¶](https://www.psycopg.org/docs/tz.html#psycopg2.tz.FixedOffsetTimezone "Link to this definition")
Fixed offset in minutes east from UTC.

This is exactly the [implementation](https://docs.python.org/library/datetime.html) found in Python 2.3.x documentation, with a small change to the `__init__()` method to allow for pickling and a default name in the form `sHH:MM` (`s` is the sign.).

The implementation also caches instances. During creation, if a FixedOffsetTimezone instance has previously been created with the same offset and name that instance will be returned. This saves memory and improves comparability.

Changed in version 2.9: The constructor can take either a timedelta or a number of minutes of offset. Previously only minutes were supported.

_class_ psycopg2.tz.LocalTimezone[¶](https://www.psycopg.org/docs/tz.html#psycopg2.tz.LocalTimezone "Link to this definition")
Platform idea of local timezone.

This is the exact implementation from the Python 2.3 documentation.
