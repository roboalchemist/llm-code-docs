# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/azure-monitor.md

# Azure Monitor

Custom Ocean integration

This integration was created using the [custom Ocean integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md) builder.<br /><!-- -->Please note that:

1. This integration will not be listed in the `Data sources` page of your Port application, and must be installed manually using the instructions on this page.
2. This integration will not create components (e.g. `blueprints`, `mapping`, etc.) in your portal automatically, you will need to create them manually using the instructions on this page.

Port's Azure Monitor integration allows you to ingest Azure Monitor resources into your software catalog using the [Ocean Custom Integration](https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/overview) framework. After installing this integration, you can visualize metrics, alerts, activity logs, and diagnostic settings from your Azure resources.

## Supported resources[â](#supported-resources "Direct link to Supported resources")

The Azure Monitor integration can ingest the following resources into Port. It is possible to reference any field that appears in the API responses in the mapping configuration. For detailed API documentation, see the [Azure Monitor REST API documentation](https://learn.microsoft.com/en-us/rest/api/monitor/).

* **Metric Alerts** - Alert rules from [`/subscriptions/{subscriptionId}/providers/Microsoft.Insights/metricAlerts`](https://learn.microsoft.com/en-us/rest/api/monitor/metricalerts/listbysubscription).
* **Activity Logs** - Activity log events from [`/subscriptions/{subscriptionId}/providers/Microsoft.Insights/eventtypes/management/values`](https://learn.microsoft.com/en-us/rest/api/monitor/activity-logs/list).
* **Diagnostic Settings** - Diagnostic settings from resource-specific endpoints (varies by resource type).
* **Metrics** - Resource metrics from resource-specific endpoints (requires resource-specific paths).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To use this integration, the following prerequisites are required:

* An Azure subscription with appropriate permissions.
* A Microsoft Entra ID application registration with appropriate API permissions.
* A client secret for the application.
* Admin consent for the required permissions.
* An access token (bearer token) for Azure Resource Manager API.

**Register an application in Microsoft Entra ID**

1. Log in to the [Azure Portal](https://portal.azure.com).
2. Navigate to **Microsoft Entra ID** > **App registrations**.
3. Click **New registration**.
4. Provide a name for your application (e.g., "Port Azure Monitor Integration").
5. Select **Accounts in this organizational directory only**.
6. Click **Register**.
7. Note the **Application (client) ID** and **Directory (tenant) ID**.

**Create a client secret**

1. In your app registration, navigate to **Certificates & secrets**.
2. Click **New client secret**.
3. Provide a description (e.g., "Port Azure Monitor Secret").
4. Select an expiration period.
5. Click **Add**.
6. **Copy the secret value immediately** - it will not be shown again.

Secret security

Store your client secret securely and never share it. The secret provides access to your Azure resources.

**Grant API permissions:**

1. In your app registration, navigate to **API permissions**.
2. Click **Add a permission**.
3. Select **Azure Service Management**.
4. Select **Application permissions**.
5. Add the following permission:
   <!-- -->
   * `user_impersonation` - Access Azure Service Management as organization users.
6. Click **Add permissions**.
7. Click **Grant admin consent for \[Your Organization]**.

Admin consent required

You need an Entra ID administrator to grant consent for these permissions before the integration can access Azure Monitor data.

**Generate an access token (bearer token)**

To authenticate with Azure Resource Manager API we need to obtain an OAuth2 access token. We can use the following curl command to get a token:

```
curl -X POST "https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "scope=https://management.azure.com/.default" \
  -d "grant_type=client_credentials" | jq -r '.access_token'
```

Replace:

* `YOUR_TENANT_ID` with your Directory (tenant) ID.
* `YOUR_CLIENT_ID` with your Application (client) ID.
* `YOUR_CLIENT_SECRET` with your client secret value.

Token expiration

Access tokens typically expire after 1 hour. For production use, consider implementing automatic token refresh or using OAuth2 client credentials flow with automatic token management.

**To find your subscription ID:**

1. Log in to the [Azure Portal](https://portal.azure.com).
2. Navigate to **Subscriptions**.
3. Copy the **Subscription ID** you want to monitor.

## Installation[â](#installation "Direct link to Installation")

Choose one of the following installation methods to deploy the Ocean Custom Integration:

* Helm
* Docker

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

## Installation

Add Port's Helm repo and install the Ocean Custom Integration:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_BEARER_TOKEN`. Get your bearer token using the curl command in the Prerequisites section.

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install my-ocean-azure-monitor-integration port-labs/port-ocean \
  --set port.clientId="YOUR_PORT_CLIENT_ID" \
  --set port.clientSecret="YOUR_PORT_CLIENT_SECRET" \
  --set port.baseUrl="https://api.port.io" \
  --set initializePortResources=true \
  --set scheduledResyncInterval=120 \
  --set integration.identifier="azure-monitor-integration" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://management.azure.com" \
  --set integration.config.authType="bearer_token" \
  --set integration.config.apiToken="YOUR_BEARER_TOKEN"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

## Configuration parameters

This table summarizes the available parameters for the installation.

| Parameter                           | Description                                                                                                                     | Example                         | Required |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | -------- |
| `port.clientId`                     | Your Port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).     |                                 | â       |
| `port.clientSecret`                 | Your Port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials). |                                 | â       |
| `port.baseUrl`                      | Your Port API URL (`https://api.port.io` for EU, `https://api.us.port.io` for US).                                              |                                 | â       |
| `integration.config.baseUrl`        | Base URL of the Azure Resource Manager API.                                                                                     | <https://management.azure.com>  | â       |
| `integration.config.authType`       | Authentication type for the API (use `bearer_token` for Azure Monitor).                                                         | bearer\_token                   | â       |
| `integration.config.apiToken`       | Azure Resource Manager API bearer token created via the OAuth2 client credentials flow.                                         | eyJ0eXAiOiJKV1QiLCJub25jZSI6... | â       |
| `integration.config.paginationType` | How the API handles pagination (offset, page, cursor, or none).                                                                 | none                            | â       |
| `integration.eventListener.type`    | Event listener type. See [event listeners](https://ocean.getport.io/framework/features/event-listener).                         | POLLING                         | â       |
| `integration.type`                  | Integration type (must be `custom`).                                                                                            | custom                          | â       |
| `integration.identifier`            | Unique identifier for the integration instance.                                                                                 | azure-monitor-integration       | â       |
| `scheduledResyncInterval`           | Minutes between scheduled syncs. When omitted, the event listener interval is used.                                             | 120                             | â       |
| `initializePortResources`           | When true, creates default blueprints and mappings on first run.                                                                | true                            | â       |
| `sendRawDataExamples`               | Sends sample payloads from the API to Port for easier mapping.                                                                  | true                            | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, and `YOUR_BEARER_TOKEN`. Get your bearer token using the curl command in the Prerequisites section.

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://management.azure.com" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="bearer_token" \
  -e OCEAN__INTEGRATION__CONFIG__API_TOKEN="YOUR_BEARER_TOKEN" \
  -e OCEAN__PORT__CLIENT_ID="YOUR_PORT_CLIENT_ID" \
  -e OCEAN__PORT__CLIENT_SECRET="YOUR_PORT_CLIENT_SECRET" \
  -e OCEAN__PORT__BASE_URL="https://api.port.io" \
  ghcr.io/port-labs/port-ocean-custom:latest
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

Before the integration can sync data, you need to create the required blueprints in Port. These blueprints define the data model for your Azure Monitor resources.

**To create the blueprints:**

1. Go to your [Builder page](https://app.getport.io/settings/data-model).

2. Click on the `+ Blueprint` button.

3. Copy and paste each blueprint JSON from the sections below.

   **Azure monitor alert blueprint (click to expand)**

   Metric alert rules:

   Create in Port

   ```
   {
     "identifier": "azure-monitor-alert",
     "title": "Azure Monitor Alert",
     "icon": "Microsoft",
     "schema": {
       "properties": {
         "name": {
           "title": "Name",
           "type": "string"
         },
         "description": {
           "title": "Description",
           "type": "string"
         },
         "severity": {
           "title": "Severity",
           "type": "string"
         },
         "enabled": {
           "title": "Enabled",
           "type": "boolean"
         },
         "evaluationFrequency": {
           "title": "Evaluation Frequency",
           "type": "string"
         },
         "windowSize": {
           "title": "Window Size",
           "type": "string"
         },
         "targetResourceType": {
           "title": "Target Resource Type",
           "type": "string"
         },
         "targetResourceRegion": {
           "title": "Target Resource Region",
           "type": "string"
         },
         "subscriptionId": {
           "title": "Subscription ID",
           "type": "string"
         },
         "resourceGroup": {
           "title": "Resource Group",
           "type": "string"
         },
         "createdAt": {
           "title": "Created At",
           "type": "string",
           "format": "date-time"
         },
         "updatedAt": {
           "title": "Updated At",
           "type": "string",
           "format": "date-time"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Azure monitor activity log blueprint (click to expand)**

   Activity log events:

   Create in Port

   ```
   {
     "identifier": "azure-monitor-activity-log",
     "title": "Azure Monitor Activity Log",
     "icon": "Microsoft",
     "schema": {
       "properties": {
         "eventName": {
           "title": "Event Name",
           "type": "string"
         },
         "resourceId": {
           "title": "Resource ID",
           "type": "string"
         },
         "resourceGroupName": {
           "title": "Resource Group Name",
           "type": "string"
         },
         "resourceProviderName": {
           "title": "Resource Provider Name",
           "type": "string"
         },
         "status": {
           "title": "Status",
           "type": "string"
         },
         "subStatus": {
           "title": "Sub Status",
           "type": "string"
         },
         "eventTimestamp": {
           "title": "Event Timestamp",
           "type": "string",
           "format": "date-time"
         },
         "caller": {
           "title": "Caller",
           "type": "string"
         },
         "operationName": {
           "title": "Operation Name",
           "type": "string"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

## Configuration[â](#configuration "Direct link to Configuration")

After installation, define which endpoints to sync in your integration configuration. Each resource maps an API endpoint to Port entities using [JQ expressions](https://stedolan.github.io/jq/manual/) to transform the data.

**Key mapping components:**

* **`kind`**: The API endpoint path (combined with your base URL).
* **`selector.query`**: JQ filter to include/exclude entities (use `'true'` to sync all).
* **`selector.data_path`**: JQ expression pointing to the array of items in the response.
* **`port.entity.mappings`**: How to map API fields to Port entity properties.

For more details on how the Ocean Custom Integration works, see the [How it works](https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/overview#how-it-works) section in the custom integration overview.

**Azure Monitor API response format:**

Azure Monitor API responses typically follow this structure:

```
{
  "value": [
    {
      "id": "/subscriptions/.../providers/Microsoft.Insights/metricAlerts/alert-name",
      "name": "alert-name",
      "type": "Microsoft.Insights/metricAlerts",
      "properties": {
        "description": "Alert description",
        "severity": 2,
        "enabled": true,
        ...
      }
    }
  ]
}
```

The actual data array is in the `.value` property.

**To configure the mappings:**

1. Go to your [data sources page](https://app.getport.io/settings/data-sources).

2. Find your Azure Monitor integration in the list.

3. Click on the integration to open the mapping editor.

4. Add the resource mapping configurations below.

   **Metric Alerts mapping (click to expand)**

   ```
   resources:
     - kind: /subscriptions/YOUR_SUBSCRIPTION_ID/providers/Microsoft.Insights/metricAlerts
       selector:
         query: 'true'
         data_path: .value
         query_params:
           api-version: '2018-03-01'
       port:
         entity:
           mappings:
             identifier: .id
             title: .name
             blueprint: '"azure-monitor-alert"'
             properties:
               name: .name
               description: .properties.description
               severity: .properties.severity
               enabled: .properties.enabled
               evaluationFrequency: .properties.evaluationFrequency
               windowSize: .properties.windowSize
               targetResourceType: .properties.targetResourceType
               targetResourceRegion: .properties.targetResourceRegion
               subscriptionId: (.id | split("/")[2])
               resourceGroup: (.properties.scopes[0] | split("/")[4] // "")
               createdAt: .properties.createdAt
               updatedAt: .properties.updatedAt
   ```

   Subscription ID

   Replace `YOUR_SUBSCRIPTION_ID` in the `kind` path with your actual Azure subscription ID.

   **Activity Logs mapping (click to expand)**

   ```
   resources:
     - kind: /subscriptions/YOUR_SUBSCRIPTION_ID/providers/Microsoft.Insights/eventtypes/management/values
       selector:
         query: 'true'
         data_path: .value
         query_params:
           api-version: '2015-04-01'
           $filter: "eventTimestamp ge '2025-12-01T00:00:00Z'"
       port:
         entity:
           mappings:
             identifier: .id
             title: .eventName.localizedValue // .operationName.localizedValue
             blueprint: '"azure-monitor-activity-log"'
             properties:
               eventName: .eventName.localizedValue
               resourceId: .resourceId
               resourceGroupName: .resourceGroupName
               resourceProviderName: .resourceProviderName.value
               status: .status.localizedValue
               subStatus: .subStatus.localizedValue
               eventTimestamp: .eventTimestamp
               caller: .caller
               operationName: .operationName.localizedValue
   ```

   Activity log filtering

   Activity logs can be very large and the API requires a date filter. Use the `$filter` query parameter to limit results by date range. The start time cannot be more than 90 days in the past. Replace the date in the filter with a date within the last 90 days.

5. Click `Save` to save the mapping.

## Customization[â](#customization "Direct link to Customization")

If you want to customize your setup or test different API endpoints before committing to a configuration, use the [interactive builder](https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration).

**The interactive builder helps you:**

1. Test your Azure Monitor API endpoints with live data.
2. Automatically detect the data structure and field types.
3. Generate blueprints and resource mappings tailored to your preferences.
4. Get installation commands with your configuration pre-filled.

Simply provide your Azure Monitor API details, and the builder will generate everything you need to install and create the integration in Port.

## Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

### Authentication errors[â](#authentication-errors "Direct link to Authentication errors")

**Symptom:** 401 "InvalidAuthenticationToken" or "Lifetime validation failed, the token is expired" errors.

**Solution:**

* Access tokens expire after 1 hour
* For production use, implement automatic token refresh or use OAuth2 client credentials flow with automatic token management
* See the [prerequisites](#prerequisites) section for token generation commands.

### API version errors[â](#api-version-errors "Direct link to API version errors")

**Symptom:** 400 "Bad Request" errors with API version messages.

**Solution:**

* Azure Monitor API requires the `api-version` query parameter.
* Ensure you include `api-version` in your `query_params` (e.g., `api-version: "2018-03-01"`).
* Check the [Azure Monitor REST API documentation](https://learn.microsoft.com/en-us/rest/api/monitor/) for the correct API version for your endpoint.

### Subscription access errors[â](#subscription-access-errors "Direct link to Subscription access errors")

**Symptom:** 403 "Forbidden" or "Authorization failed" errors.

**Solution:**

* Ensure your application has the correct permissions in Azure.
* Verify the subscription ID is correct.
* Check that admin consent has been granted for the API permissions.
* Verify your application has "Reader" role or appropriate permissions on the subscription.

### Activity log size issues[â](#activity-log-size-issues "Direct link to Activity log size issues")

**Symptom:** Very large responses or timeouts when fetching activity logs.

**Solution:**

* Use `$filter` query parameter to limit results by date range.
* Consider syncing only recent activity logs (e.g., last 7 days).
* Use pagination if available for the specific endpoint.
* Adjust `scheduledResyncInterval` to sync less frequently.
