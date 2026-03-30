# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_7_6.md

# Release 1.7.6

| Release Number | 1.7.6                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | February 25th, 2026                                                                 |
| Tag            | [infrahub-v1.7.6](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.7.6) |

### Fixed[​](#fixed "Direct link to Fixed")

* Pass order weights into Profile schema fields to prevent reordering causing a hash mismatch
* Update schema validation and processing to be completely idempotent to prevent incorrect hash errors when retrieving schemas
