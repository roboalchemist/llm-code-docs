# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/other/backstage.md

# Backstage

Loading version...

Port's Backstage integration allows you to model Backstage resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Backstage resources and their metadata in Port (see supported resources below).
* Watch for Backstage object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Backstage into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Entities API`](https://backstage.io/docs/features/software-catalog/software-catalog-api/#get-entitiesby-query)
* [`Component`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-component)
* [`Template`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-template)
* [`API`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-api)
* [`Group`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-group)
* [`User`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-user)
* [`Resource`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-resource)
* [`System`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-system)
* [`Domain`](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-domain)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Create a Backstage token[â](#create-a-backstage-token "Direct link to Create a Backstage token")

Port will authenticate to Backstage via [static tokens](https://backstage.io/docs/auth/service-to-service-auth/#static-tokens).<br /><!-- -->Configure a token for Port using the following Backstage configuration:

```
backend:
  auth:
    externalAccess:
      - type: static
        options:
          token: YOUR-TOKEN
          subject: port-ocean-access
```

Replace `YOUR-TOKEN` with your Backstage token.<br /><!-- -->To create a token, Backstage recommends to use the following command:

```
node -p 'require("crypto").randomBytes(24).toString("base64")'
```

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [Backstage<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Backstage) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  Currently, live events are not supported for this integration.<br />Resyncs will be performed **periodically** (with a configurable interval), or **manually** triggered by you via Port's UI.

  Therefore, real-time events (including GitOps) will not be ingested into Port immediately.<br />Live events support for this integration is WIP and will be supported in the near future.

  <!-- -->

### Port secrets

Some integration settings require sensitive pieces of data, such as tokens. For these settings, [Port secrets](/sso-rbac/port-secrets/.md) will be used, ensuring that your sensitive data is encrypted and secure.

When filling in such a setting, its value will be obscured (shown as `â¢â¢â¢â¢â¢â¢â¢â¢`). For each such setting, Port will automatically create a secret in your organization.

To see all secrets in your organization, follow [these steps](/sso-rbac/port-secrets/.md#usage).

### Limitations

* The maximum time for a full sync to run is based on the configured resync interval. For very large amounts of data where a resync operation is expected to take longer, please use a longer interval.

### Port source IP addresses

When using this installation method, Port will make outbound calls to your 3rd-party applications from static IP addresses. You may need to add these addresses to your allowlist, in order to allow Port to interact with the integrated service:

* **Europe (EU)**: `54.73.167.226`, `63.33.143.237`, `54.76.185.219`
* **United States (US)**: `3.234.37.33`, `54.225.172.136`, `3.225.234.99`

Using this installation method means that the integration will be able to update Port in real time using webhooks.

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

<!-- -->

1. Go to the [Backstage<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Backstage) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Backstage<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Backstage<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Backstage<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Backstage
  <!-- -->
  can reach.

If `liveEvents.baseUrl` is not provided, the integration will continue to function correctly. In such a configuration, to retrieve the latest information from the target system, the [`scheduledResyncInterval`](https://ocean.port.io/developing-an-integration/trigger-your-integration) parameter has to be set, or a manual resync will need to be triggered through Port's UI.

Debugging local integrations

To test webhooks or live event delivery to your local environment, expose your local pod or service to the internet using ngrok (e.g. `ngrok http http://localhost:8000`)

<!-- -->

<!-- -->

### Scalable mode for large integrations[â](#scalable-mode-for-large-integrations "Direct link to Scalable mode for large integrations")

If you are deploying the integration at scale and want to decouple the resync process from the live events process (recommended for large or high-throughput environments), you can enable scalable mode by adding the following flags to your Helm install command:

```
  --set workload.kind="CronJob"  \
  --set workload.cron.resyncTimeoutMinutes=60  \
  --set scheduledResyncInterval="'*/60 * * * *'"  \
  --set liveEvents.worker.enabled=true
```

<!-- -->

<!-- -->

<!-- -->

For details about the available parameters for the installation, see the table below.

