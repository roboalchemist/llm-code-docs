# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-elastic-kubernetes-service.md

# Amazon Elastic Kubernetes Service (EKS)

<!-- -->

## AWS::EKS::Cluster[â](#awsekscluster "Direct link to AWS::EKS::Cluster")

The following example demonstrates how to ingest your AWS EKS clusters to Port.

#### EKS Cluster supported actions[â](#eks-cluster-supported-actions "Direct link to EKS Cluster supported actions")

The table below summarizes the available actions for ingesting Amazon EKS Cluster resources in Port:

| Action                                                                                                | Description                                            | Type    | Required AWS Permission                  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------- | ---------------------------------------- |
| [DescribeClusterAction](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeCluster.html) | Retrieve detailed configuration data for each cluster. | Default | `eks:DescribeCluster` `eks:ListClusters` |

All properties available by default

EKS clusters expose their key properties via the default DescribeCluster action.

You can use the following Port blueprint definitions and integration configuration:

**EKS Cluster blueprint (click to expand)**

Create in Port

```
{
  "identifier": "eksCluster",
  "title": "EKS Cluster",
  "icon": "AWS",
  "schema": {
    "properties": {
      "arn": {
        "type": "string",
        "title": "ARN",
        "description": "The Amazon Resource Name (ARN) of the EKS cluster"
      },
      "name": {
        "type": "string",
        "title": "Name",
        "description": "The name of the EKS cluster"
      },
      "version": {
        "type": "string",
        "title": "Kubernetes Version",
        "description": "The Kubernetes version of the EKS cluster"
      },
      "status": {
        "type": "string",
        "title": "Status",
        "description": "The status of the EKS cluster"
      },
      "endpoint": {
        "type": "string",
        "title": "Endpoint",
        "description": "The endpoint URL for the EKS cluster"
      },
      "roleArn": {
        "type": "string",
        "title": "Role ARN",
        "description": "The IAM role ARN associated with the EKS cluster"
      },
      "tags": {
        "type": "object",
        "title": "Tags",
        "description": "Tags associated with the EKS cluster",
        "additionalProperties": {
          "type": "string"
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
      "required": false,
      "many": false
    }
  }
}
```

**EKS Cluster mapping configuration (click to expand)**

```
resources:
  - kind: AWS::EKS::Cluster
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.Arn
          title: .Properties.Name
          blueprint: '"eksCluster"'
          properties:
            arn: .Properties.Arn
            name: .Properties.Name
            version: .Properties.Version
            status: .Properties.Status
            endpoint: .Properties.Endpoint
            roleArn: .Properties.RoleArn
            tags: .Properties.Tags
          relations:
            account: .__ExtraContext.AccountId
```

For more details about EKS cluster properties, refer to the [AWS EKS API documentation](https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html).
