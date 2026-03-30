# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_2.md

| Release Number   | 1.2.2                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | March 28th, 2025                                                                    |
| Release Codename | Chicago, Patch #2                                                                   |
| Tag              | [infrahub-v1.2.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.2) |

# Release 1.2.2

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.1 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Infrahub Enterprise[​](#infrahub-enterprise "Direct link to Infrahub Enterprise")

* Fixed the `infrahub upgrade` command not working properly in Infrahub Enterprise.

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed generic schema updates to correctly propagate an updated order\_weight to a downstream attribute or relationship on an inheriting schema. ([#5684](https://github.com/opsmill/infrahub/issues/5684))
* Fixed operational status of repositories remaining to "Unknown" even after a synchronization. ([#5755](https://github.com/opsmill/infrahub/issues/5755))
* Fixed an issue that could cause the display label to not appear for nodes that have had their kind updated.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)
