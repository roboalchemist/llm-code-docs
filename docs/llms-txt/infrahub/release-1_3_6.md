# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_3_6.md

# Release 1.3.6

| Release Number | 1.3.6                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | August 11th, 2025                                                                   |
| Tag            | [infrahub-v1.3.6](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.3.6) |

### Added[​](#added "Direct link to Added")

* Add the `infrahub db check-inheritance` command to validate and fix any schemas that have had their inheritance updated and a failed migration.

### Changed[​](#changed "Direct link to Changed")

* Improve performance of node creation, for nodes with a high number of relationships ([#6883](https://github.com/opsmill/infrahub/pull/6883))
