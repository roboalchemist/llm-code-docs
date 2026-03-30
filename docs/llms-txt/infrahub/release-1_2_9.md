# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_9.md

| Release Number   | 1.2.9                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | May 7th, 2025                                                                       |
| Release Codename | Chicago, Patch #9                                                                   |
| Tag              | [infrahub-v1.2.9](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.9) |

# Release 1.2.9

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.8 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Added[​](#added "Direct link to Added")

* Added the `INFRAHUB_TESTING_SCHEMA_STRICT_MODE` environment variable to allow users to control `INFRAHUB_SCHEMA_STRICT_MODE` when using `infrahub-testcontainers`.
* Improved the performance of the core database class used throughout the backend by factoring out the classes used for creating and removing indexes.

### Changed[​](#changed "Direct link to Changed")

* Sped up computed attribute mutation by changing the node query to only request the required attributes from the database. This change will provide performance improvements for the background processing of computed attributes. ([#6403](https://github.com/opsmill/infrahub/issues/6403))

### Fixed[​](#fixed "Direct link to Fixed")

* Deleting a branch now correctly deletes nodes with agnostic relationships. This typically fixes an issue after deleting a branch where an object had been created on this branch through a ResourceManager ([#5463](https://github.com/opsmill/infrahub/issues/5463))
* Fixed `textarea` values display in the object details view. ([#6400](https://github.com/opsmill/infrahub/issues/6400))
* Added inherited kinds of a node as templates to fix GraphQL schema when inheritance is involved. ([#6415](https://github.com/opsmill/infrahub/issues/6415))
* Fixed an issue with computed attribute that would trigger multiple updates after a schema change if the attribute reference multiple kind of nodes.
* Updated the date formatting to include the year for dates before the current year, and ensure consistency between the list and detail views.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)

**After the upgrade, it is strongly recommended to rebase any open branches in Infrahub once the system is online again.**
