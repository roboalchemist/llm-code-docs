# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_5_2.md

# Release 1.5.2

| Release Number | 1.5.2                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | November 18th, 2025                                                                 |
| Tag            | [infrahub-v1.5.2](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.5.2) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fix migration that backfills display labels and human-friendly IDs to account for schema that only exist on the branch being migrated. Add new migration to add display labels and human-friendly IDs to existing instances of templates and profiles. ([#7655](https://github.com/opsmill/infrahub/issues/7655))
* Prevent attempting diff update on a deleted branch. Log a warning instead. ([#7666](https://github.com/opsmill/infrahub/issues/7666))
