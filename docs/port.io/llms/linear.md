# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/linear.md

# Linear

Loading version...

Port's Linear integration allows you to model Linear resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Linear resources and their metadata in Port (see supported resources below).
* Watch for Linear object changes (create/update/delete) in real-time, and automatically apply the changes to your software catalog.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Linear into Port are listed below.<br /><!-- -->It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [Team](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/TeamConnection)
* [Issue](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/IssueConnection)
* [Label](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/IssueLabelConnection)

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [Linear<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Linear) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

  **Supported live event triggers (click to expand)**

  * Issue
  * IssueLabel

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

Using this installation option means that the integration will be able to update Port in real time using webhooks.

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

For details about the available parameters for the installation, see the table below.

* Helm
* ArgoCD

<!-- -->

1. Go to the [Linear<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Linear) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Linear<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Linear<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Linear<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Linear
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

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

To install the integration using ArgoCD:

1. Create a `values.yaml` file in `argocd/my-ocean-linear-integration` in your git repository with the content:

note

Remember to replace the placeholder for `LINEAR_API_KEY`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-linear-integration
  type: linear
  eventListener:
    type: POLLING
  secrets:
    linearApiKey: LINEAR_API_KEY
```

<br />

1. Install the `my-ocean-linear-integration` ArgoCD Application by creating the following `my-ocean-linear-integration.yaml` manifest:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.<br /><!-- -->Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-linear-integration
  namespace: argocd
spec:
  destination:
    namespace: mmy-ocean-linear-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-linear-integration/values.yaml
      parameters:
        - name: port.clientId
          value: YOUR_PORT_CLIENT_ID
        - name: port.clientSecret
          value: YOUR_PORT_CLIENT_SECRET
        - name: port.baseUrl
          value: https://api.port.io
  - repoURL: YOUR_GIT_REPO_URL
    targetRevision: main
    ref: values
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

<br />

1. Apply your application manifest with `kubectl`:

```
kubectl apply -f my-ocean-linear-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                                 | Description                                                                                                                                                                                                                                   | Example                            | Required |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `port.clientId`                           | Your port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                    |                                    | â       |
| `port.clientSecret`                       | Your port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                |                                    | â       |
| `port.baseUrl`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                                                                             |                                    | â       |
| `integration.secrets.linearApiKey`        | Linear [API key](https://developers.linear.app/docs/graphql/working-with-the-graphql-api#personal-api-keys) used to query the Linear GraphQL API                                                                                              |                                    | â       |
| `integration.eventListener.type`          | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)                                                                                                                        |                                    | â       |
| `integration.type`                        | The integration to be installed                                                                                                                                                                                                               |                                    | â       |
| `integration.config.appHost` (deprecated) | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear. This field is deprecated. Please use the `liveEvents.baseUrl`field instead                                              | <https://my-ocean-integration.com> | â       |
| `liveEvents.baseUrl`                      | The base url of the instance where the Linear integration is hosted, used for real-time updates.                                                                                                                                              | <https://my-ocean-integration.com> | â       |
| `scheduledResyncInterval`                 | The number of minutes between each resync. When not set the integration will resync for each event listener resync event. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration) |                                    | â       |
| `initializePortResources`                 | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                |                                    | â       |
| `sendRawDataExamples`                     | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                                                                           |                                    | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

