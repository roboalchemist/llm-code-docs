# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_4_4.md

# Release 1.4.4

| Release Number | 1.4.4                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | September 3rd, 2025                                                                 |
| Tag            | [infrahub-v1.4.4](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.4.4) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fix HTTP 403 when trying to fetch object metadata in changelog without being allowed to manage permissions ([#ifc1760](https://github.com/opsmill/infrahub/issues/ifc1760))
* Fix HTTP 403 when trying to fetch nodes though a `CoreNode` query, this could prevent users to select nodes in various places with the user interface ([#6733](https://github.com/opsmill/infrahub/issues/6733))
* Re-run Migration026 in case it failed during an upgrade from 1.2.4 or earlier to 1.4.x or later. Root cause of the migration failure has already been addressed. ([#7112](https://github.com/opsmill/infrahub/issues/7112))
* Fixed rebase bug by ensuring rebase operations with data only changes correctly set the .branched\_from property of the branch within the registry. ([#7113](https://github.com/opsmill/infrahub/issues/7113))
* UI requests for proposed change objects are now branch-agnostic, preventing errors when a branch is deleted

### Housekeeping[​](#housekeeping "Direct link to Housekeeping")

* Internal UI: Decouple configuration fetching from usage
