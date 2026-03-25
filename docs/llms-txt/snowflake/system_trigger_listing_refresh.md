# Source: https://docs.snowflake.com/en/sql-reference/functions/system_trigger_listing_refresh.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$TRIGGER_LISTING_REFRESH

Triggers a one-time, on-demand data refresh for a provider’s databases or listings, accessible to all consumers. The refresh job begins immediately upon triggering and can be tracked using the [LISTING_REFRESH_HISTORY](listing_refresh_history.md) function. Consumers can track the refresh using the [AVAILABLE_LISTING_REFRESH_HISTORY](available_listing_refresh_history.md) function. You can trigger a listing refresh even if you have already set up a scheduled refresh or interval-based refresh.

> **Note:**
>
> A completed trigger listing refresh will skip the next interval-based refresh.

For details on the refresh types available for your listings, see [Auto-fulfillment for listings](../../collaboration/provider-listings-auto-fulfillment.md).

See also:
:   [LISTING_REFRESH_HISTORY](listing_refresh_history.md)

## Syntax

```sqlsyntax
SYSTEM$TRIGGER_LISTING_REFRESH( '<type>' , '<name>' )
```

## Arguments

**Required:**

`'type'`
:   Type of dataset to refresh (`LISTING` or `DATABASE`). Note that the dataset type must be enclosed in single quotes.

`'name'`
:   Name of the listing or database. Note that the entire name must be enclosed in single quotes.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MANAGE LISTING AUTO FULFILLMENT | Account | This privilege grants the ability to publish listings to remote regions. |
| USAGE | Listing or database |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* For share-based data product listings, the database associated with the listing is replicated and refreshed across all regions managed by
  auto-fulfillment.
* Application and application package data product listings refresh according to the value of the [LISTING_AUTO_FULFILLMENT_REPLICATION_REFRESH_SCHEDULE](../parameters.md)
  parameter set on the account. All listings using this schedule are refreshed simultaneously.

## Examples

```sqlexample
SELECT SYSTEM$TRIGGER_LISTING_REFRESH('DATABASE', 'MY_DATABASE');
```
