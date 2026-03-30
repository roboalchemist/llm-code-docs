# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_4_2.md

# Release 1.4.2

| Release Number | 1.4.2                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | August 28th, 2025                                                                   |
| Tag            | [infrahub-v1.4.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.4.2) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fix a bug where a proposed change could be merged without approval even if some approvals were required (Enterprise)
* Removed incorrect log warning about 'Branch schema hash is not set, cannot update branch registry' due to including the '-global-' branch when processing branch updates.
