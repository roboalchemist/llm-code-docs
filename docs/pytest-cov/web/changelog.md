# Changelog

## 7.1.0 (2026-03-21)

-

Fixed total coverage computation to always be consistent, regardless of reporting settings.
Previously some reports could produce different total counts, and consequently can make –cov-fail-under behave different depending on
reporting options.
See #641 [https://github.com/pytest-dev/pytest-cov/issues/641].

-

Improve handling of ResourceWarning from sqlite3.

The plugin adds warning filter for sqlite3 `ResourceWarning` unclosed database (since 6.2.0).
It checks if there is already existing plugin for this message by comparing filter regular expression.
When filter is specified on command line the message is escaped and does not match an expected message.
A check for an escaped regular expression is added to handle this case.

With this fix one can suppress `ResourceWarning` from sqlite3 from command line:

```
pytest -W "ignore:unclosed database in <sqlite3.Connection object at:ResourceWarning" ...

```
