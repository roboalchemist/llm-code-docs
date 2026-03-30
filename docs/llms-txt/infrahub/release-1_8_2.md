# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_8_2.md

# Release 1.8.2

| Release Number | 1.8.2                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | March 25th, 2026                                                                    |
| Tag            | [infrahub-v1.8.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.8.2) |

### Changed[​](#changed "Direct link to Changed")

* This change prevents redundant artifact regenerations by only triggering on node changes that affect fields actually read by the associated GraphQL query, reducing the number of artifacts that need to be regenerated and speeding up the pipeline.

### Fixed[​](#fixed "Direct link to Fixed")

* Fix scheduled reconfiguration of webhooks targeting "all" events ([#8694](https://github.com/opsmill/infrahub/issues/8694))
* Fixed branch rebase conflicts during 1.7 to 1.8 upgrades caused by migration 056 writing unrelated schema attributes to branch timelines
