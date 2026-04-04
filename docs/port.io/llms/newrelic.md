# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/newrelic.md

# New Relic

Loading version...

Port's New Relic integration allows you to model New Relic resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired New Relic resources and their metadata in Port (see supported resources below).
* Watch for New Relic object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from New Relic into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

The following kinds are supported by the New Relic integration:

* [**`newRelicService`**](https://docs.newrelic.com/docs/new-relic-solutions/new-relic-one/core-concepts/what-entity-new-relic/) - Maps New Relic services and applications (SERVICE and APPLICATION entity types).
* [**`newRelicAlert`**](https://docs.newrelic.com/docs/alerts-applied-intelligence/new-relic-alerts/get-started/alerts-ai-overview-page/#issues) - Maps New Relic issues/alerts.
* [**`newRelicServiceLevel`**](https://docs.newrelic.com/docs/service-level-management/consume-slm/) - Maps New Relic service level indicators (SLIs) and service level objectives (SLOs).
* [**`entity`**](https://docs.newrelic.com/docs/new-relic-solutions/new-relic-one/core-concepts/what-entity-new-relic/) - Maps generic New Relic entities, including cloud resources from AWS, Azure, and GCP.
* [**`entities`**](https://docs.newrelic.com/docs/new-relic-solutions/new-relic-one/core-concepts/what-entity-new-relic/) - Maps New Relic dashboards.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [NewRelic<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=NewRelic) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

  **Supported live event triggers (click to expand)**

  **Issues:**

  * issue\_created
  * issue\_updated
  * issue\_closed

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

1. Go to the [NewRelic<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=NewRelic) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->NewRelic<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->NewRelic<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->NewRelic<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  NewRelic
  <!-- -->
  can reach.

If `liveEvents.baseUrl` is not provided, the integration will continue to function correctly. In such a configuration, to retrieve the latest information from the target system, the [`scheduledResyncInterval`](https://ocean.port.io/developing-an-integration/trigger-your-integration) parameter has to be set, or a manual resync will need to be triggered through Port's UI.

Debugging local integrations

To test webhooks or live event delivery to your local environment, expose your local pod or service to the internet using ngrok (e.g. `ngrok http http://localhost:8000`)

### Securing Your Webhooks

The `integration.secrets.webhookUsername,integration.secrets.webhookSecret` parameters secure your webhooks. If not provided, the integration will process webhooks without validating the source of the events.

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

1. Create a `values.yaml` file in `argocd/my-ocean-newrelic-integration` in your git repository with the content:

note

Remember to replace the placeholders for `NEW_RELIC_API_KEY` and `NEW_RELIC_ACCOUNT_ID`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-newrelic-integration
  type: newrelic
  eventListener:
    type: POLLING
  secrets:
    newRelicAPIKey: NEW_RELIC_API_KEY
    newRelicAccountID: NEW_RELIC_ACCOUNT_ID
```

<br />

note

If you are using New Relic's EU region, add the highlighted code (GraphQL configuration value) to the `values.yaml`:

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-newrelic-integration
  type: newrelic
  eventListener:
    type: POLLING
  config:
    newRelicGraphqlURL: https://api.eu.newrelic.com/graphql
  secrets:
    newRelicAPIKey: NEW_RELIC_API_KEY
    newRelicAccountID: NEW_RELIC_ACCOUNT_ID
```

2. Install the `my-ocean-newrelic-integration` ArgoCD Application by creating the following `my-ocean-newrelic-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-newrelic-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-newrelic-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-newrelic-integration/values.yaml
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
kubectl apply -f my-ocean-newrelic-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                               | Description                                                                                                                                        | Required |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                         | Your port client id                                                                                                                                | â       |
| `port.clientSecret`                     | Your port client secret                                                                                                                            | â       |
| `port.baseUrl`                          | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                  | â       |
| `integration.identifier`                | Change the identifier to describe your integration                                                                                                 | â       |
| `integration.type`                      | The integration type                                                                                                                               | â       |
| `integration.eventListener.type`        | The event listener type                                                                                                                            | â       |
| `integration.secrets.newRelicAPIKey`    | The New Relic API key                                                                                                                              | â       |
| `integration.secrets.newRelicAccountID` | The New Relic account ID                                                                                                                           | â       |
| `scheduledResyncInterval`               | The number of minutes between each resync                                                                                                          | â       |
| `initializePortResources`               | Default true, When set to true the integration will create default blueprints and the port App config Mapping                                      | â       |
| `integration.secrets.webhookUsername`   | Webhook username used for authenticating incoming events. [Learn more](http://docs.newrelic.com/docs/alerts/get-notified/intro-notifications/)     | â       |
| `integration.secrets.webhookSecret`     | Webhook secret for authenticating incoming events. [Learn more](http://docs.newrelic.com/docs/alerts/get-notified/intro-notifications/)            | â       |
| `liveEvents.baseUrl`                    | The base url of the instance where the New Relic integration is hosted, used for real-time updates. (e.g.`https://mynewrelicoceanintegration.com`) | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

<!-- -->

## Recommended resource sizes

To ensure optimal performance and avoid out-of-memory (OOM) errors, we recommend the following resources for this integration:

* **CPU Limit**: `800m`
* **CPU Request**: `100m`
* **Memory Limit**: `1Gi`
* **Memory Request**: `1Gi`

### Set resource values

```
helm install my-integration port-labs/port-ocean \
# ... other parameters
--set ocean.resources.limits.cpu=800m \
--set ocean.resources.limits.memory=1Gi \
--set ocean.resources.requests.cpu=100m \
--set ocean.resources.requests.memory=1Gi
```

### Event listener

The integration uses polling to pull the configuration from Port every minute and check it for changes. If there is a change, a resync will occur.

This workflow/pipeline will run the New Relic integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                          | Description                                                                                                        | Required |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY`    | The New Relic API key                                                                                              | â       |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID` | The New Relic account ID                                                                                           | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |

<br />

Here is an example for `newrelic-integration.yml` workflow file:

note

If you are using New Relic's EU region, add the following flag to the docker command:

`-e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_URL=https://api.eu.newrelic.com/graphql`

```
name: New Relic Exporter Workflow

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
          type: 'newrelic'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            new_relic_api_key: ${{ secrets.OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY }} 
            new_relic_account_id: ${{ secrets.OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                          | Description                                                                                                        | Required |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY`    | The New Relic API key                                                                                              | â       |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID` | The New Relic account ID                                                                                           | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

note

If you are using New Relic's EU region, add the following flag to the docker command:

`-e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_URL=https://api.eu.newrelic.com/graphql`

```
pipeline {
    agent any

    stages {
        stage('Run New Relic Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY', variable: 'OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID', variable: 'OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="newrelic"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY=$OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY \
                                -e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID=$OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID \
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

| Parameter                                          | Description                                                                                                        | Required |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY`    | The New Relic API key                                                                                              | â       |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID` | The New Relic account ID                                                                                           | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |

<br />

Here is an example for `newrelic-integration.yml` pipeline file:

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
    integration_type="newrelic"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY=$(OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY) \
        -e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID=$(OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                          | Description                                                                                                        | Required |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY`    | The New Relic API key                                                                                              | â       |
| `OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID` | The New Relic account ID                                                                                           | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |

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
  INTEGRATION_TYPE: newrelic
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
        -e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY=$OCEAN__INTEGRATION__CONFIG__NEW_RELIC_API_KEY \
        -e OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID=$OCEAN__INTEGRATION__CONFIG__NEW_RELIC_ACCOUNT_ID \
        -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
        -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
```

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
- kind: newRelicService
  selector:
    query: 'true'
    newRelicTypes:
    - SERVICE
    - APPLICATION
    calculateOpenIssueCount: true
    entityQueryFilter: type in ('SERVICE','APPLICATION')
    entityExtraPropertiesQuery: |-
      ... on ApmApplicationEntityOutline {
        guid
        name
        apmSummary {
          apdexScore
          errorRate
          hostCount
          instanceCount
          responseTimeAverage
          throughput
        }
      }
  port:
    entity:
      mappings:
        identifier: .guid
        title: .name
        blueprint: '"newRelicService"'
        properties:
          has_apm: if .domain | contains("APM") then "true" else "false" end
          link: .permalink
          open_issues_count: .open_issues_count
          reporting: .reporting
          tags: .tags
          type: .type
          throughput: .apmSummary.throughput
          error_rate: .apmSummary.errorRate
          response_time_avg: .apmSummary.responseTimeAverage
          instance_count: .apmSummary.instanceCount
          apdex: .apmSummary.apdexScore
- kind: newRelicAlert
  selector:
    query: .state == "ACTIVATED" or .state == "CREATED"
    newRelicTypes:
    - ISSUE
  port:
    entity:
      mappings:
        identifier: .issueId
        title: .title[0]
        blueprint: '"newRelicAlert"'
        properties:
          priority: .priority
          state: .state
          sources: .sources
          conditionName: .conditionName
          alertPolicyNames: .policyName
          activatedAt: if .activatedAt == null then null else .activatedAt / 1000 | todate end
          link: '"https://one.newrelic.com/launcher/nrai.launcher?pane=" + ("{\"isPhoton\": true, \"id\": \"\(.issueId)\", \"nerdletId\": \"nrai.issue-redirect\"}" | @base64)'
          description: .description
        relations:
          alert_to_workload: .__APPLICATION.entity_guids + .__SERVICE.entity_guids
          cloud_resource:
            combinator: '"and"'
            rules:
            - property: '"guid"'
              operator: '"in"'
              value: .entityGuids
- kind: newRelicServiceLevel
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .serviceLevel.indicators[0].id
        title: .serviceLevel.indicators[0].name
        blueprint: '"newRelicServiceLevel"'
        properties:
          description: .serviceLevel.indicators[0].description
          targetThreshold: .serviceLevel.indicators[0].objectives[0].target
          createdAt: if .serviceLevel.indicators[0].createdAt != null then (.serviceLevel.indicators[0].createdAt | tonumber / 1000 | todate) else null end
          updatedAt: .serviceLevel.indicators[0].updatedAt
          createdBy: .serviceLevel.indicators[0].createdBy.email
          sli: .__SLI.SLI
          tags: .tags
          slo_compliance: .__SLI.SLI >= .serviceLevel.indicators[0].objectives[0].target
        relations:
          workload: .tags."nr.associatedEntityGuid"[0]
- kind: entity
  selector:
    query: 'true'
    entityQueryFilter: >-
      type IN ( 'AWSEC2INSTANCE', 'AWSS3BUCKET', 'AWSRDSDBINSTANCE', 'AWSLAMBDAFUNCTION', 'AWSELBLOADBALANCER', 'AZUREVIRTUALMACHINE', 'AZURESQLDATABASE', 'GCPCOMPUTEINSTANCE', 'GCPSTORAGEBUCKET', 'GCPSQLDATABASEINSTANCE' )
  port:
    entity:
      mappings:
        identifier: .guid
        title: .name
        blueprint: '"newRelicCloudResource"'
        properties:
          infrastructureIntegrationType: .type
          reporting: .reporting
          link: .permalink
          tags: .tags
- kind: entities
  selector:
    query: 'true'
    entityQueryFilter: type IN ( 'DASHBOARD' )
  port:
    entity:
      mappings:
        identifier: .guid
        title: .name
        blueprint: '"newRelicDashboards"'
        properties:
          dashboard_link: .permalink
- kind: newRelicService
  selector:
    query: 'true'
    newRelicTypes:
    - SERVICE
    - APPLICATION
    entityQueryFilter: type in ('SERVICE','APPLICATION')
  port:
    entity:
      mappings:
        identifier: .guid
        title: .name
        blueprint: '"workload"'
        relations:
          new_relic_workload: .guid
```

### Additional Configuration[â](#additional-configuration "Direct link to Additional Configuration")

* **newRelicTypes** - An array of Newrelic entity types that will be fetched. The default value is \['SERVICE', 'APPLICATION']. This is related to the type field in the Newrelic entity.

* **calculateOpenIssueCount:**

  * A boolean value that indicates if the integration should calculate the number of open issues for each entity. The default value is \`false\`\`.
  * **NOTE** - This can cause a performance degradation as the integration will have to calculate the number of open issues for each entity, which unfortunately is not supported by the New Relic API.

* **entityQueryFilter:**

  * A filter that will be applied to the New Relic API query. This will be placed inside the `query` field of the `entitySearch` query in the New Relic GraphQL API. For examples of query filters [click here](https://docs.newrelic.com/docs/apis/nerdgraph/examples/nerdgraph-entities-api-tutorial/#search-query).
  * Not specifying this field will cause the integration to fetch all the entities and map them to the blueprint defined in the `kind`.
  * Rule of thumb - Most of the time the `EntityQueryFilter` will be the same as the `NewRelicTypes`. For example, if we want to fetch all the services and applications we will set the `EntityQueryFilter` to `type in ('SERVICE','APPLICATION')` and the `NewRelicTypes` to `['SERVICE', 'APPLICATION']`.

* **entityExtraPropertiesQuery:**

  * An optional property that allows defining extra properties to fetch for each Newrelic entity. This will be concatenated with the default query properties we are requesting under the `entities` section in the `entitySearch` query in the Newrelic GraphQL API. For examples of additional query properties [click here](https://docs.newrelic.com/docs/apis/nerdgraph/examples/nerdgraph-entities-api-tutorial/#apm-summary).

* The `port`, `entity` and the `mappings` keys are used to map the Newrelic object fields to Port entities. To create multiple mappings of the same kind, you can add another item in the `resources` array;

## Capabilities[â](#capabilities "Direct link to Capabilities")

### Tags[â](#tags "Direct link to Tags")

Some Newrelic `entities` have a property named `tags` which contains potentially useful information such as machine information, hostname, agent name & version, and more. For example:

```
"tags": [
  {
    "key": "coreCount",
    "values": [
      "10"
    ]
  },
  {
    "key": "hostStatus",
    "values": [
      "running"
    ]
  },
]
```

Before mapping, this integration performs a transformation on each `tag`, after which the example above would look like this:

```
tags = ["coreCount":"10","hostStatus":"running"]
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Service (Entity)[â](#service-entity "Direct link to Service (Entity)")

Service blueprint

Create in Port

```
{
  "identifier": "newRelicService",
  "description": "This blueprint represents a New Relic service or application in our software catalog",
  "title": "New Relic Service",
  "icon": "NewRelic",
  "schema": {
    "properties": {
      "has_apm": {
        "title": "Has APM",
        "type": "boolean"
      },
      "open_issues_count": {
        "title": "Open Issues Count",
        "type": "number",
        "default": 0
      },
      "link": {
        "title": "Link",
        "type": "string",
        "format": "url"
      },
      "reporting": {
        "title": "Reporting",
        "type": "boolean"
      },
      "tags": {
        "title": "Tags",
        "type": "object"
      },
      "account_id": {
        "title": "Account ID",
        "type": "string"
      },
      "type": {
        "title": "Type",
        "type": "string"
      },
      "domain": {
        "title": "Domain",
        "type": "string"
      },
      "throughput": {
        "title": "Throughput",
        "type": "number"
      },
      "response_time_avg": {
        "title": "Response Time AVG",
        "type": "number"
      },
      "error_rate": {
        "title": "Error Rate",
        "type": "number"
      },
      "instance_count": {
        "title": "Instance Count",
        "type": "number"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: newRelicService
    selector:
      query: "true"
      newRelicTypes: ["SERVICE", "APPLICATION"]
      calculateOpenIssueCount: true
      entityQueryFilter: "type in ('SERVICE','APPLICATION')"
      entityExtraPropertiesQuery: |
        ... on ApmApplicationEntity {
          guid
          name
          alertSeverity
          applicationId
          apmBrowserSummary {
            ajaxRequestThroughput
            ajaxResponseTimeAverage
            jsErrorRate
            pageLoadThroughput
            pageLoadTimeAverage
          }
          apmSummary {
            apdexScore
            errorRate
            hostCount
            instanceCount
            nonWebResponseTimeAverage
            nonWebThroughput
            responseTimeAverage
            throughput
            webResponseTimeAverage
            webThroughput
          }
        }
    port:
      entity:
        mappings:
          blueprint: '"newRelicService"'
          identifier: .guid
          title: .name
          properties:
            has_apm: 'if .domain | contains("APM") then "true" else "false" end'
            link: .permalink
            open_issues_count: .__open_issues_count
            reporting: .reporting
            tags: .tags
            domain: .domain
            type: .type
```

### Issue[â](#issue "Direct link to Issue")

Issue blueprint

Create in Port

```
{
  "identifier": "newRelicAlert",
  "description": "This blueprint represents a New Relic alert in our software catalog",
  "title": "New Relic Alert",
  "icon": "NewRelic",
  "schema": {
    "properties": {
      "priority": {
        "type": "string",
        "title": "Priority",
        "enum": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
        "enumColors": {
          "CRITICAL": "red",
          "HIGH": "red",
          "MEDIUM": "yellow",
          "LOW": "green"
        }
      },
      "state": {
        "type": "string",
        "title": "State",
        "enum": ["ACTIVATED", "CLOSED", "CREATED"],
        "enumColors": {
          "ACTIVATED": "yellow",
          "CLOSED": "green",
          "CREATED": "lightGray"
        }
      },
      "trigger": {
        "type": "string",
        "title": "Trigger"
      },
      "sources": {
        "type": "array",
        "title": "Sources"
      },
      "alertPolicyNames": {
        "type": "array",
        "title": "Alert Policy Names"
      },
      "conditionName": {
        "type": "array",
        "title": "Condition Name"
      },
      "activatedAt": {
        "type": "string",
        "title": "Time Issue was activated"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "newRelicService": {
      "title": "New Relic Service",
      "target": "newRelicService",
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
  - kind: newRelicAlert
    selector:
      query: "true"
      newRelicTypes: ["ISSUE"]
    port:
      entity:
        mappings:
          blueprint: '"newRelicAlert"'
          identifier: .issueId
          title: .title[0]
          properties:
            priority: .priority
            state: .state
            sources: .sources
            conditionName: .conditionName
            alertPolicyNames: .policyName
            activatedAt: .activatedAt
          relations:
            newRelicService: .__APPLICATION.entity_guids + .__SERVICE.entity_guids
```

### Service Level[â](#service-level "Direct link to Service Level")

Service Level blueprint

Create in Port

```
{
    "identifier": "newRelicServiceLevel",
    "description": "This blueprint represents a New Relic Service Level",
    "title": "New Relic Service Level",
    "icon": "NewRelic",
    "schema": {
      "properties": {
        "description": {
          "title": "Description",
          "type": "string"
        },
        "targetThreshold": {
          "icon": "DefaultProperty",
          "title": "Target Threshold",
          "type": "number"
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
        },
        "createdBy": {
          "title": "Creator",
          "type": "string",
          "format": "user"
        },
        "sli": {
          "type": "number",
          "title": "SLI"
        },
        "tags": {
          "type": "object",
          "title": "Tags"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "newRelicService": {
        "title": "New Relic service",
        "target": "newRelicService",
        "required": false,
        "many": false
      }
    }
  }
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: newRelicServiceLevel
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"newRelicServiceLevel"'
          identifier: .serviceLevel.indicators[0].id
          title: .serviceLevel.indicators[0].name
          properties:
            description: .serviceLevel.indicators[0].description
            targetThreshold: .serviceLevel.indicators[0].objectives[0].target
            createdAt: if .serviceLevel.indicators[0].createdAt != null then (.serviceLevel.indicators[0].createdAt | tonumber / 1000 | todate) else null end
            updatedAt: .serviceLevel.indicators[0].updatedAt
            createdBy: .serviceLevel.indicators[0].createdBy.email
            sli: .__SLI.SLI
            tags: .tags
          relations:
            newRelicService: .serviceLevel.indicators[0].guid
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from New Relic. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from New Relic:

**Service (Entity) response data (Click to expand)**

```
{
  "accountId": 4444532,
  "alertSeverity": "NOT_CONFIGURED",
  "domain": "INFRA",
  "entityType": "INFRASTRUCTURE_HOST_ENTITY",
  "guid": "MTIzNDU2Nzg5fElORlJBfE5BfDY1MjQwNDc0NjE4MzUyMDkwOTU=",
  "lastReportingChangeAt": 1715351571254,
  "name": "UserMacbook",
  "permalink": "https://one.eu.newrelic.com/redirect/entity/MTIzNDU2Nzg5fElORlJBfE5BfDY1MjQwNDc0NjE4MzUyMDkwOTU=",
  "reporting": true,
  "tags": [
    {
      "key": "account",
      "values": [
        "Account 4444831"
      ]
    },
    {
      "key": "accountId",
      "values": [
        "4444831"
      ]
    },
    {
      "key": "agentName",
      "values": [
        "Infrastructure"
      ]
    },
    {
      "key": "agentVersion",
      "values": [
        "1.50.0"
      ]
    },
    {
      "key": "coreCount",
      "values": [
        "8"
      ]
    },
    {
      "key": "fullHostname",
      "values": [
        "usermacbook"
      ]
    },
    {
      "key": "hostStatus",
      "values": [
        "running"
      ]
    },
    {
      "key": "hostname",
      "values": [
        "Usermacbook"
      ]
    },
    {
      "key": "instanceType",
      "values": [
        "MacBook Air MacBookAir10,1"
      ]
    },
    {
      "key": "kernelVersion",
      "values": [
        "23.2.0"
      ]
    },
    {
      "key": "linuxDistribution",
      "values": [
        "macOS 14.2.1"
      ]
    },
    {
      "key": "operatingSystem",
      "values": [
        "macOS"
      ]
    },
    {
      "key": "processorCount",
      "values": [
        "8"
      ]
    },
    {
      "key": "systemMemoryBytes",
      "values": [
        "17179869184"
      ]
    },
    {
      "key": "trustedAccountId",
      "values": [
        "4444532"
      ]
    }
  ],
  "type": "HOST"
}
```

**Issue response data (Click to expand)**

```
{
  "issueId": "MjQwNzIwN3xBUE18QVBQTElDQVRJT058MjIwMzEwNzV8MTA0NzYwNzA5",
  "title": "My Issue",
  "priority": "CRITICAL",
  "state": "ACTIVATED",
  "sources": ["My Source"],
  "conditionName": ["My Condition"],
  "policyName": ["My Policy"],
  "activatedAt": "2022-01-01T00:00:00Z"
}
```

**Service Level response data (Click to expand)**

```
{
  "serviceLevel": {
    "indicators": [
      {
        "createdAt": 1721030560937,
        "createdBy": {
          "email": "user@domain.com"
        },
        "description": "Proportion of requests that are served faster than a threshold.",
        "guid": "NDM2OTY4MHxFWFR8U0VSVklDRV9MRVZFTHw1OTk0MzQ",
        "id": "599434",
        "name": "Service Level Name - Metric",
        "objectives": [
          {
            "description": null,
            "name": null,
            "target": 95,
            "timeWindow": {
              "rolling": {
                "count": 7,
                "unit": "DAY"
              }
            }
          }
        ],
        "resultQueries": {
          "indicator": {
            "nrql": "SELECT clamp_max(sum(newrelic.sli.good) / sum(newrelic.sli.valid) * 100, 100) AS 'SLI' FROM Metric WHERE entity.guid = 'NDM2OTY4MHxFWFR8U0VSVklDRV9MRVZFTHw1OTk0MzQ' UNTIL 2 minutes AGO"
          }
        },
        "updatedAt": null,
        "updatedBy": null
      }
    ]
  },
  "tags": {
    "account": [
      "Account [REDACTED]"
    ],
    "accountId": [
      "[REDACTED]"
    ],
    "category": [
      "latency"
    ],
    "nr.associatedEntityGuid": [
      "NDM2OTY4MHxBUE18QVBQTElDQVRJT058NTkxMTYyMjE0"
    ],
    "nr.associatedEntityName": [
      "Service Name 01"
    ],
    "nr.associatedEntityType": [
      "APM_APPLICATION"
    ],
    "nr.sliComplianceCategory": [
      "Non-compliant"
    ],
    "nr.sloPeriod": [
      "7d"
    ],
    "nr.sloTarget": [
      "95.0%"
    ],
    "trustedAccountId": [
      "[REDACTED]"
    ]
  },
  "__SLI": {
    "SLI": 87.56
  }
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

**Service (Entity) entity in Port (Click to expand)**

```
{
  "identifier": "MTIzNDU2Nzg5fElORlJBfE5BfDY1MjQwNDc0NjE4MzUyMDkwOTU=",
  "title": "UserMacbook",
  "blueprint": "newRelicAlert",
  "team": [],
  "icon": "NewRelic",
  "properties": {
    "has_apm": false,
    "link": "https://one.eu.newrelic.com/redirect/entity/MTIzNDU2Nzg5fElORlJBfE5BfDY1MjQwNDc0NjE4MzUyMDkwOTU=",
    "open_issues_count": null,
    "reporting": true,
    "tags": [
      {
        "key": "account",
        "values": [
          "Account 4444831"
        ]
      },
      {
        "key": "accountId",
        "values": [
          "4444831"
        ]
      },
      {
        "key": "agentName",
        "values": [
          "Infrastructure"
        ]
      },
      {
        "key": "agentVersion",
        "values": [
          "1.50.0"
        ]
      },
      {
        "key": "coreCount",
        "values": [
          "8"
        ]
      },
      {
        "key": "fullHostname",
        "values": [
          "usermacbook"
        ]
      },
      {
        "key": "hostStatus",
        "values": [
          "running"
        ]
      },
      {
        "key": "hostname",
        "values": [
          "Usermacbook"
        ]
      },
      {
        "key": "instanceType",
        "values": [
          "MacBook Air MacBookAir10,1"
        ]
      },
      {
        "key": "kernelVersion",
        "values": [
          "23.2.0"
        ]
      },
      {
        "key": "linuxDistribution",
        "values": [
          "macOS 14.2.1"
        ]
      },
      {
        "key": "operatingSystem",
        "values": [
          "macOS"
        ]
      },
      {
        "key": "processorCount",
        "values": [
          "8"
        ]
      },
      {
        "key": "systemMemoryBytes",
        "values": [
          "17179869184"
        ]
      },
      {
        "key": "trustedAccountId",
        "values": [
          "4444532"
        ]
      }
    ],
    "domain": "INFRA",
    "type": "HOST"
  },
  "relations": {},
  "createdAt": "2024-2-6T09:30:57.924Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2024-2-6T11:49:20.881Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

**Issue entity in Port (Click to expand)**

```
{
  "identifier": "My Issue",
  "title": "My Issue",
  "blueprint": "newRelicAlert",
  "team": [],
  "icon": "NewRelic",
  "properties": {
    "priority": "CRITICAL",
    "state": "ACTIVATED",
    "sources": ["My Source"],
    "conditionName": ["My Condition"],
    "alertPolicyNames": ["My Policy"],
    "activatedAt": "2022-01-01T00:00:00Z"
  },
  "relations": {
    "newRelicService": "My Service"
  },
  "createdAt": "2024-2-6T09:30:57.924Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2024-2-6T11:49:20.881Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

**Service Level entity in Port (Click to expand)**

```
{
    "blueprint": "newRelicServiceLevel",
    "identifier": "599434",
    "title": "Service Level Name - Metric",
    "icon": "NewRelic",
    "properties": {
      "description": "Proportion of requests that are served faster than a threshold.",
      "targetThreshold": 95,
      "createdAt": "2024-07-15T08:02:40Z",
      "updatedAt": null,
      "createdBy": "user@domain.com",
      "serviceLevelIndicator": 87.56,
      "tags": {
        "account": [
          "Account [REDACTED]"
        ],
        "accountId": [
          "[REDACTED]"
        ],
        "category": [
          "latency"
        ],
        "nr.associatedEntityGuid": [
          "NDM2OTY4MHxBUE18QVBQTElDQVRJT058NTkxMTYyMjE0"
        ],
        "nr.associatedEntityName": [
          "Service Name 01"
        ],
        "nr.associatedEntityType": [
          "APM_APPLICATION"
        ],
        "nr.sliComplianceCategory": [
          "Non-compliant"
        ],
        "nr.sloPeriod": [
          "7d"
        ],
        "nr.sloTarget": [
          "95.0%"
        ],
        "trustedAccountId": [
          "[REDACTED]"
        ]
      }
    },
    "relations": {
      "newRelicService": "NDM2OTY4MHxFWFR8U0VSVklDRV9MRVZFTHw1OTk0MzQ"
    },
  "createdAt": "2024-08-06T09:30:57.924Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2024-08-06T09:49:20.881Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
  }
```
