# Source: https://docs.snowflake.com/en/guides-overview-secure.md

# Securing Snowflake

Snowflake provides industry-leading features that help ensure you can configure the highest levels of security for your account and users,
as well as all the data you store in Snowflake.

These topics are intended primarily for administrators (i.e. users with the ACCOUNTADMIN, SYSADMIN, or SECURITYADMIN roles).

## Authentication

[Authentication policies](user-guide/authentication-policies.md)
:   Using authentication policies to restrict account and user authentication by client, authentication methods, and more.

[Multi-factor authentication (MFA)](user-guide/security-mfa.md)
:   Using multi-factor authentication with Snowflake.

[Federated Authentication & SSO](user-guide/admin-security-fed-auth-overview.md)
:   Topics related to federated authentication to Snowflake.

[Key-pair authentication and key-pair rotation](user-guide/key-pair-auth.md)
:   Using key-pair authentication to Snowflake.

[Using programmatic access tokens for authentication](user-guide/programmatic-access-tokens.md)
:   Generating and managing programmatic access tokens for authentication.

[OAuth](user-guide/oauth-intro.md)
:   Topics related to using Snowflake OAuth and External OAuth to connect to Snowflake.

[Workload identity federation](user-guide/workload-identity-federation.md)
:   Preferred authentication method for service-to-service workloads.

[External API authentication and secrets](user-guide/api-authentication.md)
:   Configuring Snowflake to authenticate to external services.

## Network security

[Malicious IP Protection](user-guide/malicious-ip-protection.md)
:   Protecting your account from IP addresses that are known to be malicious.

[Controlling network traffic with network policies](user-guide/network-policies.md)
:   Using network policies to restrict access to Snowflake.

[Network rules](user-guide/network-rules.md)
:   Using network rules with other Snowflake features to restrict access to and from Snowflake.

## Private connectivity

[Private connectivity for inbound network traffic](user-guide/private-connectivity-inbound.md)
:   Using private connectivity to access the Snowflake service, Snowsight, Streamlit in Snowflake, internal stages, and Snowpark Container
    Services.

[Private connectivity for outbound network traffic](user-guide/private-connectivity-outbound.md)
:   Using private connectivity for external network locations, external functions, external stages, external tables, external
    volumes, and Snowpipe automation.

## Administration and authorization

[Trust Center](user-guide/trust-center/overview.md)
:   Using the Trust Center to evaluate and monitor your account for security risks.

[Snowflake sessions and session policies](user-guide/session-policies.md)
:   Using session policies to manage your Snowflake session.

[SCIM](user-guide/scim-intro.md)
:   Topics related to using SCIM to provision users and groups to Snowflake.

[Access Control](user-guide/security-access-control-overview.md)
:   Topics related to role-based access control (RBAC) in Snowflake.

[End to End Encryption](user-guide/security-encryption-end-to-end.md)
:   Using end-to-end encryption in Snowflake.
