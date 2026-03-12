# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/project-management/jira-server.md

# Jira Server (self-hosted)

Loading version...

Port's Jira Server integration allows you to model Jira Server resources in your software catalog and ingest data into them.

Jira Server Support

This integration is specifically designed for **Jira Server (Self-Hosted)** installations. For Jira Cloud, use [Port's Jira Cloud integration](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/.md).

## Overview[â](#overview "Direct link to Overview")

This integration allows you to:

* Watch for Jira Server object changes (create/update/delete) via scheduled resync, and automatically apply the changes to your software catalog.
* Define self-service actions that can create/delete Jira Server objects or perform any other logic on Jira Server resources.

### Supported resources[â](#supported-resources "Direct link to Supported resources")

The resources that can be ingested from Jira Server into Port are listed below.<br /><!-- -->It is possible to reference any field that appears in the API responses linked below in the mapping configuration.

* [`Project`](https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/#api/2/project-getAllProjects) - Get all projects visible to the user
* [`User`](https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/#api/2/user/search-findUsers) - Search for users using username query
* [`Issue`](https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/#api/2/search-search) - Search for issues using JQL (Jira Query Language)

## Setup[â](#setup "Direct link to Setup")

Choose one of the following installation methods:<br /><!-- -->Not sure which method is right for your use case? Check the available [installation methods](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

* Self-hosted (Recommended)
* CI

This workflow will run the Jira Server integration and update Port in real time using scheduled polling.

## Live event support

This integration supports live events, allowing real-time updates to your software catalog without waiting for the next scheduled sync.

**Supported live event triggers (click to expand)**

**Issue:**

* jira:issue\_created
* jira:issue\_updated
* jira:issue\_deleted

**Project:**

* project\_created
* project\_updated
* project\_deleted

**User:**

* user\_created
* user\_updated
* user\_deleted

## Prerequisites

* A Kubernetes cluster - the integration's container chart will be deployed to this cluster.

* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [`helm`](https://helm.sh/) must be installed on your machine. Your `kubectl` CLI must be connected to the Kubernetes cluster where you plan to install the integration.

For details about the available parameters for the installation, see the table below.

* Helm
* ArgoCD

To install the integration using Helm, run the following command:

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install jira-server port-labs/port-ocean \
  --set port.clientId="YOUR_PORT_CLIENT_ID"  \
  --set port.clientSecret="YOUR_PORT_CLIENT_SECRET"  \
  --set port.baseUrl="https://api.port.io"  \
  --set initializePortResources=true  \
  --set scheduledResyncInterval=1440 \
  --set integration.identifier="jira-server"  \
  --set integration.type="jira-server"  \
  --set integration.eventListener.type="POLLING"  \
  --set integration.config.jiraServerHost="https://jira.yourdomain.com"  \
  --set integration.secrets.token="YOUR_JIRA_TOKEN"
```

To install the integration using ArgoCD:

1. Create a `values.yaml` file in `argocd/my-ocean-jira-server-integration` in your git repository with the content:

note

Remember to replace the placeholders for `JIRA_SERVER_HOST` and your authentication method (either `JIRA_TOKEN` or `JIRA_USERNAME`/`JIRA_PASSWORD`).

```
initializePortResources: true
scheduledResyncInterval: 1440
integration:
  identifier: my-ocean-jira-server-integration
  type: jira-server
  eventListener:
    type: POLLING
  config:
    jiraServerHost: JIRA_SERVER_HOST
  secrets:
    token: JIRA_TOKEN  # For Personal Access Token authentication
    # OR for Basic Authentication:
    # username: JIRA_USERNAME
    # password: JIRA_PASSWORD
```

<br />

2. Install the `my-ocean-jira-server-integration` ArgoCD Application by creating the following `my-ocean-jira-server-integration.yaml` manifest:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.<br /><!-- -->Multiple sources ArgoCD documentation can be found [here](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

ArgoCD Application (Click to expand)

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-ocean-jira-server-integration
  namespace: argocd
spec:
  destination:
    namespace: my-ocean-jira-server-integration
    server: https://kubernetes.default.svc
  project: default
  sources:
  - repoURL: 'https://port-labs.github.io/helm-charts/'
    chart: port-ocean
    targetRevision: 0.9.5
    helm:
      valueFiles:
      - $values/argocd/my-ocean-jira-server-integration/values.yaml
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

<br />

3. Apply your application manifest with `kubectl`:

```
kubectl apply -f my-ocean-jira-server-integration.yaml
```

This table summarizes the available parameters for the installation.

| Parameter                           | Description                                                                                                                                                                                                                                   | Example                                       | Required |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------- |
| `port.clientId`                     | Your port [client id](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                    |                                               | â       |
| `port.clientSecret`                 | Your port [client secret](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)                                                                                                                |                                               | â       |
| `port.baseUrl`                      | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                                                                                                                             |                                               | â       |
| `integration.secrets.token`         | [Personal Access Token](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) for your Jira Server. **Either token or username/password must be provided.**                                               | `your_jira_server_personal_access_token_here` | â       |
| `integration.secrets.username`      | Username for Jira Server authentication. **Required if token is not provided.**                                                                                                                                                               | `admin`                                       | â       |
| `integration.secrets.password`      | Password for Jira Server authentication. **Required if token is not provided.**                                                                                                                                                               |                                               | â       |
| `integration.config.jiraServerHost` | The URL of your Jira Server                                                                                                                                                                                                                   | `https://jira.yourdomain.com`                 | â       |
| `integration.eventListener.type`    | The event listener type. Read more about [event listeners](https://ocean.getport.io/framework/features/event-listener)                                                                                                                        | `POLLING`                                     | â       |
| `integration.type`                  | The integration to be installed                                                                                                                                                                                                               | `jira-server`                                 | â       |
| `scheduledResyncInterval`           | The number of minutes between each resync. When not set the integration will resync for each event listener resync event. Read more about [scheduledResyncInterval](https://ocean.port.io/developing-an-integration/trigger-your-integration) | `1440` (24 hours)                             | â       |
| `initializePortResources`           | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                                                                                                                                | `true`                                        | â       |
| `sendRawDataExamples`               | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true                                                                                                           | `true`                                        | â       |

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

This workflow/pipeline will run the Jira Server integration once and then exit, this is useful for **scheduled** ingestion of data.

* GitHub
* Jenkins
* Azure Devops
* GitLab

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

| Parameter                                      | Description                                                                                                                                                 | Example                       | Required |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                       | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                   | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |                               | â       |
| `OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST` | The URL of your Jira Server                                                                                                                                 | `https://jira.yourdomain.com` | â       |
| `OCEAN__INTEGRATION__CONFIG__TOKEN`            | Personal Access Token for your Jira Server. **Either token or username/password must be provided.**                                                         |                               | â       |
| `OCEAN__INTEGRATION__SECRETS__USERNAME`        | Username for Jira Server authentication. **Required if token is not provided.**                                                                             | `admin`                       | â       |
| `OCEAN__INTEGRATION__SECRETS__PASSWORD`        | Password for Jira Server authentication. **Required if token is not provided.**                                                                             |                               | â       |

<br />

Ocean Sail Github Action

The following example uses the **Ocean Sail** Github Action to run the Jira Server integration. For further information about the action, please visit the [Ocean Sail Github Action](https://github.com/marketplace/actions/ocean-sail)

<br />

Here is an example for `jira-server-integration.yml` workflow file:

```
name: Jira Server Exporter Workflow

on:
  workflow_dispatch:
  schedule:
    - cron: '0 */2 * * *' # Determines the scheduled interval for this workflow. This example runs every 2 hours.

jobs:
  run-integration:
    runs-on: ubuntu-latest
    timeout-minutes: 30 # Set a time limit for the job

    steps:
      - uses: port-labs/ocean-sail@v1
        with:
          type: 'jira-server'
          port_client_id: ${{ secrets.OCEAN__PORT__CLIENT_ID }}
          port_client_secret: ${{ secrets.OCEAN__PORT__CLIENT_SECRET }}
          port_base_url: https://api.port.io
          config: |
            jira_server_host: ${{ secrets.OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST }}
          secrets: |
            token: ${{ secrets.OCEAN__INTEGRATION__CONFIG__TOKEN }}
```

Tip for Jenkins agent

Your Jenkins agent should be able to run docker commands.

Make sure to configure the following [Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/) of `Secret Text` type:

| Parameter                                      | Description                                                                                                                                                 | Example                       | Required |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                       | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                   | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |                               | â       |
| `OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST` | The URL of your Jira Server                                                                                                                                 | `https://jira.yourdomain.com` | â       |
| `OCEAN__INTEGRATION__CONFIG__TOKEN`            | Personal Access Token for your Jira Server. **Either token or username/password must be provided.**                                                         |                               | â       |
| `OCEAN__INTEGRATION__SECRETS__USERNAME`        | Username for Jira Server authentication. **Required if token is not provided.**                                                                             | `admin`                       | â       |
| `OCEAN__INTEGRATION__SECRETS__PASSWORD`        | Password for Jira Server authentication. **Required if token is not provided.**                                                                             |                               | â       |

<br />

Here is an example for `Jenkinsfile` groovy pipeline file:

```
pipeline {
    agent any

    stages {
        stage('Run Jira Server Integration') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST', variable: 'OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST'),
                        string(credentialsId: 'OCEAN__INTEGRATION__CONFIG__TOKEN', variable: 'OCEAN__INTEGRATION__CONFIG__TOKEN'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_ID', variable: 'OCEAN__PORT__CLIENT_ID'),
                        string(credentialsId: 'OCEAN__PORT__CLIENT_SECRET', variable: 'OCEAN__PORT__CLIENT_SECRET'),
                    ]) {
                        sh('''
                            #Set Docker image and run the container
                            integration_type="jira-server"
                            version="latest"
                            image_name="ghcr.io/port-labs/port-ocean-${integration_type}:${version}"
                            docker run -i --rm --platform=linux/amd64 \
                                -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
                                -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
                                -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
                                -e OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST=$OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST \
                                -e OCEAN__INTEGRATION__CONFIG__TOKEN=$OCEAN__INTEGRATION__CONFIG__TOKEN \
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

Make sure to configure the following variables using [Azure DevOps variable groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups). Add them into a variable group called `port-ocean-credentials`:

| Parameter                                      | Description                                                                                                                                                 | Example                       | Required |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                       | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                   | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |                               | â       |
| `OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST` | The URL of your Jira Server                                                                                                                                 | `https://jira.yourdomain.com` | â       |
| `OCEAN__INTEGRATION__CONFIG__TOKEN`            | Personal Access Token for your Jira Server. **Either token or username/password must be provided.**                                                         |                               | â       |
| `OCEAN__INTEGRATION__SECRETS__USERNAME`        | Username for Jira Server authentication. **Required if token is not provided.**                                                                             | `admin`                       | â       |
| `OCEAN__INTEGRATION__SECRETS__PASSWORD`        | Password for Jira Server authentication. **Required if token is not provided.**                                                                             |                               | â       |

<br />

Here is an example for `jira-server-integration.yml` pipeline file:

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
      integration_type="jira-server"
      version="latest"

      image_name="ghcr.io/port-labs/port-ocean-$integration_type:$version"

      docker run -i --rm \
        -e OCEAN__EVENT_LISTENER='{"type":"ONCE"}' \
        -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
        -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
        -e OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST=$(OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST) \
        -e OCEAN__INTEGRATION__CONFIG__TOKEN=$(OCEAN__INTEGRATION__CONFIG__TOKEN) \
        -e OCEAN__PORT__CLIENT_ID=$(OCEAN__PORT__CLIENT_ID) \
        -e OCEAN__PORT__CLIENT_SECRET=$(OCEAN__PORT__CLIENT_SECRET) \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $image_name

      exit $?
    displayName: "Ingest Data into Port"
```

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                      | Description                                                                                                                                                 | Example                       | Required |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------- |
| `OCEAN__PORT__CLIENT_ID`                       | Your Port client id ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials))     |                               | â       |
| `OCEAN__PORT__CLIENT_SECRET`                   | Your Port client secret ([How to get the credentials](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials)) |                               | â       |
| `OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST` | The URL of your Jira Server                                                                                                                                 | `https://jira.yourdomain.com` | â       |
| `OCEAN__INTEGRATION__CONFIG__TOKEN`            | Personal Access Token for your Jira Server. **Either token or username/password must be provided.**                                                         |                               | â       |
| `OCEAN__INTEGRATION__SECRETS__USERNAME`        | Username for Jira Server authentication. **Required if token is not provided.**                                                                             | `admin`                       | â       |
| `OCEAN__INTEGRATION__SECRETS__PASSWORD`        | Password for Jira Server authentication. **Required if token is not provided.**                                                                             |                               | â       |

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
  INTEGRATION_TYPE: jira-server
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
        -e OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST=$OCEAN__INTEGRATION__CONFIG__JIRA_SERVER_HOST \
        -e OCEAN__INTEGRATION__CONFIG__TOKEN=$OCEAN__INTEGRATION__CONFIG__TOKEN \
        -e OCEAN__PORT__CLIENT_ID=$OCEAN__PORT__CLIENT_ID \
        -e OCEAN__PORT__CLIENT_SECRET=$OCEAN__PORT__CLIENT_SECRET \
        -e OCEAN__PORT__BASE_URL='https://api.port.io' \
        $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
    - when: manual
```

Advanced integration configuration

For advanced configuration such as proxies or self-signed certificates, [click here](https://ocean.getport.io/framework/advanced-configuration).

## Authentication[â](#authentication "Direct link to Authentication")

The Jira Server integration supports two authentication methods:

Token authentication recommended

We recommend using Personal Access Token authentication for better security and easier management.

### Option 1: Personal Access Token (Recommended)[â](#option-1-personal-access-token-recommended "Direct link to Option 1: Personal Access Token (Recommended)")

Personal Access Tokens provide a more secure authentication method and are the recommended approach.

1. **Create a Personal Access Token in Jira Server:**

   * Log in to your Jira Server as an administrator
   * Go to **Jira Administration** â **System** â **User Management**
   * Select the user account that will be used for the integration
   * Click **Personal Access Tokens** in the left menu
   * Click **Create token**
   * Enter a name for the token and click **Create**
   * **Important:** Copy the token value immediately as it won't be shown again

2. **Configure the integration:**

   * Use the `token` parameter in your integration configuration
   * Do not provide `username` and `password` when using token authentication

### Option 2: Basic Authentication (Username/Password)[â](#option-2-basic-authentication-usernamepassword "Direct link to Option 2: Basic Authentication (Username/Password)")

Basic authentication uses a username and password combination.

1. **Use an existing Jira user account:**

   * Ensure the user has appropriate permissions to read projects, issues, and users
   * The user should have **Browse Projects** and **Browse Users** permissions

2. **Configure the integration:**

   * Use the `username` and `password` parameters in your integration configuration
   * Do not provide the `token` parameter when using basic authentication

Security Recommendation

Personal Access Tokens are more secure than username/password authentication as they can be easily revoked and have limited scope. We strongly recommend using Personal Access Tokens for production environments.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

For the default mapping configuration and blueprints that come with this integration, see the [examples page](/build-your-software-catalog/sync-data-to-catalog/project-management/jira-server/examples.md#defaults).

### JQL support for issues[â](#jql-support-for-issues "Direct link to JQL support for issues")

The Ocean Jira Server integration supports querying objects from the `issue` kind using [JQL (Jira Query Language)](https://www.atlassian.com/software/jira/guides/jql/overview), making it possible to specifically filter the issues that are queried from Jira Server and ingested to Port.

To use JQL filtering, add to the `selector` object a `jql` key with your desired JQL query as the value. For example:

```
resources:
  - kind: issue # JQL filtering can only be used with the "issue" kind
    selector:
      query: "true" # JQ boolean expression. If evaluated to false - this object will be skipped.
      jql: "status != Done" # JQL query, will only ingest issues whose status is not "Done"
    port:
```

## Examples[â](#examples "Direct link to Examples")

To view and test the integration's mapping against examples of the third-party API responses, use the **jq playground** in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

Additional examples of blueprints and the relevant integration configurations can be found on the jira server [examples page](/build-your-software-catalog/sync-data-to-catalog/project-management/jira-server/examples.md)

## Alternative option - using the webhook integration[â](#alternative-option---using-the-webhook-integration "Direct link to Alternative option - using the webhook integration")

In this alternative approach, you can create a webhook integration between your Jira Server and Port instead of using the Ocean integration. The webhook integration will facilitate the ingestion of Jira project and issue entities into Port through real-time webhook events.

### Port configuration[â](#port-configuration "Direct link to Port configuration")

Create the following blueprint definitions:

Jira project blueprint

Create in Port

```
{
  "identifier": "jiraProject",
  "description": "This blueprint represents a project in Jira",
  "title": "Jira Project",
  "icon": "Jira",
  "schema": {
    "properties": {
      "url": {
        "title": "Project URL",
        "type": "string",
        "format": "url"
      },
      "description": {
        "title": "Description",
        "type": "string"
      },
      "type": {
        "title": "Type",
        "type": "string"
      },
      "lead": {
        "title": "Project Lead",
        "type": "string"
      },
      "issueCount": {
        "title": "Issue Count",
        "type": "number"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```

Jira issue blueprint

Create in Port

```
{
  "identifier": "jiraIssue",
  "description": "This blueprint represents a Jira issue",
  "title": "Jira Issue",
  "icon": "Jira",
  "schema": {
    "properties": {
      "url": {
        "title": "Issue URL",
        "type": "string",
        "format": "url"
      },
      "status": {
        "title": "Status",
        "type": "string"
      },
      "issueType": {
        "title": "Issue Type",
        "type": "string"
      },
      "priority": {
        "title": "Priority",
        "type": "string"
      },
      "assignee": {
        "title": "Assignee",
        "type": "string"
      },
      "reporter": {
        "title": "Reporter",
        "type": "string"
      },
      "creator": {
        "title": "Creator",
        "type": "string"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {
    "project": {
      "title": "Project",
      "target": "jiraProject",
      "required": false,
      "many": false
    }
  }
}
```

Blueprint Properties

You may modify the properties in your blueprints depending on what you want to track in your Jira projects and issues.

Create the following webhook configuration [using Port's UI](/build-your-software-catalog/custom-integration/webhook/.md?operation=ui#configuring-webhook-endpoints)

Jira webhook configuration

1. **Basic details** tab - fill the following details:

   <!-- -->

   1. Title : `Jira mapper`;
   2. Identifier : `jira_mapper`;
   3. Description : `A webhook configuration to map Jira projects and issues to Port`;
   4. Icon : `Jira`;

2. **Integration configuration** tab - fill the following JQ mapping:

```
mappings:
  - blueprint: jiraProject
    filter: .webhookEvent == "project_created" or .webhookEvent == "project_updated"
    entity:
      identifier: .project.key
      title: .project.name
      properties:
        url: .project.self
        description: .project.description
        type: .project.projectTypeKey
        lead: .project.lead.displayName // null
        issueCount: 0
  - blueprint: jiraIssue
    filter: .webhookEvent | startswith("jira:issue")
    entity:
      identifier: .issue.key
      title: .issue.fields.summary
      properties:
        url: .issue.self
        status: .issue.fields.status.name
        issueType: .issue.fields.issuetype.name
        priority: .issue.fields.priority.name // null
        assignee: .issue.fields.assignee.displayName // null
        reporter: .issue.fields.reporter.displayName // null
        creator: .issue.fields.creator.displayName // null
      relations:
        project: .issue.fields.project.key
```

note

Take note of, and copy the Webhook URL that is provided in this tab

3. Click **Save** at the bottom of the page.

### Create a webhook in Jira[â](#create-a-webhook-in-jira "Direct link to Create a webhook in Jira")

1. Log in to Jira as a user with the Administer global permission;

2. Click the gear icon at the top right corner;

3. Choose **System**;

4. At the bottom of the sidebar on the left, under **Advanced**, choose **WebHooks**;

5. Click on **Create a WebHook**

6. Input the following details:

   <!-- -->

   1. `Name` - use a meaningful name such as Port Webhook;
   2. `Status` - be sure to keep the webhook **Enabled**;
   3. `Webhook URL` - enter the value of the `url` key you received after creating the webhook configuration in Port;
   4. `Description` - enter a description for the webhook;
   5. `Issue related events` - enter a JQL query in this section to filter the issues that get sent to the webhook (if you leave this field empty, all issues will trigger a webhook event);
   6. Under `Issue` - mark created, updated and delete;
   7. Under the `Project related events` section, go to `Projects` and mark created, updated and deleted;

7. Click **Create** at the bottom of the page.

tip

In order to view the different payloads and events available in Jira webhooks, [look here](https://developer.atlassian.com/server/jira/platform/webhooks/)

Done! any change you make to a project or an issue (open, close, edit, etc.) will trigger a webhook event that Jira will send to the webhook URL provided by Port. Port will parse the events according to the mapping and update the catalog entities accordingly.

### Import Jira Historical Issues (Python Script)[â](#import-jira-historical-issues-python-script "Direct link to Import Jira Historical Issues (Python Script)")

In addition to real-time webhook events, you can use the following Python script to fetch existing data from the Jira Server API and ingest it to Port.

#### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This example utilizes the same [blueprint and webhook](#port-configuration) definition from the previous section.

In addition, you require the following environment variables:

* `PORT_CLIENT_ID` - Your Port client id
* `PORT_CLIENT_SECRET` - Your Port client secret
* `JIRA_API_URL` - Your Jira server host such as `https://jira.yourdomain.com`
* `JIRA_USERNAME` - Your Jira username to use when accessing the Jira Software (Server) resources
* `JIRA_PASSWORD` - Your Jira account password or token to use when accessing the Jira resources

Port credentials

Find your credentials using [these instructions](https://docs.port.io/build-your-software-catalog/custom-integration/api/#find-your-port-credentials).

Use the following Python script to ingest historical Jira issues into port:

Jira Python script for historical issues

```
import requests
import json
import os
from requests.auth import HTTPBasicAuth

# Port API configuration
PORT_CLIENT_ID = os.getenv("PORT_CLIENT_ID")
PORT_CLIENT_SECRET = os.getenv("PORT_CLIENT_SECRET")
PORT_API_URL = "https://api.port.io"

# Jira configuration
JIRA_API_URL = os.getenv("JIRA_API_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_PASSWORD = os.getenv("JIRA_PASSWORD")

def get_port_token():
    """Get Port access token"""
    response = requests.post(
        f"{PORT_API_URL}/v1/auth/access_token",
        json={
            "clientId": PORT_CLIENT_ID,
            "clientSecret": PORT_CLIENT_SECRET
        }
    )
    response.raise_for_status()
    return response.json()["accessToken"]

def get_jira_projects():
    """Fetch all projects from Jira"""
    auth = HTTPBasicAuth(JIRA_USERNAME, JIRA_PASSWORD)
    response = requests.get(
        f"{JIRA_API_URL}/rest/api/2/project",
        auth=auth
    )
    response.raise_for_status()
    return response.json()

def get_jira_issues(project_key):
    """Fetch all issues for a specific project"""
    auth = HTTPBasicAuth(JIRA_USERNAME, JIRA_PASSWORD)
    start_at = 0
    max_results = 100
    all_issues = []
    
    while True:
        response = requests.get(
            f"{JIRA_API_URL}/rest/api/2/search",
            auth=auth,
            params={
                "jql": f"project = {project_key}",
                "startAt": start_at,
                "maxResults": max_results,
                "fields": "summary,status,issuetype,priority,assignee,reporter,creator,project"
            }
        )
        response.raise_for_status()
        data = response.json()
        
        all_issues.extend(data["issues"])
        
        if len(data["issues"]) < max_results:
            break
            
        start_at += max_results
    
    return all_issues

def create_port_entity(entity_data, blueprint_id, port_token):
    """Create an entity in Port"""
    headers = {
        "Authorization": f"Bearer {port_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        f"{PORT_API_URL}/v1/blueprints/{blueprint_id}/entities",
        headers=headers,
        json=entity_data
    )
    
    if response.status_code == 409:
        # Entity already exists, update it
        entity_identifier = entity_data["identifier"]
        response = requests.put(
            f"{PORT_API_URL}/v1/blueprints/{blueprint_id}/entities/{entity_identifier}",
            headers=headers,
            json=entity_data
        )
    
    response.raise_for_status()
    return response.json()

def main():
    # Get Port token
    port_token = get_port_token()
    print("Got Port token")
    
    # Fetch projects from Jira
    projects = get_jira_projects()
    print(f"Found {len(projects)} projects")
    
    for project in projects:
        # Create project entity in Port
        project_entity = {
            "identifier": project["key"],
            "title": project["name"],
            "properties": {
                "url": project["self"],
                "description": project.get("description", ""),
                "type": project.get("projectTypeKey", ""),
                "lead": project.get("lead", {}).get("displayName", ""),
                "issueCount": 0
            }
        }
        
        try:
            create_port_entity(project_entity, "jiraProject", port_token)
            print(f"Created/updated project: {project['key']}")
        except Exception as e:
            print(f"Error creating project {project['key']}: {e}")
        
        # Fetch and create issues for this project
        issues = get_jira_issues(project["key"])
        print(f"Found {len(issues)} issues for project {project['key']}")
        
        for issue in issues:
            issue_entity = {
                "identifier": issue["key"],
                "title": issue["fields"]["summary"],
                "properties": {
                    "url": issue["self"],
                    "status": issue["fields"]["status"]["name"],
                    "issueType": issue["fields"]["issuetype"]["name"],
                    "priority": issue["fields"]["priority"]["name"] if issue["fields"]["priority"] else None,
                    "assignee": issue["fields"]["assignee"]["displayName"] if issue["fields"]["assignee"] else None,
                    "reporter": issue["fields"]["reporter"]["displayName"] if issue["fields"]["reporter"] else None,
                    "creator": issue["fields"]["creator"]["displayName"] if issue["fields"]["creator"] else None
                },
                "relations": {
                    "project": issue["fields"]["project"]["key"]
                }
            }
            
            try:
                create_port_entity(issue_entity, "jiraIssue", port_token)
                print(f"Created/updated issue: {issue['key']}")
            except Exception as e:
                print(f"Error creating issue {issue['key']}: {e}")

if __name__ == "__main__":
    main()
```

Done! you can now import historical issues from Jira into Port. Port will parse the issues according to the mapping and update the catalog entities accordingly.
