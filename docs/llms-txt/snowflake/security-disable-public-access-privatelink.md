# Source: https://docs.snowflake.com/en/user-guide/security-disable-public-access-privatelink.md

# Enforcement of privatelink-only access

## Overview

Each Snowflake customer can access their Snowflake account using their customer-specific, dedicated account URLs and generic Snowflake UI
URLs. Enabling private connectivity establishes private URLs for your account. After establishing private connectivity, the private URLs
that you use to connect to Snowflake must include “privatelink”. For example, the host URL can have the following formats:

* Account Name: `https://<orgname>-<account_name>.privatelink.snowflakecomputing.com`
* Connection Name: `https://<orgname>-<connectionname>.privatelink.snowflakecomputing.com`
* Account Locator (legacy): `https://<account_locator>.<region>.privatelink.snowflakecomputing.com`

Accounts that use only privatelink for inbound connections to Snowflake are also known as “privatelink-only” accounts. For more information
about using URLs to connect to your Snowflake account, see [Connecting with a URL](organizations-connect.md).

You can harden your security posture by disabling public access to your privatelink-only accounts. For example, after you disable public
access to your privatelink-only accounts, anyone attempting to “guess” your Snowflake account URL by providing a public URL sees a static
web page that displays: `HTTP - 404 account not found`. Snowflake Core Service checks requests incoming from the public internet before
requesting authorization. Returning `HTTP - 404 account not found` provides no indication that the account exists. In this way, disabling
public access protects your privatelink-only accounts.

> **Important:**
>
> Connect to your account using private connectivity, then run the [SYSTEM$ENFORCE_PRIVATELINK_ACCESS_ONLY](../sql-reference/functions/system_enforce_privatelink_access_only.md)
> command. Any SaaS service that does not support private connectivity cannot connect to Snowflake after you have disabled public access to
> your privatelink-only accounts.

Disabling public access to your privatelink-only accounts:

* Disables **public** access to all Snowflake service endpoints only.
* Does not affect public access to internal stage buckets.

### Granular network access restrictions

You can define granular access to your account by creating network rules that restrict network access through specific private endpoint IDs.
You can also define network rules to limit or deny publicly-routed sessions. For more information, see [CREATE NETWORK RULE](../sql-reference/sql/create-network-rule.md).

To enforce the access definitions, you can create network policies that use your network rule definitions. For more information,
see [Controlling network traffic with network policies](network-policies.md).

> **Note:**
>
> Blocking access to private endpoints using network rules is not (yet) supported on Google Cloud.

## Disable public access to your privatelink-only accounts

To disable public access to all Snowflake service endpoints in your Snowflake account:

1. Verify or establish private connectivity to your account.
2. Call the [SYSTEM$ENFORCE_PRIVATELINK_ACCESS_ONLY](../sql-reference/functions/system_enforce_privatelink_access_only.md) function.

## Restore public access to your privatelink-only accounts

To restore public access to all Snowflake service endpoints in your Snowflake account, call the [SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY](../sql-reference/functions/system_disable_privatelink_access_only.md) function.

## Restrict access to the function that restores public access

Customers who want to restrict their account administrators from restoring public access for inbound network traffic must request that
Snowflake modify their account.

To restrict access to the SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY function:

1. Contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).
2. Request that Snowflake restrict access to the SYSTEM$DISABLE_PRIVATELINK_ACCESS_ONLY function for your account.
