# Source: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/private-connectivity.md

# Configuring private connectivity

This section explains inbound private connectivity (to endpoints exposed by Snowpark Container Services) and outbound private connectivity (egress traffic from your service).

## Inbound connectivity

Snowpark Container Services exposes three endpoints:

* **Image registry service:** It serves the OCIv2 API for you to upload your application images to a repository in your Snowflake account. For more information, see [Snowpark Container Services: Working with an image registry and repository](working-with-registry-repository.md).
* **Public endpoints exposed by a service:** You can allow users, in your account, access to your service from outside Snowflake (ingress) by declaring one or more endpoints as public. For more information, see [Using a service](working-with-services.md).
* **Authentication endpoint:** When a user attempts to access a service’s public endpoint, Snowpark Container Services redirects the user through this endpoint for authentication.

This section explains how to enable private connectivity to these endpoints.

> **Note:**
>
> * When configuring private connectivity, you control the DNS resolution; there are no DNS records controlled by Snowflake.

### Configure prerequisites

To enable private connectivity to Snowpark Container Services, first configure private connectivity to connect your Snowflake account to your cloud provider account’s network. For more information, see [Inbound private connectivity to Snowflake service](../../user-guide/private-connectivity-inbound.md).

In addition, create CNAME records in your DNS for the `regionless-privatelink-account-url` value returned from calling [SYSTEM$GET_PRIVATELINK_CONFIG](../../sql-reference/functions/system_get_privatelink_config.md).

### Configure public endpoints access

To enable ingress requests from your network to your service’s public endpoint:

1. Call [SYSTEM$GET_PRIVATELINK_CONFIG](../../sql-reference/functions/system_get_privatelink_config.md) in your Snowflake account to get a list of hostnames for your account. In the output:

   1. `app-service-privatelink-url` key provides a wildcard hostname for Snowpark Container Services public endpoints.
   2. `spcs-auth-privatelink-url` key provides the hostname required for routing Snowpark Container Services authentication.
2. To access Snowflake via private connectivity, you must create CNAME records in your DNS to resolve the endpoint values from the SYSTEM$GET_PRIVATELINK_CONFIG function to your private network.

   > **Note:**
   >
   > Hostname routing at an account level is currently not supported.

### Configuring access to Snowpark Container Services Registry in Snowflake

1. Call SYSTEM$GET_PRIVATELINK_CONFIG in your Snowflake account to get a list of hostnames for your account. In the output, the `spcs-registry-privatelink-url` key provides the hostname required for routing Snowpark Container Services image registry requests.
2. To access Snowflake via private connectivity, it is necessary to create records in your DNS to resolve the endpoint values from the SYSTEM$GET_PRIVATELINK_CONFIG function to your private network.

### Security considerations

The following apply for public endpoints that services expose:

* Each endpoint can serve both HTTPS-encrypted traffic and WebSocket-encrypted traffic.
* Each endpoint has their own top-level domain, with no shared elements with Snowsight. This ensures that browsers isolate services from Snowsight and services from each other, mitigating risks of cross-origin attacks.

## Outbound connectivity

Instead of routing network egress via the public internet, you might opt to direct your service’s egress traffic through a private connectivity endpoint. For more information, see [Network egress using private connectivity](service-network-communications.md).