This workflow/pipeline will run the Linear integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                   | Description                                                                                                                                                 | Example                            | Required |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `port_client_id`            | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |                                    | â       |
| `port_client_secret`        | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |                                    | â       |
| `port_base_url`             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |                                    | â       |
| `config -> linear_api_key`  | Linear [API key](https://developers.linear.app/docs/graphql/working-with-the-graphql-api#personal-api-keys) used to query the Linear GraphQL API            |                                    | â       |
| `initialize_port_resources` | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |                                    | â       |
| `identifier`                | The identifier of the integration that will be installed                                                                                                    |                                    | â       |
| `version`                   | The version of the integration that will be installed                                                                                                       | latest                             | â       |
| `sendRawDataExamples`       | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | true                               |          |
| `liveEvents.baseUrl`        | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        | <https://my-ocean-integration.com> | â       |

<br />

Ocean Sail Github Action

The following example uses the **Ocean Sail** Github Action to run the Linear integration. For further information about the action, please visit the [Ocean Sail Github Action](https://github.com/marketplace/actions/ocean-sail)

<br />

Here is an example for `linear-integration.yml` workflow file:

```
name: Linear Exporter Workflow

on:
  workflow_dispatch:
  schedule:
    - cron: '0 */1 * * *' # Determines the scheduled interval for this workflow. This example runs every hour.

jobs:
  run-integration:
    runs-on: ubuntu-latest
    timeout-minutes: 30 # Set a time limit for the job

    steps:
      - uses: port-labs/ocean-sail@v1
        with:
          type: 'linear'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            linear_api_key: ${{ secrets.OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY }}
```

Tip for Jenkins agent

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                    | Description                                                                                                                                                 | Example | Required |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY` | Linear API key used to query the Linear GraphQL API                                                                                                         |         | â       |
| `OCEAN__PORT__CLIENT_ID`                     | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`                 | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`             | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`              | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |
| `OCEAN__BASE_URL`                            | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        |         | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Linear Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY', variable: 'OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="linear"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY=$OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY \
                                -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
                                -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
                                -e OCEAN__PORT__BASE_URL='https://api.port.io' \
                                $image_name

                            exit $?
                        ''')
                    }
                }
            }
        }
    }
}
```

**Prerequisites**

* Your Azure Devops agent should be able to run docker commands. Learn more about agents [here](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops\&tabs=yaml%2Cbrowser).
* You must have permissions to create and manage Azure DevOps [variable groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops\&tabs=yaml) for storing credentials.

**Set up your credentials**

1. Create a Variable Group: Name it **port-ocean-credentials**.

2. Store the required variables (see the table below).

3. Authorize Your Pipeline:

   <!-- -->

   * Go to **"Library" -> "Variable groups."**

   * Find **port-ocean-credentials** and click on it.

   * Select "Pipeline Permissions" and add your pipeline to the authorized list.

     ![](/img/build-your-software-catalog/sync-data-to-catalog/code-quality-security/azureVarGroups.png)

<br />

| Parameter                                    | Description                                                                                                                                                 | Example | Required |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY` | Linear API key used to query the Linear GraphQL API                                                                                                         |         | â       |
| `OCEAN__PORT__CLIENT_ID`                     | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`                 | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`             | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`              | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |
| `OCEAN__BASE_URL`                            | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        |         | â       |

<br />

Here is an example for `linear-integration.yml` pipeline file:

```
trigger:
  - main

pool:
  vmImage: "ubuntu-latest"

variables:
  - group: port-ocean-credentials

steps:
  - script: |
      # Set Docker image and run the container
      integration_type="linear"
      version="latest"

      image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

      docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY=$(OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

      exit $?
    displayName: "Ingest Data into Port"
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                    | Description                                                                                                                                                 | Example | Required |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY` | Linear API key used to query the Linear GraphQL API                                                                                                         |         | â       |
| `OCEAN__PORT__CLIENT_ID`                     | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`                 | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`             | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`              | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |
| `OCEAN__BASE_URL`                            | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        |         | â       |

<br />

Here is an example for `.gitlab-ci.yml` pipeline file:

```
default:
  image: docker:24.0.5
  services:
    - docker:24.0.5-dind
  before_script:
    - docker info
    
variables:
  INTEGRATION_TYPE: linear
  VERSION: latest

stages:
  - ingest

ingest_data:
  stage: ingest
  variables:
    IMAGE_NAME: ghcr.io/port-labs/port-ocean-$INTEGRATION_TYPE:$VERSION
  script:
    - |
      docker run -i --rm --platform=linux/amd64 \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY=$OCEAN__INTEGRATION__CONFIG__LINEAR_API_KEY \
        -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
        -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration you get after installing the Linear integration.

**Default mapping configuration (Click to expand)**

```

createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
- kind: team
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .key
        title: .name
        blueprint: '"linearTeam"'
        properties:
          description: .description
          workspaceName: .organization.name
          url: '"https://linear.app/" + .organization.urlKey + "/team/" + .key'
- kind: label
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"linearLabel"'
        properties:
          isGroup: .isGroup
        relations:
          parentLabel: .parent.id
          childLabels: '[.children.edges[].node.id]'
- kind: issue
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .identifier
        title: .title
        blueprint: '"linearIssue"'
        properties:
          url: .url
          status: .state.name
          assignee: .assignee.email
          creator: .creator.email
          priority: .priorityLabel
          created: .createdAt
          updated: .updatedAt
        relations:
          team: .team.key
          labels: .labelIds
          parentIssue: .parent.identifier
          childIssues: .children.edges[].node.identifier
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations:

### Team[â](#team "Direct link to Team")

Team blueprint

Create in Port

```
{
  "identifier": "linearTeam",
  "title": "Linear Team",
  "icon": "Linear",
  "description": "A Linear team",
  "schema": {
    "properties": {
      "description": {
        "type": "string",
        "title": "Description",
        "description": "Team description"
      },
      "workspaceName": {
        "type": "string",
        "title": "Workspace Name",
        "description": "The name of the workspace this team belongs to"
      },
      "url": {
        "title": "Team URL",
        "type": "string",
        "format": "url",
        "description": "URL to the team in Linear"
      }
    }
  },
  "calculationProperties": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: team
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .key
          title: .name
          blueprint: '"linearTeam"'
          properties:
            description: .description
            workspaceName: .organization.name
            url: "\"https://linear.app/\" + .organization.urlKey + \"/team/\" + .key"
```

### Label[â](#label "Direct link to Label")

Label blueprint

Create in Port

```
{
  "identifier": "linearLabel",
  "title": "Linear Label",
  "icon": "Linear",
  "description": "A Linear label",
  "schema": {
    "properties": {
      "isGroup": {
        "type": "boolean",
        "title": "Is group",
        "description": "Whether this label is considered to be a group"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "parentLabel": {
      "target": "linearLabel",
      "title": "Parent Label",
      "required": false,
      "many": false
    },
    "childLabels": {
      "target": "linearLabel",
      "title": "Child Labels",
      "required": false,
      "many": true
    }
  }
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: label
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"linearLabel"'
          properties:
            isGroup: .isGroup
          relations:
            parentLabel: .parent.id
            childLabels: "[.children.edges[].node.id]"
```

### Issue[â](#issue "Direct link to Issue")

Issue blueprint

Create in Port

```
{
  "identifier": "linearIssue",
  "title": "Linear Issue",
  "icon": "Linear",
  "schema": {
    "properties": {
      "url": {
        "title": "Issue URL",
        "type": "string",
        "format": "url",
        "description": "URL to the issue in Linear"
      },
      "status": {
        "title": "Status",
        "type": "string",
        "description": "The status of the issue"
      },
      "assignee": {
        "title": "Assignee",
        "type": "string",
        "format": "user",
        "description": "The user assigned to the issue"
      },
      "creator": {
        "title": "Creator",
        "type": "string",
        "description": "The user that created to the issue",
        "format": "user"
      },
      "priority": {
        "title": "Priority",
        "type": "string",
        "description": "The priority of the issue"
      },
      "created": {
        "title": "Created At",
        "type": "string",
        "description": "The created datetime of the issue",
        "format": "date-time"
      },
      "updated": {
        "title": "Updated At",
        "type": "string",
        "description": "The updated datetime of the issue",
        "format": "date-time"
      }
    }
  },
  "calculationProperties": {},
  "relations": {
    "team": {
      "target": "linearTeam",
      "title": "Team",
      "description": "The Linear team that contains this issue",
      "required": false,
      "many": false
    },
    "parentIssue": {
      "title": "Parent Issue",
      "target": "linearIssue",
      "required": false,
      "many": false
    },
    "labels": {
      "target": "linearLabel",
      "title": "Labels",
      "required": false,
      "many": true
    }
  }
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: issue
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .identifier
          title: .title
          blueprint: '"linearIssue"'
          properties:
            url: .url
            status: .state.name
            assignee: .assignee.email
            creator: .creator.email
            priority: .priorityLabel
            created: .createdAt
            updated: .updatedAt
          relations:
            team: .team.key
            labels: .labelIds
            parentIssue: .parent.identifier
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes sample response data from Linear. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Linear:

Team response data

```
{
  "id": "92d25fa4-fb1c-449f-b314-47f82e8f280d",
  "name": "Port",
  "key": "POR",
  "description": null,
  "organization": {
      "id": "36968e1b-496c-4610-8c25-641364da172e",
      "name": "Getport",
      "urlKey": "getport"
  }
}
```

Label response data

```
{
  "id": "36f84d2c-7b7d-4a71-96f2-6ea4140004d5",
  "createdAt": "2024-05-17T15:17:40.858Z",
  "updatedAt": "2024-05-17T15:17:40.858Z",
  "archivedAt": null,
  "name": "New-sample-label",
  "description": null,
  "color": "#bec2c8",
  "isGroup": true,
  "parent": null,
  "children": {
      "edges": [
          {
              "node": {
                  "id": "2e483c90-2aca-4db6-924d-b0571d49f691"
              }
          }
      ]
  }
}
```

Issue response data

```
{
  "id": "9b4745c2-a8e6-4432-9e56-0fa97b79ccbf",
  "createdAt": "2024-05-16T21:52:00.299Z",
  "updatedAt": "2024-05-17T09:27:40.077Z",
  "archivedAt": null,
  "number": 2,
  "title": "sub issue with new title",
  "priority": 3,
  "estimate": null,
  "sortOrder": -991,
  "startedAt": null,
  "completedAt": null,
  "startedTriageAt": null,
  "triagedAt": null,
  "canceledAt": null,
  "autoClosedAt": null,
  "autoArchivedAt": null,
  "dueDate": null,
  "slaStartedAt": null,
  "slaBreachesAt": null,
  "trashed": null,
  "snoozedUntilAt": null,
  "labelIds": [
      "402b218c-938c-4ddf-85db-0019bc632316"
  ],
  "previousIdentifiers": [],
  "subIssueSortOrder": -56.17340471045278,
  "priorityLabel": "Medium",
  "integrationSourceType": null,
  "identifier": "POR-2",
  "url": "https://linear.app/getport/issue/POR-2/sub-issue-with-new-title",
  "branchName": "mor/por-2-sub-issue-with-new-title",
  "customerTicketCount": 0,
  "description": "",
  "descriptionState": "AQG/pOWPAgAHAQtwcm9zZW1pcnJvcgMJcGFyYWdyYXBoAA==",
  "team": {
      "id": "92d25fa4-fb1c-449f-b314-47f82e8f280d",
      "name": "Port",
      "key": "POR"
  },
  "state": {
      "name": "Todo"
  },
  "creator": {
      "name": "Mor Paz",
      "email": "mor@getport.io"
  },
  "assignee": {
      "name": "Dudi Elhadad",
      "email": "dudi@getport.io"
  },
  "parent": {
      "id": "5ddd8e85-ad89-4c96-b901-0b901b29100d",
      "identifier": "POR-1"
  }
}
              
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Team entity in Port

```
{
  "identifier": "POR",
  "title": "Port",
  "icon": "Linear",
  "blueprint": "linearTeam",
  "team": [],
  "properties": {
      "url": "https://linear.app/getport/team/POR",
      "workspaceName": "Getport"
  },
  "relations": {},
  "createdAt": "2024-05-19T16:19:15.232Z",
  "createdBy": "KZ5zDPudPshQMShUb4cLopBEE1fNSJGE",
  "updatedAt": "2024-05-19T16:19:15.232Z",
  "updatedBy": "KZ5zDPudPshQMShUb4cLopBEE1fNSJGE"
}
```

Label entity in Port

```
{
  "identifier": "36f84d2c-7b7d-4a71-96f2-6ea4140004d5",
  "title": "New-sample-label",
  "icon": "Linear",
  "blueprint": "linearLabel",
  "team": [],
  "properties": {
      "isGroup": false
  },
  "relations": {
      "childLabels": [],
      "parentLabel": null
  },
  "createdAt": "2024-05-19T16:19:17.747Z",
  "createdBy": "KZ5zDPudPshQMShUb4cLopBEE1fNSJGE",
  "updatedAt": "2024-05-19T16:19:17.747Z",
  "updatedBy": "KZ5zDPudPshQMShUb4cLopBEE1fNSJGE"
}
```

Issue entity in Port

```
{
  "identifier": "POR-2",
  "title": "sub issue with new title",
  "icon": "Linear",
  "blueprint": "linearIssue",
  "team": [],
  "properties": {
      "status": "Todo",
      "url": "https://linear.app/getport/issue/POR-2/sub-issue-with-new-title",
      "created": "2024-05-16T21:52:00.299Z",
      "priority": "Medium",
      "assignee": "dudi@getport.io",
      "updated": "2024-05-17T09:27:40.077Z",
      "creator": "mor@getport.io"
  },
  "relations": {
      "team": "POR",
      "labels": [
          "402b218c-938c-4ddf-85db-0019bc632316"
      ],
      "parentIssue": "POR-1"
  },
  "createdAt": "2024-05-19T16:19:21.143Z",
  "createdBy": "KZ5zDPudPshQMShUb4cLopBEE1fNSJGE",
  "updatedAt": "2024-05-19T16:19:21.143Z",
  "updatedBy": "KZ5zDPudPshQMShUb4cLopBEE1fNSJGE"
}
```

## Alternative installation via webhook[â](#alternative-installation-via-webhook "Direct link to Alternative installation via webhook")

While the Ocean integration described above is the recommended installation method, you may prefer to use a webhook to ingest data from Linear. If so, use the following instructions:

**Note** that when using the webhook installation method, data will be ingested into Port only when the webhook is triggered.

**Webhook installation (click to expand)**

In this example you are going to create a webhook integration between [Linear](https://linear.app/) and Port, which will ingest Linear issue entities.

## Port configuration

Create the following blueprint definition:

Linear issue blueprint

Create in Port

```
{
    "identifier": "linearIssue",
    "title": "Linear Issue",
    "icon": "Linear",
    "schema": {
      "properties": {
        "url": {
          "title": "Issue URL",
          "type": "string",
          "format": "url",
          "description": "URL to the issue in Linear"
        },
        "status": {
          "title": "Status",
          "type": "string",
          "description": "The status of the issue"
        },
        "assignee": {
          "title": "Assignee",
          "type": "string",
          "format": "user",
          "description": "The user assigned to the issue"
        },
        "creator": {
          "title": "Creator",
          "type": "string",
          "description": "The user that created to the issue",
          "format": "user"
        },
        "priority": {
          "title": "Priority",
          "type": "string",
          "description": "The priority of the issue"
        },
        "created": {
          "title": "Created At",
          "type": "string",
          "description": "The created datetime of the issue",
          "format": "date-time"
        },
        "updated": {
          "title": "Updated At",
          "type": "string",
          "description": "The updated datetime of the issue",
          "format": "date-time"
        }
      }
    },
    "calculationProperties": {},
    "relations": {}
  }
```

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints)

Linear issue webhook configuration

1. **Basic details** tab - fill the following details:

   1. Title : `Linear mapper`;
   2. Identifier : `linear_mapper`;
   3. Description : `A webhook configuration to map Linear issues to Port`;
   4. Icon : `Linear`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "linearIssue",
       "entity": {
         "identifier": ".body.data.identifier",
         "title": ".body.data.title",
         "properties": {
           "url": ".body.data.url",
           "status": ".body.data.state.name",
           "assignee": ".body.data.assignee.email",
           "creator": ".body.data.creator.email",
           "priority": ".body.data.priorityLabel",
           "created": ".body.data.createdAt",
           "updated": ".body.data.updatedAt"
         }
       }
     }
   ]
   ```

3. Click **Save** at the bottom of the page.

## Create a webhook in Linear

You can follow the instruction in [Linear's docs](https://developers.linear.app/docs/graphql/webhooks#configuring-with-the-settings-ui), they are also outlined here for reference:

1. Log in to Linear as a user with admin permissions.

2. Click the workspace label at the top left corner.

3. Choose **Workspace Settings**.

4. At the bottom of the sidebar on the left, under **My Account**, choose **API**.

5. Click on **Create new webhook**.

6. Input the following details:

   <!-- -->

   1. `Label` - use a meaningful name such as Port Webhook.
   2. `URL` - enter the value of the `url` key you received after creating the webhook configuration.
   3. Under `Data change events` - mark issues.

7. Click **Create webhook** at the bottom of the page.

Linear events and payload

In order to view the different payloads and events available in Linear webhooks, [look here](https://developers.linear.app/docs/graphql/webhooks#the-webhook-payload)

Done! any change you make to an issue (open, close, edit, etc.) will trigger a webhook event that Linear will send to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Let's Test It

This section includes a sample webhook event sent from Linear when an issue is created or updated. In addition, it includes the entity created from the event based on the webhook configuration provided in the previous section.

### Payload

Here is an example of the payload structure sent to the webhook URL when a Linear issue is created:

Webhook event payload

```
{
  "action": "create",
  "actor": {
    "id": "11c5ce7d-229b-4487-b23b-f404e4a8c85d",
    "name": "Mor Paz",
    "type": "user"
  },
  "createdAt": "2024-05-19T17:55:29.277Z",
  "data": {
    "id": "d62a755d-5389-4dbd-98bb-3db03f239d9d",
    "createdAt": "2024-05-19T17:55:29.277Z",
    "updatedAt": "2024-05-19T17:55:29.277Z",
    "number": 5,
    "title": "New issue again",
    "priority": 0,
    "boardOrder": 0,
    "sortOrder": -3975,
    "labelIds": [],
    "teamId": "92d25fa4-fb1c-449f-b314-47f82e8f280d",
    "previousIdentifiers": [],
    "creatorId": "11c5ce7d-229b-4487-b23b-f404e4a8c85d",
    "stateId": "f12cad17-9b8f-470d-b20a-5e17da8e46b9",
    "priorityLabel": "No priority",
    "botActor": null,
    "identifier": "POR-5",
    "url": "https://linear.app/getport/issue/POR-5/new-issue-again",
    "state": {
      "id": "f12cad17-9b8f-470d-b20a-5e17da8e46b9",
      "color": "#e2e2e2",
      "name": "Todo",
      "type": "unstarted"
    },
    "team": {
      "id": "92d25fa4-fb1c-449f-b314-47f82e8f280d",
      "key": "POR",
      "name": "Port"
    },
    "subscriberIds": [
      "11c5ce7d-229b-4487-b23b-f404e4a8c85d"
    ],
    "labels": []
  },
  "url": "https://linear.app/getport/issue/POR-5/new-issue-again",
  "type": "Issue",
  "organizationId": "36968e1b-496c-4610-8c25-641364da172e",
  "webhookTimestamp": 1716141329394,
  "webhookId": "ee1fa20e-6b57-4448-86f7-39d9672ddedd"
}
```

### Mapping Result

The combination of the sample payload and the webhook configuration generates the following Port entity:

```
{
  "identifier": "POR-5",
  "title": "New issue again",
  "team": [],
  "properties": {
    "status": "Todo",
    "url": "https://linear.app/getport/issue/POR-5/new-issue-again",
    "created": "2024-05-19T17:55:29.277Z",
    "priority": "No priority",
    "updated": "2024-05-19T17:55:29.277Z"
  },
  "relations": {
    "labels": []
  },
  "icon": "Linear"
}
```
