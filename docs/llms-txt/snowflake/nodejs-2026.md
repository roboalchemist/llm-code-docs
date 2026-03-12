# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/nodejs-2026.md

# Node.js Driver release notes for 2026

This article contains the release notes for the Node.js Driver, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

Snowflake uses semantic versioning for Node.js Driver updates.

See [Node.js Driver](../../developer-guide/node-js/nodejs-driver.md) for documentation.

## Version 2.3.4 (Feb 09, 2026)

### New features and updates

* Reduced memory usage during PUT operations.
* Added `APPLICATION_PATH` to `login-request` telemetry.
* Added Linux distribution details parsed from `/etc/os-release` to `login-request` telemetry.
* Bumped axios to version 1.13.4 to address a bug in axios interceptors.
* Bumped other dependencies to their latest minor versions.

### Bug fixes

* Fixed inconsistent retry behavior across HTTP requests and ensured all recoverable failures are properly retried.
* Fixed invalid oauth scope when `role` and `oauthScope` are missing from the connection configuration.
* Fixed `APPLICATION` field not being passed from the connection configuration to `login-request` telemetry.
* Fixed build errors in bundlers caused by the `minicore` module.
