# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_3.md

| Release Number   | 1.2.3                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | March 31st, 2025                                                                    |
| Release Codename | Chicago, Patch #3                                                                   |
| Tag              | [infrahub-v1.2.3](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.3) |

# Release 1.2.3

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.2 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Added[​](#added "Direct link to Added")

* Added support for Jinja2 filters from Netutils. ([#5899](https://github.com/opsmill/infrahub/issues/5899))

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed the menu upgrade when Non-Builtin items are attached to a Builtin menu item. ([#6182](https://github.com/opsmill/infrahub/issues/6182))
* Added a migration to backfill hierarchy data missing from the default branch after a branch is merged and then deleted. The root cause of the missing data has already been fixed. ([#6019](https://github.com/opsmill/infrahub/issues/6019))
* Fixed a broken hierarchy when renaming a kind participating to a hierarchy. ([#6051](https://github.com/opsmill/infrahub/issues/6051))
* Fixed the schema migration validator to allow renaming the kind of a generic. ([#6060](https://github.com/opsmill/infrahub/issues/6060))
* Fixed an error in IPAM reconciliation logic to correctly assign 0.0.0.0/0 as a parent prefix. ([#6172](https://github.com/opsmill/infrahub/issues/6172))
* Ensured that node level migrations are not executed on a generic.
* Fixed updating a node through Upsert when payload contains existing unique attributes not part of HFID.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)
