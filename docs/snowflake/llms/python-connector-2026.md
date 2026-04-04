# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/python-connector-2026.md

# Snowflake Connector for Python release notes for 2026

This article contains the release notes for the Snowflake Connector for Python, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for Snowflake Connector for Python updates.

See [Snowflake Connector for Python](../../developer-guide/python-connector/python-connector.md) for documentation.

## Version 4.3.0 (Feb 12, 2026)

### Deprecated features

* Deprecated support for custom revocation error classes in OCSP response cache deserialization.

  > By default, only `RevocationCheckError` exceptions are deserialized from OCSP cache. Custom exception classes can be temporarily enabled by setting the `SNOWFLAKE_ENABLE_CUSTOM_REVOCATION_ERRORS` environment variable to `true` or `1`, but this support will be removed in a future release.

### New features and updates

* Bumped vendored `urllib3` to version 2.6.3.
* Added `force_microseconds_precision` to `cursor.fetch_arrow_all` and `cursor.fetch_pandas_all` to avoid PyArrow schema inconsistencies between batches.
* Added a warning when using HTTP protocol for OAuth URLs.
* Updated the `server_session_keep_alive` parameter in `SnowflakeConnection` to skip checking for pending asyncronous queries, providing faster connection close times, especially when many asyncronous queries are executed.

### Bug fixes

* Fixed the string representation of `INTERVAL YEAR` and `INTERVAL MONTH` types.
* Ensured proper list conversions; the converter now runs `to_snowflake` on all list items.

## Version 4.2.0 (Jan 07, 2026)

### New features and updates

* Added the `SnowflakeCursor.stats` property to expose granular DML statistics (rows inserted, deleted, updated, and duplicates) for operations like CTAS where `rowcount` is insufficient.
* Added support for injecting Snowpark Container Services (SPCS) service identifier tokens (`SPCS_TOKEN`) into login requests when present in SPCS containers.
* Introduced a shared library for extended telemetry to identify and prepare testing platforms for native Rust extensions.

### Bug fixes

* None.
