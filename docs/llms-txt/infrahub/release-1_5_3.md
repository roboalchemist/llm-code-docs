# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_5_3.md

# Release 1.5.3

| Release Number | 1.5.3                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | November 24th, 2025                                                                 |
| Tag            | [infrahub-v1.5.3](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.5.3) |

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed bug that prevented retrieving cardinality-one relationships on a branch that was already merged and included changes to the relationship. This bug would be visible to the user as errors that look like `ValidationError: Too many relationships, max 1 at field_name` ([#7338](https://github.com/opsmill/infrahub/issues/7338))
* Enable caching of the task count in order to avoid performance issues when having a long task history. ([#7568](https://github.com/opsmill/infrahub/issues/7568))
* Refactor task setup to avoid excessive tasks being scheduled for branches that previously didn't contain tasks. The updated behaviour is that the task will only be triggered on the branch if the task signature differs from that of the default branch. ([#7692](https://github.com/opsmill/infrahub/issues/7692))
* Delete branch-aware human friendly ID and display label attributes from branch-agnostic nodes if they were erroneously added. Add branch-agnostic human friendly ID and display label attributes to branch-agnostic nodes and set their values. ([#7694](https://github.com/opsmill/infrahub/issues/7694))
