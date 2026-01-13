# Source: https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility_api.md

---
title: Cross-Organization Connections API
description: >-
  Configure cross-organization data sharing connections using the API to enable
  insights across multiple organizations in your account.
breadcrumbs: Docs > Account Management > Cross-Organization Connections API
source_url: https://docs.datadoghq.com/org_settings/cross_org_visibility_api/index.html
---

# Cross-Organization Connections API

{% callout %}
##### Join the Preview!

Cross-organization visibility is in beta.
{% /callout %}

[Cross-organization visibility](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility) allows customers to share data between different organizations in the same account, and show insights from multiple organizations in one place.

This document describes how to configure cross-organization connections through the API. To configure connections through the UI, see [cross-organization visibility](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility).

## API endpoint{% #api-endpoint %}

Configure connections through the public API `/api/v2/org_connections` endpoint. The application key you use to authenticate to the endpoint must have the [`org_connections_write`](https://docs.datadoghq.com/account_management/rbac/permissions/#access-management) and [`org_connections_read`](https://docs.datadoghq.com/account_management/rbac/permissions/#access-management) permissions.

## List connections{% #list-connections %}

List all the connections this organization participates in, either as a source organization or as a destination organization. Listing connections requires the *Org Connections Read* permission.

GET https://{datadog_site}/api/v2/org_connections

### Example{% #example %}

```json
curl -X get "https://{datadog_site}/api/v2/org_connections/" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
  -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
```

## Create a connection{% #create-a-connection %}

Creates a connection from this organization to the destination organization. You must perform this operation in the to-be-source organization. Creating connections requires the *Org Connections Write* permission.

POST https://{datadog_site}/api/v2/org_connections

**Note:** The payload of this call requires the destination organization UUID. Get the destination organization's UUID from the "List your managed organizations" [endpoint](https://docs.datadoghq.com/api/latest/organizations/#list-your-managed-organizations).

### Example{% #example-1 %}

```json
curl -X POST "https://{datadog_site}/api/v2/org_connections" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
  -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
   -d '{
        "data": {
          "type": "org_connection",
          "relationships": {
              "sink_org": {
                  "data": {
                      "type": "orgs",
                      "id": "{{the destination organization UUID}}"
                  }
              }
          }
      }
  }'
```

### Failure scenarios{% #failure-scenarios %}

- The connection already exists
- The connection refers to a destination organization ID outside of the account

## Update a connection{% #update-a-connection %}

Updates the connection type of an existing connection. You must perform this operation from the source organization. Updating connections requires the *Org Connections Write* permission.

PATCH https://{datadog_site}/api/v2/org_connections/{connection_id}

**Note:** The payload of this call requires the connection UUID. Get the connection UUID from the "List your managed organizations" [endpoint](https://docs.datadoghq.com/api/latest/organizations/#list-your-managed-organizations).

### Example{% #example-2 %}

```json
curl -X PATCH "https://{datadog_site}/api/v2/org_connections" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
  -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
   -d '{
        "data": {
          "type": "org_connection",
          "id": "{{the connection UUID}}",
          "attributes": {
              "connection_types": [
                  "logs",
                  "metrics"
              ]
        }
      },
  }'
```

### Failure scenarios{% #failure-scenarios-1 %}

- The organization does not participate as a source to the connection
- The connection does not exist

## Delete a connection{% #delete-a-connection %}

Deletes a connection. Perform this operation either from the source organization or the destination organization. Reference the connection to delete with its ID, which you can get from the List connections request. Deleting connections requires the *Org Connections Write* permission.

DELETE https://{datadog_site}/api/v2/org_connections/{connection_id}

### Example{% #example-3 %}

```json
curl -X DELETE "https://{datadog_site}/api/v2/org_connections/{connection_id}" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
  -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
```

### Failure scenarios{% #failure-scenarios-2 %}

- The organization does not participate as a source or a destination to the connection
- The connection does not exist
