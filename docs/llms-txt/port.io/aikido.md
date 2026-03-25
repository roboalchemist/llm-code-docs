# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/aikido.md

# Aikido

Loading version...

Port's Aikido integration allows you to model Aikido resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Track security vulnerabilities from Aikido in Port
* Map repositories and their security findings
* Maintain real-time synchronization between Aikido and Port

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Aikido into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Repositories`](https://apidocs.aikido.dev/reference/listcoderepos)
* [`Issues`](https://apidocs.aikido.dev/reference/exportissues)

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [Aikido<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Aikido) in your portal.

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

  * issue.open.created
  * issue.snoozed
  * issue.ignored.manual
  * issue.closed

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

1. Go to the [Aikido<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Aikido) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Aikido<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Aikido<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Aikido<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Aikido
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

1. Create a `values.yaml` file in `argocd/my-ocean-aikido-integration` in your git repository with the content:

Default behaviour

Remember to replace the placeholder for `AIKIDO_CLIENT_ID`,`AIKIDO_CLIENT_SECRET`, `AIKIDO_API_URL`, `WEBHOOK_SECRET`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-aikido-integration
  type: aikido
  eventListener:
    type: POLLING
  config:
    aikidoApiUrl: AIKIDO_API_URL
  secrets:
    aikidoClientId: AIKIDO_CLIENT_ID
    aikidoClientSecret: AIKIDO_CLIENT_SECRET
    webhookSecret: WEBHOOK_SECRET
```

<br />

2. Install the `my-ocean-aikido-integration` ArgoCD Application by creating the following `my-ocean-aikido-integration.yaml` manifest:

Configuration variable replacement

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-aikido-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-aikido-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.8.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-aikido-integration/values.yaml
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
kubectl apply -f my-ocean-aikido-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                                | Description                                                                                                          | Required |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                          | Your Port client id                                                                                                  | â       |
| `port.clientSecret`                      | Your Port client secret                                                                                              | â       |
| `port.baseUrl`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                    | â       |
| `integration.identifier`                 | Change the identifier to describe your integration                                                                   | â       |
| `integration.type`                       | The integration type                                                                                                 | â       |
| `integration.eventListener.type`         | The event listener type                                                                                              | â       |
| `integration.secrets.aikidoClientId`     | The Aikido Client ID                                                                                                 | â       |
| `integration.secrets.aikidoClientSecret` | The Aikido Client Secret                                                                                             | â       |
| `integration.config.apiUrl`              | The Aikido API URL. If not specified, the default will be <https://app.aikido.dev>                                   | â       |
| `baseUrl`                                | The host of the Port Ocean app. Used to set up the integration endpoint as the target for Webhooks created in Aikido | â       |
| `integration.secret.webhookSecret`       | This is a password you create, that Aikido uses to sign webhook events to Port                                       | â       |
| `scheduledResyncInterval`                | The number of minutes between each resync                                                                            | â       |
| `initializePortResources`                | Default true, When set to true the integration will create default blueprints and the port App config Mapping        | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

This workflow/pipeline will run the Aikido integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID`     | The Aikido Client ID                                                                                                                                        | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET` | The Aikido API Client Secret                                                                                                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`       | Aikido webhook secret used to verify the webhook request                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL`       | The Aikido API URL. If not specified, the default will be <https://app.aikido.dev>                                                                          | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |
| `OCEAN__BASE_URL`                                  | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Aikido                                        | â       |

<br />

Here is an example for `aikido-integration.yml` workflow file:

```
name: Aikido Exporter Workflow

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
          type: 'aikido'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            aikido_client_id: ${{ secrets.OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID }}
            aikido_client_secret: ${{ secrets.OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET }}
            aikido_api_url: ${{ secrets.OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL }}
            webhook_secret: ${{ secrets.OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID`     | The Aikido Client ID                                                                                                                                        | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET` | The Aikido API Client Secret                                                                                                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`       | Aikido webhook secret used to verify the webhook request                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL`       | The Aikido API URL. If not specified, the default will be <https://app.aikido.dev>                                                                          | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |
| `OCEAN__BASE_URL`                                  | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Aikido                                        | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Aikido Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID', variable: 'OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET', variable: 'OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL', variable: 'OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET', variable: 'OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="aikido"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID=$OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID \
                                -e OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET=$OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET \
                                -e OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL=$OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL \
                                -e OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET=$OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET \
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

tip

Your Azure Devops agent should be able to run docker commands.

Make sure to configure the following variables using [Azure Devops variable groups](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops\&tabs=yaml). Add them into in a variable group named `port-ocean-credentials`:

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID`     | The Aikido Client ID                                                                                                                                        | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET` | The Aikido API Client Secret                                                                                                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`       | Aikido webhook secret used to verify the webhook request                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL`       | The Aikido API URL. If not specified, the default will be <https://app.aikido.dev>                                                                          | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |
| `OCEAN__BASE_URL`                                  | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Aikido                                        | â       |

<br />

Here is an example for `aikido-integration.yml` pipeline file:

```
trigger:
- main

