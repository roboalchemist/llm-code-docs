# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_6.md

| Release Number   | 1.2.6                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | April 18th, 2025                                                                    |
| Release Codename | Chicago, Patch #6                                                                   |
| Tag              | [infrahub-v1.2.6](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.6) |

# Release 1.2.6

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.5 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Added[​](#added "Direct link to Added")

* Added generics to node selection in number pool form.
* Enabled node select in the webhook form to quickly choose the node kind.

### Changed[​](#changed "Direct link to Changed")

* Raised a more accurate error when trying to lookup a node by HFID, specifically when the schema does not have an HFID or the number of elements does not match.

### Fixed[​](#fixed "Direct link to Fixed")

* Cleared GraphQL schema manager cache when deleting branches to release memory. ([#6021](https://github.com/opsmill/infrahub/issues/6021))
* Added attributes and relationships to generic templates to ensure proper GraphQL schema generation. ([#6287](https://github.com/opsmill/infrahub/issues/6287))
* Fixed node lookup by its HFID with a generic template kind. ([#6301](https://github.com/opsmill/infrahub/issues/6301))
* Disabled option creation for restricted namespaces in dropdown and enum.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)
