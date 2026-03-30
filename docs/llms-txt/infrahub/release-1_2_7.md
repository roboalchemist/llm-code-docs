# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_2_7.md

| Release Number   | 1.2.7                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | April 28th, 2025                                                                    |
| Release Codename | Chicago, Patch #7                                                                   |
| Tag              | [infrahub-v1.2.7](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.2.7) |

# Release 1.2.7

This release brings some changes and bug-fixes to resolve issues found in Infrahub v1.2.6 and prior.

## Main changes[​](#main-changes "Direct link to Main changes")

The complete list of changes can always be found in the `CHANGELOG.md` file in the Infrahub Git repository.

### Security[​](#security "Direct link to Security")

* Update the `h11` package to 0.16.0.

### Fixed[​](#fixed "Direct link to Fixed")

* Mutating a backend node with extra attributes now logs an error instead of raising an error. It also fixes an issue preventing a corrupted node mutation. ([#6349](https://github.com/opsmill/infrahub/issues/6349))
* Improved the performance of computed attributes when updating a large number of objects at once. Replaced client.filter call in Jinja2 based computed attributes. ([#6351](https://github.com/opsmill/infrahub/issues/6351))
* Improved the IPAM allocation performance by leveraging database indexes (+10% improvement).

### Housekeeping[​](#housekeeping "Direct link to Housekeeping")

* Updated the Python `certifi` package to 2025.1.31.
* Updated Infrahub SDK to version 1.11.1.

## Upgrade guide[​](#upgrade-guide "Direct link to Upgrade guide")

Please refer to the Upgrade Guide in the documentation for more information on how to upgrade your Infrahub instance.

[Upgrade Guide](/guides/upgrade.md)

**After the upgrade, it is strongly recommended to rebase any open branches in Infrahub once the system is online again.**
