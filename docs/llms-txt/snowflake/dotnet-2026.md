# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/dotnet-2026.md

# .NET Driver release notes for 2026

This article contains the release notes for the .NET Driver, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for .NET Driver updates.

See [.NET Driver](../../developer-guide/dotnet/dotnet-driver.md) for documentation.

## Version 5.4.1 (February 17, 2026)

### New features and improvements

* Extended login-request telemetry with Linux distribution details parsed from `/etc/os-release`.

### Bug fixes

* Fixed `IndexOutOfRangeException` in Arrow result chunk processing by adding retry state cleanup, batch integrity validation, and defensive bounds checking in `ExtractCell()`.

## Version 5.4.0 (February 05, 2026)

### New features and improvements

* Added support for Red Hat Enterprise Linux (RHEL) 9.
* Added support for the [DECFLOAT](../../sql-reference/data-types-numeric.md) data type (returned as string to preserve full precision).

### Bug fixes

* Fixed `IndexOutOfRangeException` in Arrow result processing when empty batches are returned by the Snowflake backend.

## Version 5.3.0 (January 07, 2026)

### New features and improvements

* Introduced a shared library for extended telemetry to identify and prepare the testing platform for native Rust extensions.

### Bug fixes

* None.
