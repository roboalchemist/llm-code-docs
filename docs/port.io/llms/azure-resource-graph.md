# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md

# Azure Resource Graph (Beta)

Loading version...

Availability Notice

This integration is in closed beta and is not available for general use. Please contact [Port's support team](http://support.port.io/) to request access.

This integration provides a robust solution for syncing your Azure resources to Port by leveraging the open-source [Ocean framework](https://ocean.port.io). It is designed for high-volume data ingestion across multiple subscriptions and efficiently queries the Azure Resource Graph API, ensuring high-performance data ingestion even in large-scale environments.

Key advantages:

* **Centralized Syncing**: Ingest resources from all your Azure subscriptions with a single deployment.
* **High-Speed Ingestion**: Leverage Azure Resource Graph to query and sync up to 5000 subscriptions simultaneously for maximum performance.
* **Customizable Mapping**: Take full control over which resource types are ingested and how they are mapped to your software catalog.

On each run, the integration performs a full synchronization, so your software catalog always reflects the current state of your Azure resources. You can use declarative YAML mapping to transform raw data and model it according to your software catalog's structure.

The integration is packaged as a Docker container and can be deployed in any environment that supports it, such as Kubernetes or your CI/CD pipeline. This gives you full control over its execution schedule and operational management.

## Supported resources[â](#supported-resources "Direct link to Supported resources")

The Azure Resource Graph integration supports the following `kinds`:

* `Resources` - represents an Azure resource. By default, they're pulled from the `resources` table, which includes a wide array of Azure resources such as virtual machines, storage accounts, network interfaces, and more. You can override this by specifying another Azure Resource Graph table. To see all supported tables, refer to the [official documentation](https://learn.microsoft.com/en-us/azure/governance/resource-graph/reference/supported-tables-resources).
* `ResourceContainers` - represents management groups, subscriptions, and resource groups, providing the hierarchical context for your Azure resources.
* `Subscription` - represents subscriptions from the Azure Resource Manager API.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration you get after installing the Azure integration.

**Default mapping configuration (click to expand)**

```
resources:
- kind: subscription
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .subscriptionId
        title: .displayName
        blueprint: '"azureSubscription"'
        properties:
          tags: .tags
          state: .state
          subscriptionPolicies: .subscriptionPolicies
- kind: resourceContainer
  selector:
    query: 'true'
    graphQuery: >-
      "resourcecontainers 
      | where type =~'microsoft.resources/subscriptions/resourcegroups' 
      | project id, type, name, location, tags, subscriptionId, resourceGroup 
      | extend resourceGroup=tolower(resourceGroup) 
      | extend type=tolower(type)
      | order by id"
  port:
    entity:
      mappings:
        identifier: .id | gsub(" ";"_")
        title: .name
        blueprint: '"azureResourceGroup"'
        properties:
          tags: .tags
          type: .type
          location: .location
        relations:
          subscription: ("/subscriptions/" + .subscriptionId) | gsub(" ";"_")
- kind: resource
  selector:
    query: 'true'
    graphQuery: >-
      "resources 
      | project id, type, name, location, tags, subscriptionId, resourceGroup 
      | extend resourceGroup=tolower(resourceGroup) 
      | extend type=tolower(type) 
      | join kind=leftouter (
          resourcecontainers
          | where type =~ 'microsoft.resources/subscriptions/resourcegroups'
          | project rgName=tolower(name), rgTags=tags, rgSubscriptionId=subscriptionId
      ) on $left.subscriptionId == $right.rgSubscriptionId and
      $left.resourceGroup == $right.rgName 
      | project id, type, name, location, tags, subscriptionId, resourceGroup, rgTags
      | order by id"
  port:
    entity:
      mappings:
        identifier: .id | gsub(" ";"_")
        title: .name
        blueprint: '"azureResource"'
        properties:
          tags: .tags
          location: .location
        relations:
          resource_group: >-
            ("/subscriptions/" + .subscriptionId + "/resourceGroups/"  +
            .resourceGroup) | gsub(" ";"_")
```

### The `graphQuery` selector[â](#the-graphquery-selector "Direct link to the-graphquery-selector")

The `graphQuery` selector is a powerful feature that allows you to specify a custom query to fetch the exact Azure resources you need. It uses the [**Kusto Query Language (KQL)**](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/query-language).

With `graphQuery`, you can:

* **Filter resources** based on their properties, tags, or any other attribute.
* **Select specific properties** to reduce the amount of data ingested.
* **Join different resource tables** to enrich the data.
* **Perform aggregations** and other advanced operations.

Optimizing your `graphQuery`

It is highly recommended to optimize your `graphQuery` to fetch only the data you need. A well-crafted query can significantly improve the performance of the integration and ensure that your software catalog is not cluttered with unnecessary information.

For example, instead of fetching all resources and then filtering them in the mapping, you can use the `where` clause in your query to filter the resources at the source.

Required: Add order by id to all queries

Due to [known limitations](#known-limitations) in the Azure Resource Graph API, you should include `| order by id` at the end of all your `graphQuery` selectors. This ensures stable pagination and prevents data inconsistencies. See the [known limitations](#known-limitations) section for details.

Here is an example of a broad query versus an optimized query:

**Broad Query:**

```
resources
| project id, type, name, location, tags, subscriptionId, resourceGroup
| order by id
```

**Optimized Query:**

```
resources
| where type in~ ('microsoft.compute/virtualmachines', 'microsoft.storage/storageaccounts') and tags.environment == 'production'
| project id, type, name, location, tags, subscriptionId, resourceGroup
| order by id
```

The optimized query fetches only virtual machines and storage accounts that have the `environment` tag set to `production`, which is much more efficient.

### Known limitations[â](#known-limitations "Direct link to Known limitations")

The Azure Resource Graph API has undocumented behavior that can cause data inconsistencies when querying large datasets. We have identified two specific issues:

1. **Data inconsistency with multi-subscription queries** - When querying multiple Azure subscriptions simultaneously, subscriptions with a large number of resources may return inconsistent or incomplete data.
2. **Data drift during pagination** - If resources are created or deleted in Azure while the integration is paginating through results, the API may return newly created resources instead of existing ones on subsequent pages. This can cause entities to appear as "deleted" in Port when they still exist in Azure.

#### Workaround[â](#workaround "Direct link to Workaround")

To prevent these issues, **adding `| order by id` at the end of all your `graphQuery` selectors**. This ensures stable ordering during pagination and significantly reduces data inconsistencies.

**Before (problematic):**

```
resources
| where type in~ ('microsoft.compute/virtualmachines')
| project id, type, name, location, tags, subscriptionId, resourceGroup
```

**After (recommended):**

```
resources
| where type in~ ('microsoft.compute/virtualmachines')
| project id, type, name, location, tags, subscriptionId, resourceGroup
| order by id
```

## Setup[â](#setup "Direct link to Setup")

To set up the Azure Resource Graph exporter, you'll need to configure both Port credentials and Azure app registration.

### Port credentials

To get your Port credentials, go to your [Port application](https://app.getport.io), click on the `...` button in the top right corner, and select `Credentials`. Here you can view and copy your `CLIENT_ID` and `CLIENT_SECRET`:

![](/img/software-catalog/credentials-modal.png)

### Azure setup

This integration requires the standard [Azure app registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate%2Cexpose-a-web-api) setup.

Keep the following credentials handy after setup:

* `AZURE_CLIENT_ID`: The client ID of the Azure service principal
* `AZURE_CLIENT_SECRET`: The client secret of the Azure service principal
* `AZURE_TENANT_ID`: The tenant ID of the Azure service principal

## Azure App Registration Setup

To ingest resources from Azure, you will need to create an Azure App Registration and assign it read permissions to the resources you want to ingest.

1. Create an Azure App Registration in the Azure portal.

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/1-app-registration.png)

   <br />

   <br />

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/2-register-an-application.png)

   <br />

   <br />

2. Copy the `Application (client) ID` and `Directory (tenant) ID` from the App Registration.

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/3-result-of-app-registration.png)

   <br />

   <br />

3. Create a client secret for the App Registration.

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/4-creating-client-secret.png)

   <br />

   <br />

