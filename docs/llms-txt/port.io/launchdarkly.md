# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/feature-management/launchdarkly.md

# LaunchDarkly

Loading version...

Port's LaunchDarkly integration allows you to model LaunchDarkly resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired LaunchDarkly resources and their metadata in Port (see supported resources below).
* Watch for LaunchDarkly object changes (create/update/delete) in real-time, and automatically apply the changes to your software catalog.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from LaunchDarkly into Port are listed below.<br /><!-- -->It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Project`](https://apidocs.launchdarkly.com/tag/Projects)
* [`Flag`](https://apidocs.launchdarkly.com/tag/Feature-flags)
* [`Environment`](https://apidocs.launchdarkly.com/tag/Environments)
* [`Flag Status`](https://apidocs.launchdarkly.com/tag/Feature-flags#operation/getFeatureFlagStatusAcrossEnvironments)

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [LaunchDarkly<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=LaunchDarkly) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

  **Supported live event triggers (click to expand)**

  * flag
  * environment
  * project
  * auditlog

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

1. Go to the [Launchdarkly<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Launchdarkly) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Launchdarkly<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Launchdarkly<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Launchdarkly<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Launchdarkly
  <!-- -->
  can reach.

If `liveEvents.baseUrl` is not provided, the integration will continue to function correctly. In such a configuration, to retrieve the latest information from the target system, the [`scheduledResyncInterval`](https://ocean.port.io/developing-an-integration/trigger-your-integration) parameter has to be set, or a manual resync will need to be triggered through Port's UI.

Debugging local integrations

To test webhooks or live event delivery to your local environment, expose your local pod or service to the internet using ngrok (e.g. `ngrok http http://localhost:8000`)

<!-- -->

### Securing Your Webhooks

The `integration.config.webhookSecret` parameter secures your webhooks. If not provided, the integration will process webhooks without validating the source of the events.

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

1. Create a `values.yaml` file in `argocd/my-ocean-launchdarkly-integration` in your git repository with the content:

note

Remember to replace the placeholders for `LAUNCHDARKLY_HOST` and `LAUNCHDARKLY_TOKEN`.

```
initializePortResources: true
scheduledResyncInterval: 120
integration:
  identifier: my-ocean-launchdarkly-integration
  type: launchdarkly
  eventListener:
    type: POLLING
  secrets:
    launchdarklyHost: LAUNCHDARKLY_HOST
    launchdarklyToken: LAUNCHDARKLY_TOKEN
```

<br />

2. Install the `my-ocean-launchdarkly-integration` ArgoCD Application by creating the following `my-ocean-launchdarkly-integration.yaml` manifest:

