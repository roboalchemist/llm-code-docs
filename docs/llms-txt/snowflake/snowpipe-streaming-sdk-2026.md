# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/snowpipe-streaming-sdk-2026.md

# Snowpipe Streaming SDK release notes for 2026

This article contains the release notes for the Snowpipe Streaming SDK, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for Snowpipe Streaming SDK updates.

## Version 1.2.0 (February 16, 2026)

### New features and updates

* Added support for encrypted key-pair authentication. You can now connect to your instances by using both encrypted and unencrypted private keys, providing greater flexibility for your security workflows.

## Version 1.1.2 (January 20, 2026)

### Behavior changes

* Fixed a race condition in the channel status cache to improve multi-threaded stability.
* Reduced log flooding by removing redundant messages for cleaner monitoring.

### New features and updates

* Added support for account locators with region suffixes.

### Bug fixes

* Removed unused configuration parameters and addressed minor internal logic issues to improve reliability.
