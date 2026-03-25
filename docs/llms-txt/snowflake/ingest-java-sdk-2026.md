# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/ingest-java-sdk-2026.md

# Ingest Java SDK release notes for 2026

This article contains the release notes for the Ingest Java SDK, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for Ingest Java SDK updates.

## Version 4.4.2 (January 12, 2026)

### Bug fixes

* Security update: Updated core networking libraries to resolve a known vulnerability in the netty-codec-http component.
* System stability: Refreshed several internal dependencies to ensure compatibility and improve overall application reliability.

## Version 4.4.1 (January 06, 2026)

### Bug fixes

* Fixed an issue where ingesting repeated fields (arrays) containing multiple null entries would cause a validation error. The ingestion process now correctly handles these structures, ensuring data flows smoothly without unnecessary failures.
