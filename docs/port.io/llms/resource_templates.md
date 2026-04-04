# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates.md

# Resource Templates

This page contains the base examples for mapping Azure resources to Port.

This base example thrives to provide a simpler and more abstract way to map Azure resources to Port.

The simplification is achieved by using the generic `cloudResource` blueprint, which can be used to map any Azure resource to Port.

![Azure Basic Blueprints](/assets/images/basic-examples-blueprints-0300756d307e74b5d667da5e94dbbe2a.png)

## Mapping Azure Subscriptions[â](#mapping-azure-subscriptions "Direct link to Mapping Azure Subscriptions")

The following example demonstrates how to ingest your Azure Subscriptions to Port.<br /><!-- -->You can use the following Port blueprint definitions and integration configuration:

Subscription Blueprint

Create in Port

```
{
  "identifier": "azureSubscription",
  "title": "Azure Subscription",
  "icon": "Azure",
  "schema": {
    "properties": {
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
}
```

Mapping configuration for Azure Subscriptions

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
          properties: {
            tags: .tags
          }
```

Here are the API references we used to create those blueprints and app config:

* [Subscription](https://docs.microsoft.com/en-us/rest/api/resources/subscriptions/list)

## Mapping Resource Groups[â](#mapping-resource-groups "Direct link to Mapping Resource Groups")

Relate subscriptions and resource groups

The Resource Group has a relation to the Subscription, so the creation of the [Subscription blueprint](#mapping-azure-subscriptions) is required.

The following example demonstrates how to ingest your Azure Resource Groups to Port.<br /><!-- -->You can use the following Port blueprint definitions and integration configuration:

Resource Group blueprint

Create in Port

```
{
  "identifier": "azureResourceGroup",
  "description": "This blueprint represents an Azure Resource Group in our software catalog",
  "title": "Resource Group",
  "icon": "Azure",
  "schema": {
    "properties": {
      "location": {
        "title": "Location",
        "type": "string"
      },
      "provisioningState": {
        "title": "Provisioning State",
        "type": "string"
      },
      "tags": {
        "title": "Tags",
        "type": "object"
      }
    }
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "subscription": {
      "target": "azureSubscription",
      "title": "Subscription",
      "required": false,
      "many": false
    }
  }
}
```

Mapping Configuration for Resource group

```
resources:
  - kind: Microsoft.Resources/resourceGroups
    selector:
      query: 'true'
      apiVersion: '2022-09-01'
    port:
      entity:
        mappings:
          identifier: >-
            .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase |
            join("/")
          title: .name
          blueprint: '"azureResourceGroup"'
          properties:
            location: .location
            provisioningState: .properties.provisioningState + .properties.provisioning_state
            tags: .tags
          relations:
            subscription: >-
              .id | split("/") | .[1] |= ascii_downcase |.[2] |= ascii_downcase
              | .[:3] |join("/")
