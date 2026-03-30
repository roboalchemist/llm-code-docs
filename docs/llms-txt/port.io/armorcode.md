# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/armorcode.md

# ArmorCode

Port's ArmorCode integration allows you to model ArmorCode resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Track security vulnerabilities and findings from ArmorCode in Port.
* Map products, sub-products, and their security findings.
* Monitor security posture across your software catalog.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from ArmorCode into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Products`](https://docs.armorcode.com/api/products) - ArmorCode products representing applications or services.
* [`Sub-Products`](https://docs.armorcode.com/api/sub-products) - Repositories or components within products.
* [`Findings`](https://docs.armorcode.com/api/findings) - Security vulnerabilities and issues detected by ArmorCode.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:

* Hosted by Port
* Self-hosted
* CI

1. Go to the [ArmorCode<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=ArmorCode) in your portal.

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

1. Go to the [ArmorCode<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=ArmorCode) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->ArmorCode<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->ArmorCode<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->ArmorCode<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  ArmorCode
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

1. Create a `values.yaml` file in `argocd/my-ocean-armorcode-integration` in your git repository with the content:

Default behaviour

Remember to replace the placeholder for `ARMORCODE_API_TOKEN`, `ARMORCODE_API_URL`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-armorcode-integration
  type: armorcode
  eventListener:
    type: POLLING
  config:
    armorcodeApiUrl: ARMORCODE_API_URL
  secrets:
    armorcodeApiToken: ARMORCODE_API_TOKEN
```

<br />

2. Install the `my-ocean-armorcode-integration` ArgoCD Application by creating the following `my-ocean-armorcode-integration.yaml` manifest:

Configuration variable replacement

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

**ArgoCD Application (click to expand)**

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-armorcode-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-armorcode-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.8.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-armorcode-integration/values.yaml
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
kubectl apply -f my-ocean-armorcode-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                               | Description                                                                                                   | Required |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                         | Your Port client id                                                                                           | â       |
| `port.clientSecret`                     | Your Port client secret                                                                                       | â       |
| `port.baseUrl`                          | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                             | â       |
| `integration.identifier`                | Change the identifier to describe your integration                                                            | â       |
| `integration.type`                      | The integration type                                                                                          | â       |
| `integration.eventListener.type`        | The event listener type                                                                                       | â       |
| `integration.secrets.armorcodeApiToken` | The ArmorCode API Token                                                                                       | â       |
| `integration.config.armorcodeApiUrl`    | The ArmorCode API URL. If not specified, the default will be <https://api.armorcode.com>                      | â       |
| `scheduledResyncInterval`               | The number of minutes between each resync                                                                     | â       |
| `initializePortResources`               | Default true, When set to true the integration will create default blueprints and the port App config Mapping | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

This workflow/pipeline will run the ArmorCode integration once and then exit, this is useful for **scheduled** ingestion of data.

Real-time updates

If you want the integration to update Port in real time using webhooks you should use the [Real-time (self-hosted)](/build-your-software-catalog/sync-data-to-catalog/code-quality-security/armorcode/.md?installation-methods=real-time-self-hosted#setup) installation option

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                         | Description                                                                                                                                                 | Required |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN` | The ArmorCode API Token                                                                                                                                     | â       |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL`   | The ArmorCode API URL. If not specified, the default will be <https://api.armorcode.com>                                                                    | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                  | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                          | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                      | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

<br />

Here is an example for `armorcode-integration.yml` workflow file:

```
name: ArmorCode Exporter Workflow

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
          type: 'armorcode'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            armorcode_api_token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN }}
            armorcode_api_url: ${{ secrets.OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                         | Description                                                                                                                                                 | Required |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN` | The ArmorCode API Token                                                                                                                                     | â       |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL`   | The ArmorCode API URL. If not specified, the default will be <https://api.armorcode.com>                                                                    | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                  | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                          | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                      | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |
| `OCEAN__BASE_URL`                                 | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in ArmorCode                                     | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run ArmorCode Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL', variable: 'OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="armorcode"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN=$OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN \
                                -e OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL=$OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL \
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

| Parameter                                         | Description                                                                                                                                                 | Required |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN` | The ArmorCode API Token                                                                                                                                     | â       |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL`   | The ArmorCode API URL. If not specified, the default will be <https://api.armorcode.com>                                                                    | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                  | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                          | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                      | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

<br />

Here is an example for `armorcode-integration.yml` pipeline file:

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
    integration_type="armorcode"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
    -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
    -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
    -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
    -e OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN=$OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN \
    -e OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL=$OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL \
    -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
    -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
    -e OCEAN__PORT__BASE_URL='https://api.port.io' \
    $image_name

    exit $?
  displayName: 'Ingest ArmorCode Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                         | Description                                                                                                                                                 | Required |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN` | The ArmorCode API Token                                                                                                                                     | â       |
| `OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL`   | The ArmorCode API URL. If not specified, the default will be <https://api.armorcode.com>                                                                    | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                          | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                  | Change the identifier to describe your integration, if not set will use the default one                                                                     | â       |
| `OCEAN__PORT__CLIENT_ID`                          | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                      | Your port client ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) secret | â       |
| `OCEAN__PORT__BASE_URL`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           | â       |

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
  INTEGRATION_TYPE: armorcode
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
        -e OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN=$OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_TOKEN \
        -e OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL=$OCEAN__INTEGRATION__CONFIG__ARMORCODE_API_URL \
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

