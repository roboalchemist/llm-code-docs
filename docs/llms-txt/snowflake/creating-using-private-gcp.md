# Source: https://docs.snowflake.com/en/developer-guide/external-network-access/creating-using-private-gcp.md

# External network access and private connectivity on Google Cloud

This topic provides configuration details to set up outbound private connectivity to a Google Cloud external service by way of
[external network access](external-network-access-overview.md). The primary differences between
the outbound public connectivity and outbound private connectivity configurations are that, with private connectivity, you must do the
following operations:

* Create a private connectivity endpoint. This step requires the ACCOUNTADMIN role.
* Create a network rule so the `TYPE` property is set to `PRIVATE_HOST_PORT`.

## Outbound private connectivity costs

You pay for each private connectivity endpoint along with total data processed. For pricing of these items, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

You can explore the cost of these items by filtering on the following service types when querying billing views in the ACCOUNT_USAGE and ORGANIZATION_USAGE schemas:

* OUTBOUND_PRIVATELINK_ENDPOINT
* OUTBOUND_PRIVATELINK_DATA_PROCESSED

For example, you can query the [USAGE_IN_CURRENCY_DAILY](../../sql-reference/organization-usage/usage_in_currency_daily.md) view and filter on these service types.

## Configure external network access

To configure outbound private connectivity with external network access on Google Cloud, do the following steps:

1. In Snowflake, call the [SYSTEM$PROVISION_PRIVATELINK_ENDPOINT](../../sql-reference/functions/system_provision_privatelink_endpoint.md) system function to provision a private
   connectivity endpoint in your Snowflake VNet to enable Snowflake to connect to a Google Cloud external service using private connectivity:

   ```sqlexample
   USE ROLE ACCOUNTADMIN;

   SELECT SYSTEM$PROVISION_PRIVATELINK_ENDPOINT(
     'projects/<project_id>/regions/us-west2/serviceAttachments/cloud-func',
     'my-hello-echo-function.com',
   );
   ```

2. In the Google Cloud console, go to the service attachment and accept the newly connected Snowflake project.
3. In Snowflake, create a [network rule](../../sql-reference/sql/create-network-rule.md), specifying the `PRIVATE_HOST_PORT` property to
   enable private connectivity:

   ```sqlexample
   CREATE DATABASE IF NOT EXISTS external_access_db;

   CREATE OR REPLACE NETWORK RULE external_access_db.public.cloud_func_rule
     MODE = EGRESS
     TYPE = PRIVATE_HOST_PORT
     VALUE_LIST = ('my-hello-echo-function:443');
   ```

4. In Snowflake, create an [external access integration](../../sql-reference/sql/create-external-access-integration.md), specifying the network rule from
   the previous step:

   ```sqlexample
   CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION web_server_eai
     ALLOWED_NETWORK_RULES = (external_access_db.public.cloud_func_rule)
     ENABLED = TRUE;
   ```

5. In Snowflake, execute the following SQL statements to create a function that can use the external access integration:

   ```sqlexample-java
   CREATE OR REPLACE FUNCTION call_func(name VARCHAR)
     returns VARCHAR
     LANGUAGE JAVA
     EXTERNAL_ACCESS_INTEGRATIONS = (web_server_eai)
     HANDLER = 'UDFClient.call'
     AS
     $$
     import java.net.http.HttpClient;
     import java.net.http.HttpRequest;
     import java.net.http.HttpResponse;
     import java.net.URI;
     import java.io.IOException;

     public class UDFClient {
       private HttpClient client;

       public UDFClient() {
         this.client = HttpClient.newBuilder().version(HttpClient.Version.HTTP_1_1).build();
    }

     public String call(String name) throws IOException, InterruptedException {
       HttpRequest request = HttpRequest.newBuilder()
            .header("Content-Type", "application/json")
            .uri(URI.create("http://my-hello-echo-function?name=" + name))
            .GET()
            .build();

       HttpResponse<String> response =
            client.send(request, HttpResponse.BodyHandlers.ofString());

       return String.valueOf(response.body());
      }
     }
     $$;
   ```

6. In Snowflake, call the function you created in the previous step:

   ```sqlexample
   SELECT call_func("snowflake");

   -- Returns "Hello snowflake!"
   ```

If you no longer need the private connectivity endpoint for the external network access integration, call the [SYSTEM$DEPROVISION_PRIVATELINK_ENDPOINT](../../sql-reference/functions/system_deprovision_privatelink_endpoint.md) system function.
