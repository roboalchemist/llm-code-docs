# Source: https://docs.airbyte.com/platform/understanding-airbyte/airbyte-protocol-versioning.md

# Source: https://docs.airbyte.com/platform/2.0/understanding-airbyte/airbyte-protocol-versioning.md

# Source: https://docs.airbyte.com/platform/1.8/understanding-airbyte/airbyte-protocol-versioning.md

# Source: https://docs.airbyte.com/platform/1.7/understanding-airbyte/airbyte-protocol-versioning.md

# Source: https://docs.airbyte.com/platform/1.6/understanding-airbyte/airbyte-protocol-versioning.md

# Airbyte Protocol Versioning

Copy Page

## Goal[​](#goal "Direct link to Goal")

The goal of this document is to define our approach to protocol changes.

We need a compromise between frequent breaking changes that are heavy on operations and infinite backward compatibility which is a burden from a software engineering point of view.

## Versioning Scheme[​](#versioning-scheme "Direct link to Versioning Scheme")

We are using a `<MAJOR>.<MINOR>.<PATCH>` scheme for the Protocol Versioning. (see [SemVer](https://semver.org/)).

We increment the

* MAJOR version when you make incompatible protocol changes
* MINOR version when you add functionality in a backwards compatible manner
* PATCH version when you make backwards compatible bug fixes

## Development Guidelines[​](#development-guidelines "Direct link to Development Guidelines")

1. We will continue to do our best effort to avoid introducing breaking changes to the Airbyte Protocol.
2. When introducing a new minor version of the Airbyte Protocol, new fields must come with sensible defaults for backward compatibility within the same major version, or be entirely optional.
3. When introducing a new major version of the Airbyte Protocol, all connectors from the previous major version will continue to work. This requires the ability to “translate” messages between 1 major version of the Airbyte Protocol.

## Safeguards[​](#safeguards "Direct link to Safeguards")

To ensure continuous operation, we have a few safeguards to prevent breaking existing configuration through protocol version incompatibilities.

### When upgrading Airbyte[​](#when-upgrading-airbyte "Direct link to When upgrading Airbyte")

When removing support for older versions of the Protocol, there is a risk removing the support for a version that is currently used.

To mitigate this, as part of the pre-upgrade checks that happens in the `airbyte-bootloader`, we verify that any connector currently part of an active connection will still be supported after the upgrade.

If any connector fails this check, we abort the upgrade and the `airbyte-bootloader` logs contains a list of connectors to upgrade. Those connectors will need to be upgraded from the UI before the platform itself can be upgraded.

### When upgrading a Connector[​](#when-upgrading-a-connector "Direct link to When upgrading a Connector")

When upgrading a Connector from the UI, we will verify that the Protocol Version is supported before finalizing the Connector upgrade.
