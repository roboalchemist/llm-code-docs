# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/kafka-connector-2026.md

# Snowflake Connector for Kafka release notes for 2026

This article contains the release notes for the Snowflake Connector for Kafka, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for Snowflake Connector for Kafka updates.

See [Snowflake Connector for Kafka](../../user-guide/kafka-connector.md) for documentation.

## Version 3.5.1 (Jan 8, 2026)

### New features

* Upgraded Snowflake Ingest SDK to version 4.4.1.

### Bug fixes

* Fixed a `NullPointerException` in `SnowflakeSinkTask#precommit()`.
