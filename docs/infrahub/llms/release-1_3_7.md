# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_3_7.md

# Release 1.3.7

| Release Number | 1.3.7                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | August 14th, 2025                                                                   |
| Tag            | [infrahub-v1.3.7](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.3.7) |

### Fixed[​](#fixed "Direct link to Fixed")

* Ensure that only users with "manage schema" permissions can add or remove dropdown and enum values ([#6410](https://github.com/opsmill/infrahub/issues/6410))
* Fix bug in branch delete cypher query that could leave behind orphaned branch-agnostic relationships. Includes a migration to clean up these orphaned relationships. ([#6933](https://github.com/opsmill/infrahub/issues/6933))
* Fix bug in display label rendering that prevented schemas from defining display labels with the same attribute names in different ways (`name` vs `name__value`, for example) ([#7022](https://github.com/opsmill/infrahub/issues/7022))
* Fix resource pool allocation on concurrent mutations. Assignments from the resource pools are now done within a lock to prevent invalid assignments that might occur during concurrent requests.
