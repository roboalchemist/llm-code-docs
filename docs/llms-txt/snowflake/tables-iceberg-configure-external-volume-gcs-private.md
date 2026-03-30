# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-external-volume-gcs-private.md

# Private connectivity to external volumes for Google Cloud

This topic describes how to configure outbound private connectivity to an external volume on Google Cloud Storage (GCS). The
primary difference between outbound public connectivity and outbound private connectivity is how you set the USE_PRIVATELINK_ENDPOINT
property for the external volume.

When the external volume is configured to use private connectivity, your connection to the Google Cloud Storage service goes through the
Google Cloud internal network. By configuring your external volume to use outbound private connectivity, you add additional security to your
data-unloading operations by blocking public access to the storage account.

For more information about using external volumes to connect to your external cloud storage for Iceberg tables, see
[Configure an external volume](tables-iceberg-configure-external-volume.md).

> **Note:**
>
> You can use Google Cloud Private Service Connect to access Snowflake-managed Iceberg tables and Iceberg tables that use a catalog
> integration for object storage. In addition, you can use Google Cloud Private Service Connect to access externally managed Iceberg tables and Iceberg tables
> created from Delta files in object storage.

## Outbound private connectivity costs

You pay for each private connectivity endpoint along with total data processed. For pricing of these items, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

You can explore the cost of these items by filtering on the following service types when querying billing views in the ACCOUNT_USAGE and ORGANIZATION_USAGE schemas:

* OUTBOUND_PRIVATELINK_ENDPOINT
* OUTBOUND_PRIVATELINK_DATA_PROCESSED

For example, you can query the [USAGE_IN_CURRENCY_DAILY](../sql-reference/organization-usage/usage_in_currency_daily.md) view and filter on these service types.

## Considerations

You can configure outbound public connectivity and outbound private connectivity for the same cloud storage service. If you want to do this,
create a dedicated external volume for outbound public connectivity and specify `USE_PRIVATELINK_ENDPOINT = FALSE`.

## Limitations

Outbound private connectivity to Google Cloud Storage volumes does not support multi-region buckets.

## Set up outbound private connectivity to an external volume

To set up outbound private connectivity to an external volume, you use SQL or
use Snowsight.

### Use SQL

#### Specify private connectivity for an external volume

The USE_PRIVATELINK_ENDPOINT property of an external volume determines whether it is accessed through private connectivity or
by traversing the public network. To use private connectivity, set `USE_PRIVATELINK_ENDPOINT = TRUE` when creating or modifying an external
volume, as shown in the following examples.

Use the following syntax to create an external volume:

```sqlsyntax
CREATE OR REPLACE EXTERNAL VOLUME <ext_volume_name>
  STORAGE_LOCATIONS =
  (
    (
      NAME = 'my-gcs-loc'
      STORAGE_PROVIDER = 'gcs'
      STORAGE_BASE_URL = 'gcs://<bucket>/<prefix>/'
      USE_PRIVATELINK_ENDPOINT = [ TRUE | FALSE ]
    )
  )
  ALLOW_WRITES=true;
```

Use the following syntax to alter an existing external volume:

```sqlsyntax
ALTER EXTERNAL VOLUME <ext_volume_name>
  UPDATE STORAGE_LOCATION = '<storage_location_name>'
  USE_PRIVATELINK_ENDPOINT = [ TRUE | FALSE ]
```

The [DESCRIBE EXTERNAL VOLUME](../sql-reference/sql/desc-external-volume.md) command includes the USE_PRIVATELINK_ENDPOINT property and its value.

#### Provision a private endpoint

Use the following steps to provision a private endpoint for your Google Cloud Storage volume:

1. In Snowflake, call the [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT](../sql-reference/functions/system_provision_privatelink_endpoint.md) system function.
   Provide as arguments a regional Storage API endpoint and host name. For example:

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

   Using SYSTEM$PROVISION_PRIVATELINK_ENDPOINT to provision a private endpoint in your Snowflake VNet to enable Snowflake to connect to
   external Google Cloud Storage over private connectivity. Only buckets referenced by an external volume that has the USE_PRIVATELINK_ENDPOINT
   property enabled can be accessed using the endpoint.