note

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.

Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-launchdarkly-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-launchdarkly-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-launchdarkly-integration/values.yaml
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
kubectl apply -f my-ocean-launchdarkly-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                                 | Description                                                                                                                                                                                           | Required |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                           | Your Port client id                                                                                                                                                                                   | â       |
| `port.clientSecret`                       | Your Port client secret                                                                                                                                                                               | â       |
| `port.baseUrl`                            | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                                     | â       |
| `integration.identifier`                  | Change the identifier to describe your integration                                                                                                                                                    | â       |
| `integration.type`                        | The integration type                                                                                                                                                                                  | â       |
| `integration.eventListener.type`          | The event listener type                                                                                                                                                                               | â       |
| `integration.config.launchdarklyHost`     | Your LaunchDarkly host. For example <https://app.launchdarkly.com> for the default endpoint                                                                                                           | â       |
| `integration.config.launchdarklyToken`    | The LaunchDarkly API token, docs can be found [here](https://docs.launchdarkly.com/home/account/api-create)                                                                                           | â       |
| `integration.config.appHost` (deprecated) | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in LauchDarkly. This field is deprecated. Please use the `liveEvents.baseUrl`field instead | â       |
| `integration.config.webhookSecret`        | Webhook secret for authenticating incoming events.                                                                                                                                                    | â       |
| `liveEvents.baseUrl`                      | The base url of the instance where the LaunchDarkly integration is hosted, used for real-time updates. (e.g.`https://mylaunchdarklyoceanintegration.com`)                                             | â       |
| `scheduledResyncInterval`                 | The number of minutes between each resync                                                                                                                                                             | â       |
| `initializePortResources`                 | Default true, When set to true the integration will create default blueprints and the port App config Mapping                                                                                         | â       |
| `sendRawDataExamples`                     | Default, true, Enable sending raw data examples from the third part API to port for testing and managing the integration mapping                                                                      | â       |

### Event listener

The integration uses polling to pull the configuration from Port every minute and check it for changes. If there is a change, a resync will occur.

This workflow/pipeline will run the LaunchDarkly integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                           | Description                                                                                                                      | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST`     | Your LaunchDarkly host. For example <https://Launchdarkly.com>                                                                   | â       |
| `OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN`    | The LaunchDarkly Cloud API token                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`        | Webhook secret for authenticating incoming events.                                                                               | â       |
| `OCEAN__INTEGRATION__CONFIG__APP_HOST` (deprecated) | Your application's host url. This field is deprecated. Please use the `OCEAN__PORT__BASE_URL` field instead                      | â       |
| `OCEAN__BASE_URL`                                   | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in LaunchDarkly       | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to false the integration will not create default blueprints and the port App config Mapping               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Default, true, Enable sending raw data examples from the third part API to port for testing and managing the integration mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | Change the identifier to describe your integration, if not set will use the default one                                          | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your Port client id                                                                                                              | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your Port client secret                                                                                                          | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                | â       |

<br />

Here is an example for `launchdarkly-integration.yml` workflow file:

```
name: LaunchDarkly Exporter Workflow

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
          type: "launchdarkly"
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            launchdarkly_host: ${{ secrets.OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST }}
            launchdarkly_token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN }}
```

tip

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [LaunchDarkly Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                           | Description                                                                                                                      | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST`     | Your LaunchDarkly host. For example <https://Launchdarkly.com>                                                                   | â       |
| `OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN`    | The LaunchDarkly Cloud API token                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`        | Webhook secret for authenticating incoming events.                                                                               | â       |
| `OCEAN__INTEGRATION__CONFIG__APP_HOST` (deprecated) | Your application's host url. This field is deprecated. Please use the `OCEAN__PORT__BASE_URL` field instead                      | â       |
| `OCEAN__BASE_URL`                                   | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in LaunchDarkly       | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to false the integration will not create default blueprints and the port App config Mapping               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Default, true, Enable sending raw data examples from the third part API to port for testing and managing the integration mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | Change the identifier to describe your integration, if not set will use the default one                                          | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your Port client id                                                                                                              | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your Port client secret                                                                                                          | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run LaunchDarkly Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST', variable: 'OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET')
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="launchdarkly"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST=$OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST \
                                -e OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN=$OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN \
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

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                           | Description                                                                                                                      | Required |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST`     | Your LaunchDarkly host. For example <https://Launchdarkly.com>                                                                   | â       |
| `OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN`    | The LaunchDarkly Cloud API token                                                                                                 | â       |
| `OCEAN__INTEGRATION__CONFIG__WEBHOOK_SECRET`        | Webhook secret for authenticating incoming events.                                                                               | â       |
| `OCEAN__INTEGRATION__CONFIG__APP_HOST` (deprecated) | Your application's host url. This field is deprecated. Please use the `OCEAN__PORT__BASE_URL` field instead                      | â       |
| `OCEAN__BASE_URL`                                   | The host of the Port Ocean app. Used to set up the integration endpoint as the target for webhooks created in LaunchDarkly       | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                  | Default true, When set to false the integration will not create default blueprints and the port App config Mapping               | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                     | Default, true, Enable sending raw data examples from the third part API to port for testing and managing the integration mapping | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`                    | Change the identifier to describe your integration, if not set will use the default one                                          | â       |
| `OCEAN__PORT__CLIENT_ID`                            | Your Port client id                                                                                                              | â       |
| `OCEAN__PORT__CLIENT_SECRET`                        | Your Port client secret                                                                                                          | â       |
| `OCEAN__PORT__BASE_URL`                             | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                | â       |

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
  INTEGRATION_TYPE: launchdarkly
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
        -e OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST=$OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_HOST \
        -e OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN=$OCEAN__INTEGRATION__CONFIG__LAUNCHDARKLY_TOKEN \
        -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
        -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
    - when: manual
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

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
- kind: project
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .key
        title: .name
        blueprint: '"launchDarklyProject"'
        properties:
          tags: .tags
- kind: flag
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .key + "-" + .__projectKey
        title: .name
        blueprint: '"launchDarklyFeatureFlag"'
        properties:
          kind: .kind
          description: .description
          creationDate: .creationDate / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ")
          clientSideAvailability: .clientSideAvailability
          temporary: .temporary
          tags: .tags
          maintainer: ._maintainer.email
          deprecated: .deprecated
          variations: .variations
          customProperties: .customProperties
          archived: .archived
        relations:
          project: .__projectKey
- kind: environment
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .key + "-" + .__projectKey
        title: .name
        blueprint: '"launchDarklyEnvironment"'
        properties:
          defaultTtl: .defaultTtl
          secureMode: .secureMode
          defaultTrackEvents: .defaultTrackEvents
          requireComments: .requireComments
          confirmChanges: .confirmChanges
          tags: .tags
          critical: .critical
        relations:
          project: .__projectKey
- kind: flag-status
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: . as $root | ._links.self.href | split("/") | last as $last | "\($last)-\($root.__environmentKey)"
        title: . as $root | ._links.self.href | split("/") | last as $last | "\($last)-\($root.__environmentKey)"
        blueprint: '"launchDarklyFFInEnvironment"'
        properties:
          status: .name
        relations:
          environment: .__environmentKey + "-" + .__projectKey
          featureFlag: . as $input | $input._links.self.href | split("/") | .[-1] + "-" + $input.__projectKey
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations:

### Project[â](#project "Direct link to Project")

Project blueprint

Create in Port

```
  {
    "identifier": "launchDarklyProject",
    "description": "This blueprint represents a project in LaunchDarkly.",
    "title": "LaunchDarkly Project",
    "icon": "Launchdarkly",
    "schema": {
      "properties": {
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags associated with the project for organizational purposes."
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
resources:
  - kind: project
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .key
          title: .name
          blueprint: '"launchDarklyProject"'
          properties:
            tags: .tags
```

### Feature Flag[â](#feature-flag "Direct link to Feature Flag")

Feature Flag blueprint

Create in Port

```
  {
    "identifier": "launchDarklyFeatureFlag",
    "description": "This blueprint represents a feature flag in LaunchDarkly.",
    "title": "LaunchDarkly Feature Flag",
    "icon": "Launchdarkly",
    "schema": {
      "properties": {
        "kind": {
          "type": "string",
          "title": "Flag Kind",
          "description": "The type of the feature flag (e.g., boolean)."
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "A description of what the flag controls."
        },
        "creationDate": {
          "type": "string",
          "format": "date-time",
          "title": "Creation Date",
          "description": "The date and time when the flag was created."
        },
        "clientSideAvailability": {
          "type": "object",
          "title": "Client-Side Availability",
          "description": "Availability of the flag for client-side applications."
        },
        "temporary": {
          "type": "boolean",
          "title": "Temporary Flag",
          "description": "Indicates if the flag is temporary."
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags associated with the feature flag."
        },
        "maintainer": {
          "type": "string",
          "title": "Maintainer",
          "description": "Email address of the maintainer of the flag."
        },
        "customProperties": {
          "type": "object",
          "title": "Custom Properties",
          "description": "Custom properties associated with the flag."
        },
        "archived": {
          "type": "boolean",
          "title": "Archived",
          "description": "Indicates if the flag is archived."
        },
        "deprecated": {
          "type": "boolean",
          "title": "Deprecated",
          "description": "Indicates if the flag is deprecated."
        },
        "variations": {
          "type": "array",
          "title": "Variations",
          "description": "An array of possible variations for the flag"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "project": {
        "title": "Project",
        "target": "launchDarklyProject",
        "required": true,
        "many": false
      }
    }
  }
```

Integration configuration

```
- kind: flag
  selector:
    query: "true"
  port:
    entity:
      mappings:
        identifier: .key + "-" + .__projectKey
        title: .name
        blueprint: '"launchDarklyFeatureFlag"'
        properties:
          kind: .kind
          description: .description
          creationDate: .creationDate / 1000 | strftime("%Y-%m-%dT%H:%M:%SZ")
          clientSideAvailability: .clientSideAvailability
          temporary: .temporary
          tags: .tags
          maintainer: ._maintainer.email
          deprecated: .deprecated
          variations: .variations
          customProperties: .customProperties
          archived: .archived
        relations:
          project: .__projectKey
```

### Environment[â](#environment "Direct link to Environment")

Environment blueprint

Create in Port

```
{
  "identifier": "launchDarklyEnvironment",
  "description": "This blueprint represents an environment in LaunchDarkly",
  "title": "LaunchDarkly Environment",
  "icon": "Launchdarkly",
  "schema": {
    "properties": {
      "defaultTtl": {
        "type": "number",
        "title": "Default TTL",
        "description": "The default time-to-live (in minutes) for feature flag settings in this environment."
      },
      "secureMode": {
        "type": "boolean",
        "title": "Secure Mode",
        "description": "Indicates whether Secure Mode is enabled for the environment, enhancing security by verifying user tokens."
      },
      "defaultTrackEvents": {
        "type": "boolean",
        "title": "Default Track Events",
        "description": "Indicates whether event tracking is enabled by default for all flags in this environment."
      },
      "requireComments": {
        "type": "boolean",
        "title": "Require Comments",
        "description": "Indicates whether comments are required for changes made in this environment."
      },
      "confirmChanges": {
        "type": "boolean",
        "title": "Confirm Changes",
        "description": "Indicates whether changes need to be confirmed before being applied in this environment."
      },
      "tags": {
        "type": "array",
        "title": "Tags",
        "description": "A list of tags associated with the environment for organizational purposes."
      },
      "critical": {
        "type": "boolean",
        "title": "Critical Environment",
        "description": "Indicates whether this environment is considered critical, which may affect change management and notifications."
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "project": {
      "title": "Project",
      "target": "launchDarklyProject",
      "required": true,
      "many": false
    }
  }
}
```

Integration configuration

```
- kind: environment
  selector:
    query: "true"
  port:
    entity:
      mappings:
        identifier: .key + "-" + .__projectKey
        title: .name
        blueprint: '"launchDarklyEnvironment"'
        properties:
          defaultTtl: .defaultTtl
          secureMode: .secureMode
          defaultTrackEvents: .defaultTrackEvents
          requireComments: .requireComments
          confirmChanges: .confirmChanges
          tags: .tags
          critical: .critical
        relations:
          project: .__projectKey
```

### Feature Flags In Environment[â](#feature-flags-in-environment "Direct link to Feature Flags In Environment")

Feature Flags In Environment blueprint

Create in Port

```
{
    "identifier": "launchDarklyFFInEnvironment",
    "description": "This blueprint represents a feature flag in LaunchDarkly Environment.",
    "title": "Feature Flag In Environment",
    "icon": "Launchdarkly",
    "schema": {
      "properties": {
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the feature flag"
        }
      },
      "required": []
    },
    "mirrorProperties": {
      "kind": {
        "title": "Kind",
        "path": "featureFlag.kind"
      },
      "description": {
        "title": "Description",
        "path": "featureFlag.description"
      },
      "deprecated": {
        "title": "Deprecated",
        "path": "featureFlag.deprecated"
      }
    },
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "environment": {
        "title": "Environment",
        "target": "launchDarklyEnvironment",
        "required": false,
        "many": false
      },
      "featureFlag": {
        "title": "Feature Flag",
        "target": "launchDarklyFeatureFlag",
        "required": false,
        "many": false
      }
    }
  }
```

Integration configuration

```
- kind: flag-status
  selector:
    query: "true"
  port:
    entity:
      mappings:
        identifier: >-
          . as $root | ._links.self.href | split("/") | last as $last |
          "\($last)-\($root.__environmentKey)"
        title: >-
          . as $root | ._links.self.href | split("/") | last as $last |
          "\($last)-\($root.__environmentKey)"
        blueprint: '"launchDarklyFFInEnvironment"'
        properties:
          status: .name
        relations:
          environment: .__environmentKey + "-" + .__projectKey
          featureFlag: . as $input | $input._links.self.href | split("/") | .[-1] + "-" + $input.__projectKey
```

## Let's Test It[â](#lets-test-it "Direct link to Let's Test It")

This section includes sample response data from LaunchDarkly. In addition, it includes the entity created from the resync event based on the Ocean configuration provided in the previous section.

### Payload[â](#payload "Direct link to Payload")

Here is an example of the payload structure from LaunchDarkly:

Project response data

```
{
  "_links": {
    "environments": {
      "href": "/api/v2/projects/fourth-project/environments",
      "type": "application/json"
    },
    "flagDefaults": {
      "href": "/api/v2/projects/fourth-project/flag-defaults",
      "type": "application/json"
    },
    "self": {
      "href": "/api/v2/projects/fourth-project",
      "type": "application/json"
    }
  },
  "_id": "666b298cc671e81012b578c6",
  "key": "fourth-project",
  "includeInSnippetByDefault": false,
  "defaultClientSideAvailability": {
    "usingMobileKey": false,
    "usingEnvironmentId": false
  },
  "name": "Fourth Project",
  "tags": []
}
```

Feature Flag response data

```
{
  "_links": {
    "parent": {
      "href": "/api/v2/flags/fourth-project",
      "type": "application/json"
    },
    "self": {
      "href": "/api/v2/flags/fourth-project/randomflag",
      "type": "application/json"
    }
  },
  "_maintainer": {
    "_id": "6669b0f34162860fefd6d724",
    "_links": {
      "self": {
        "href": "/api/v2/members/6669b0f34162860fefd6d724",
        "type": "application/json"
      }
    },
    "email": "example@gmail.com",
    "firstName": "John",
    "lastName": "Doe",
    "role": "owner"
  },
  "_version": 1,
  "archived": false,
  "clientSideAvailability": {
    "usingEnvironmentId": false,
    "usingMobileKey": false
  },
  "creationDate": 1718299647527,
  "customProperties": {},
  "defaults": {
    "offVariation": 1,
    "onVariation": 0
  },
  "deprecated": false,
  "description": "",
  "environments": {
    "fourth-env": {
      "_environmentName": "fourth-env",
      "_site": {
        "href": "/fourth-project/fourth-env/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718299647539,
      "on": false,
      "salt": "c713989066a446febf07a42d488221e8",
      "sel": "6d7c3692dd9d4ffa8eee8e2d96b6fd2c",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "new-env": {
      "_environmentName": "new env",
      "_site": {
        "href": "/fourth-project/new-env/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718299647539,
      "on": false,
      "salt": "caa436a38411406491f0da9230349bb3",
      "sel": "8bcf1667ab2f4f628fc26ad31966f045",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "new-project": {
      "_environmentName": "new_project",
      "_site": {
        "href": "/fourth-project/new-project/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718299647539,
      "on": false,
      "salt": "f79c8849d22d497d8a519fbb6263aeda",
      "sel": "257f0acaf18f4252b40258f8aa93b966",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "production": {
      "_environmentName": "Production",
      "_site": {
        "href": "/fourth-project/production/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718299647539,
      "on": false,
      "salt": "28c5efba5fd445d5896a8b9f7f8fbff6",
      "sel": "28a317cdf3aa4d40b8a0b1c6f56be4c9",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "shadow": {
      "_environmentName": "shadow",
      "_site": {
        "href": "/fourth-project/shadow/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718311480830,
      "on": false,
      "salt": "cb214aeac84f48d08ff136514c589b11",
      "sel": "00b5f9ae56a547db9c4e5e619bdb39f3",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "some-random-env": {
      "_environmentName": "some-random-env",
      "_site": {
        "href": "/fourth-project/some-random-env/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718300514123,
      "on": false,
      "salt": "0618861de85c48a5a77c360db7a8847b",
      "sel": "5ae511fe5630469084453c2c4d45f719",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "staging": {
      "_environmentName": "staging",
      "_site": {
        "href": "/fourth-project/staging/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718300902420,
      "on": false,
      "salt": "bc27ddc205984379a4863f5f1323bdb0",
      "sel": "2762811a62734de79277544ff4362f8c",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    },
    "test": {
      "_environmentName": "Test",
      "_site": {
        "href": "/fourth-project/test/features/randomflag",
        "type": "text/html"
      },
      "_summary": {
        "prerequisites": 0,
        "variations": {
          "0": {
            "contextTargets": 0,
            "isFallthrough": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          },
          "1": {
            "contextTargets": 0,
            "isOff": true,
            "nullRules": 0,
            "rules": 0,
            "targets": 0
          }
        }
      },
      "archived": false,
      "lastModified": 1718299647539,
      "on": false,
      "salt": "fac0fe470f844433986166f3d570415d",
      "sel": "8e8ae9542dc94f35b1ac64c845277d8a",
      "trackEvents": false,
      "trackEventsFallthrough": false,
      "version": 1
    }
  },
  "experiments": {
    "baselineIdx": 0,
    "items": []
  },
  "goalIds": [],
  "includeInSnippet": false,
  "key": "randomflag",
  "kind": "boolean",
  "maintainerId": "6669b0f34162860fefd6d724",
  "name": "randomflag",
  "tags": [],
  "temporary": true,
  "variationJsonSchema": null,
  "variations": [
    {
      "_id": "8868f0d9-8b1d-4575-9436-827188276792",
      "value": true
    },
    {
      "_id": "8929317b-d2aa-479c-9249-e6c0ec5dc415",
      "value": false
    }
  ],
  "__projectKey": "fourth-project"
}
```

Environment response data

```
{
  "_links": {
    "analytics": {
      "href": "https://app.launchdarkly.com/snippet/events/v1/666b2a74cbdbfb108f3fc911.js",
      "type": "text/html"
    },
    "apiKey": {
      "href": "/api/v2/projects/fourth-project/environments/fourth-env/apiKey",
      "type": "application/json"
    },
    "mobileKey": {
      "href": "/api/v2/projects/fourth-project/environments/fourth-env/mobileKey",
      "type": "application/json"
    },
    "self": {
      "href": "/api/v2/projects/fourth-project/environments/fourth-env",
      "type": "application/json"
    },
    "snippet": {
      "href": "https://app.launchdarkly.com/snippet/features/666b2a74cbdbfb108f3fc911.js",
      "type": "text/html"
    }
  },
  "_id": "666b2a74cbdbfb108f3fc911",
  "_pubnub": {
    "channel": "b4f644c56dbbfe88a4028cb2d2142c258926f9b7a9add263d105202f0cd6599c",
    "cipherKey": "9571e2de187881614fe9b6b94d13a99fbdb056e508c9226e6c6bb7d0be117725"
  },
  "key": "fourth-env",
  "name": "fourth-env",
  "apiKey": "sdk-1b3cf928-acae-4553-aab3-c956b7f04219",
  "mobileKey": "mob-87679d8a-698d-4c5f-9ec1-05e368975afe",
  "color": "e2e6ff",
  "defaultTtl": 0,
  "secureMode": false,
  "defaultTrackEvents": false,
  "requireComments": false,
  "confirmChanges": false,
  "tags": [],
  "approvalSettings": {
    "required": false,
    "bypassApprovalsForPendingChanges": false,
    "minNumApprovals": 1,
    "canReviewOwnRequest": false,
    "canApplyDeclinedChanges": true,
    "serviceKind": "launchdarkly",
    "serviceConfig": {},
    "requiredApprovalTags": []
  },
  "critical": false,
  "__projectKey": "fourth-project"
}
```

Feature Flag In Environment response data

```
{
  "_links": {
    "parent": {
      "href": "/api/v2/flags/fourth-project/olulufe",
      "type": "application/json"
    },
    "self": {
      "href": "/api/v2/flag-statuses/fourth-project/shadow/olulufe",
      "type": "application/json"
    }
  },
  "name": "new",
  "lastRequested": null,
  "__environmentKey": "shadow",
  "__projectKey": "fourth-project"
}
```

### Mapping Result[â](#mapping-result "Direct link to Mapping Result")

The combination of the sample payload and the Ocean configuration generates the following Port entity:

Project entity in Port

```
{
  "identifier": "fourth-project",
  "title": "Fourth Project",
  "blueprint": "launchDarklyProject",
  "properties": {
    "tags": []
  },
  "relation": {
    "service": "fourth-project"
  }
}
```

Feature Flag entity in Port

```
{
  "identifier": "randomflag-fourth-project",
  "title": "randomflag",
  "blueprint": "launchDarklyFeatureFlag",
  "properties": {
    "kind": "boolean",
    "description": "",
    "creationDate": "2024-06-13T17:27:27Z",
    "clientSideAvailability": {
      "usingEnvironmentId": false,
      "usingMobileKey": false
    },
    "temporary": true,
    "tags": [],
    "maintainer": "example@gmail.com",
    "deprecated": false,
    "variations": [
      {
        "_id": "8868f0d9-8b1d-4575-9436-827188276792",
        "value": true
      },
      {
        "_id": "8929317b-d2aa-479c-9249-e6c0ec5dc415",
        "value": false
      }
    ],
    "customProperties": {},
    "archived": false
  },
  "relations": {
    "project": "fourth-project"
  }
}
```

Environment entity in Port

```
{
    "identifier": "fourth-env-fourth-project",
    "title": "fourth-env",
    "blueprint": "launchDarklyEnvironment",
    "properties": {
      "defaultTtl": 0,
      "secureMode": false,
      "defaultTrackEvents": false,
      "requireComments": false,
      "confirmChanges": false,
      "tags": [],
      "critical": false
    },
    "relations": {
      "project": "fourth-project"
    }
  }
```

Feature Flag In Environment entity in Port

```
{
    "identifier": "olulufe-shadow",
    "title": "olulufe-shadow",
    "blueprint": "launchDarklyFFInEnvironment",
    "properties": {
      "status": "new"
    },
    "relations": {
      "environment": "shadow-fourth-project",
      "featureFlag": "olulufe-fourth-project"
    }
  }
```

## Relevant Guides[â](#relevant-guides "Direct link to Relevant Guides")

For relevant guides and examples, see the [guides section](https://docs.port.io/guides?tags=Launchdarkly).
