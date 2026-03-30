# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cicd/jenkins.md

# Jenkins

Loading version...

Port's Jenkins integration allows you to model Jenkins resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Jenkins resources and their metadata in Port (see supported resources below).
* Watch for Jenkins object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

* `job` - (`<your-jenkins-host>/api/json`)
* `build` - (`<your-jenkins-host>/api/json`)
* `user` - (`<your-jenkins-host>/people/api/json`)

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Generate Jenkins API Token[â](#generate-jenkins-api-token "Direct link to Generate Jenkins API Token")

To generate a token for authenticating the Jenkins API calls:

1. In the Jenkins banner frame, click your user name to open the user menu.
2. Navigate to your **Username** > **Configure** > **API Token**.
3. Click Add new Token.
4. Click Generate.
5. Copy the API token that is generated to use as the `JENKINS_TOKEN`.

![](/img/build-your-software-catalog/sync-data-to-catalog/jenkins/configure-api-token.png)

### Install Required Plugins[â](#install-required-plugins "Direct link to Install Required Plugins")

To ensure full functionality of the Jenkins integration, please install the following plugins:

1. **People View Plugin**: Required for user information API (for Jenkins versions 2.452 and above)

   * Navigate to **Manage Jenkins** -> **Plugins**
   * Search for and install the [**"People View"** plugin](https://plugins.jenkins.io/people-view/)

2. **Pipeline: Stage View Plugin**: Required for fetching stages data

   * Navigate to **Manage Jenkins** -> **Plugins**
   * Search for and install the [**"Pipeline: Stage View"** plugin](https://plugins.jenkins.io/pipeline-stage-view/)

These plugins are essential for the integration to access user information and pipeline stage data.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port
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

1. Go to the [Jenkins<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Jenkins) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Jenkins<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Jenkins<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Jenkins<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Jenkins
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

1. Create a `values.yaml` file in `argocd/my-ocean-jenkins-integration` in your git repository with the content:

note

Remember to replace the placeholders for `JENKINS_USER`, `JENKINS_TOKEN` and `JENKINS_HOST`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-jenkins-integration
  type: jenkins
  eventListener:
    type: POLLING
  config:
    jenkinsHost: JENKINS_HOST
  secrets:
    jenkinsUser: JENKINS_USER
    jenkinsToken: JENKINS_TOKEN
```

<br />

2. Install the `my-ocean-jenkins-integration` ArgoCD Application by creating the following `my-ocean-jenkins-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-jenkins-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-jenkins-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-jenkins-integration/values.yaml
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
kubectl apply -f my-ocean-jenkins-integration.yaml
```

This table summarizes the available parameters for the installation.<br /><!-- -->Note the parameters specific to this integration, they are last in the table.

| Parameter                          | Description                                                                                                                                          | Required |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                    | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `port.clientSecret`                | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `port.baseUrl`                     | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |
| `integration.identifier`           | Change the identifier to describe your integration                                                                                                   | â       |
| `integration.type`                 | The integration type                                                                                                                                 | â       |
| `integration.eventListener.type`   | The event listener type                                                                                                                              | â       |
| `integration.config.appHost`       | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Jenkins                                | â       |
| `scheduledResyncInterval`          | The number of minutes between each resync                                                                                                            | â       |
| `initializePortResources`          | Default true, When set to true the integration will create default blueprints and the port App config Mapping                                        | â       |
| `sendRawDataExamples`              | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `integration.secrets.jenkinsUser`  | The Jenkins username                                                                                                                                 | â       |
| `integration.secrets.jenkinsToken` | The Jenkins password or token                                                                                                                        | â       |
| `integration.config.jenkinsHost`   | The Jenkins host                                                                                                                                     | â       |

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

This workflow/pipeline will run the Jenkins integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                   | Description                                                                                                                                          | Required |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_USER`  | The Jenkins Username                                                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN` | The Jenkins Token                                                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_HOST`  | The Jenkins Host                                                                                                                                     | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`          | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`             | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`            | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                    | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                     | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

<br />

Here is an example for `jenkins-integration.yml` workflow file:

```
name: Jenkins Exporter Workflow

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
          type: 'jenkins'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            jenkins_host: ${{ secrets.OCEAN__INTEGRATION__CONFIG__JENKINS_HOST }}
            jenkins_user: ${{ secrets.OCEAN__INTEGRATION__CONFIG__JENKINS_USER }}
            jenkins_token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                   | Description                                                                                                                                          | Required |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_USER`  | The Jenkins Username                                                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN` | The Jenkins Token                                                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_HOST`  | The Jenkins Host                                                                                                                                     | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`          | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`             | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`            | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                    | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                     | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Jenkins Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__JENKINS_USER', variable: 'OCEAN__INTEGRATION__CONFIG__JENKINS_USER'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__JENKINS_HOST', variable: 'OCEAN__INTEGRATION__CONFIG__JENKINS_HOST'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="jenkins"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__JENKINS_USER=$OCEAN__INTEGRATION__CONFIG__JENKINS_USER \
                                -e OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN=$OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN \
                                -e OCEAN__INTEGRATION__CONFIG__JENKINS_HOST=$OCEAN__INTEGRATION__CONFIG__JENKINS_HOST \
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

| Parameter                                   | Description                                                                                                                                          | Required |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_USER`  | The Jenkins Username                                                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN` | The Jenkins Token                                                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_HOST`  | The Jenkins Host                                                                                                                                     | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`          | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`             | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`            | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                    | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                     | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

<br />

Here is an example for `jenkins-integration.yml` pipeline file:

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
    integration_type="jenkins"
    version="latest"

    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__JENKINS_USER=$(OCEAN__INTEGRATION__CONFIG__JENKINS_USER) \
        -e OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN=$(OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN) \
        -e OCEAN__INTEGRATION__CONFIG__JENKINS_HOST=$(OCEAN__INTEGRATION__CONFIG__JENKINS_HOST) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                   | Description                                                                                                                                          | Required |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_USER`  | The Jenkins Username                                                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN` | The Jenkins Token                                                                                                                                    | â       |
| `OCEAN__INTEGRATION__CONFIG__JENKINS_HOST`  | The Jenkins Host                                                                                                                                     | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`          | Default true, When set to false the integration will not create default blueprints and the port App config Mapping                                   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`             | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                  | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`            | Provide a unique identifier for your integration. If not provided, the default identifier will be used.                                              | â       |
| `OCEAN__PORT__CLIENT_ID`                    | Your port client id ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     | â       |
| `OCEAN__PORT__CLIENT_SECRET`                | Your port client secret ([Get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) | â       |
| `OCEAN__PORT__BASE_URL`                     | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                    | â       |

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
  INTEGRATION_TYPE: jenkins
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
        -e OCEAN__INTEGRATION__CONFIG__JENKINS_USER=$OCEAN__INTEGRATION__CONFIG__JENKINS_USER \
        -e OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN=$OCEAN__INTEGRATION__CONFIG__JENKINS_TOKEN \
        -e OCEAN__INTEGRATION__CONFIG__JENKINS_HOST=$OCEAN__INTEGRATION__CONFIG__JENKINS_HOST \
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
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: job
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .url | split("://")[1] | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") | gsub("/"; "-") | .[:-1]
          title: .fullName
          blueprint: '"jenkinsJob"'
          properties:
            jobName: .name
            url: .url
            jobStatus: '{"notbuilt": "created", "blue": "passing", "red": "failing"}[.color]'
            timestamp: .time
            parentJob: .__parentJob
  
 
  - kind: build
    selector:
      query: 'true'
      maxBuildsPerJob: 100
    port:
      entity:
        mappings:
          identifier: >-
            .url | split("://")[1] | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") | gsub("/"; "-") | .[:-1]
          title: .displayName
          blueprint: '"jenkinsBuild"'
          properties:
            buildStatus: .result
            buildUrl: .url
            buildDuration: .duration
            timestamp: .timestamp / 1000 | todate
          relations:
            parentJob: .url | split("://")[1] | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") | gsub("/"; "-") | .[:-1] | gsub("-[0-9]+$"; "")
            previousBuild: >-
              if .previousBuild then (.previousBuild.url | split("://")[1] |
              sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") |
              gsub("/"; "-") | .[:-1]) else null end

  - kind: user
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .user.id
          title: .user.fullName
          blueprint: '"jenkinsUser"'
          properties:
            url: .user.absoluteUrl
            lastUpdateTime: if .lastChange then (.lastChange/1000) else now end | strftime("%Y-%m-%dT%H:%M:%SZ")
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

Examples of blueprints and the relevant integration configurations:

### Job[â](#job "Direct link to Job")

**Job blueprint (click to expand)**

Create in Port

```
{
  "identifier": "jenkinsJob",
  "description": "This blueprint represents a job event from Jenkins",
  "title": "Jenkins Job",
  "icon": "Jenkins",
  "schema": {
    "properties": {
      "jobName": {
        "type": "string",
        "title": "Project Name"
      },
      "jobStatus": {
        "type": "string",
        "title": "Job Status",
        "enum": ["created", "updated", "deleted"],
        "enumColors": {
          "created": "green",
          "updated": "yellow",
          "deleted": "red"
        }
      },
      "timestamp": {
        "type": "string",
        "format": "date-time",
        "title": "Timestamp",
        "description": "Last updated timestamp of the job"
      },
      "url": {
        "type": "string",
        "title": "Project URL"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {
    "jobUrl": {
      "title": "Job Full URL",
      "calculation": "'https://your_jenkins_url/' + .properties.url",
      "type": "string",
      "format": "url"
    }
  },
  "relations": {}
}
```

**Integration configuration (click to expand)**

```
  createMissingRelatedEntities: true
  deleteDependentEntities: true
  resources:
    - kind: job
      selector:
        query: "true"
      port:
        entity:
          mappings:
            identifier: .url | split("://")[1] | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("/"; "-") | .[:-1]
            title: .fullName
            blueprint: '"jenkinsJob"'
            properties:
              jobName: .name
              url: .url
              jobStatus: '{"notbuilt": "created", "blue": "passing", "red": "failing"}[.color]'
              timestamp: .time
              parentJob: .__parentJob
```

### Build[â](#build "Direct link to Build")

Build Limit

By default, the integration fetches up to 100 builds per Jenkins job. This limit is configurable using the `maxBuildsPerJob` selector. See the configuration options below for more details.

**Build blueprint (click to expand)**

Create in Port

```
{
  "identifier": "jenkinsBuild",
  "description": "This blueprint represents a build event from Jenkins",
  "title": "Jenkins Build",
  "icon": "Jenkins",
  "schema": {
    "properties": {
      "buildStatus": {
        "type": "string",
        "title": "Build Status",
        "enum": ["SUCCESS", "FAILURE", "UNSTABLE"],
        "enumColors": {
          "SUCCESS": "green",
          "FAILURE": "red",
          "UNSTABLE": "yellow"
        }
      },
      "buildUrl": {
        "type": "string",
        "title": "Build URL",
        "description": "URL to the build"
      },
      "timestamp": {
        "type": "string",
        "format": "date-time",
        "title": "Timestamp",
        "description": "Last updated timestamp of the build"
      },
      "buildDuration": {
        "type": "number",
        "title": "Build Duration",
        "description": "Duration of the build"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "jenkinsJob": {
      "title": "Jenkins Job",
      "target": "jenkinsJob",
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
    - kind: build
      selector:
        query: "true"
        maxBuildsPerJob: 100
      port:
        entity:
          mappings:
            identifier: .url | split("://")[1] | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") | gsub("/"; "-") | .[:-1]
            title: .displayName
            blueprint: '"jenkinsBuild"'
            properties:
              buildStatus: .result
              buildUrl: .url
              buildDuration: .duration
              timestamp: '.timestamp / 1000 | todate'
            relations:
              parentJob: .url | split("://")[1] | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") | gsub("/"; "-") | .[:-1] | gsub("-[0-9]+$"; "")
              previousBuild: >-
                if .previousBuild then (.previousBuild.url | split("://")[1] |
                sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") |
                gsub("/"; "-") | .[:-1]) else null end
```

* Include Max Builds Per Job

The `maxBuildsPerJob` selector is an optional parameter that allows you to limit the number of builds to fetch for each job. By default, this selector is set to `100` which means the last 100 builds of each job will be fetched.

```
  - kind: build
    selector:
      query: 'true'
      maxBuildsPerJob: 100
```

### User[â](#user "Direct link to User")

**User blueprint (click to expand)**

Create in Port

```
{
  "identifier": "jenkinsUser",
  "description": "This blueprint represents a jenkins user",
  "title": "Jenkins User",
  "icon": "Jenkins",
  "schema": {
      "properties": {
          "url": {
              "type": "string",
              "title": "URL",
              "format": "url"
          },
          "lastUpdateTime": {
              "type": "string",
              "format": "date-time",
              "title": "Last Update",
              "description": "Last updated timestamp of the user"
          }
      },
      "required": []
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
  - kind: user
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .user.id
          title: .user.fullName
          blueprint: '"jenkinsUser"'
          properties:
            url: .user.absoluteUrl
            lastUpdateTime: if .lastChange then (.lastChange/1000) else now end | strftime("%Y-%m-%dT%H:%M:%SZ")
```

### Stage[â](#stage "Direct link to Stage")

**Stage blueprint (click to expand)**

Create in Port

```
{
  "identifier": "jenkinsStage",
  "description": "This blueprint represents a stage in a Jenkins build",
  "title": "Jenkins Stage",
  "icon": "Jenkins",
  "schema": {
    "properties": {
      "status": {
        "type": "string",
        "title": "Stage Status",
        "enum": [
          "SUCCESS",
          "FAILURE",
          "UNSTABLE",
          "ABORTED",
          "IN_PROGRESS",
          "NOT_BUILT",
          "PAUSED_PENDING_INPUT"
        ],
        "enumColors": {
          "SUCCESS": "green",
          "FAILURE": "red",
          "UNSTABLE": "yellow",
          "ABORTED": "darkGray",
          "IN_PROGRESS": "blue",
          "NOT_BUILT": "lightGray",
          "PAUSED_PENDING_INPUT": "orange"
        }
      },
      "startTimeMillis": {
        "type": "number",
        "title": "Start Time (ms)",
        "description": "Timestamp in milliseconds when the stage started"
      },
      "durationMillis": {
        "type": "number",
        "title": "Duration (ms)",
        "description": "Duration of the stage in milliseconds"
      },
      "stageUrl": {
        "type": "string",
        "title": "Stage URL",
        "description": "URL to the stage"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "parentBuild": {
      "title": "Jenkins Build",
      "target": "jenkinsBuild",
      "required": true,
      "many": false
    }
  }
}
```

**Integration configuration (click to expand)**

Control Stage Fetching

To prevent overwhelming your Ocean instance with potentially thousands of stages from Jenkins, the integration requires you to specify a specific job. This ensures that Ocean only retrieves stages related to that job, keeping things focused and efficient.

**Important**: The integration will also fetch stages from all nested jobs within the specified job.

```
- kind: stage
  selector:
    query: 'true'
    # Example jobUrl - replace with your own Jenkins job URL
    jobUrl: http://your-jenkins-server/job/your-project/job/your-job
  port:
    entity:
      mappings:
        identifier: >-
          ._links.self.href  | sub("^.*?/"; "") | gsub("%20"; "-") |
          gsub("%252F"; "-") | gsub("/"; "-")
        title: .name
        blueprint: '"jenkinsStage"'
        properties:
          status: .status
          startTimeMillis: .startTimeMillis
          durationMillis: .durationMillis
          stageUrl: env.OCEAN__INTEGRATION__CONFIG__JENKINS_HOST  + ._links.self.href
        relations:
          parentBuild: >-
            ._links.self.href | sub("/execution/node/[0-9]+/wfapi/describe$";
            "") | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") |
            gsub("/"; "-")
# Additional stage configurations follow the same pattern.
- kind: stage
  selector:
    query: 'true'
    # Example jobUrl - replace with your own Jenkins job URL
    jobUrl: http://your-jenkins-server/job/your-project/job/another-job
  port:
    entity:
      mappings:
        identifier: >-
          ._links.self.href  | sub("^.*?/"; "") | gsub("%20"; "-") |
          gsub("%252F"; "-") | gsub("/"; "-")
        title: .name
        blueprint: '"jenkinsStage"'
        properties:
          status: .status
          startTimeMillis: .startTimeMillis
          durationMillis: .durationMillis
          stageUrl: env.OCEAN__INTEGRATION__CONFIG__JENKINS_HOST  + ._links.self.href
        relations:
          parentBuild: >-
            ._links.self.href | sub("/execution/node/[0-9]+/wfapi/describe$";
            "") | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") |
            gsub("/"; "-")

- kind: stage
  selector:
    query: 'true'
    # Example jobUrl - replace with your own Jenkins job URL
    jobUrl: http://your-jenkins-server/job/your-project/job/third-job
  port:
    entity:
      mappings:
        identifier: >-
          ._links.self.href  | sub("^.*?/"; "") | gsub("%20"; "-") |
          gsub("%252F"; "-") | gsub("/"; "-")
        title: .name
        blueprint: '"jenkinsStage"'
        properties:
          status: .status
          startTimeMillis: .startTimeMillis
          durationMillis: .durationMillis
          stageUrl: env.OCEAN__INTEGRATION__CONFIG__JENKINS_HOST  + ._links.self.href
        relations:
          parentBuild: >-
            ._links.self.href | sub("/execution/node/[0-9]+/wfapi/describe$";
            "") | sub("^.*?/"; "") | gsub("%20"; "-") | gsub("%252F"; "-") |
            gsub("/"; "-")
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes a sample response data from Jenkins. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Jenkins:

**Job response data (click to expand)**

```
{
  "_class" : "hudson.model.FreeStyleProject",
  "displayName" : "Hello Job",
  "fullName" : "Hello Job",
  "name" : "Hello Job",
  "url" : "http://localhost:8080/job/Hello%20Job/",
  "buildable" : true,
  "builds" : [
    {
      "_class" : "hudson.model.FreeStyleBuild",
      "displayName" : "#2",
      "duration" : 221,
      "fullDisplayName" : "Hello Job #2",
      "id" : "2",
      "number" : 2,
      "result" : "SUCCESS",
      "timestamp" : 1700569094576,
      "url" : "http://localhost:8080/job/Hello%20Job/2/"
    },
    {
      "_class" : "hudson.model.FreeStyleBuild",
      "displayName" : "#1",
      "duration" : 2214,
      "fullDisplayName" : "Hello Job #1",
      "id" : "1",
      "number" : 1,
      "result" : "SUCCESS",
      "timestamp" : 1700567994163,
      "url" : "http://localhost:8080/job/Hello%20Job/1/"
    }
  ],
  "color" : "blue"
}
```

**Build response data (click to expand)**

```
{
  "_class" : "hudson.model.FreeStyleBuild",
  "displayName" : "#2",
  "duration" : 221,
  "fullDisplayName" : "Hello Job #2",
  "id" : "2",
  "number" : 2,
  "result" : "SUCCESS",
  "timestamp" : 1700569094576,
  "url" : "http://localhost:8080/job/Hello%20Job/2/"
}
```

**User response data (click to expand)**

```
{
  "user" : {
    "absoluteUrl" : "http://localhost:8080/user/admin",
    "fullName" : "admin",
    "description" : "System Administrator",
    "id" : "admin"
  },
  "lastChange" : 1700569094576
}
```

**Stage response data (click to expand)**

```
{
  "_links": {
    "self": {
      "href": "/job/Phalbert/job/salesdash/job/master/227/execution/node/17/wfapi/describe"
    }
  },
  "id": "17",
  "name": "Declarative: Post Actions",
  "execNode": "",
  "status": "SUCCESS",
  "startTimeMillis": 1717073271079,
  "durationMillis": 51,
  "pauseDurationMillis": 0
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

**Job entity (click to expand)**

```
{
  "identifier": "hello-job",
  "title": "Hello Job",
  "icon": "Jenkins",
  "blueprint": "jenkinsJob",
  "properties": {
    "jobName": "Hello Job",
    "url": "http://localhost:8080/job/Hello%20Job/",
    "jobStatus": "passing",
    "timestamp": "2023-09-08T14:58:14Z"
  },
  "relations": {},
  "createdAt": "2023-12-18T08:37:21.637Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2023-12-18T08:37:21.637Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

**Build entity (click to expand)**

```
{
  "identifier": "hello-job-2",
  "title": "Hello Job #2",
  "icon": "Jenkins",
  "blueprint": "jenkinsBuild",
  "properties": {
    "buildStatus": "SUCCESS",
    "buildUrl": "http://localhost:8080/job/Hello%20Job/2/",
    "buildDuration": 221,
    "timestamp": "2023-09-08T14:58:14Z"
  },
  "relations": {
    "parentJob": "hello-job"
  },
  "createdAt": "2023-12-18T08:37:21.637Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2023-12-18T08:37:21.637Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

**User entity (click to expand)**

```
{
  "identifier": "admin",
  "title": "admin",
  "icon": "Jenkins",
  "blueprint": "jenkinsUser",
  "properties": {
    "url": "http://localhost:8080/user/admin",
    "lastUpdateTime": "2023-09-08T14:58:14Z"
  },
  "relations": {},
  "createdAt": "2023-12-18T08:37:21.637Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2023-12-18T08:37:21.637Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

**Stage entity (click to expand)**

```
{
  "identifier": "job-Phalbert-job-salesdash-job-master-229-execution-node-17-wfapi-describe",
  "title": "Declarative: Post Actions",
  "icon": "Jenkins",
  "blueprint": "jenkinsStage",
  "team": [],
  "properties": {
    "status": "SUCCESS",
    "startTimeMillis": 1717073272012,
    "durationMillis": 26,
    "stageUrl": "http://localhost:8080/job/Phalbert/job/salesdash/job/master/229/execution/node/17/wfapi/describe"
  },
  "relations": {
    "parentBuild": "job-Phalbert-job-salesdash-job-master-229"
  },
  "createdAt": "2024-08-28T10:27:33.549Z",
  "createdBy": "<port-client-id>",
  "updatedAt": "2024-08-28T10:27:30.274Z",
  "updatedBy": "<port-client-id>"
}
```

## Alternative installation via webhook[â](#alternative-installation-via-webhook "Direct link to Alternative installation via webhook")

While the Ocean integration described above is the recommended installation method, you may prefer to use a webhook to ingest job and build entities from Jenkins. If so, use the following instructions:

**Note** that when using this method, data will be ingested into Port only when the webhook is triggered.

**Webhook installation (click to expand)**

## Port configuration

Create the following blueprint definitions:

Jenkins job blueprint

**Job blueprint (click to expand)**

Create in Port

```
{
  "identifier": "jenkinsJob",
  "description": "This blueprint represents a job event from Jenkins",
  "title": "Jenkins Job",
  "icon": "Jenkins",
  "schema": {
    "properties": {
      "jobName": {
        "type": "string",
        "title": "Project Name"
      },
      "jobStatus": {
        "type": "string",
        "title": "Job Status",
        "enum": ["created", "updated", "deleted"],
        "enumColors": {
          "created": "green",
          "updated": "yellow",
          "deleted": "red"
        }
      },
      "timestamp": {
        "type": "string",
        "format": "date-time",
        "title": "Timestamp",
        "description": "Last updated timestamp of the job"
      },
      "url": {
        "type": "string",
        "title": "Project URL"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {
    "jobUrl": {
      "title": "Job Full URL",
      "calculation": "'https://your_jenkins_url/' + .properties.url",
      "type": "string",
      "format": "url"
    }
  },
  "relations": {}
}
```

Jenkins build blueprint (including the Jenkins job relation)

**Build blueprint (click to expand)**

Create in Port

```
{
  "identifier": "jenkinsBuild",
  "description": "This blueprint represents a build event from Jenkins",
  "title": "Jenkins Build",
  "icon": "Jenkins",
  "schema": {
    "properties": {
      "buildStatus": {
        "type": "string",
        "title": "Build Status",
        "enum": ["SUCCESS", "FAILURE", "UNSTABLE"],
        "enumColors": {
          "SUCCESS": "green",
          "FAILURE": "red",
          "UNSTABLE": "yellow"
        }
      },
      "buildUrl": {
        "type": "string",
        "title": "Build URL",
        "description": "URL to the build"
      },
      "timestamp": {
        "type": "string",
        "format": "date-time",
        "title": "Timestamp",
        "description": "Last updated timestamp of the build"
      },
      "buildDuration": {
        "type": "number",
        "title": "Build Duration",
        "description": "Duration of the build"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "jenkinsJob": {
      "title": "Jenkins Job",
      "target": "jenkinsJob",
      "required": false,
      "many": false
    }
  }
}
```

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints):

Jenkins job and build webhook configuration

1. **Basic details** tab - fill the following details:

   1. Title : `Jenkins Mapper`;
   2. Identifier : `jenkins_mapper`;
   3. Description : `A webhook configuration to map Jenkins builds and jobs to Port`;
   4. Icon : `Jenkins`;

2. **Integration configuration** tab - fill the following JQ mapping:

   ```
   [
     {
       "blueprint": "jenkinsJob",
       "filter": ".body.type | startswith(\"item\")",
       "entity": {
         "identifier": ".body.url | sub(\"%20\"; \"-\"; \"g\") | sub(\"/\"; \"-\"; \"g\") | .[:-1]",
         "title": ".body.data.displayName",
         "properties": {
           "jobName": ".body.data.fullName",
           "url": ".body.url",
           "jobStatus": ".body.type | split(\".\") | last",
           "timestamp": ".body.time"
         }
       }
     },
     {
       "blueprint": "jenkinsBuild",
       "filter": ".body.type | startswith(\"run\")",
       "entity": {
         "identifier": ".body.data.fullDisplayName | sub(\" \"; \"-\"; \"g\") | sub(\"#\"; \"\"; \"g\")",
         "title": ".body.data.displayName",
         "properties": {
           "buildStatus": ".body.data.result",
           "buildUrl": ".body.url",
           "buildDuration": ".body.data.duration",
           "timestamp": ".body.data.timestamp / 1000 | todate"
         },
         "relations": {
           "jenkinsJob": ".body.source | tostring | sub(\"%20\"; \"-\"; \"g\") | sub(\"/\"; \"-\"; \"g\") | .[:-1]"
         }
       }
     }
   ]
   ```

3. Click **Save** at the bottom of the page.

## Create a webhook in Jenkins

1. Go to your Jenkins dashboard.
2. At the sidebar on the left side of the page, select **Manage Jenkins** and click on **Manage Plugins**.
3. Navigate to the **Available Plugins** tab and search for **Generic Event** in the search bar. Install the [Generic Event](https://plugins.jenkins.io/generic-event/) or a suitable plugin that can notify some endpoints about all events that happen in Jenkins.
4. Go back to your Jenkins dashboard and click on **Manage Jenkins** at the left side menu.
5. Click on the **Configure System** tab and scroll down to the **Event Dispatcher** section.
6. Enter the value of the `url` key you received after creating the webhook configuration in the textbox.
7. Click on **Save** at the bottom of the page.

tip

In order to view the different payloads and events available in Jenkins webhooks, [click here](https://plugins.jenkins.io/generic-event/).

Done! Any changes to a job or build process (queued, started, completed, finalized, etc.) will trigger a webhook event to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

## Let's Test It

This section includes a sample response data from Jenkins. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload

Here is an example of the payload structure from Jenkins:

Job response data

```
{
  "_class" : "hudson.model.FreeStyleProject",
  "displayName" : "Hello Job",
  "fullName" : "Hello Job",
  "name" : "Hello Job",
  "url" : "http://localhost:8080/job/Hello%20Job/",
  "buildable" : true,
  "builds" : [
    {
      "_class" : "hudson.model.FreeStyleBuild",
      "displayName" : "#2",
      "duration" : 221,
      "fullDisplayName" : "Hello Job #2",
      "id" : "2",
      "number" : 2,
      "result" : "SUCCESS",
      "timestamp" : 1700569094576,
      "url" : "http://localhost:8080/job/Hello%20Job/2/"
    },
    {
      "_class" : "hudson.model.FreeStyleBuild",
      "displayName" : "#1",
      "duration" : 2214,
      "fullDisplayName" : "Hello Job #1",
      "id" : "1",
      "number" : 1,
      "result" : "SUCCESS",
      "timestamp" : 1700567994163,
      "url" : "http://localhost:8080/job/Hello%20Job/1/"
    }
  ],
  "color" : "blue"
}
```

Build response data

```
{
  "_class" : "hudson.model.FreeStyleBuild",
  "displayName" : "#2",
  "duration" : 221,
  "fullDisplayName" : "Hello Job #2",
  "id" : "2",
  "number" : 2,
  "result" : "SUCCESS",
  "timestamp" : 1700569094576,
  "url" : "http://localhost:8080/job/Hello%20Job/2/"
}
```

### Mapping Result

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Job entity

```
{
  "identifier": "hello-job",
  "title": "Hello Job",
  "blueprint": "jenkinsJob",
  "properties": {
    "jobName": "Hello Job",
    "url": "http://localhost:8080/job/Hello%20Job/",
    "jobStatus": "passing",
    "timestamp": "2023-09-08T14:58:14Z"
  },
  "relations": {},
  "createdAt": "2023-12-18T08:37:21.637Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2023-12-18T08:37:21.637Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```

Build entity

```
{
  "identifier": "hello-job-2",
  "title": "Hello Job #2",
  "blueprint": "jenkinsBuild",
  "properties": {
    "buildStatus": "SUCCESS",
    "buildUrl": "http://localhost:8080/job/Hello%20Job/2/",
    "buildDuration": 221,
    "timestamp": "2023-09-08T14:58:14Z"
  },
  "relations": {
    "parentJob": "hello-job"
  },
  "createdAt": "2023-12-18T08:37:21.637Z",
  "createdBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW",
  "updatedAt": "2023-12-18T08:37:21.637Z",
  "updatedBy": "hBx3VFZjqgLPEoQLp7POx5XaoB0cgsxW"
}
```