```

Here are the API references we used to create those blueprints and app config:

* [Resource Group](https://docs.microsoft.com/en-us/rest/api/resources/resourcegroups/list)

## Mapping Cloud Resources[â](#mapping-cloud-resources "Direct link to Mapping Cloud Resources")

The following example demonstrates how to ingest your Azure Resources to Port.<br /><!-- -->You can use the following Port blueprint definitions and integration configuration:

Relate resources and resource groups

The Resources below have a relation to the Resource Group, so the creation of the [Resource Group blueprint](#mapping-resource-groups) is required.

Cloud Resource Blueprint

Create in Port

```
{
  "identifier": "azureCloudResource",
  "title": "Cloud Resource",
  "icon": "Azure",
  "schema": {
    "properties": {
      "type": {
        "icon": "Service",
        "title": "Type",
        "type": "string"
      },
      "location": {
        "icon": "Home",
        "title": "Location",
        "type": "string"
      },
      "tags": {
        "title": "Tags",
        "type": "object",
        "icon": "BlankPage"
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
```

Mapping configuration for cloud resources

Cloud resource kind

The `cloudResource` kind is a generic kind that can be used to map most cloud resources.

The mapping requires passing the resource kind and version as a parameter inside the `resourceKinds` object.

It is possible that some of the kinds that you want to export are not in this example, head to the bottom of the page to see how to add them.

```
resources:
  - kind: Microsoft.App/containerApps
    selector:
      query: 'true'
      apiVersion: '2022-03-01'
    port:
      entity:
        mappings:
          identifier: >-
            .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase |
            join("/")
          title: .name
          blueprint: '"azureCloudResource"'
          properties:
            location: .location
            type: .type
            tags: .tags
          relations:
            resource_group: >-
              .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
              | .[:5] |join("/")
  - kind: Microsoft.Storage/storageAccounts
    selector:
      query: 'true'
      apiVersion: '2023-01-01'
    port:
      entity:
        mappings:
          identifier: >-
            .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase |
            join("/")
          title: .name
          blueprint: '"azureCloudResource"'
          properties:
            location: .location
            type: .type
            tags: .tags
          relations:
            resource_group: >-
              .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
              | .[:5] |join("/")
  - kind: Microsoft.Compute/virtualMachines
    selector:
      query: 'true'
      apiVersion: '2023-03-01'
    port:
      entity:
        mappings:
          identifier: >-
            .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase |
            join("/")
          title: .name
          blueprint: '"azureCloudResource"'
          properties:
            location: .location
            type: .type
            tags: .tags
          relations:
            resource_group: >-
              .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
              | .[:5] |join("/")
  - kind: Microsoft.ContainerService/managedClusters
    selector:
      query: 'true'
      apiVersion: '2023-05-01'
    port:
      entity:
        mappings:
          identifier: >-
            .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase |
            join("/")
          title: .name
          blueprint: '"azureCloudResource"'
          properties:
            location: .location
            type: .type
            tags: .tags
          relations:
            resource_group: >-
              .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
              | .[:5] |join("/")
  - kind: Microsoft.Network/loadBalancers
    selector:
      query: 'true'
      apiVersion: '2023-02-01'
    port:
      entity:
        mappings:
          identifier: >-
            .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase |
            join("/")
          title: .name
          blueprint: '"azureCloudResource"'
          properties:
            location: .location
            type: .type
            tags: .tags
          relations:
            resource_group: >-
              .id | split("/") | .[3] |= ascii_downcase |.[4] |= ascii_downcase
              | .[:5] |join("/")
```

Here are the API references we used to create those blueprints and app config:

* [AKS](https://learn.microsoft.com/en-us/rest/api/aks/managed-clusters/list?tabs=HTTP)
* [Container App](https://learn.microsoft.com/en-us/rest/api/containerapps/stable/container-apps/list-by-subscription?tabs=HTTP)
* [Load Balancer](https://learn.microsoft.com/en-us/rest/api/load-balancer/load-balancers/list-all?tabs=HTTP)
* [Virtual Machine](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/list-all?tabs=HTTP)
* [Storage Account](https://docs.microsoft.com/en-us/rest/api/storagerp/storageaccounts/list)

## Mapping Extra Resources[â](#mapping-extra-resources "Direct link to Mapping Extra Resources")

The resources in this page are only a few of the resources that the Azure Exporter supports.

If the resources you want to ingest into Port do not appear in these examples, you can head to the [Mapping Extra Resources](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/mapping_extra_resources.md) page to learn about all of the kinds of Azure resources that are supported by the Azure integration and how to map them into Port.

## Advanced Use Cases[â](#advanced-use-cases "Direct link to Advanced Use Cases")

In certain scenarios you may want to model your Azure resources in a more detailed way.

For example, you may want to model a Storage Account and its Containers separately.

For these cases, head to the [Advanced Resource templates](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/advanced.md) page to learn how to model your Azure resources in a more detailed way.
