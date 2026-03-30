# Source: https://dateparser.readthedocs.io/en/latest/modules.html

Title: API reference — DateParser 1.3.0 documentation

URL Source: https://dateparser.readthedocs.io/en/latest/modules.html

Markdown Content:
API reference — DateParser 1.3.0 documentation
===============

[![Image 1: Logo](https://dateparser.readthedocs.io/en/latest/_static/dateparser-logo.png)](https://dateparser.readthedocs.io/en/latest/index.html)

 1.3.0

* [Introduction to dateparser](https://dateparser.readthedocs.io/en/latest/introduction.html)
* [Installation](https://dateparser.readthedocs.io/en/latest/installation.html)
* [Using DateDataParser](https://dateparser.readthedocs.io/en/latest/usage.html)
* [Settings](https://dateparser.readthedocs.io/en/latest/settings.html)
* [Custom language detection](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html)
* [Supported languages and locales](https://dateparser.readthedocs.io/en/latest/supported_locales.html)
* [Contributing](https://dateparser.readthedocs.io/en/latest/contributing.html)
* [API reference](https://dateparser.readthedocs.io/en/latest/modules.html#)
  * [dateparser package](https://dateparser.readthedocs.io/en/latest/dateparser.html)

* [Credits](https://dateparser.readthedocs.io/en/latest/authors.html)
* [History](https://dateparser.readthedocs.io/en/latest/history.html)

[![Image 2: Sponsored: Promoted](https://media.ethicalads.io/media/images/2025/12/cropped_UiZ6BUl.png)](https://server.ethicalads.io/proxy/click/10084/019cdc98-8b34-7313-b116-ebfd5012272b/)

[Get the APM insights you need without enterprise price tags. Built for dev teams, not Fortune 500s.](https://server.ethicalads.io/proxy/click/10084/019cdc98-8b34-7313-b116-ebfd5012272b/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=rtd-sidebar-buy-ads)

![Image 3](https://server.ethicalads.io/proxy/view/10084/019cdc98-8b34-7313-b116-ebfd5012272b/)

[DateParser](https://dateparser.readthedocs.io/en/latest/index.html)

* [](https://dateparser.readthedocs.io/en/latest/index.html)
* API reference
* [View page source](https://dateparser.readthedocs.io/en/latest/_sources/modules.rst.txt)

* * *

API reference[](https://dateparser.readthedocs.io/en/latest/modules.html#api-reference "Link to this heading")
===============================================================================================================

* [dateparser package](https://dateparser.readthedocs.io/en/latest/dateparser.html)
  * [Subpackages](https://dateparser.readthedocs.io/en/latest/dateparser.html#subpackages)
    * [dateparser.languages package](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html)
      * [Submodules](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#submodules)
      * [dateparser.languages.dictionary module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.dictionary)
      * [dateparser.languages.loader module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.loader)
      * [dateparser.languages.locale module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.locale)
      * [dateparser.languages.validation module](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages.validation)
      * [Module contents](https://dateparser.readthedocs.io/en/latest/dateparser.languages.html#module-dateparser.languages)

    * [dateparser.calendars package](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html)
      * [Submodules](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html#submodules)
      * [Module contents](https://dateparser.readthedocs.io/en/latest/dateparser.calendars.html#module-dateparser.calendars)

  * [Submodules](https://dateparser.readthedocs.io/en/latest/dateparser.html#submodules)
  * [dateparser.conf module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.conf)
    * [`SettingValidationError`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.SettingValidationError)
    * [`Settings`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings)
      * [`Settings.get_key()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings.get_key)
      * [`Settings.replace()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.Settings.replace)

    * [`apply_settings()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.apply_settings)
    * [`check_settings()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.conf.check_settings)

  * [dateparser.date module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.date)
    * [`DateData`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateData)
    * [`DateDataParser`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser)
      * [`DateDataParser.get_date_data()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser.get_date_data)
      * [`DateDataParser.get_date_tuple()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser.get_date_tuple)
      * [`DateDataParser.locale_loader`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.DateDataParser.locale_loader)

    * [`date_range()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.date_range)
    * [`get_date_from_timestamp()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.get_date_from_timestamp)
    * [`get_intersecting_periods()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.get_intersecting_periods)
    * [`parse_with_formats()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.parse_with_formats)
    * [`sanitize_date()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.sanitize_date)
    * [`sanitize_spaces()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date.sanitize_spaces)

  * [dateparser.date_parser module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.date_parser)
    * [`DateParser`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date_parser.DateParser)
      * [`DateParser.parse()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.date_parser.DateParser.parse)

  * [dateparser.freshness_date_parser module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.freshness_date_parser)
    * [`FreshnessDateDataParser`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser)
      * [`FreshnessDateDataParser.get_date_data()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.get_date_data)
      * [`FreshnessDateDataParser.get_kwargs()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.get_kwargs)
      * [`FreshnessDateDataParser.get_local_tz()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.get_local_tz)
      * [`FreshnessDateDataParser.parse()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.freshness_date_parser.FreshnessDateDataParser.parse)

  * [dateparser.timezone_parser module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.timezone_parser)
    * [`StaticTzInfo`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo)
      * [`StaticTzInfo.dst()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.dst)
      * [`StaticTzInfo.localize()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.localize)
      * [`StaticTzInfo.tzname()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.tzname)
      * [`StaticTzInfo.utcoffset()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.StaticTzInfo.utcoffset)

    * [`build_tz_offsets()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.build_tz_offsets)
    * [`convert_to_local_tz()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.convert_to_local_tz)
    * [`get_local_tz_offset()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.get_local_tz_offset)
    * [`pop_tz_offset_from_string()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.pop_tz_offset_from_string)
    * [`word_is_tz()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.timezone_parser.word_is_tz)

  * [dateparser.timezones module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.timezones)
  * [dateparser.utils module](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser.utils)
    * [`apply_dateparser_timezone()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_dateparser_timezone)
    * [`apply_timezone()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_timezone)
    * [`apply_timezone_from_settings()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_timezone_from_settings)
    * [`apply_tzdatabase_timezone()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.apply_tzdatabase_timezone)
    * [`combine_dicts()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.combine_dicts)
    * [`find_date_separator()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.find_date_separator)
    * [`get_last_day_of_month()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_last_day_of_month)
    * [`get_logger()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_logger)
    * [`get_next_leap_year()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_next_leap_year)
    * [`get_previous_leap_year()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_previous_leap_year)
    * [`get_timezone_from_tz_string()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.get_timezone_from_tz_string)
    * [`localize_timezone()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.localize_timezone)
    * [`normalize_unicode()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.normalize_unicode)
    * [`registry()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.registry)
    * [`set_correct_day_from_settings()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.set_correct_day_from_settings)
    * [`set_correct_month_from_settings()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.set_correct_month_from_settings)
    * [`setup_logging()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.setup_logging)
    * [`strip_braces()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.utils.strip_braces)

  * [Module contents](https://dateparser.readthedocs.io/en/latest/dateparser.html#module-dateparser)
    * [`parse()`](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.parse)

[Previous](https://dateparser.readthedocs.io/en/latest/template.html "Language Data Template")[Next](https://dateparser.readthedocs.io/en/latest/dateparser.html "dateparser package")

* * *

© Copyright 2014, Scrapinghub.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).