4. Copy the `Application (client) Secret` from the App Registration.

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/5-copy-secret-value.png)

   <br />

   <br />

5. Create a new role assignment for the App Registration. Go to the `Access control (IAM)` section of the subscription you want to ingest resources from.<br /><br />Click on `Add role assignment`.

   Multi Account Support

   It is supported to ingest resources from multiple subscriptions, for that you will have to repeat the role assignment for each subscription you want to ingest resources from.

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/6-add-role-assignment.png)

   <br />

   <br />

6. Assign the `Reader` role to the App Registration.

   Permissions

   The Reader role is recommended for querying all resources in your Azure subscription. You can restrict permissions to specific resource groups or types by assigning a different role. If you do this, remember to adjust permissions when adding more resources to the catalog. Basic permissions required for ingesting resources from Azure include:

   * `Microsoft.Resources/subscriptions/read` (to list the accessible subscriptions)
   * `Microsoft.Resources/subscriptions/resourceGroups/read` (to list the accessible resource groups)
   * `read`/`list` permissions to the resources you want to ingest

   ![](/img/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/app-registration/7-assign-member-to-role.png)

   <br />

   <br />

## Installation[â](#installation "Direct link to Installation")

* Helm (Scheduled)
* CI/CD (Scheduled)
* On-Prem (Once)

