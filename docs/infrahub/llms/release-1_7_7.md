# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_7_7.md

# Release 1.7.7

| Release Number | 1.7.7                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | March 12th, 2026                                                                    |
| Tag            | [infrahub-v1.7.7](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.7.7) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed display labels showing 'None' for relationship-based fields after upsert. Relationship peer attributes needed by display label and HFID templates are now correctly loaded during node updates. Includes a migration to correct objects that had their display labels and or human-friendly IDs improperly updated to include a null value.
