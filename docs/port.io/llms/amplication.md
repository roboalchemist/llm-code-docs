# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/other/amplication.md

# Amplication

Loading version...

Port's Amplication integration allows you to model [Amplication](https://amplication.com) resources in your software catalog, from which you can then automate code generation using predefined templates, ensuring standardization for resource creation.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Automate scaffolding of new services using Amplicationâs templates.
* Ensure standardization by enforcing predefined golden paths for resource creation.
* Leverage code generation to accelerate development and maintain consistency.
* Poll Amplication for templates, resources, and outdated version alerts to keep you in sync with your Amplication resources.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Amplication into Port are listed below:

* [`Template`](https://docs.amplication.com/day-zero/live-templates)
* [`Resource`](https://docs.amplication.com/day-one/overview)
* [`Outdated Version Alert`](https://docs.amplication.com/day-two/automated-alerts)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Generate an Amplication API token[â](#generate-an-amplication-api-token "Direct link to Generate an Amplication API token")

1. Navigate to `https://app.amplication.com/` and go to the settings tab of your workspace.

2. Navigate to the `API Tokens` section and generate a new token.

3. Copy the token and save it in a secure location.

### Amplication host URL[â](#amplication-host-url "Direct link to Amplication host URL")

Your Amplication host URL should be `https://server.amplication.com/graphql`.

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

1. Go to the [Amplication<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Amplication) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Amplication<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Amplication<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Amplication<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Amplication
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

1. Create a `values.yaml` file in `argocd/my-ocean-amplication-integration` in your git repository with the content:

note

Remember to replace the placeholders for `AMPLICATION_HOST` and `AMPLICATION_TOKEN`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-amplication-integration
  type: amplication
  eventListener:
    type: POLLING
  config:
    amplicationHost: AMPLICATION_HOST
  secrets:
    amplicationToken: AMPLICATION_TOKEN
```

<br />

2. Install the `my-ocean-amplication-integration` ArgoCD Application by creating the following `my-ocean-amplication-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-amplication-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-amplication-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-amplication-integration/values.yaml
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
kubectl apply -f my-ocean-amplication-integration.yaml
```

This table summarizes the available parameters for the installation. Note the parameters specific to this integration, they are last in the table.

| Parameter                              | Description                                                                                                   | Required |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                        | Your port client id                                                                                           | â       |
| `port.clientSecret`                    | Your port client secret                                                                                       | â       |
| `port.baseUrl`                         | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                             | â       |
| `integration.identifier`               | Change the identifier to describe your integration                                                            | â       |
| `integration.type`                     | The integration type                                                                                          | â       |
| `integration.eventListener.type`       | The event listener type                                                                                       | â       |
| `scheduledResyncInterval`              | The number of minutes between each resync                                                                     | â       |
| `initializePortResources`              | Default true, When set to true the integration will create default blueprints and the port App config Mapping | â       |
| `integration.secrets.amplicationToken` | The Amplication API [token](https://docs.amplication.com/docs/api-reference/authentication).                  | â       |
| `integration.config.amplicationHost`   | The Amplication host. For example <https://server.amplication.com/graphql>                                    | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

### Event listener

The integration uses polling to pull the configuration from Port every minute and check it for changes. If there is a change, a resync will occur.

This workflow/pipeline will run the Amplication integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                       | Description                                                                                                        | Required |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                        | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                    | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                         | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST`  | The Amplication host. For example <https://server.amplication.com/graphql>                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN` | The Amplication API [token](https://docs.amplication.com/docs/api-reference/authentication).                       | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`              | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

<br />

Here is an example for `amplication-integration.yml` workflow file:

```
name: Amplication Exporter Workflow

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
          type: 'amplication'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            amplication_token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN }}
            amplication_host: ${{ secrets.OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                       | Description                                                                                                        | Required |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                        | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                    | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                         | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST`  | The Amplication host. For example <https://server.amplication.com/graphql>                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN` | The Amplication API [token](https://docs.amplication.com/docs/api-reference/authentication).                       | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`              | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Amplication Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST', variable: 'OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="amplication"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN=$OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN \
                                -e OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST=$OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST \
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

| Parameter                                       | Description                                                                                                        | Required |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                        | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                    | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                         | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST`  | The Amplication host. For example <https://server.amplication.com/graphql>                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN` | The Amplication API [token](https://docs.amplication.com/docs/api-reference/authentication).                       | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`              | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

<br />

Here is an example for `amplication-integration.yml` pipeline file:

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
    integration_type="amplication"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
       -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
      -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
      -e OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN=$(OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN) \
      -e OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST=$(OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST) \
      -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
      -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
      -e OCEAN__PORT__BASE_URL='https://api.port.io' \
      $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                       | Description                                                                                                        | Required |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                        | Your port client id                                                                                                | â       |
| `OCEAN__PORT__CLIENT_SECRET`                    | Your port client secret                                                                                            | â       |
| `OCEAN__PORT__BASE_URL`                         | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                  | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST`  | The Amplication host. For example <https://server.amplication.com/graphql>                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN` | The Amplication API [token](https://docs.amplication.com/docs/api-reference/authentication).                       | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                | Change the identifier to describe your integration, if not set will use the default one                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`              | Default true, When set to false the integration will not create default blueprints and the port App config Mapping | â       |

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
  INTEGRATION_TYPE: amplication
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
        -e OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN=$OCEAN__INTEGRATION__CONFIG__AMPLICATION_TOKEN \
        -e OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST=$OCEAN__INTEGRATION__CONFIG__AMPLICATION_HOST \
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

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from Amplication's API into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (Click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
resources:
- kind: amplication_template
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"AmplicationTemplate"'
        properties:
          description: .description
          project: .project.name
          project_id: .project.id
          blueprint: .blueprint.name
          blueprint_id: .blueprint.id
- kind: amplication_resource
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .name
        blueprint: '"AmplicationResource"'
        properties:
          description: .description
          project: .project.name
          project_id: .project.id
          blueprint: .blueprint.name
          blueprint_id: .blueprint.id
          git_organization: .gitRepository.gitOrganization.provider
          git_repository: .gitRepository.gitOrganization.name + "/" + .gitRepository.name
        relations:
          template: if .serviceTemplate != null then .serviceTemplate.id else null end
- kind: amplication_alert
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: 'if .block != null then .type + ": " + .block.displayName else .type end'
        blueprint: '"AmplicationAlert"'
        properties:
          block_id: if .block != null then .block.id else null end
          block_displayName: if .block != null then .block.displayName else null end
          type: .type
          outdatedVersion: .outdatedVersion
          latestVersion: .latestVersion
          status: .status
        relations:
          resource: .resourceId
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Templates[â](#templates "Direct link to Templates")

Template Blueprint

Create in Port

```
{
  "identifier": "AmplicationTemplate",
  "description": "Blueprint for templates coming from Amplication's app",
  "title": "Amplication Template",
  "icon": "Amplication",
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
      "project": {
        "type": "string",
        "title": "Project"
      },
      "project_id": {
        "type": "string",
        "title": "Project ID"
      },
      "blueprint": {
        "type": "string",
        "title": "Blueprint"
      },
      "blueprint_id": {
        "type": "string",
        "title": "Blueprint ID"
      }
    },
    "required": [
      "name",
      "project_id",
      "project"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {
    "resource_count": {
      "title": "Resource Count",
      "icon": "Amplication",
      "type": "number",
      "description": "Number of resources created from this template",
      "target": "AmplicationResource",
      "calculationSpec": {
        "func": "count",
        "calculationBy": "entities"
      }
    }
  },
  "relations": {}
}
```

Integration configuration

```
createMissingRelatedEntities: True
resources:
  - kind: amplication_template
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"AmplicationTemplate"'
          properties:
            name: .name
            description: .description
            project: .project.name
            project_id: .project.id
            blueprint: .blueprint.name
            blueprint_id: .blueprint.id
```

### Resources[â](#resources "Direct link to Resources")

Resource blueprint

Create in Port

```
{
  "identifier": "AmplicationResource",
  "description": "Blueprint for resources coming from Amplication's app",
  "title": "Amplication Resource",
  "icon": "Amplication",
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
      "project": {
        "type": "string",
        "title": "Project"
      },
      "project_id": {
        "type": "string",
        "title": "Project ID"
      },
      "git_organization": {
        "icon": "Git",
        "type": "string",
        "title": "Git Organization"
      },
      "git_repository": {
        "icon": "Git",
        "type": "string",
        "title": "Git Repository"
      },
      "blueprint": {
        "type": "string",
        "title": "Blueprint"
      },
      "blueprint_id": {
        "type": "string",
        "title": "Blueprint ID"
      }
    },
    "required": [
      "name",
      "project",
      "project_id"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {
    "new_alerts_count": {
      "title": "Alerts Count",
      "icon": "Alert",
      "type": "number",
      "description": "Number of new outdated version alerts this resource has",
      "target": "AmplicationAlert",
      "query": {
        "combinator": "and",
        "rules": [
          {
            "property": "status",
            "operator": "=",
            "value": "New"
          }
        ]
      },
      "calculationSpec": {
        "func": "count",
        "calculationBy": "entities"
      }
    }
  },
  "relations": {
    "template": {
      "target": "AmplicationTemplate",
      "title": "Template",
      "description": "The template of this resource",
      "required": false,
      "many": false
    }
  }
}
```

Integration configuration

```
createMissingRelatedEntities: True
resources:
  - kind: amplication_resource
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .name
          blueprint: '"AmplicationResource"'
          properties:
            name: .name
            description: .description
            project: .project.name
            project_id: .project.id
            blueprint: .blueprint.name
            blueprint_id: .blueprint.id
            git_organization: .gitRepository.gitOrganization.provider
            git_repository: '.gitRepository.gitOrganization.name + "/" + .gitRepository.name'
          relations:
            template: if .serviceTemplate != null and .serviceTemplate != "None" then .serviceTemplate.id else null end
```

### Outdated Version Alerts[â](#outdated-version-alerts "Direct link to Outdated Version Alerts")

Outdated Version Alert blueprint

Create in Port

```
{
  "identifier": "AmplicationAlert",
  "description": "Blueprint for outdated version alerts coming from Amplication's app",
  "title": "Amplication Version Alert",
  "icon": "Amplication",
  "schema": {
    "properties": {
      "block_id": {
        "type": "string",
        "title": "Block ID"
      },
      "block_displayName": {
        "type": "string",
        "title": "Plugin Name"
      },
      "type": {
        "type": "string",
        "title": "Type",
        "default": "Other",
        "enum": [
          "PluginVersion",
          "TemplateVersion",
          "CodeEngineVersion",
          "Other"
        ],
        "enumColors": {
          "PluginVersion": "blue",
          "TemplateVersion": "orange",
          "CodeEngineVersion": "purple",
          "Other": "bronze"
        }
      },
      "outdatedVersion": {
        "type": "string",
        "title": "Outdated Version"
      },
      "latestVersion": {
        "type": "string",
        "title": "Latest Version"
      },
      "status": {
        "type": "string",
        "title": "Status",
        "default": "New",
        "enum": [
          "New",
          "Resolved",
          "Ignored",
          "Canceled"
        ],
        "enumColors": {
          "New": "turquoise",
          "Resolved": "red",
          "Ignored": "green",
          "Canceled": "blue"
        }
      }
    },
    "required": [
      "block_id",
      "block_displayName",
      "type",
      "outdatedVersion",
      "latestVersion",
      "status"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "resource": {
      "title": "Resource",
      "target": "AmplicationResource",
      "required": false,
      "many": false
    }
  }
}
```

Integration configuration

```
createMissingRelatedEntities: True
resources:
  - kind: amplication_alert
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: '.type + ": " + .block.displayName'
          blueprint: '"AmplicationAlert"'
          properties:
            block_id: .block.id
            block_displayName: .block.displayName
            type: .type
            outdatedVersion: .outdatedVersion
            latestVersion: .latestVersion
            status: .status
          relations:
            resource: .resourceId
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Amplication. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Amplication:

Template response data

```
{
  "id": "cm6zln01a0209utjtlorazri1",
  "name": "Port Node.js Template",
  "description": "Template created from an existing resource",
  "resourceType": "ServiceTemplate",
  "project": {
    "id": "cm6zlfk2o01liutjtdw8xj7f0",
    "name": "Port Integration"
  },
  "blueprint": {
    "id": "cm6gb3j00000p14gz2n11otq4",
    "name": "Node.js Service (Amplication's Standard)"
  }
}
```

Resource response data

```
{
  "id": "cm6gr9t4s0000jx5t8l8prvik",
  "name": "Sample Resource Name",
  "description": "General description for the resource",
  "resourceType": "Service",
  "project": {
    "id": "cm6gb3j0a000q14gzlq9m7h1o",
    "name": "Sample Project"
  },
  "blueprint": {
    "id": "cm6gb3j00000p14gz2n11otq4",
    "name": "Node.js Service (Amplication's Standard)"
  },
  "serviceTemplate": null,
  "gitRepository": {
    "name": "examplerepo",
    "gitOrganization": {
      "name": "examplecompany",
      "provider": "Github"
    }
  }
}
```

Alert response data

```
{
  "id": "cm71nzqfh00lftp1dh9bslk0n",
  "createdAt": "2025-02-12T08:44:11.022Z",
  "updatedAt": "2025-02-12T08:44:11.022Z",
  "resourceId": "cm71nzdyn00kltp1dyoe4abpu",
  "blockId": "cm67mln9k004k55uul3j4ywww",
  "block": {
    "id": "cm67mln9k004k55uul3j4ywww",
    "displayName": "Resource Template Version"
  },
  "type": "TemplateVersion",
  "outdatedVersion": "0.1.0",
  "latestVersion": "0.2.0",
  "status": "New"
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Template entity in Port

```
{
  "identifier": "cm6zln01a0209utjtlorazri1",
  "title": "Port Node.js Template",
  "team": [],
  "properties": {
    "name": "Port Node.js Template",
    "description": "Template created from an existing resource",
    "project": "Port Integration",
    "project_id": "cm6zlfk2o01liutjtdw8xj7f0",
    "blueprint": "Node.js Service (Amplication's Standard)",
    "blueprint_id": "cm6gb3j00000p14gz2n11otq4"
  },
  "relations": {},
  "icon": "Amplication"
}
```

Resource entity in Port

```
{
  "identifier": "cm6gr9t4s0000jx5t8l8prvik",
  "title": "Sample Resource Name",
  "team": [],
  "properties": {
    "name": "Sample Resource Name",
    "description": "General description for the resource",
    "project": "Sample Project",
    "project_id": "cm6gb3j0a000q14gzlq9m7h1o",
    "git_organization": "Github",
    "git_repository": "examplecompany/examplerepo",
    "blueprint": "Node.js Service (Amplication's Standard)",
    "blueprint_id": "cm6gb3j00000p14gz2n11otq4"
  },
  "relations": {},
  "icon": "Amplication"
}
```

Alert entity in Port

```
{
  "identifier": "cm71nzqfh00lftp1dh9bslk0n",
  "title": "TemplateVersion: Resource Template Version",
  "icon": "Amplication",
  "team": [],
  "properties": {
    "block_id": "cm67mln9k004k55uul3j4ywww",
    "block_displayName": "Resource Template Version",
    "type": "PluginVersion",
    "outdatedVersion": "0.1.0",
    "latestVersion": "0.2.0",
    "status": "New"
  },
  "relations": {
    "resource": "cm6gr9t4s0000jx5t8l8prvik"
  }
}
```
