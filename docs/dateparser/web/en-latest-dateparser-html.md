# Source: https://dateparser.readthedocs.io/en/latest/dateparser.html

Title: dateparser package — DateParser 1.3.0 documentation

URL Source: https://dateparser.readthedocs.io/en/latest/dateparser.html

Markdown Content:
Subpackages[](https://dateparser.readthedocs.io/en/latest/dateparser.html#subpackages "Link to this heading")
--------------------------------------------------------------------------------------------------------------

* [dateparser.languages package](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html)
  * [Submodules](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#submodules)
  * [dateparser.languages.dictionary module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.dictionary)
    * [`Dictionary`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.dictionary.Dictionary)
      * [`Dictionary.are_tokens_valid()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.dictionary.Dictionary.are_tokens_valid)
      * [`Dictionary.split()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.dictionary.Dictionary.split)

    * [`NormalizedDictionary`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.dictionary.NormalizedDictionary)
    * [`UnknownTokenError`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.dictionary.UnknownTokenError)

  * [dateparser.languages.loader module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.loader)
    * [`LocaleDataLoader`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.loader.LocaleDataLoader)
      * [`LocaleDataLoader.get_locale()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.loader.LocaleDataLoader.get_locale)
      * [`LocaleDataLoader.get_locale_map()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.loader.LocaleDataLoader.get_locale_map)
      * [`LocaleDataLoader.get_locales()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.loader.LocaleDataLoader.get_locales)

  * [dateparser.languages.locale module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.locale)
    * [`Locale`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale)
      * [`Locale.clean_dictionary()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.clean_dictionary)
      * [`Locale.count_applicability()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.count_applicability)
      * [`Locale.get_wordchars_for_detection()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.get_wordchars_for_detection)
      * [`Locale.is_applicable()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.is_applicable)
      * [`Locale.to_parserinfo()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.to_parserinfo)
      * [`Locale.translate()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.translate)
      * [`Locale.translate_search()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.locale.Locale.translate_search)

  * [dateparser.languages.validation module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.validation)
    * [`LanguageValidator`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.validation.LanguageValidator)
      * [`LanguageValidator.VALID_KEYS`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.validation.LanguageValidator.VALID_KEYS)
      * [`LanguageValidator.get_logger()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.validation.LanguageValidator.get_logger)
      * [`LanguageValidator.logger`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.validation.LanguageValidator.logger)
      * [`LanguageValidator.validate_info()`](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#dateparser.languages.validation.LanguageValidator.validate_info)

  * [Module contents](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages)

* [dateparser.calendars package](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html)
  * [Submodules](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html#submodules)
  * [Module contents](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html#module-dateparser.calendars)
    * [`CalendarBase`](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html#dateparser.calendars.CalendarBase)

Submodules[](https://dateparser.readthedocs.io/en/latest/dateparser.html#submodules "Link to this heading")
------------------------------------------------------------------------------------------------------------

dateparser.conf module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.conf "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

_exception_ dateparser.conf.SettingValidationError[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/conf.html#SettingValidationError)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.SettingValidationError "Link to this definition")
Bases: [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")

_class_ dateparser.conf.Settings[_*args_, _**kwargs_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/conf.html#Settings)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings "Link to this definition")
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Control and configure default parsing behavior of dateparser. Currently, supported settings are:

* DATE_ORDER

* PREFER_LOCALE_DATE_ORDER

* TIMEZONE

* TO_TIMEZONE

* RETURN_AS_TIMEZONE_AWARE

* PREFER_MONTH_OF_YEAR

* PREFER_DAY_OF_MONTH

* PREFER_DATES_FROM

* RELATIVE_BASE

* STRICT_PARSING

* REQUIRE_PARTS

* SKIP_TOKENS

* NORMALIZE

* RETURN_TIME_AS_PERIOD

* RETURN_TIME_SPAN

* DEFAULT_START_OF_WEEK

* DEFAULT_DAYS_IN_MONTH

* PARSERS

* DEFAULT_LANGUAGES

* LANGUAGE_DETECTION_CONFIDENCE_THRESHOLD

* CACHE_SIZE_LIMIT

_classmethod_ get_key[_settings=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/conf.html#Settings.get_key)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings.get_key "Link to this definition")replace[_mod\_settings=None_, _**kwds_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/conf.html#Settings.replace)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings.replace "Link to this definition")dateparser.conf.apply_settings[_f_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/conf.html#apply_settings)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.apply_settings "Link to this definition")dateparser.conf.check_settings[_settings_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/conf.html#check_settings)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.check_settings "Link to this definition")
Check if provided settings are valid, if not it raises SettingValidationError. Only checks for the modified settings.

dateparser.date module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.date "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

_class_ dateparser.date.DateData[_*_, _date\_obj=None_, _period=None_, _locale=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#DateData)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateData "Link to this definition")
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Class that represents the parsed data with useful information. It can be accessed with square brackets like a dict object.

_class_ dateparser.date.DateDataParser[_languages=None_, _locales=None_, _region=None_, _try\_previous\_locales=False_, _use\_given\_order=False_, _settings=None_, _detect\_languages\_function=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#DateDataParser)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser "Link to this definition")
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Class which handles language detection, translation and subsequent generic parsing of string representing date and/or time.

Parameters:

* **languages** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of language codes, e.g. [‘en’, ‘es’, ‘zh-Hant’]. If locales are not given, languages and region are used to construct locales for translation.

* **locales** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of locale codes, e.g. [‘fr-PF’, ‘qu-EC’, ‘af-NA’]. The parser uses only these locales to translate date string.

* **region** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A region code, e.g. ‘IN’, ‘001’, ‘NE’. If locales are not given, languages and region are used to construct locales for translation.

* **try_previous_locales** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – If True, locales previously used to translate date are tried first.

* **use_given_order** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – If True, locales are tried for translation of date string in the order in which they are given.

* **settings** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Configure customized behavior using settings defined in [`dateparser.conf.Settings`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings "dateparser.conf.Settings").

* **detect_languages_function** (_function_) – A function for language detection that takes as input a text and a confidence_threshold, and returns a list of detected language codes. Note: this function is only used if `languages` and `locales` are not provided.

Returns:
A parser instance

Raises:
`ValueError`: Unknown Language, `TypeError`: Languages argument must be a list, `SettingValidationError`: A provided setting is not valid.

get_date_data[_date\_string_, _date\_formats=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#DateDataParser.get_date_data)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser.get_date_data "Link to this definition")
Parse string representing date and/or time in recognizable localized formats. Supports parsing multiple languages and timezones.

Parameters:

* **date_string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string representing date and/or time in a recognizably valid format.

* **date_formats** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of format strings using directives as given [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior). The parser applies formats one by one, taking into account the detected languages.

Returns:
a `DateData` object.

Raises:
ValueError - Unknown Language

Note

_Period_ values can be a ‘day’ (default), ‘week’, ‘month’, ‘year’, ‘time’.

_Period_ represents the granularity of date parsed from the given string.

In the example below, since no day information is present, the day is assumed to be current day `16` from _current date_ (which is June 16, 2015, at the moment of writing this). Hence, the level of precision is `month`:

>>> DateDataParser().get_date_data('March 2015')
DateData(date_obj=datetime.datetime(2015, 3, 16, 0, 0), period='month', locale='en')

Similarly, for date strings with no day and month information present, level of precision is `year` and day `16` and month `6` are from _current\_date_.

>>> DateDataParser().get_date_data('2014')
DateData(date_obj=datetime.datetime(2014, 6, 16, 0, 0), period='year', locale='en')

Dates with time zone indications or UTC offsets are returned in UTC time unless specified using [Settings](https://dateparser.readthedocs.io/en/latest/settings.html#settings).

>>> DateDataParser().get_date_data('23 March 2000, 1:21 PM CET')
DateData(date_obj=datetime.datetime(2000, 3, 23, 13, 21, tzinfo=<StaticTzInfo 'CET'>),
period='day', locale='en')

get_date_tuple[_*args_, _**kwargs_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#DateDataParser.get_date_tuple)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser.get_date_tuple "Link to this definition")locale_loader _=None_[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser.locale_loader "Link to this definition")dateparser.date.date_range[_begin_, _end_, _**kwargs_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#date_range)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.date_range "Link to this definition")dateparser.date.get_date_from_timestamp[_date\_string_, _settings_, _negative=False_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#get_date_from_timestamp)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.get_date_from_timestamp "Link to this definition")dateparser.date.get_intersecting_periods[_low_, _high_, _period='day'_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#get_intersecting_periods)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.get_intersecting_periods "Link to this definition")dateparser.date.parse_with_formats[_date\_string_, _date\_formats_, _settings_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#parse_with_formats)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.parse_with_formats "Link to this definition")
Parse with formats and return a dictionary with ‘period’ and ‘obj_date’.

Returns:
[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)"), dict or None

dateparser.date.sanitize_date[_date\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#sanitize_date)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.sanitize_date "Link to this definition")dateparser.date.sanitize_spaces[_date\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date.html#sanitize_spaces)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.sanitize_spaces "Link to this definition")
dateparser.date_parser module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.date_parser "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

_class_ dateparser.date_parser.DateParser[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date_parser.html#DateParser)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date_parser.DateParser "Link to this definition")
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

parse[_date\_string_, _parse\_method_, _settings=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/date_parser.html#DateParser.parse)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date_parser.DateParser.parse "Link to this definition")
dateparser.freshness_date_parser module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.freshness_date_parser "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ dateparser.freshness_date_parser.FreshnessDateDataParser[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/freshness_date_parser.html#FreshnessDateDataParser)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser "Link to this definition")
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Parses date string like “1 year, 2 months ago” and “3 hours, 50 minutes ago”

get_date_data[_date\_string_, _settings=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/freshness_date_parser.html#FreshnessDateDataParser.get_date_data)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.get_date_data "Link to this definition")get_kwargs[_date\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/freshness_date_parser.html#FreshnessDateDataParser.get_kwargs)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.get_kwargs "Link to this definition")get_local_tz()[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/freshness_date_parser.html#FreshnessDateDataParser.get_local_tz)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.get_local_tz "Link to this definition")parse[_date\_string_, _settings_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/freshness_date_parser.html#FreshnessDateDataParser.parse)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.parse "Link to this definition")
dateparser.timezone_parser module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.timezone_parser "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ dateparser.timezone_parser.StaticTzInfo[_name_, _offset_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#StaticTzInfo)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo "Link to this definition")
Bases: [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")

dst[_dt_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#StaticTzInfo.dst)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.dst "Link to this definition")
datetime -> DST offset as timedelta positive east of UTC.

localize[_dt_, _is\_dst=False_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#StaticTzInfo.localize)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.localize "Link to this definition")tzname[_dt_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#StaticTzInfo.tzname)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.tzname "Link to this definition")
datetime -> string name of time zone.

utcoffset[_dt_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#StaticTzInfo.utcoffset)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.utcoffset "Link to this definition")
datetime -> timedelta showing offset from UTC, negative values indicating West of UTC

dateparser.timezone_parser.build_tz_offsets[_search\_regex\_parts_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#build_tz_offsets)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.build_tz_offsets "Link to this definition")dateparser.timezone_parser.convert_to_local_tz[_datetime\_obj_, _datetime\_tz\_offset_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#convert_to_local_tz)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.convert_to_local_tz "Link to this definition")dateparser.timezone_parser.get_local_tz_offset()[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#get_local_tz_offset)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.get_local_tz_offset "Link to this definition")dateparser.timezone_parser.pop_tz_offset_from_string[_date\_string_, _as\_offset=True_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#pop_tz_offset_from_string)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.pop_tz_offset_from_string "Link to this definition")dateparser.timezone_parser.word_is_tz[_word_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/timezone_parser.html#word_is_tz)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.word_is_tz "Link to this definition")
dateparser.timezones module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.timezones "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

dateparser.utils module[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.utils "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

dateparser.utils.apply_dateparser_timezone[_utc\_datetime_, _offset\_or\_timezone\_abb_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#apply_dateparser_timezone)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_dateparser_timezone "Link to this definition")dateparser.utils.apply_timezone[_date\_time_, _tz\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#apply_timezone)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_timezone "Link to this definition")dateparser.utils.apply_timezone_from_settings[_date\_obj_, _settings_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#apply_timezone_from_settings)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_timezone_from_settings "Link to this definition")dateparser.utils.apply_tzdatabase_timezone[_date\_time_, _pytz\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#apply_tzdatabase_timezone)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_tzdatabase_timezone "Link to this definition")dateparser.utils.combine_dicts[_primary\_dict_, _supplementary\_dict_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#combine_dicts)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.combine_dicts "Link to this definition")dateparser.utils.find_date_separator[_format_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#find_date_separator)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.find_date_separator "Link to this definition")dateparser.utils.get_last_day_of_month[_year_, _month_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#get_last_day_of_month)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_last_day_of_month "Link to this definition")dateparser.utils.get_logger()[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#get_logger)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_logger "Link to this definition")dateparser.utils.get_next_leap_year[_year_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#get_next_leap_year)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_next_leap_year "Link to this definition")dateparser.utils.get_previous_leap_year[_year_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#get_previous_leap_year)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_previous_leap_year "Link to this definition")dateparser.utils.get_timezone_from_tz_string[_tz\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#get_timezone_from_tz_string)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_timezone_from_tz_string "Link to this definition")dateparser.utils.localize_timezone[_date\_time_, _tz\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#localize_timezone)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.localize_timezone "Link to this definition")dateparser.utils.normalize_unicode[_string_, _form='NFKD'_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#normalize_unicode)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.normalize_unicode "Link to this definition")dateparser.utils.registry[_cls_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#registry)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.registry "Link to this definition")dateparser.utils.set_correct_day_from_settings[_date\_obj_, _settings_, _current\_day=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#set_correct_day_from_settings)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.set_correct_day_from_settings "Link to this definition")
Set correct day attending the PREFER_DAY_OF_MONTH setting.

dateparser.utils.set_correct_month_from_settings[_date\_obj_, _settings_, _current\_month=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#set_correct_month_from_settings)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.set_correct_month_from_settings "Link to this definition")
Set correct month attending the PREFER_MONTH_OF_YEAR setting.

dateparser.utils.setup_logging()[[source]](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#setup_logging)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.setup_logging "Link to this definition")dateparser.utils.strip_braces[_date\_string_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser/utils.html#strip_braces)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.strip_braces "Link to this definition")
Module contents[](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

dateparser.parse[_date\_string_, _date\_formats=None_, _languages=None_, _locales=None_, _region=None_, _settings=None_, _detect\_languages\_function=None_]([source)](https://dateparser.readthedocs.io/en/latest/_modules/dateparser.html#parse)[](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.parse "Link to this definition")
Parse date and time from given date string.

Parameters:

* **date_string** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string representing date and/or time in a recognizably valid format.

* **date_formats** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) –

A list of format strings using directives as given [here](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior). The parser applies formats one by one, taking into account the detected languages/locales.

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
