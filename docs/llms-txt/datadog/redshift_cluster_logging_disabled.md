# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/redshift_cluster_logging_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/redshift_cluster_logging_disabled.md

---
title: Redshift cluster logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Redshift cluster logging disabled
---

# Redshift cluster logging disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3de2d4ff-fe53-4fc9-95d3-2f8a69bf90d6`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-loggingproperties)

### Description{% #description %}

Redshift clusters must have audit and query logging enabled so user actions and query activity are captured for detection, incident response, and compliance. Without logging, malicious activity and data access can go undetected. In AWS CloudFormation, `AWS::Redshift::Cluster` resources must define the `LoggingProperties` property and include a valid `BucketName` (and optional `S3KeyPrefix`) so logs are delivered to an S3 bucket. Resources missing `LoggingProperties` will be flagged. Ensure the destination S3 bucket has appropriate access controls, encryption, and retention or lifecycle policies to protect and retain logs.

```yaml
MyRedshiftCluster:
  Type: AWS::Redshift::Cluster
  Properties:
    ClusterIdentifier: my-cluster
    NodeType: dc2.large
    MasterUsername: masteruser
    MasterUserPassword: ChangeMe123!
    NumberOfNodes: 2
    LoggingProperties:
      BucketName: my-redshift-logs
      S3KeyPrefix: redshift/logs
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: Redshift Stack
Resources:
  RedshiftCluster:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterSubnetGroupName: !Ref RedshiftClusterSubnetGroup
      ClusterType: !If [ SingleNode, single-node, multi-node ]
      NumberOfNodes: !If [ SingleNode, !Ref 'AWS::NoValue', !Ref RedshiftNodeCount ] #'
      DBName: !Sub ${DatabaseName}
      IamRoles:
        - !GetAtt RawDataBucketAccessRole.Arn
      MasterUserPassword: !Ref MasterUserPassword
      MasterUsername: !Ref MasterUsername
      PubliclyAccessible: true
      NodeType: dc1.large
      Port: 5439
      VpcSecurityGroupIds:
        - !Sub ${RedshiftSecurityGroup}
      PreferredMaintenanceWindow: Sun:09:15-Sun:09:45
      KmsKeyId: wewewewewefsa
      LoggingProperties:
        BucketName: "Some bucket name"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "Redshift Stack",
  "Resources": {
    "RedshiftCluster2": {
      "Type": "AWS::Redshift::Cluster",
      "Properties": {
        "IamRoles": [
          "RawDataBucketAccessRole.Arn"
        ],
        "PubliclyAccessible": true,
        "NodeType": "dc1.large",
        "Port": 5439,
        "VpcSecurityGroupIds": [
          "${RedshiftSecurityGroup}"
        ],
        "PreferredMaintenanceWindow": "Sun:09:15-Sun:09:45",
        "ClusterType": [
          "SingleNode",
          "single-node",
          "multi-node"
        ],
        "NumberOfNodes": [
          "SingleNode",
          "AWS::NoValue",
          "RedshiftNodeCount"
        ],
        "DBName": "${DatabaseName}",
        "MasterUserPassword": "MasterUserPassword",
        "MasterUsername": "MasterUsername",
        "KmsKeyId": "wewewewewefsa",
        "ClusterSubnetGroupName": "RedshiftClusterSubnetGroup",
        "LoggingProperties": {
          "BucketName": "Some bucket name"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "Redshift Stack",
  "Resources": {
    "RedshiftCluster4": {
      "Properties": {
        "NodeType": "dc1.large",
        "Port": 5439,
        "VpcSecurityGroupIds": [
          "${RedshiftSecurityGroup}"
        ],
        "ClusterSubnetGroupName": "RedshiftClusterSubnetGroup",
        "ClusterType": [
          "SingleNode",
          "single-node",
          "multi-node"
        ],
        "MasterUserPassword": "MasterUserPassword",
        "MasterUsername": "MasterUsername",
        "PreferredMaintenanceWindow": "Sun:09:15-Sun:09:45",
        "NumberOfNodes": [
          "SingleNode",
          "AWS::NoValue",
          "RedshiftNodeCount"
        ],
        "DBName": "${DatabaseName}",
        "IamRoles": [
          "RawDataBucketAccessRole.Arn"
        ],
        "PubliclyAccessible": true
      },
      "Type": "AWS::Redshift::Cluster"
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: Redshift Stack
Resources:
  RedshiftCluster3:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterSubnetGroupName: !Ref RedshiftClusterSubnetGroup
      ClusterType: !If [ SingleNode, single-node, multi-node ]
      NumberOfNodes: !If [ SingleNode, !Ref 'AWS::NoValue', !Ref RedshiftNodeCount ] #'
      DBName: !Sub ${DatabaseName}
      IamRoles:
        - !GetAtt RawDataBucketAccessRole.Arn
      MasterUserPassword: !Ref MasterUserPassword
      MasterUsername: !Ref MasterUsername
      PubliclyAccessible: true
      NodeType: dc1.large
      Port: 5439
      VpcSecurityGroupIds:
        - !Sub ${RedshiftSecurityGroup}
      PreferredMaintenanceWindow: Sun:09:15-Sun:09:45
```
