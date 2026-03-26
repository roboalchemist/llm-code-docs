# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_3_3.md

# Release 1.3.3

| Release Number   | 1.3.3                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| Release Date     | July 15th, 2025                                                                     |
| Release Codename | Amsterdam                                                                           |
| Tag              | [infrahub-v1.3.3](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.3.3) |

### Added[​](#added "Direct link to Added")

* Added the `infrahub db check` command to look for illegal data in the database
* Add a command to run a single migration
* Updated GraphQL sandbox to GraphiQL 5

### Fixed[​](#fixed "Direct link to Fixed")

* Fix upsert mutation for webhooks ([#6641](https://github.com/opsmill/infrahub/issues/6641))
* Prevent a merge operation and a diff update from running at the same time on the same branch ([#6704](https://github.com/opsmill/infrahub/issues/6704))
* Fix branch delete logic to handle very large branches (millions of edges) and add a migration to clean up any partially deleted branches ([#6797](https://github.com/opsmill/infrahub/issues/6797))
* Explicitly expose port 7687 for Neo4j to ensure the integration tests are running on all setup
* Fix a bug in node creating that could cause duplicate relationships if the node being created included a relationship to a node of a schema that had its kind or inheritance updated in the past
* Fix an issue where prefixes could not be allocated from a pool when passing `member_type` inside the data parameter
* Migration to clean up duplicated relationships