pool:
  vmImage: "ubuntu-latest"

variables:
  - group: port-ocean-credentials # OCEAN__PORT__CLIENT_ID, OCEAN__PORT__CLIENT_SECRET, OCEAN__INTEGRATION__CONFIG__TOKEN


steps:
- script: |
    echo Add other tasks to build, test, and deploy your project.
    # Set Docker image and run the container
    integration_type="aikido"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
    -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
    -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
    -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
    -e OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID=$OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID \
    -e OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET=$OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET \
    -e OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL=$OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL \
    -e OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET=$OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET \
    -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
    -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
    -e OCEAN__PORT__BASE_URL='https://api.port.io' \
    $image_name

    exit $?
  displayName: 'Ingest Aikido Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                          | Description                                                                                                                                                 | Required |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID`     | The Aikido Client ID                                                                                                                                        | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET` | The Aikido API Client Secret                                                                                                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`       | Aikido webhook secret used to verify the webhook request                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL`       | The Aikido API URL. If not specified, the default will be <https://app.aikido.dev>                                                                          | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                 | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                    | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                   | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                           | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                       | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |
| `OCEAN__BASE_URL`                                  | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Aikido                                        | â       |

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
  INTEGRATION_TYPE: aikido
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
        -e OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID=$OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_ID \
        -e OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET=$OCEAN__INTEGRATION__CONFIG__AIKIDO_CLIENT_SECRET \
        -e OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL=$OCEAN__INTEGRATION__CONFIG__AIKIDO_API_URL \
        -e OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET=$OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET \
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

### Webhook Configuration[â](#webhook-configuration "Direct link to Webhook Configuration")

