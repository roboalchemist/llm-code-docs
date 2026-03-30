# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_6_2.md

# Release 1.6.2

| Release Number | 1.6.2                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | December 22nd, 2025                                                                 |
| Tag            | [infrahub-v1.6.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.6.2) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fix Migration041 to determine edge uniqueness correctly and account for incoming Relationship edges. Add new migration to un-delete improperly deleted Relationship metadata. This would only be a problem for Relationships between schemas that have both had their name, namespace, or kind updated multiple times. ([#7916](https://github.com/opsmill/infrahub/issues/7916))
