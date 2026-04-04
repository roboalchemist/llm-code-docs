# Source: https://www.apollographql.com/docs/graphos/platform/access-management/api-keys.md

# API Keys

Every system that communicates with Apollo GraphOS must use an API key. [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content) enables you to create and manage your API keys.

Use personal keys for your local development setup. Use graph or subgraph keys in all other instances.

## Graph API keys

A graph API key provides access to interacting with a single graph in GraphOS.

Create a unique graph API key for each non-development system that communicates with GraphOS. Doing so enables you to revoke access to a single system without affecting others.

API keys are secret credentials. Never share them outside your organization or commit them to version control. Delete and replace API keys that you believe are compromised.

1. Go to [studio.apollographql.com](https://studio.apollographql.com/?referrer=docs-content) and click the graph you want to obtain an API key for.

2. If a **Publish your Schema** dialog appears, copy the protected value that appears after `APOLLO_KEY=` in the example code block (it begins with `service:`), and you're all set.

   Otherwise, proceed to the next step.

3. Open your graph's Settings page and select the API Keys tab. Click **Create New Key**. Give your key a name, such as `Production`. This helps you keep track of each API key's use.

   If you don't see the API Keys tab, you don't have sufficient permissions for your graph. Only organization members with the **Org Admin** or **Graph Admin** role can manage graph API keys. [Learn more about member roles.](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/)

4. Copy the key's value. For security, you cannot view an API key's value in Studio after creating it.

### Setting permissions

Unless you have an Enterprise plan, every graph API key provides full access to its associated graph.

If you have an Enterprise plan, you can [assign a role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#graph-api-key-roles) to each graph API key you create. If you do, the API key's permissions are limited to that role's permissions.

You can't change a graph API key's role after it's created. Instead, create a new key with the desired role.

## Subgraph API keys

A subgraph API key provides access to a specific subgraph within a variant, or set of subgraph-variant pairs, within your organization's graph.

Use subgraph keys when you need to run checks on subgraphs, create subgraphs, or publish updates to subgraph schemas within CI/CD pipelines. You should create one subgraph API key per pipeline workflow.

Subgraph keys expire one year from creation.

Subgraph API keys are secret credentials. Never share them with others or commit them to version control. Delete and replace any compromised API keys.

Only organization members with the **Org Admin** or **Graph Admin** role in an Enterprise or Standard plan can create subgraph API keys.
Customers on Standard plans may create up to 5 subgraph keys. Enterprise plans have no limit on subgraph keys.

### Using the Rover CLI

Use the `rover api-key create` command, passing in a subgraph configuration file with the subgraphs you want to grant access to. See the [`rover api-key create` command documentation](https://www.apollographql.com/docs/rover/commands/api-key#creating-api-keys).

### Using the Platform API

To create a subgraph API key, use the `createKey` mutation from the [Platform API](https://www.apollographql.com/docs/graphos/platform/platform-api).

Before starting, you need the following information:

* Your organization ID
* The subgraph you would like to grant access to (including the graph ID and variant it's associated with)

Use the following mutation:

```graphql
mutation Mutation($organizationId: ID!, $name: String!, $type: GraphOsKeyType!, $resources: ApiKeyResourceInput) {  
  organization(id: $organizationId) {    
    createKey(name: $name, type: $type, resources: $resources) {      
      keyName      
      id      
      token    
    }
  }
}
```

Include a request payload with the following properties, filling in your own values:

```graphql title=Request payload
{
  "name": <YOUR_SUBGRAPH_API_KEY_NAME>,
  "type": "SUBGRAPH",
  "organizationId": <YOUR_ORGANIZATION_ID>,
  "resources": {
    "subgraphs": [
      {
        "graphId": <YOUR_GRAPH_ID>,
        "subgraphName": <YOUR_SUBGRAPH_ID>,
        "variantName": <YOUR_VARIANT_NAME_1>
      },
      {
        "graphId": <YOUR_GRAPH_ID>,
        "subgraphName": <YOUR_SUBGRAPH_ID>,
        "variantName": <YOUR_VARIANT_NAME_2>
      }
    ]
  }
}
```

Here's an example of the response payload:

```graphql title=Response payload
{
  "data": {
    "organization": {
      "createKey": {
        "keyName": "Subgraph test key",
        "id": "6ca72032-535a-4bba-b816-fa8d88823863",
        "token": "ak_v2_RkZFMjE4ODYtMzk5Qy00QkMzLUExRDYtMDRBMjE5NTdFNTdF_MUU3M0MxQ0MtMjY5OS00QjhBLTk4MjYtQzVFMUJFRjFBQUZB"
     }
    }
  }
}
```

Make sure to copy the key's value and store it securely. You can't view an API key's value after creating it.

Only organization members with the **Org Admin** or **Graph Admin** role can manage subgraph API keys.

## Managing keys

Org members with the **Org Admin** role can manage subgraph API keys in the following ways:

* View all subgraph keys
* View a single subgraph key
* Delete a subgraph key

### Using the Rover CLI

To manage subgraph keys, you can [use the `rover api-key` commands](https://www.apollographql.com/docs/rover/commands/api-key/).

### Using the Platform API

You can also send requests to the [Platform API](https://www.apollographql.com/docs/graphos/platform/platform-api) using the following operations:

## View all subgraph keys

To view all the keys in your organization, use the `apiKeys` query:

```graphql
query ApiKeys($organizationId: ID!) {
  organization(id: $organizationId) {
    apiKeys {
      totalCount
      nodes {
        createdAt
        expiresAt
        id
        keyName
        resources {
          resourceId
          resourceType
        }
        token
      }
    }
  }
}
```

Include a request payload with the following properties, filling in your own values:

```graphql title=Request payload
{
  "organizationId": "test-organization-id"
}
```

Here's an example of the response payload:

```graphql title=Response payload
{
  "data": {
    "organization": {
      "apiKeys": {
        "totalCount": 2,
        "nodes": [
          {
            "createdAt": "2025-08-22T16:39:55.333903000Z",
            "expiresAt": "2026-08-22T16:40:17.876252636Z,
            "id": "00f8a1f8-53cb-47b9-b6f8-9a12d94d101f",
            "keyName": "Subgraph Test Key 1",
            "resources": [
              {
                "resourceId": "test-graph-id:staging:test-subgraph-name",
                "resourceType": "SUBGRAPH"
              },
              {
                "resourceId": "test-graph-id:staging:another-subgraph",
                "resourceType": "SUBGRAPH"
              }
            ]
          },
          {
            "createdAt": "2025-08-26T17:40:17.992591000Z",
            "expiresAt": "2026-08-26T17:40:17.876252636Z",
            "id": "982e5fbf-bbe6-4efa-bf05-0ce9fd5110ab",
            "keyName": "Subgraph Test Key 2",
            "resources": [
              {
                "resourceId": "test-graph-id:prod:test-subgraph-name",
                "resourceType": "SUBGRAPH"
              }
            ]
          }
        ]
      }
    }
  }
}
```

## View a subgraph key

To view a single subgraph API key, use the `apiKey` query, passing in the `keyId` of the key you want to view.

You can obtain the `keyId` value from when you first created the key, or by viewing all subgraph keys and obtaining the `id` value.

```graphql
query ApiKey($keyId: ID!, $organizationId: ID!) {
  organization(id: $organizationId) {
    apiKey(keyId: $keyId) {
      createdAt
      expiresAt
      id
      keyName
      resources {
        resourceId
        resourceType
      }
    }
  }
}
```

Include a request payload with the following properties, filling in your own values:

```graphql title=Request payload
{
  "keyId": "982e5fbf-bbe6-4efa-bf05-0ce9fd5110ab",
  "organizationId": "test-organization-id"
}
```

Here's an example of the response payload:

```graphql title=Response payload
{
  "data": {
    "organization": {
      "apiKey": {
        "createdAt": "2025-08-26T17:40:17.992591000Z",
        "expiresAt": "2026-08-26T17:40:17.876252636Z",
        "id": "982e5fbf-bbe6-4efa-bf05-0ce9fd5110ab",
        "keyName": "Subgraph test key",
        "resources": [
          {
            "resourceId": "test-graph-id:prod:test-subgraph-name",
            "resourceType": "SUBGRAPH"
          }
        ]
      }
    }
  }
}
```

## Delete a subgraph key

To delete a subgraph API key, use the `deleteKey` mutation:

```graphql
mutation DeleteKey($keyId: ID!, $organizationId: ID!) {
  organization(id: $organizationId) {
    deleteKey(keyId: $keyId)
  }
}
```

Include a request payload with the following properties, filling in your own values:

```graphql title=Request payload
{
  "keyId": "982e5fbf-bbe6-4efa-bf05-0ce9fd5110ab",
  "organizationId": "test-organization-id"
}
```

Here's an example of the response payload, where a successful deletion returns the deleted `keyId`:

```graphql title=Response payload
{
  "data": {
    "organization": {
      "deleteKey": "982e5fbf-bbe6-4efa-bf05-0ce9fd5110ab"
    }
  }
}
```

## Personal API keys

A personal API key provides partial access to every graph in every organization you belong to. Specifically, it has the same permissions that your user account has in each of those organizations.

Personal API keys are useful for local development tools (like the [Rover CLI](https://www.apollographql.com/docs/rover/) and the Apollo [VS Code extension](https://www.apollographql.com/docs/devtools/editor-plugins/)) to load schemas and other data from GraphOS.

Personal API keys are secret credentials. Never share them with others or commit them to version control. Delete and replace API keys that you believe are compromised.

1. Go to [studio.apollographql.com/user-settings](https://studio.apollographql.com/user-settings).

2. In the Personal API Key section, click **Create New Key**. Give your key a name, such as `Local development laptop`. This helps you keep track of each API key's use.

3. Copy the key's value. For security, you cannot view an API key's value in Studio after creating it.

## Storing API keys

After creating an API key, securely store the token value in your secret manager of choice. You can't view an API key's value after creating it.
