# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_snowflake_platform_info.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO

Returns platform information for the cloud provider that hosts your Snowflake account.
The function returns different values, depending on your cloud provider:

* For Amazon Web Services (AWS) and Microsoft Azure,
  the function returns the Amazon Virtual Private Cloud (Amazon VPC) IDs or Azure Virtual Network (VNet) IDs.

  A cloud administrator in your company can specify VPC IDs in trust policies. Doing so allows Snowflake to connect to
  the following resources, and denies requests that originate from outside of the virtual network:

  * Your cloud storage.
  * Your [proxy service](../external-functions-introduction.md) for your
    [external function](../external-functions.md).

  This security restriction can limit traffic to your cloud storage or proxy service on the same cloud platform.
* For Google Cloud, the function returns the project ID and Google Workspace customer ID associated with the Snowflake service account.

  A cloud administrator can use this information to update the domain restriction constraint in an organization policy.

For more information, see the following information for your cloud platform:

AWS:
:   [Allowing the Virtual Private Cloud IDs](../../user-guide/data-load-s3-allow.md)

GCS:
:   [Allow access to Google Cloud Storage](../../user-guide/data-load-gcs-allow.md)

Azure:
:   [Allow the VNet subnet IDs](../../user-guide/data-load-azure-allow.md)

## Syntax

```sqlsyntax
SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO()
```

## Arguments

None.

## Usage notes

Only returns results for account administrators (users with the ACCOUNTADMIN role).

## Examples

Query the IDs of the virtual network in which your Snowflake account is located:

> ```sqlexample
> SELECT SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO();
> ```
