# Source: https://dateparser.readthedocs.io/en/latest/

Title: dateparser – python parser for human readable dates — DateParser 1.3.0 documentation

URL Source: https://dateparser.readthedocs.io/en/latest/

Published Time: Wed, 04 Feb 2026 16:00:02 GMT

Markdown Content:
[![Image 1: pypi downloads](https://img.shields.io/pypi/dm/dateparser)](https://pypi.python.org/pypi/dateparser)[![Image 2: pypi version](https://img.shields.io/pypi/v/dateparser.svg)](https://pypi.python.org/pypi/dateparser)[![Image 3: Code Coverage](https://codecov.io/gh/scrapinghub/dateparser/branch/master/graph/badge.svg)](https://codecov.io/gh/scrapinghub/dateparser)[![Image 4: Github Build](https://github.com/scrapinghub/dateparser/workflows/Build/badge.svg)](https://github.com/scrapinghub/dateparser/actions)[![Image 5: Documentation Status](https://readthedocs.org/projects/dateparser/badge/?version=latest)](http://dateparser.readthedocs.org/en/latest/?badge=latest)
dateparser provides modules to easily parse localized dates in almost any string formats commonly found on web pages.

Documentation[](https://dateparser.readthedocs.io/en/latest/#documentation "Link to this heading")
---------------------------------------------------------------------------------------------------

This documentation is built automatically and can be found on [Read the Docs](https://dateparser.readthedocs.org/en/latest/).

Introduction to dateparser[](https://dateparser.readthedocs.io/en/latest/#introduction-to-dateparser "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

Features[](https://dateparser.readthedocs.io/en/latest/#features "Link to this heading")
-----------------------------------------------------------------------------------------

* Generic parsing of dates in over 200 language locales plus numerous formats in a language agnostic fashion.

* Generic parsing of relative dates like: `'1 min ago'`, `'2 weeks ago'`, `'3 months, 1 week and 1 day ago'`, `'in 2 days'`, `'tomorrow'`.

* Generic parsing of dates with time zones abbreviations or UTC offsets like: `'August 14, 2015 EST'`, `'July 4, 2013 PST'`, `'21 July 2013 10:15 pm +0500'`.

* Date lookup in longer texts.

* Support for non-Gregorian calendar systems. See [Supported Calendars](https://dateparser.readthedocs.io/en/latest/#supported-calendars).

* Extensive test coverage.

Basic Usage[](https://dateparser.readthedocs.io/en/latest/#basic-usage "Link to this heading")
-----------------------------------------------------------------------------------------------

The most straightforward way is to use the [dateparser.parse](https://dateparser.readthedocs.io/en/latest/#dateparser.parse) function, that wraps around most of the functionality in the module.

dateparser.parse[_date\_string_, _date\_formats=None_, _languages=None_, _locales=None_, _region=None_, _settings=None_, _detect\_languages\_function=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser.html#parse)
Parse date and time from given date string.

Parameters:

* **date_string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string representing date and/or time in a recognizably valid format.

* **date_formats** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of format strings using directives as given [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior). The parser applies formats one by one, taking into account the detected languages/locales.

* **languages** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of language codes, e.g. [‘en’, ‘es’, ‘zh-Hant’]. If locales are not given, languages and region are used to construct locales for translation.

* **locales** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of locale codes, e.g. [‘fr-PF’, ‘qu-EC’, ‘af-NA’]. The parser uses only these locales to translate date string.

* **region** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A region code, e.g. ‘IN’, ‘001’, ‘NE’. If locales are not given, languages and region are used to construct locales for translation.

* **settings** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Configure customized behavior using settings defined in [`dateparser.conf.Settings`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings "dateparser.conf.Settings").

* **detect_languages_function** (_function_) – A function for language detection that takes as input a string (the date_string) and a confidence_threshold, and returns a list of detected language codes. Note: this function is only used if `languages` and `locales` are not provided.

Returns:
Returns [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") representing parsed date if successful, else returns None

Return type:
[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)").

Raises:
`ValueError`: Unknown Language, `TypeError`: Languages argument must be a list, `SettingValidationError`: A provided setting is not valid.

### Popular Formats[](https://dateparser.readthedocs.io/en/latest/#popular-formats "Link to this heading")

>>> import dateparser
>>> dateparser.parse('12/12/12')
datetime.datetime(2012, 12, 12, 0, 0)
>>> dateparser.parse('Fri, 12 Dec 2014 10:55:50')
datetime.datetime(2014, 12, 12, 10, 55, 50)
>>> dateparser.parse('Martes 21 de Octubre de 2014')  # Spanish (Tuesday 21 October 2014)
datetime.datetime(2014, 10, 21, 0, 0)
>>> dateparser.parse('Le 11 Décembre 2014 à 09:00')  # French (11 December 2014 at 09:00)
datetime.datetime(2014, 12, 11, 9, 0)
>>> dateparser.parse('13 января 2015 г. в 13:34')  # Russian (13 January 2015 at 13:34)
datetime.datetime(2015, 1, 13, 13, 34)
>>> dateparser.parse('1 เดือนตุลาคม 2005, 1:00 AM')  # Thai (1 October 2005, 1:00 AM)
datetime.datetime(2005, 10, 1, 1, 0)

This will try to parse a date from the given string, attempting to detect the language each time.

You can specify the language(s), if known, using `languages` argument. In this case, given languages are used and language detection is skipped:

>>> dateparser.parse('2015, Ago 15, 1:08 pm', languages=['pt', 'es'])
datetime.datetime(2015, 8, 15, 13, 8)

If you know the possible formats of the dates, you can use the `date_formats` argument:

>>> dateparser.parse('22 Décembre 2010', date_formats=['%d %B %Y'])
datetime.datetime(2010, 12, 22, 0, 0)

### Relative Dates[](https://dateparser.readthedocs.io/en/latest/#relative-dates "Link to this heading")

>>> parse('1 hour ago')
datetime.datetime(2015, 5, 31, 23, 0)
>>> parse('Il ya 2 heures')  # French (2 hours ago)
datetime.datetime(2015, 5, 31, 22, 0)
>>> parse('1 anno 2 mesi')  # Italian (1 year 2 months)
datetime.datetime(2014, 4, 1, 0, 0)
>>> parse('yaklaşık 23 saat önce')  # Turkish (23 hours ago)
datetime.datetime(2015, 5, 31, 1, 0)
>>> parse('Hace una semana')  # Spanish (a week ago)
datetime.datetime(2015, 5, 25, 0, 0)
>>> parse('2小时前')  # Chinese (2 hours ago)
datetime.datetime(2015, 5, 31, 22, 0)

Note

Testing above code might return different values for you depending on your environment’s current date and time.

Note

For Finnish language, please specify `settings={'SKIP_TOKENS': []}` to correctly parse relative dates.

### OOTB Language Based Date Order Preference[](https://dateparser.readthedocs.io/en/latest/#ootb-language-based-date-order-preference "Link to this heading")

>>> # parsing ambiguous date
>>>
>>> parse('02-03-2016')  # assumes english language, uses MDY date order
datetime.datetime(2016, 2, 3, 0, 0)
>>> parse('le 02-03-2016')  # detects french, uses DMY date order
datetime.datetime(2016, 3, 2, 0, 0)

Note

Ordering is not locale based, that’s why do not expect DMY order for UK/Australia English. You can specify date order in that case as follows using [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings):

>>> parse('18-12-15 06:00', settings={'DATE_ORDER': 'DMY'})
datetime.datetime(2015, 12, 18, 6, 0)

For more on date order, please look at [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings).

### Timezone and UTC Offset[](https://dateparser.readthedocs.io/en/latest/#timezone-and-utc-offset "Link to this heading")

By default, dateparser returns tzaware datetime if timezone is present in date string. Otherwise, it returns a naive datetime object.

> >>> parse('January 12, 2012 10:00 PM EST')
> datetime.datetime(2012, 1, 12, 22, 0, tzinfo=<StaticTzInfo 'EST'>)
>
>
>
> >>> parse('January 12, 2012 10:00 PM -0500')
> datetime.datetime(2012, 1, 12, 22, 0, tzinfo=<StaticTzInfo 'UTC\-05:00'>)
>
>
>
> >>> parse('2 hours ago EST')
> datetime.datetime(2017, 3, 10, 15, 55, 39, 579667, tzinfo=<StaticTzInfo 'EST'>)
>
>
>
> >>> parse('2 hours ago -0500')
> datetime.datetime(2017, 3, 10, 15, 59, 30, 193431, tzinfo=<StaticTzInfo 'UTC\-05:00'>)
>
>
> If date has no timezone name/abbreviation or offset, you can specify it using TIMEZONE setting.
>
>
>
> >>> parse('January 12, 2012 10:00 PM', settings={'TIMEZONE': 'US/Eastern'})
> datetime.datetime(2012, 1, 12, 22, 0)
>
>
>
> >>> parse('January 12, 2012 10:00 PM', settings={'TIMEZONE': '+0500'})
> datetime.datetime(2012, 1, 12, 22, 0)

`TIMEZONE` option may not be useful alone as it only attaches given timezone to resultant `datetime` object. But can be useful in cases where you want conversions from and to different timezones or when simply want a tzaware date with given timezone info attached.

>>> parse('January 12, 2012 10:00 PM', settings={'TIMEZONE': 'US/Eastern', 'RETURN_AS_TIMEZONE_AWARE': True})
datetime.datetime(2012, 1, 12, 22, 0, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>)

>>> parse('10:00 am', settings={'TIMEZONE': 'EST', 'TO_TIMEZONE': 'EDT'})
datetime.datetime(2016, 9, 25, 11, 0)

Some more use cases for conversion of timezones.

>>> parse('10:00 am EST', settings={'TO_TIMEZONE': 'EDT'})  # date string has timezone info
datetime.datetime(2017, 3, 12, 11, 0, tzinfo=<StaticTzInfo 'EDT'>)

>>> parse('now EST', settings={'TO_TIMEZONE': 'UTC'})  # relative dates
datetime.datetime(2017, 3, 10, 23, 24, 47, 371823, tzinfo=<StaticTzInfo 'UTC'>)

In case, no timezone is present in date string or defined in [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings). You can still return tzaware `datetime`. It is especially useful in case of relative dates when uncertain what timezone is relative base.

>>> parse('2 minutes ago', settings={'RETURN_AS_TIMEZONE_AWARE': True})
datetime.datetime(2017, 3, 11, 4, 25, 24, 152670, tzinfo=<DstTzInfo 'Asia/Karachi' PKT+5:00:00 STD>)

In case, you want to compute relative dates in UTC instead of default system’s local timezone, you can use TIMEZONE setting.

>>> parse('4 minutes ago', settings={'TIMEZONE': 'UTC'})
datetime.datetime(2017, 3, 10, 23, 27, 59, 647248, tzinfo=<StaticTzInfo 'UTC'>)

Note

In case, when timezone is present both in string and also specified using [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings), string is parsed into tzaware representation and then converted to timezone specified in [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings).

>>> parse('10:40 pm PKT', settings={'TIMEZONE': 'UTC'})
datetime.datetime(2017, 3, 12, 17, 40, tzinfo=<StaticTzInfo 'UTC'>)

>>> parse('20 mins ago EST', settings={'TIMEZONE': 'UTC'})
datetime.datetime(2017, 3, 12, 21, 16, 0, 885091, tzinfo=<StaticTzInfo 'UTC'>)

For more on timezones, please look at [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings).

### Incomplete Dates[](https://dateparser.readthedocs.io/en/latest/#incomplete-dates "Link to this heading")

>>> from dateparser import parse
>>> parse('December 2015')  # default behavior
datetime.datetime(2015, 12, 16, 0, 0)
>>> parse('December 2015', settings={'PREFER_DAY_OF_MONTH': 'last'})
datetime.datetime(2015, 12, 31, 0, 0)
>>> parse('December 2015', settings={'PREFER_DAY_OF_MONTH': 'first'})
datetime.datetime(2015, 12, 1, 0, 0)

>>> parse('March')
datetime.datetime(2015, 3, 16, 0, 0)
>>> parse('March', settings={'PREFER_DATES_FROM': 'future'})
datetime.datetime(2016, 3, 16, 0, 0)

>>> # parsing with preference set for 'past'
>>>
>>> parse('August', settings={'PREFER_DATES_FROM': 'past'})
datetime.datetime(2015, 8, 15, 0, 0)

>>> import dateparser
>>> dateparser.parse("2015") # default behavior
datetime.datetime(2015, 3, 27, 0, 0)
>>> dateparser.parse("2015", settings={"PREFER_MONTH_OF_YEAR": "last"})
datetime.datetime(2015, 12, 27, 0, 0)
>>> dateparser.parse("2015", settings={"PREFER_MONTH_OF_YEAR": "first"})
datetime.datetime(2015, 1, 27, 0, 0)
>>> dateparser.parse("2015", settings={"PREFER_MONTH_OF_YEAR": "current"})
datetime.datetime(2015, 3, 27, 0, 0)

You can also ignore parsing incomplete dates altogether by setting STRICT_PARSING flag as follows:

>>> parse('December 2015', settings={'STRICT_PARSING': True})
None

For more on handling incomplete dates, please look at [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings).

### Search for Dates in Longer Chunks of Text[](https://dateparser.readthedocs.io/en/latest/#search-for-dates-in-longer-chunks-of-text "Link to this heading")

Warning

Support for searching dates is really limited and needs a lot of improvement, we look forward to community’s contribution to get better on that part. See “[Contributing](https://dateparser.readthedocs.io/en/latest/contributing.html#contributing)”.

You can extract dates from longer strings of text. They are returned as list of tuples with text chunk containing the date and parsed datetime object.

dateparser.search.search_dates[_text_, _languages=None_, _settings=None_, _add\_detected\_language=False_, _detect\_languages\_function=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/search.html#search_dates)
Find all substrings of the given string which represent date and/or time and parse them.

Parameters:

* **text** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string in a natural language which may contain date and/or time expressions.

* **languages** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of two letters language codes.e.g. [‘en’, ‘es’]. If languages are given, it will not attempt to detect the language.

* **settings** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Configure customized behavior using settings defined in [`dateparser.conf.Settings`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings "dateparser.conf.Settings").

* **add_detected_language** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Indicates if we want the detected language returned in the tuple.

* **detect_languages_function** (_function_) – A function for language detection that takes as input a text and a confidence_threshold, and returns a list of detected language codes. Note: detect_languages_function is only uses if languages are not provided.

Returns:
Returns list of tuples containing: substrings representing date and/or time, corresponding `datetime.datetime` object and detected language if _add\_detected\_language_ is True. Returns None if no dates that can be parsed are found.

Return type:
[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

Raises:
ValueError - Unknown Language

>>> from dateparser.search import search_dates
>>> search_dates('The first artificial Earth satellite was launched on 4 October 1957.')
[('on 4 October 1957', datetime.datetime(1957, 10, 4, 0, 0))]

>>> search_dates('The first artificial Earth satellite was launched on 4 October 1957.',
>>> add_detected_language=True)
[('on 4 October 1957', datetime.datetime(1957, 10, 4, 0, 0), 'en')]

>>> search_dates("The client arrived to the office for the first time in March 3rd, 2004 "
>>> "and got serviced, after a couple of months, on May 6th 2004, the customer "
>>> "returned indicating a defect on the part")
[('in March 3rd, 2004 and', datetime.datetime(2004, 3, 3, 0, 0)),
 ('on May 6th 2004', datetime.datetime(2004, 5, 6, 0, 0))]

### Time Span Detection[](https://dateparser.readthedocs.io/en/latest/#time-span-detection "Link to this heading")

The search_dates function can detect time spans from expressions like “past month”, “last week”, etc. When RETURN_TIME_SPAN is enabled, it returns start and end dates for the detected period.

>>> search_dates("Messages from the past month", settings={'RETURN_TIME_SPAN': True})
[('past month (start)', datetime.datetime(2024, 11, 7, 0, 0)),
 ('past month (end)', datetime.datetime(2024, 12, 7, 23, 59, 59, 999999))]

Advanced Usage[](https://dateparser.readthedocs.io/en/latest/#advanced-usage "Link to this heading")
-----------------------------------------------------------------------------------------------------

If you need more control over what is being parser check the [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings) section as well as the [Using DateDataParser](https://dateparser.readthedocs.io/en/latest/usage.html#using-datedataparser) section.

Dependencies[](https://dateparser.readthedocs.io/en/latest/#dependencies "Link to this heading")
-------------------------------------------------------------------------------------------------

dateparser relies on following libraries in some ways:

> * [dateutil](https://pypi.python.org/pypi/python-dateutil)’s module `relativedelta` for its freshness parser.
>
> * [convertdate](https://pypi.python.org/pypi/convertdate) to convert _Jalali_ dates to _Gregorian_.
>
> * [hijridate](https://pypi.python.org/pypi/hijridate) to convert _Hijri_ dates to _Gregorian_.
>
> * [tzlocal](https://pypi.python.org/pypi/tzlocal) to reliably get local timezone.
>
> * [ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml) (optional) for operations on language files.

Supported languages and locales[](https://dateparser.readthedocs.io/en/latest/#supported-languages-and-locales "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

You can check the supported locales by visiting the “[Supported languages and locales](https://dateparser.readthedocs.io/en/latest/supported_locales.html#supported-locales)” section.

Supported Calendars[](https://dateparser.readthedocs.io/en/latest/#supported-calendars "Link to this heading")
---------------------------------------------------------------------------------------------------------------

Apart from the Georgian calendar, dateparser supports the Persian Jalali calendar and the Hijri/Islami calendar

To be able to use them you need to install the calendar extra by typing:

> pip install dateparser[calendars]

* Example using the Persian Jalali calendar. For more information, refer to [Persian Jalali Calendar](https://en.wikipedia.org/wiki/Iranian_calendars#Zoroastrian_calendar).

>>> from dateparser.calendars.jalali import JalaliCalendar
>>> JalaliCalendar('جمعه سی ام اسفند ۱۳۸۷').get_date()
DateData(date_obj=datetime.datetime(2009, 3, 20, 0, 0), period='day', locale=None)

* Example using the Hijri/Islamic Calendar. For more information, refer to [Hijri Calendar](https://en.wikipedia.org/wiki/Islamic_calendar).

>>> from dateparser.calendars.hijri import HijriCalendar
>>> HijriCalendar('17-01-1437 هـ 08:30 مساءً').get_date()
DateData(date_obj=datetime.datetime(2015, 10, 30, 20, 30), period='day', locale=None)

Note

HijriCalendar only works with Python ≥ 3.7.

Indices and tables[](https://dateparser.readthedocs.io/en/latest/#indices-and-tables "Link to this heading")
-------------------------------------------------------------------------------------------------------------

Contents:

* [Introduction to dateparser](https://dateparser.readthedocs.io/en/latest/introduction.html)
  * [Features](https://dateparser.readthedocs.io/en/latest/introduction.html#features)
  * [Basic Usage](https://dateparser.readthedocs.io/en/latest/introduction.html#basic-usage)
  * [Advanced Usage](https://dateparser.readthedocs.io/en/latest/introduction.html#advanced-usage)
  * [Dependencies](https://dateparser.readthedocs.io/en/latest/introduction.html#dependencies)
  * [Supported languages and locales](https://dateparser.readthedocs.io/en/latest/introduction.html#supported-languages-and-locales)
  * [Supported Calendars](https://dateparser.readthedocs.io/en/latest/introduction.html#supported-calendars)

* [Installation](https://dateparser.readthedocs.io/en/latest/installation.html)
* [Using DateDataParser](https://dateparser.readthedocs.io/en/latest/usage.html)
* [Settings](https://dateparser.readthedocs.io/en/latest/settings.html)
  * [Date Order](https://dateparser.readthedocs.io/en/latest/settings.html#date-order)
  * [Timezone Related Configurations](https://dateparser.readthedocs.io/en/latest/settings.html#timezone-related-configurations)
  * [Handling Incomplete Dates](https://dateparser.readthedocs.io/en/latest/settings.html#handling-incomplete-dates)
  * [Language Detection](https://dateparser.readthedocs.io/en/latest/settings.html#language-detection)
  * [Default Languages](https://dateparser.readthedocs.io/en/latest/settings.html#default-languages)
  * [Optional language detection](https://dateparser.readthedocs.io/en/latest/settings.html#optional-language-detection)
  * [Other settings](https://dateparser.readthedocs.io/en/latest/settings.html#other-settings)

* [Custom language detection](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html)
  * [Built-in implementations](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html#built-in-implementations)
  * [Custom implementation](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html#custom-implementation)

* [Supported languages and locales](https://dateparser.readthedocs.io/en/latest/supported_locales.html)
* [Contributing](https://dateparser.readthedocs.io/en/latest/contributing.html)
  * [Types of Contributions](https://dateparser.readthedocs.io/en/latest/contributing.html#types-of-contributions)
  * [Get Started!](https://dateparser.readthedocs.io/en/latest/contributing.html#get-started)
  * [Pull Request Guidelines](https://dateparser.readthedocs.io/en/latest/contributing.html#pull-request-guidelines)
  * [Guidelines for Editing Translation Data](https://dateparser.readthedocs.io/en/latest/contributing.html#guidelines-for-editing-translation-data)
  * [Updating the List of Supported Languages and Locales](https://dateparser.readthedocs.io/en/latest/contributing.html#updating-the-list-of-supported-languages-and-locales)
  * [Updating the Timezone Cache](https://dateparser.readthedocs.io/en/latest/contributing.html#updating-the-timezone-cache)

* [API reference](https://dateparser.readthedocs.io/en/latest/modules.html)
  * [dateparser package](https://dateparser.readthedocs.io/en/latest/dateparser.html)

* [Credits](https://dateparser.readthedocs.io/en/latest/authors.html)
* [History](https://dateparser.readthedocs.io/en/latest/history.html)
  * [1.3.0 (2026-02-04)](https://dateparser.readthedocs.io/en/latest/history.html#id1)
  * [1.2.2 (2025-06-26)](https://dateparser.readthedocs.io/en/latest/history.html#id2)
  * [1.2.1 (2025-02-05)](https://dateparser.readthedocs.io/en/latest/history.html#id3)
  * [1.2.0 (2023-11-17)](https://dateparser.readthedocs.io/en/latest/history.html#id4)
  * [1.1.8 (2023-03-22)](https://dateparser.readthedocs.io/en/latest/history.html#id5)
  * [1.1.7 (2023-02-02)](https://dateparser.readthedocs.io/en/latest/history.html#id6)
  * [1.1.6 (2023-01-12)](https://dateparser.readthedocs.io/en/latest/history.html#id7)
  * [1.1.5 (2022-12-29)](https://dateparser.readthedocs.io/en/latest/history.html#id8)
  * [1.1.4 (2022-11-21)](https://dateparser.readthedocs.io/en/latest/history.html#id9)
  * [1.1.3 (2022-11-03)](https://dateparser.readthedocs.io/en/latest/history.html#id10)
  * [1.1.2 (2022-10-20)](https://dateparser.readthedocs.io/en/latest/history.html#id11)
  * [1.1.1 (2022-03-17)](https://dateparser.readthedocs.io/en/latest/history.html#id12)
  * [1.1.0 (2021-10-04)](https://dateparser.readthedocs.io/en/latest/history.html#id13)
  * [1.0.0 (2020-10-29)](https://dateparser.readthedocs.io/en/latest/history.html#id14)
  * [0.7.6 (2020-06-12)](https://dateparser.readthedocs.io/en/latest/history.html#id15)
  * [0.7.5 (2020-06-10)](https://dateparser.readthedocs.io/en/latest/history.html#id16)
  * [0.7.4 (2020-03-06)](https://dateparser.readthedocs.io/en/latest/history.html#id17)
  * [0.7.3 (2020-03-06)](https://dateparser.readthedocs.io/en/latest/history.html#id18)
  * [0.7.2 (2019-09-17)](https://dateparser.readthedocs.io/en/latest/history.html#id19)
  * [0.7.1 (2019-02-12)](https://dateparser.readthedocs.io/en/latest/history.html#id20)
  * [0.7.0 (2018-02-08)](https://dateparser.readthedocs.io/en/latest/history.html#id21)
  * [0.6.0 (2017-03-13)](https://dateparser.readthedocs.io/en/latest/history.html#id22)
  * [0.5.1 (2016-12-18)](https://dateparser.readthedocs.io/en/latest/history.html#id23)
  * [0.5.0 (2016-09-26)](https://dateparser.readthedocs.io/en/latest/history.html#id24)
  * [0.4.0 (2016-06-17)](https://dateparser.readthedocs.io/en/latest/history.html#id25)
  * [0.3.5 (2016-04-27)](https://dateparser.readthedocs.io/en/latest/history.html#id26)
  * [0.3.4 (2016-03-03)](https://dateparser.readthedocs.io/en/latest/history.html#id27)
  * [0.3.3 (2016-02-29)](https://dateparser.readthedocs.io/en/latest/history.html#id28)
  * [0.3.2 (2016-01-25)](https://dateparser.readthedocs.io/en/latest/history.html#id29)
  * [0.3.1 (2015-10-28)](https://dateparser.readthedocs.io/en/latest/history.html#id30)
  * [0.3.0 (2015-07-29)](https://dateparser.readthedocs.io/en/latest/history.html#id31)
  * [0.2.1 (2015-07-13)](https://dateparser.readthedocs.io/en/latest/history.html#id32)
  * [0.2.0 (2015-06-17)](https://dateparser.readthedocs.io/en/latest/history.html#id33)
  * [0.1.0 (2014-11-24)](https://dateparser.readthedocs.io/en/latest/history.html#id34)

* [Index](https://dateparser.readthedocs.io/en/latest/genindex.html)

* [Module Index](https://dateparser.readthedocs.io/en/latest/py-modindex.html)

* [Search Page](https://dateparser.readthedocs.io/en/latest/search.html)
