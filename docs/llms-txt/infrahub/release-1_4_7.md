# Source: https://docs.infrahub.app/release-notes/infrahub/release-1_4_7.md

# Release 1.4.7

| Release Number | 1.4.7                                                                               |
| -------------- | ----------------------------------------------------------------------------------- |
| Release Date   | September 16th, 2025                                                                |
| Tag            | [infrahub-v1.4.7](https://github.com/opsmill/infrahub/releases/tag/infrahub-v1.4.7) |

### Added[​](#added "Direct link to Added")

* Added optional configuration to fetch and map groups when using Google as an identity provider for OAuth/OIDC.
* Added the name of the artifact definition to the payload of artifact webhook events.

### Fixed[​](#fixed "Direct link to Fixed")

* Allow RequestGraphQLQueryGroupUpdate parameters to accept any type of value, not just strings. ([#7208](https://github.com/opsmill/infrahub/issues/7208))
* The available IPs filter in IPAM list views now stays applied when switching kind.
