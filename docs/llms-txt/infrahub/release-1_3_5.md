# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_3_5.md

# Release 1.3.5

| Release Number | 1.3.5                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | August 5th, 2025                                                                    |
| Tag            | [infrahub-v1.3.5](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.3.5) |

### Added[​](#added "Direct link to Added")

* Add a new check for orphaned Relationship vertices to `infrahub db check`

### Fixed[​](#fixed "Direct link to Fixed")

* Fix repository objects view when there is no group tied to the repository [repository-objects](https://github.com/opsmill/infrahub/issues/repo-objects)
* Prevent Python keywords from being used as attribute/relationship names in schemas. Schema validation now rejects Python keywords (like `from`, `class`, `import`) as attribute or relationship names, preventing 500 errors during GraphQL schema generation. ([#6730](https://github.com/opsmill/infrahub/issues/6730))
* Fix bug in diff calculation logic that could prevent the diff from generating if the peer of a deleted node had its kind or inheritance changed on multiple branches ([#6928](https://github.com/opsmill/infrahub/issues/6928))
* Fix an issue in a cypher query to get the peers of a node that has been migrated for a kind or inheritance update.
* Fix an issue in the diff calculation that could double count properties of a node that has been migrated for a kind or inheritance update.
