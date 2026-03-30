# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-elastic-compute-cloud.md

# Amazon Elastic Compute Cloud (EC2)

<!-- -->

## AWS::EC2::Instance[â](#awsec2instance "Direct link to AWS::EC2::Instance")

The following example demonstrates how to ingest your AWS EC2 instances to Port.

#### EC2 Instance supported actions[â](#ec2-instance-supported-actions "Direct link to EC2 Instance supported actions")

The table below summarizes the available actions for ingesting Amazon EC2 Instance resources in Port:

| Action                                                                                                            | Description                                                      | Type     | Required AWS Permission      |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------- | ---------------------------- |
| [DescribeInstancesAction](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)      | Discover EC2 instances and retrieve detailed configuration data. | Default  | `ec2:DescribeInstances`      |
| [GetInstanceStatusAction](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html) | Retrieve instance status information.                            | Optional | `ec2:DescribeInstanceStatus` |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**EC2 Instance blueprint (click to expand)**

Create in Port

```
{
  "identifier": "ec2Instance",
  "description": "This blueprint represents an AWS EC2 instance in our software catalog",
  "title": "EC2 instance",
  "icon": "AWS",
  "schema": {
    "properties": {
      "instanceArn": {
        "type": "string",
        "title": "Instance ARN"
      },
      "instanceId": {
        "type": "string",
        "title": "Instance ID"
      },
      "instanceType": {
        "type": "string",
        "title": "Instance type"
      },
      "availabilityZone": {
        "type": "string",
        "title": "Availability zone"
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

**EC2 Instance mapping configuration (click to expand)**

```
resources:
  - kind: AWS::EC2::Instance
    selector:
      query: 'true'
      includeActions:
        # Optional: Include up to 3 additional actions for more properties
        # Choose based on which properties you need most
        # - GetInstanceStatusAction
    port:
      entity:
        mappings:
          identifier: .Properties.InstanceId
          title: .Properties.InstanceId
          blueprint: '"ec2Instance"'
          properties:
            instanceArn: .Properties.InstanceArn
            instanceId: .Properties.InstanceId
            instanceType: .Properties.InstanceType
            availabilityZone: .Properties.AvailabilityZone
            tags: .Properties.Tags
          relations:
            account: .__ExtraContext.AccountId
```

For more details about EC2 instance properties, refer to the [AWS EC2 API documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html).
