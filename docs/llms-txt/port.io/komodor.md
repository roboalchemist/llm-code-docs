# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/komodor.md

# Komodor

Port's Komodor integration allows you to model [Komodor](https://komodor.com/) resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to map, organize, and sync your desired Komodor resources and their metadata in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Komodor into Port are listed below:

* [`Services`](https://api.komodor.com/api/docs/index.html#/Services/post_api_v2_services_search)
* [`Health Monitoring`](https://help.komodor.com/hc/en-us/categories/22390793120274-Health-Management)

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

#### Generate a Komodor Api Key[â](#generate-a-komodor-api-key "Direct link to Generate a Komodor Api Key")

1. Log in to the [Komodor platfrom](https://app.komodor.com).

2. Access API Keys management page:

   <!-- -->

   * Click on your user profile in the top-right corner of the platform.
   * Select `API Keys` from the dropdown menu.

3. Generate a new API key:

   <!-- -->

   * Click the `Generate Key` button.
   * Provide a descriptive name for the API key to help you identify its purpose later (e.g., "Port.io api key").

4. Copy the token and save it in a secure location.

To read more, see the [Komodor documentation](https://help.komodor.com/hc/en-us/articles/22434108566674-Using-the-Komodor-API).

API key permissions

Make sure the user who creates the API key has view permissions (ideally full access) for the resources you wish to ingest into Port, since the API key inherits the user's permissions.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=undefined) in your portal.

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

Using this installation method means that the integration will be able to update Port in real time.

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

For details about the available parameters for the installation, see the table below.

* Helm
* ArgoCD

<!-- -->

1. Go to the [Komodor<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Komodor) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Komodor<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Komodor<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Komodor<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Komodor
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

1. Create a `values.yaml` file in `argocd/my-ocean-komodor-integration` in your git repository with the content:

note

Remember to replace the placeholders for `KOMODOR_TOKEN`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-komodor-integration
  type: komodor
  eventListener:
    type: POLLING
  secrets:
  komodorApiKey: KOMODOR_API_KEY
```

<br />

2. Install the `my-ocean-komodor-integration` ArgoCD Application by creating the following `my-ocean-komodor-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-komodor-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-komodor-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-komodor-integration/values.yaml
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
kubectl apply -f my-ocean-komodor-integration.yaml
```

This table summarizes the available parameters for the installation. Note the parameters specific to this integration, they are last in the table.

| Parameter                           | Description                                                                                                   | Required |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                     | Your port client id                                                                                           | â       |
| `port.clientSecret`                 | Your port client secret                                                                                       | â       |
| `port.baseUrl`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                             | â       |
| `integration.identifier`            | Change the identifier to describe your integration                                                            | â       |
| `integration.type`                  | The integration type                                                                                          | â       |
| `integration.eventListener.type`    | The event listener type                                                                                       | â       |
| `scheduledResyncInterval`           | The number of minutes between each resync                                                                     | â       |
| `initializePortResources`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping | â       |
| `integration.secrets.komodorApiKey` | The Komodor API key [token](https://help.komodor.com/hc/en-us/articles/22434108566674-Using-the-Komodor-API). | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

### Event listener

The integration uses polling to pull the configuration from Port every minute and check it for changes. If there is a change, a resync will occur.

This workflow/pipeline will run the Komodor integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                     | Description                                                                                                        | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__KOMODOR_API_KEY` | The Komodor API [token](https://help.komodor.com/hc/en-us/articles/22434108566674-Using-the-Komodor-API).          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

<br />

Here is an example for `komodor-integration.yml` workflow file:

```
name: Komodor Exporter Workflow

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
          type: 'komodor'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            komodor_token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                     | Description                                                                                                        | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__KOMODOR_API_KEY` | The Komodor API [token](https://help.komodor.com/hc/en-us/articles/22434108566674-Using-the-Komodor-API).          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Komodor Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="komodor"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN=$OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN \
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

| Parameter                                     | Description                                                                                                        | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__KOMODOR_API_KEY` | The Komodor API [token](https://help.komodor.com/hc/en-us/articles/22434108566674-Using-the-Komodor-API).          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

<br />

Here is an example for `komodor-integration.yml` pipeline file:

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
    integration_type="komodor"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
       -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
      -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
      -e OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN=$(OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN) \
      -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
      -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
      -e OCEAN__PORT__BASE_URL='https://api.port.io' \
      $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                     | Description                                                                                                        | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__KOMODOR_API_KEY` | The Komodor API [token](https://help.komodor.com/hc/en-us/articles/22434108566674-Using-the-Komodor-API).          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

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
  INTEGRATION_TYPE: komodor
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
        -e OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN=$OCEAN__INTEGRATION__CONFIG__KOMODOR_TOKEN \
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

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from Komodor's API into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration you get after installing the Komodor integration.

**Default mapping configuration (Click to expand)**

```

deleteDependentEntities: true
createMissingRelatedEntities: false
enableMergeEntity: true
resources:
- kind: komodorService
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .kind + "-" + .cluster + "-" + .namespace + "-" + .service
        title: .service
        blueprint: '"komodorService"'
        properties:
          service_id: .uid
          status: .status
          cluster_name: .cluster
          workload_kind: .kind
          namespace_name: .namespace
          service_name: .service
          komodor_link: .link + "&utmSource=port"
          labels: .labels
          last_deploy_at: .lastDeploy.endTime | todate
          last_deploy_status: .lastDeploy.status
- kind: komodorHealthMonitoring
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .komodorUid | gsub("\\|"; "-") | sub("-+$"; "")
        blueprint: '"komodorHealthMonitoring"'
        properties:
          status: .status
          resource_identifier: .komodorUid | gsub("\\|"; "-") | sub("-+$"; "")
          severity: .severity
          supporting_data: .supportingData
          komodor_link: .link + "&utmSource=port"
          created_at: .createdAt | todate
          last_evaluated_at: .lastEvaluatedAt | todate
          check_type: .checkType
          workload_type: .komodorUid | split("|") | .[0]
          cluster_name: .komodorUid | split("|") | .[1]
          namespace_name: .komodorUid | split("|") | .[2]
          workload_name: .komodorUid | split("|") | .[3]
- kind: komodorHealthMonitoring
  selector:
    query: ( .komodorUid | split("|") as $parts | (length == 4 and all($parts[]; length > 0)) )
  port:
    entity:
      mappings:
        identifier: .id
        title: .komodorUid | gsub("\\|"; "-") | sub("-+$"; "")
        blueprint: '"komodorHealthMonitoring"'
        properties: {}
        relations:
          service: .komodorUid | gsub("\\|"; "-")
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Services[â](#services "Direct link to Services")

Service Blueprint

Create in Port

```
{
 "identifier": "komodorService",
 "title": "Komodor Service",
 "icon": "Komodor",
 "schema": {
   "properties": {
     "status": {
       "type": "string",
       "title": "Status",
       "enum": [
         "healthy",
         "unhealthy"
       ],
       "enumColors": {
         "healthy": "green",
         "unhealthy": "red"
       }
     },
     "cluster_name": {
       "icon": "Cluster",
       "type": "string",
       "title": "Cluster"
     },
     "workload_kind": {
       "icon": "Deployment",
       "type": "string",
       "title": "Kind"
     },
     "service_name": {
       "icon": "DefaultProperty",
       "type": "string",
       "title": "Service"
     },
     "namespace_name": {
       "icon": "Environment",
       "type": "string",
       "title": "Namespace"
     },
     "last_deploy_at": {
       "type": "string",
       "title": "Last Deploy At",
       "format": "date-time"
     },
     "komodor_link": {
       "type": "string",
       "title": "Komodor Link",
       "format": "url",
       "icon": "LinkOut"
     },
     "labels": {
       "icon": "JsonEditor",
       "type": "object",
       "title": "Labels"
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

Integration configuration

```
deleteDependentEntities: true
createMissingRelatedEntities: false
enableMergeEntity: true
resources:
  - kind: komodorService
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .uid
          title: .service
          blueprint: '"komodorService"'
          properties:
            service_id: .uid
            status: .status
            cluster_name: .cluster
            workload_kind: .kind
            namespace_name: .namespace
            service_name: .service
            komodor_link: .link + "&utmSource=port"
            labels: .labels
            last_deploy_at: .lastDeploy.endTime | todate
            last_deploy_status: .lastDeploy.status
```

### Health Monitors[â](#health-monitors "Direct link to Health Monitors")

Health Monitor blueprint

Create in Port

```
{
  "identifier": "komodorHealthMonitoring",
  "title": "Komodor Health Monitoring",
  "icon": "Komodor",
  "schema": {
    "properties": {
      "supporting_data": {
        "icon": "JsonEditor",
        "type": "object",
        "title": "Supporting Data"
      },
      "komodor_link": {
        "icon": "LinkOut",
        "type": "string",
        "title": "Komodor Link",
        "format": "url"
      },
      "severity": {
        "type": "string",
        "title": "Severity",
        "enum": [
          "high",
          "medium",
          "low"
        ],
        "enumColors": {
          "high": "red",
          "medium": "orange",
          "low": "yellow"
        }
      },
      "created_at": {
        "type": "string",
        "title": "Created at",
        "format": "date-time"
      },
      "last_evaluated_at": {
        "icon": "Clock",
        "type": "string",
        "title": "Last Evaluated At",
        "format": "date-time"
      },
      "check_type": {
        "type": "string",
        "title": "Check Type"
      },
      "status": {
        "type": "string",
        "title": "Status",
        "enum": [
          "open",
          "confirmed",
          "resolved",
          "dismissed",
          "ignored",
          "manually_resolved"
        ],
        "enumColors": {
          "open": "red",
          "confirmed": "turquoise",
          "resolved": "green",
          "dismissed": "purple",
          "ignored": "darkGray",
          "manually_resolved": "bronze"
        }
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "service": {
      "title": "Service",
      "target": "komodorService",
      "required": false,
      "many": false
    }
  }
}
```

Integration configuration

```
deleteDependentEntities: true
createMissingRelatedEntities: false
enableMergeEntity: true
resources:
  - kind: komodorHealthMonitoring
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .komodorUid | gsub("\\|"; "-") | sub("-+$"; "")
          blueprint: '"komodorHealthMonitoring"'
          properties:
            status: .status
            resource_identifier: .komodorUid | gsub("\\|"; "-") | sub("-+$"; "")
            severity: .severity
            supporting_data: .supportingData
            komodor_link: .link + "&utmSource=port"
            created_at: .createdAt | todate
            last_evaluated_at: .lastEvaluatedAt | todate
            check_type: .checkType
            workload_type: .komodorUid | split("|") | .[0]
            cluster_name: .komodorUid | split("|") | .[1]
            namespace_name: .komodorUid | split("|") | .[2]
            workload_name: .komodorUid | split("|") | .[3]
  - kind: komodorHealthMonitoring
    selector:
      query: (.komodorUid | split("|") | length) == 4
    port:
      entity:
        mappings:
          identifier: .id
          title: .komodorUid | gsub("\\|"; "-") | sub("-+$"; "")
          blueprint: '"komodorHealthMonitoring"'
          properties: {}
          relations:
            service: .komodorUid | gsub("\\|"; "-")
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Komodor. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Komodor. All variables are written in uppercase letters for improved readability:

Service response data

```
{
  "data": {
    "services": [
      {
        "annotations": {
          "checksum/config": "CHECKSUM",
          "deployment.kubernetes.io/revision": "1",
          "meta.helm.sh/release-name": "komodor-agent",
          "meta.helm.sh/release-namespace": "komodor"
        },
        "cluster": "test",
        "kind": "Deployment",
        "labels": {
          "app.kubernetes.io/instance": "komodor-agent",
          "app.kubernetes.io/managed-by": "Helm",
          "app.kubernetes.io/name": "komodor-agent",
          "app.kubernetes.io/version": "X.X.X",
          "helm.sh/chart": "komodor-agent-X.X.X"
        },
        "lastDeploy": {
          "endTime": 1740140297,
          "startTime": 1740140297,
          "status": "success"
        },
        "link": "https://app.komodor.com/services/ACCOUNT.CLUSTER.SERVICE?workspaceId=null&referer=public-api",
        "namespace": "komodor",
        "service": "komodor-agent",
        "status": "healthy",
        "uid": "INTERNAL_KOMODOR_UID"
      }
    ]
  },
  "meta": {
    "nextPage": 1,
    "page": 0,
    "pageSize": 1
  }
}
```

Health Monitor response data

```
{
  "checkType": "restartingContainers",
  "createdAt": 1742447493,
  "id": "RANDOM_UID",
  "komodorUid": "WORKLOAD_KIND|CLUSTER_NAME|NAMESPACE_NAME|WORKLOAD_NAME",
  "lastEvaluatedAt": 1743292800,
  "link": "https://app.komodor.com/health/risks/drawer?checkCategory=workload-health&checkType=restartingContainers&violationId=78f44264-dbe1-4d0f-9096-9925f5e74ae8",
  "severity": "medium",
  "status": "open",
  "supportingData": {
    "restartingContainers": {
      "containers": [
        {
          "name": "CONTAINER_NAME",
          "restarts": 969
        }
      ],
      "restartReasons": {
        "breakdown": [
          {
            "message": "Container Exited With Error - Exit Code: 1",
            "percent": 100,
            "numOccurences": 1825,
            "reason": "ProcessExit"
          }
        ],
        "additionalInfo": {
          "podSamples": [
            {
              "podName": "POD_NAME_1",
              "restarts": 607
            },
            {
              "podName": "POD_NAME_2",
              "restarts": 170
            },
            {
              "podName": "POD_NAME_3",
              "restarts": 57
            },
            {
              "podName": "POD_NAME_4",
              "restarts": 53
            },
            {
              "podName": "POD_NAME_5",
              "restarts": 22
            }
          ],
          "numRestartsOnTimeseries": 909,
          "numRestartsOnDB": 1825
        }
      }
    }
  }
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entities:

Service entity in Port

```
{
  "identifier": "SERVICE_ID",
  "title": "komodor-agent",
  "blueprint": "komodorService",
  "properties": {
    "serviceId": "KOMODOR_INTERNAL_ID",
    "status": "healthy",
    "cluster_name": "test",
    "workload_kind": "Deployment",
    "namespace_name": "komodor",
    "service_name": "komodor-agent",
    "link_to_komodor": "https://app.komodor.com/services/ACCOUNT_NAME.CLUSTER.SERVICE?workspaceId=null&referer=public-api",
    "labels": {
      "app.kubernetes.io/instance": "komodor-agent",
      "app.kubernetes.io/managed-by": "Helm",
      "app.kubernetes.io/name": "komodor-agent",
      "app.kubernetes.io/version": "X.X.X",
      "helm.sh/chart": "komodor-agent-X.X.X"
    },
    "last_deploy_at": "2025-01-22T08:26:42Z",
    "last_deploy_status": "success"
  }
}
```

Health Monitor entity in Port

```
{
  "identifier": "random-uuid",
  "title": "KIND|CLUSTER|NAMESPACE|NAME",
  "blueprint": "komodorHealthMonitoring",
  "properties": {
    "status": "open",
    "resource_identifier": "KIND-CLUSTER-NAMESPACE-NAME",
    "severity": "medium",
    "supporting_data": {
      "restartingContainers": {
        "containers": [
          {
            "name": "container-name",
            "restarts": 969
          }
        ],
        "restartReasons": {
          "breakdown": [
            {
              "message": "Container Exited With Error - Exit Code: 1",
              "percent": 100,
              "numOccurences": 1825,
              "reason": "ProcessExit"
            }
          ],
          "additionalInfo": {
            "podSamples": [
              {
                "podName": "POD_NAME_1",
                "restarts": 607
              },
              {
                "podName": "POD_NAME_2",
                "restarts": 170
              },
              {
                "podName": "POD_NAME_3",
                "restarts": 57
              },
              {
                "podName": "POD_NAME_4",
                "restarts": 53
              },
              {
                "podName": "POD_NAME_5",
                "restarts": 22
              }
            ],
            "numRestartsOnTimeseries": 909,
            "numRestartsOnDB": 1825
          }
        }
      }
    },
    "komodor_link": "https://app.komodor.com/health/risks/drawer?checkCategory=workload-health&checkType=restartingContainers&violationId=UID&utmSource=port",
    "created_at": "2025-03-20T05:11:33Z",
    "last_evaluated_at": "2025-03-30T00:00:00Z",
    "check_type": "restartingContainers",
    "workload_type": "WORKLOAD_KIND",
    "cluster_name": "CLUSTER_NAME",
    "namespace_name": "NAMESPACE_NAME",
    "workload_name": "NAME"
  },
  "relations": {
    "service": [
      "ServiceUID"
    ]
  }
}
```

## Connect Komodor services to k8s workloads[â](#connect-komodor-services-to-k8s-workloads "Direct link to Connect Komodor services to k8s workloads")

### Prerequisites[â](#prerequisites-1 "Direct link to Prerequisites")

* Install Komodor integration.
* Install Port's k8s exporter integration on your cluster.
* Install Komodor agent on your cluster.

### Create the relation[â](#create-the-relation "Direct link to Create the relation")

1. Navigate to the [data model](https://app.getport.io/settings/data-model) page of your portal.

2. Click on the Komodor Service blueprint.

3. Click on the `...` button in the top right corner, choose `Edit blueprint`, then click on the `Edit JSON` button.

4. Update the existing JSON by incorporating the following data in it.

   **Mapping configuration (Click to expand)**

   ```
   {
     "relations": {
       "workload": {
         "title": "Workload",
         "target": "workload",
         "required": false,
         "many": false
       }
     }
   }
   ```

### Set up mapping configuration[â](#set-up-mapping-configuration "Direct link to Set up mapping configuration")

1. Navigate to the [data sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Click on the Komodor integration, and scroll to the mapping section in the bottom-left corner.

3. Copy the following configuration and paste it in the editor, then click `Save & Resync`.

   **Mapping configuration (Click to expand)**

   ```
     - kind: komodorService
       selector:
         query: 'true'
       port:
         entity:
           mappings:
             identifier: .kind + "-" + .cluster + "-" + .namespace + "-" + .service
             blueprint: '"komodorService"'
             properties: {}
             relations:
               workload: .service + "-" + .kind + "-" + .namespace + "-" + .cluster
   ```

Default values

This assumes that both your Komodor integration and Kubernetes exporter are using their default key and field values. If any mappings or blueprints have been modified in either integration, you may need to adjust these values accordingly.
