# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cicd/octopus-deploy.md

# Octopus Deploy Integration

Loading version...

Port's Octopus Deploy integration allows you to model Octopus Deploy resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Octopus Deploy resources and their metadata in Port (see supported resources below).
* Watch for Octopus Deploy object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

Some of the resources that can be ingested from Octopus Deploy into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Space`](https://octopus.com/docs/octopus-rest-api/examples/spaces)
* [`Project`](https://octopus.com/docs/octopus-rest-api/examples/projects)
* [`Release`](https://octopus.com/docs/octopus-rest-api/examples/releases)
* [`Deployment`](https://octopus.com/docs/octopus-rest-api/examples/deployments)

Ingesting Additional Resources

The integration supports additional resources, see the [ingest additional resources](/build-your-software-catalog/sync-data-to-catalog/cicd/octopus-deploy/mapping-extra-resources/.md) page for more information

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [Octopus<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Octopus) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

  **Supported live event triggers (click to expand)**

  * spaces
  * projects
  * deployments
  * releases
  * machines

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

1. Go to the [Octopus<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Octopus) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Octopus<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Octopus<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Octopus<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Octopus
  <!-- -->
  can reach.

If `liveEvents.baseUrl` is not provided, the integration will continue to function correctly. In such a configuration, to retrieve the latest information from the target system, the [`scheduledResyncInterval`](https://ocean.port.io/developing-an-integration/trigger-your-integration) parameter has to be set, or a manual resync will need to be triggered through Port's UI.

Debugging local integrations

To test webhooks or live event delivery to your local environment, expose your local pod or service to the internet using ngrok (e.g. `ngrok http http://localhost:8000`)

<!-- -->

### Securing Your Webhooks

The `integration.secrets.webhookSecret` parameter secures your webhooks. If not provided, the integration will process webhooks without validating the source of the events.

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

1. Create a `values.yaml` file in `argocd/my-octopus-integration` in your git repository with the content:

note

Remember to replace the placeholders for `OCTOPUS_HOST`, `APP_HOST` and `OCTOPUS_API_KEY`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-octopus-integration
  type: octopus
  eventListener:
    type: POLLING
  config:
    serverUrl: OCTOPUS_HOST
    appHost: APP_HOST
  secrets:
    octopusApiKey: OCTOPUS_API_KEY
```

<br />

2. Install the `my-octopus-integration` ArgoCD Application by creating the following `my-octopus-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-octopus-integration
  namespace: argocd
