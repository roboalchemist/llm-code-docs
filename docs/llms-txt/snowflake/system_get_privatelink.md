# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_privatelink.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$GET_PRIVATELINK

Verifies whether your current account is authorized for private connectivity to the Snowflake service.

Returns:
:   Boolean

    `TRUE`: The current Snowflake account is authorized (i.e. enabled) to use private connectivity to the Snowflake service.

    `FALSE`: The current Snowflake account is unauthorized (i.e. disabled) to use private connectivity to the Snowflake service.

See also:
:   [SYSTEM$AUTHORIZE_PRIVATELINK](system_authorize_privatelink.md) , [SYSTEM$REVOKE_PRIVATELINK](system_revoke_privatelink.md) ,
    [SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS](system_get_privatelink_authorized_endpoints.md)

## Syntax

**AWS:**

> ```sqlsyntax
> SYSTEM$GET_PRIVATELINK( '<aws_id>' , '<federated_token>' )
> ```

**Azure:**

> ```sqlsyntax
> SYSTEM$GET_PRIVATELINK( '<private-endpoint-resource-id>' , '<federated_token>' )
> ```

**GCP**

> ```sqlsyntax
> SYSTEM$GET_PRIVATELINK( '<gcp_project_id>' , '<access_token>' )
> ```

## Arguments

`'aws_id'`
:   The 12-digit identifier that uniquely identifies your Amazon Web Services (AWS) account, as a string.

`'private-endpoint-resource-id'`
:   The identifier that uniquely identifies the private endpoint in Microsoft Azure (Azure) as a string.

`'federated_token'`
:   The federated token value that contains access credentials for a federated user as a string.

    To obtain this value, execute the appropriate command for the cloud platform that hosts your Snowflake account. Use the command-line tool
    provided by the platform:

    * For Snowflake on AWS:

      ```bash
      aws sts get-federation-token --name sam
      ```
    * For Snowflake on Azure:

      ```bash
      az account get-access-token --subscription <SubscriptionID>
      ```

      Where:

      + `SubscriptionID`
        :   The unique identifier for your subscription. For example:

            > `13c...`

            To obtain this value, execute the following Azure CLI command in your command-line environment:

            > ```bash
            > az account list --output table
            > ```
            >
            > Note the output value in the `SubscriptionID` column, which is truncated in this example:
            >
            > > ```text
            > > Name     CloudName   SubscriptionId                        State    IsDefault
            > > -------  ----------  ------------------------------------  -------  ----------
            > > MyCloud  AzureCloud  13c...                                Enabled  True
            > > ```

`'gcp_project_id'`
:   The identifier that uniquely identifies your Google Cloud (GCP) project, as a string.

`'access_token'`
:   The access token value that contains access credentials for a Google Cloud user as a string.

## Usage notes

* Only account administrators (i.e. users with the ACCOUNTADMIN role) can execute this function.
* This function can be used with Snowflake accounts on AWS or Azure; Google Cloud Platform (GCP) is not currently supported.
* Call the [SYSTEM$AUTHORIZE_PRIVATELINK](system_authorize_privatelink.md) function to enable your Snowflake account to use private
  connectivity to the Snowflake service.
* Call the [SYSTEM$REVOKE_PRIVATELINK](system_revoke_privatelink.md) function to disable your Snowflake account to use private
  connectivity to the Snowflake service.

## Examples

Verify whether AWS PrivateLink is authorized for your Snowflake account on AWS. Note that the values are truncated in this example.

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> select SYSTEM$GET_PRIVATELINK(
>     '185...',
>     '{
>       "Credentials": {
>           "AccessKeyId": "ASI...",
>           "SecretAccessKey": "enw...",
>           "SessionToken": "Fwo...",
>           "Expiration": "2021-01-07T19:06:23+00:00"
>       },
>       "FederatedUser": {
>           "FederatedUserId": "185...:sam",
>           "Arn": "arn:aws:sts::185...:federated-user/sam"
>       },
>       "PackedPolicySize": 0
>   }'
>   );
> ```

Verify whether Azure Private Link is authorized for your Snowflake account on Azure. Note that the values are truncated in this example.

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> select SYSTEM$GET_PRIVATELINK(
>   '/subscriptions/26d.../resourcegroups/sf-1/providers/microsoft.network/privateendpoints/test-self-service',
>   'eyJ...');
> ```

Verify whether Google Cloud Private Service Connect is authorized for your Snowflake account on GCP:

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> select SYSTEM$GET_PRIVATELINK(
>   'my-gcp-project-id',
>   'ya29.a0AcM612zT4pJaXdYfwgY8aiMoDE9W_xkqQ20coFTB1TJcImKDPo...'
>   );
> ```
