# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_8_1.md

# Release 1.8.1

| Release Number | 1.8.1                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | March 19th, 2026                                                                    |
| Tag            | [infrahub-v1.8.1](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.8.1) |

### Added[​](#added "Direct link to Added")

* Added schema processing to schema integrity check in order to validate the schema ([#8355](https://github.com/opsmill/infrahub/issues/8355))

### Fixed[​](#fixed "Direct link to Fixed")

* Prevent multiple merge operations from running simultaneously, whether they are for the same branch or different branches. Only a single merge operation can run at a given time. Before executing any updates, the merge operation will check if the branch being merged is open to prevent merging a branch multiple times. ([#6794](https://github.com/opsmill/infrahub/issues/6794))
* Fixed read-only repository operational status after successful sync ([#8166](https://github.com/opsmill/infrahub/issues/8166))
* Fixed artifact detail page not being accessible when the artifact failed to generate ([#8394](https://github.com/opsmill/infrahub/issues/8394))
* Fixed long branch names overflowing in the branch selector and ensured the branch creation button maintains its size when disabled ([#8629](https://github.com/opsmill/infrahub/issues/8629))
