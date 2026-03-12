# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-cost/kubecost.md

# Kubecost

Loading version...

Port's Kubecost integration allows you to model Kubecost resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Kubecost resources and their metadata in Port (see supported resources below).
* Watch for Kubecost object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Kubecost into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`kubesystem`](https://docs.kubecost.com/apis/monitoring-apis/api-allocation#allocation-api)
* [`cloud`](https://docs.kubecost.com/apis/monitoring-apis/cloud-cost-api#cloud-cost-querying-api)

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

Using this installation option means that the integration will be able to update Port in real time using webhooks.

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

For details about the available parameters for the installation, see the table below.

* Helm
* ArgoCD

<!-- -->

1. Go to the [Kubecost<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Kubecost) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Kubecost<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Kubecost<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Kubecost<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Kubecost
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

1. Create a `values.yaml` file in `argocd/my-ocean-kubecost-integration` in your git repository with the content:

note

Remember to replace the placeholders for `KUBECOST_HOST`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-kubecost-integration
  type: kubecost
  eventListener:
    type: POLLING
  config:
    kubecostHost: KUBECOST_HOST
```

<br />

2. Install the `my-ocean-kubecost-integration` ArgoCD Application by creating the following `my-ocean-kubecost-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-kubecost-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-kubecost-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-kubecost-integration/values.yaml
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
kubectl apply -f my-ocean-kubecost-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                               | Description                                                                                                                         | Required |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                         | Your port client id                                                                                                                 | â       |
| `port.clientSecret`                     | Your port client secret                                                                                                             | â       |
| `port.baseUrl`                          | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                   | â       |
| `integration.identifier`                | Change the identifier to describe your integration                                                                                  | â       |
| `integration.type`                      | The integration type                                                                                                                | â       |
| `integration.eventListener.type`        | The event listener type                                                                                                             | â       |
| `integration.config.kubecostHost`       | The Kubecost server URL                                                                                                             | â       |
| `integration.config.kubecostApiVersion` | The API version of the Kubecost instance. Possible values are v1 and v2. The default value is v2                                    | â       |
| `scheduledResyncInterval`               | The number of minutes between each resync                                                                                           | â       |
| `initializePortResources`               | Default true, When set to true the integration will create default blueprints and the port App config Mapping                       | â       |
| `sendRawDataExamples`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

This workflow/pipeline will run the Kubecost integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST`        | The Kubecost server                                                                                                                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_API_VERSION` | The API version of the Kubecost instance. Possible values are v1 and v2. The default value is v2                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

<br />

Here is an example for `kubecost-integration.yml` workflow file:

```
name: Kubecost Exporter Workflow

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
          type: 'kubecost'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            kubecost_host: ${{ secrets.OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST`        | The Kubecost server                                                                                                                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_API_VERSION` | The API version of the Kubecost instance. Possible values are v1 and v2. The default value is v2                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Kubecost Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST', variable: 'OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="kubecost"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST=$OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST \
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

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST`        | The Kubecost server                                                                                                                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_API_VERSION` | The API version of the Kubecost instance. Possible values are v1 and v2. The default value is v2                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

<br />

Here is an example for `kubecost-integration.yml` pipeline file:

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
    integration_type="kubecost"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST=$(OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST`        | The Kubecost server                                                                                                                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__KUBECOST_API_VERSION` | The API version of the Kubecost instance. Possible values are v1 and v2. The default value is v2                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

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
  INTEGRATION_TYPE: kubecost
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
        -e OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST=$OCEAN__INTEGRATION__CONFIG__KUBECOST_HOST \
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

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
- kind: kubesystem
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        blueprint: '"kubecostResourceAllocation"'
        identifier: .name
        title: .name
        properties:
          cluster: .properties.cluster
          namespace: .properties.namespace
          startDate: .start
          endDate: .end
          cpuCoreHours: .cpuCoreHours
          cpuCost: .cpuCost
          cpuEfficiency: .cpuEfficiency
          gpuHours: .gpuHours
          gpuCost: .gpuCost
          networkCost: .networkCost
          loadBalancerCost: .loadBalancerCost
          pvCost: .pvCost
          pvBytes: .pvBytes
          ramBytes: .ramBytes
          ramCost: .ramCost
          ramEfficiency: .ramEfficiency
          sharedCost: .sharedCost
          externalCost: .externalCost
          totalCost: .totalCost
          totalEfficiency: .totalEfficiency
- kind: cloud
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        blueprint: '"kubecostCloudAllocation"'
        identifier: .properties.provider + "/" + .properties.providerID + "/" + .properties.category + "/" + .properties.service | gsub("[^A-Za-z0-9@_.:\\\\/=-]"; "-")
        title: .properties.provider + "/" + .properties.service
        properties:
          provider: .properties.provider
          accountID: .properties.accountID
          invoiceEntityID: .properties.invoiceEntityID
          startDate: .window.start
          endDate: .window.end
          listCost: .listCost.cost
          listCostPercent: .listCost.kubernetesPercent
          netCost: .netCost.cost
          netCostPercent: .netCost.kubernetesPercent
          amortizedNetCost: .amortizedNetCost.cost
          amortizedNetCostPercent: .amortizedNetCost.kubernetesPercent
          invoicedCost: .invoicedCost.cost
          invoicedCostPercent: .invoicedCost.kubernetesPercent
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Cost allocation[â](#cost-allocation "Direct link to Cost allocation")

Cost allocation blueprint

Create in Port

```
{
  "identifier": "kubecostResourceAllocation",
  "description": "This blueprint represents an Kubecost resource allocation in our software catalog",
  "title": "Kubecost Resource Allocation",
  "icon": "Cluster",
  "schema": {
    "properties": {
      "cluster": {
        "type": "string",
        "title": "Cluster"
      },
      "namespace": {
        "type": "string",
        "title": "Namespace"
      },
      "startDate": {
        "title": "Start Date",
        "type": "string",
        "format": "date-time"
      },
      "endDate": {
        "title": "End Date",
        "type": "string",
        "format": "date-time"
      },
      "cpuCoreHours": {
        "title": "CPU Core Hours",
        "type": "number"
      },
      "cpuCost": {
        "title": "CPU Cost",
        "type": "number"
      },
      "cpuEfficiency": {
        "title": "CPU Efficiency",
        "type": "number"
      },
      "gpuHours": {
        "title": "GPU Hours",
        "type": "number"
      },
      "gpuCost": {
        "title": "GPU Cost",
        "type": "number"
      },
      "networkCost": {
        "title": "Network Cost",
        "type": "number"
      },
      "loadBalancerCost": {
        "title": "Load Balancer Cost",
        "type": "number"
      },
      "pvCost": {
        "title": "PV Cost",
        "type": "number"
      },
      "pvBytes": {
        "title": "PV Bytes",
        "type": "number"
      },
      "ramBytes": {
        "title": "RAM Bytes",
        "type": "number"
      },
      "ramCost": {
        "title": "RAM Cost",
        "type": "number"
      },
      "ramEfficiency": {
        "title": "RAM Efficiency",
        "type": "number"
      },
      "sharedCost": {
        "title": "Shared Cost",
        "type": "number"
      },
      "externalCost": {
        "title": "External Cost",
        "type": "number"
      },
      "totalCost": {
        "title": "Total Cost",
        "type": "number"
      },
      "totalEfficiency": {
        "title": "Total Efficiency",
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
  - kind: kubesystem
    selector:
      query: "true"
    port:
      entity:
        mappings:
          blueprint: '"kubecostResourceAllocation"'
          identifier: .name
          title: .name
          properties:
            cluster: .properties.cluster
            namespace: .properties.namespace
            startDate: .start
            endDate: .end
            cpuCoreHours: .cpuCoreHours
            cpuCost: .cpuCost
            cpuEfficiency: .cpuEfficiency
            gpuHours: .gpuHours
            gpuCost: .gpuCost
            networkCost: .networkCost
            loadBalancerCost: .loadBalancerCost
            pvCost: .pvCost
            pvBytes: .pvBytes
            ramBytes: .ramBytes
            ramCost: .ramCost
            ramEfficiency: .ramEfficiency
            sharedCost: .sharedCost
            externalCost: .externalCost
            totalCost: .totalCost
            totalEfficiency: .totalEfficiency
```

### Cloud cost[â](#cloud-cost "Direct link to Cloud cost")

Cloud cost blueprint

Create in Port

```
{
  "identifier": "kubecostCloudAllocation",
  "description": "This blueprint represents an Kubecost cloud resource allocation in our software catalog",
  "title": "Kubecost Cloud Allocation",
  "icon": "Cluster",
  "schema": {
    "properties": {
      "provider": {
        "type": "string",
        "title": "Provider"
      },
      "accountID": {
        "type": "string",
        "title": "Account ID"
      },
      "invoiceEntityID": {
        "type": "string",
        "title": "Invoice Entity ID"
      },
      "startDate": {
        "title": "Start Date",
        "type": "string",
        "format": "date-time"
      },
      "endDate": {
        "title": "End Date",
        "type": "string",
        "format": "date-time"
      },
      "listCost": {
        "title": "List Cost Value",
        "type": "number"
      },
      "listCostPercent": {
        "title": "List Cost Percent",
        "type": "number"
      },
      "netCost": {
        "title": "Net Cost Value",
        "type": "number"
      },
      "netCostPercent": {
        "title": "Net Cost Percent",
        "type": "number"
      },
      "amortizedNetCost": {
        "title": "Amortized Net Cost",
        "type": "number"
      },
      "amortizedNetCostPercent": {
        "title": "Amortized Net Cost Percent",
        "type": "number"
      },
      "invoicedCost": {
        "title": "Invoice Cost",
        "type": "number"
      },
      "invoicedCostPercent": {
        "title": "Invoice Cost Percent",
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
  - kind: cloud
    selector:
      query: "true"
    port:
      entity:
        mappings:
          blueprint: '"kubecostCloudAllocation"'
          identifier: .properties.provider + "/" + .properties.providerID + "/" + .properties.category + "/" + .properties.service | gsub("[^A-Za-z0-9@_.:\\\\/=-]"; "-")
          title: .properties.provider + "/" + .properties.service
          properties:
            provider: .properties.provider
            accountID: .properties.accountID
            invoiceEntityID: .properties.invoiceEntityID
            startDate: .window.start
            endDate: .window.end
            listCost: .listCost.cost
            listCostPercent: .listCost.kubernetesPercent
            netCost: .netCost.cost
            netCostPercent: .netCost.kubernetesPercent
            amortizedNetCost: .amortizedNetCost.cost
            amortizedNetCostPercent: .amortizedNetCost.kubernetesPercent
            invoicedCost: .invoicedCost.cost
            invoicedCostPercent: .invoicedCost.kubernetesPercent
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Kubecost. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Kubecost:

Cost response data

```
{
  "name": "argocd",
  "properties": {
    "cluster": "cluster-one",
    "node": "gke-my-regional-cluster-default-pool-e8093bfa-0bjg",
    "namespace": "argocd",
    "providerID": "gke-my-regional-cluster-default-pool-e8093bfa-0bjg",
    "namespaceLabels": {
      "kubernetes_io_metadata_name": "argocd"
    }
  },
  "window": {
    "start": "2023-10-30T00:00:00Z",
    "end": "2023-10-30T01:00:00Z"
  },
  "start": "2023-10-30T00:00:00Z",
  "end": "2023-10-30T01:00:00Z",
  "minutes": 60,
  "cpuCores": 0.00515,
  "cpuCoreRequestAverage": 0,
  "cpuCoreUsageAverage": 0.00514,
  "cpuCoreHours": 0.00515,
  "cpuCost": 0.00012,
  "cpuCostAdjustment": 0,
  "cpuEfficiency": 1,
  "gpuCount": 0,
  "gpuHours": 0,
  "gpuCost": 0,
  "gpuCostAdjustment": 0,
  "networkTransferBytes": 2100541.53,
  "networkReceiveBytes": 2077024.88318,
  "networkCost": 0,
  "networkCrossZoneCost": 0,
  "networkCrossRegionCost": 0,
  "networkInternetCost": 0,
  "networkCostAdjustment": 0,
  "loadBalancerCost": 0.02708,
  "loadBalancerCostAdjustment": 0,
  "pvBytes": 0,
  "pvByteHours": 0,
  "pvCost": 0,
  "pvs": "None",
  "pvCostAdjustment": 0,
  "ramBytes": 135396181.33333,
  "ramByteRequestAverage": 0,
  "ramByteUsageAverage": 135394433.70477,
  "ramByteHours": 135396181.33333,
  "ramCost": 0.00041,
  "ramCostAdjustment": 0,
  "ramEfficiency": 1,
  "externalCost": 0,
  "sharedCost": 0,
  "totalCost": 0.02761,
  "totalEfficiency": 1,
  "proportionalAssetResourceCosts": {},
  "lbAllocations": {
    "cluster-one/argocd/argocd-server": {
      "service": "argocd/argocd-server",
      "cost": 0.027083333333333334,
      "private": false,
      "ip": ""
    }
  },
  "sharedCostBreakdown": {}
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Cost entity in Port

```
{
  "identifier": "argocd",
  "title": "argocd",
  "icon": "Cluster",
  "blueprint": "kubecostResourceAllocation",
  "team": [],
  "properties": {
    "cluster": "cluster-one",
    "namespace": "argocd",
    "startDate": "2023-10-30T04:00:00.000Z",
    "endDate": "2023-10-30T05:00:00.000Z",
    "cpuCoreHours": 0.0051,
    "cpuCost": 0.00012,
    "cpuEfficiency": 1,
    "gpuHours": 0,
    "gpuCost": 0,
    "networkCost": 0,
    "loadBalancerCost": 0.02708,
    "pvCost": 0,
    "pvBytes": 0,
    "ramBytes": 135396181.33333,
    "ramCost": 0.00041,
    "ramEfficiency": 1,
    "sharedCost": 0,
    "externalCost": 0,
    "totalCost": 0.02761,
    "totalEfficiency": 1
  },
  "relations": {},
  "createdAt": "2023-10-30T13:25:42.717Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2023-10-30T13:28:37.379Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

## Advanced[â](#advanced "Direct link to Advanced")

For advanced configuration including customizing how Kubecost kinds are ingested, read the [advanced section of Kubecost](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/kubecost/advanced.md) guide.
