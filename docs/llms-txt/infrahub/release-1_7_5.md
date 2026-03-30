# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_7_5.md

# Release 1.7.5

| Release Number | 1.7.5                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | February 23rd, 2026                                                                 |
| Tag            | [infrahub-v1.7.5](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.7.5) |

### Removed[​](#removed "Direct link to Removed")

* Removed unused `enable` configuration toggle from broker, cache, and workflow settings

### Fixed[​](#fixed "Direct link to Fixed")

* Add migration to handle setting duplicated schemas on the default branch to be deleted, keeping the one with the latest update ([#8221](https://github.com/opsmill/infrahub/issues/8221))
* Handle deleted parent relationship schemas when combining diffs without crashing ([#8388](https://github.com/opsmill/infrahub/issues/8388))
* Prevent saving generated "profiles" and "object\_template" schema relationships to the database. Includes a migration to clean up any already on the database. ([#8426](https://github.com/opsmill/infrahub/issues/8426))
* Fixed regression (introduced in Infrahub 1.5) regarding merge performance. ([#8438](https://github.com/opsmill/infrahub/issues/8438))
* Add full support for updating existing Template instances via schema migrations when the associated node or generic schema is updated in a manner that would add or remove attributes to or from the Template's schema.
* Adds automatic retries to database queries during a branch merge to handle transient errors
* Allow generating Template schemas for both a generic schema and a node inheriting from that generic. Previously, schema validation would raise a validation error and prevent this.
* Fixed an issue where Infrahub was calculating the wrong authentication signature caused by HTTPX v0.28.0 switching to compact JSON payload encoding.
* Fixed issue where system user showed as the last user changing a proposed change after merge
