# Source: https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/unbundled-cancelled-behavior-changes.md

# Canceled unbundled behavior changes

Canceled unbundled behavior changes are changes that were originally intended to be released but have been canceled and will not be implemented.

To help you manage your operations and minimize disruption to your Snowflake service, we document behavior changes that may impact your usage,
including:

* [Recently implemented changes](unbundled-behavior-changes.md) that were previously pending/disabled, were not part of a behavior change bundle, and cannot be disabled.
* [Upcoming pending changes](unbundled-behavior-changes.md) that will not be part of a behavior change bundle and cannot be enabled in advance.

If you have questions about any of these behavior changes, please feel free to contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

## Canceled unbundled behavior changes

The following table lists canceled behavior changes. Canceled behavior changes are behavior changes that have been previously planned but will not be implemented.

| Originally Planned BCR Bundle | Functional Area | Canceled Behavior Change | Additional Notes |
| --- | --- | --- | --- |
| [2025_06 Bundle](../2025_06_bundle.md) | Security | [OAuth authentication: Change in network policy behavior (Canceled)](bcr-2094.md) |  |
| [2025_04 Bundle](../2025_04_bundle.md) | Security | [Mandatory multi-factor authentication on Snowsight login (Replaced)](bcr-1972.md) | Replaced by [Multi-factor authentication: MFA_ENROLLMENT parameter values change](../2025_06/bcr-2097.md) |
| [2025_04 Bundle](../2025_04_bundle.md) | Snowpark Python | [Snowpark Python: Eliminate repeated subqueries in Snowpark-generated queries (Canceled)](bcr-1995.md) |  |
| [2024_08 Bundle](../2024_08_bundle.md) | Data Governance | [Use primary role for authorizing view and materialized view creation (Canceled)](bcr-1782.md) |  |
| [2024_08 Bundle](../2024_08_bundle.md) | Security | [GRANT OWNERSHIP ON ROLE command: Restrict transfer of role ownership to itself (Canceled)](bcr-1781.md) |  |