To enable real-time data synchronization from Aikido to Port, you must configure webhooks in Aikido following [this guide](https://apidocs.aikido.dev/reference/webhooks). This setup allows Port to receive immediate notifications whenever relevant changes occur in Aikido. When setting up the webhook, the URL should follow the format:

`<base_url>/integration/webhook`

IMPORTANT

For security and event authenticity, we strongly recommend setting an HMAC secret in the Aikido dashboard. Once configured, make sure to set the corresponding value in your Port environment using the variable `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET` . This ensures Port can securely verify incoming webhook events from Aikido.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
  - kind: repositories
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"aikidoRepository"'
          identifier: .id | tostring
          title: .name
          properties:
            name: .name
            provider: .provider
            externalRepoId: .external_repo_id
            active: .active
            url: .url
            branch: .branch
            lastScannedAt: .last_scanned_at
  - kind: issues
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"aikidoIssue"'
          identifier: .id | tostring
          title: .rule | tostring
          properties:
            status: .status
            severity: .severity
            severityScore: .severity_score
            affectedFile: .affected_file
            attackSurface: .attack_surface
            type: .type
            rule: .rule
            codeRepoId: .code_repo_id
            codeRepoName: .code_repo_name
          relations:
            aikidoRepository: .code_repo_id
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Repository[â](#repository "Direct link to Repository")

Repository blueprint

Create in Port

```
{
    "identifier": "aikidoRepository",
    "title": "Aikido Repository",
    "icon": "Aikido",
    "schema": {
        "properties": {
            "name": {
                "type": "string",
                "title": "Repository Name"
            },
            "provider": {
                "type": "string",
                "title": "Provider",
                "enum": ["github", "gitlab", "gitlab-server", "bitbucket", "azure_devops", "selfscan"]
            },
            "externalRepoId": {
                "type": "string",
                "title": "External Repository ID"
            },
            "active": {
                "type": "boolean",
                "title": "Active"
            },
            "url": {
                "type": "string",
                "title": "Repository URL"
            },
            "branch": {
                "type": "string",
                "title": "Default Branch"
            },
            "lastScannedAt": {
                "type": "number",
                "title": "Last Scanned At"
            }
        },
        "required": ["name", "provider"]
    },
    "relations": {
        "aikidoIssue": {
            "title": "Issues",
            "target": "aikidoIssue",
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
  - kind: repositories
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"aikidoRepository"'
          identifier: .id | tostring
          title: .name
          properties:
            name: .name
            provider: .provider
            externalRepoId: .external_repo_id
            active: .active
            url: .url
            branch: .branch
            lastScannedAt: .last_scanned_at
```

### Issue[â](#issue "Direct link to Issue")

Issue blueprint

Create in Port

```
{
  "identifier": "aikidoIssue",
  "title": "Aikido Issue",
  "icon": "Aikido",
  "schema": {
      "properties": {
          "groupId": {
              "type": "number",
              "title": "Group ID"
          },
          "attackSurface": {
              "type": "string",
              "title": "Attack Surface",
              "enum": ["backend", "frontend", "infrastructure", "docker_container",  "cloud"]
          },
          "status": {
              "type": "string",
              "title": "Status",
              "enum": ["open", "closed", "ignored", "snoozed"],
              "enumColors": {
                  "open": "red",
                  "closed": "green",
                  "ignored": "yellow",
                  "snoozed": "blue"
              }
          },
          "severity": {
              "type": "string",
              "title": "Severity",
              "enum": ["critical", "high", "medium", "low"]
          },
          "severityScore": {
              "type": "number",
              "title": "Severity Score"
          },
          "type": {
              "type": "string",
              "title": "Issue Type",
              "enum": ["open_source", "leaked_secret", "cloud", "iac", "sast", "mobile", "surface_monitoring", "malware", "eol", "scm_security", "ai_pentest","license"]
          },
          "rule": {
              "type": "string",
              "title": "Rule Name"
          },
          "affectedFile": {
              "type": "string",
              "title": "Affected File"
          },
          "codeRepoName": {
              "type": "string",
              "title": "Code Repository Name"
          },
          "codeRepoId": {
              "type": "number",
              "title": "Code Repository ID"
          },
          "closedAt": {
              "type": "number",
              "title": "Closed At"
          }
      },
      "required": ["status", "severity", "type"]
  },
  "relations": {
      "aikidoRepository": {
          "title": "Repository",
          "target": "aikidoRepository",
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
  - kind: issues
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"aikidoIssue"'
          identifier: .id | tostring
          title: .rule | tostring
          properties:
            status: .status
            severity: .severity
            severityScore: .severity_score
            affectedFile: .affected_file
            attackSurface: .attack_surface
            type: .type
            rule: .rule
            codeRepoId: .code_repo_id
            codeRepoName: .code_repo_name
          relations:
            aikidoRepository: .code_repo_id
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Aikido. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Aikido:

Repository response data

```
{
  "id": 1,
  "name": "Compression service",
  "provider": "github",
  "external_repo_id": "R_kgDOI5RlKA",
  "active": true,
  "url": "https://api.github.com/repos/aikidemo/compression-service",
  "branch": "main",
  "last_scanned_at": 1720083163
}
```

Issue response data

```
{
    "id": 1,
    "group_id": 1,
    "attack_surface": "backend",
    "status": "open",
    "severity": 90,
    "severity_score": "critical",
    "type": "open_source",
    "rule": "SQL injection",
    "rule_id": "aik_cloud_aws_001",
    "affected_package": "minimist",
    "affected_file": "index.php",
    "first_detected_at": 1700489005,
    "code_repo_name": "test-service",
    "code_repo_id": 1,
    "container_repo_id": 1,
    "container_repo_name": "aikido/test-service",
    "sla_days": 5,
    "sla_remediate_by": 1700924603,
    "ignored_at": null,
    "ignored_by": "user",
    "closed_at": null,
    "start_line": 68,
    "end_line": 70,
    "snooze_until": null,
    "cwe_classes": [
      "CWE-89"
    ],
    "installed_version": "4.2.0",
    "patched_versions": [
      "4.2.1",
      "5.0.0"
    ],
    "license": null,
    "programming_language": "PHP"
}
```
