# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-01-organization-usage-new-views.md

# Feb 01, 2026: New ORGANIZATION_USAGE premium views

The ORGANIZATION_USAGE schema now includes three new [premium views](../../../user-guide/organization-accounts-premium-views.md)
that are available in the [organization account](../../../user-guide/organization-accounts.md). These views provide
visibility into usage across all accounts in your organization.

The new views are:

* [METERING_HISTORY](../../../sql-reference/organization-usage/metering_history.md) — Returns hourly credit usage for each account in your organization.
* [QUERY_ATTRIBUTION_HISTORY](../../../sql-reference/organization-usage/query_attribution_history.md) — Attributes compute costs to specific queries run on warehouses in your organization.

For more information about accessing premium views in the organization account, see [Access schema in the organization account](../../../sql-reference/organization-usage.md).

> **Note:**
>
> The new premium views are being rolled out slowly and should be available to all accounts by February 9, 2026.