This table summarizes the parameters used for the installation.<br /><!-- -->Note the parameters specific to this integration, they are last in the table.

| Parameter                                | Description                                                                                                                         | Required |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                          | Your Port client id, used to identify your account                                                                                  | â       |
| `port.clientSecret`                      | Your Port client secret, used to identify your account                                                                              | â       |
| `port.baseUrl`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                   | â       |
| `initializePortResources`                | Default: `true`. When `true`, the integration will create default blueprints and configuration mapping                              | â       |
| `sendRawDataExamples`                    | Default: `true`. Enable sending raw data examples from the third party API to Port for testing and managing the integration mapping | â       |
| `integration.identifier`                 | The integration's identifier, used to reference the integration when using Port's API                                               | â       |
| `integration.type`                       | The integration type, used to denote the integrated tool/platform                                                                   | â       |
| `integration.eventListener.type`         | The method used to listen to events from the 3rd party tool (`POLLING` or `KAFKA`)                                                  | â       |
| **`integration.secrets.backstageToken`** | The Backstage token used to authenticate Port to Backstage                                                                          | â       |
| **`integration.config.backstageUrl`**    | The URL of the Backstage instance, including the port of the Backend API (usually 7007)                                             | â       |

This installation method will run the integration once and then exit, this is useful for **scheduled** ingestion of data.

The integration will run as a workflow in your CI/CD pipeline.

1. Go to the [Backstage<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Backstage) in your portal.

2. Select the `Scheduled` method using your preferred CI/CD tool.

   ![](/img/sync-data-to-catalog/scheduledCiMethod.png)

3. Copy the workflow contents into a new workflow in your CI/CD tool. Make sure to:

   * Create the necessary secrets in your CI/CD tool.
   * Replace the placeholders in the workflow with your own values.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
resources:
- kind: component
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"component"'
        properties:
          type: .spec.type
          lifecycle: .spec.lifecycle
          language: .spec.language
          description: .metadata.description
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
        relations:
          owningUser: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("user:"))) | .targetRef
          owningGroup: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("group:"))) | .targetRef
          system: '"system:" + (.metadata.namespace // "default") + "/" + .spec.system'
          subcomponentOf: .relations[] | select(.type == "subcomponentOf" and (.targetRef | startswith("component:"))) | .targetRef
          providesApis: .relations[] | select(.type == "providesApi" and (.targetRef | startswith("api:"))) | .targetRef
          consumesApis: .relations[] | select(.type == "consumesApi" and (.targetRef | startswith("api:"))) | .targetRef
          dependsOnComponent: .relations[] | select(.type == "dependsOn" and (.targetRef | startswith("component:"))) | .targetRef
          dependsOnResource: .relations[] | select(.type == "dependsOn" and (.targetRef | startswith("resource:"))) | .targetRef
- kind: API
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"api"'
        properties:
          type: .spec.type
          lifecycle: .spec.lifecycle
          definition: .spec.definition | tostring
          definitionOpenAPI: if .spec.type == "open-api" then .spec.definition else null end
          definitionAsyncAPI: if .spec.type == "async-api" then .spec.definition else null end
          definitionGRPC: if .spec.type == "grpc" then .spec.definition else null end
          definitionGraphQL: if .spec.type == "graphql" then .spec.definition else null end
          description: .metadata.description
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
        relations:
          owningUser: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("user:"))) | .targetRef
          owningGroup: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("group:"))) | .targetRef
          system: '"system:" + (.metadata.namespace // "default") + "/" + .spec.system'
- kind: group
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"group"'
        properties:
          description: .metadata.description
          type: .metadata.type
          email: .metadata.email
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
        relations:
          parent: .relations[] | select(.type == "childOf" and (.targetRef | startswith("group:"))) | .targetRef
          members: .relations[] | select(.type == "hasMember" and (.targetRef | startswith("user:"))) | .targetRef
