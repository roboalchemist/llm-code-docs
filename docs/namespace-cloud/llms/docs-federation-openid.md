<!-- Source: https://namespace.so/docs/federation/openid -->

# Workload Federation with OpenID Connect

Namespace relies on Workload Identity Federation to allow Namespace to interact with different systems, instead of relying on pre-shared keys which can be more easily compromised.
OpenID Connect (OIDC) is an industry-standard authentication protocol built on top of OAuth 2.0.
It provides a secure, standardized way for applications to verify user identities and exchange authentication information across different systems.
OIDC is widely adopted by major cloud providers, identity systems, and enterprise applications, making it an ideal foundation for workload federation.

## Accessing cloud resources from Namespace

Identity Federation with OpenID Connect allows your Namespace workloads to identify themselves to any OIDC-compliant system using short-lived secure credentials.
To enable this federation, Namespace can issue ID tokens that conform to the OpenID Connect standard, allowing your workloads to authenticate with any cloud provider or service that accepts OIDC tokens.

### Generate a Namespace ID token

You can generate an OpenID Connect ID token from Namespace to authenticate with external systems:

```
$

```
nsc auth issue-id-token --audience <aud>
```
```

Replace `<aud>` with the audience claim required by your target system. This is typically:

- The URL of the service you're authenticating with
- A specific identifier required by the cloud provider (e.g., `sts.amazonaws.com` for AWS)
- The client ID of the application you're accessing

### Example Usage of Namespace ID tokens

1. Generate the ID token for your target system:

   ```
   $

   ```
   export ID_TOKEN=$(nsc auth issue-id-token --audience https://your-service.example.com)
   ```
   ```
2. Use the token to authenticate with the external service according to their OIDC integration requirements. For example:

   ```
   $

   ```
   curl -H "Authorization: Bearer $ID_TOKEN" https://your-service.example.com/api/resource
   ```
   ```

The ID token is issued by `https://federation.namespaceapis.com` and contains standard OIDC claims including your Namespace workspace identity. This allows external systems to verify and authorize your requests in detail.

## Accessing Namespace resources from external systems

Identity Federation with OpenID Connect allows external systems with OIDC tokens to identify themselves to Namespace using short-lived secure credentials.
To enable this federation, you need to register your OIDC issuer as a trusted identity provider with Namespace, then exchange OIDC tokens for Namespace access tokens.

### Prerequisites

Before you can exchange OIDC tokens for Namespace credentials, you must register your issuer with Namespace:
Contact [Namespace Support](mailto:support@namespace.so) to register your OIDC issuer as a known and trusted issuer. You'll need to provide:

- The issuer URL (e.g., `https://your-identity-provider.com`)
- Your Workspace ID from the Dashboard
- Details about the expected token claims and audience

### Obtain Namespace credentials from an OIDC token

Once your issuer is registered, you can exchange OIDC tokens for Namespace access tokens:

1. Obtain an OIDC token from your identity provider. The method depends on your system:

   - Kubernetes: Use service account tokens or workload identity
   - Cloud platforms: Use platform-specific token endpoints
   - Custom systems: Use your OIDC client library to obtain tokens

   Make sure `federation.namespaceapis.com` is configured as the audience.
2. Exchange the OIDC token for Namespace credentials:

   ```
   $

   ```
   nsc auth exchange-oidc-token --token <token> --tenant_id <workspace-id>
   ```
   ```

   Replace `<token>` with your OIDC ID token or access token and `<workspace-id>` with your Namespace workspace identifier (found in the [**Dashboard**](https://cloud.namespace.so/workspace/settings)).

   The command should succeed and display the name of the workspace you've signed in to.
   It stores a short-lived token that will be used automatically in subsequent nsc commands.

Last updated September 30, 2025
