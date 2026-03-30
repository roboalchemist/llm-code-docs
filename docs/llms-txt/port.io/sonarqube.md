# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/code-quality-security/sonarqube.md

# SonarQube

Loading version...

Port's SonarQube integration allows you to model SonarQube resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired SonarQube resources and their metadata in Port (see supported resources below).
* Watch for SonarQube object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from SonarQube into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Project`](https://next.sonarqube.com/sonarqube/web_api/api/projects/search) - represents a SonarQube project. Retrieves data from [`components`](https://next.sonarqube.com/sonarqube/web_api/api/components), [`measures`](https://next.sonarqube.com/sonarqube/web_api/api/measures), and [`branches`](https://next.sonarqube.com/sonarqube/web_api/api/project_branches).
* [`Issue`](https://next.sonarqube.com/sonarqube/web_api/api/issues) - represents a SonarQube issue
* `Saas Analysis` - represents analysis and latest activity in your SonarCloud environment.
* `On-premise Analysis` - since SonarQube doesn't offer a straightforward API for fetching analysis and latest activity in on-premise installations, Port's integration provides an alternative solution for on-premise installation.
  <br />
  <!-- -->
  By utilizing the [pull requests](https://next.sonarqube.com/sonarqube/web_api/api/project_pull_requests) and [measures](https://next.sonarqube.com/sonarqube/web_api/api/measures) APIs, you can now visualize the results of scan analyses for each pull request.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port
* Self-hosted
* CI

1. Go to the [SonarQube<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=SonarQube) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

  **Supported live event triggers (click to expand)**

  * Analysis completion events
  * Quality gate status change events

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

- Helm
- ArgoCD

<!-- -->

1. Go to the [Sonarqube<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Sonarqube) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Sonarqube<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Sonarqube<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Sonarqube<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Sonarqube
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

1. Create a `values.yaml` file in `argocd/my-ocean-sonarqube-integration` in your git repository with the content:

note

Remember to replace the placeholders for `MY_ORG_KEY`, `IS_ON_PREMISE`, and `MY_API_TOKEN`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-sonarqube-integration
  type: sonarqube
  eventListener:
    type: POLLING
  config:
    sonarOrganizationId: MY_ORG_KEY
    sonarIsOnPremise: IS_ON_PREMISE
  secrets:
    sonarApiToken: MY_API_TOKEN
```

<br />

