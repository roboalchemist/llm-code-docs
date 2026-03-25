# Source: https://docs.snowflake.com/en/developer-guide/streamlit/object-management/privatelink.md

# Private connectivity for Streamlit in Snowflake

This topic describes using private connectivity when accessing Streamlit in Snowflake.

## Configuring access to Snowflake

1. Set up private connectivity for your Snowflake account for a supported service:

   * [AWS PrivateLink](../../../user-guide/admin-security-privatelink.md)
   * [Azure Private Link](../../../user-guide/privatelink-azure.md)
   * [Google Cloud Private Service Connect](../../../user-guide/private-service-connect-google.md)
2. Set up private connectivity for [Snowsight](../../../user-guide/ui-snowsight-gs.md).

## Configuring access to Streamlit in Snowflake

To determine the hostname, call [SYSTEM$GET_PRIVATELINK_CONFIG](../../../sql-reference/functions/system_get_privatelink_config.md) in your Snowflake account.
The Streamlit hostname is displayed under the `app-service-privatelink-url` key, which is the wildcard URL required for
routing Streamlit application traffic through a private connectivity service, such as AWS PrivateLink.

> **Note:**
>
> You can set up a new VPC endpoint for Streamlit or create a DNS record to the same VPC endpoint of your Snowflake account, as shown in the following example:
>
> * Record name: `*.<identifier>.privatelink.snowflake.app`
> * Type: CNAME
> * Route traffic to: same VPC as your Snowflake traffic.

Hostname routing at an account level is currently not supported.

## Security considerations

Streamlit in Snowflake apps serve both HTTPS-encrypted traffic and WebSocket-encrypted traffic. The Streamlit browser client application is mounted in a third-party, cross-origin
iframe within Snowsight. This enables strict cross-site browser isolation control.

Streamlit in Snowflake uses a separate URL scheme for specific security requirements. Streamlit URLs have their own top-level domain with no shared elements
with Snowsight. Each Streamlit app has a unique origin.

> **Note:**
>
> When using AWS PrivateLink or Azure Private Link, you control the DNS resolution; there are no PrivateLink DNS records controlled by Snowflake.
