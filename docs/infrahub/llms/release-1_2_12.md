# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_12.md

| Release Number   | 1.2.12                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | June 3rd, 2025                                                                        |
| Release Codename | Chicago, Patch #12                                                                    |
| Tag              | [infrahub-v1.2.12](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.12) |

# Release 1.2.12

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.11 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Fixed[​](#fixed "Direct link to Fixed")

* Remove uniqueness constraint on generic templates to support upsert mutations ([#6478](https://github.com/opsmill/infrahub/issues/6478))
* Add a migration to clean up duplicated data from improper merges of branches containing node schemas with an updated kind or inheritance ([#6502](https://github.com/opsmill/infrahub/issues/6502))
* Update the cypher query that saves a diff to use less memory. ([#6568](https://github.com/opsmill/infrahub/issues/6568))
* Add missing database session instantiations
* Display generic relationships with cardinality one in the object detail view.
* Fixes schema migration to add new attributes, so that it no longer adds that attribute to nodes that have been deleted. Includes a migration to clean up those illegal edges.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)

**After the upgrade, it is strongly recommended to rebase any open branches in Infrahub once the system is online again.**
