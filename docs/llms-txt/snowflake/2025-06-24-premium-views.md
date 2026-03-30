# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-06-24-premium-views.md

# Jun 24, 2025: Premium views in the organization account (*General availability*)

The ORGANIZATION_USAGE schema in the organization account contains premium views that aggregate account usage across accounts. These premium
views are not found in the ORGANIZATION_USAGE schema of a regular ORGADMIN-enabled account, and incur additional storage and compute costs.
For example, the organization account lets you query premium views to track login history, access history, and query history across the
organization.

For more information, see [Premium views in the organization account](../../../user-guide/organization-accounts-premium-views.md).
