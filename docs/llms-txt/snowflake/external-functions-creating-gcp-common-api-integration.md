# Source: https://docs.snowflake.com/en/sql-reference/external-functions-creating-gcp-common-api-integration.md

# Step 3: Create the API integration for GCP in Snowflake

This topic provides instructions for creating an API integration object in Snowflake to work with your proxy service (i.e. Google Cloud API
Gateway).

## Previous step

[Step 2: Create the proxy service (Google Cloud API Gateway) in the console](external-functions-creating-gcp-ui-proxy-service.md)

## Create the API integration object

Use the [CREATE API INTEGRATION](sql/create-api-integration.md) command to create the API integration object:

1. Open a Snowflake session, typically a Snowflake web interface session.
2. Execute the USE ROLE command to use the ACCOUNTADMIN role or a role with the CREATE INTEGRATION privilege. For example:

   > ```sqlexample
   > use role has_accountadmin_privileges;
   > ```
>
3. Enter a CREATE API INTEGRATION statement. The statement should look similar to the following:

   > ```sqlexample
   > create or replace api integration <integration_name>
   >     api_provider = google_api_gateway
   >     google_audience = '<google_audience_claim>'
   >     api_allowed_prefixes = ('<url>')
   >     enabled = true;
   > ```

   In the statement:

   > 1. Replace `<integration_name>` with a unique integration name (e.g. `my_api_integration_name`. The name must follow the rules for
   >    [Object identifiers](identifiers.md).
   >
   >    In addition, record the integration name in the `API Integration Name` field in your tracking worksheet. You will need the name when
   >    you execute the CREATE EXTERNAL FUNCTION command later in the creation process.
   > 2. For `google_audience`, replace `<google_audience_claim>` with the value from the `Managed Service Identifier` field in your
   >    tracking worksheet.
   >
   >    During authentication, Snowflake passes a JWT (JSON Web Token) to Google. The JWT contains an “aud” (“audience”) claim, which
   >    Snowflake sets to the value for `google_audience`.
   >
   >    For more information about authenticating with Google, see the Google service account
   >    [authentication documentation](https://cloud.google.com/api-gateway/docs/authenticate-service-account#configure_auth).
   > 3. For `api_allowed_prefixes`, replace `<url>` with the value from the `Gateway Base URL` field in your tracking worksheet.
   >
   >    This field allows you to restrict the URLs to which this API integration can be applied. You can use a value that is more restrictive
   >    than the Gateway Base URL.
4. If you haven’t already, execute the CREATE API INTEGRATION statement you entered.

## Record the API_GCP_SERVICE_ACCOUNT information for the API integration

1. Execute the [DESCRIBE INTEGRATION](sql/desc-integration.md) command. For example:

   > ```sqlexample
   > describe integration my_api_integration_name;
   > ```
>
2. Record the value for `API_GCP_SERVICE_ACCOUNT` in the `API_GCP_SERVICE_ACCOUNT` field in your tracking worksheet.

## Next step

[Step 4: Create the external function for GCP in Snowflake](external-functions-creating-gcp-common-ext-function.md)
