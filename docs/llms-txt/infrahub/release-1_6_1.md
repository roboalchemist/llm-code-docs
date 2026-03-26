# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_6_1.md

# Release 1.6.1

| Release Number | 1.6.1                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | December 11th, 2025                                                                 |
| Tag            | [infrahub-v1.6.1](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.6.1) |

### Added[​](#added "Direct link to Added")

* Add support for PKCE within Oauth2 and OIDC authentications. With this change the client\_secret for Oauth2 and OIDC have been switched to being optional. PKCE is enabled by default but can be switched off in the configuration if required. ([#7400](https://github.com/opsmill/infrahub/issues/7400))

### Changed[​](#changed "Direct link to Changed")

* Upgrade infrahub-sdk to v1.17.0 ([#7870](https://github.com/opsmill/infrahub/pull/7870))

### Fixed[​](#fixed "Direct link to Fixed")

* Fixed bug that prevented retrieving cardinality-one relationships on a branch that was already merged and included changes to the relationship. This bug would be visible to the user as errors that look like `ValidationError: Too many relationships, max 1 at field_name` ([#7338](https://github.com/opsmill/infrahub/issues/7338))
* Enable caching of the task count in order to avoid performance issues when having a long task history. ([#7568](https://github.com/opsmill/infrahub/issues/7568))
* Refactor task setup to avoid excessive tasks being scheduled for branches that previously didn't contain tasks. The updated behaviour is that the task will only be triggered on the branch if the task signature differs from that of the default branch. ([#7692](https://github.com/opsmill/infrahub/issues/7692))
* Delete branch-aware human friendly ID and display label attributes from branch-agnostic nodes if they were erroneously added. Add branch-agnostic human friendly ID and display label attributes to branch-agnostic nodes and set their values. ([#7694](https://github.com/opsmill/infrahub/issues/7694))