spec:
  destination:
    namespace: my-octopus-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-octopus-integration/values.yaml
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
kubectl apply -f my-octopus-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                                | Description                                                                                                                                           | Required |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                          | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))      | â       |
| `port.clientSecret`                      | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))  | â       |
| `port.baseUrl`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                     | â       |
| `integration.identifier`                 | Change the identifier to describe your integration                                                                                                    | â       |
| `integration.type`                       | The integration type                                                                                                                                  | â       |
| `integration.eventListener.type`         | The event listener type                                                                                                                               | â       |
| `integration.secrets.octopusApiKey`      | The Octopus API Key, docs can be found [here](https://octopus.com/docs/octopus-rest-api/how-to-create-an-api-key)                                     | â       |
| `integration.config.serverUrl`           | The Octopus host                                                                                                                                      | â       |
| `integration.config.appHost(deprecated)` | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Octopus                                 | â       |
| `scheduledResyncInterval`                | The number of minutes between each resync                                                                                                             | â       |
| `initializePortResources`                | Default true, When set to true the integration will create default blueprints and the port App config Mapping                                         | â       |
| `sendRawDataExamples`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                   | â       |
| `integration.secrets.webhookSecret`      | Webhook secret for authenticating incoming events. [Learn more](https://octopus.com/docs/administration/managing-infrastructure/subscriptions)        | â       |
| `liveEvents.baseUrl`                     | The base url of the instance where the Octopus integration is hosted, used for real-time updates. (e.g.`https://myoctopusdeployoceanintegration.com`) | â       |

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

This workflow/pipeline will run the Octopus integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                     | Description                                                                                                                                          | Required |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY` | The Octopus API Key                                                                                                                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__SERVER_URL`      | The Octopus Deploy Host                                                                                                                              | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

<br />

Here is an example for `octopus-integration.yml` workflow file:

```
name: Octopus Exporter Workflow

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
          type: 'octopus'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            octopus_api_key: ${{ secrets.OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY }}
            server_url: ${{ OCEAN__INTEGRATION__CONFIG__SERVER_URL }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                     | Description                                                                                                                                          | Required |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY` | The Octopus API Key                                                                                                                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__SERVER_URL`      | The Octopus Deploy Host                                                                                                                              | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Octopus Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY', variable: 'OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__SERVER_URL', variable: 'OCEAN__INTEGRATION__CONFIG__SERVER_URL'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="octopus"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY=$OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY \
                                -e OCEAN__INTEGRATION__CONFIG__SERVER_URL=$OCEAN__INTEGRATION__CONFIG__SERVER_URL \
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

| Parameter                                     | Description                                                                                                                                          | Required |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY` | The Octopus API Key                                                                                                                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__SERVER_URL`      | The Octopus Deploy Host                                                                                                                              | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

<br />

Here is an example for `octopus-integration.yml` pipeline file:

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
    integration_type="octopus"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY=$(OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY) \
        -e OCEAN__INTEGRATION__CONFIG__SERVER_URL=$(OCEAN__INTEGRATION__CONFIG__SERVER_URL) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                     | Description                                                                                                                                          | Required |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY` | The Octopus API Key                                                                                                                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__SERVER_URL`      | The Octopus Deploy Host                                                                                                                              | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                      | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

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
  INTEGRATION_TYPE: octopus
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
        -e OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY=$OCEAN__INTEGRATION__CONFIG__OCTOPUS_API_KEY \
        -e OCEAN__INTEGRATION__CONFIG__SERVER_URL=$OCEAN__INTEGRATION__CONFIG__SERVER_URL \
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
- kind: space
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .Id
        title: .Name
        blueprint: '"octopusSpace"'
        properties:
          url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .Id
          description: .Description
- kind: project
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .Id
        title: .Name
        blueprint: '"octopusProject"'
        properties:
          url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/projects/" + .Id
          description: .Description
          isDisabled: .IsDisabled
          tenantedDeploymentMode: .TenantedDeploymentMode
        relations:
          space: .SpaceId
- kind: release
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .Id
        title: .ProjectId + "(" + .Version + ")"
        blueprint: '"octopusRelease"'
        properties:
          version: .Version
          assembledDate: .Assembled
          channelId: .ChannelId
          releaseNotes: .ReleaseNotes
          url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/releases/" + .Id
        relations:
          project: .ProjectId
- kind: deployment
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .Id
        title: .Name
        blueprint: '"octopusDeployment"'
        properties:
          createdAt: .Created
          deployedBy: .DeployedBy
          taskId: .TaskId
          failureEncountered: .FailureEncountered
          comments: .Comments
          url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/deployments/" + .Id
        relations:
          release: .ReleaseId
          project: .ProjectId
- kind: machine
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .Id
        title: .Name
        blueprint: '"octopusMachine"'
        properties:
          roles: .Roles
          status: .HealthStatus
          url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/infrastructure/machines/" + .Id + "/settings"
          isDisabled: .IsDisabled
          operatingSystem: .OperatingSystem
          architecture: .Architecture
          statusSummary: .StatusSummary
          endpointType: .Endpoint.DeploymentTargetTypeId
          communicationStyle: .Endpoint.CommunicationStyle
        relations:
          space: .SpaceId
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Space[â](#space "Direct link to Space")

Space blueprint

Create in Port

```
{
  "identifier": "octopusSpace",
  "title": "Octopus Space",
  "icon": "Octopus",
  "description": "A space in Octopus Deploy",
  "schema": {
    "properties": {
      "url": {
        "type": "string",
        "title": "Space URL",
        "format": "url",
        "description": "The Link to the Space in Octopus Deploy"
      },
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The description of the space"
      }
    }
  },
  "calculationProperties": {},
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: space
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusSpace"'
          properties:
            url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .Id
            description: .Description
```

### Project[â](#project "Direct link to Project")

Project blueprint

```
{
  "identifier": "octopusProject",
  "title": "Octopus Project",
  "icon": "Octopus",
  "description": "An Octopus project",
  "schema": {
    "properties": {
      "slug": {
        "type": "string",
        "title": "Slug",
        "description": "The slug identifier of the project"
      },
      "url": {
        "type": "string",
        "title": "Project URL",
        "format": "url",
        "description": "The URL to access the project in Octopus Deploy"
      },
      "description": {
        "type": "string",
        "title": "Description",
        "description": "The project description"
      },
      "isDisabled": {
        "type": "boolean",
        "title": "Is Disabled",
        "description": "Indicates if the project is disabled"
      },
      "tenantedDeploymentMode": {
        "type": "string",
        "title": "Tenanted Deployment Mode",
        "description": "The deployment mode regarding tenants"
      }
    }
  },
  "calculationProperties": {},
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
    - kind: project
      selector:
      query: "true"
      port:
        entity:
          mappings:
            identifier: .Id
            title: .Name
            blueprint: '"octopusProject"'
            properties:
              url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/projects/" + .Id
              description: .Description
              isDisabled: .IsDisabled
              tenantedDeploymentMode: .TenantedDeploymentMode
```

### Release[â](#release "Direct link to Release")

Release blueprint

Create in Port

```
{
  "identifier": "octopusRelease",
  "title": "Octopus Release",
  "icon": "Octopus",
  "description": "A release in Octopus Deploy",
  "schema": {
    "properties": {
      "version": {
        "type": "string",
        "title": "Version",
        "description": "The version of the release"
      },
      "assembledDate": {
        "type": "string",
        "title": "Assembled Date",
        "format": "date-time",
        "description": "The datetime the release was assembled"
      },
      "channelId": {
        "type": "string",
        "title": "Channel ID",
        "description": "The ID of the channel associated with the release"
      },
      "releaseNotes": {
        "type": "string",
        "title": "Release Notes",
        "description": "Notes provided for the release"
      },
      "url": {
        "type": "string",
        "title": "Release URL",
        "format": "url",
        "description": "The URL to access the release in Octopus Deploy"
      }
    }
  },
  "calculationProperties": {},
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: release
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: ".ProjectId + \"(\" + .Version + \")\""
          blueprint: '"octopusRelease"'
          properties:
            version: .Version
            assembledDate: .Assembled
            channelId: .ChannelId
            releaseNotes: .ReleaseNotes
            url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/releases/" + .Id
```

### Deployment[â](#deployment "Direct link to Deployment")

Deployment blueprint

Create in Port

```
{
  "identifier": "octopusDeployment",
  "title": "Octopus Deployment",
  "icon": "Octopus",
  "description": "A deployment in Octopus Deploy",
  "schema": {
    "properties": {
      "createdAt": {
        "type": "string",
        "title": "Created At",
        "format": "date-time",
        "description": "The datetime when the deployment was created"
      },
      "deployedBy": {
        "type": "string",
        "title": "Deployed By",
        "description": "The user or system that performed the deployment"
      },
      "taskId": {
        "type": "string",
        "title": "Task ID",
        "description": "The ID of the task associated with the deployment"
      },
      "failureEncountered": {
        "type": "boolean",
        "title": "Failure Encountered",
        "description": "Indicates if any failure was encountered during the deployment"
      },
      "comments": {
        "type": "string",
        "title": "Comments",
        "description": "Comments regarding the deployment"
      },
      "url": {
        "type": "string",
        "title": "Deployment URL",
        "format": "url",
        "description": "The URL to access the deployment in Octopus Deploy"
      }
    }
  },
  "calculationProperties": {},
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: deployment
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusDeployment"'
          properties:
            createdAt: .Created
            deployedBy: .DeployedBy
            taskId: .TaskId
            failureEncountered: .FailureEncountered
            comments: .Comments
            url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/deployments/" + .Id
```

### Machine[â](#machine "Direct link to Machine")

Machine blueprint

Create in Port

```
{
  "identifier": "octopusMachine",
  "title": "Octopus Machine",
  "icon": "Octopus",
  "description": "A deployment target in Octopus Deploy",
  "schema": {
    "properties": {
      "roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "title": "Roles",
        "description": "Roles assigned to the target"
      },
      "status": {
        "type": "string",
        "title": "Status",
        "description": "The health status of the target"
      },
      "url": {
        "type": "string",
        "title": "Machine URL",
        "format": "url",
        "description": "The URL of the target"
      },
      "isDisabled": {
        "type": "boolean",
        "title": "Is Disabled",
        "description": "Indicates if the target is disabled"
      },
      "operatingSystem": {
        "type": "string",
        "title": "Operating System",
        "description": "The operating system of the target"
      },
      "architecture": {
        "type": "string",
        "title": "Architecture",
        "description": "The architecture of the target"
      },
      "statusSummary": {
        "type": "string",
        "title": "Status Summary",
        "description": "Summary of the target's status"
      },
      "endpointType": {
        "type": "string",
        "title": "Endpoint Type",
        "description": "The type of deployment target endpoint"
      },
      "communicationStyle": {
        "type": "string",
        "title": "Communication Style",
        "description": "The communication style of the target"
      }
    }
  },
  "calculationProperties": {},
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: machine
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .Id
          title: .Name
          blueprint: '"octopusMachine"'
          properties:
            roles: .Roles
            status: .HealthStatus
            url: env.OCEAN__INTEGRATION__CONFIG__SERVER_URL + "/app#/" + .SpaceId + "/infrastructure/machines/" + .Id + "/settings"
            isDisabled: .IsDisabled
            operatingSystem: .OperatingSystem
            architecture: .Architecture
            statusSummary: .StatusSummary
            endpointType: .Endpoint.DeploymentTargetTypeId
            communicationStyle: .Endpoint.CommunicationStyle
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Octopus. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Octopus:

Space response data

```
{
  "Id": "Spaces-1",
  "Name": "Default",
  "Slug": "default",
  "Description": "Description cannot be empty",
  "IsDefault": true,
  "IsPrivate": false,
  "TaskQueueStopped": false,
  "SpaceManagersTeams": [
    "teams-administrators",
    "teams-managers",
    "teams-spacemanagers-Spaces-1"
  ],
  "SpaceManagersTeamMembers": [],
  "Icon": null,
  "ExtensionSettings": [],
  "LastModifiedOn": "0001-01-01T00:00:00.000+00:00",
  "Links": {
    "Self": "/api/spaces/Spaces-1",
    "SpaceHome": "/api/Spaces-1",
    "Web": "/app#/spaces/Spaces-1",
    "Logo": "/api/spaces/Spaces-1/logo?cb=2024.3.10989",
    "Search": "/api/spaces/Spaces-1/search"
  }
}
```

Project response data

```
{
  "Id": "Projects-1",
  "SpaceId": "Spaces-1",
  "VariableSetId": "variableset-Projects-1",
  "DeploymentProcessId": "deploymentprocess-Projects-1",
  "ClonedFromProjectId": null,
  "DiscreteChannelRelease": false,
  "IncludedLibraryVariableSetIds": [],
  "DefaultToSkipIfAlreadyInstalled": false,
  "TenantedDeploymentMode": "Untenanted",
  "DefaultGuidedFailureMode": "EnvironmentDefault",
  "VersioningStrategy": {
    "Template": null,
    "DonorPackage": null
  },
  "ReleaseCreationStrategy": {
    "ChannelId": null,
    "ReleaseCreationPackage": null,
    "ReleaseCreationPackageStepId": null
  },
  "Templates": [],
  "AutoDeployReleaseOverrides": [],
  "ReleaseNotesTemplate": null,
  "DeploymentChangesTemplate": null,
  "ForcePackageDownload": false,
  "Icon": {
    "Id": "map-signs",
    "Color": "#5E2EA2"
  },
  "AllowIgnoreChannelRules": true,
  "ExecuteDeploymentsOnResilientPipeline": null,
  "ExtensionSettings": [],
  "Name": "Sample Project",
  "Slug": "sample-project",
  "Description": "Explore how to automate your deployments with Octopus Deploy.\n\nEdit the custom script step, tweak the variables, and run your first deployment. Experiment and make it your own!",
  "IsDisabled": false,
  "ProjectGroupId": "ProjectGroups-2",
  "LifecycleId": "Lifecycles-2",
  "AutoCreateRelease": false,
  "IsVersionControlled": false,
  "PersistenceSettings": {
    "Type": "Database"
  },
  "ProjectConnectivityPolicy": {
    "SkipMachineBehavior": "None",
    "TargetRoles": [],
    "AllowDeploymentsToNoTargets": false,
    "ExcludeUnhealthyTargets": false
  },
  "Links": {
    "Self": "/api/Spaces-1/projects/Projects-1",
    "Variables": "/api/Spaces-1/projects/Projects-1/variables",
    "Releases": "/api/Spaces-1/projects/Projects-1/releases{/version}{?skip,take,searchByVersion}",
    "Channels": "/api/Spaces-1/projects/Projects-1/channels{/id}{?skip,take,partialName}",
    "Triggers": "/api/Spaces-1/projects/Projects-1/triggers{?skip,take,partialName,triggerActionType,triggerActionCategory,runbooks}",
    "ScheduledTriggers": "/api/Spaces-1/projects/Projects-1/triggers/scheduled{?skip,take,partialName,ids}",
    "OrderChannels": "/api/Spaces-1/projects/Projects-1/channels/order",
    "Progression": "/api/Spaces-1/projects/Projects-1/progression{?releaseHistoryCount}",
    "RunbookTaskRunDashboardItemsTemplate": "/api/Spaces-1/progression/runbooks/taskRuns{?skip,take,ids,projectIds,runbookIds,environmentIds,tenantIds,taskIds}",
    "DeploymentProcess": "/api/Spaces-1/projects/Projects-1/deploymentprocesses",
    "DeploymentSettings": "/api/Spaces-1/projects/Projects-1/deploymentsettings",
    "Web": "/app#/Spaces-1/projects/Projects-1",
    "Logo": "/api/Spaces-1/projects/Projects-1/logo?cb=map-signs-%235E2EA2-2024.3.10989",
    "Metadata": "/api/Spaces-1/projects/Projects-1/metadata",
    "Runbooks": "/api/Spaces-1/projects/Projects-1/runbooks{?skip,take,partialName}",
    "RunbookSnapshots": "/api/Spaces-1/projects/Projects-1/runbookSnapshots{/name}{?skip,take,searchByName}",
    "Summary": "/api/Spaces-1/projects/Projects-1/summary",
    "GitConnectionTest": "/api/Spaces-1/projects/Projects-1/git/connectivity-test",
    "InsightsMetrics": "/api/Spaces-1/projects/Projects-1/insights/metrics{?channelId,environmentId,tenantId,tenantFilter,timeRange,granularity,timeZone}",
    "GitCompatibilityReport": "/api/Spaces-1/projects/Projects-1/git/compatibility-report",
    "ConvertToGit": "/api/Spaces-1/projects/Projects-1/git/convert",
    "ConvertToVcs": "/api/Spaces-1/projects/Projects-1/git/convert"
  }
}
```

Release response data

```
{
  "Id": "Releases-44",
  "SpaceId": "Spaces-1",
  "ProjectId": "Projects-41",
  "Version": "0.0.2",
  "ChannelId": "Channels-41",
  "ReleaseNotes": null,
  "ProjectDeploymentProcessSnapshotId": "deploymentprocess-Projects-41-s-1-QXLY2",
  "IgnoreChannelRules": false,
  "BuildInformation": [],
  "Assembled": "2024-08-21T16:17:46.750+00:00",
  "LibraryVariableSetSnapshotIds": [],
  "SelectedPackages": [],
  "SelectedGitResources": [],
  "ProjectVariableSetSnapshotId": "variableset-Projects-41-s-0-S6LJL",
  "VersionControlReference": null,
  "Links": {
    "Self": "/api/Spaces-1/releases/Releases-44",
    "Project": "/api/Spaces-1/projects/Projects-41",
    "Channel": "/api/Spaces-1/projects/Projects-41/channels/Channels-41",
    "Progression": "/api/Spaces-1/releases/Releases-44/progression",
    "Deployments": "/api/Spaces-1/releases/Releases-44/deployments{?skip,take}",
    "DeploymentTemplate": "/api/Spaces-1/releases/Releases-44/deployments/template",
    "Artifacts": "/api/Spaces-1/artifacts?regarding=Releases-44",
    "ProjectVariableSnapshot": "/api/Spaces-1/variables/variableset-Projects-41-s-0-S6LJL",
    "ProjectDeploymentProcessSnapshot": "/api/Spaces-1/deploymentprocesses/deploymentprocess-Projects-41-s-1-QXLY2",
    "Web": "/app#/Spaces-1/releases/Releases-44",
    "SnapshotVariables": "/api/Spaces-1/releases/Releases-44/snapshot-variables",
    "Defects": "/api/Spaces-1/releases/Releases-44/defects",
    "ReportDefect": "/api/Spaces-1/releases/Releases-44/defects",
    "ResolveDefect": "/api/Spaces-1/releases/Releases-44/defects/resolve",
    "DeploymentPreviews": "/api/Spaces-1/releases/Releases-44/deployments/previews/",
    "Variables": "/api/Spaces-1/projects/Projects-41/releases/Releases-44/variables"
  }
}
```

Deployment response data

```
{
  "Id": "Deployments-1",
  "SpaceId": "Spaces-1",
  "ReleaseId": "Releases-1",
  "ChannelId": "Channels-2",
  "DeploymentProcessId": "deploymentprocess-Projects-1-s-1-CGNSF",
  "Changes": [],
  "ChangesMarkdown": null,
  "EnvironmentId": "Environments-1",
  "TenantId": null,
  "ForcePackageDownload": false,
  "ForcePackageRedeployment": false,
  "Priority": "LifecycleDefault",
  "SkipActions": [],
  "SpecificMachineIds": [],
  "ExcludedMachineIds": [],
  "ManifestVariableSetId": null,
  "TaskId": "ServerTasks-11599",
  "ProjectId": "Projects-1",
  "UseGuidedFailure": false,
  "Comments": null,
  "FormValues": {},
  "QueueTime": null,
  "QueueTimeExpiry": null,
  "Name": "Deploy to Development",
  "Created": "2024-08-02T05:07:42.445+00:00",
  "TentacleRetentionPeriod": null,
  "ChangeRequestSettings": null,
  "DeployedBy": "System",
  "DeployedById": null,
  "FailureEncountered": false,
  "DeployedToMachineIds": [],
  "ExecutionPlanLogContext": {
    "Steps": []
  },
  "Links": {
    "Self": "/api/Spaces-1/deployments/Deployments-1",
    "Release": "/api/Spaces-1/releases/Releases-1",
    "Environment": "/api/Spaces-1/environments/Environments-1",
    "Project": "/api/Spaces-1/projects/Projects-1",
    "Task": "/api/tasks/ServerTasks-11599",
    "Web": "/app#/Spaces-1/deployments/Deployments-1",
    "Artifacts": "/api/Spaces-1/artifacts?regarding=Deployments-1",
    "Interruptions": "/api/Spaces-1/interruptions?regarding=Deployments-1",
    "DeploymentProcess": "/api/Spaces-1/deploymentprocesses/deploymentprocess-Projects-1-s-1-CGNSF"
  }
}
],
"Links": {
"Self": "/api/Spaces-1/deployments?skip=0&take=30",
"Template": "/api/Spaces-1/deployments{?skip,take,ids,projects,environments,tenants,channels,taskState,partialName}",
"Page.All": "/api/Spaces-1/deployments?skip=0&take=2147483647",
"Page.Current": "/api/Spaces-1/deployments?skip=0&take=30",
"Page.Last": "/api/Spaces-1/deployments?skip=0&take=30"
}
```

Machine response data

```
{
  "Id": "Machines-4",
  "EnvironmentIds": [
    "Environments-1"
  ],
  "Roles": [
    "test-server"
  ],
  "TenantedDeploymentParticipation": "Untenanted",
  "TenantIds": [],
  "TenantTags": [],
  "SpaceId": "Spaces-1",
  "Name": "ECS Instance Dev",
  "Thumbprint": null,
  "Uri": null,
  "IsDisabled": false,
  "MachinePolicyId": "MachinePolicies-1",
  "HealthStatus": "Unhealthy",
  "HasLatestCalamari": true,
  "StatusSummary": "There was a problem communicating with this machine (last checked: Tuesday, 27 August 2024 5:39:57 PM +00:00)",
  "IsInProcess": false,
  "Endpoint": {
    "CommunicationStyle": "StepPackage",
    "DeploymentTargetTypeId": "aws-ecs-target",
    "StepPackageId": "aws-ecs-target",
    "StepPackageVersion": "3.0.1",
    "LastSavedStepPackageVersion": "3.0.1",
    "Inputs": {
      "clusterName": " team-isaac",
      "region": "eu-west-1",
      "authentication": {
        "credentials": {
          "type": "account",
          "account": "Accounts-1"
        },
        "role": {
          "type": "noAssumedRole"
        }
      }
    },
    "DefaultWorkerPoolId": "",
    "Id": null,
    "LastModifiedOn": null,
    "LastModifiedBy": null,
    "Links": {
      "Logo": "/api/steps/deploymenttargets/aws-ecs-target/3.0.1/logo"
    }
  },
  "OperatingSystem": "Unknown",
  "ShellName": "Unknown",
  "ShellVersion": "Unknown",
  "Architecture": "Unknown",
  "Slug": "ecs-instance-dev",
  "SkipInitialHealthCheck": false,
  "Links": {
    "Self": "/api/Spaces-1/machines/Machines-4",
    "Connection": "/api/Spaces-1/machines/Machines-4/connection",
    "TasksTemplate": "/api/Spaces-1/machines/Machines-4/tasks{?skip,take,type}",
    "SinglyScopedVariableDetails": "/api/Spaces-1/machines/Machines-4/singlyScopedVariableDetails"
  }
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Space entity

```
{
  "identifier": "Spaces-1",
  "title": "Default",
  "icon": "Octopus",
  "blueprint": "octopusSpace",
  "team": [],
  "properties": {
    "url": "https://testport.octopus.app/app#/Spaces-1",
    "description": null
  },
  "relations": {},
  "createdAt": "2024-08-22T14:27:34.746Z",
  "createdBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT",
  "updatedAt": "2024-08-22T14:27:34.746Z",
  "updatedBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT"
}
```

Project entity

```
{
  "identifier": "Projects-1",
  "title": "Sample Project",
  "icon": "Octopus",
  "blueprint": "octopusProject",
  "team": [],
  "properties": {
    "slug": null,
    "url": "https://testport.octopus.app/app#/Spaces-1/projects/Projects-1",
    "description": "Explore how to automate your deployments with Octopus Deploy.\n\nEdit the custom script step, tweak the variables, and run your first deployment. Experiment and make it your own!",
    "isDisabled": false,
    "tenantedDeploymentMode": "Untenanted"
  },
  "relations": {},
  "createdAt": "2024-08-22T14:27:37.814Z",
  "createdBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT",
  "updatedAt": "2024-08-22T14:27:37.814Z",
  "updatedBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT"
}
```

Release entity

```
{
  "identifier": "Releases-44",
  "title": "Projects-41(0.0.2)",
  "icon": "Octopus",
  "blueprint": "octopusRelease",
  "team": [],
  "properties": {
    "version": "0.0.2",
    "assembledDate": "2024-08-21T16:17:46.750+00:00",
    "channelId": "Channels-41",
    "releaseNotes": null,
    "url": "https://testport.octopus.app/app#/Spaces-1/releases/Releases-44"
  },
  "relations": {},
  "createdAt": "2024-08-22T14:27:41.697Z",
  "createdBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT",
  "updatedAt": "2024-08-22T14:27:41.697Z",
  "updatedBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT"
}
```

Deployment entity

```
{
  "identifier": "Deployments-1",
  "title": "Deploy to Development",
  "icon": "Octopus",
  "blueprint": "octopusDeployment",
  "team": [],
  "properties": {
    "createdAt": "2024-08-02T05:07:42.445+00:00",
    "deployedBy": "System",
    "taskId": "ServerTasks-11599",
    "failureEncountered": false,
    "comments": null,
    "url": "https://testport.octopus.app/app#/Spaces-1/deployments/Deployments-1"
  },
  "relations": {},
  "createdAt": "2024-08-22T14:27:45.276Z",
  "createdBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT",
  "updatedAt": "2024-08-22T14:27:45.276Z",
  "updatedBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT"
}
```

Machine entity

```
{
  "identifier": "Machines-4",
  "title": "ECS Instance Dev",
  "icon": "Octopus",
  "blueprint": "octopusMachine",
  "team": [],
  "properties": {
    "roles": [
      "test-server"
    ],
    "status": "Unhealthy",
    "url": "https://testport.octopus.app/app#/Spaces-1/infrastructure/machines/Machines-4/settings",
    "isDisabled": false,
    "operatingSystem": "Unknown",
    "architecture": "Unknown",
    "statusSummary": "There was a problem communicating with this machine (last checked: Monday, 26 August 2024 5:40:16 PM +00:00)",
    "endpointType": "aws-ecs-target",
    "communicationStyle": "StepPackage"
  },
  "relations": {},
  "createdAt": "2024-08-22T14:27:53.944Z",
  "createdBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT",
  "updatedAt": "2024-08-27T12:29:12.362Z",
  "updatedBy": "zhOWp1YybWfY12bAxNz3d1ByX18iA1yT"
}
```