2. Install the `my-ocean-sonarqube-integration` ArgoCD Application by creating the following `my-ocean-sonarqube-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

**ArgoCD Application (click to expand)**

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-sonarqube-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-sonarqube-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-sonarqube-integration/values.yaml
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
kubectl apply -f my-ocean-sonarqube-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                                | Description                                                                                                                                                                                  | Example                            | Required |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `port.clientId`                          | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                      |                                    | â       |
| `port.clientSecret`                      | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                  |                                    | â       |
| `port.baseUrl`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                            |                                    | â       |
| `integration.secrets.sonarApiToken`      | The [SonarQube API token](https://docs.sonarsource.com/sonarqube/9.8/user-guide/user-account/generating-and-using-tokens/#generating-a-token)                                                |                                    | â       |
| `integration.config.sonarOrganizationId` | The SonarQube [organization Key](https://docs.sonarsource.com/sonarcloud/appendices/project-information/#project-and-organization-keys) (Not required when using on-prem sonarqube instance) | myOrganization                     | â       |
| `integration.config.sonarIsOnPremise`    | A boolean value indicating whether the SonarQube instance is on-premise. The default value is `false`                                                                                        | false                              | â       |
| `liveEvents.baseUrl`                     | A URL bounded to the integration container that can be accessed by sonarqube. When used the integration will create webhooks on top of sonarqube to listen to any live changes in the data   | <https://my-ocean-integration.com> | â       |
| `integration.config.sonarUrl`            | Required if using **On-Prem**, Your SonarQube instance URL                                                                                                                                   | <https://my-sonar-instance.com>    | â       |
| `integration.secrets.webhookSecret`      | A secret token used to secure webhooks between SonarQube and the integration.                                                                                                                |                                    | â       |

**Advanced configuration**

| Parameter                        | Description                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `integration.eventListener.type` | The event listener type. `POLLING` (default) checks the config mapping periodically and triggers a resync if changes are detected. `KAFKA` and `WEBHOOK` enable real-time updates. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)                                                                                                        |
| `integration.type`               | The integration to be installed                                                                                                                                                                                                                                                                                                                                                         |
| `scheduledResyncInterval`        | The number of minutes between each full resync of all data from the third-party tool. When set, the integration will fetch fresh data at this interval regardless of config mapping changes. When not set, resyncs only occur when triggered by the event listener. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration) |
| `initializePortResources`        | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                                                                                                                                                          |
| `sendRawDataExamples`            | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                                                                                                                                                                                                                     |

<br />

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

This workflow/pipeline will run the SonarQube integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                           | Description                                                                                                                                                                                  | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN`       | The [SonarQube API token](https://docs.sonarsource.com/sonarqube/9.8/user-guide/user-account/generating-and-using-tokens/#generating-a-token)                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID` | The SonarQube [organization Key](https://docs.sonarsource.com/sonarcloud/appendices/project-information/#project-and-organization-keys) (Not required when using on-prem sonarqube instance) | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE`   | A boolean value indicating whether the SonarQube instance is on-premise. The default value is false                                                                                          | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_URL`             | Required if using **On-Prem**, Your SonarQube instance URL                                                                                                                                   | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                      | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                  | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | The identifier of the integration that will be installed                                                                                                                                     | â       |

<br />

Here is an example for `sonarqube-integration.yml` workflow file:

```
name: SonarQube Exporter Workflow

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
          type: 'sonarqube'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            sonar_api_token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN }}
            sonar_organization_id: ${{ secrets.OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID }}
            sonar_is_on_premise: ${{ secrets.OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE }}
            sonar_url: ${{ secrets.OCEAN__INTEGRATION__CONFIG__SONAR_URL }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                           | Description                                                                                                                                                                                  | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN`       | The [SonarQube API token](https://docs.sonarsource.com/sonarqube/9.8/user-guide/user-account/generating-and-using-tokens/#generating-a-token)                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID` | The SonarQube [organization Key](https://docs.sonarsource.com/sonarcloud/appendices/project-information/#project-and-organization-keys) (Not required when using on-prem sonarqube instance) | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE`   | A boolean value indicating whether the SonarQube instance is on-premise. The default value is false                                                                                          | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_URL`             | Required if using **On-Prem**, Your SonarQube instance URL                                                                                                                                   | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                      | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                  | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | The identifier of the integration that will be installed                                                                                                                                     | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run SonarQube Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID', variable: 'OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE', variable: 'OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="sonarqube"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN=$OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN \
                                -e OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID=$OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID \
                                -e OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE=$OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE \
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

| Parameter                                           | Description                                                                                                                                                                                  | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN`       | The [SonarQube API token](https://docs.sonarsource.com/sonarqube/9.8/user-guide/user-account/generating-and-using-tokens/#generating-a-token)                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID` | The SonarQube [organization Key](https://docs.sonarsource.com/sonarcloud/appendices/project-information/#project-and-organization-keys) (Not required when using on-prem sonarqube instance) | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE`   | A boolean value indicating whether the SonarQube instance is on-premise. The default value is false                                                                                          | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_URL`             | Required if using **On-Prem**, Your SonarQube instance URL                                                                                                                                   | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                      | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                  | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | The identifier of the integration that will be installed                                                                                                                                     | â       |

<br />

Here is an example for `sonar-integration.yml` pipeline file:

```
trigger:
- main

pool:
  vmImage: "ubuntu-latest"

variables:
  - group: port-ocean-credentials


steps:
- script: |
    echo Add other tasks to build, test, and deploy your project.
    # Set Docker image and run the container
    integration_type="sonarqube"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
    -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
    -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
    -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
    -e OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN=$(OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN) \
    -e OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID=$(OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID) \
    -e OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE=$(OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE) \
    -e OCEAN__INTEGRATION__CONFIG__SONAR_URL=$(OCEAN__INTEGRATION__CONFIG__SONAR_URL) \
    -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
    -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
    -e OCEAN__PORT__BASE_URL='https://api.port.io' \
    $image_name

    exit $?
  displayName: 'Ingest SonarQube Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                           | Description                                                                                                                                                                                  | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN`       | The [SonarQube API token](https://docs.sonarsource.com/sonarqube/9.8/user-guide/user-account/generating-and-using-tokens/#generating-a-token)                                                | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID` | The SonarQube [organization Key](https://docs.sonarsource.com/sonarcloud/appendices/project-information/#project-and-organization-keys) (Not required when using on-prem sonarqube instance) | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE`   | A boolean value indicating whether the SonarQube instance is on-premise. The default value is false                                                                                          | â       |
| `OCEAN__INTEGRATION__CONFIG__SONAR_URL`             | Required if using **On-Prem**, Your SonarQube instance URL                                                                                                                                   | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                      | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))                                  | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                            | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                          | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | The identifier of the integration that will be installed                                                                                                                                     | â       |

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
  INTEGRATION_TYPE: sonarqube
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
        -e OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN=$OCEAN__INTEGRATION__CONFIG__SONAR_API_TOKEN \
        -e OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID=$OCEAN__INTEGRATION__CONFIG__SONAR_ORGANIZATION_ID \
        -e OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE=$OCEAN__INTEGRATION__CONFIG__SONAR_IS_ON_PREMISE \
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
- kind: projects_ga
  selector:
    query: 'true'
    apiFilters:
      qualifier:
      - TRK
    metrics:
    - code_smells
    - coverage
    - bugs
    - vulnerabilities
    - duplicated_files
    - security_hotspots
    - new_violations
    - new_coverage
    - new_duplicated_lines_density
  port:
    entity:
      mappings:
        identifier: .key
        title: .name
        blueprint: '"sonarQubeProject"'
        properties:
          organization: .organization
          link: .__link
          qualityGateStatus: .__branch.status.qualityGateStatus
          lastAnalysisDate: .analysisDate
          numberOfBugs: .__measures[]? | select(.metric == "bugs") | .value
          numberOfCodeSmells: .__measures[]? | select(.metric == "code_smells") | .value
          numberOfVulnerabilities: .__measures[]? | select(.metric == "vulnerabilities") | .value
          numberOfHotSpots: .__measures[]? | select(.metric == "security_hotspots") | .value
          numberOfDuplications: .__measures[]? | select(.metric == "duplicated_files") | .value
          coverage: .__measures[]? | select(.metric == "coverage") | .value
          mainBranch: .__branch.name
          revision: .revision
          managed: .managed
        relations:
          group: '"all_teams"'
- kind: issues
  selector:
    query: 'true'
    apiFilters:
      resolved: 'false'
    projectApiFilters: {}
  port:
    entity:
      mappings:
        identifier: .key
        title: .message
        blueprint: '"sonarQubeIssue"'
        properties:
          type: .type
          severity: .severity
          link: .__link
          status: .status
          assignees: .assignee
          tags: .tags
          createdAt: .creationDate
        relations:
          sonarQubeProject: .project
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Examples of blueprints and the relevant integration configurations can be found on the sonarqube [examples page](/build-your-software-catalog/sync-data-to-catalog/code-quality-security/sonarqube/examples.md)

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from SonarQube when a code repository is scanned for quality assurance. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from SonarQube:

**Project response data (click to expand)**

```
{
  "organization": "peygis",
  "key": "PeyGis_Chatbot_For_Social_Media_Transaction",
  "name": "Chatbot_For_Social_Media_Transaction",
  "isFavorite": true,
  "visibility": "public",
  "eligibilityStatus": "COMPLETED",
  "eligible": true,
  "isNew": false,
  "lastAnalysisDate": "2017-03-02T15:21:47+0300",
  "revision": "7be96a94ac0c95a61ee6ee0ef9c6f808d386a355",
  "managed": false,
  "__measures": [
    {
      "metric": "bugs",
      "value": "6",
      "bestValue": false
    },
    {
      "metric": "code_smells",
      "value": "216",
      "bestValue": false
    },
    {
      "metric": "duplicated_files",
      "value": "2",
      "bestValue": false
    },
    {
      "metric": "vulnerabilities",
      "value": "1",
      "bestValue": false
    },
    {
      "metric": "security_hotspots",
      "value": "8",
      "bestValue": false
    }
  ],
  "__branch": {
    "name": "master",
    "isMain": true,
    "type": "LONG",
    "status": {
      "qualityGateStatus": "ERROR",
      "bugs": 6,
      "vulnerabilities": 1,
      "codeSmells": 216
    },
    "analysisDate": "2023-09-07T14:38:41+0200",
    "commit": {
      "sha": "5b01b6dcb200df0bfd1c66df65be30f9ea5423d8",
      "author": {
        "name": "Username",
        "login": "Username@github",
        "avatar": "9df2ac1caa70b0a67ff0561f7d0363e5"
      },
      "date": "2023-09-07T14:38:36+0200",
      "message": "Merge pull request #21 from PeyGis/test-sonar"
    }
  },
  "__link": "https://sonarcloud.io/project/overview?id=PeyGis_Chatbot_For_Social_Media_Transaction"
}
```

**Issue response data (click to expand)**

```
{
  "key": "AYhnRlhI0rLhE5EBPGHW",
  "rule": "xml:S1135",
  "severity": "INFO",
  "component": "PeyGis_Chatbot_For_Social_Media_Transaction:node_modules/json-schema/draft-zyp-json-schema-04.xml",
  "project": "PeyGis_Chatbot_For_Social_Media_Transaction",
  "line": 313,
  "hash": "8346d5371c3d1b0d1d57937c7b967090",
  "textRange": {
    "startLine": 313,
    "endLine": 313,
    "startOffset": 3,
    "endOffset": 56
  },
  "flows": [],
  "status": "OPEN",
  "message": "Complete the task associated to this \"TODO\" comment.",
  "effort": "0min",
  "debt": "0min",
  "assignee": "Username@github",
  "author": "email@gmail.com",
  "tags": [],
  "creationDate": "2018-04-06T02:44:46+0200",
  "updateDate": "2023-05-29T13:30:14+0200",
  "type": "CODE_SMELL",
  "organization": "peygis",
  "cleanCodeAttribute": "COMPLETE",
  "cleanCodeAttributeCategory": "INTENTIONAL",
  "impacts": [
    {
      "softwareQuality": "MAINTAINABILITY",
      "severity": "LOW"
    }
  ],
  "__link": "https://sonarcloud.io/project/issues?open=AYhnRlhI0rLhE5EBPGHW&id=PeyGis_Chatbot_For_Social_Media_Transaction"
}
```

**Analysis response data (click to expand)**

```
{
  "analysisId": "AYpvptJNv89mE9ClYP-q",
  "firstAnalysis": false,
  "measures": {
    "violations_added": "0",
    "violations_fixed": "0",
    "coverage_change": "0.0",
    "duplicated_lines_density_change": "0.0",
    "ncloc_change": "0"
  },
  "branch": {
    "analysisDate": "2023-09-07T12:38:41.279Z",
    "isMain": true,
    "name": "master",
    "commit": {
      "sha": "5b01b6dcb200df0bfd1c66df65be30f9ea5423d8",
      "author": {
        "avatar": "9df2ac1caa70b0a67ff0561f7d0363e5",
        "login": "Username@github",
        "name": "Username"
      },
      "date": "2023-09-07T12:38:36Z",
      "message": "Merge pull request #21 from PeyGis/test-sonar"
    },
    "type": "LONG",
    "status": {
      "qualityGateStatus": "ERROR"
    }
  },
  "__branchName": "master",
  "__analysisDate": "2023-09-07T12:38:41.279Z",
  "__commit": {
    "sha": "5b01b6dcb200df0bfd1c66df65be30f9ea5423d8",
    "author": {
      "avatar": "9df2ac1caa70b0a67ff0561f7d0363e5",
      "login": "Username@github",
      "name": "Username"
    },
    "date": "2023-09-07T12:38:36Z",
    "message": "Merge pull request #21 from PeyGis/test-sonar"
  },
  "__project": "PeyGis_Chatbot_For_Social_Media_Transaction"
}
```

**Portfolio response data (click to expand)**

```
{
  "key": "GetPort_SelfService",
  "name": "GetPort SelfService",
  "desc": "Test",
  "qualifier": "VW",
  "visibility": "public",
  "selectionMode": "NONE",
  "subViews": [
    {
      "key": "GetPort_SelfService_Second",
      "name": "GetPort SelfService Second",
      "qualifier": "SVW",
      "selectionMode": "NONE",
      "subViews": [
        {
          "key": "GetPort_SelfService_Third",
          "name": "GetPort SelfService Third",
          "qualifier": "SVW",
          "selectionMode": "NONE",
          "subViews": [],
          "referencedBy": []
        },
        {
          "key": "Port_Test",
          "name": "Port Test",
          "qualifier": "SVW",
          "selectionMode": "NONE",
          "subViews": [],
          "referencedBy": []
        }
      ],
      "referencedBy": []
    },
    {
      "key": "Python",
      "name": "Python",
      "qualifier": "SVW",
      "selectionMode": "NONE",
      "subViews": [
        {
          "key": "Time",
          "name": "Time",
          "qualifier": "SVW",
          "selectionMode": "NONE",
          "subViews": [
            {
              "key": "port_ayodeji",
              "name": "port-ayodeji",
              "qualifier": "SVW",
              "selectionMode": "NONE",
              "subViews": [
                {
                  "key": "port_ayodeji:REferenced",
                  "name": "REferenced",
                  "qualifier": "VW",
                  "visibility": "public",
                  "originalKey": "REferenced"
                }
              ],
              "referencedBy": []
            }
          ],
          "referencedBy": []
        }
      ],
      "referencedBy": []
    },
    {
      "key": "GetPort_SelfService:Authentication_Application",
      "name": "Authentication Application",
      "desc": "For auth services",
      "qualifier": "APP",
      "visibility": "private",
      "selectedBranches": [
        "main"
      ],
      "originalKey": "Authentication_Application"
    }
  ],
  "referencedBy": [
    {
      "key": "GetPort_SelfService:Authentication_Application",
      "name": "Authentication Application",
      "desc": "For auth services",
      "qualifier": "VW",
      "visibility": "private",
      "selectedBranches": [
        "main"
      ],
      "originalKey": "Authentication_Application"
    }
  ]
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

**Project entity in Port (click to expand)**

```
{
  "identifier": "PeyGis_Chatbot_For_Social_Media_Transaction",
  "title": "Chatbot_For_Social_Media_Transaction",
  "blueprint": "sonarQubeProject",
  "team": [],
  "properties": {
    "organization": "peygis",
    "link": "https://sonarcloud.io/project/overview?id=PeyGis_Chatbot_For_Social_Media_Transaction",
    "lastAnalysisDate": "2023-09-07T12:38:41.000Z",
    "numberOfBugs": 6,
    "numberOfCodeSmells": 216,
    "numberOfVulnerabilities": 1,
    "numberOfHotSpots": 8,
    "numberOfDuplications": 2,
    "mainBranch": "master",
    "mainBranchLastAnalysisDate": "2023-09-07T12:38:41.000Z",
    "revision": "7be96a94ac0c95a61ee6ee0ef9c6f808d386a355",
    "managed": true
  },
  "relations": {},
  "icon": "sonarqube"
}
```

**Issue entity in Port (click to expand)**

```
{
  "identifier": "AYhnRlhI0rLhE5EBPGHW",
  "title": "Complete the task associated to this \"TODO\" comment.",
  "blueprint": "sonarQubeIssue",
  "team": [],
  "properties": {
    "type": "CODE_SMELL",
    "severity": "INFO",
    "link": "https://sonarcloud.io/project/issues?open=AYhnRlhI0rLhE5EBPGHW&id=PeyGis_Chatbot_For_Social_Media_Transaction",
    "status": "OPEN",
    "assignees": "Username@github",
    "tags": [],
    "createdAt": "2018-04-06T00:44:46.000Z"
  },
  "relations": {
    "sonarQubeProject": "PeyGis_Chatbot_For_Social_Media_Transaction"
  },
  "icon": "sonarqube"
}
```

**Analysis entity in Port (click to expand)**

```
{
  "identifier": "AYpvptJNv89mE9ClYP-q",
  "title": "Merge pull request #21 from PeyGis/test-sonar",
  "blueprint": "sonarQubeAnalysis",
  "team": [],
  "properties": {
    "branch": "master",
    "fixedIssues": 0,
    "newIssues": 0,
    "coverage": 0,
    "duplications": 0,
    "createdAt": "2023-09-07T12:38:41.279Z"
  },
  "relations": {
    "sonarQubeProject": "PeyGis_Chatbot_For_Social_Media_Transaction"
  },
  "icon": "sonarqube"
}
```

**Portfolio entity in Port (click to expand)**

```
{
  "identifier": "GetPort_SelfService",
  "title": "GetPort SelfService",
  "blueprint": "sonarQubePortfolio",
  "properties": {
    "description": null,
    "visibility": "PUBLIC",
    "selectionMode": "NONE",
    "disabled": null
  },
  "relations": {
    "subPortfolios": [
      "GetPort_SelfService_Second",
      "Python"
    ],
    "referencedBy": [
      "GetPort_SelfService:Authentication_Application"
    ]
  }
}
```

## Migration from SonarQube integration version `<=0.1.121`[â](#migration-from-sonarqube-integration-version-01121 "Direct link to migration-from-sonarqube-integration-version-01121")

Versions prior to `v0.1.115` used SonarQube's internal API for components to retrieve projects. Since this API is internal and subject to change, it is not globally available and not recommended for new users.

To remedy this, we have switched to the globally available API for projects instead for new users of the SonarQube integration. This comes with a few changes that are listed below.

### Changes to the SonarQube integration[â](#changes-to-the-sonarqube-integration "Direct link to Changes to the SonarQube integration")

* The `project` kind is deprecated in support for the `projects_ga` kind. *Deprecation effective: 2024-02-23*

* Since the `tags` property is only available with the internal API, it will read `null` for existing users of the SonarQube integration.

* Minor but backwards compatible changes have been made to the `sonarQubeProject` blueprint:

Deprecation notice

SonarQube deprecated the `qualifiers` filter for the `projects_ga` kind. The `components/search` endpoint now defaults to returning only Projects (TRK qualifier), as described in [SonarQube's community forum](https://community.sonarsource.com/t/deprecation-of-api-endpoint-parameters-for-api-components-search-in-2-weeks/41318). *Effective: 2026-02-02*

**`<=v0.1.121` `sonarqubeProject` blueprint (click to expand)**

Create in Port

```
{
    "identifier": "sonarQubeProject",
    "title": "SonarQube Project",
    "icon": "sonarqube",
    "schema": {
      "properties": {
        "organization": {
          "type": "string",
          "title": "Organization",
          "icon": "TwoUsers"
        },
        "link": {
          "type": "string",
          "format": "url",
          "title": "Link",
          "icon": "Link"
        },
        "lastAnalysisDate": {
          "type": "string",
          "format": "date-time",
          "icon": "Clock",
          "title": "Last Analysis Date"
        },
        "qualityGateStatus": {
          "title": "Quality Gate Status",
          "type": "string",
          "enum": [
            "OK",
            "WARN",
            "ERROR"
          ],
          "enumColors": {
            "OK": "green",
            "WARN": "yellow",
            "ERROR": "red"
          }
        },
        "numberOfBugs": {
          "type": "number",
          "title": "Number Of Bugs"
        },
        "numberOfCodeSmells": {
          "type": "number",
          "title": "Number Of CodeSmells"
        },
        "numberOfVulnerabilities": {
          "type": "number",
          "title": "Number Of Vulnerabilities"
        },
        "numberOfHotSpots": {
          "type": "number",
          "title": "Number Of HotSpots"
        },
        "numberOfDuplications": {
          "type": "number",
          "title": "Number Of Duplications"
        },
        "coverage": {
          "type": "number",
          "title": "Coverage"
        },
        "mainBranch": {
          "type": "string",
          "icon": "Git",
          "title": "Main Branch"
        },
        "tags": {
          "type": "array",
          "title": "Tags"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {
      "criticalOpenIssues": {
        "title": "Number Of Open Critical Issues",
        "type": "number",
        "target": "sonarQubeIssue",
        "query": {
          "combinator": "and",
          "rules": [
            {
              "property": "status",
              "operator": "in",
              "value": ["OPEN", "REOPENED"]
            },
            {
              "property": "severity",
              "operator": "=",
              "value": "CRITICAL"
            }
          ]
        },
        "calculationSpec": {
          "calculationBy": "entities",
          "func": "count"
        }
      },
      "numberOfOpenIssues": {
        "title": "Number Of Open Issues",
        "type": "number",
        "target": "sonarQubeIssue",
        "query": {
          "combinator": "and",
          "rules": [
            {
              "property": "status",
              "operator": "in",
              "value": [
                "OPEN",
                "REOPENED"
              ]
            }
          ]
        },
        "calculationSpec": {
          "calculationBy": "entities",
          "func": "count"
        }
      }
    },
    "relations": {}
  }
```

**`>=v0.1.115` `sonarqubeProject` blueprint (click to expand)**

Create in Port

```
{
    "identifier": "sonarQubeProject",
    "title": "SonarQube Project",
    "icon": "sonarqube",
    "schema": {
      "properties": {
        "organization": {
          "type": "string",
          "title": "Organization",
          "icon": "TwoUsers"
        },
        "link": {
          "type": "string",
          "format": "url",
          "title": "Link",
          "icon": "Link"
        },
        "lastAnalysisDate": {
          "type": "string",
          "format": "date-time",
          "icon": "Clock",
          "title": "Last Analysis Date"
        },
        "qualityGateStatus": {
          "title": "Quality Gate Status",
          "type": "string",
          "enum": [
            "OK",
            "WARN",
            "ERROR"
          ],
          "enumColors": {
            "OK": "green",
            "WARN": "yellow",
            "ERROR": "red"
          }
        },
        "numberOfBugs": {
          "type": "number",
          "title": "Number Of Bugs"
        },
        "numberOfCodeSmells": {
          "type": "number",
          "title": "Number Of CodeSmells"
        },
        "numberOfVulnerabilities": {
          "type": "number",
          "title": "Number Of Vulnerabilities"
        },
        "numberOfHotSpots": {
          "type": "number",
          "title": "Number Of HotSpots"
        },
        "numberOfDuplications": {
          "type": "number",
          "title": "Number Of Duplications"
        },
        "coverage": {
          "type": "number",
          "title": "Coverage"
        },
        "mainBranch": {
          "type": "string",
          "icon": "Git",
          "title": "Main Branch"
        },
        "mainBranchLastAnalysisDate": {
          "type": "string",
          "format": "date-time",
          "icon": "Clock",
          "title": "Main Branch Last Analysis Date"
        },
        "revision": {
          "type": "string",
          "title": "Revision"
        },
        "managed": {
          "type": "boolean",
          "title": "Managed"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {
      "criticalOpenIssues": {
        "title": "Number Of Open Critical Issues",
        "type": "number",
        "target": "sonarQubeIssue",
        "query": {
          "combinator": "and",
          "rules": [
            {
              "property": "status",
              "operator": "in",
              "value": ["OPEN", "REOPENED"]
            },
            {
              "property": "severity",
              "operator": "=",
              "value": "CRITICAL"
            }
          ]
        },
        "calculationSpec": {
          "calculationBy": "entities",
          "func": "count"
        }
      },
      "numberOfOpenIssues": {
        "title": "Number Of Open Issues",
        "type": "number",
        "target": "sonarQubeIssue",
        "query": {
          "combinator": "and",
          "rules": [
            {
              "property": "status",
              "operator": "in",
              "value": [
                "OPEN",
                "REOPENED"
              ]
            }
          ]
        },
        "calculationSpec": {
          "calculationBy": "entities",
          "func": "count"
        }
      }
    },
    "relations": {}
  }
```

* If you however, choose to stick with the internal API with the `project` kind, use any of the blueprints with the following mapping:

**Project mapping for `project` kind(click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: projects
    selector:
      query: 'true'
      apiFilters:
        filter:
          qualifier: TRK
      metrics:
        - code_smells
        - coverage
        - bugs
        - vulnerabilities
        - duplicated_files
        - security_hotspots
        - new_violations
        - new_coverage
        - new_duplicated_lines_density
    port:
      entity:
        mappings:
          blueprint: '"sonarQubeProject"' # or any other blueprint you decide to use
          identifier: .key
          title: .name
          properties:
            organization: .organization
            link: .__link
            qualityGateStatus: .__branch.status.qualityGateStatus
            lastAnalysisDate: .__branch.analysisDate
            numberOfBugs: .__measures[]? | select(.metric == "bugs") | .value
            numberOfCodeSmells: .__measures[]? | select(.metric == "code_smells") | .value
            numberOfVulnerabilities: .__measures[]? | select(.metric == "vulnerabilities") | .value
            numberOfHotSpots: .__measures[]? | select(.metric == "security_hotspots") | .value
            numberOfDuplications: .__measures[]? | select(.metric == "duplicated_files") | .value
            coverage: .__measures[]? | select(.metric == "coverage") | .value
            mainBranch: .__branch.name
            tags: .tags
```

## Alternative installation via webhook[â](#alternative-installation-via-webhook "Direct link to Alternative installation via webhook")

While the Ocean integration described above is the recommended installation method, you may prefer to use a webhook to ingest data from SonarQube. If so, use the following instructions:

****Webhook installation (click to expand)** (click to expand)**

In this example you are going to create a webhook integration between [SonarQube's SonarCloud](https://www.sonarsource.com/products/sonarcloud/) and Port, which will ingest SonarQube code quality `analysis` entities.

## Port configuration

Create the following blueprint definition:

**SonarQube analysis blueprint (click to expand)**

Create in Port

```
{
  "identifier": "sonarCloudAnalysis",
  "description": "This blueprint represents a SonarCloud Analysis in our software catalog",
  "title": "SonarCloud Analysis",
  "icon": "sonarqube",
  "schema": {
    "properties": {
      "serverUrl": {
        "type": "string",
        "format": "url",
        "title": "Server URL"
      },
      "projectName": {
        "type": "string",
        "title": "Project name"
      },
      "projectUrl": {
        "type": "string",
        "format": "url",
        "title": "Project URL"
      },
      "branchName": {
        "type": "string",
        "title": "Branch Name"
      },
      "branchType": {
        "type": "string",
        "title": "Branch Type"
      },
      "branchUrl": {
        "type": "string",
        "format": "url",
        "title": "Branch URL"
      },
      "qualityGateName": {
        "type": "string",
        "title": "Quality Gate Name"
      },
      "qualityGateStatus": {
        "type": "string",
        "title": "Quality Gate Status",
        "description": "General status of quality checks"
      },
      "qualityGateConditions": {
        "type": "array",
        "items": {
          "type": "object"
        },
        "title": "Quality Gate Conditions",
        "description": "Conditions of the qaulity gate"
      },
      "status": {
        "type": "string",
        "title": "General Status"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints):

**SonarQube analysis webhook configuration (click to expand)**

1. **Basic details** tab - fill the following details:

   1. Title : `SonarQube mapper`;
   2. Identifier : `sonarqube_mapper`;
   3. Description : `A webhook configuration to map SonarQube alerts to Port`;
   4. Icon : `sonarqube`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "sonarCloudAnalysis",
       "entity": {
         "identifier": ".body.taskId",
         "title": ".body.project.name + \"-\" + .body.taskId",
         "properties": {
           "serverUrl": ".body.serverUrl",
           "status": ".body.status",
           "projectName": ".body.project.name",
           "projectUrl": ".body.project.url",
           "branchName": ".body.branch.name",
           "branchType": ".body.branch.type",
           "branchUrl": ".body.branch.url",
           "qualityGateName": ".body.qualityGate.name",
           "qualityGateStatus": ".body.qualityGate.status",
           "qualityGateConditions": ".body.qualityGate.conditions"
         }
       }
     }
   ]
   ```

3. Scroll down to **Advanced settings** and input the following details:

   1. secret: `WEBHOOK_SECRET`;
   2. Signature Header Name : `x-sonar-webhook-hmac-sha256`;
   3. Signature Algorithm : Select `sha256` from dropdown option;
   4. Click **Save** at the bottom of the page.

   Remember to replace the `WEBHOOK_SECRET` with the real secret you specify when creating the webhook in SonarCloud.

## Create a webhook in SonarCloud

1. Go to [SonarCloud](https://sonarcloud.io/projects) and select a project you want to configure a webhook for;

2. Click on **Administration** at the bottom left of the page and select **Webhooks**;

3. Click on **Create**

4. Input the following details:

   <!-- -->

   1. `Name` - use a meaningful name such as Port Webhook;
   2. `URL` - enter the value of the `url` key you received after creating the webhook configuration;
   3. `Secret` - enter the secret value you specified when creating the webhook;

5. Click **Create** at the bottom of the page.

tip

In order to view the different payloads and events available in SonarQube webhooks, [look here](https://docs.sonarqube.org/latest/project-administration/webhooks/)

Done! any new analysis you run (for example, on new PRs or changes to PRs) will trigger a webhook event that SonarCloud will send to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Let's Test It

This section includes a sample webhook event sent from SonarQube when a code repository is scanned for quality assurance. In addition, it includes the entity created from the event based on the webhook configuration provided in the previous section.

### Payload

Here is an example of the payload structure sent to the webhook URL when a SonarQube repository is scanned:

**Webhook event payload (click to expand)**

```
{
  "serverUrl": "https://sonarcloud.io",
  "taskId": "AYi_1w1fcGD_RU1S5-r_",
  "status": "SUCCESS",
  "analysedAt": "2023-06-15T16:15:05+0000",
  "revision": "575718d8287cd09630ff0ff9aa4bb8570ea4ef29",
  "changedAt": "2023-06-15T16:15:05+0000",
  "project": {
    "key": "Username_Test_Python_App",
    "name": "Test_Python_App",
    "url": "https://sonarcloud.io/dashboard?id=Username_Test_Python_App"
  },
  "branch": {
    "name": "master",
    "type": "LONG",
    "isMain": true,
    "url": "https://sonarcloud.io/dashboard?id=Username_Test_Python_App"
  },
  "qualityGate": {
    "name": "My Quality Gate",
    "status": "ERROR",
    "conditions": [
      {
        "metric": "code_smells",
        "operator": "GREATER_THAN",
        "value": "217",
        "status": "ERROR",
        "errorThreshold": "5"
      },
      {
        "metric": "ncloc",
        "operator": "GREATER_THAN",
        "value": "8435",
        "status": "ERROR",
        "errorThreshold": "20"
      },
      {
        "metric": "new_branch_coverage",
        "operator": "LESS_THAN",
        "status": "NO_VALUE",
        "errorThreshold": "1"
      },
      {
        "metric": "new_sqale_debt_ratio",
        "operator": "GREATER_THAN",
        "value": "1.0303030303030303",
        "status": "OK",
        "errorThreshold": "5"
      },
      {
        "metric": "new_violations",
        "operator": "GREATER_THAN",
        "value": "3",
        "status": "ERROR",
        "errorThreshold": "1"
      }
    ]
  },
  "properties": {}
}
```

### Mapping Result

The combination of the sample payload and the webhook configuration generates the following Port entity:

```
{
  "identifier": "AYi_1w1fcGD_RU1S5-r_",
  "title": "Test_Python_App-AYi_1w1fcGD_RU1S5-r_",
  "blueprint": "sonarCloudAnalysis",
  "properties": {
    "serverUrl": "https://sonarcloud.io",
    "status": "SUCCESS",
    "projectName": "Test_Python_App",
    "projectUrl": "https://sonarcloud.io/dashboard?id=Username_Test_Python_App",
    "branchName": "master",
    "branchType": "LONG",
    "branchUrl": "https://sonarcloud.io/dashboard?id=Username_Test_Python_App",
    "qualityGateName": "My Quality Gate",
    "qualityGateStatus": "ERROR",
    "qualityGateConditions": [
      {
        "metric": "code_smells",
        "operator": "GREATER_THAN",
        "value": "217",
        "status": "ERROR",
        "errorThreshold": "5"
      },
      {
        "metric": "ncloc",
        "operator": "GREATER_THAN",
        "value": "8435",
        "status": "ERROR",
        "errorThreshold": "20"
      },
      {
        "metric": "new_branch_coverage",
        "operator": "LESS_THAN",
        "status": "NO_VALUE",
        "errorThreshold": "1"
      },
      {
        "metric": "new_sqale_debt_ratio",
        "operator": "GREATER_THAN",
        "value": "1.0303030303030303",
        "status": "OK",
        "errorThreshold": "5"
      },
      {
        "metric": "new_violations",
        "operator": "GREATER_THAN",
        "value": "3",
        "status": "ERROR",
        "errorThreshold": "1"
      }
    ]
  },
  "relations": {}
}
```
