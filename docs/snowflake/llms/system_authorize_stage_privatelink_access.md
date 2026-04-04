# Source: https://docs.snowflake.com/en/sql-reference/functions/system_authorize_stage_privatelink_access.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS

Authorizes Snowflake to access the private endpoint for [Azure private endpoints for internal stages](../../user-guide/private-internal-stages-azure.md) and
[Google Private Service Connect endpoints for internal stages](../../user-guide/private-internal-stages-gcp.md) for the current account.

See also:
:   [SYSTEM$REVOKE_STAGE_PRIVATELINK_ACCESS](system_revoke_stage_privatelink_access.md)

## Syntax

**Azure**

```sqlsyntax
SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS( '<private_endpoint_resource_id>' )
```

**Google Cloud**

```sqlsyntax
SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS( '<google_cloud_vpc_network_name>' )
```

## Arguments

`'private_endpoint_resource_id'`
:   The unique identifier for the Azure Private Endpoint.

`'google_cloud_vpc_network_name'`
:   The fully qualified path value for the Google Cloud VPC Network.

    This value is from the Google Cloud VPC network path that Snowflake uses to limit access to your internal stage through the cloud provider’s internal network and avoid using the public internet.

    For instructions on how to obtain this value on Azure, see [Configuring private endpoints to access Snowflake internal stages](../../user-guide/private-internal-stages-azure.md); for Google Cloud, see [Configure private endpoints to access Snowflake internal stages](../../user-guide/private-internal-stages-gcp.md).

## Usage notes

* Only account administrators (that is, users with the ACCOUNTADMIN role) can call this function.
* This function is not supported for Snowflake accounts on
  Amazon Web Services (AWS).

## Examples

**Azure**

Authorize Snowflake to access an Azure private endpoint:

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> SELECT SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS('/subscriptions/subId/resourceGroups/rg1/providers/Microsoft.Network/privateEndpoints/pe1');
> ```

**Google Cloud**

Authorize Snowflake to access a Google Private Service Connect endpoint:

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> SELECT SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS('projects/vpc_network_name/global/networks/network_name');
> ```
