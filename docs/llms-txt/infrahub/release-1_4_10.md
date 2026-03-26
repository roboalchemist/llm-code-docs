# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_4_10.md

# Release 1.4.10

| Release Number | 1.4.10                                                                                |
| -------------- | ------------------------------------------------------------------------------------- |
| Release Date   | October 1st, 2025                                                                     |
| Tag            | [infrahub-v1.4.10](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.4.10) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fix issue with template that would set the value/source of all attributes even for the attribute that are not defined in the template. ([#7259](https://github.com/opsmill/infrahub/issues/7259))
* Fix bug in artifact diff cypher query that could improperly exclude artifacts on the default branch ([#7301](https://github.com/opsmill/infrahub/issues/7301))

### Housekeeping[​](#housekeeping "Direct link to Housekeeping")

* Update docs to download compose file first and then run compose up/down. This change was made due to community members using the one liner for long standing installations without the docker-compose.yml file locally. The new approach is more explicit and easier for the community to maintain their Infrahub instances in the future. ([#compose](https://github.com/opsmill/infrahub/issues/compose))
