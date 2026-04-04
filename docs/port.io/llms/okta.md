# Source: https://docs.port.io/sso-rbac/sso-providers/saml/okta.md

# Source: https://docs.port.io/sso-rbac/sso-providers/oidc/okta.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/identity-providers/okta.md

# Okta

Loading version...

Port's Okta integration allows you to model Okta identity and access management resources in your software catalog and ingest data into them.

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Map and organize your desired Okta resources and their metadata in Port (see supported resources below).
* Watch for Okta object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.
* Track user and group relationships for better access management visibility.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Okta into Port are listed below. It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Users`](https://developer.okta.com/docs/reference/api/users/) - User accounts and their profile information
* [`Groups`](https://developer.okta.com/docs/reference/api/groups/) - User groups and their memberships

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

### Create an Okta API token[â](#create-an-okta-api-token "Direct link to Create an Okta API token")

1. Log in to your Okta admin console.
2. Navigate to **Security** > **API** > **Tokens**.
3. Click **Create Token**.
4. Provide a name for your token (e.g., "Port Integration").
5. Click **Create Token**.
6. Copy the generated token and save it securely.

Token Security

Store your API token securely and never share it. The token provides access to your Okta data.

### Okta Domain[â](#okta-domain "Direct link to Okta Domain")

Your Okta domain is the subdomain of your Okta organization URL. For example, if your Okta URL is `https://dev-123456.okta.com`, your domain would be `dev-123456.okta.com`.

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Hosted by Port (Recommended)
* Self-hosted
* CI

1. Go to the [Okta<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Okta) in your portal.

2. Under `Select your installation method`, choose `Hosted by Port`.

3. Configure the `Installation parameters` and `Advanced configuration` as you wish (see below for details).

### Installation parameters

Each integration requires specific parameters (such as an API token, a URL, etc.), as seen in Port's UI when installing it. Hover over the â icon next to each parameter to see more details about it.

### Advanced configuration

