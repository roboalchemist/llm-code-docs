# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-elastic-container-registry.md

# Amazon Elastic Container Registry (ECR)

<!-- -->

## AWS::ECR::Repository[â](#awsecrrepository "Direct link to AWS::ECR::Repository")

The following example demonstrates how to ingest your AWS ECR repositories to Port.

#### ECR Repository supported actions[â](#ecr-repository-supported-actions "Direct link to ECR Repository supported actions")

The table below summarizes the available actions for ingesting Amazon ECR Repository resources in Port:

| Action                                                                                                                | Description                                                         | Type     | Required AWS Permission    |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------- | -------------------------- |
| [DescribeRepositoriesAction](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositories.html) | Discover ECR repositories and retrieve detailed configuration data. | Default  | `ecr:DescribeRepositories` |
| [GetRepositoryPolicyAction](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRepositoryPolicy.html)   | Retrieve the repository policy for ECR repositories.                | Optional | `ecr:GetRepositoryPolicy`  |
| [GetLifecyclePolicyAction](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicy.html)     | Retrieve the lifecycle policy for ECR repositories.                 | Optional | `ecr:GetLifecyclePolicy`   |
| [ListTagsForResourceAction](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListTagsForResource.html)   | Retrieve tags associated with ECR repositories.                     | Optional | `ecr:ListTagsForResource`  |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**ECR Repository blueprint (click to expand)**

Create in Port

```
{
  "identifier": "ecrRepository",
  "description": "This blueprint represents an AWS ECR repository in our software catalog",
  "title": "ECR Repository",
  "icon": "AWS",
  "schema": {
    "properties": {
      "repositoryUri": {
        "type": "string",
        "title": "Repository URI"
      },
      "registryId": {
        "type": "string",
        "title": "Registry ID"
      },
      "createdAt": {
        "type": "string",
        "title": "Created At"
      },
      "imageTagMutability": {
        "type": "string",
        "title": "Image Tag Mutability"
      },
      "imageScanningConfiguration": {
        "type": "object",
        "title": "Image Scanning Configuration"
      },
      "encryptionConfiguration": {
        "type": "object",
        "title": "Encryption Configuration"
      },
      "lifecyclePolicy": {
        "type": "object",
        "title": "Lifecycle Policy"
      },
      "repositoryPolicyText": {
        "type": "string",
        "title": "Repository Policy Text"
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

**ECR Repository mapping configuration (click to expand)**

```
resources:
  - kind: AWS::ECR::Repository
    selector:
      query: 'true'
      includeActions:
        # Optional: Include additional actions for more properties
        # - GetRepositoryPolicyAction
        # - GetLifecyclePolicyAction
        # - ListTagsForResourceAction
    port:
      entity:
        mappings:
          identifier: .Properties.RepositoryArn
          title: .Properties.RepositoryName
          blueprint: '"ecrRepository"'
          properties:
            repositoryUri: .Properties.RepositoryUri
            registryId: .Properties.RegistryId
            createdAt: .Properties.CreatedAt
            imageTagMutability: .Properties.ImageTagMutability
            imageScanningConfiguration: .Properties.ImageScanningConfiguration
            encryptionConfiguration: .Properties.EncryptionConfiguration
            lifecyclePolicy: .Properties.LifecyclePolicy
            repositoryPolicyText: .Properties.RepositoryPolicyText
            tags: .Properties.Tags
          relations:
            account: .__ExtraContext.AccountId
```

#### Example response[â](#example-response "Direct link to Example response")

The following example shows the structure of the response data that Port processes for an ECR repository.

**ECR Repository response example (click to expand)**

```
{
  "Type": "AWS::ECR::Repository",
  "Properties": {
    "RepositoryName": "testing-actions",
    "RepositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/testing-actions",
    "RepositoryUri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/testing-actions",
    "RegistryId": "123456789012",
    "CreatedAt": "2024-05-14T12:12:40.109000+03:00",
    "ImageTagMutability": "MUTABLE",
    "ImageScanningConfiguration": {
      "scanOnPush": false
    },
    "EncryptionConfiguration": {
      "encryptionType": "AES256"
    },
    "RepositoryPolicyText": "{\n  \"Version\" : \"2012-10-17\",\n  \"Statement\" : [ {\n    \"Sid\" : \"new statement\",\n    \"Effect\" : \"Allow\",\n    \"Principal\" : {\n      \"AWS\" : \"arn:aws:iam::123456789012:role/admin-access\"\n    },\n    \"Action\" : \"ecr:DescribeRepositories\"\n  } ]\n}",
    "LifecyclePolicy": {
      "registryId": "123456789012",
      "repositoryName": "testing-actions",
      "lifecyclePolicyText": "{\"rules\":[{\"rulePriority\":1,\"selection\":{\"tagStatus\":\"tagged\",\"tagPatternList\":[\"testimagetag\"],\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":1},\"action\":{\"type\":\"expire\"}}]}",
      "lastEvaluatedAt": "1970-01-01T03:00:00+03:00"
    },
    "Tags": [
      {
        "Key": "Environment",
        "Value": "Production"
      },
      {
        "Key": "Team",
        "Value": "DevOps"
      }
    ]
  },
  "__ExtraContext": {
    "AccountId": "123456789012",
    "Region": "us-west-2"
  }
}
```

For more details about ECR repository properties, refer to the [AWS ECR API documentation](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/Welcome.html).
