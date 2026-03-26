# Source: https://www.zuplo.com/docs/policies/openfga-authz-inbound.md

# OpenFGA Authorization Policy

Implement fine-grained authorization for your API using OpenFGA, a
high-performance system based on Google's Zanzibar model. This policy verifies
access permissions by checking relationships between users, objects, and
actions.

With this policy, you'll benefit from:

- **Fine-Grained Access Control**: Define precise permissions based on complex
  relationships
- **Scalable Authorization**: Leverage OpenFGA's high-performance design for
  enterprise workloads
- **Flexible Implementation**: Adapt authorization checks dynamically based on
  request context
- **Consistent Security**: Apply standardized access control across your entire
  API
- **Relationship-Based Model**: Express complex authorization scenarios using
  intuitive object relationships

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
  "name": "my-openfga-authz-inbound-policy",
  "policyType": "openfga-authz-inbound",
  "handler": {
    "export": "OpenFGAAuthZInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "apiUrl": "https://api.us1.fga.dev",
      "authorizationModelId": "$env(FGA_MODEL_ID)",
      "credentials": {
        "method": "client-credentials",
        "clientId": "$env(FGA_CLIENT_ID)",
        "clientSecret": "$env(FGA_CLIENT_SECRET)",
        "apiAudience": "https://api.us1.fga.dev/",
        "oauthTokenEndpointUrl": "https://fga.us.auth0.com/oauth/token"
      },
      "storeId": "$env(FGA_STORE_ID)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `openfga-authz-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `OpenFGAAuthZInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `apiUrl` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The URL of the OpenFGA service.
- `storeId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The ID of the store.
- `authorizationModelId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The ID of the authorization model.
- `allowUnauthorizedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if authorization fails. Default is `false` which means unauthorized users will automatically receive a 403 response. Defaults to `false`.
- `credentials` **(required)** <code className="text-green-600">&lt;undefined&gt;</code> - No description available.

## Using the Policy

This policy integrates with OpenFGA to provide fine-grained authorization for
your API endpoints. OpenFGA implements Google's Zanzibar authorization model,
allowing you to define and check complex permission relationships between users
and resources.

### Usage

To use this policy, you must programmatically set the relationship checks to be
performed against your OpenFGA store. This is done using the static
`setContextChecks` method.

The most common way to set the authorization checks are:

1. Creating custom inbound policies for each authorization scenario
2. Creating a custom inbound policy that reads data from the OpenAPI operation
   and sets the authorization checks dynamically

### Example: Custom Authorization Policies

Create a file like `modules/openfga-checks.ts` to define your custom
authorization policies:

```typescript
import {
  ZuploRequest,
  ZuploContext,
  RuntimeError,
  HttpProblems,
  OpenFGAAuthZInboundPolicy,
} from "@zuplo/runtime";

export async function canReadFolder(
  request: ZuploRequest,
  context: ZuploContext,
) {
  if (!request.params?.folderId) {
    throw new RuntimeError("Folder ID not found in request");
  }

  context.log.info("Setting OpenFGA context checks");

  if (!request.user?.sub) {
    return HttpProblems.forbidden(request, context, {
      detail: "User not found",
    });
  }

  // Set the authorization check to verify if the user has viewer access to the folder
  OpenFGAAuthZInboundPolicy.setContextChecks(context, {
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
  OpenFGAAuthZInboundPolicy.setContextChecks(context, {
    user: `user:${request.user.sub}`,
    relation: "editor",
    object: `document:${request.params.documentId}`,
  });

  return request;
}
```

#### Applying to Routes

In your route configuration, apply both the custom authorization policy and the
OpenFGA policy:

```json
{
  "path": "/folders/:folderId",
  "methods": ["GET"],
  "policies": {
    "inbound": ["jwt-auth", "authz-can-read-folder", "openfga-authz"]
  }
}
```

Then in your `policies.json`:

```json
{
  "name": "authz-can-read-folder",
  "export": "canReadFolder",
  "module": "$import(./modules/openfga-checks)"
},
{
  "name": "openfga-authz",
  "export": "OpenFGAAuthZInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    // OpenFGA configuration...
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
  OpenFGAAuthZInboundPolicy.setContextChecks(context, {
    user: `user:${request.user.sub}`,
    relation: authzData.permission,
    object: `${authzData.resourceType}:${resourceId}`,
  });

  return request;
}
```

Then in your OpenAPI document, you would set the custom data on the `x-authz`
property:

````json
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

### Policy Configuration

To configure the OpenFGA policy, you need to provide connection details to your OpenFGA instance:

```json
{
  "name": "openfga-authz",
  "export": "OpenFGAAuthZInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "apiScheme": "https",
    "apiHost": "api.openfga.example.com",
    "storeId": "YOUR_STORE_ID",
    "authorizationModelId": "YOUR_MODEL_ID",
    "credentials": {
      "method": "api-token",
      "token": "$env(OPENFGA_API_TOKEN)"
    }
  }
}
````

Read more about [how policies work](/articles/policies)
