# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_11.md

| Release Number   | 1.2.11                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | May 23rd, 2025                                                                        |
| Release Codename | Chicago, Patch #11                                                                    |
| Tag              | [infrahub-v1.2.11](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.11) |

# Release 1.2.11

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.10 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Added[​](#added "Direct link to Added")

* Add the `CoreWeightedPoolResource` generic to better control which resource should be used when allocating from a pool. The higher the weight of the resource, the more likely it is to be selected for allocation.

### Changed[​](#changed "Direct link to Changed")

* The scrollbar in the infinite scroll tables, is now only visible when your mouse hovers the table.

### Fixed[​](#fixed "Direct link to Fixed")

* Fix a problem in the logic to calculate a diff that could cause it to quit too early under certain unlikely circumstances
* Fixes an issue where the next page of data was loaded even when the infinite scroll table wasn't scrolled.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)

**After the upgrade, it is strongly recommended to rebase any open branches in Infrahub once the system is online again.**
