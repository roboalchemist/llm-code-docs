# Source: https://dateparser.readthedocs.io/en/latest/usage.html

Title: Using DateDataParser — DateParser 1.3.0 documentation

URL Source: https://dateparser.readthedocs.io/en/latest/usage.html

Markdown Content:
[DateParser](https://dateparser.readthedocs.io/en/latest/index.html)
[`dateparser.parse()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.parse "dateparser.parse") uses a default parser which tries to detect language every time it is called and is not the most efficient way while parsing dates from the same source.

[`DateDataParser`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser "dateparser.date.DateDataParser") provides an alternate and efficient way to control language detection behavior.

The instance of [`DateDataParser`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser "dateparser.date.DateDataParser") caches the found languages and will prioritize them when trying to parse the next string.

[`dateparser.date.DateDataParser`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser "dateparser.date.DateDataParser") can also be initialized with known languages:

>>> ddp = DateDataParser(languages=['de', 'nl'])
>>> ddp.get_date_data('vr jan 24, 2014 12:49')
DateData(date_obj=datetime.datetime(2014, 1, 24, 12, 49), period='day', locale='nl')
>>> ddp.get_date_data('18.10.14 um 22:56 Uhr')
DateData(date_obj=datetime.datetime(2014, 10, 18, 22, 56), period='day', locale='de')
>>> ddp.get_date_data('11 July 2012')
DateData(date_obj=None, period='day', locale=None)
