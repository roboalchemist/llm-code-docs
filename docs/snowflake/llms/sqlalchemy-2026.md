# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/sqlalchemy-2026.md

# SQLAlchemy release notes for 2026

This article contains the release notes for the SQLAlchemy, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for SQLAlchemy updates.

See [Using the Snowflake SQLAlchemy toolkit with the Python Connector](../../developer-guide/python-connector/sqlalchemy.md) for documentation.

## Version 1.9.0 (March 04, 2026)

### New features and updates

* Added support for `DECFLOAT` and `VECTOR` data types.
* Added support for `server_version_info` support.
* Added support for `ILIKE` in queries.
* Introduced a shared helper for fully-qualified schema name resolution, replacing inconsistent ad-hoc patterns across reflection methods.
* Refactored column reflection internals into dedicated helpers to reduce complexity without changing behavior.
* Added `pytest-xdist` parallel test support via per-worker schema provisioning hooks.
* Bumped pandas lower bound in the sa14 test environment from <2.1 to >=2.1.1,<2.2 to ensure pre-built wheels are available for Python 3.12.
* Added support for timezone in timestamp and datetime types.

### Bug fixes

* Fixed `SYSDATE()` rendering.
* Fixed and improved schema reflection.
* Fixed a crash issue when reflecting without specifying a schema, caused by `None` arguments in internal schema resolution.
* Fixed a crash issue when SHOW TABLES returns empty string table names, causing `IndexError` during reflection.
* Fixed incomplete identity column reflection metadata. This column now includes all fields required by SQLAlchemy 2.0+ (`always`, `cycle`, `order`, and so on).
* Fixed SQLAlchemy version parsing.
