# Source: https://boltons.readthedocs.io/en/latest/timeutils.html

Title: datetime additions — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/timeutils.html

Markdown Content:
`timeutils` - `datetime` additions[](https://boltons.readthedocs.io/en/latest/timeutils.html#module-boltons.timeutils "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Python’s [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)") module provides some of the most complex and powerful primitives in the Python standard library. Time is nontrivial, but thankfully its support is first-class in Python. `dateutils` provides some additional tools for working with time.

Additionally, timeutils provides a few basic utilities for working with timezones in Python. The Python [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)") module’s documentation describes how to create a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")-compatible [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)") subtype. It even provides a few examples.

The following module defines usable forms of the timezones in those docs, as well as a couple other useful ones, [`UTC`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.UTC "boltons.timeutils.UTC") (aka GMT) and [`LocalTZ`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.LocalTZ "boltons.timeutils.LocalTZ") (representing the local timezone as configured in the operating system). For timezones beyond these, as well as a higher degree of accuracy in corner cases, check out [pytz](https://pypi.python.org/pypi/pytz) and [`dateutil`_](https://boltons.readthedocs.io/en/latest/timeutils.html#id5).

boltons.timeutils.daterange(_start_, _stop_, _step=1_, _inclusive=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#daterange)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.daterange "Link to this definition")
In the spirit of `range()` and `xrange()`, the daterange generator that yields a sequence of [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)") objects, starting at _start_, incrementing by _step_, until _stop_ is reached.

When _inclusive_ is True, the final date may be _stop_, **if**_step_ falls evenly on it. By default, _step_ is one day. See details below for many more details.

Parameters:
*   **start** ([_datetime.date_](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")) – The starting date The first value in the sequence.

*   **stop** ([_datetime.date_](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")) – The stopping date. By default not included in return. Can be None to yield an infinite sequence.

*   **step** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The value to increment _start_ by to reach _stop_. Can be an [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") number of days, a [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)"), or a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") of integers, (year, month, day). Positive and negative _step_ values are supported.

*   **inclusive** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether or not the _stop_ date can be returned. _stop_ is only returned when a _step_ falls evenly on it.

>>> christmas = date(year=2015, month=12, day=25)
>>> boxing_day = date(year=2015, month=12, day=26)
>>> new_year = date(year=2016, month=1,  day=1)
>>> for day in daterange(christmas, new_year):
...     print(repr(day))
datetime.date(2015, 12, 25)
datetime.date(2015, 12, 26)
datetime.date(2015, 12, 27)
datetime.date(2015, 12, 28)
datetime.date(2015, 12, 29)
datetime.date(2015, 12, 30)
datetime.date(2015, 12, 31)
>>> for day in daterange(christmas, boxing_day):
...     print(repr(day))
datetime.date(2015, 12, 25)
>>> for day in daterange(date(2017, 5, 1), date(2017, 8, 1),
...                      step=(0, 1, 0), inclusive=True):
...     print(repr(day))
datetime.date(2017, 5, 1)
datetime.date(2017, 6, 1)
datetime.date(2017, 7, 1)
datetime.date(2017, 8, 1)

_Be careful when using stop=None, as this will yield an infinite sequence of dates._

boltons.timeutils.isoparse(_iso\_str_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#isoparse)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.isoparse "Link to this definition")
Parses the limited subset of [ISO8601-formatted time](https://en.wikipedia.org/wiki/ISO_8601) strings as returned by [`datetime.datetime.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat "(in Python v3.14)").

>>> epoch_dt = datetime.fromtimestamp(0, timezone.utc).replace(tzinfo=None)
>>> iso_str = epoch_dt.isoformat()
>>> print(iso_str)
1970-01-01T00:00:00
>>> isoparse(iso_str)
datetime.datetime(1970, 1, 1, 0, 0)

>>> utcnow = datetime.now(timezone.utc).replace(tzinfo=None)
>>> utcnow == isoparse(utcnow.isoformat())
True

For further datetime parsing, see the [iso8601](https://pypi.python.org/pypi/iso8601) package for strict ISO parsing and [`dateutil`_](https://boltons.readthedocs.io/en/latest/timeutils.html#id7) package for loose parsing and more.

boltons.timeutils.parse_timedelta(_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#parse_timedelta)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.parse_timedelta "Link to this definition")
Robustly parses a short text description of a time period into a [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)"). Supports weeks, days, hours, minutes, and seconds, with or without decimal points:

Parameters:
**text** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Text to parse.

Returns:
datetime.timedelta

Raises:
[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – on parse failure.

>>> parse_td('1d 2h 3.5m 0s') == timedelta(days=1, seconds=7410)
True

Also supports full words and whitespace.

>>> parse_td('2 weeks 1 day') == timedelta(days=15)
True

Negative times are supported, too:

>>> parse_td('-1.5 weeks 3m 20s') == timedelta(days=-11, seconds=43400)
True

boltons.timeutils.strpdate(_string_, _format_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#strpdate)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.strpdate "Link to this definition")
Parse the date string according to the format in format. Returns a `date` object. Internally, `datetime.strptime()` is used to parse the string and thus conversion specifiers for time fields (e.g. %H) may be provided; these will be parsed but ignored.

Parameters:
*   **string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The date string to be parsed.

*   **format** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The [strptime](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior)-style date format string.

Returns:
datetime.date

>>> strpdate('2016-02-14', '%Y-%m-%d')
datetime.date(2016, 2, 14)
>>> strpdate('26/12 (2015)', '%d/%m (%Y)')
datetime.date(2015, 12, 26)
>>> strpdate('20151231 23:59:59', '%Y%m%d %H:%M:%S')
datetime.date(2015, 12, 31)
>>> strpdate('20160101 00:00:00.001', '%Y%m%d %H:%M:%S.%f')
datetime.date(2016, 1, 1)

boltons.timeutils.total_seconds()[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.total_seconds "Link to this definition")
Total seconds in the duration.

boltons.timeutils.dt_to_timestamp(_dt_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#dt_to_timestamp)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.dt_to_timestamp "Link to this definition")
Converts from a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") object to an integer timestamp, suitable interoperation with [`time.time()`](https://docs.python.org/3/library/time.html#time.time "(in Python v3.14)") and other Epoch-based timestamps.

>>> timestamp = int(time.time())
>>> utc_dt = datetime.fromtimestamp(timestamp, timezone.utc)
>>> timestamp - dt_to_timestamp(utc_dt)
0.0

`dt_to_timestamp` supports both timezone-aware and naïve [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") objects. Note that it assumes naïve datetime objects are implied UTC, such as those generated with [`datetime.datetime.utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "(in Python v3.14)"). If your datetime objects are local time, such as those generated with [`datetime.datetime.now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "(in Python v3.14)"), first convert it using the [`datetime.datetime.replace()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.replace "(in Python v3.14)") method with `tzinfo=`[`LocalTZ`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.LocalTZ "boltons.timeutils.LocalTZ") object in this module, then pass the result of that to `dt_to_timestamp`.

boltons.timeutils.relative_time(_d_, _other=None_, _ndigits=0_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#relative_time)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.relative_time "Link to this definition")
Get a string representation of the difference between two [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") objects or one [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") and the current time. Handles past and future times.

Parameters:
*   **d** (_datetime_) – The first datetime object.

*   **other** (_datetime_) – An optional second datetime object. If unset, defaults to the current time as determined `datetime.utcnow()`.

*   **ndigits** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The number of decimal digits to round to, defaults to `0`.

Returns:
A short English-language string.

>>> now = datetime.now(timezone.utc).replace(tzinfo=None)
>>> relative_time(now, ndigits=1)
'0 seconds ago'
>>> relative_time(now - timedelta(days=1, seconds=36000), ndigits=1)
'1.4 days ago'
>>> relative_time(now + timedelta(days=7), now, ndigits=1)
'1 week from now'

boltons.timeutils.decimal_relative_time(_d_, _other=None_, _ndigits=0_, _cardinalize=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#decimal_relative_time)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.decimal_relative_time "Link to this definition")
Get a tuple representing the relative time difference between two [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") objects or one [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") and now.

Parameters:
*   **d** (_datetime_) – The first datetime object.

*   **other** (_datetime_) – An optional second datetime object. If unset, defaults to the current time as determined `datetime.utcnow()`.

*   **ndigits** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The number of decimal digits to round to, defaults to `0`.

*   **cardinalize** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to pluralize the time unit if appropriate, defaults to `True`.

Returns:A tuple of the [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") difference and
respective unit of time, pluralized if appropriate and _cardinalize_ is set to `True`.

Return type:
([float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"))

Unlike [`relative_time()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.relative_time "boltons.timeutils.relative_time"), this method’s return is amenable to localization into other languages and custom phrasing and formatting.

>>> now = datetime.now(timezone.utc).replace(tzinfo=None)
>>> decimal_relative_time(now - timedelta(days=1, seconds=3600), now)
(1.0, 'day')
>>> decimal_relative_time(now - timedelta(seconds=0.002), now, ndigits=5)
(0.002, 'seconds')
>>> decimal_relative_time(now, now - timedelta(days=900), ndigits=1)
(-2.5, 'years')

General timezones[](https://boltons.readthedocs.io/en/latest/timeutils.html#general-timezones "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

By default, [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") objects are “naïve”, meaning they lack attached timezone information. These objects can be useful for many operations, but many operations require timezone-aware datetimes.

The two most important timezones in programming are Coordinated Universal Time ([UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)) and the local timezone of the host running your code. Boltons provides two [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)") subtypes for working with them:

Note

These days, Python has a [built-in UTC](https://docs.python.org/3/library/datetime.html#datetime.timezone.utc), and the UTC tzinfo here, while equivalent, is just for backwards compat.

timeutils.UTC _=ConstantTZInfo(name='UTC',offset=datetime.timedelta(0))_[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.UTC "Link to this definition")boltons.timeutils.LocalTZ _=LocalTZInfo()_[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.LocalTZ "Link to this definition")
The `LocalTZInfo` type takes data available in the time module about the local timezone and makes a practical [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)") to represent the timezone settings of the operating system.

For a more in-depth integration with the operating system, check out [tzlocal](https://pypi.python.org/pypi/tzlocal). It builds on [pytz](https://pypi.python.org/pypi/pytz) and implements heuristics for many versions of major operating systems to provide the official `pytz` tzinfo, instead of the LocalTZ generalization.

_class_ boltons.timeutils.ConstantTZInfo(_name='ConstantTZ'_, _offset=datetime.timedelta(0)_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#ConstantTZInfo)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.ConstantTZInfo "Link to this definition")
A [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)") subtype whose _offset_ remains constant (no daylight savings).

Parameters:
*   **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the timezone.

*   **offset** ([_datetime.timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")) – Offset of the timezone.

US timezones[](https://boltons.readthedocs.io/en/latest/timeutils.html#us-timezones "Link to this heading")
------------------------------------------------------------------------------------------------------------

These four US timezones were implemented in the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)") documentation and have been reproduced here in boltons for convenience. More in-depth support is provided by [`dateutil`_](https://boltons.readthedocs.io/en/latest/timeutils.html#id9) and [pytz](https://pypi.python.org/pypi/pytz).

timeutils.Eastern _=Eastern_[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Eastern "Link to this definition")timeutils.Central _=Central_[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Central "Link to this definition")timeutils.Mountain _=Mountain_[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Mountain "Link to this definition")timeutils.Pacific _=Pacific_[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Pacific "Link to this definition")_class_ boltons.timeutils.USTimeZone(_hours_, _reprname_, _stdname_, _dstname_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/timeutils.html#USTimeZone)[](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.USTimeZone "Link to this definition")
Copied directly from the Python docs, the `USTimeZone` is a [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)") subtype used to create the [`Eastern`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Eastern "boltons.timeutils.Eastern"), [`Central`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Central "boltons.timeutils.Central"), [`Mountain`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Mountain "boltons.timeutils.Mountain"), and [`Pacific`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.Pacific "boltons.timeutils.Pacific") tzinfo types.
