# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-elastic-container-service.md

# Amazon Elastic Container Service (ECS)

<!-- -->

## AWS::ECS::Cluster[â](#awsecscluster "Direct link to AWS::ECS::Cluster")

The following example demonstrates how to ingest your AWS ECS clusters to Port.

#### ECS Cluster supported actions[â](#ecs-cluster-supported-actions "Direct link to ECS Cluster supported actions")

The table below summarizes the available actions for ingesting Amazon ECS Cluster resources in Port:

| Action                                                                                                        | Description                                                     | Type    | Required AWS Permission                    |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------- | ------------------------------------------ |
| [DescribeClustersAction](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html) | Discover ECS clusters and retrieve detailed configuration data. | Default | `ecs:ListClusters`, `ecs:DescribeClusters` |

All properties available by default

ECS clusters expose their key properties via the default DescribeClusters action.

You can use the following Port blueprint definitions and integration configuration:

**ECS Cluster blueprint (click to expand)**

Create in Port

```
{
  "identifier": "ecsCluster",
  "description": "This blueprint represents an AWS ECS cluster in our software catalog",
  "title": "ECS cluster",
  "icon": "AWS",
  "schema": {
    "properties": {
      "status": {
        "type": "string",
        "title": "Status"
      },
      "runningTasksCount": {
        "type": "number",
        "title": "Running tasks count"
      },
      "activeServicesCount": {
        "type": "number",
        "title": "Active services count"
      },
      "pendingTasksCount": {
        "type": "number",
        "title": "Pending tasks count"
      },
      "registeredContainerInstancesCount": {
        "type": "number",
        "title": "Registered container instances count"
      },
      "capacityProviders": {
        "type": "array",
        "title": "Capacity providers"
      },
      "clusterArn": {
        "type": "string",
        "title": "Cluster ARN"
      },
      "tags": {
        "type": "array",
        "title": "Tags",
        "items": {
          "type": "object",
          "properties": {
            "Key": {
              "type": "string"
            },
            "Value": {
              "type": "string"
            }
          }
        }
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": true,
      "many": false
    }
  }
}
```

**ECS Cluster mapping configuration (click to expand)**

```
resources:
  - kind: AWS::ECS::Cluster
    selector:
      query: 'true'
      # includeActions: No optional actions available for ECS clusters
      # All properties are included by default via DescribeClustersAction
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

## AWS::ECS::Service[â](#awsecsservice "Direct link to AWS::ECS::Service")

The following example demonstrates how to ingest your AWS ECS services to Port.

#### ECS Service supported actions[â](#ecs-service-supported-actions "Direct link to ECS Service supported actions")

The table below summarizes the available actions for ingesting Amazon ECS Service resources in Port:

| Action                                                                                                        | Description                                                                          | Type    | Required AWS Permission                    |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------- | ------------------------------------------ |
| [DescribeServicesAction](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html) | Discover ECS services within your clusters and retrieve detailed configuration data. | Default | `ecs:ListServices`, `ecs:DescribeServices` |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**ECS Service blueprint (click to expand)**

Create in Port

```
{
  "identifier": "ecsService",
  "title": "ECS Service",
  "icon": "AWS",
  "schema": {
    "properties": {
      "serviceName": {
        "type": "string",
        "title": "Service Name",
        "description": "The name of the ECS service"
      },
      "serviceArn": {
        "type": "string",
        "title": "ARN",
        "description": "The Amazon Resource Name (ARN) of the service"
      },
      "clusterArn": {
        "type": "string",
        "title": "Cluster ARN",
        "description": "The ARN of the cluster that hosts the service"
      },
      "taskDefinition": {
        "type": "string",
        "title": "Task Definition",
        "description": "The ARN of the task definition associated with the service"
      },
      "desiredCount": {
        "type": "number",
        "title": "Desired Count",
        "description": "The desired number of tasks for the service"
      },
      "runningCount": {
        "type": "number",
        "title": "Running Count",
        "description": "The number of tasks that are currently running"
      },
      "launchType": {
        "type": "string",
        "title": "Launch Type",
        "description": "The launch type of the service",
        "enum": ["EC2", "FARGATE", "EXTERNAL"]
      },
      "status": {
        "type": "string",
        "title": "Status",
        "description": "The current status of the service",
        "enum": ["ACTIVE", "DRAINING", "INACTIVE"]
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": false,
      "many": false
    },
    "cluster": {
      "title": "Cluster",
      "target": "ecsCluster",
      "required": false,
      "many": false
    }
  }
}
```

**ECS Service mapping configuration (click to expand)**

```
resources:
  - kind: AWS::ECS::Service
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.ServiceArn
          title: .Properties.ServiceName
          blueprint: '"ecsService"'
          properties:
            serviceName: .Properties.ServiceName
            serviceArn: .Properties.ServiceArn
            clusterArn: .Properties.ClusterArn
            taskDefinition: .Properties.TaskDefinition
            desiredCount: .Properties.DesiredCount
            runningCount: .Properties.RunningCount
            launchType: .Properties.LaunchType
            status: .Properties.Status
          relations:
            account: .__ExtraContext.AccountId
            cluster: .Properties.ClusterArn
```

For more details about ECS cluster properties, refer to the [AWS ECS API documentation](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html).