**Default mapping configuration (click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
  - kind: product
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"armorcodeProduct"'
          identifier: .id | tostring
          title: .name
          properties:
            name: .name
            description: .description
            businessOwner: .business_owner
            securityOwner: .security_owner
  - kind: sub-product
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"armorcodeSubProduct"'
          identifier: .id | tostring
          title: .name
          properties:
            name: .name
            repoLink: .repo_link
            programmingLanguage: .programming_language
            technologies: .technologies
          relations:
            product: .product_id
  - kind: finding
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"armorcodeFinding"'
          identifier: .id | tostring
          title: .title
          properties:
            source: .source
            description: .description
            mitigation: .mitigation
            severity: .severity
            findingCategory: .finding_category
            status: .status
            productStatus: .product_status
            subProductStatuses: .sub_product_statuses
            title: .title
            toolSeverity: .tool_severity
            createdAt: .created_at
            lastUpdated: .last_updated
            cwe: .cwe
            cve: .cve
            link: .link
            riskScore: .risk_score
            findingScore: .finding_score
          relations:
            product: .product_id
            subProduct: .sub_product_id
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Product[â](#product "Direct link to Product")

**Product blueprint (click to expand)**

Create in Port

```
{
  "identifier": "armorcodeProduct",
  "title": "Armorcode Product",
  "icon": "Package",
  "schema": {
    "properties": {
      "name": {
        "type": "string",
        "title": "Name"
      },
      "description": {
        "type": "string",
        "title": "Description"
      },
      "businessOwner": {
        "type": "string",
        "title": "Business Owner"
      },
      "securityOwner": {
        "type": "string",
        "title": "Security Owner"
      }
    },
    "required": [
      "name"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: products
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"armorcodeProduct"'
          identifier: .id | tostring
          title: .name
          properties:
            name: .name
            description: .description
            businessOwner: .business_owner
            securityOwner: .security_owner
```

### Sub-Product[â](#sub-product "Direct link to Sub-Product")

**Sub-Product blueprint (click to expand)**

Create in Port

```
{
  "identifier": "armorcodeSubProduct",
  "title": "Armorcode Sub-Product",
  "icon": "Git",
  "schema": {
    "properties": {
      "name": {
        "type": "string",
        "title": "Name"
      },
      "repoLink": {
        "type": "string",
        "title": "Repository Link",
        "format": "url"
      },
      "programmingLanguage": {
        "type": "string",
        "title": "Language"
      },
      "technologies": {
        "type": "array",
        "title": "Technologies",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "name"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "product": {
      "title": "Product",
      "target": "armorcodeProduct",
      "required": false,
      "many": false
    }
  }
}
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: sub_products
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"armorcodeSubProduct"'
          identifier: .id | tostring
          title: .name
          properties:
            name: .name
            repoLink: .repo_link
            programmingLanguage: .programming_language
            technologies: .technologies
          relations:
            product: .product_id
```

### Finding[â](#finding "Direct link to Finding")

**Finding blueprint (click to expand)**

Create in Port

```
{
  "identifier": "armorcodeFinding",
  "title": "ArmorCode Finding",
  "icon": "Bug",
  "schema": {
    "properties": {
      "source": {
        "title": "Source",
        "type": "string",
        "description": "The security tool that generated this finding"
      },
      "description": {
        "title": "Description",
        "type": "string",
        "description": "Detailed description of the security finding"
      },
      "mitigation": {
        "title": "Mitigation",
        "type": "string",
        "description": "Recommended mitigation steps for this finding"
      },
      "severity": {
        "type": "string",
        "title": "Severity",
        "enum": [
          "CRITICAL",
          "HIGH",
          "MEDIUM",
          "LOW",
          "INFORMATIONAL",
          "UNKNOWN"
        ],
        "enumColors": {
          "CRITICAL": "red",
          "HIGH": "orange",
          "MEDIUM": "yellow",
          "LOW": "darkGray",
          "INFORMATIONAL": "silver",
          "UNKNOWN": "lightGray"
        }
      },
      "findingCategory": {
        "title": "Finding Category",
        "type": "string",
        "description": "Category classification of the finding"
      },
      "status": {
        "type": "string",
        "title": "Status",
        "enum": [
          "OPEN",
          "CLOSED",
          "ACTIVE",
          "IN_PROGRESS",
          "RESOLVED",
          "TRIAGE",
          "CONTROLLED",
          "SUPPRESS",
          "MITIGATED"
        ],
        "enumColors": {
          "OPEN": "paleBlue",
          "ACTIVE": "olive",
          "CLOSED": "lightGray",
          "RESOLVED": "green",
          "IN_PROGRESS": "orange",
          "TRIAGE": "yellow",
          "CONTROLLED": "purple",
          "SUPPRESS": "darkGray",
          "MITIGATED": "lime"
        }
      },
      "productStatus": {
        "title": "Product Status",
        "type": "string",
        "description": "Status of the product containing this finding"
      },
      "subProductStatuses": {
        "title": "Sub-Product Status",
        "type": "string",
        "description": "Status of the sub-product containing this finding"
      },
      "title": {
        "title": "Title",
        "type": "string",
        "description": "Brief title describing the finding"
      },
      "toolSeverity": {
        "title": "Tool Severity",
        "type": "string",
        "description": "Original severity as reported by the security tool"
      },
      "createdAt": {
        "title": "Created At",
        "type": "string",
        "description": "When the finding was first created"
      },
      "lastUpdated": {
        "title": "Last Updated",
        "type": "string",
        "format": "date-time",
        "description": "When the finding was last updated"
      },
      "cwe": {
        "title": "CWE",
        "type": "array",
        "description": "Common Weakness Enumeration identifiers",
        "items": {
          "type": "string"
        }
      },
      "cve": {
        "title": "CVE",
        "type": "array",
        "description": "Common Vulnerabilities and Exposures identifiers",
        "items": {
          "type": "string"
        }
      },
      "link": {
        "title": "Link to Finding",
        "type": "string",
        "format": "url",
        "description": "Direct link to the finding in ArmorCode"
      },
      "riskScore": {
        "title": "Risk Score",
        "type": "number",
        "description": "Calculated risk score for the finding"
      },
      "findingScore": {
        "title": "Finding Score",
        "type": "number",
        "description": "ArmorCode finding score"
      }
    },
    "required": [
      "title",
      "status",
      "severity",
      "source",
      "findingCategory"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "product": {
      "title": "Product",
      "target": "armorcodeProduct",
      "required": true,
      "many": false
    },
    "subProduct": {
      "title": "Sub-Product",
      "target": "armorcodeSubProduct",
      "required": true,
      "many": false
    }
  }
}
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: findings
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          blueprint: '"armorcodeFinding"'
          identifier: .id | tostring
          title: .title
          properties:
            source: .source
            description: .description
            mitigation: .mitigation
            severity: .severity
            findingCategory: .finding_category
            status: .status
            productStatus: .product_status
            subProductStatuses: .sub_product_statuses
            title: .title
            toolSeverity: .tool_severity
            createdAt: .created_at
            lastUpdated: .last_updated
            cwe: .cwe
            cve: .cve
            link: .link
            riskScore: .risk_score
            findingScore: .finding_score
          relations:
            product: .product_id
            subProduct: .sub_product_id
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from ArmorCode. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from ArmorCode:

**Product response data (click to expand)**

```
{
  "id": 1,
  "name": "E-commerce Platform",
  "description": "Main e-commerce application for online retail",
  "business_owner": "John Smith",
  "security_owner": "Sarah Johnson",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-20T14:45:00Z"
}
```

**Sub-Product response data (click to expand)**

```
{
  "id": 101,
  "name": "payment-service",
  "repo_link": "https://github.com/company/payment-service",
  "programming_language": "Java",
  "technologies": ["Spring Boot", "PostgreSQL", "Redis"],
  "product_id": 1,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-20T14:45:00Z"
}
```

**Finding response data (click to expand)**

```
{
  "id": 1001,
  "title": "SQL Injection Vulnerability",
  "source": "SAST",
  "description": "Potential SQL injection vulnerability detected in user input validation",
  "mitigation": "Use parameterized queries and input validation",
  "severity": "HIGH",
  "finding_category": "Code Security",
  "status": "OPEN",
  "product_status": "ACTIVE",
  "sub_product_statuses": "ACTIVE",
  "tool_severity": "HIGH",
  "created_at": "2024-01-15T10:30:00Z",
  "last_updated": "2024-01-20T14:45:00Z",
  "cwe": ["CWE-89"],
  "cve": ["CVE-2023-1234"],
  "link": "https://app.armorcode.com/findings/1001",
  "risk_score": 8.5,
  "finding_score": 7.2,
  "product_id": 1,
  "sub_product_id": 101
}
```
