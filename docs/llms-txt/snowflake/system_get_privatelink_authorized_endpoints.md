# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_privatelink_authorized_endpoints.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS

Returns a list of the authorized endpoints for your current account to use with private connectivity to the Snowflake service.

The endpoint value in the command output can be used as the value for the `aws_id` or the
`private-endpoint-resource-id` when using these functions:

* [SYSTEM$GET_PRIVATELINK](system_get_privatelink.md)
* [SYSTEM$AUTHORIZE_PRIVATELINK](system_authorize_privatelink.md)
* [SYSTEM$REVOKE_PRIVATELINK](system_revoke_privatelink.md)

## Syntax

> ```sqlsyntax
> SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS()
> ```

## Arguments

None

## Returns

Returns a list of JSON objects that show key-value pairs where a key represents the `endpoint Id Type`, and a value represents the
`endpoint Id`. For Azure, SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS returns two values, an endpoint ID and a Link Identifier.

**AWS:**

> `endpoint Id Type`
> :   A string label that represents the type of AWS endpoint.
>
> `endpoint Id`
> :   The AWS account ID which has been authorized to connect to the Snowflake endpoint service.

**Azure:**

> `endpoint Id Type`
> :   A string value that represents the type of Azure endpoint.
>
> `endpoint Id`
> :   The Azure resource ID authorized to connect to the Snowflake privatelink service.
>
> `link Identifier`
> :   The link ID of the endpoint that is associated with Azure resource ID.

**GCP:**

> `endpoint Id Type`
> :   A string value that represents the type of Google Cloud endpoint.
>
> `endpoint Id`
> :   The Google Cloud project ID authorized to create the private service connect endpoint to the Snowflake service attachment.

## Usage notes

* Only account administrators (that is. users with the ACCOUNTADMIN role) can execute this function.
* This function can be used with Snowflake accounts on Amazon Web Services (AWS), Microsoft Azure (Azure), and Google Cloud.

## Examples

**AWS**

Returns the authorized endpoints for your Snowflake account to use with AWS PrivateLink for your Snowflake account on AWS:

> ```sqlexample
> use role accountadmin;
> select system$get_privatelink_authorized_endpoints();
> ```

You can optionally use the following command to flatten the query result. For example:

> ```sqlexample
> select
>   value: endpointId
> from
>   table(
>     flatten(
>       input => parse_json(system$get_privatelink_authorized_endpoints())
>     )
>   );
> ```
>
> Returns (endpoints for a Snowflake account on AWS):
>
> > ```none
> > +----------------------+---------------------+
> > | KEY:ENDPOINT ID TYPE |   VALUE:ENDPOINT ID |
> > +----------------------+---------------------+
> > |  "123456789012"      |    "123456789012"   |
> > +----------------------+---------------------+
> > ```
