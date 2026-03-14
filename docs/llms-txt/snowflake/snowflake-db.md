# Source: https://docs.snowflake.com/en/sql-reference/snowflake-db.md

# SNOWFLAKE database

Snowflake provides a system-defined, read-only shared database named SNOWFLAKE that contains metadata and historical usage data
about the objects in your organization and accounts.
The SNOWFLAKE database is an example of [Secure Data Sharing](../guides-overview-sharing.md), and provides object metadata and other usage metrics for your organization and accounts.

In each account, the SNOWFLAKE database contains the following schemas (also read-only):

ACCOUNT_USAGE:
:   Views that display object metadata and usage metrics for your account.

ALERT:
:   Functions that are intended for use in [alert objects](../user-guide/alerts.md).

BILLING:
:   Views that contains billing information for the customers of Snowflake resellers and distributors. Only resellers and distributors
    can access the views in the BILLING schema.

CORE:
:   Contains views and other schema objects to support select Snowflake features, such as the
    [system tags](../user-guide/classify-intro.md) used with classifying data and the
    [system data metric functions](../user-guide/data-quality-system-dmfs.md) used to measure data quality.

DATA_PRIVACY:
:   Contains functions and stored procedures related to data privacy. Also contains the
    [custom_classifier class](../user-guide/classify-custom.md).

DATA_SHARING_USAGE:
:   Views that display object metadata and usage metrics related to listings published in the Snowflake Marketplace or
    a data exchange.

EXTERNAL_ACCESS:
:   Schema that contains built-in network rules specific to connections for network traffic outbound from Snowflake.
    For information about egress network rules, see [Snowflake-managed egress network rules](../user-guide/network-rules.md).

INFORMATION_SCHEMA:
:   This schema is automatically created in all databases. In a shared database, such as SNOWFLAKE, this schema doesn’t
    serve a purpose and can be disregarded.

LOCAL:
:   This schema is used by some account-level Snowflake features for logging to [telemetry event tables](../developer-guide/logging-tracing/event-table-setting-up.md).
    For more information about this schema, see [LOCAL](local.md).

ML:
:   Contains [ML functions](../guides-overview-ml-functions.md), which is a suite of analysis tools built by Snowflake, and the
    [DOCUMENT_INTELLIGENCE](classes/document-intelligence.md) class used in [Document AI](../user-guide/snowflake-cortex/document-ai/overview.md).

MONITORING:
:   Views that provide historical information for objects in your account. In the
    [Information Schema](info-schema.md), the views and table functions that return historical information will eventually be
    migrated to the MONITORING schema in the future.

NETWORK_SECURITY:
:   Schema that contains built-in network rules that define the set of allowed IP addresses that a frequently used, third-party
    partner application uses to connect with Snowflake. For more information about Snowflake-managed network rules, see [Snowflake-managed
    network rules](../user-guide/network-rules.md).

NOTIFICATION:
:   Stored procedures and functions for [sending notifications](../user-guide/notifications/snowflake-notifications.md).

ORGANIZATION_USAGE:
:   Views that display historical usage data across all the accounts in your organization.

READER_ACCOUNT_USAGE:
:   Similar to ACCOUNT_USAGE, but only contains views relevant to the reader accounts (if any) provisioned for the
    account.

SPCS:
:   Functions for use with [Snowpark Container Services](../developer-guide/snowpark-container-services/working-with-services.md).

TELEMETRY:
:   Tables, views, and stored procedures to support [collecting telemetry data](../developer-guide/logging-tracing/logging-tracing-overview.md)
    such as log messages, trace event data, and metrics data.

TRUST_CENTER:
:   Views that display data about the [Trust Center extensions](../user-guide/trust-center/trust-center-extensions.md).

Some SNOWFLAKE schemas include classes. A class is an extensible object type that encapsulates object data and code. For more information,
see [Snowflake classes](snowflake-db-classes.md).

> **Important:**
>
> By default, the SNOWFLAKE database is visible to all users. This does not mean all objects within the SNOWFLAKE database are accessible
> to all users.
>
> Objects that are not meant to be accessible by default remain inaccessible unless access is explicitly granted by a user with the
> ACCOUNTADMIN role, including access to the ACCOUNT_USAGE, READER_ACCOUNT_USAGE, ORGANIZATION_USAGE, and DATA_SHARING_USAGE schemas.
>
> Privileges to perform other actions on these views can be granted to other roles in your account. For more information, see
> [Enabling other roles to use schemas in the SNOWFLAKE database](account-usage.md).
