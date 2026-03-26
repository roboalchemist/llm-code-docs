# Source: https://www.zuplo.com/docs/policies/upstream-gcp-service-auth-inbound.md

# Upstream GCP Service Auth Policy

Secure your Google Cloud Platform services by automatically adding GCP-issued ID
tokens to upstream requests. This policy enables your Zuplo gateway to
authenticate with GCP IAM-protected services without requiring any code changes
to your backend.

With this policy, you'll benefit from:

- **Enhanced Backend Security**: Restrict access to your GCP services to only
  your Zuplo gateway
- **Simplified Authentication**: Delegate authentication and authorization to
  your gateway without backend code changes
- **Automatic Token Management**: Handle token acquisition, caching, and renewal
  automatically
- **GCP Integration**: Seamlessly connect with Cloud Run, Cloud Functions, GKE
  with IAP, and other GCP services
- **Credential Security**: Store sensitive GCP service account credentials
  securely in your Zuplo environment

This policy works with
[GCP Identity Aware Proxy](https://zuplo.com/docs/articles/gke-with-upstream-auth-policy)
or services like [Cloud Run](https://cloud.google.com/iap/docs/managing-access)
that natively support IAM authorization.

For information on how Google's service-based auth works, see
[Authenticating for invocation](https://cloud.google.com/functions/docs/securing/authenticating).

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-upstream-gcp-service-auth-inbound-policy",
  "policyType": "upstream-gcp-service-auth-inbound",
  "handler": {
    "export": "UpstreamGcpServiceAuthInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "audience": "https://my-service-a2ev-uc.a.run.app",
      "scopes": ["https://www.googleapis.com/auth/cloud-platform"],
      "serviceAccountJson": "$env(SERVICE_ACCOUNT_JSON)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `upstream-gcp-service-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `UpstreamGcpServiceAuthInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `audience` <code className="text-green-600">&lt;string&gt;</code> - The audience for the service to be called. This is typically the URL of your service endpoint like 'https://my-service-a2ev-uc.a.run.app'. If calling a Google API, leave this empty.
- `scopes` <code className="text-green-600">&lt;string[]&gt;</code> - The scopes to grant the access token. See [documentation](https://developers.google.com/identity/protocols/oauth2/scopes) for details. This is only set with calling a Google API. If calling a service like Cloud Run, etc. leave this empty.
- `serviceAccountJson` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The Google Service Account key in JSON format. Note you can load this from environment variables using the `$env(ENV_VAR)` syntax.
- `tokenRetries` <code className="text-green-600">&lt;number&gt;</code> - The number of times to retry fetching the token in the event of a failure. Defaults to `3`.
- `expirationOffsetSeconds` <code className="text-green-600">&lt;number&gt;</code> - The number of seconds less than the token expiration to cache the token. Defaults to `300`.
- `useMemoryCacheOnly` <code className="text-green-600">&lt;boolean&gt;</code> - This is an advanced option that should only be used if you do not want to persist information in ZoneCache.
- `version` <code className="text-green-600">&lt;number&gt;</code> - The version of the policy. Allowed values are `1`, `2`. Defaults to `1`.

## Using the Policy

This policy authenticates your Zuplo gateway to Google Cloud Platform services
by automatically adding GCP-issued ID tokens to the `Authorization` header of
upstream requests. It supports both authenticating to your own GCP services and
calling Google APIs directly.

### How It Works

The policy performs the following operations:

1. Uses your GCP service account credentials to obtain an ID token or access
   token
2. Caches the token for subsequent requests until it expires
3. Adds the token to the `Authorization` header as a Bearer token
4. Automatically handles token renewal when needed

### Setup Instructions

#### Create the GCP Service Account

1. [Create a service account](https://cloud.google.com/iam/docs/service-accounts-create)
   specifically for your Zuplo Gateway (e.g., `zuplo-gateway`)
2. Grant the account permission to call any GCP services you want to proxy with
   Zuplo
3. [Create a Service Account key](https://cloud.google.com/iam/docs/keys-create-delete)
   in JSON format
4. In your Zuplo project, set an environment variable (e.g.,
   `GCP_SERVICE_ACCOUNT`) as a secret with the value of the downloaded JSON

:::caution

The value of the private key is a JSON file. **Before saving it to Zuplo's
environment variables**, you must remove all line breaks and all instances of
the `\n` escape character. The JSON file should be a single line.

:::

### Policy Configuration

This policy supports two main use cases, each with different configuration
requirements:

#### 1. Authenticating to Your GCP Services

When calling your own services like Cloud Run, Cloud Functions, or services
protected by Identity Aware Proxy (IAP), use the `audience` property:

```json
{
  "name": "gcp-service-auth",
  "export": "UpstreamGcpServiceAuthInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "audience": "https://my-app-1235.a.run.app",
    "serviceAccountJson": "$env(GCP_SERVICE_ACCOUNT)"
  }
}
```

**Audience Values:**

- For **Cloud Run**: Use the full URL of your Cloud Run service (e.g.,
  `https://my-service.a.run.app`)
- For **Identity Aware Proxy**: Use the Client ID of your OAuth application
- For **Cloud Functions**: Use the full URL of your function

#### 2. Calling Google APIs

When calling Google APIs directly (e.g., executing a
[Workflow](https://cloud.google.com/workflows/docs/executing-workflow)), use the
`scopes` property:

```json
{
  "name": "gcp-service-auth-gcloud-api",
  "export": "UpstreamGcpServiceAuthInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "scopes": [
      "https://www.googleapis.com/auth/cloud-platform",
      "https://www.googleapis.com/auth/cloud-platform.read-only"
    ],
    "serviceAccountJson": "$env(GCP_SERVICE_ACCOUNT)"
  }
}
```

**Finding Required Scopes:** Refer to Google's API documentation for the
specific API you're calling. Look for the
[**Authorization scopes**](https://cloud.google.com/resource-manager/reference/rest/v1/projects/get#authorization-scopes)
section, which lists the required scopes in URL format (e.g.,
`https://www.googleapis.com/auth/cloud-platform`).

### Usage Example

#### Securing Cloud Run Access

Apply the policy to routes that need to access your Cloud Run service:

```json
{
  "paths": {
    "/api/data": {
      "get": {
        "x-zuplo-route": {
          "policies": {
            "inbound": ["jwt-auth", "gcp-service-auth"]
          },
          "handler": {
            "export": "forwardToOrigin",
            "module": "$import(@zuplo/runtime)",
            "options": {
              "baseUrl": "https://my-service-1235.a.run.app"
            }
          }
        }
      }
    }
  }
}
```

### Security Considerations

- Store the service account JSON as an environment variable using
  `$env(VARIABLE_NAME)` syntax
- Follow the principle of least privilege when assigning permissions to your
  service account
- Regularly rotate your service account keys according to your security policies
- Consider using
  [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)
  for keyless authentication when possible
- Monitor your service account usage through GCP audit logs

Read more about [how policies work](/articles/policies)