* **During the installation** process each integration may have additional settings under the `Advanced configuration` section in Port's UI.<br /><!-- -->Additionally, each integration has one or more settings that can be configured **after installation**. To do so, click on the integration's name in the [Data sources](https://app.getport.io/settings/data-sources) page and navigate to the `Setting` tab.<br /><!-- -->Hover over the â icon next to each setting to see more details about it.

* If the integration supports live events, the option to enable/disable them will be available in this section.

  This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

  **Supported live event triggers (click to expand)**

  **User:**

  * user.lifecycle.create
  * user.lifecycle.activate
  * user.lifecycle.deactivate
  * user.lifecycle.suspend
  * user.lifecycle.unsuspend
  * user.lifecycle.delete
  * user.account.update\_profile

  **Group:**

  * group.lifecycle.create
  * group.lifecycle.delete
  * group.lifecycle.update

  **Group Membership:**

  * group.user\_membership.add
  * group.user\_membership.remove

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

Using this installation method means that the integration will be able to update Port in real time using webhooks.

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

<!-- -->

1. Go to the [Okta<!-- --> data source page](https://app.getport.io/settings/data-sources?section=EXPORTERS\&provider=Okta) in your portal.

2. Select the `Self-hosted` method.

3. A `helm` command will be displayed, with default values already filled out (e.g. your Port client ID, client secret, etc). Copy the command, replace the placeholders with your values, then run it in your terminal to install the integration.

<!-- -->

### BaseUrl & webhook configuration[â](#baseurl--webhook-configuration "Direct link to BaseUrl & webhook configuration")

To enable real-time updates of the data in your software catalog, you need to define the `liveEvents.baseUrl` parameter.<br /><!-- -->This parameter should be set to the URL of your <!-- -->Okta<!-- --> integration instance, which needs to have the option to setup webhooks via HTTP requests/receive HTTP requests, so ensure the network is configured accordingly.

* **If <!-- -->Okta<!-- --> and the integration are in the same cluster/network**: Use an internal URL (e.g., a Kubernetes service DNS name).
  <br />
  <!-- -->
  For Kubernetes deployments, create a service to expose the integration pod and use the service URL as `liveEvents.baseUrl`. If both the source system and integration are in the same cluster, an internal ClusterIP service is sufficient.
* **If <!-- -->Okta<!-- --> is external to the integration's network**: The integration must be exposed via an ingress, load balancer, or public URL that
  <!-- -->
  Okta
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

For details about the available parameters for the installation, see the table below.

This table summarizes the parameters used for the installation.<br /><!-- -->Note the parameters specific to this integration, they are last in the table.

| Parameter                                   | Description                                                                                                                         | Required |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `port.clientId`                             | Your Port client id, used to identify your account                                                                                  | â       |
| `port.clientSecret`                         | Your Port client secret, used to identify your account                                                                              | â       |
| `port.baseUrl`                              | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                   | â       |
| `initializePortResources`                   | Default: `true`. When `true`, the integration will create default blueprints and configuration mapping                              | â       |
| `sendRawDataExamples`                       | Default: `true`. Enable sending raw data examples from the third party API to Port for testing and managing the integration mapping | â       |
| `integration.identifier`                    | The integration's identifier, used to reference the integration when using Port's API                                               | â       |
| `integration.type`                          | The integration type, used to denote the integrated tool/platform                                                                   | â       |
| `integration.eventListener.type`            | The method used to listen to events from the 3rd party tool (`POLLING` or `KAFKA`)                                                  | â       |
| **`integration.secrets.oktaApiToken`**      | The Okta API token used to authenticate Port to Okta                                                                                | â       |
| **`integration.config.oktaDomain`**         | Your Okta domain (e.g., dev-123456.okta.com)                                                                                        | â       |
| **`integration.secrets.oktaWebhookSecret`** | Optional secret used to verify incoming webhook requests                                                                            | â       |

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

This workflow/pipeline will run the Okta integration once and then exit, this is useful for scheduled ingestion of data.

Real-time updates

If you want the integration to update Port in real time you should use the [Self-hosted](/build-your-software-catalog/sync-data-to-catalog/identity-providers/okta.md?installation-methods=real-time-self-hosted#setup) installation option.

* GitHub
* Jenkins
* Azure Devops
* GitLab
* Docker

Make sure to configure the following [GitHub Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                     | Description                                                                                       | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your Port client id                                                                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your Port client secret                                                                           | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                 | â       |
| `OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN`     | Your Okta domain. For example `dev-123456.okta.com`                                               | â       |
| `OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN` | The Okta API token. Generate it from Okta Admin Console under Security > API > Tokens             | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration; if not set, a default identifier will be used | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true. When set to false, the integration will not create default blueprints and mapping   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Default true. When set to false, raw data examples will not be sent to Port                       | â       |

<br />

Here is an example for `okta-integration.yml` workflow file:

```
name: Okta Exporter Workflow
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
          type: 'okta'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            okta_domain: ${{ secrets.OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN }}
            okta_api_token: ${{ secrets.OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN }}
```

Jenkins Docker Requirements

Your Jenkins agent should be able to run docker commands.

<br />

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                     | Description                                                                                       | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your Port client id                                                                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your Port client secret                                                                           | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                 | â       |
| `OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN`     | Your Okta domain. For example `dev-123456.okta.com`                                               | â       |
| `OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN` | The Okta API token. Generate it from Okta Admin Console under Security > API > Tokens             | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration; if not set, a default identifier will be used | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true. When set to false, the integration will not create default blueprints and mapping   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Default true. When set to false, raw data examples will not be sent to Port                       | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Okta Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN', variable: 'OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN'),
                        string(credentialsId: 'OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN', variable: 'OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN'),
                    ]) {
                        sh('''
                            # Set Docker image and run the container
                            integration_type="okta"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN=$OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN \
                                -e OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN=$OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN \
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

Azure DevOps Docker Requirements

Your Azure DevOps agent should be able to run docker commands.

<br />

Make sure to configure the following [Azure DevOps Variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops\&tabs=yaml%2Cbatch) as secret variables:

| Parameter                                     | Description                                                                                       | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your Port client id                                                                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your Port client secret                                                                           | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                 | â       |
| `OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN`     | Your Okta domain. For example `dev-123456.okta.com`                                               | â       |
| `OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN` | The Okta API token. Generate it from Okta Admin Console under Security > API > Tokens             | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration; if not set, a default identifier will be used | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true. When set to false, the integration will not create default blueprints and mapping   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Default true. When set to false, raw data examples will not be sent to Port                       | â       |

<br />

Here is an example for `okta-integration.yml` pipeline file:

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
    integration_type="okta"
    version="latest"
    image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

    docker run -i --rm \
      -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
      -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
      -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
      -e OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN=$(OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN) \
      -e OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN=$(OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN) \
      -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
      -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
      -e OCEAN__PORT__BASE_URL='https://api.port.io' \
      $image_name

    exit $?
  displayName: 'Ingest Data into Port'
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                     | Description                                                                                       | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your Port client id                                                                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your Port client secret                                                                           | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                 | â       |
| `OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN`     | Your Okta domain. For example `dev-123456.okta.com`                                               | â       |
| `OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN` | The Okta API token. Generate it from Okta Admin Console under Security > API > Tokens             | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration; if not set, a default identifier will be used | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true. When set to false, the integration will not create default blueprints and mapping   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Default true. When set to false, raw data examples will not be sent to Port                       | â       |

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
  INTEGRATION_TYPE: okta
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
        -e OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN=$OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN \
        -e OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN=$OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN \
        -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
        -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
    - when: manual
```

To run the integration using Docker for a one-time sync:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID`, `YOUR_PORT_CLIENT_SECRET`, `YOUR_OKTA_DOMAIN`, and `YOUR_OKTA_API_TOKEN`.

| Parameter                                     | Description                                                                                       | Required |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                      | Your Port client id                                                                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                  | Your Port client secret                                                                           | â       |
| `OCEAN__PORT__BASE_URL`                       | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                 | â       |
| `OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN`     | Your Okta domain. For example `dev-123456.okta.com`                                               | â       |
| `OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN` | The Okta API token. Generate it from Okta Admin Console under Security > API > Tokens             | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`              | Change the identifier to describe your integration; if not set, a default identifier will be used | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`            | Default true. When set to false, the integration will not create default blueprints and mapping   | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`               | Default true. When set to false, raw data examples will not be sent to Port                       | â       |

<br />

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__INTEGRATION__CONFIG__OKTA_DOMAIN="YOUR_OKTA_DOMAIN" \
  -e OCEAN__INTEGRATION__SECRETS__OKTA_API_TOKEN="YOUR_OKTA_API_TOKEN" \
  -e OCEAN__PORT__CLIENT_ID="YOUR_PORT_CLIENT_ID" \
  -e OCEAN__PORT__CLIENT_SECRET="YOUR_PORT_CLIENT_SECRET" \
  -e OCEAN__PORT__BASE_URL="https://api.port.io" \
  ghcr.io/port-labs/port-ocean-okta:latest
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (click to expand)**

```
resources:
- kind: okta-user
  selector:
    query: 'true'
    include_groups: true
    include_applications: true
    fields: "id,status,created,activated,lastLogin,lastUpdated,profile:(login,firstName,lastName,displayName,email,title,department,employeeNumber,mobilePhone,primaryPhone,streetAddress,city,state,zipCode,countryCode)"
  port:
    entity:
      mappings:
        identifier: .id
        title: .profile.displayName // .profile.firstName + " " + .profile.lastName // .profile.login
        blueprint: '"okta-user"'
        properties:
          login: .profile.login
          email: .profile.email
          firstName: .profile.firstName
          lastName: .profile.lastName
          displayName: .profile.displayName
          title: .profile.title
          department: .profile.department
          employeeNumber: .profile.employeeNumber
          mobilePhone: .profile.mobilePhone
          primaryPhone: .profile.primaryPhone
          streetAddress: .profile.streetAddress
          city: .profile.city
          state: .profile.state
          zipCode: .profile.zipCode
          countryCode: .profile.countryCode
          status: .status
          created: .created
          activated: .activated
          lastLogin: .lastLogin
          lastUpdated: .lastUpdated
        relations:
          groups: .groups[]?.id
- kind: okta-group
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .id
        title: .profile.name
        blueprint: '"okta-group"'
        properties:
          name: .profile.name
          description: .profile.description
          type: .type
          created: .created
          lastUpdated: .lastUpdated
        relations:
          members: .users[]?.id
```

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations:

### User[â](#user "Direct link to User")

**User blueprint (click to expand)**

Create in Port

```
{
  "identifier": "okta-user",
  "title": "Okta User",
  "icon": "Okta",
  "schema": {
    "properties": {
      "login": {
        "title": "Login",
        "type": "string"
      },
      "email": {
        "title": "Email",
        "type": "string",
        "format": "email"
      },
      "firstName": {
        "title": "First Name",
        "type": "string"
      },
      "lastName": {
        "title": "Last Name",
        "type": "string"
      },
      "displayName": {
        "title": "Display Name",
        "type": "string"
      },
      "title": {
        "title": "Job Title",
        "type": "string"
      },
      "department": {
        "title": "Department",
        "type": "string"
      },
      "employeeNumber": {
        "title": "Employee Number",
        "type": "string"
      },
      "mobilePhone": {
        "title": "Mobile Phone",
        "type": "string"
      },
      "primaryPhone": {
        "title": "Primary Phone",
        "type": "string"
      },
      "streetAddress": {
        "title": "Street Address",
        "type": "string"
      },
      "city": {
        "title": "City",
        "type": "string"
      },
      "state": {
        "title": "State",
        "type": "string"
      },
      "zipCode": {
        "title": "ZIP Code",
        "type": "string"
      },
      "countryCode": {
        "title": "Country Code",
        "type": "string"
      },
      "status": {
        "title": "Status",
        "type": "string",
        "enum": ["ACTIVE", "INACTIVE", "PASSWORD_EXPIRED", "LOCKED_OUT", "SUSPENDED", "DEPROVISIONED"]
      },
      "created": {
        "title": "Created Date",
        "type": "string",
        "format": "date-time"
      },
      "activated": {
        "title": "Activated Date",
        "type": "string",
        "format": "date-time"
      },
      "lastLogin": {
        "title": "Last Login",
        "type": "string",
        "format": "date-time"
      },
      "lastUpdated": {
        "title": "Last Updated",
        "type": "string",
        "format": "date-time"
      }
    },
    "required": ["login", "email"]
  },
  "calculationProperties": {},
  "relations": {
    "groups": {
      "title": "Groups",
      "target": "okta-group",
      "required": false,
      "many": true
    }
  }
}
```

**Mapping configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: okta-user
    selector:
      query: "true"
      include_groups: true
      include_applications: true
    port:
      entity:
        mappings:
          identifier: .id
          title: .profile.displayName // .profile.firstName + " " + .profile.lastName // .profile.login
          blueprint: '"okta-user"'
          properties:
            login: .profile.login
            email: .profile.email
            firstName: .profile.firstName
            lastName: .profile.lastName
            displayName: .profile.displayName
            title: .profile.title
            department: .profile.department
            employeeNumber: .profile.employeeNumber
            mobilePhone: .profile.mobilePhone
            primaryPhone: .profile.primaryPhone
            streetAddress: .profile.streetAddress
            city: .profile.city
            state: .profile.state
            zipCode: .profile.zipCode
            countryCode: .profile.countryCode
            status: .status
            created: .created
            activated: .activated
            lastLogin: .lastLogin
            lastUpdated: .lastUpdated
          relations:
            groups: .groups[]?.id
```

### Group[â](#group "Direct link to Group")

**Group blueprint (click to expand)**

Create in Port

```
{
  "identifier": "okta-group",
  "title": "Okta Group",
  "icon": "Okta",
  "schema": {
    "properties": {
      "name": {
        "title": "Name",
        "type": "string"
      },
      "description": {
        "title": "Description",
        "type": "string"
      },
      "type": {
        "title": "Type",
        "type": "string",
        "enum": ["BUILT_IN", "OKTA_GROUP", "APP_GROUP"]
      },
      "created": {
        "title": "Created Date",
        "type": "string",
        "format": "date-time"
      },
      "lastUpdated": {
        "title": "Last Updated",
        "type": "string",
        "format": "date-time"
      }
    },
    "required": ["name"]
  },
  "calculationProperties": {},
  "relations": {
    "members": {
      "title": "Members",
      "target": "okta-user",
      "required": false,
      "many": true
    }
  }
}
```

**Mapping configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: okta-group
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .id
          title: .profile.name
          blueprint: '"okta-group"'
          properties:
            name: .profile.name
            description: .profile.description
            type: .type
            created: .created
            lastUpdated: .lastUpdated
          relations:
            members: .users[]?.id
```

## Webhook configuration[â](#webhook-configuration "Direct link to Webhook configuration")

The Okta integration supports real-time updates through webhooks. When using the self-hosted installation method, the integration will automatically:

1. Create an Event Hook in your Okta organization
2. Configure the webhook to send user and group change events
3. Process incoming webhook events to update Port entities in real-time

### Webhook events[â](#webhook-events "Direct link to Webhook events")

The integration listens for the following Okta events:

* `user.lifecycle.create`
* `user.lifecycle.activate`
* `user.lifecycle.deactivate`
* `user.lifecycle.suspend`
* `user.lifecycle.unsuspend`
* `user.lifecycle.delete`
* `user.account.update_profile`
* `group.user_membership.add`
* `group.user_membership.remove`
* `group.lifecycle.create`
* `group.lifecycle.delete`
* `group.lifecycle.update`

## Limitations[â](#limitations "Direct link to Limitations")

* The integration currently supports users and groups only
* Custom Okta attributes are not automatically mapped but can be added to the configuration
* Webhook verification is optional but recommended for production environments

## Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

### Common Issues[â](#common-issues "Direct link to Common Issues")

1. **Authentication Errors**: Verify your Okta API token has the correct permissions and is not expired
2. **Domain Issues**: Ensure your Okta domain is correctly formatted (e.g., `dev-123456.okta.com`)
3. **Webhook Failures**: Check that your self-hosted integration is accessible from the internet for webhook delivery
4. **Rate Limiting**: Okta has API rate limits; the integration handles this automatically with retries