Deploy the Azure resource graph exporter using Helm on Kubernetes to support scheduled resyncs of resources from Azure to Port.

## Prerequisites

* [Port API credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)
* [Helm](https://helm.sh/docs/intro/install/) >= 3.0.0
* [Azure App Registration Credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)

## Installation

Now that you have the Azure App Registration details, you can install the Azure exporter using Helm.

You should have the following information ready:

* Port API credentials, you can check out the [Port API documentation](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup).

  <!-- -->

  * `PORT_CLIENT_ID`
  * `PORT_CLIENT_SECRET`

* Azure Credentials:

  <!-- -->

  * `AZURE_CLIENT_ID`: The Application (client) ID from the Azure App Registration.
  * `AZURE_CLIENT_SECRET`: The Application (client) Secret from the Azure App Registration.
  * `AZURE_TENANT_ID`: The Directory (tenant) ID from the Azure App Registration.

```
helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install azure port-labs/port-ocean \
  --set port.clientId="PORT_CLIENT_ID"  \
  --set port.clientSecret="PORT_CLIENT_SECRET"  \
  --set port.baseUrl="https://api.port.io"  \
  --set initializePortResources=true  \
  --set sendRawDataExamples=true  \
  --set scheduledResyncInterval=1440 \
  --set integration.type="azure-rg"  \
  --set integration.identifier="azure-resource-graph"  \
  --set integration.eventListener.type="POLLING"  \
  --set integration.config.azureClientId="<AZURE_CLIENT_ID>"  \
  --set integration.config.azureClientSecret="<AZURE_CLIENT_SECRET>" \
  --set integration.config.azureTenantId="<AZURE_TENANT_ID>"
```

Selecting a Port API URL by account region

The `port_region`, `port.baseUrl`, `portBaseUrl`, `port_base_url` and `OCEAN__PORT__BASE_URL` parameters select which Port API instance to use:

* **EU** ([app.port.io](https://app.port.io)) â `https://api.port.io`
* **US** ([app.us.port.io](https://app.us.port.io)) â `https://api.us.port.io`

- Azure DevOps
- GitHub Actions
- ArgoCD
- GitLab

Deploy the Azure exporter using an Azure DevOps pipeline to support scheduled resyncs of resources from Azure to Port.

## Prerequisites

* [Port API credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)
* Access to an Azure DevOps project with permission to configure pipelines and secrets.
* [Azure App Registration Credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)

## Installation

Now that you have the Azure App Registration details, you can set up the Azure exporter using an Azure DevOps pipeline.

Make sure to configure the following [secret variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops\&tabs=yaml%2Cbash) in a variable group:

* Port API credentials:

  <!-- -->

  * `PORT_CLIENT_ID`
  * `PORT_CLIENT_SECRET`

* Azure Credentials:

  <!-- -->

  * `OCEAN__SECRET__AZURE_CLIENT_ID`: The Application (client) ID from the Azure App Registration.
  * `OCEAN__SECRET__AZURE_CLIENT_SECRET`: The Application (client) Secret from the Azure App Registration.
  * `OCEAN__SECRET__AZURE_TENANT_ID`: The Directory (tenant) ID from the Azure App Registration.

Here is an example for `azure-pipeline-integration.yml` workflow file:<br /><!-- -->Make sure to change the highlighted line to your variable group's name.

**Azure pipeline integration (click to expand)**

```
name: Azure Resource Graph Exporter Pipeline

trigger: none

schedules:
  - cron: "0 */4 * * *"
    displayName: Every 4 Hours
    branches:
      include:
        - main
    always: true

variables:
  - group: port-azure-exporter-secrets  # Contains the secrets used below

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: Bash@3
    displayName: 'Run Ocean Sail (Azure-RG)'
    inputs:
      targetType: 'inline'
      script: |
        set -euo pipefail

        echo "Building .env file for Ocean Sail..."

        echo "OCEAN__PORT__CLIENT_ID=$(PORT_CLIENT_ID)" > .sail-env
        echo "OCEAN__PORT__CLIENT_SECRET=$(PORT_CLIENT_SECRET)" >> .sail-env
        echo "OCEAN__PORT__BASE_URL=https://api.port.io" >> .sail-env

        echo "OCEAN__EVENT_LISTENER={\"type\":\"ONCE\"}" >> .sail-env
        echo "OCEAN__INITIALIZE_PORT_RESOURCES=true" >> .sail-env

        echo "OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_ID=$(OCEAN__SECRET__AZURE_CLIENT_ID)" >> .sail-env
        echo "OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_SECRET=$(OCEAN__SECRET__AZURE_CLIENT_SECRET)" >> .sail-env
        echo "OCEAN__INTEGRATION__CONFIG__AZURE_TENANT_ID=$(OCEAN__SECRET__AZURE_TENANT_ID)" >> .sail-env

        echo "Running Ocean Sail container..."
        docker run -i --rm \
          --platform=linux/amd64 \
          --env-file .sail-env \
          ghcr.io/port-labs/port-ocean-azure-rg:latest

  - task: Bash@3
    displayName: 'Clean up .env file'
    condition: always()
    inputs:
      targetType: 'inline'
      script: |
        rm -f .sail-env
```

Deploy the Azure exporter using Github Actions to support scheduled resyncs of resources from Azure to Port.

* [Port API credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)
* [Azure App Registration Credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)

## Installation

Now that you have the Azure App Registration details, you can set up the Azure exporter using Github Actions.

Make sure to configure the following [Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions):

* Port API credentials:

  <!-- -->

  * `PORT_CLIENT_ID`
  * `PORT_CLIENT_SECRET`

* Azure Credentials:

  <!-- -->

  * `OCEAN__SECRET__AZURE_CLIENT_ID`: The Application (client) ID from the Azure App Registration.
  * `OCEAN__SECRET__AZURE_CLIENT_SECRET`: The Application (client) Secret from the Azure App Registration.
  * `OCEAN__SECRET__AZURE_TENANT_ID`: The Directory (tenant) ID from the Azure App Registration.

| Parameter                            | Description                                                                                                                          | Required |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`             | Your port client id.                                                                                                                 | â       |
| `OCEAN__PORT__CLIENT_SECRET`         | Your port client secret.                                                                                                             | â       |
| `OCEAN__PORT__BASE_URL`              | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US.                                                   | â       |
| `OCEAN__SECRET__AZURE_CLIENT_ID`     | Your Azure client ID.                                                                                                                | â       |
| `OCEAN__SECRET__AZURE_CLIENT_SECRET` | Your Azure client secret.                                                                                                            | â       |
| `OCEAN__SECRET__AZURE_TENANT_ID`     | Your Azure tenant ID.                                                                                                                | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`   | Default true, When set to false the integration will not create default blueprints and the port App config Mapping.                  | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`      | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true. | â       |
| `OCEAN__INTEGRATION__IDENTIFIER`     | Change the identifier to describe your integration, if not set will use the default one.                                             | â       |

<br />

Here is an example for `azure-rg-integration.yml` workflow file:

**GitHub Action integration (click to expand)**

```
name: Azure Resource Graph Exporter Workflow

on:
workflow_dispatch:
schedule:
	- cron: '0 */4 * * *' 

jobs:
run-integration:
	runs-on: ubuntu-latest
	steps:
	- name: Run azure-rg Integration
		uses: port-labs/ocean-sail@v1
		with:
		type: azure-rg
		port_client_id: ${{ secrets.PORT_CLIENT_ID }}
		port_client_secret: ${{ secrets.PORT_CLIENT_SECRET }}
		port_base_url: "https://api.port.io"
		config: |
			azure_client_id: ${{ secrets.OCEAN__SECRET__AZURE_CLIENT_ID }}
			azure_client_secret: ${{ secrets.OCEAN__SECRET__AZURE_CLIENT_SECRET }}
			azure_tenant_id: ${{ secrets.OCEAN__SECRET__AZURE_TENANT_ID }}
```

## Prerequisites

* [Port API credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)
* [ArgoCD](https://argo-cd.readthedocs.io/en/stable/getting_started/) >= 2.0.0
* [Azure App Registration Credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)

## Installation

1. Create a `values.yaml` file in `argocd/azure-rg-integration` in your git repository with the content:

```
  initializePortResources: true
  scheduledResyncInterval: 120
  integration:
    identifier: azure-rg-integration
    type: azure-rg
    eventListener:
      type: POLLING
	  config:
      azureClientId: <AZURE_CLIENT_ID>
		  azureClientSecret: <AZURE_CLIENT_SECRET>
		  azureTenantId: <AZURE_TENANT_ID>
```

2. Install the `azure-rg-integration` ArgoCD Application by creating the following `azure-rg-integration.yaml` manifest:

Replace placeholders

Remember to replace the placeholders for `YOUR_PORT_CLIENT_ID` `YOUR_PORT_CLIENT_SECRET` and `YOUR_GIT_REPO_URL`.<br /><!-- -->Multiple sources ArgoCD documentation can be found in the [official documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/#helm-value-files-from-external-git-repository).

**ArgoCD Application (click to expand)**

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
name: my-ocean-azure-rg-integration
namespace: argocd
spec:
destination:
	namespace: mmy-ocean-azure-rg-integration
	server: https://kubernetes.default.svc
project: default
sources:
- repoURL: 'https://port-labs.github.io/helm-charts/'
	chart: port-ocean
	targetRevision: 0.9.5
	helm:
	valueFiles:
	- $values/argocd/my-ocean-azure-rg-integration/values.yaml
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

3. Apply the `azure-rg-integration.yaml` manifest to your Kubernetes cluster.

```
kubectl apply -f azure-rg-integration.yaml
```

## Prerequisites

* [Port API credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)
* [Azure App Registration Credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)

Make sure to [configure the following GitLab variables](https://docs.gitlab.com/ee/ci/variables/#for-a-project):

| Parameter                                         | Description                                                                                                                          | Required |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `OCEAN__PORT__CLIENT_ID`                          | Your port client id.                                                                                                                 | â       |
| `OCEAN__PORT__CLIENT_SECRET`                      | Your port client secret.                                                                                                             | â       |
| `OCEAN__PORT__BASE_URL`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US.                                                   | â       |
| `OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_ID`     | The client ID of the Azure App Registration.                                                                                         | â       |
| `OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_SECRET` | The client secret of the Azure App Registration.                                                                                     | â       |
| `OCEAN__INTEGRATION__CONFIG__AZURE_TENANT_ID`     | The tenant ID of the Azure App Registration.                                                                                         | â       |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                | Default true, when set to false the integration will not create default blueprints and the port App config mapping.                  | â       |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true. | â       |

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
  INTEGRATION_TYPE: azure-rg
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
          -e OCEAN__PORT__CLIENT_ID=$PORT_CLIENT_ID \
          -e OCEAN__PORT__CLIENT_SECRET=$PORT_CLIENT_SECRET \
          -e OCEAN__PORT__BASE_URL="https://api.port.io" \
          -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
          -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
          -e OCEAN__EVENT_LISTENER='{"type": "ONCE"}' \
          -e OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_ID="Enter value here" \
          -e OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_SECRET="Enter value here" \
          -e OCEAN__INTEGRATION__CONFIG__AZURE_TENANT_ID="Enter value here" \
          $IMAGE_NAME

  rules: # Run only when changes are made to the main branch
    - if: '$CI_COMMIT_BRANCH == "main"'
```

## Prerequisites

* [Port API credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)
* [Docker](https://docs.docker.com/get-docker/)
* [Azure App Registration Credentials](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup)

## Installation

Now that you have the Azure App Registration details, you can install the Azure exporter using Docker.

You should have the following information ready:

* Port API credentials, you can check out the [Port API documentation](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/azure-resource-graph.md#setup).

  <!-- -->

  * `PORT_CLIENT_ID`
  * `PORT_CLIENT_SECRET`

* Azure Credentials:

  <!-- -->

  * `AZURE_CLIENT_ID`: The Application (client) ID from the Azure App Registration.
  * `AZURE_CLIENT_SECRET`: The Application (client) Secret from the Azure App Registration.
  * `AZURE_TENANT_ID`: The Directory (tenant) ID from the Azure App Registration.

**Environment Variables (click to expand)**

| Variable                                          | Description                                                                                                                         |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `OCEAN__PORT__CLIENT_ID`                          | Your Port client ID.                                                                                                                |
| `OCEAN__PORT__CLIENT_SECRET`                      | Your Port client secret.                                                                                                            |
| `OCEAN__PORT__BASE_URL`                           | Your Port API URL - `https://api.port.io` for EU, `https://api.us.port.io` for US                                                   |
| `OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_ID`     | The client ID of the Azure App Registration.                                                                                        |
| `OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_SECRET` | The client secret of the Azure App Registration.                                                                                    |
| `OCEAN__INTEGRATION__CONFIG__AZURE_TENANT_ID`     | The tenant ID of the Azure App Registration.                                                                                        |
| `OCEAN__EVENT_LISTENER`                           | [The event listener object](https://ocean.getport.io/framework/features/event-listener/).                                           |
| `OCEAN__INTEGRATION__IDENTIFIER`                  | The identifier of the integration.                                                                                                  |
| `OCEAN__INTEGRATION__TYPE`                        | should be set to `azure-rg`.                                                                                                        |
| `OCEAN__INITIALIZE_PORT_RESOURCES`                | Default true, When set to true the integration will create default blueprints and the port App config Mapping.                      |
| `OCEAN__SEND_RAW_DATA_EXAMPLES`                   | Enable sending raw data examples from the third party API to port for testing and managing the integration mapping. Default is true |

For example:

```
docker run -i --rm --platform=linux/amd64 \
  -e OCEAN__PORT__CLIENT_ID="$PORT_CLIENT_ID" \
  -e OCEAN__PORT__CLIENT_SECRET="$PORT_CLIENT_SECRET" \
  -e OCEAN__PORT__BASE_URL="https://api.port.io" \
  -e OCEAN__INITIALIZE_PORT_RESOURCES=true \
  -e OCEAN__SEND_RAW_DATA_EXAMPLES=true \
  -e OCEAN__EVENT_LISTENER='{"type": "ONCE"}' \
  -e OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_ID=AZURE_CLIENT_ID \
  -e OCEAN__INTEGRATION__CONFIG__AZURE_CLIENT_SECRET=$AZURE_CLIENT_SECRET \
  -e OCEAN__INTEGRATION__CONFIG__AZURE_TENANT_ID=$AZURE_TENANT_ID \
ghcr.io/port-labs/port-ocean-azure-rg:latest
```

## Examples[â](#examples "Direct link to Examples")

### Mapping Azure cloud resources[â](#mapping-azure-cloud-resources "Direct link to Mapping Azure cloud resources")

The following example demonstrates how to ingest your Azure Subscriptions to Port.<br /><!-- -->You can use the following Port blueprint definitions and integration configuration:

**Blueprint (click to expand)**

Create in Port

```
{
  "identifier": "azureCloudResources",
  "description": "This blueprint represents an Azure Cloud Resource in our software catalog",
  "title": "Azure Cloud Resources",
  "icon": "Azure",
  "schema": {
    "properties": {
      "tags": {
        "title": "Tags",
        "type": "object"
      },
      "type": {
        "title": "Type",
        "type": "string"
      },
      "location": {
        "title": "Location",
        "type": "string"
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

**Mapping configuration (click to expand)**

```
resources:
  - kind: resource
    selector:
      query: 'true'
      graphQuery: >-
        "resources 
        | where type in~ ('microsoft.insights/datacollectionendpoints', 'microsoft.compute/virtualmachines')
        | project id, type, name, location, tags, subscriptionId, resourceGroup 
        | extend resourceGroup=tolower(resourceGroup) 
        | extend type=tolower(type)
        | order by id"
    port:
      entity:
        mappings:
          identifier: .id | gsub(" ";"_")
          title: .name
          blueprint: '"azureCloudResources"'
          properties:
            tags: .tags
            type: .type
            location: .location
```

### Mapping cloud resources and resource groups[â](#mapping-cloud-resources-and-resource-groups "Direct link to Mapping cloud resources and resource groups")

The following example demonstrates how to ingest your Azure Subscriptions to Port.<br /><!-- -->You can use the following Port blueprint definitions and integration configuration:

**Blueprints (click to expand)**

```

[
  {
    "identifier": "azureResourceGroup",
    "description": "This blueprint represents an Azure Resource Group in our software catalog",
    "title": "Azure Resource Group",
    "icon": "Azure",
    "schema": {
      "properties": {
        "location": {
          "title": "Location",
          "type": "string"
        },
        "tags": {
          "title": "Tags",
          "type": "object"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {}
  },
  {
    "identifier": "azureResource",
    "description": "This blueprint represents an AzureCloud Resource in our software catalog",
    "title": "Azure Cloud Resources",
    "icon": "Git",
    "schema": {
      "properties": {
        "tags": {
          "title": "Tags",
          "type": "object"
        },
        "type": {
          "title": "Type",
          "type": "string"
        },
        "location": {
          "title": "Location",
          "type": "string"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "resource_group": {
        "title": "Resource Group",
        "target": "azureResourceGroup",
        "required": false,
        "many": false
      }
    }
  }
]
```

**Mapping configuration (click to expand)**

```
resources:
- kind: resourceContainer
  selector:
    query: 'true'
    graphQuery: >-
       "resourcecontainers 
        | where type =~ 'microsoft.resources/subscriptions/resourcegroups' 
        | where (tostring(tags['environment']) =~ 'prod')
        | project id, type, name, location, tags, subscriptionId, resourceGroup 
        | extend resourceGroup=tolower(resourceGroup) 
        | extend type=tolower(type)
        | order by id"
  port:
    entity:
      mappings:
        identifier: .id | gsub(" ";"_")
        title: .name
        blueprint: '"azureResourceGroup"'
        properties:
          tags: .tags
          location: .location

- kind: resource
  selector:
    query: 'true'
    graphQuery: >-
        "resources 
         | project id, type, name, location, tags, subscriptionId, resourceGroup 
         | extend resourceGroup=tolower(resourceGroup) 
         | extend type=tolower(type) 
         | join kind=leftouter (
            resourcecontainers
            | where type =~ 'microsoft.resources/subscriptions/resourcegroups'
            | project rgName=tolower(name), rgTags=tags, rgSubscriptionId=subscriptionId
        ) on $left.subscriptionId == $right.rgSubscriptionId and $left.resourceGroup == $right.rgName 
         | where (tostring(rgTags['environment']) =~ 'prod') and not (tostring(rgTags['environment']) =~ 'staging')
         | project id, type, name, location, tags, subscriptionId, resourceGroup, rgTags
         | order by id"
  port:
    entity:
      mappings:
        identifier: .id | gsub(" ";"_")
        title: .name
        blueprint: '"azureResource"'
        properties:
          tags: .tags
          type: .type
          location: .location
        relations:
          resource_group: >-
            ("/subscriptions/" + .subscriptionId + "/resourceGroups/"  + .resourceGroup) | gsub(" ";"_")
```
