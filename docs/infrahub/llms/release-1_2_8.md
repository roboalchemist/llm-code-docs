# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_8.md

| Release Number   | 1.2.8                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | May 1st, 2025                                                                       |
| Release Codename | Chicago, Patch #8                                                                   |
| Tag              | [infrahub-v1.2.8](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.8) |

# Release 1.2.8

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.7 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Added[​](#added "Direct link to Added")

* Added support for "convert\_query\_response" for Python Transformations. The feature works the same way as with Generators. Note any non-default branch will need to be rebased after this upgrade. ([#6383](https://github.com/opsmill/infrahub/issues/6383))
* Enabled HCL syntax highlighting for artifacts.

### Fixed[​](#fixed "Direct link to Fixed")

* Improved performance when retrieving nodes that have thousands of relationships.
* Improved performance of the Git credential helper.

### Housekeeping[​](#housekeeping "Direct link to Housekeeping")

* Background performance improvements due to Prefect 3.3.7 upgrade.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)

**After the upgrade, it is strongly recommended to rebase any open branches in Infrahub once the system is online again.**
