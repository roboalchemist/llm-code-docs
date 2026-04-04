# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_4_5.md

# Release 1.4.5

| Release Number | 1.4.5                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | September 8th, 2025                                                                 |
| Tag            | [infrahub-v1.4.5](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.4.5) |

### Security[​](#security "Direct link to Security")

* Fixes bug in authentication logic that allowed expired and/or deleted API tokens to authenticate successfully.

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed an issue where switching between relationships to the same schema didn’t refresh the table correctly. ([#6418](https://github.com/opsmill/infrahub/issues/6418))
* Add initialization instructions for Infrahub repository to docs. ([#7137](https://github.com/opsmill/infrahub/issues/7137))
* Relationship properties now show a clearer loading indicator.
* Standardize internal cache-key generation using factories to make request handling easier and more consistent.
* Fixed a bug in the object table where the kind selector was not filtering its options correctly.

### Housekeeping[​](#housekeeping "Direct link to Housekeeping")

* Internal(frontend): Upgraded Biome to v2. Now use Ultracite to configure Biome
* Internal(frontend): Cleaned up unused files and functions
