# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_4_6.md

# Release 1.4.6

| Release Number | 1.4.6                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | September 10th, 2025                                                                |
| Tag            | [infrahub-v1.4.6](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.4.6) |

### Added[​](#added "Direct link to Added")

* Make related nodes clickable in task views ([#6420](https://github.com/opsmill/infrahub/issues/6420))
* Add an option to match trigger actions on any attribute value

### Fixed[​](#fixed "Direct link to Fixed")

* Fix bug in IP reconciliation that could cause prefixes or addresses updated on a branch to have incorrect parents or children. ([#6934](https://github.com/opsmill/infrahub/issues/6934))
* Fixed the accepted types for the query payload in the `execute_query` POST endpoint. ([#7119](https://github.com/opsmill/infrahub/issues/7119))
* Fixed issue where the artifact diff view would randomly add space characters to the diff content and highlight it as a diff. ([#6974](https://github.com/opsmill/infrahub/issues/6974))
