# Source: https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/setup.md

# Setup

Using this installation option means that the integration will run in your own infrastructure, giving you full control over resources and configuration. You can deploy it using Helm or Docker, and it will run continuously in your environment to keep your data synchronized with Port.

High-scale environments

For high-scale environments with large datasets, allocate sufficient CPU and memory based on your data volume.

## Installation[â](#installation "Direct link to Installation")

Choose your preferred deployment method:

* Helm
* Docker

To install the integration using Helm:

1. Go to the [custom data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Custom) in your portal.

2. Select the **Real-time and always on** method:

![](/img/sync-data-to-catalog/selfHostedMethod.png)

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

Alternatively, you can install manually using the following steps:

1. Add Port's Helm chart repository:

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
```

2. Install the Helm chart with your configuration:

```
helm install ocean-custom port-labs/port-ocean \
  --set port.clientId="<PORT_CLIENT_ID>" \
  --set port.clientSecret="<PORT_CLIENT_SECRET>" \
  --set port.baseUrl="https://api.port.io" \
  --set initializePortResources=true \
  --set scheduledResyncInterval=60 \
  --set integration.identifier="ocean-custom" \
  --set integration.type="custom" \
  --set integration.eventListener.type="POLLING" \
  --set integration.config.baseUrl="https://api.yourcompany.com" \
  --set integration.config.authType="bearer_token" \
  --set integration.secrets.apiToken="<YOUR_API_TOKEN>" \
  --set integration.config.paginationType="page" \
  --set integration.config.pageSize=100
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

To install the integration using Docker:

1. Pull the Docker image:

```
docker pull ghcr.io/port-labs/port-ocean-custom:latest
```

2. Run the container with your configuration:

```
docker run -i --rm \
  -e OCEAN__PORT__CLIENT_ID="<PORT_CLIENT_ID>" \
  -e OCEAN__PORT__CLIENT_SECRET="<PORT_CLIENT_SECRET>" \
  -e OCEAN__PORT__BASE_URL="https://api.port.io" \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SCHEDULED_RESYNC_INTERVAL=60 \
  -e OCEAN__INTEGRATION__IDENTIFIER="ocean-custom" \
  -e OCEAN__INTEGRATION__TYPE="custom" \
  -e OCEAN__EVENT_LISTENER='{"type":"POLLING"}' \
  -e OCEAN__INTEGRATION__CONFIG__BASE_URL="https://api.yourcompany.com" \
  -e OCEAN__INTEGRATION__CONFIG__AUTH_TYPE="bearer_token" \
  -e OCEAN__INTEGRATION__CONFIG__API_TOKEN="<YOUR_API_TOKEN>" \
  -e OCEAN__INTEGRATION__CONFIG__PAGINATION_TYPE="page" \
  -e OCEAN__INTEGRATION__CONFIG__PAGE_SIZE=100 \
  ghcr.io/port-labs/port-ocean-custom:latest
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Health check endpoint

All Ocean integrations expose a health check endpoint at `/docs`.

For example, if your integration is accessible at `https://your-integration-host:8000`, you can access the health check at `https://your-integration-host:8000/docs`.

## Configuration parameters[â](#configuration-parameters "Direct link to Configuration parameters")

This table summarizes the available parameters for the installation.

| Parameter                           | Description                                                                                                                                                                                                                                                                                     | Example                       | Required |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------- |
| `port.clientId`                     | Your port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                                                                      |                               | â       |
| `port.clientSecret`                 | Your port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                                                                  |                               | â       |
| `port.baseUrl`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                                                                                                                               |                               | â       |
| `integration.config.baseUrl`        | The root URL of your API (e.g., `https://api.yourcompany.com`)                                                                                                                                                                                                                                  | <https://api.yourcompany.com> | â       |
| `integration.config.authType`       | Authentication type: `bearer_token`, `api_key`, `basic_auth`, `custom`, or `none`. For custom authentication (OAuth2, JWT, etc.), see [custom authentication](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/custom-authentication.md) | bearer\_token                 | â       |
| `integration.secrets.apiToken`      | Bearer token for authentication (required when `authType` is `bearer_token`)                                                                                                                                                                                                                    |                               | â       |
| `integration.config.paginationType` | Pagination type: `offset`, `page`, `cursor`, or `none`                                                                                                                                                                                                                                          | page                          | â       |
| `integration.config.pageSize`       | Number of items per page (for offset/page pagination)                                                                                                                                                                                                                                           | 100                           | â       |
| `integration.config.timeout`        | Request timeout in seconds (default: 30)                                                                                                                                                                                                                                                        | 30                            | â       |
| `integration.eventListener.type`    | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)                                                                                                                                                                          | POLLING                       | â       |
| `integration.type`                  | The integration to be installed                                                                                                                                                                                                                                                                 | custom                        | â       |
| `scheduledResyncInterval`           | The number of minutes between each resync. When not set the integration will resync for each event listener resync event. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration)                                                   | 60                            | â       |
| `initializePortResources`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                                                                  | true                          | â       |
| `sendRawDataExamples`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                                                                                                                             | true                          | â       |

<!-- -->

<!-- -->

## Recommended resource sizes

To ensure optimal performance and avoid out-of-memory (OOM) errors, we recommend the following resources for this integration:

* **CPU Limit**: `800m`
* **CPU Request**: `400m`
* **Memory Limit**: `4Gi`
* **Memory Request**: `4Gi`

### Set resource values

```
helm install my-integration port-labs/port-ocean \
# ... other parameters
--set ocean.resources.limits.cpu=800m \
--set ocean.resources.limits.memory=4Gi \
--set ocean.resources.requests.cpu=400m \
--set ocean.resources.requests.memory=4Gi
```

## Authentication[â](#authentication "Direct link to Authentication")

The integration supports several authentication types:

* **Bearer token**: Use `authType: "bearer_token"` with an API token
* **API key**: Use `authType: "api_key"` with an API key and optional custom header name
* **Basic auth**: Use `authType: "basic_auth"` with username and password
* **Custom authentication**: Use `authType: "custom"` for OAuth2, JWT, and other dynamic token-based flows. See [custom authentication](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/custom-authentication.md) for details.
* **None**: Use `authType: "none"` for public APIs without authentication

## Ready to build?[â](#ready-to-build "Direct link to Ready to build?")

Head to [build your integration](/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md) for a step-by-step guide with an interactive configuration builder.

## More resources[â](#more-resources "Direct link to More resources")

For all configuration options, code examples, and advanced use cases, check out the [Ocean custom integration repository on GitHub](https://github.com/port-labs/ocean/tree/main/integrations/custom).
