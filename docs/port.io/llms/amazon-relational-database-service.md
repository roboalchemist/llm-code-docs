# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-relational-database-service.md

# Amazon Relational Database Service (RDS)

<!-- -->

## AWS::RDS::DBInstance[â](#awsrdsdbinstance "Direct link to AWS::RDS::DBInstance")

The following example demonstrates how to ingest your AWS RDS DB instances to Port.

#### RDS DB Instance supported actions[â](#rds-db-instance-supported-actions "Direct link to RDS DB Instance supported actions")

The table below summarizes the available actions for ingesting Amazon RDS DB Instance resources in Port:

| Action                                                                                                              | Description                                               | Type     | Required AWS Permission   |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------- | ------------------------- |
| [DescribeDBInstancesAction](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) | Discover DB instances and retrieve configuration details. | Default  | `rds:DescribeDBInstances` |
| [ListTagsForResourceAction](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ListTagsForResource.html) | Retrieve tags for each DB instance.                       | Optional | `rds:ListTagsForResource` |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**RDS DB Instance blueprint (click to expand)**

Create in Port

```
{
  "identifier": "rdsDbInstance",
  "title": "RDS DB Instance",
  "icon": "AWS",
  "schema": {
    "properties": {
      "dbInstanceIdentifier": {
        "type": "string",
        "title": "DB Instance Identifier",
        "description": "The unique identifier of the RDS DB instance"
      },
      "dbInstanceArn": {
        "type": "string",
        "title": "ARN",
        "description": "The Amazon Resource Name (ARN) of the DB instance"
      },
      "engine": {
        "type": "string",
        "title": "Engine",
        "description": "The database engine type (e.g., mysql, postgres, oracle-ee)"
      },
      "dbInstanceClass": {
        "type": "string",
        "title": "Instance Class",
        "description": "The compute and memory capacity of the DB instance (e.g., db.t3.micro, db.m4.xlarge)"
      },
      "dbInstanceStatus": {
        "type": "string",
        "title": "Status",
        "description": "The current status of the DB instance",
        "enum": [
          "available",
          "backing-up",
          "creating",
          "deleting",
          "failed",
          "incompatible-credentials",
          "incompatible-network",
          "incompatible-option-group",
          "incompatible-parameters",
          "incompatible-restore",
          "maintenance",
          "modifying",
          "rebooting",
          "renaming",
          "resetting-master-credentials",
          "restore-error",
          "storage-full",
          "storage-optimization",
          "upgrading"
        ]
      },
      "multiAZ": {
        "type": "boolean",
        "title": "Multi-AZ",
        "description": "Whether the DB instance is deployed in multiple Availability Zones"
      },
      "storageEncrypted": {
        "type": "boolean",
        "title": "Storage Encrypted",
        "description": "Whether the DB instance storage is encrypted"
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

**RDS DB Instance mapping configuration (click to expand)**

```
resources:
  - kind: AWS::RDS::DBInstance
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.DBInstanceArn
          title: .Properties.DBInstanceIdentifier
          blueprint: '"rdsDbInstance"'
          properties:
            dbInstanceIdentifier: .Properties.DBInstanceIdentifier
            dbInstanceArn: .Properties.DBInstanceArn
            engine: .Properties.Engine
            dbInstanceClass: .Properties.DBInstanceClass
            dbInstanceStatus: .Properties.DBInstanceStatus
            multiAZ: .Properties.MultiAZ
            storageEncrypted: .Properties.StorageEncrypted
          relations:
            account: .__ExtraContext.AccountId
```

For more details about RDS DB instance properties, refer to the [AWS RDS API documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ProgrammingGuide.html).
