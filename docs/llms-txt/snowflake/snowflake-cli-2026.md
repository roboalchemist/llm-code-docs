# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/snowflake-cli-2026.md

# Snowflake CLI release notes for 2026

This article contains the release notes for the Snowflake CLI, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

See [Snowflake CLI](../../developer-guide/snowflake-cli/index.md) for documentation.

## Version 3.15.0 (Feb 03, 2026)

### New features and updates

* Added the `--if-exists` option to the `snow object drop` command and object-specific drop commands (for example, `snow stage drop`) to drop objects only if they exist, preventing errors when dropping non-existent objects.
* Updated the project definition with supported Python versions aligned with `snowflake-connector-python`.

### Bug fixes

* Fixed git repository path parsing to allow quotes around both repository and branch names (such as `@"example-repo"/branches/"feature/branch"/*`).
* Fixed external browser authentication (`EXTERNALBROWSER`) for headless systems.
