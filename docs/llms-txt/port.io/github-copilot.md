# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/ai-agents/github-copilot.md

# GitHub Copilot

Loading version...

Deprecation Notice: Team Metrics

GitHub is sunsetting the legacy Copilot Metrics API on **April 2, 2026**.

* The `copilot-team-metrics` resource will stop functioning after this date.
* Team-level metrics are **not supported** in the new GitHub API. Users are advised to migrate to **Organization-level** metrics using the instructions below.

Port's Github Copilot integration allows you to ingest your Github Copilot usage metrics into your software catalog.

## Supported aggregation hierarchies[â](#supported-aggregation-hierarchies "Direct link to Supported aggregation hierarchies")

Some aggregation hierarchies of Github Copilot usage metrics can be ingested into Port, they are listed below.<br /><!-- -->It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [organization-usage-metrics (new API)](https://docs.github.com/en/rest/copilot/copilot-usage-metrics) - **Recommended**
* [copilot-organization-metrics (sunset)](https://docs.github.com/en/rest/copilot/copilot-metrics?apiVersion=2022-11-28#get-copilot-metrics-for-an-organization) - *Sunsetting April 2026*
* [copilot-team-metrics (sunset)](https://docs.github.com/en/rest/copilot/copilot-metrics?apiVersion=2022-11-28#get-copilot-metrics-for-a-team) - *Sunsetting April 2026*

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [Github Copilot<!-- --> data source page](<https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Github Copilot>) in your portal.

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

1. Go to the [Github Copilot<!-- --> data source page](<https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Github Copilot>) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Github Copilot<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Github Copilot<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Github Copilot<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Github Copilot
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

1. Create a `values.yaml` file in `argocd/my-ocean-github-copilot-integration` in your git repository with the content:

note

Remember to replace the placeholder for `GITHUB_TOKEN`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-github-copilot-integration
  type: github-copilot
  eventListener:
    type: POLLING
  secrets:
    githubToken: GITHUB_TOKEN
```

<br />

1. Install the `my-ocean-github-copilot-integration` ArgoCD Application by creating the following `my-ocean-github-copilot-integration.yaml` manifest:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.<br /><!-- -->Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-github-copilot-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-github-copilot-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-github-copilot-integration/values.yaml
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
kubectl apply -f my-ocean-github-copilot-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                         | Description                                                                                                                                                                                                                                   | Example                  | Required |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | -------- |
| `port.clientId`                   | Your port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                    |                          | â       |
| `port.clientSecret`               | Your port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                |                          | â       |
| `port.baseUrl`                    | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                                                                             |                          | â       |
| `integration.secrets.githubToken` | Github [token](https://github.com/settings/tokens/new) used to query Github api                                                                                                                                                               |                          | â       |
| `integration.config.githubHost`   | The host of the Github api instance                                                                                                                                                                                                           | <https://api.github.com> | â       |
| `integration.eventListener.type`  | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)                                                                                                                        |                          | â       |
| `integration.type`                | The integration to be installed                                                                                                                                                                                                               |                          | â       |
| `scheduledResyncInterval`         | The number of minutes between each resync. When not set the integration will resync for each event listener resync event. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration) |                          | â       |
| `initializePortResources`         | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                |                          | â       |
| `sendRawDataExamples`             | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                                                                           |                          | â       |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

This workflow/pipeline will run the Github Copilot integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                   | Description                                                                                                                                                 | Example | Required |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `port_client_id`            | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `port_client_secret`        | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `port_base_url`             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `config -> githubToken`     | Github [token](https://github.com/settings/tokens/new) used to query Github api                                                                             |         | â       |
| `initialize_port_resources` | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `identifier`                | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `version`                   | The version of the integration that will be installed                                                                                                       | latest  | â       |
| `sendRawDataExamples`       | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | true    |          |

<br />

Ocean Sail Github Action

The following example uses the **Ocean Sail** Github Action to run the Github Copilot integration. For further information about the action, please visit the [Ocean Sail Github Action](https://github.com/marketplace/actions/ocean-sail)

<br />

Here is an example for `github-copilot-integration.yml` workflow file:

```
name: Github Copilot Exporter Workflow

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
          type: 'github-copilot'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            githubToken: ${{ secrets.OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN }}
```

Tip for Jenkins agent

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                  | Description                                                                                                                                                 | Example | Required |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN` | Github token used to query Github api (Classic token only)                                                                                                  |         | â       |
| `OCEAN__PORT__CLIENT_ID`                   | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`               | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                    | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`         | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`           | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`            | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Github Copilot Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="github-copilot"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN=$OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN \
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

| Parameter                                  | Description                                                                                                                                                 | Example | Required |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN` | Github token used to query Github api (Classic token only)                                                                                                  |         | â       |
| `OCEAN__PORT__CLIENT_ID`                   | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`               | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                    | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`         | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`           | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`            | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |

<br />

Here is an example for `github-copilot-integration.yml` pipeline file:

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
      integration_type="github-copilot"
      version="latest"

      image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

      docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN=$(OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

      exit $?
    displayName: "Ingest Data into Port"
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                  | Description                                                                                                                                                 | Example | Required |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN` | Github token used to query Github api (Classic token only)                                                                                                  |         | â       |
| `OCEAN__PORT__CLIENT_ID`                   | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`               | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                    | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`         | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`           | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`            | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |

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
  INTEGRATION_TYPE: github-copilot
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
        -e OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN=$OCEAN__INTEGRATION__CONFIG__GITHUB_TOKEN \
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
entityDeletionThreshold: 0
resources:
- kind: copilot-team-metrics
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: (.__team.slug + "@" + .date)
        title: (.__team.slug + " copilot-metrics " + .date)
        blueprint: '"github_copilot_usage"'
        properties:
          record_date: .date  + "T00:00:00Z"
          breakdown: .
          total_suggestions_count: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_suggestions] | map(select(. != null) ) | add'
          total_acceptances_count: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_acceptances] | map(select(. != null)) | add'
          total_lines_suggested: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_suggested] | map(select(. != null)) | add'
          total_lines_accepted: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_accepted] | map(select(. != null)) | add'
          total_active_users: .total_active_users
          total_chat_acceptances: |-
            [
              (.copilot_ide_chat.editors[]?.models[]?.total_chat_copy_events // 0),
              (.copilot_ide_chat.editors[]?.models[]?.total_chat_insertion_events // 0)
            ] | map(select(. != null)) | add
          total_chat_turns: '[.copilot_ide_chat.editors[]?.models[]?.total_chats // 0] | map(select(. != null)) | add'
          total_active_chat_users: '[.copilot_ide_chat.editors[]?.total_engaged_users // 0] | map(select(. != null)) | add'
          git_hub_org: .__organization.login
          git_hub_team: .__team.slug
- kind: copilot-organization-metrics
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: (.__organization.login + "@" + .date)
        title: (.__organization.login + " copilot-metrics " + .date)
        blueprint: '"github_copilot_usage"'
        properties:
          record_date: .date  + "T00:00:00Z"
          breakdown: .
          total_suggestions_count: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_suggestions] | map(select(. != null) ) | add'
          total_acceptances_count: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_acceptances] | map(select(. != null)) | add'
          total_lines_suggested: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_suggested] | map(select(. != null)) | add'
          total_lines_accepted: '[.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_accepted] | map(select(. != null)) | add'
          total_active_users: .total_active_users
          total_chat_acceptances: |-
            [
              (.copilot_ide_chat.editors[]?.models[]?.total_chat_copy_events // 0),
              (.copilot_ide_chat.editors[]?.models[]?.total_chat_insertion_events // 0)
            ] | map(select(. != null)) | add
          total_chat_turns: '[.copilot_ide_chat.editors[]?.models[]?.total_chats // 0] | map(select(. != null)) | add'
          total_active_chat_users: '[.copilot_ide_chat.editors[]?.total_engaged_users // 0] | map(select(. != null)) | add'
          git_hub_org: .__organization.login
- kind: organization-usage-metrics
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: (.__organization.login + "@" + .day)
          title: (.__organization.login + " copilot-metrics " + .day)
          blueprint: '"githubCopilotOrganizationUsage"'
          properties:
            record_date: .day + "T00:00:00Z"
            daily_active_users: .daily_active_users
            code_generation_activity_count: .code_generation_activity_count
            code_acceptance_activity_count: .code_acceptance_activity_count
            loc_suggested_to_add_sum: .loc_suggested_to_add_sum
            loc_added_sum: .loc_added_sum
            user_initiated_interaction_count: .user_initiated_interaction_count
            git_hub_org: .__organization.login
```

## Permissions[â](#permissions "Direct link to Permissions")

Port's Github Copilot integration requires a classic Github token **generated by organization owners or parent enterprise owners and billing managers** with at least one of the following scopes to be enabled:

* `manage_billing:copilot`.
* `read:org`.
* `read:enterprise`.

In addition, the Copilot Metrics API access policy must be enabled for the organization within GitHub settings.

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources).<br /><!-- -->Find the integration in the list of data sources and click on it to open the playground.

GitHub Copilot Usage Blueprint (Sunset) (click to expand)

Create in Port

```
{
    "identifier": "github_copilot_usage",
    "title": "GitHub Copilot Usage",
    "icon": "Github",
    "schema": {
      "properties": {
        "record_date": {
          "type": "string",
          "title": "Record Date",
          "format": "date-time"
        },
        "breakdown": {
          "type": "object",
          "title": "Breakdown"
        },
        "total_suggestions_count": {
          "type": "number",
          "title": "Total Suggestions Count"
        },
        "total_acceptances_count": {
          "type": "number",
          "title": "Total Acceptances Count"
        },
        "total_lines_suggested": {
          "type": "number",
          "title": "Total Lines Suggested"
        },
        "total_lines_accepted": {
          "type": "number",
          "title": "Total Lines Accepted"
        },
        "total_active_users": {
          "type": "number",
          "title": "Total Active Users"
        },
        "total_chat_acceptances": {
          "type": "number",
          "title": "Total Chat Acceptances"
        },
        "total_chat_turns": {
          "type": "number",
          "title": "Total Chat Turns"
        },
        "total_active_chat_users": {
          "type": "number",
          "title": "Total Active Chat Users"
        },
        "git_hub_org": {
          "type": "string",
          "title": "GitHub Org"
        },
        "git_hub_team": {
          "type": "string",
          "title": "GitHub Team"
        }
      },
      "required": []
    },
    "calculationProperties": {
      "acceptance_rate": {
        "title": "Acceptance Rate",
        "icon": "DefaultProperty",
        "calculation": "if (.properties.total_suggestions_count == 0)  then 0  else    ((.properties.total_acceptances_count / .properties.total_suggestions_count) * 100     | round)  end",
        "type": "number"
      }
    },
    "relations": {}
  }
```

## Team hierarchy metrics (sunset - April 2026)[â](#team-hierarchy-metrics-sunset---april-2026 "Direct link to Team hierarchy metrics (sunset - April 2026)")

Integration configuration (click to expand)

```
entityDeletionThreshold: 0
resources:
  - kind: copilot-team-metrics
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: (.__team.slug + "@" + .date)
          title: (.__team.slug + " copilot-metrics " + .date)
          blueprint: '"github_copilot_usage"'
          properties:
            record_date: .date  + "T00:00:00Z"
            breakdown: .
            total_suggestions_count: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_suggestions]
              | map(select(. != null) ) | add
            total_acceptances_count: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_acceptances]
              | map(select(. != null)) | add
            total_lines_suggested: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_suggested]
              | map(select(. != null)) | add
            total_lines_accepted: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_accepted]
              | map(select(. != null)) | add
            total_active_users: .total_active_users
            total_chat_acceptances: >-
              [
                (.copilot_ide_chat.editors[]?.models[]?.total_chat_copy_events // 0),
                (.copilot_ide_chat.editors[]?.models[]?.total_chat_insertion_events // 0)
              ]
              | map(select(. != null)) | add
            total_chat_turns: >-
              [.copilot_ide_chat.editors[]?.models[]?.total_chats // 0]
              | map(select(. != null)) | add
            total_active_chat_users: >-
              [.copilot_ide_chat.editors[]?.total_engaged_users // 0]
              | map(select(. != null)) | add
            git_hub_org: .__organization.login
            git_hub_team: .__team.slug
```

## Organization hierarchy metrics (deprecated)[â](#organization-hierarchy-metrics-deprecated "Direct link to Organization hierarchy metrics (deprecated)")

Integration configuration (click to expand)

```
entityDeletionThreshold: 0
resources:
  - kind: copilot-organization-metrics
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: (.__organization.login + "@" + .date)
          title: (.__organization.login + " copilot-metrics " + .date)
          blueprint: '"github_copilot_usage"'
          properties:
            record_date: .date  + "T00:00:00Z"
            breakdown: .
            total_suggestions_count: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_suggestions]
              | map(select(. != null) ) | add
            total_acceptances_count: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_acceptances]
              | map(select(. != null)) | add
            total_lines_suggested: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_suggested]
              | map(select(. != null)) | add
            total_lines_accepted: >-
              [.copilot_ide_code_completions.editors[]?.models[]?.languages[]?.total_code_lines_accepted]
              | map(select(. != null)) | add
            total_active_users: .total_active_users
            total_chat_acceptances: >-
              [
                (.copilot_ide_chat.editors[]?.models[]?.total_chat_copy_events // 0),
                (.copilot_ide_chat.editors[]?.models[]?.total_chat_insertion_events // 0)
              ]
              | map(select(. != null)) | add
            total_chat_turns: >-
              [.copilot_ide_chat.editors[]?.models[]?.total_chats // 0]
              | map(select(. != null)) | add
            total_active_chat_users: >-
              [.copilot_ide_chat.editors[]?.total_engaged_users // 0]
              | map(select(. != null)) | add
            git_hub_org: .__organization.login
```

## Organization usage metrics[â](#organization-usage-metrics "Direct link to Organization usage metrics")

GitHub Copilot Organization Usage Blueprint

Create in Port

```
  {
    "identifier": "githubCopilotOrganizationUsage",
    "title": "GitHub Copilot Organization Usage",
    "icon": "Github",
    "schema": {
      "properties": {
        "record_date": {
          "type": "string",
          "title": "Record Date",
          "format": "date-time"
        },
        "daily_active_users": {
          "type": "number",
          "title": "Daily Active Users"
        },
        "code_generation_activity_count": {
          "type": "number",
          "title": "Code Generation Activity Count"
        },
        "code_acceptance_activity_count": {
          "type": "number",
          "title": "Code Acceptance Activity Count"
        },
        "loc_suggested_to_add_sum": {
          "type": "number",
          "title": "LOC Suggested To Add"
        },
        "loc_added_sum": {
          "type": "number",
          "title": "LOC Added"
        },
        "user_initiated_interaction_count": {
          "type": "number",
          "title": "User Initiated Interaction Count"
        },
        "git_hub_org": {
          "type": "string",
          "title": "GitHub Org"
        }
      },
      "required": []
    },
    "calculationProperties": {
      "acceptance_rate": {
        "title": "Acceptance Rate",
        "icon": "DefaultProperty",
        "calculation": "if (.properties.code_generation_activity_count == 0) then 0 else ((.properties.code_acceptance_activity_count / .properties.code_generation_activity_count) * 100 | round) end",
        "type": "number"
      }
    }
  }
```

Integration configuration (click to expand)

```
entityDeletionThreshold: 0
resources:
  - kind: organization-usage-metrics
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: (.__organization.login + "@" + .day)
          title: (.__organization.login + " copilot-metrics " + .day)
          blueprint: '"githubCopilotOrganizationUsage"'
          properties:
            record_date: .day + "T00:00:00Z"
            daily_active_users: .daily_active_users
            code_generation_activity_count: .code_generation_activity_count
            code_acceptance_activity_count: .code_acceptance_activity_count
            loc_suggested_to_add_sum: .loc_suggested_to_add_sum
            loc_added_sum: .loc_added_sum
            user_initiated_interaction_count: .user_initiated_interaction_count
            git_hub_org: .__organization.login
```

## Related guide[â](#related-guide "Direct link to Related guide")

[Visualize GitHub Copilot metrics](/guides/all/visualize-github-copilot-metrics.md)
