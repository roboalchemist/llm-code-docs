# Source: https://docs.snowflake.com/en/user-guide/data-load-gcs-private.md

# Private connectivity to external stages for Google Cloud

This topic describes how to configure outbound private connectivity to an external stage on Google Cloud. The primary
difference between the outbound public connectivity and outbound private connectivity is how you configure the storage integration.
For example, you can specify the USE_PRIVATELINK_ENDPOINT property for the storage integration and then reference this storage
integration in the external stage. The external stage inherits the private endpoint configuration from the storage integration.
Subsequently, your connection to the Google Cloud stage goes through the Google Cloud internal network. By configuring your storage
integration and stage to use outbound private connectivity, you add additional security to your data unloading operations by blocking
public access to the storage account.

## Outbound private connectivity costs

You pay for each private connectivity endpoint along with total data processed. For pricing of these items, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

You can explore the cost of these items by filtering on the following service types when querying billing views in the ACCOUNT_USAGE and ORGANIZATION_USAGE schemas:

* OUTBOUND_PRIVATELINK_ENDPOINT
* OUTBOUND_PRIVATELINK_DATA_PROCESSED

For example, you can query the [USAGE_IN_CURRENCY_DAILY](../sql-reference/organization-usage/usage_in_currency_daily.md) view and filter on these service types.

## Considerations

You can configure outbound public connectivity and outbound private connectivity for the same storage account. If you want to do this,
create a dedicated storage integration for outbound public connectivity and specify `USE_PRIVATELINK_ENDPOINT = FALSE`.

## Limitations

Outbound private connectivity to a Google Cloud stage doesn’t support multi-region buckets.

## Specify private connectivity for a storage integration

To specify private connectivity when creating, replacing, or modifying a storage integration, include the USE_PRIVATELINK_ENDPOINT
property as shown in the following examples. To use private connectivity, set `USE_PRIVATELINK_ENDPOINT = TRUE` for the integration.

Storage integration
:   The following examples shows how you can specify the USE_PRIVATELINK_ENDPOINT property when you create a storage integration that has one or more locations:

    ```sqlsyntax
    CREATE OR REPLACE STORAGE INTEGRATION my_int
      TYPE=EXTERNAL_STAGE
      STORAGE_PROVIDER='gcs'
      STORAGE_ALLOWED_LOCATIONS=('gcs://<bucket>/<prefix>/')
      USE_PRIVATELINK_ENDPOINT = { TRUE | FALSE }
    ```

    The following example shows how you can modify a storage integration and set the USE_PRIVATELINK_ENDPOINT property:

    ```sqlsyntax
    ALTER STORAGE INTEGRATION my_int
      SET USE_PRIVATELINK_ENDPOINT = { TRUE | FALSE }
    ```

External stages
:   Updates for USE_PRIVATELINK_ENDPOINT syntax aren’t supported when you create or modify the stage. The following example shows how you must alter the storage
    integration to use the URL of the new or modified stage:

    ```sqlsyntax
    CREATE OR REPLACE STAGE my_gcs_stage
      URL = 'gcs://<bucket>/<prefix>/'
      STORAGE_INTEGRATION=my_int
    ```

## Configure external stage access

These steps are unique to using outbound private connectivity with a storage integration to unload data to an external stage on Google Cloud.

1. In Snowflake, call the [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT](../sql-reference/functions/system_provision_privatelink_endpoint.md) system function.
   Provide as arguments a regional Storage API endpoint and a host name. For example:

   ```sqlexample
   USE ROLE ACCOUNTADMIN;

   SELECT SYSTEM$PROVISION_PRIVATELINK_ENDPOINT(
     'storage.us-east4.rep.googleapis.com',
     'storage.us-east4.rep.googleapis.com');
   ```

   > **Note:**
   >
   > Snowflake supports only Google Cloud regional Storage API endpoints.
   > Google Cloud multi-region buckets aren’t supported.

   Using SYSTEM$PROVISION_PRIVATELINK_ENDPOINT to provision a private endpoint in your Snowflake VNet binds the private endpoint to the host name. This enables the storage integration to connect to your external Google Cloud stage by using private connectivity.
2. In Snowflake, call the [SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO](../sql-reference/functions/system_get_privatelink_endpoints_info.md) function.

   When the output of SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO includes `"status": "APPROVED"`, your connection from Snowflake to your storage account can use private connectivity (after the other necessary Snowflake objects are enabled for outbound private connectivity).

   You can continue with the next steps while awaiting the `"APPROVED"` status.
3. Create a storage integration and be sure to specify TRUE as the value for the USE_PRIVATELINK_ENDPOINT property. For example:

   ```sqlexample
   CREATE OR REPLACE STORAGE INTEGRATION outbound_private_link_int
     TYPE = EXTERNAL_STAGE
     STORAGE_PROVIDER = 'gcs'
     STORAGE_ALLOWED_LOCATIONS = ('gcs://mybucket1/path1/'')
     USE_PRIVATELINK_ENDPOINT = true
     ENABLED = true;
   ```

   For information about creating a role for the storage integration, see [Configure an integration for Google Cloud Storage](data-load-gcs-config.md).
4. Create an external stage that references the storage integration. For example:

   ```sqlexample
   CREATE OR REPLACE STAGE my_gcs_stage
     URL = 'gcs://mybucket1/path1/'
     STORAGE_INTEGRATION = outbound_private_link_int;
   ```

5. After the private endpoint has “APPROVED” status, test unloading data from Snowflake to the external stage. For example:

   ```sqlexample
   COPY INTO @my_gcs_stage
     FROM mytable
     FILE_FORMAT = (FORMAT_NAME = my_csv_format);
   ```

6. View the result in your Google Cloud stage.

## Disable private connectivity

If you no longer require private connectivity for the external stage, you can set the USE_PRIVATELINK_ENDPOINT property on the storage integration
to FALSE, and then call the [SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT](../sql-reference/functions/system_deprovision_privatelink_endpoint.md) system function to deprovision the endpoint.
For example:

```sqlexample
USE ROLE ACCOUNTADMIN;

ALTER STORAGE INTEGRATION my_int
  SET USE_PRIVATELINK_ENDPOINT = false;

SELECT SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT('storage.us-east4.rep.googleapis.com');
```
