# Source: https://docs.snowflake.com/en/sql-reference/functions/system_restore_privatelink_endpoint_tss.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS

Restores a private connectivity endpoint in the Snowflake VPC or VNet to enable Snowflake to connect to an external key management service (KMS) resource
by using private connectivity. The endpoint can be a service endpoint or a resource endpoint, depending on the cloud platform that hosts your
Snowflake account.

You can restore a private endpoint within 7 days of deprovisioning it. After 7 days, the endpoint cannot be restored and you need to
recreate the endpoint with the [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT_TSS](system_provision_privatelink_endpoint_tss.md) system function.

## Syntax

**AWS:**

```sqlsyntax
SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS(
  '<provider_service_name>'
  )
```

**Azure:**

```sqlsyntax
SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS(
  '<provider_resource_id>'
  )
```

**Google Cloud:**

```sqlsyntax
SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS(
  '<target_service_id>'
  )
```

## Arguments

**AWS:**

`provider_service_name`
:   Specifies the external KMS resource endpoint to restore.

**Azure:**

`provider_resource_id`
:   Specifies the fully-qualified identifier for the resource in your VPC or VNet.

**Google Cloud:**

`target_service_id`
:   Specifies the service attachment ID (to a custom service), or regional Google API endpoint to connect to.

## Returns

Returns a status message stating that the endpoint, with its identifier, is restored successfully.

If unsuccessful, returns an error — for example, if the provided argument is not a valid existing endpoint. If you do not know the endpoint
name, you can use the [SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO](system_get_privatelink_endpoints_info.md) system function to list all endpoints in your
Snowflake account.

## Access control requirements

Only account administrators (users with the ACCOUNTADMIN role) can call this function.

## Usage notes

An error message occurs if a private connectivity endpoint is not associated with the specified arguments.

## Examples

**AWS:**

Restore a private endpoint with external access to an AWS key store.

```sqlexample
SELECT SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS(
  'com.amazonaws.us-west-2.s3'
);
```

**Azure:**

Restore a private endpoint to allow Snowflake on Microsoft Azure to connect to the Azure key vault in your Azure VNet:

```sqlexample
SELECT SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS(
  '/subscriptions/12345678-90ab-cdef-1234-567890abcdef/resourceGroups/myvault/providers/Microsoft.KeyVault/vaults/TriSecretVault'
);
```

```output
"Resource Endpoint with id "/subscriptions/12345678-90ab-cdef-1234-567890abcdef/resourceGroups/myvault/privatelink-test/providers/Microsoft.KeyVault/vaults/TriSecretVault/privateEndpoints/" restored successfully.
```

**Google Cloud:**

```sqlexample
SELECT SYSTEM$RESTORE_PRIVATELINK_ENDPOINT_TSS(
  'cloudkms.us-west2.rep.googleapis.com'
);
```

```output
Private endpoint with id 'abcd0000000000001234' restored successfully.
```
