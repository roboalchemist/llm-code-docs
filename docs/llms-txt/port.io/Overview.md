# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/Overview.md

# Overview

Port's AWS integration allows you to import your AWS resources into Port, with flexible deployment options to match your needs.

## Deployment options[â](#deployment-options "Direct link to Deployment options")

The integration can be deployed using one of the following methods:

* **[Hosted by Port](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/installation/hosted-by-port/.md)**: Fully managed by Port with zero maintenance required. Simply create IAM roles via CloudFormation, and Port handles the rest.
* **[Self-hosted](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/installation/self-hosted/.md)**: Deploy the integration in your own infrastructure using Helm or Docker for complete control.

The integration periodically syncs your AWS resources to ensure your Port catalog stays up-to-date with your AWS infrastructure. For detailed information about the IAM role architecture for the hosted version, see the [IAM role architecture](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/installation/hosted-by-port/iam-role-architecture.md) page.

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

Easily fill your software catalog with data directly from your AWS Organization, for example:

* Map all the resources in your AWS Accounts, including **ECS Clusters**, **S3 Buckets**, and **EC2 Instances** with zero maintenance required.
* Keep your Port catalog synchronized with your AWS infrastructure through periodic updates.
* Use relations to create complete, easily digestible views of your AWS infrastructure inside Port.
* Enjoy a fully managed experience with no infrastructure to maintain or updates to apply.

## Key advantages[â](#key-advantages "Direct link to Key advantages")

AWS Hosted by Port provides several advantages over the [AWS on-premise integration](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/installations/installation.md):

* **Fully hosted**: No infrastructure to maintain, update, or monitor.
* **Simplified installation**: Just deploy CloudFormation templates to create IAM roles.
* **Complete data**: Ensures no missing or incomplete resource information.

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

Property naming conventions

The AWS Hosted by Port integration returns all resource properties in **PascalCase** (for example: `Arn`, `BucketName`, `CreationDate`). When writing mappings and JQ expressions, reference properties using PascalCasing as shown in the examples below.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration you get after installing AWS Hosted by Port.

**Default mapping configuration (click to expand)**

```
deleteDependentEntities: true
createMissingRelatedEntities: true
enableMergeEntity: true
resources:
  - kind: AWS::Account::Info
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.Id
          title: .Properties.Name
          blueprint: '"awsAccount"'
  - kind: AWS::S3::Bucket
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.Arn
          title: .Properties.BucketName
          blueprint: '"s3Bucket"'
          properties:
            arn: .Properties.Arn
            region: .Properties.LocationConstraint
            creationDate: .Properties.CreationDate
            tags: .Properties.Tags
          relations:
            account: .__ExtraContext.AccountId
  - kind: AWS::EC2::Instance
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.InstanceId
          title: .Properties.InstanceId
          blueprint: '"ec2Instance"'
          properties:
            instanceType: .Properties.InstanceType
            state: .Properties.State.Name
            publicIpAddress: .Properties.PublicIpAddress
            privateIpAddress: .Properties.PrivateIpAddress
            tags: .Properties.Tags
            arn: >-
              "arn:aws:ec2:" + .__Region + ":" + .__AccountId + ":instance/" +
              .Properties.InstanceId
          relations:
            account: .__ExtraContext.AccountId
  - kind: AWS::ECS::Cluster
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.ClusterArn
          title: .Properties.ClusterName
          blueprint: '"ecsCluster"'
          properties:
            status: .Properties.Status
            runningTasksCount: .Properties.RunningTasksCount
            activeServicesCount: .Properties.ActiveServicesCount
            pendingTasksCount: .Properties.PendingTasksCount
            registeredContainerInstancesCount: .Properties.RegisteredContainerInstancesCount
            capacityProviders: .Properties.CapacityProviders
            clusterArn: .Properties.ClusterArn
            tags: .Properties.Tags
          relations:
            account: .__ExtraContext.AccountId
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Resource and property reference[â](#resource-and-property-reference "Direct link to Resource and property reference")

Refer to the [resource and property reference](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/.md) page for details on available AWS resources, their properties, and mapping examples.
