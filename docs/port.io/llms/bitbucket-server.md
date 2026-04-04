# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-server.md

# Bitbucket (self-hosted)

Loading version...

Port's Bitbucket (Self-Hosted) integration allows you to model Bitbucket Server / Bitbucket Data Center resources in your software catalog and ingest data into them.

**Note:** While Bitbucket Server has been [deprecated and replaced by Bitbucket Data Center](https://www.atlassian.com/blog/announcements/journey-to-cloud), they expose the same set of APIs and this integration covers both.

Bitbucket Self-Hosted

This documentation covers Port's integration with **Bitbucket (Self-Hosted)**. For information about integrating with Bitbucket Cloud, please refer to the [Bitbucket Cloud integration documentation](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/.md).

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Bitbucket resources and their metadata in Port (see supported resources below).
* Watch for Bitbucket object changes (create/update/delete) in real-time, and automatically apply the changes to your software catalog.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Bitbucket (Self-Hosted) into Port are listed below.<br /><!-- -->It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [Project](https://developer.atlassian.com/server/bitbucket/rest/v906/api-group-project/#api-api-latest-projects-get)
* [Repository](https://developer.atlassian.com/server/bitbucket/rest/v906/api-group-project/#api-api-latest-projects-projectkey-repos-get)
* [Pull Request](https://developer.atlassian.com/server/bitbucket/rest/v906/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-get)
* [User](https://developer.atlassian.com/server/bitbucket/rest/v906/api-group-permission-management/#api-api-latest-admin-users-get)

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port
* Self-hosted
* CI

Using this installation option means that the integration will be hosted by Port, with a customizable resync interval to ingest data into Port.

### Live event support

This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

**Supported live event triggers**

**Pull Request:**

* pr:modified
* pr:opened
* pr:merged
* pr:reviewer:updated
* pr:declined
* pr:deleted
* pr:comment:deleted
* pr:from\_ref\_updated
* pr:comment:edited
* pr:reviewer:unapproved
* pr:reviewer:needs\_work
* pr:reviewer:approved
* pr:comment:added

**Repository:**

* repo:modified
* repo:refs\_changed

**Project:**

* project:modified

Self-hosted installation

Alternatively, you can install the integration using the [Self-hosted](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-server/.md?installation-methods=real-time-self-hosted#setup) method to update Port in real time using webhooks.

### Installation

To install, follow these steps:

1. Go to the [Data sources](https://app.getport.io/settings/data-sources) page of your portal.

2. Click on the `+ Data source` button in the top-right corner.

3. Click on the relevant integration in the list.

4. Under `Select your installation method`, choose `Hosted by Port`.

5. Configure the `integration settings` and `application settings` as you wish (see below for details).

### Application settings

Every integration hosted by Port has the following customizable application settings, which are configurable after installation:

* `Resync interval`: The frequency at which Port will ingest data from the integration. There are various options available, ranging from every 1 hour to once a day.

* `Send raw data examples`: A boolean toggle (`enabled` by default). If enabled, raw data examples will be sent from the integration to Port. These examples are used when [testing your mapping configuration](/build-your-software-catalog/customize-integrations/configure-mapping.md#test-your-mapping---jq-playground), they allow you to run your `jq` expressions against real data and see the results.

### Integration settings

Every integration has its own tool-specific settings, under the `Integration settings` section.<br /><!-- -->Each of these settings has an â icon next to it, which you can hover over to see a description of the setting.

#### Port secrets

Some integration settings require sensitive pieces of data, such as tokens.<br /><!-- -->For these settings, [Port secrets](/sso-rbac/port-secrets/.md) will be used, ensuring that your sensitive data is encrypted and secure.

When filling in such a setting, its value will be obscured (shown as `â¢â¢â¢â¢â¢â¢â¢â¢`).<br /><!-- -->For each such setting, Port will automatically create a secret in your organization.

To see all secrets in your organization, follow [these steps](/sso-rbac/port-secrets/.md#usage).

### Limitations

* The maximum time for a full sync to run is based on the configured resync interval. For very large amounts of data where a resync operation is expected to take longer, please use a longer interval.

### Port source IP addresses

When using this installation method, Port will make outbound calls to your 3rd-party applications from static IP addresses.<br /><!-- -->You may need to add these addresses to your allowlist, in order to allow Port to interact with the integrated service:

* Europe (EU)
* United States (US)

```
54.73.167.226  
63.33.143.237  
54.76.185.219
```

```
3.234.37.33  
54.225.172.136  
3.225.234.99
```

Bitbucket (Self-Hosted) version

You should toggle the `Bitbucket Is Version 8 Point 7 Or Older` option to `true` if you are using Bitbucket (Self-Hosted) version 8.7 or older. This is because webhook events are setup differently in Bitbucket (Self-Hosted) 8.8 and above.

Using this installation option means that the integration will be able to update Port in real time using webhooks.

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

For details about the available parameters for the installation, see the table below.

* Helm
* ArgoCD

<!-- -->

1. Go to the [Bitbucket Self-Hosted<!-- --> data source page](<https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Bitbucket Self-Hosted>) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Bitbucket Self-Hosted<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Bitbucket Self-Hosted<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Bitbucket Self-Hosted<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Bitbucket Self-Hosted
  <!-- -->
  can reach.

If `liveEvents.baseUrl` is not provided, the integration will continue to function correctly. In such a configuration, to retrieve the latest information from the target system, the [`scheduledResyncInterval`](https://ocean.port.io/developing-an-integration/trigger-your-integration) parameter has to be set, or a manual resync will need to be triggered through Port's UI.

Debugging local integrations

To test webhooks or live event delivery to your local environment, expose your local pod or service to the internet using ngrok (e.g. `ngrok http http://localhost:8000`)

<!-- -->

### Securing Your Webhooks

The `integration.secrets.bitbucketWebhookSecret` parameter secures your webhooks. If not provided, the integration will process webhooks without validating the source of the events.

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

1. Create a `values.yaml` file in `argocd/my-ocean-bitbucket-server-integration` in your git repository with the content:

note

Remember to replace the placeholder for `BITBUCKET_USERNAME`, `BITBUCKET_PASSWORD`, `BITBUCKET_BASE_URL`, `BITBUCKET_WEBHOOK_SECRET`, `BITBUCKET_IS_VERSION8_POINT7_OR_OLDER`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-bitbucket-server-integration
  type: bitbucket-server
  eventListener:
    type: POLLING
  config:
    bitbucketBaseUrl: BITBUCKET_BASE_URL
    bitbucketUsername: BITBUCKET_USERNAME
    bitbucketIsVersion8Point7OrOlder: BITBUCKET_IS_VERSION8_POINT7_OR_OLDER
  secrets:
    bitbucketPassword: BITBUCKET_PASSWORD
    bitbucketWebhookSecret: BITBUCKET_WEBHOOK_SECRET
```

<br />

1. Install the `my-ocean-bitbucket-server-integration` ArgoCD Application by creating the following `my-ocean-bitbucket-server-integration.yaml` manifest:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.<br /><!-- -->Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-bitbucket-server-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-bitbucket-server-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-bitbucket-server-integration/values.yaml
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
kubectl apply -f my-ocean-bitbucket-server-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                                             | Description                                                                                                                                                                     | Required |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                                       | Your port client id                                                                                                                                                             | â       |
| `port.clientSecret`                                   | Your port client secret                                                                                                                                                         | â       |
| `port.baseUrl`                                        | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                               | â       |
| `integration.identifier`                              | Change the identifier to describe your integration                                                                                                                              | â       |
| `integration.type`                                    | The integration type                                                                                                                                                            | â       |
| `integration.eventListener.type`                      | The event listener type                                                                                                                                                         | â       |
| `integration.config.bitbucketUsername`                | Bitbucket username                                                                                                                                                              | â       |
| `integration.secrets.bitbucketPassword`               | Bitbucket password                                                                                                                                                              | â       |
| `integration.secrets.bitbucketWebhookSecret`          | Bitbucket webhook secret used to verify the webhook request                                                                                                                     | â       |
| `integration.config.bitbucketBaseUrl`                 | Bitbucket base url                                                                                                                                                              | â       |
| `integration.config.bitbucketIsVersion8Point7OrOlder` | Bitbucket is version 8.7 or older                                                                                                                                               | â       |
| `scheduledResyncInterval`                             | The number of minutes between each resync                                                                                                                                       | â       |
| `initializePortResources`                             | Default true, When set to true the integration will create default blueprints and the port App config Mapping                                                                   | â       |
| `sendRawDataExamples`                                 | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                             | â       |
| `integration.config.bitbucketRateLimitQuota`          | Maximum number of API requests allowed within the rate limit window. Default is `1000`                                                                                          | â       |
| `integration.config.bitbucketRateLimitWindow`         | Time window in seconds for rate limiting. Default is `3600` (1 hour)                                                                                                            | â       |
| `liveEvents.baseUrl`                                  | The base url of the instance where the Bitbucket (Self-Hosted) integration is hosted, used for real-time updates. (e.g.`https://mybitbucket-self-hosted-ocean-integration.com`) | â       |

**Note:** You should set the `integration.config.bitbucketIsVersion8Point7OrOlder` parameter to `true` if you are using Bitbucket (Self-Hosted) version 8.7 or older. This is because webhook events are setup differently in Bitbucket (Self-Hosted) 8.7 and above.

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

This workflow/pipeline will run the Bitbucket (Self-Hosted) integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                         | Description                                                                                                                                                 | Example                            | Required |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `port_client_id`                                  | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |                                    | â       |
| `port_client_secret`                              | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |                                    | â       |
| `port_base_url`                                   | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |                                    | â       |
| `config -> bitbucket_username`                    | Bitbucket username                                                                                                                                          |                                    | â       |
| `config -> bitbucket_password`                    | Bitbucket password                                                                                                                                          |                                    | â       |
| `config -> bitbucket_base_url`                    | Bitbucket base url                                                                                                                                          |                                    | â       |
| `config -> bitbucket_webhook_secret`              | Bitbucket webhook secret used to verify the webhook request                                                                                                 |                                    | â       |
| `config -> bitbucket_is_version8_point7_or_older` | Bitbucket is version 8.7 or older                                                                                                                           |                                    | â       |
| `config -> bitbucket_rate_limit_quota`            | Maximum number of API requests allowed within the rate limit window. Default is `1000`                                                                      |                                    | â       |
| `config -> bitbucket_rate_limit_window`           | Time window in seconds for rate limiting. Default is `3600` (1 hour)                                                                                        |                                    | â       |
| `initialize_port_resources`                       | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |                                    | â       |
| `identifier`                                      | The identifier of the integration that will be installed                                                                                                    |                                    | â       |
| `version`                                         | The version of the integration that will be installed                                                                                                       | latest                             | â       |
| `sendRawDataExamples`                             | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         | true                               | â       |
| `liveEvents.baseUrl`                              | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Bitbucket (Self-Hosted)                       | <https://my-ocean-integration.com> | â       |

<br />

Ocean Sail Github Action

The following example uses the **Ocean Sail** Github Action to run the Bitbucket (Self-Hosted) integration. For further information about the action, please visit the [Ocean Sail Github Action](https://github.com/marketplace/actions/ocean-sail)

<br />

Here is an example for `bitbucket-server-integration.yml` workflow file:

```
name: Bitbucket (Self-Hosted) Exporter Workflow

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
          type: 'bitbucket-server'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            bitbucket_username: ${{ secrets.OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME }}
            bitbucket_password: ${{ secrets.OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD }}
            bitbucket_base_url: ${{ secrets.OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL }}
            bitbucket_webhook_secret: ${{ secrets.OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET }}
            bitbucket_is_version8_point7_or_older: ${{ secrets.OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER }}
```

**Note:** You should set the `bitbucket_is_version8_point7_or_older` parameter to `true` if you are using Bitbucket (Self-Hosted) version 8.7 or older. This is because webhook events are setup differently in Bitbucket (Self-Hosted) 8.7 and above.

Tip for Jenkins agent

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                                             | Description                                                                                                                                                 | Example | Required |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME`                      | Bitbucket Server username                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD`                      | Bitbucket Server password                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL`                      | Bitbucket Server base url                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET`                | Bitbucket Server webhook secret used to verify the webhook request                                                                                          |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION_8_POINT_7_OR_OLDER` | Bitbucket Server is version 8.7 or older                                                                                                                    |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_RATE_LIMIT_QUOTA`              | Maximum number of API requests allowed within the rate limit window. Default is `1000`                                                                      |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_RATE_LIMIT_WINDOW`             | Time window in seconds for rate limiting. Default is `3600` (1 hour)                                                                                        |         | â       |
| `OCEAN__PORT__CLIENT_ID`                                              | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`                                          | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                                               | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                                    | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                                      | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                                       | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |
| `OCEAN__BASE_URL`                                                     | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        |         | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Bitbucket Self-Hosted Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME', variable: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD', variable: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL', variable: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET', variable: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER', variable: 'OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="bitbucket-server"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME \
                                -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD \
                                -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL \
                                -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET \
                                -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER \
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

**Note:** You should set the `OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER` parameter to `true` if you are using Bitbucket (Self-Hosted) version 8.7 or older. This is because webhook events are setup differently in Bitbucket (Self-Hosted) 8.7 and above.

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

| Parameter                                                             | Description                                                                                                                                                 | Example | Required |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME`                      | Bitbucket Server username                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD`                      | Bitbucket Server password                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL`                      | Bitbucket Server base url                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET`                | Bitbucket Server webhook secret used to verify the webhook request                                                                                          |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION_8_POINT_7_OR_OLDER` | Bitbucket Server is version 8.7 or older                                                                                                                    |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_RATE_LIMIT_QUOTA`              | Maximum number of API requests allowed within the rate limit window. Default is `1000`                                                                      |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_RATE_LIMIT_WINDOW`             | Time window in seconds for rate limiting. Default is `3600` (1 hour)                                                                                        |         | â       |
| `OCEAN__PORT__CLIENT_ID`                                              | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`                                          | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                                               | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                                    | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                                      | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                                       | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |
| `OCEAN__BASE_URL`                                                     | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        |         | â       |

<br />

Here is an example for `bitbucket-server-integration.yml` pipeline file:

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
      integration_type="bitbucket-server"
      version="latest"

      image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

      docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME=$(OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME) \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD=$(OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD) \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL=$(OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL) \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET=$(OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET) \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER=$(OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

      exit $?
    displayName: "Ingest Data into Port"
```

**Note:** You should set the `OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER` parameter to `true` if you are using Bitbucket (Self-Hosted) version 8.7 or older. This is because webhook events are setup differently in Bitbucket (Self-Hosted) 8.7 and above.

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                                             | Description                                                                                                                                                 | Example | Required |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME`                      | Bitbucket Server username                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD`                      | Bitbucket Server password                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL`                      | Bitbucket Server base url                                                                                                                                   |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET`                | Bitbucket Server webhook secret used to verify the webhook request                                                                                          |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION_8_POINT_7_OR_OLDER` | Bitbucket Server is version 8.7 or older                                                                                                                    |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_RATE_LIMIT_QUOTA`              | Maximum number of API requests allowed within the rate limit window. Default is `1000`                                                                      |         | â       |
| `OCEAN__INTEGRATION__CONFIG__BITBUCKET_RATE_LIMIT_WINDOW`             | Time window in seconds for rate limiting. Default is `3600` (1 hour)                                                                                        |         | â       |
| `OCEAN__PORT__CLIENT_ID`                                              | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |         | â       |
| `OCEAN__PORT__CLIENT_SECRET`                                          | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |         | â       |
| `OCEAN__PORT__BASE_URL`                                               | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                           |         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                                    | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                              |         | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                                      | The identifier of the integration that will be installed                                                                                                    |         | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                                       | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                         |         | â       |
| `OCEAN__BASE_URL`                                                     | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in Linear                                        |         | â       |

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
  INTEGRATION_TYPE: bitbucket-server
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
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_USERNAME \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_PASSWORD \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_BASE_URL \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_WEBHOOK_SECRET \
        -e OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER=$OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER \
        -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
        -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
```

**Note:** You should set the `OCEAN__INTEGRATION__CONFIG__BITBUCKET_IS_VERSION8_POINT7_OR_OLDER` parameter to `true` if you are using Bitbucket (Self-Hosted) version 8.7 or older. This is because webhook events are setup differently in Bitbucket (Self-Hosted) 8.7 and above.

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Filtering data[â](#filtering-data "Direct link to Filtering data")

The integration supports several selector properties to control which data is ingested from Bitbucket Server into Port.

#### Filtering projects[â](#filtering-projects "Direct link to Filtering projects")

You can filter projects by providing a list of specific project keys using the `projects` selector. When set, only repositories belonging to the listed projects are ingested:

**Filter by project keys (click to expand)**

```
resources:
  - kind: repository
    selector:
      query: "true"
      projects:
        - "PROJ"
        - "TEAM-A"
    port:
      entity:
        mappings:
          identifier: .slug
          title: .name
          blueprint: '"bitbucketRepository"'
          properties:
            description: .description
            state: .state
            forkable: .forkable
            public: .public
            link: .links.self[0].href
          relations:
            project: .project.key
```

The `projects` selector is available for the `project`, `repository`, and `pull-request` kinds, and applies the same filtering to those resources.

#### Filtering projects using regex[â](#filtering-projects-using-regex "Direct link to Filtering projects using regex")

You can also use the `projectFilterRegex` selector to filter projects by a regex pattern applied to project keys. This is useful when you want to match a set of projects by naming convention:

**Filter by project regex (click to expand)**

```
resources:
  - kind: repository
    selector:
      query: "true"
      projectFilterRegex: "^TEAM-.*"
    port:
      entity:
        mappings:
          identifier: .slug
          title: .name
          blueprint: '"bitbucketRepository"'
          properties:
            description: .description
            state: .state
            forkable: .forkable
            public: .public
            link: .links.self[0].href
          relations:
            project: .project.key
```

Common regex patterns include:

* `^TEAM-.*` â matches projects whose keys start with `TEAM-`.
* `.*-PROD$` â matches projects whose keys end with `-PROD`.
* `^(PROJ|INFRA)$` â matches the exact keys `PROJ` or `INFRA`.

Combining filters

When both `projects` and `projectFilterRegex` are set on the same resource kind, both conditions must match (AND logic). A project will only be included if its key appears in the `projects` list **and** matches the `projectFilterRegex` pattern.

#### Filtering pull request state[â](#filtering-pull-request-state "Direct link to Filtering pull request state")

For the `pull-request` kind, you can use the `state` selector to control which pull requests are ingested. Accepted values are `ALL`, `OPEN`, `MERGED`, and `DECLINED`. The default is `OPEN`:

**Filter pull request state (click to expand)**

```
resources:
  - kind: pull-request
    selector:
      query: "true"
      state: "ALL"
    port:
      entity:
        mappings:
          identifier: .id | tostring
          title: .title
          blueprint: '"bitbucketPullRequest"'
          properties:
            created_on: .createdDate | (tonumber / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ"))
            updated_on: .updatedDate | (tonumber / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ"))
            state: .state
            owner: .author.user.emailAddress
            link: .links.self[0].href
            destination: .toRef.displayId
            source: .fromRef.displayId
          relations:
            repository: .toRef.repository.slug
```

You can combine all the selectors together. For example, to sync only `OPEN` pull requests from projects matching a regex:

**Combine selectors (click to expand)**

```
resources:
  - kind: pull-request
    selector:
      query: "true"
      projectFilterRegex: "^TEAM-.*"
      state: "OPEN"
    port:
      entity:
        mappings:
          identifier: .id | tostring
          title: .title
          blueprint: '"bitbucketPullRequest"'
          properties:
            created_on: .createdDate | (tonumber / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ"))
            updated_on: .updatedDate | (tonumber / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ"))
            state: .state
            owner: .author.user.emailAddress
            link: .links.self[0].href
            destination: .toRef.displayId
            source: .fromRef.displayId
          relations:
            repository: .toRef.repository.slug
```

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations:

### Project[â](#project "Direct link to Project")

Project blueprint

Create in Port

```
{
    "identifier": "bitbucketProject",
    "description": "A software catalog to represent Bitbucket project",
    "title": "Bitbucket Project",
    "icon": "BitBucket",
    "schema": {
        "properties": {
            "public": {
                "icon": "DefaultProperty",
                "title": "Public",
                "type": "boolean"
            },
            "description": {
                "title": "Description",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "type": {
                "icon": "DefaultProperty",
                "title": "Type",
                "type": "string"
            },
            "link": {
                "title": "Link",
                "icon": "DefaultProperty",
                "type": "string"
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
  - kind: project
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .key
          title: .name
          blueprint: '"bitbucketProject"'
          properties:
            public: .public
            type: .type
            description: .description
            link: .links.self[0].href
```

### Repository[â](#repository "Direct link to Repository")

Repository blueprint

Create in Port

```
{
    "identifier": "bitbucketRepository",
    "description": "A software catalog to represent Bitbucket repositories",
    "title": "Bitbucket Repository",
    "icon": "BitBucket",
    "schema": {
        "properties": {
            "forkable": {
                "icon": "DefaultProperty",
                "title": "Is Forkable",
                "type": "boolean"
            },
            "description": {
                "title": "Description",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "public": {
                "icon": "DefaultProperty",
                "title": "Is Public",
                "type": "boolean"
            },
            "state": {
                "icon": "DefaultProperty",
                "title": "State",
                "type": "string"
            },
            "link": {
                "title": "Link",
                "icon": "DefaultProperty",
                "type": "string"
            },
            "documentation": {
                "icon": "DefaultProperty",
                "title": "Documentation",
                "type": "string",
                "format": "markdown"
            },
            "swagger_url": {
                "title": "Swagger URL",
                "type": "string",
                "format": "url",
                "spec": "async-api",
                "icon": "DefaultProperty"
            },
            "readme": {
                "title": "Readme",
                "type": "string",
                "format": "markdown",
                "icon": "DefaultProperty"
            }
        },
        "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
        "latestCommitAuthor": {
            "title": "Latest Commit By",
            "description": "The user that made the most recent commit to the base branch",
            "target": "bitbucketUser",
            "required": false,
            "many": false
        },
        "project": {
            "title": "Project",
            "target": "bitbucketProject",
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
  - kind: repository
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .slug
          title: .name
          blueprint: '"bitbucketRepository"'
          properties:
            description: .description
            state: .state
            forkable: .forkable
            public: .public
            link: .links.self[0].href
            documentation: .__readme
          relations:
            project: .project.key
            latestCommitAuthor: .__latestCommit.author.emailAddress
```

### Pull Request[â](#pull-request "Direct link to Pull Request")

Pull Request blueprint

Create in Port

```
{
    "identifier": "bitbucketPullRequest",
    "description": "A software catalog to represent Bitbucket pull requests",
    "title": "Bitbucket Pull Request",
    "icon": "BitBucket",
    "schema": {
        "properties": {
            "created_on": {
                "title": "Created On",
                "type": "string",
                "format": "date-time",
                "icon": "DefaultProperty"
            },
            "updated_on": {
                "title": "Updated On",
                "type": "string",
                "format": "date-time",
                "icon": "DefaultProperty"
            },
            "description": {
                "title": "Description",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "state": {
                "icon": "DefaultProperty",
                "title": "State",
                "type": "string",
                "enum": [
                    "OPEN",
                    "MERGED",
                    "DECLINED",
                    "SUPERSEDED"
                ],
                "enumColors": {
                    "OPEN": "yellow",
                    "MERGED": "green",
                    "DECLINED": "red",
                    "SUPERSEDED": "purple"
                }
            },
            "owner": {
                "title": "Owner",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "link": {
                "title": "Link",
                "icon": "DefaultProperty",
                "type": "string"
            },
            "destination": {
                "title": "Destination Branch",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "source": {
                "title": "Source Branch",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "reviewers": {
                "items": {
                    "type": "string"
                },
                "title": "Reviewers",
                "type": "array",
                "icon": "DefaultProperty"
            },
            "merge_commit": {
                "title": "Merge Commit",
                "type": "string",
                "icon": "DefaultProperty"
            },
            "mergedAt": {
                "title": "Merged At",
                "type": "string",
                "format": "date-time",
                "icon": "DefaultProperty"
            }
        },
        "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
        "participants": {
            "title": "Participants",
            "description": "Users that contributed to the PR",
            "target": "bitbucketUser",
            "required": false,
            "many": true
        },
        "repository": {
            "title": "Repository",
            "target": "bitbucketRepository",
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
  - kind: pull-request
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: (.toRef.repository.slug // .toRef.repository.project.key) + "-" + (.id|tostring)
          title: .title
          blueprint: '"bitbucketPullRequest"'
          properties:
            created_on: .createdDate | (tonumber / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ"))
            updated_on: .updatedDate | (tonumber / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ"))
            merge_commit: .fromRef.latestCommit
            state: .state
            owner: .author.user.emailAddress
            link: .links.self[0].href
            destination: .toRef.displayId
            source: .fromRef.displayId
            mergedAt: .closedDate as $d | if $d == null then null else ($d / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ")) end
            reviewers: "[.reviewers[].user.emailAddress]"
          relations:
            repository: .toRef.repository.slug
            participants: "[.participants[].user.emailAddress]"
```

### User[â](#user "Direct link to User")

User blueprint

Create in Port

```
{
    "identifier": "bitbucketUser",
    "description": "A software catalog to represent Bitbucket users",
    "title": "Bitbucket User",
    "icon": "BitBucket",
    "schema": {
        "properties": {
            "username": {
                "type": "string",
                "title": "Username",
                "description": "The username of the user"
            },
            "url": {
                "title": "URL",
                "description": "The link to the user profile",
                "icon": "BitBucket",
                "type": "string"
            },
            "portUser": {
                "title": "Port User",
                "type": "string",
                "icon": "DefaultProperty",
                "format": "user"
            }
        },
        "required": [
            "username"
        ]
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {}
}
```

Integration configuration

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
          identifier: .emailAddress
          title: .displayName
          blueprint: '"bitbucketUser"'
          properties:
            username: .name
            url: .links.self[0].href
            portUser: .emailAddress
```

## Let's test it[â](#lets-test-it "Direct link to Let's test it")

This section includes sample response data from Bitbucket (Self-Hosted). In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from Bitbucket (Self-Hosted):

Project response data

```
{
  "key": "PROJ",
  "id": 1,
  "name": "Project",
  "public": false,
  "type": "NORMAL",
  "links": {
    "self": [
      {
        "href": "http://localhost:7990/projects/PROJ"
      }
    ]
  }
}
```

Repository response data

```
{
  "slug": "repostiroy-3",
  "id": 3,
  "name": "Repostiroy-3",
  "hierarchyId": "0a8dadb07bb606236d8c",
  "scmId": "git",
  "state": "AVAILABLE",
  "statusMessage": "Available",
  "forkable": true,
  "project": {
    "key": "PRO3",
    "id": 3,
    "name": "Project Three",
    "public": false,
    "type": "NORMAL",
    "links": {
      "self": [
        {
          "href": "http://localhost:7990/projects/PRO3"
        }
      ]
    }
  },
  "public": false,
  "archived": false,
  "links": {
    "clone": [
      {
        "href": "ssh://git@localhost:7999/pro3/repostiroy-3.git",
        "name": "ssh"
      },
      {
        "href": "http://localhost:7990/scm/pro3/repostiroy-3.git",
        "name": "http"
      }
    ],
    "self": [
      {
        "href": "http://localhost:7990/projects/PRO3/repos/repostiroy-3/browse"
      }
    ]
  },
  "__readme": "",
  "__latestCommit": {
    "id": "965068d1461f119139bb6be582bb22a555a195ba",
    "displayId": "965068d1461",
    "author": {
      "name": "[REDACTED]",
      "emailAddress": "admin@gmail.com",
      "active": true,
      "displayName": "Admin",
      "id": 3,
      "slug": "[REDACTED]",
      "type": "NORMAL",
      "links": {
        "self": [
          {
            "href": "http://localhost:7990/users/[REDACTED]"
          }
        ]
      }
    },
    "authorTimestamp": 1747744649000,
    "committer": {
      "name": "[REDACTED]",
      "emailAddress": "admin@gmail.com",
      "active": true,
      "displayName": "Admin",
      "id": 3,
      "slug": "[REDACTED]",
      "type": "NORMAL",
      "links": {
        "self": [
          {
            "href": "http://localhost:7990/users/[REDACTED]"
          }
        ]
      }
    },
    "committerTimestamp": 1747744649000,
    "message": "Pull request #1: readme.md edited online with Bitbucket\n\nMerge in PRO3/repostiroy-3 from main to master\n\n* commit '3e4df0573a0ba1845ebdfa919c907745497313aa':\n  readme.md edited online with Bitbucket",
    "parents": [
      {
        "id": "9534663d88977c0aa5c25249986eae851fd83a8d",
        "displayId": "9534663d889"
      },
      {
        "id": "3e4df0573a0ba1845ebdfa919c907745497313aa",
        "displayId": "3e4df0573a0"
      }
    ]
  }
}
```

Pull Request response data

```
{
  "id": 1,
  "version": 1,
  "title": "readme.md edited online with Bitbucket",
  "state": "OPEN",
  "open": true,
  "closed": false,
  "draft": false,
  "createdDate": 1747730324792,
  "updatedDate": 1747730324792,
  "fromRef": {
    "id": "refs/heads/main",
    "displayId": "main",
    "latestCommit": "3e4df0573a0ba1845ebdfa919c907745497313aa",
    "type": "BRANCH",
    "repository": {
      "slug": "repostiroy-3",
      "id": 3,
      "name": "Repostiroy 3",
      "hierarchyId": "0a8dadb07bb606236d8c",
      "scmId": "git",
      "state": "AVAILABLE",
      "statusMessage": "Available",
      "forkable": true,
      "project": {
        "key": "PRO3",
        "id": 3,
        "name": "Project Three",
        "public": false,
        "type": "NORMAL",
        "links": {
          "self": [
            {
              "href": "http://localhost:7990/projects/PRO3"
            }
          ]
        }
      },
      "public": false,
      "archived": false,
      "links": {
        "clone": [
          {
            "href": "ssh://git@localhost:7999/pro3/repostiroy-3.git",
            "name": "ssh"
          },
          {
            "href": "http://localhost:7990/scm/pro3/repostiroy-3.git",
            "name": "http"
          }
        ],
        "self": [
          {
            "href": "http://localhost:7990/projects/PRO3/repos/repostiroy-3/browse"
          }
        ]
      }
    }
  },
  "toRef": {
    "id": "refs/heads/master",
    "displayId": "master",
    "latestCommit": "9534663d88977c0aa5c25249986eae851fd83a8d",
    "type": "BRANCH",
    "repository": {
      "slug": "repostiroy-3",
      "id": 3,
      "name": "Repostiroy 3",
      "hierarchyId": "0a8dadb07bb606236d8c",
      "scmId": "git",
      "state": "AVAILABLE",
      "statusMessage": "Available",
      "forkable": true,
      "project": {
        "key": "PRO3",
        "id": 3,
        "name": "Project Three",
        "public": false,
        "type": "NORMAL",
        "links": {
          "self": [
            {
              "href": "http://localhost:7990/projects/PRO3"
            }
          ]
        }
      },
      "public": false,
      "archived": false,
      "links": {
        "clone": [
          {
            "href": "ssh://git@localhost:7999/pro3/repostiroy-3.git",
            "name": "ssh"
          },
          {
            "href": "http://localhost:7990/scm/pro3/repostiroy-3.git",
            "name": "http"
          }
        ],
        "self": [
          {
            "href": "http://localhost:7990/projects/PRO3/repos/repostiroy-3/browse"
          }
        ]
      }
    }
  },
  "locked": false,
  "author": {
    "user": {
      "name": "[REDACTED]",
      "emailAddress": "admin@gmail.com",
      "active": true,
      "displayName": "Admin",
      "id": 3,
      "slug": "[REDACTED]",
      "type": "NORMAL",
      "links": {
        "self": [
          {
            "href": "http://localhost:7990/users/[REDACTED]"
          }
        ]
      }
    },
    "role": "AUTHOR",
    "approved": false,
    "status": "UNAPPROVED"
  },
  "reviewers": [],
  "participants": [],
  "properties": {
    "mergeResult": {
      "outcome": "CLEAN",
      "current": false
    },
    "resolvedTaskCount": 0,
    "commentCount": 0,
    "openTaskCount": 0
  },
  "links": {
    "self": [
      {
        "href": "http://localhost:7990/projects/PRO3/repos/repostiroy-3/pull-requests/1"
      }
    ]
  }
}
```

User response data

```
{
  "name": "[REDACTED]",
  "emailAddress": "admin@gmail.com",
  "active": true,
  "displayName": "Admin",
  "id": 3,
  "slug": "[REDACTED]",
  "type": "NORMAL",
  "links": {
    "self": [
      {
        "href": "http://localhost:7990/users/[REDACTED]"
      }
    ]
  }
}  
```

### Mapping result[â](#mapping-result "Direct link to Mapping result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Project entity in Port

```
{
  "blueprint": "bitbucketProject",
  "identifier": "PROJ",
  "createdAt": "2025-05-20T09:14:22.361Z",
  "updatedBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "createdBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "team": [],
  "title": "Project",
  "relations": {},
  "properties": {
    "public": false,
    "link": "http://localhost:7990/projects/PROJ",
    "description": null,
    "type": "NORMAL"
  },
  "updatedAt": "2025-05-22T20:46:27.616Z"
}
```

Repository entity in Port

```
{
  "blueprint": "bitbucketRepository",
  "identifier": "repostiroy-3",
  "createdAt": "2025-05-20T13:14:09.505Z",
  "updatedBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "createdBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "team": [],
  "title": "Repostiroy-3",
  "relations": {
    "project": "PRO3",
    "latestCommitAuthor": "admin@gmail.com"
  },
  "properties": {
    "public": false,
    "documentation": "",
    "link": "http://localhost:7990/projects/PRO3/repos/repostiroy-3/browse",
    "forkable": true,
    "description": null,
    "state": "AVAILABLE",
    "readme": null,
    "swagger_url": null
  },
  "updatedAt": "2025-05-20T13:14:09.505Z"
}
```

Pull Request entity in Port

```
{
  "blueprint": "bitbucketPullRequest",
  "identifier": "1",
  "createdAt": "2025-05-20T09:22:29.565Z",
  "updatedBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "createdBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "team": [],
  "title": "readme.md edited online with Bitbucket",
  "relations": {
    "repository": "repostiroy-3",
    "participants": []
  },
  "properties": {
    "updated_on": "2025-05-20T12:37:29Z",
    "owner": "admin@gmail.com",
    "created_on": "2025-05-20T08:38:44Z",
    "mergedAt": "2025-05-20T12:37:29Z",
    "link": "http://localhost:7990/projects/PRO3/repos/repostiroy-3/pull-requests/1",
    "destination": "master",
    "description": null,
    "state": "MERGED",
    "source": "main",
    "reviewers": [],
    "merge_commit": "3e4df0573a0ba1845ebdfa919c907745497313aa"
  },
  "updatedAt": "2025-05-20T12:37:34.111Z"
}
```

User entity in Port

```
{
  "blueprint": "bitbucketUser",
  "identifier": "admin@gmail.com",
  "createdAt": "2025-05-20T09:10:04.195Z",
  "updatedBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "createdBy": "jqoQ34Azuy08BJFFUZAKyP3sXranvmgc",
  "team": [],
  "title": "Admin",
  "relations": {},
  "properties": {
    "portUser": "admin@gmail.com",
    "url": "http://localhost:7990/users/admin",
    "username": "admin"
  },
  "updatedAt": "2025-05-20T09:10:04.195Z"
}
```

## GitOps[â](#gitops "Direct link to GitOps")

The Bitbucket (Self-Hosted) Ocean integration by itself does not support GitOps yet. This capability is planned for a future release and is WIP. If you really need GitOps support, you can use the [webhook gitops](/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-server/gitops.md) installation method.

## Alternative installation via webhooks[â](#alternative-installation-via-webhooks "Direct link to Alternative installation via webhooks")

While the Ocean integration described above is the recommended installation method, you may prefer to use a webhook to ingest users, projects, repositories and pull request entities from Bitbucket (Self-Hosted). If so, use the following instructions:

**Note** that when using this method, data will be ingested into Port only when the webhook is triggered.

**Webhook installation (click to expand)**

### Port configuration

Create the following blueprint definitions:

Bitbucket project blueprint

Create in Port

```
{
  "identifier": "bitbucketProject",
  "description": "A software catalog to represent Bitbucket project",
  "title": "Bitbucket Project",
  "icon": "BitBucket",
  "schema": {
    "properties": {
      "public": {
        "icon": "DefaultProperty",
        "title": "Public",
        "type": "boolean"
      },
      "description": {
        "title": "Description",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "type": {
        "icon": "DefaultProperty",
        "title": "Type",
        "type": "string"
      },
      "link": {
        "title": "Link",
        "icon": "DefaultProperty",
        "type": "string"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Bitbucket user blueprint

Create in Port

```
{
  "identifier": "bitbucketUser",
  "description": "A software catalog to represent Bitbucket users",
  "title": "Bitbucket User",
  "icon": "BitBucket",
  "schema": {
    "properties": {
      "username": {
        "type": "string",
        "title": "Username",
        "description": "The username of the user"
      },
      "url": {
        "title": "URL",
        "description": "The link to the user profile",
        "icon": "BitBucket",
        "type": "string"
      }
    },
    "required": [
      "username"
    ]
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

Bitbucket repository blueprint

Create in Port

```
{
  "identifier": "bitbucketRepository",
  "description": "A software catalog to represent Bitbucket repositories",
  "title": "Bitbucket Repository",
  "icon": "BitBucket",
  "schema": {
    "properties": {
      "forkable": {
        "icon": "DefaultProperty",
        "title": "Is Forkable",
        "type": "boolean"
      },
      "description": {
        "title": "Description",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "public": {
        "icon": "DefaultProperty",
        "title": "Is Public",
        "type": "boolean"
      },
      "state": {
        "icon": "DefaultProperty",
        "title": "State",
        "type": "string"
      },
      "link": {
        "title": "Link",
        "icon": "DefaultProperty",
        "type": "string"
      },
      "documentation": {
        "icon": "DefaultProperty",
        "title": "Documentation",
        "type": "string",
        "format": "markdown"
      },
      "swagger_url": {
        "title": "Swagger URL",
        "type": "string",
        "format": "url",
        "spec": "async-api",
        "icon": "DefaultProperty"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "latestCommitAuthor": {
      "title": "Latest Commit By",
      "description": "The user that made the most recent commit to the base branch",
      "target": "bitbucketUser",
      "required": false,
      "many": false
    },
    "project": {
      "title": "Project",
      "target": "bitbucketProject",
      "required": false,
      "many": false
    }
  }
}
```

Bitbucket pull request blueprint

Create in Port

```
{
  "identifier": "bitbucketPullrequest",
  "description": "A software catalog to represent Bitbucket pull requests",
  "title": "Bitbucket Pull Request",
  "icon": "BitBucket",
  "schema": {
    "properties": {
      "created_on": {
        "title": "Created On",
        "type": "string",
        "format": "date-time",
        "icon": "DefaultProperty"
      },
      "updated_on": {
        "title": "Updated On",
        "type": "string",
        "format": "date-time",
        "icon": "DefaultProperty"
      },
      "description": {
        "title": "Description",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "state": {
        "icon": "DefaultProperty",
        "title": "State",
        "type": "string",
        "enum": [
          "OPEN",
          "MERGED",
          "DECLINED",
          "SUPERSEDED"
        ],
        "enumColors": {
          "OPEN": "yellow",
          "MERGED": "green",
          "DECLINED": "red",
          "SUPERSEDED": "purple"
        }
      },
      "owner": {
        "title": "Owner",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "link": {
        "title": "Link",
        "icon": "DefaultProperty",
        "type": "string"
      },
      "destination": {
        "title": "Destination Branch",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "source": {
        "title": "Source Branch",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "reviewers": {
        "items": {
          "type": "string"
        },
        "title": "Reviewers",
        "type": "array",
        "icon": "DefaultProperty"
      },
      "merge_commit": {
        "title": "Merge Commit",
        "type": "string",
        "icon": "DefaultProperty"
      },
      "mergedAt": {
        "title": "Merged At",
        "type": "string",
        "format": "date-time",
        "icon": "DefaultProperty"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "participants": {
      "title": "Participants",
      "description": "Users that contributed to the PR",
      "target": "bitbucketUser",
      "required": false,
      "many": true
    },
    "repository": {
      "title": "Repository",
      "target": "bitbucketRepository",
      "required": false,
      "many": false
    }
  }
}
```

Blueprint Properties

You may modify the properties in your blueprints depending on what you want to track in your Bitbucket account.

### Let's test it

This section includes a sample webhook event sent from Bitbucket when a pull request is merged. In addition, it includes the entity created from the event based on the webhook configuration provided in the previous section.

#### Payload

Here is an example of the payload structure sent to the webhook URL when a Bitbucket pull request is merged:

Webhook event payload

```
{
  "body": {
    "eventKey": "pr:merged",
    "date": "2023-11-16T11:03:42+0000",
    "actor": {
      "name": "admin",
      "emailAddress": "username@gmail.com",
      "active": true,
      "displayName": "Test User",
      "id": 2,
      "slug": "admin",
      "type": "NORMAL",
      "links": {
        "self": [
          {
            "href": "http://myhost:7990/users/admin"
          }
        ]
      }
    },
    "pullRequest": {
      "id": 2,
      "version": 2,
      "title": "lint code",
      "description": "here is the description",
      "state": "MERGED",
      "open": false,
      "closed": true,
      "createdDate": 1700132280533,
      "updatedDate": 1700132622026,
      "closedDate": 1700132622026,
      "fromRef": {
        "id": "refs/heads/dev",
        "displayId": "dev",
        "latestCommit": "9e08604e14fa72265d65696608725c2b8f7850f2",
        "type": "BRANCH",
        "repository": {
          "slug": "data-analyses",
          "id": 1,
          "name": "data analyses",
          "description": "This is for my repository and all the blah blah blah",
          "hierarchyId": "24cfae4b0dd7bade7edc",
          "scmId": "git",
          "state": "AVAILABLE",
          "statusMessage": "Available",
          "forkable": true,
          "project": {
            "key": "MOPP",
            "id": 1,
            "name": "My On Prem Project",
            "description": "On premise test project is sent to us for us",
            "public": false,
            "type": "NORMAL",
            "links": {
              "self": [
                {
                  "href": "http://myhost:7990/projects/MOPP"
                }
              ]
            }
          },
          "public": false,
          "archived": false,
          "links": {
            "clone": [
              {
                "href": "ssh://git@myhost:7999/mopp/data-analyses.git",
                "name": "ssh"
              },
              {
                "href": "http://myhost:7990/scm/mopp/data-analyses.git",
                "name": "http"
              }
            ],
            "self": [
              {
                "href": "http://myhost:7990/projects/MOPP/repos/data-analyses/browse"
              }
            ]
          }
        }
      },
      "toRef": {
        "id": "refs/heads/main",
        "displayId": "main",
        "latestCommit": "e461aae894b6dc951f405dca027a3f5567ea6bee",
        "type": "BRANCH",
        "repository": {
          "slug": "data-analyses",
          "id": 1,
          "name": "data analyses",
          "description": "This is for my repository and all the blah blah blah",
          "hierarchyId": "24cfae4b0dd7bade7edc",
          "scmId": "git",
          "state": "AVAILABLE",
          "statusMessage": "Available",
          "forkable": true,
          "project": {
            "key": "MOPP",
            "id": 1,
            "name": "My On Prem Project",
            "description": "On premise test project is sent to us for us",
            "public": false,
            "type": "NORMAL",
            "links": {
              "self": [
                {
                  "href": "http://myhost:7990/projects/MOPP"
                }
              ]
            }
          },
          "public": false,
          "archived": false,
          "links": {
            "clone": [
              {
                "href": "ssh://git@myhost:7999/mopp/data-analyses.git",
                "name": "ssh"
              },
              {
                "href": "http://myhost:7990/scm/mopp/data-analyses.git",
                "name": "http"
              }
            ],
            "self": [
              {
                "href": "http://myhost:7990/projects/MOPP/repos/data-analyses/browse"
              }
            ]
          }
        }
      },
      "locked": false,
      "author": {
        "user": {
          "name": "admin",
          "emailAddress": "username@gmail.com",
          "active": true,
          "displayName": "Test User",
          "id": 2,
          "slug": "admin",
          "type": "NORMAL",
          "links": {
            "self": [
              {
                "href": "http://myhost:7990/users/admin"
              }
            ]
          }
        },
        "role": "AUTHOR",
        "approved": false,
        "status": "UNAPPROVED"
      },
      "reviewers": [],
      "participants": [],
      "properties": {
        "mergeCommit": {
          "displayId": "1cbccf99220",
          "id": "1cbccf99220b23f89624c7c604f630663a1aaf8e"
        }
      },
      "links": {
        "self": [
          {
            "href": "http://myhost:7990/projects/MOPP/repos/data-analyses/pull-requests/2"
          }
        ]
      }
    }
  },
  "headers": {
    "X-Forwarded-For": "10.0.148.57",
    "X-Forwarded-Proto": "https",
    "X-Forwarded-Port": "443",
    "Host": "ingest.getport.io",
    "X-Amzn-Trace-Id": "Self=1-6555f719-267a0fce1e7a4d8815de94f7;Root=1-6555f719-1906872f41621b17250bb83a",
    "Content-Length": "2784",
    "User-Agent": "Atlassian HttpClient 3.0.4 / Bitbucket-8.15.1 (8015001) / Default",
    "Content-Type": "application/json; charset=UTF-8",
    "accept": "*/*",
    "X-Event-Key": "pr:merged",
    "X-Hub-Signature": "sha256=bf366faf8d8c41a4af21d25d922b87c3d1d127b5685238b099d2f311ad46e978",
    "X-Request-Id": "d5fa6a16-bb6c-40d6-9c50-bc4363e79632",
    "via": "HTTP/1.1 AmazonAPIGateway",
    "forwarded": "for=154.160.30.235;host=ingest.getport.io;proto=https"
  },
  "queryParams": {}
}
```

Mapping result

```
{
   "identifier":"2",
   "title":"lint code",
   "blueprint":"bitbucketPullrequest",
   "properties":{
      "created_on":"2023-11-16T10:58:00Z",
      "updated_on":"2023-11-16T11:03:42Z",
      "merge_commit":"9e08604e14fa72265d65696608725c2b8f7850f2",
      "state":"MERGED",
      "owner":"Test User",
      "link":"http://myhost:7990/projects/MOPP/repos/data-analyses/pull-requests/2",
      "destination":"main",
      "source":"dev",
      "participants":[],
      "reviewers":[]
   },
   "relations":{
      "repository":"data-analyses"
   },
   "filter":true
}
```

### Import Bitbucket historical issues

In this example you are going to use the provided Python script to set up webhooks and fetch data from the Bitbucket Server / Bitbucket Data Center API and ingest it to Port.

#### Prerequisites

This example utilizes the [blueprint](#port-configuration) definition from the previous section.

In addition, provide the following environment variables:

* `PORT_CLIENT_ID` - Your Port client id
* `PORT_CLIENT_SECRET` - Your Port client secret
* `BITBUCKET_HOST` - Bitbucket Server / Bitbucket Data Center host such as `http://localhost:7990`
* `BITBUCKET_USERNAME` - Bitbucket username to use when accessing the Bitbucket resources
* `BITBUCKET_PASSWORD` - Bitbucket account password
* `BITBUCKET_PROJECTS_FILTER` - An optional comma separated list of Bitbucket projects to filter. If not provided, all projects will be fetched.
* `WEBHOOK_SECRET` - An optional secret to use when creating a webhook in Port. If not provided, `bitbucket_webhook_secret` will be used.
* `PORT_API_URL` - An optional variable that defaults to the EU Port API `https://api.port.io/v1`. For US organizations use `https://api.us.port.io/v1` instead.
* `BITBUCKET_IS_VERSION8_POINT7_OR_OLDER` - An optional variable that specifies whether the Bitbucket version is older than 8.7. This setting determines if webhooks should be created at the repository level (for older versions `<=8.7`) or at the project level (for newer versions `>=8.8`).
* `PULL_REQUEST_STATE` - An optional variable to specify the state of Bitbucket pull requests to be ingested. Accepted values are `"ALL"`, `"OPEN"`, `"MERGED"`, or `"DECLINED"`. If not specified, the default value is `OPEN`.

Webhook Configuration

This app will automatically set up a webhook that allows Bitbucket to send events to Port. To understand more about how Bitbucket sends event payloads via webhooks, you can refer to [this documentation](https://confluence.atlassian.com/bitbucketserver/event-payload-938025882.html).

Ensure that the Bitbucket credentials you use have `PROJECT_ADMIN` permissions to successfully configure the webhook. For more details on the necessary permissions and setup, see the [official Bitbucket documentation](https://developer.atlassian.com/server/bitbucket/rest/v910/api-group-project/#api-api-latest-projects-projectkey-webhooks-post).

Find your Port credentials using this [guide](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)

Use the following Python script to set up webhook and ingest historical Bitbucket users, projects, repositories and pull requests into port:

Bitbucket Python script

Latest Version

You can pull the latest version of this code by cloning this [repository](https://github.com/port-labs/bitbucket-workspace-data/)

```
import json
import re
import time
from datetime import datetime, timedelta
import asyncio
from typing import Any, Optional
import httpx
from decouple import config
from loguru import logger
from httpx import BasicAuth

# These are the credentials passed by the variables of your pipeline to your tasks and into your env
PORT_CLIENT_ID = config("PORT_CLIENT_ID")
PORT_CLIENT_SECRET = config("PORT_CLIENT_SECRET")
BITBUCKET_USERNAME = config("BITBUCKET_USERNAME")
BITBUCKET_PASSWORD = config("BITBUCKET_PASSWORD")
BITBUCKET_API_URL = config("BITBUCKET_HOST")
BITBUCKET_PROJECTS_FILTER = config(
    "BITBUCKET_PROJECTS_FILTER", cast=lambda v: v.split(",") if v else None, default=[]
)
PORT_API_URL = config("PORT_API_URL", default="https://api.port.io/v1")
WEBHOOK_SECRET = config("WEBHOOK_SECRET", default="bitbucket_webhook_secret")
IS_VERSION_8_7_OR_OLDER = config("IS_VERSION_8_7_OR_OLDER", default=False)
VALID_PULL_REQUEST_STATES = {"ALL", "OPEN", "MERGED", "DECLINED"}
PULL_REQUEST_STATE = config("PULL_REQUEST_STATE", default="OPEN").upper()


# According to https://support.atlassian.com/bitbucket-cloud/docs/api-request-limits/
RATE_LIMIT = 1000  # Maximum number of requests allowed per hour
RATE_PERIOD = 3600  # Rate limit reset period in seconds (1 hour)
WEBHOOK_IDENTIFIER = "bitbucket_mapper"
WEBHOOK_EVENTS = [
    "repo:modified",
    "project:modified",
    "pr:modified",
    "pr:opened",
    "pr:merged",
    "pr:reviewer:updated",
    "pr:declined",
    "pr:deleted",
    "pr:comment:deleted",
    "pr:from_ref_updated",
    "pr:comment:edited",
    "pr:reviewer:unapproved",
    "pr:reviewer:needs_work",
    "pr:reviewer:approved",
    "pr:comment:added",
]

# Initialize rate limiting variables
request_count = 0
rate_limit_start = time.time()
port_access_token, token_expiry_time = None, datetime.now()
port_headers = {}
bitbucket_auth = BasicAuth(username=BITBUCKET_USERNAME, password=BITBUCKET_PASSWORD)
client = httpx.AsyncClient(timeout=httpx.Timeout(60))


async def get_access_token():
    credentials = {"clientId": PORT_CLIENT_ID, "clientSecret": PORT_CLIENT_SECRET}
    token_response = await client.post(
        f"{PORT_API_URL}/auth/access_token", json=credentials
    )
    response_data = token_response.json()
    access_token = response_data["accessToken"]
    expires_in = response_data["expiresIn"]
    token_expiry_time = datetime.now() + timedelta(seconds=expires_in)
    return access_token, token_expiry_time


async def refresh_access_token():
    global port_access_token, token_expiry_time, port_headers
    logger.info("Refreshing access token...")
    port_access_token, token_expiry_time = await get_access_token()
    port_headers = {"Authorization": f"Bearer {port_access_token}"}
    logger.info(f"New token received. Expiry time: {token_expiry_time}")


async def refresh_token_if_expired():
    if datetime.now() >= token_expiry_time:
        await refresh_access_token()


async def refresh_token_and_retry(method: str, url: str, **kwargs):
    await refresh_access_token()
    response = await client.request(method, url, headers=port_headers, **kwargs)
    return response


def sanitize_identifier(identifier: str) -> str:
    pattern = r"[^A-Za-z0-9@_.+:\/=-]"
    # Replace any character that does not match the pattern with an underscore
    return re.sub(pattern, "_", identifier)


async def send_port_request(method: str, endpoint: str, payload: Optional[dict] = None):
    global port_access_token, token_expiry_time, port_headers
    await refresh_token_if_expired()
    url = f"{PORT_API_URL}/{endpoint}"
    try:
        response = await client.request(method, url, headers=port_headers, json=payload)
        response.raise_for_status()
        return response
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            logger.info("Received 401 Unauthorized. Refreshing token and retrying...")
            try:
                response = await refresh_token_and_retry(method, url, json=payload)
                response.raise_for_status()
                return response
            except httpx.HTTPStatusError as e:
                logger.error(
                    f"Error after retrying: {e.response.status_code}, {e.response.text}"
                )
                return {"status_code": e.response.status_code, "response": e.response}
        else:
            logger.error(
                f"HTTP error occurred: {e.response.status_code}, {e.response.text}"
            )
            return {"status_code": e.response.status_code, "response": e.response}
    except httpx.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        return {"status_code": None, "error": e}


async def get_or_create_port_webhook():
    logger.info("Checking if a Bitbucket webhook is configured on Port...")
    response = await send_port_request(
        method="GET", endpoint=f"webhooks/{WEBHOOK_IDENTIFIER}"
    )
    if isinstance(response, dict):
        if response.get("status_code") == 404:
            logger.info("Port webhook not found, creating a new one.")
            return await create_port_webhook()
        else:
            return None
    else:
        webhook_url = response.json().get("integration", {}).get("url")
        logger.info(f"Webhook configuration exists in Port. URL: {webhook_url}")
        return webhook_url


async def create_port_webhook():
    logger.info("Creating a webhook for Bitbucket on Port...")
    with open("./resources/webhook_configuration.json", "r") as file:
        mappings = json.load(file)
    webhook_data = {
        "identifier": WEBHOOK_IDENTIFIER,
        "title": "Bitbucket Webhook",
        "description": "Webhook for receiving Bitbucket events",
        "icon": "BitBucket",
        "mappings": mappings,
        "enabled": True,
        "security": {
            "secret": WEBHOOK_SECRET,
            "signatureHeaderName": "x-hub-signature",
            "signatureAlgorithm": "sha256",
            "signaturePrefix": "sha256=",
            "requestIdentifierPath": ".headers['x-request-id']",
        },
        "integrationType": "custom",
    }
    response = await send_port_request(
        method="POST", endpoint="webhooks", payload=webhook_data
    )
    if isinstance(response, dict):
        if response.get("status_code") == 442:
            logger.error("Incorrect mapping, kindly fix!")
        return None
    else:
        webhook_url = response.json().get("integration", {}).get("url")
        logger.info(
            f"Webhook configuration successfully created in Port: {webhook_url}"
        )
        return webhook_url


def generate_webhook_data(webhook_url: str, events: list[str]) -> dict:
    return {
        "name": "Port Webhook",
        "url": webhook_url,
        "events": events,
        "active": True,
        "sslVerificationRequired": True,
        "configuration": {"secret": WEBHOOK_SECRET, "createdBy": "Port"},
    }


async def create_project_level_webhook(
    project_key: str, webhook_url: str, events: list[str]
):
    logger.info(f"Creating project-level webhook for project: {project_key}")
    webhook_data = generate_webhook_data(webhook_url, events)

    try:
        response = await client.post(
            f"{BITBUCKET_API_URL}/rest/api/1.0/projects/{project_key}/webhooks",
            json=webhook_data,
            auth=bitbucket_auth,
        )
        response.raise_for_status()
        logger.info(f"Successfully created project-level webhook for {project_key}")
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(
            f"HTTP error when creating webhook for project: {project_key} code: {e.response.status_code} response: {e.response.text}"
        )
        return None


async def create_repo_level_webhook(
    project_key: str, repo_key: str, webhook_url: str, events: list[str]
):
    logger.info(f"Creating repo-level webhook for repo: {repo_key}")
    webhook_data = generate_webhook_data(webhook_url, events)

    try:
        response = await client.post(
            f"{BITBUCKET_API_URL}/rest/api/1.0/projects/{project_key}/repos/{repo_key}/webhooks",
            json=webhook_data,
            auth=bitbucket_auth,
        )
        response.raise_for_status()
        logger.info(f"Successfully created repo-level webhook for {repo_key}")
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(
            f"HTTP error when creating webhook for repo: {repo_key} code: {e.response.status_code} response: {e.response.text}"
        )
        return None


async def get_or_create_bitbucket_webhook(
    project_key: str,
    webhook_url: str,
    events: list[str],
    repo_key: Optional[str] = None,
):
    logger.info(f"Checking webhooks for {repo_key or project_key}")
    if webhook_url is not None:
        try:
            matching_webhooks = [
                webhook
                async for project_webhooks_batch in get_paginated_resource(
                    path=(
                        f"projects/{project_key}/repos/{repo_key}/webhooks"
                        if repo_key
                        else f"projects/{project_key}/webhooks"
                    )
                )
                for webhook in project_webhooks_batch
                if webhook["url"] == webhook_url
            ]
            if matching_webhooks:
                logger.info(f"Webhook already exists for {repo_key or project_key}.")
                return matching_webhooks[0]
            logger.info(
                f"Webhook not found for {repo_key or project_key}. Creating a new one."
            )
            if repo_key:
                return await create_repo_level_webhook(
                    project_key, repo_key, webhook_url, events
                )
            else:
                return await create_project_level_webhook(
                    project_key, webhook_url, events
                )
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error when checking webhooks for project: {project_key} code: {e.response.status_code} response: {e.response.text}"
            )
            return None
    else:
        logger.error("Port webhook URL is not available. Skipping webhook check...")
        return None


async def add_entity_to_port(blueprint_id, entity_object):
    response = await send_port_request(
        method="POST",
        endpoint=f"blueprints/{blueprint_id}/entities?upsert=true&merge=true",
        payload=entity_object,
    )
    if not isinstance(response, dict):
        logger.info(response.json())


async def get_paginated_resource(
    path: str,
    params: dict[str, Any] = None,
    page_size: int = 25,
    full_response: bool = False,
):
    global request_count, rate_limit_start

    # Check if we've exceeded the rate limit, and if so, wait until the reset period is over
    if request_count >= RATE_LIMIT:
        elapsed_time = time.time() - rate_limit_start
        if elapsed_time < RATE_PERIOD:
            sleep_time = RATE_PERIOD - elapsed_time
            await asyncio.sleep(sleep_time)

        # Reset the rate limiting variables
        request_count = 0
        rate_limit_start = time.time()

    url = f"{BITBUCKET_API_URL}/rest/api/1.0/{path}"
    params = params or {}
    params["limit"] = page_size
    next_page_start = None

    while True:
        try:
            if next_page_start:
                params["start"] = next_page_start

            response = await client.get(url=url, auth=bitbucket_auth, params=params)
            response.raise_for_status()
            page_json = response.json()
            request_count += 1
            logger.debug(
                f"Requested data for {path}, with params: {params} and response code: {response.status_code}"
            )
            if full_response:
                yield page_json
            else:
                batch_data = page_json["values"]
                yield batch_data

            next_page_start = page_json.get("nextPageStart")
            if not next_page_start:
                break
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                logger.info(
                    f"Could not find the requested resources {path}. Terminating gracefully..."
                )
                return
            logger.error(
                f"HTTP error with code {e.response.status_code}, content: {e.response.text}"
            )
        except httpx.HTTPError as e:
            logger.error(f"HTTP occurred while fetching Bitbucket data: {e}")
        logger.info(f"Successfully fetched paginated data for {path}")


async def get_single_project(project_key: str):
    response = await client.get(
        f"{BITBUCKET_API_URL}/rest/api/1.0/projects/{project_key}", auth=bitbucket_auth
    )
    response.raise_for_status()
    return response.json()


def convert_to_datetime(timestamp: int):
    converted_datetime = datetime.utcfromtimestamp(timestamp / 1000.0)
    return converted_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_repository_file_response(file_response: dict[str, Any]) -> str:
    lines = file_response.get("lines", [])
    logger.info(f"Received readme file with {len(lines)} entries")
    readme_content = ""

    for line in lines:
        readme_content += line.get("text", "") + "\n"

    return readme_content


async def process_user_entities(users_data: list[dict[str, Any]]):
    blueprint_id = "bitbucketUser"

    for user in users_data:
        entity = {
            "title": user.get("displayName"),
            "properties": {
                "username": user.get("name"),
                "url": user.get("links", {}).get("self", [{}])[0].get("href"),
            },
            "relations": {},
        }
        identifier = str(user.get("emailAddress"))
        if identifier:
            entity["identifier"] = sanitize_identifier(identifier)
        await add_entity_to_port(blueprint_id=blueprint_id, entity_object=entity)


async def process_project_entities(projects_data: list[dict[str, Any]]):
    blueprint_id = "bitbucketProject"

    for project in projects_data:
        entity = {
            "title": project.get("name"),
            "properties": {
                "description": project.get("description"),
                "public": project.get("public"),
                "type": project.get("type"),
                "link": project.get("links", {}).get("self", [{}])[0].get("href"),
            },
            "relations": {},
        }
        identifier = str(project.get("key"))
        if identifier:
            entity["identifier"] = sanitize_identifier(identifier)
        await add_entity_to_port(blueprint_id=blueprint_id, entity_object=entity)


async def process_repository_entities(repository_data: list[dict[str, Any]]):
    blueprint_id = "bitbucketRepository"

    for repo in repository_data:
        readme_content = await get_repository_readme(
            project_key=repo["project"]["key"], repo_slug=repo["slug"]
        )
        entity = {
            "title": repo.get("name"),
            "properties": {
                "description": repo.get("description"),
                "state": repo.get("state"),
                "forkable": repo.get("forkable"),
                "public": repo.get("public"),
                "link": repo.get("links", {}).get("self", [{}])[0].get("href"),
                "documentation": readme_content,
                "swagger_url": f"https://api.{repo.get('slug')}.com",
            },
            "relations": dict(
                project=repo.get("project", {}).get("key"),
                latestCommitAuthor=repo.get("__latestCommit", {})
                .get("committer", {})
                .get("emailAddress"),
            ),
        }
        identifier = str(repo.get("slug"))
        if identifier:
            entity["identifier"] = sanitize_identifier(identifier)
        await add_entity_to_port(blueprint_id=blueprint_id, entity_object=entity)


async def process_pullrequest_entities(pullrequest_data: list[dict[str, Any]]):
    blueprint_id = "bitbucketPullrequest"

    for pr in pullrequest_data:
        entity = {
            "title": pr.get("title"),
            "properties": {
                "created_on": convert_to_datetime(pr.get("createdDate")),
                "updated_on": convert_to_datetime(pr.get("updatedDate")),
                "mergedAt": convert_to_datetime(pr.get("closedDate", 0)),
                "merge_commit": pr.get("fromRef", {}).get("latestCommit"),
                "description": pr.get("description"),
                "state": pr.get("state"),
                "owner": pr.get("author", {}).get("user", {}).get("emailAddress"),
                "link": pr.get("links", {}).get("self", [{}])[0].get("href"),
                "destination": pr.get("toRef", {}).get("displayId"),
                "reviewers": [
                    reviewer_email
                    for reviewer in pr.get("reviewers", [])
                    if (reviewer_email := reviewer.get("user", {}).get("emailAddress"))
                ],
                "source": pr.get("fromRef", {}).get("displayId"),
            },
            "relations": {
                "repository": pr["toRef"]["repository"]["slug"],
                "participants": [
                    email
                    for email in [
                        pr.get("author", {}).get("user", {}).get("emailAddress")
                    ]
                    + [
                        user.get("user", {}).get("emailAddress", "")
                        for user in pr.get("participants", [])
                    ]
                    if email
                ],
            },
        }
        identifier = str(pr.get("id"))
        if identifier:
            entity["identifier"] = sanitize_identifier(identifier)
        await add_entity_to_port(blueprint_id=blueprint_id, entity_object=entity)


async def get_repository_readme(project_key: str, repo_slug: str) -> str:
    file_path = f"projects/{project_key}/repos/{repo_slug}/browse/README.md"
    readme_content = ""
    async for readme_file_batch in get_paginated_resource(
        path=file_path, page_size=500, full_response=True
    ):
        file_content = parse_repository_file_response(readme_file_batch)
        readme_content += file_content
    return readme_content


async def get_latest_commit(project_key: str, repo_slug: str) -> dict[str, Any]:
    try:
        commit_path = f"projects/{project_key}/repos/{repo_slug}/commits"
        async for commit_batch in get_paginated_resource(path=commit_path):
            if commit_batch:
                latest_commit = commit_batch[0]
                return latest_commit
            return {}
    except Exception as e:
        logger.error(f"Error fetching latest commit for repo {repo_slug}: {e}")
    return {}


async def get_repositories(project: dict[str, Any], port_webhook_url: str):
    repositories_path = f"projects/{project['key']}/repos"
    async for repositories_batch in get_paginated_resource(path=repositories_path):
        logger.info(
            f"received repositories batch with size {len(repositories_batch)} from project: {project['key']}"
        )
        await process_repository_entities(
            repository_data=[
                {
                    **repo,
                    "__latestCommit": await get_latest_commit(
                        project_key=project["key"], repo_slug=repo["slug"]
                    ),
                }
                for repo in repositories_batch
            ]
        )
        if IS_VERSION_8_7_OR_OLDER:
            [
                await get_or_create_bitbucket_webhook(
                    project_key=project["key"],
                    repo_key=repo["slug"],
                    webhook_url=port_webhook_url,
                    events=WEBHOOK_EVENTS,
                )
                for repo in repositories_batch
            ]
        await get_repository_pull_requests(repository_batch=repositories_batch)


async def get_repository_pull_requests(repository_batch: list[dict[str, Any]]):
    global PULL_REQUEST_STATE
    for repository in repository_batch:
        pull_requests_path = f"projects/{repository['project']['key']}/repos/{repository['slug']}/pull-requests"
        if PULL_REQUEST_STATE not in VALID_PULL_REQUEST_STATES:
            logger.warning(
                f"Invalid PULL_REQUEST_STATE '{PULL_REQUEST_STATE}' provided. Defaulting to 'OPEN'."
            )
            PULL_REQUEST_STATE = "OPEN"
        async for pull_requests_batch in get_paginated_resource(
            path=pull_requests_path,
            params={"state": PULL_REQUEST_STATE},
        ):
            logger.info(
                f"received pull requests batch with size {len(pull_requests_batch)} from repo: {repository['slug']}"
            )
            await process_pullrequest_entities(pullrequest_data=pull_requests_batch)


async def main():
    logger.info("Starting Bitbucket data extraction")
    async for users_batch in get_paginated_resource(path="admin/users"):
        logger.info(f"received users batch with size {len(users_batch)}")
        await process_user_entities(users_data=users_batch)

    project_path = "projects"
    if BITBUCKET_PROJECTS_FILTER:

        async def filtered_projects_generator():
            yield [await get_single_project(key) for key in BITBUCKET_PROJECTS_FILTER]

        projects = filtered_projects_generator()
    else:
        projects = get_paginated_resource(path=project_path)

    port_webhook_url = await get_or_create_port_webhook()
    if not port_webhook_url:
        logger.error("Failed to get or create Port webhook. Skipping webhook setup...")

    async for projects_batch in projects:
        logger.info(f"received projects batch with size {len(projects_batch)}")
        await process_project_entities(projects_data=projects_batch)

        for project in projects_batch:
            await get_repositories(project=project, port_webhook_url=port_webhook_url)
            if not IS_VERSION_8_7_OR_OLDER:
                await get_or_create_bitbucket_webhook(
                    project_key=project["key"],
                    webhook_url=port_webhook_url,
                    events=WEBHOOK_EVENTS,
                )
    logger.info("Bitbucket data extraction completed")
    await client.aclose()


if __name__ == "__main__":
    asyncio.run(main())
```

Bitbucket webhook configuration

```
[
  {
    "blueprint": "bitbucketProject",
    "filter": ".body.eventKey == \"project:modified\"",
    "entity": {
      "identifier": ".body.new.key | tostring",
      "title": ".body.new.name",
      "properties": {
        "public": ".body.new.public",
        "type": ".body.new.type",
        "description": ".body.new.description",
        "link": ".body.new.links.self[0].href"
      }
    }
  },
  {
    "blueprint": "bitbucketRepository",
    "filter": ".body.eventKey == \"repo:modified\"",
    "entity": {
      "identifier": ".body.new.slug",
      "title": ".body.new.name",
      "properties": {
        "description": ".body.new.description",
        "state": ".body.new.state",
        "forkable": ".body.new.forkable",
        "public": ".body.new.public",
        "link": ".body.new.links.self[0].href"
      },
      "relations": {
        "project": ".body.new.project.key"
      }
    }
  },
  {
    "blueprint": "bitbucketPullrequest",
    "filter": ".body.eventKey | startswith(\"pr:\")",
    "entity": {
      "identifier": ".body.pullRequest.id | tostring",
      "title": ".body.pullRequest.title",
      "properties": {
        "created_on": ".body.pullRequest.createdDate | (tonumber / 1000 | strftime(\"%Y-%m-%dT%H:%M:%SZ\"))",
        "updated_on": ".body.pullRequest.updatedDate | (tonumber / 1000 | strftime(\"%Y-%m-%dT%H:%M:%SZ\"))",
        "merge_commit": ".body.pullRequest.fromRef.latestCommit",
        "state": ".body.pullRequest.state",
        "owner": ".body.pullRequest.author.user.emailAddress",
        "link": ".body.pullRequest.links.self[0].href",
        "destination": ".body.pullRequest.toRef.displayId",
        "source": ".body.pullRequest.fromRef.displayId",
        "mergedAt": ".body.pullRequest.closedDate | (tonumber / 1000 | strftime(\"%Y-%m-%dT%H:%M:%SZ\"))",
        "reviewers": "[.body.pullRequest.reviewers[].user.emailAddress]"
      },
      "relations": {
        "repository": ".body.pullRequest.toRef.repository.slug",
        "participants": "[.body.pullRequest.participants[].user.emailAddress]"
      }
    }
  }
]
```

Done! you are now able to import historical users, projects, repositories and pull requests from Bitbucket into Port and any change that happens to your project, repository or pull requests in Bitbucket will trigger a webhook event to the webhook URL provided by Port. Port will parse the events and objects according to the mapping and update the catalog entities accordingly.