- kind: user
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"user"'
        properties:
          email: .metadata.email
          description: .metadata.description
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
- kind: resource
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"resource"'
        properties:
          type: .spec.type
          description: .metadata.description
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
        relations:
          owningUser: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("user:"))) | .targetRef
          owningGroup: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("group:"))) | .targetRef
          system: '"system:" + (.metadata.namespace // "default") + "/" + .spec.system'
          dependsOnResource: .relations[] | select(.type == "dependsOn" and (.targetRef | startswith("resource:"))) | .targetRef
          dependsOnComponent: .relations[] | select(.type == "dependsOn" and (.targetRef | startswith("component:"))) | .targetRef
- kind: system
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"system"'
        properties:
          description: .metadata.description
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
        relations:
          owningUser: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("user:"))) | .targetRef
          owningGroup: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("group:"))) | .targetRef
          domain: .relations[] | select(.type == "partOf" and (.targetRef | startswith("domain:"))) | .targetRef
- kind: domain
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .metadata.identifier
        title: .metadata.title // .metadata.name
        blueprint: '"domain"'
        properties:
          description: .metadata.description
          labels: .metadata.labels
          annotations: .metadata.annotations
          links: .metadata.links
          tags: .metadata.tags
        relations:
          owningUser: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("user:"))) | .targetRef
          owningGroup: .relations[] | select(.type == "ownedBy" and (.targetRef | startswith("group:"))) | .targetRef
```

## Limitations[â](#limitations "Direct link to Limitations")

Currently, the integration does not support [custom entity](https://backstage.io/docs/features/software-catalog/extending-the-model/#implementing-custom-model-extensions) kinds.

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations:

### Component[â](#component "Direct link to Component")

**Component blueprint (click to expand)**

Create in Port

```
{
  "identifier": "component",
  "title": "Component",
  "icon": "Cloud",
  "schema": {
    "properties": {
      "type": {
        "title": "Type",
        "type": "string"
      },
      "lifecycle": {
        "title": "Lifecycle",
        "type": "string"
      },
      "language": {
        "type": "string",
        "title": "Language"
      },
      "description": {
        "type": "string",
        "format": "markdown",
        "title": "Description"
      },
      "labels": {
        "type": "object",
        "title": "Labels"
      },
      "annotations": {
        "type": "object",
        "title": "Annotations"
      },
      "links": {
        "type": "array",
        "items": {
          "format": "url",
          "type": "string"
        },
        "title": "Links"
      },
      "tags": {
        "type": "array",
        "title": "Tags"
      }
    },
    "required": []
  },
  "calculationProperties": {}
}
```

**Mapping configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: component
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .metadata.identifier
          title: .metadata.title // .metadata.name
          blueprint: '"component"'
          properties:
            type: .spec.type
            lifecycle: .spec.lifecycle
            language: .spec.language
            description: .metadata.description
            labels: .metadata.labels
            annotations: .metadata.annotations
            links: .metadata.links
            tags: .metadata.tags
```

### Group[â](#group "Direct link to Group")

**Group blueprint (click to expand)**

Create in Port

```
{
  "identifier": "group",
  "title": "Group",
  "icon": "TwoUsers",
  "schema": {
    "properties": {
      "type": {
        "title": "Type",
        "type": "string"
      },
      "email": {
        "title": "Email",
        "type": "string",
        "format": "email"
      },
      "description": {
        "type": "string",
        "format": "markdown",
        "title": "Description"
      },
      "labels": {
        "type": "object",
        "title": "Labels"
      },
      "annotations": {
        "type": "object",
        "title": "Annotations"
      },
      "links": {
        "type": "array",
        "items": {
          "format": "url",
          "type": "string"
        },
        "title": "Links"
      },
      "tags": {
        "type": "array",
        "title": "Tags"
      }
    },
    "required": []
  },
  "calculationProperties": {}
}
```

**Mapping configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: group
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .metadata.identifier
          title: .metadata.title // .metadata.name
          blueprint: '"group"'
          properties:
            description: .metadata.description
            type: .metadata.type
            email: .metadata.email
            labels: .metadata.labels
            annotations: .metadata.annotations
            links: .metadata.links
            tags: .metadata.tags
```
