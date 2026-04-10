# Source: https://www.zuplo.com/docs/policies/upstream-azure-ad-service-auth-inbound.md

# Upstream Azure AD Service Auth Policy

Secure your origin server with Azure Active Directory authentication by
automatically adding an `Authorization` header to upstream requests. This policy
enables your Zuplo gateway to authenticate with Azure AD-protected services
using client credentials flow.

With this policy, you'll benefit from:

- **Enhanced Backend Security**: Restrict access to your origin servers to only
  your Zuplo gateway
- **Simplified Authentication**: Delegate authentication and authorization to
  your gateway without backend code changes
- **Automatic Token Management**: Handle token acquisition, caching, and renewal
  automatically
- **Azure Integration**: Seamlessly connect with Azure App Services, Functions,
  and other Azure AD-protected resources
- **Credential Security**: Store sensitive Azure AD credentials securely in your
  Zuplo environment

For instructions on configuring Azure AD authentication, see
[Configure your App Service or Azure Functions app to use Azure AD login](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad).

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-azure-ad-service-auth-inbound-policy",
  "policyType": "upstream-azure-ad-service-auth-inbound",
  "handler": {
    "export": "UpstreamAzureAdServiceAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "activeDirectoryClientId": "20edbb34-13e9-42d0-a63c-1b6a0a20d02d",
      "activeDirectoryClientSecret": "$env(ACTIVE_DIRECTORY_CLIENT_SECRET)",
      "activeDirectoryTenantId": "b8e4141e-31f4-43e3-9a96-f97f3eba1eea",
      "expirationOffsetSeconds": 300,
      "tokenRetries": 3
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-azure-ad-service-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamAzureAdServiceAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `activeDirectoryTenantId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - Azure Active Directory Tenant ID.
- `activeDirectoryClientId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Application (client) ID of the Azure AD App Registration.
- `activeDirectoryClientSecret` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The client secret of the Azure AD App Registration.
- `tokenRetries` <code className="text-green-600">&lt;number&gt;</code> - The number of times to retry fetching the token in the event of a failure.. Defaults to `3`.
- `expirationOffsetSeconds` <code className="text-green-600">&lt;number&gt;</code> - The number of seconds less than the token expiration to cache the token. Defaults to `300`.

## Using the Policy

This policy authenticates your Zuplo gateway to Azure AD-protected backend
services by automatically adding an OAuth 2.0 Bearer token to the
`Authorization` header of upstream requests. It uses the Azure AD client
credentials flow to obtain access tokens.

### How It Works

The policy performs the following operations:

1. Requests an access token from Azure AD using the configured client
   credentials
2. Caches the token for subsequent requests until it nears expiration
3. Adds the token to the `Authorization` header as a Bearer token
4. Automatically handles token renewal when needed

### Policy Configuration

Configure the policy with your Azure AD application credentials:

```json
{
  "name": "azure-ad-service-auth",
  "export": "UpstreamAzureAdServiceAuthInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "activeDirectoryTenantId": "YOUR_TENANT_ID",
    "activeDirectoryClientId": "YOUR_CLIENT_ID",
    "activeDirectoryClientSecret": "$env(AZURE_CLIENT_SECRET)",
    "tokenRetries": 3,
    "expirationOffsetSeconds": 300
  }
}
```

### Usage Example

#### Securing Azure Function App Access

Apply the policy to routes that need to access your Azure Function App:

```json
{
  "paths": {
    "/api/data": {
      "get": {
        "x-zuplo-route": {
          "policies": {
            "inbound": ["jwt-auth", "azure-ad-service-auth"]
          },
          "handler": {
            "export": "forwardToOrigin",
            "module": "$import(@zuplo/runtime)",
            "options": {
              "baseUrl": "https://your-function-app.azurewebsites.net"
            }
          }
        }
      }
    }
  }
}
```

### Azure AD Configuration

To use this policy, you need to:

1. Create an Azure AD app registration for your Zuplo gateway
2. Generate a client secret for the app registration
3. Configure your backend service (e.g., Azure Functions, App Service) to use
   Azure AD authentication
4. Grant the necessary permissions for your app registration to access your
   backend service

### Security Considerations

- Store the client secret as an environment variable using `$env(VARIABLE_NAME)`
  syntax
- Ensure your Azure AD app has the minimum required permissions to access your
  backend services
- Consider using managed identities for Azure resources when possible
- Regularly rotate your client secrets according to your security policies

Read more about [how policies work](/articles/policies)