2. In Snowflake, call the [SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO](../sql-reference/functions/system_get_privatelink_endpoints_info.md) function.

   When the output of SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO includes `"status": "APPROVED"`, your connection from Snowflake to your storage
   account can use private connectivity.

   You can continue with the next steps while awaiting the `"APPROVED"` status.

#### Configure external volume access

Use the following steps to configure private connectivity to your external storage volume:

1. Create the external volume, and set the USE_PRIVATELINK_ENDPOINT property to TRUE. For example:

   ```sqlexample
   CREATE EXTERNAL VOLUME external_volume
     STORAGE_LOCATIONS =
     (
       (
         NAME = 'my-gcs-loc'
         STORAGE_PROVIDER = 'gcs'
         STORAGE_BASE_URL =  'gcs://<bucket>/<prefix>/'
         USE_PRIVATELINK_ENDPOINT = true
       )
     )
     ALLOW_WRITES=true;
   ```

2. Use the [CREATE ICEBERG TABLE](../sql-reference/sql/create-iceberg-table.md) command to create an Iceberg table that references the external volume. For example:

   ```sqlexample
   CREATE ICEBERG TABLE rand_table (data STRING)
     BASE_LOCATION='table'
     EXTERNAL_VOLUME=external_volume
     CATALOG='snowflake';
   ```

3. After the private endpoint has “APPROVED” status, test unloading data from Snowflake to the external volume.

### Use Snowsight

To set up external volume access using private connectivity in Snowsight, follow these steps:

1. In Snowflake, call the [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT](../sql-reference/functions/system_provision_privatelink_endpoint.md) system function.
   Provide as arguments a regional Storage API endpoint and host name. For example:

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

   Using SYSTEM$PROVISION_PRIVATELINK_ENDPOINT to provision a private endpoint in your Snowflake VNet to enable Snowflake to connect to
   external Google Cloud Storage over private connectivity. Only buckets referenced by an external volume that has the USE_PRIVATELINK_ENDPOINT
   property enabled can be accessed using the endpoint.
2. In Snowflake, call the [SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO](../sql-reference/functions/system_get_privatelink_endpoints_info.md) function.

   When the output of SYSTEM$GET_PRIVATELINK_ENDPOINTS_INFO includes `"status": "APPROVED"`, your connection from Snowflake to your storage
   account can use private connectivity.

   You can continue with the next steps while awaiting the `"APPROVED"` status.
3. Follow the steps to
   [configure an external volume for Google Cloud Storage by using Snowsight](tables-iceberg-configure-external-volume-gcs.md)
   and enable private connectivity when you configure the external volume.

   > **Important:**
   >
   > To enable private connectivity, on the Configure external volume page, from the Connectivity field, you must select
   > Private (Private Service Connect).
4. Use the [CREATE ICEBERG TABLE](../sql-reference/sql/create-iceberg-table.md) command to create an Iceberg table that references the external volume. For example:

   ```sqlexample
   CREATE ICEBERG TABLE rand_table (data STRING)
     BASE_LOCATION='table'
     EXTERNAL_VOLUME=external_volume
     CATALOG='snowflake';
   ```

5. After the private endpoint has “APPROVED” status, test unloading data from Snowflake to the external volume.

## Disable private connectivity

If you no longer require private connectivity for the external volume, you can set the USE_PRIVATELINK_ENDPOINT property for the volume to
FALSE, and then call the [SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT](../sql-reference/functions/system_deprovision_privatelink_endpoint.md) system function tp deprovision the endpoint.
For example:

```sqlexample
ALTER EXTERNAL VOLUME <ext_volume_name>
  UPDATE STORAGE_LOCATION = '<storage_location_name>'
  USE_PRIVATELINK_ENDPOINT = false;

SELECT SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT('storage.us-east4.rep.googleapis.com');
```
