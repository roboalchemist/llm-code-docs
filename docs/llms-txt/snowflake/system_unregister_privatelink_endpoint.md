# Source: https://docs.snowflake.com/en/sql-reference/functions/system_unregister_privatelink_endpoint.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$UNREGISTER_PRIVATELINK_ENDPOINT

Unregisters a private connectivity endpoint to route your connection to the Snowflake service.

## Syntax

**AWS**

```sqlsyntax
SYSTEM$UNREGISTER_PRIVATELINK_ENDPOINT(
  '<aws_private_endpoint_vpce_id>',
  '<aws_account_id>',
  '<token>'
  )
```

**Azure**

```sqlsyntax
SYSTEM$UNREGISTER_PRIVATELINK_ENDPOINT(
  '<azure_private_endpoint_link_id>',
  '<azure_private_endpoint_resource_id>',
  '<token>'
  )
```

## Arguments

**AWS**

`aws_private_endpoint_vpce_id`
:   Specifies the identifier for your Amazon Web Services (AWS) virtual private cloud endpoint (AWS VPCEID).

    To obtain the AWS VPCEID value, navigate through the AWS console or use the following command:

    ```bash
    aws ec2 describe-vpc-endpoints
    ```

`aws_account_id`
:   The 12-digit identifier that uniquely identifies your Amazon Web Services (AWS) account, as a string.

    To obtain the AWS account ID value, navigate through the AWS console or use the following command:

    ```bash
    aws sts get-caller-identity
    ```

**Azure**

`azure_private_endpoint_link_id`
:   Specifies the identifier for your Microsoft Azure (Azure) virtual private cloud endpoint link (Azure LinkID).

    To obtain the Azure LinkID value:

    Run the [SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS](system_get_privatelink_authorized_endpoints.md) system function.

`azure_private_endpoint_resource_id`
:   The identifier that uniquely identifies your Snowflake account in Microsoft Azure (Azure) as a string.

    To obtain the Azure private endpoint resource Id, use the following command:

    ```bash
    az network private-endpoint list --resource-group my_resource_group
    ```

`token`
:   Specifies an access token to verify ownership of the private connectivity endpoint.

    To obtain the token, you must have the corresponding read or describe privilege on the private connectivity endpoint at a minimum.
    For more information, see:

    * [AWS endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)
    * [Azure private endpoint privileges](https://learn.microsoft.com/en-us/azure/private-link/rbac-permissions#private-endpoint)

    To obtain the token, use the following commands:

    * For Snowflake on AWS:

      ```bash
      aws sts get-federation-token --name snowflake --policy '{ "Version": "2012-10-17", "Statement"
      : [ { "Effect": "Allow", "Action": ["ec2:DescribeVpcEndpoints"], "Resource": ["*"] } ] }'
      ```
    * For Snowflake on Azure:

      ```bash
      az account get-access-token --subscription <subscription_id>
      ```

    For more information about limiting the scope of an access token, see:

    * For Snowflake on AWS: [Managing access token scope on Amazon Web Services](../../user-guide/pin-private-endpoints.md)
    * For Snowflake on Azure: [Managing access token scope on Microsoft Azure](../../user-guide/pin-private-endpoints.md)

## Returns

Returns a status message about the registration of the private connectivity endpoint.

## Usage notes

Only account administrators (users with the ACCOUNTADMIN role) can call this function.

## Examples

Unregister a VPC endpoint for your Snowflake account. Note that the `AccessKeyId`, `SecretAccessKey`, and
`SessionToken` values are truncated:

**AWS**

> ```sqlexample
> SELECT SYSTEM$UNREGISTER_PRIVATELINK_ENDPOINT(
>   'vpce-0c1...',
>   '174...',
>   '{
>     "Credentials": {
>       "AccessKeyId": "ASI...",
>       "SecretAccessKey": "aFP...",
>       "SessionToken": "Fwo...",
>       "Expiration": "2024-04-26 05:49:09+00:00"
>     },
>     "FederatedUser": {
>       "FederatedUserId": "0123...:snowflake",
>       "Arn": "arn:aws:sts::174...:federated-user/sam"
>     },
>     "PackedPolicySize": 9
>   }'
> );
> ```

**Azure**

```sqlexample
SELECT SYSTEM$UNREGISTER_PRIVATELINK_ENDPOINT(
  '123...',
  '/subscriptions/0cc51670-.../resourceGroups/dbsec_test_rg/providers/Microsoft.Network/
  privateEndpoints/...',
  'eyJ...'
  );
```
