# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure.md

# Azure

Our integration with Azure provides the ability to export your Azure resources to Port, according to your configuration. After the initial import of data, the integration will also listen to live events from Azure to update data inside Port in real time.

Our integration with Azure supports real-time event processing, this allows for an accurate **real-time** representation of your Azure infrastructure inside Port.

tip

Port's Azure exporter is open source, view the source code [**here**](https://github.com/port-labs/ocean/tree/main/integrations/azure).

## ð¡ Azure integration common use cases[â](#-azure-integration-common-use-cases "Direct link to ð¡ Azure integration common use cases")

Our Azure integration makes it easy to fill the software catalog with data directly from your Azure subscription, for example:

* Map resources from your Azure subscriptions, such as **AKS**, **Storage Accounts**, **Container Apps**, **Load Balancers** and other Azure resources.
* Watch for Azure object changes (create/update/delete) in real-time, and automatically apply the changes to your entities in Port.
* Configure relations to other resources in your organization to create complete, easily digestible views of your resources and their relationships inside Port.

## Installation[â](#installation "Direct link to Installation")

The Azure exporter can be deployed in multiple ways, including Helm, ContainerApp, Docker and more.

Continue to the [installation](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/installation.md) guide to learn how to install the Azure exporter.

## Ingest Azure resources[â](#ingest-azure-resources "Direct link to Ingest Azure resources")

The Azure exporter can retrieve all the resources supported by the [Azure Resource Manager REST API](https://learn.microsoft.com/en-us/rest/api/resources/resources/list), and export them to Port as entities of existing blueprints.

For examples on how to map resources head to the [resource templates](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/.md) page.

## Sync approaches[â](#sync-approaches "Direct link to Sync approaches")

Port offers multiple approaches for synchronizing Azure resources, each suited for different use cases:

### Azure exporter (ocean-based)[â](#azure-exporter-ocean-based "Direct link to Azure exporter (ocean-based)")

* **Full resource scanning** for complete state synchronization via **Azure Resource Manager (ARM) REST API**.
* **Change notifications** via Azure Event Grid (**available only in the Terraform deployment**).
* **Managed deployment** via Helm, Docker, or ContainerApp.
* **Best for**: Production environments requiring comprehensive resource visibility, full resource schema, and real-time Event Grid updates (with Terraform).

### Azure incremental sync (standalone)[â](#azure-incremental-sync-standalone "Direct link to Azure incremental sync (standalone)")

* **Lightweight change detection** via Azure Resource Graph.
* **Efficient polling** with configurable time windows.
* **GitHub Actions deployment** for automated workflows.
* **Best for**: Production environments requiring comprehensive resource visibility, full resource schema, and real-time Event Grid updates.

Choosing the right approach

Use the Azure exporter when you need comprehensive resource scanning and can set up Event Grid for change notifications. Use the incremental sync integration when you want lightweight, efficient synchronization with minimal resource, don't have Event Grid infrastructure or partial schema coverage is acceptable.

## Next Steps[â](#next-steps "Direct link to Next Steps")

* Refer to the [Resource Templates](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/.md) page for templates on how to map Azure resources to Port.
* Check out the [Azure Multi Subscriptions](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/multi-subscriptions.md) guide for setting up synchronization of Azure resources.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration you get after installing the Azure integration.

**Default mapping configuration (Click to expand)**

```
resources:
- kind: subscription
  selector:
    query: 'true'
    apiVersion: '2022-09-01'
  port:
    entity:
      mappings:
        identifier: .id
        title: .display_name
        blueprint: '"azureSubscription"'
        properties:
          tags: .tags
- kind: Microsoft.Resources/resourceGroups
  selector:
    query: 'true'
    apiVersion: '2022-09-01'
  port:
    entity:
      mappings:
        identifier: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
          | join("/")
        title: .name
        blueprint: '"azureResourceGroup"'
        properties:
          location: .location
          provisioningState: .properties.provisioningState + .properties.provisioning_state
          tags: .tags
        relations:
          subscription: .id | split("/") | .[1] |= ascii_downcase |.[2] |= ascii_downcase
            | .[:3] |join("/")
- kind: Microsoft.App/containerApps
  selector:
    query: 'true'
    apiVersion: '2022-03-01'
  port:
    entity:
      mappings:
        identifier: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
          | join("/")
        title: .name
        blueprint: '"azureCloudResource"'
        properties:
          location: .location
          type: .type
          tags: .tags
        relations:
          resource_group: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
            | .[:5] |join("/")
- kind: Microsoft.Storage/storageAccounts
  selector:
    query: 'true'
    apiVersion: '2023-01-01'
  port:
    entity:
      mappings:
        identifier: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
          | join("/")
        title: .name
        blueprint: '"azureCloudResource"'
        properties:
          location: .location
          type: .type
          tags: .tags
        relations:
          resource_group: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
            | .[:5] |join("/")
- kind: Microsoft.Compute/virtualMachines
  selector:
    query: 'true'
    apiVersion: '2023-03-01'
  port:
    entity:
      mappings:
        identifier: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
          | join("/")
        title: .name
        blueprint: '"azureCloudResource"'
        properties:
          location: .location
          type: .type
          tags: .tags
        relations:
          resource_group: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
            | .[:5] |join("/")
- kind: Microsoft.ContainerService/managedClusters
  selector:
    query: 'true'
    apiVersion: '2023-05-01'
  port:
    entity:
      mappings:
        identifier: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
          | join("/")
        title: .name
        blueprint: '"azureCloudResource"'
        properties:
          location: .location
          type: .type
          tags: .tags
        relations:
          resource_group: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
            | .[:5] |join("/")
- kind: Microsoft.Network/loadBalancers
  selector:
    query: 'true'
    apiVersion: '2023-02-01'
  port:
    entity:
      mappings:
        identifier: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
          | join("/")
        title: .name
        blueprint: '"azureCloudResource"'
        properties:
          location: .location
          type: .type
          tags: .tags
        relations:
          resource_group: .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
            | .[:5] |join("/")
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).
