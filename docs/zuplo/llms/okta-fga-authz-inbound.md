# Source: https://www.zuplo.com/docs/policies/okta-fga-authz-inbound.md

# Okta FGA Authorization Policy

This policy authorizes requests using Okta Fine-Grained Authorization (FGA),
providing robust access control for your API resources. If the request is not
authorized, a 403 response will be returned.

With this policy, you'll benefit from:

- **Powerful Authorization Model**: Implement complex relationship-based access
  control using Okta FGA's authorization model
- **Flexible Permission Structure**: Define granular permissions with
  user-to-resource relationships that scale with your application
- **Seamless Okta Integration**: Leverage your existing Okta identity
  infrastructure for consistent authorization across your ecosystem
- **Dynamic Authorization Logic**: Create context-aware authorization rules that
  adapt based on route, method, or request properties
- **Simplified Implementation**: Reduce development time with ready-to-use
  authorization checks that integrate with your API gateway
- **Enhanced Security**: Apply fine-grained access control to protect sensitive
  resources and operations
- **Centralized Policy Management**: Manage all your authorization rules in one
  place through Okta FGA

:::caution{title="Beta"}

This policy is in beta. You can use it today, but it may change in non-backward compatible ways before the final release.

:::

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-okta-fga-authz-inbound-policy",
  "policyType": "okta-fga-authz-inbound",
  "handler": {
    "export": "OktaFGAAuthZInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "authorizationModelId": "$env(FGA_MODEL_ID)",
      "credentials": {
        "clientId": "$env(FGA_CLIENT_ID)",
        "clientSecret": "$env(FGA_CLIENT_SECRET)"
      },
      "region": "us1",
      "storeId": "$env(FGA_STORE_ID)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `okta-fga-authz-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `OktaFGAAuthZInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `region` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The region your store is deployed. Allowed values are `us1`, `eu1`, `au1`.
- `storeId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The ID of the store.
- `authorizationModelId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The ID of the authorization model.
- `allowUnauthorizedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if authorization fails. Default is `false` which means unauthorized users will automatically receive a 403 response. Defaults to `false`.
- `credentials` **(required)** <code className="text-green-600">&lt;object&gt;</code> - No description available.
  - `clientId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The client ID.
  - `clientSecret` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The client secret.

## Using the Policy

## Usage

To use this policy, you must programmatically set the relationship checks to be
performed against your Okta FGA store. This is done using the static
`setContextChecks` method.

The most common way to set the authorization checks are:

1. Creating custom inbound policies for each authorization scenario
2. Creating a custom inbound policy that reads data from the OpenAPI operation
   and sets the authorization checks dynamically

### Example: Custom Authorization Policies

Create a file like `modules/oktafga-checks.ts` to define your custom
authorization policies:

```typescript
import {
  ZuploRequest,
  ZuploContext,
  RuntimeError,
  HttpProblems,
  OktaFGAAuthZInboundPolicy,
} from "@zuplo/runtime";

export async function canReadFolder(
  request: ZuploRequest,
  context: ZuploContext,
) {
  if (!request.params?.folderId) {
    throw new RuntimeError("Folder ID not found in request");
  }

  context.log.info("Setting OktaFGA context checks");

  if (!request.user?.sub) {
    return HttpProblems.forbidden(request, context, {
      detail: "User not found",
    });
  }

  // Set the authorization check to verify if the user has viewer access to the folder
  OktaFGAAuthZInboundPolicy.setContextChecks(context, {
    user: `user:${request.user.sub}`,
    relation: "viewer",
    object: `folder:${request.params.folderId}`,
  });

  return request;
}

export async function canEditDocument(
  request: ZuploRequest,
  context: ZuploContext,
) {
  if (!request.params?.documentId) {
    throw new RuntimeError("Document ID not found in request");
  }

  if (!request.user?.sub) {
    return HttpProblems.forbidden(request, context, {
      detail: "User not found",
    });
  }

  // Set the authorization check to verify if the user has editor access to the document
  OktaFGAAuthZInboundPolicy.setContextChecks(context, {
    user: `user:${request.user.sub}`,
    relation: "editor",
    object: `document:${request.params.documentId}`,
  });

  return request;
}
```

#### Applying to Routes

In your route configuration, apply both the custom authorization policy and the
OktaFGA policy:

```json
{
  "path": "/folders/:folderId",
  "methods": ["GET"],
  "policies": {
    "inbound": ["jwt-auth", "authz-can-read-folder", "oktafga-authz"]
  }
}
```

Then in your `policies.json`:

```json
{
  "name": "authz-can-read-folder",
  "export": "canReadFolder",
  "module": "$import(./modules/oktafga-checks)"
},
{
  "name": "oktafga-authz",
  "export": "OktaFGAAuthZInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    // OktaFGA configuration...
  }
}
```

### Example: Dynamic Authorization Checks

You can make your authorization checks more dynamic by reading data from your
OpenAPI specification or other sources. This allows you to define authorization
rules that adapt based on the route, method, or other request properties.

For example, you could access custom data defined in your route:

```typescript
export async function dynamicAuthCheck(
  request: ZuploRequest,
  context: ZuploContext,
) {
  // Access custom data from the route configuration
  const data = context.route.raw<{
    "x-authz": {
      resourceType: string;
      permission: string;
      resourceIdParam: string;
    };
  }>();
  const authzData = data["x-authz"];

  if (!authzData?.resourceType || !authzData?.permission) {
    throw new RuntimeError(
      "Missing resource type or permission in route config",
    );
  }

  if (!request.user?.sub) {
    return HttpProblems.forbidden(request, context);
  }

  // Extract resource ID from request parameters
  const resourceId = request.params?.[authzData.resourceIdParam];

  if (!resourceId) {
    throw new RuntimeError(
      `Resource ID parameter '${authzData.resourceIdParam}' not found`,
    );
  }

  // Set dynamic authorization check
  OktaFGAAuthZInboundPolicy.setContextChecks(context, {
    user: `user:${request.user.sub}`,
    relation: authzData.permission,
    object: `${authzData.resourceType}:${resourceId}`,
  });

  return request;
}
```

Then in your OpenAPI document, you would set the custom data on the `x-authz`
property:

```json
{
  "paths": {
    "/custom-data": {
      "post": {
        "x-authz": {
          "resourceType": "document",
          "resourceIdParam": "documentId",
          "permission": "editor"
        }
      }
    }
  }
}
```

Read more about [how policies work](/articles/policies)
