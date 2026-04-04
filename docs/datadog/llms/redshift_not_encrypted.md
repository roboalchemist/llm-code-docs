# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/redshift_not_encrypted.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/redshift_not_encrypted.md

---
title: Redshift not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Redshift not encrypted
---

# Redshift not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3b316b05-564c-44a7-9c3f-405bb95e211e`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html)

### Description{% #description %}

Redshift clusters must have storage encryption enabled to protect sensitive data at rest and to ensure snapshots and automated backups are encrypted and not exposed if storage media is compromised. In AWS CloudFormation, the `Encrypted` property on `AWS::Redshift::Cluster` resources must be defined and set to `true`. Resources missing this property or with `Encrypted` set to `false` will be flagged. If `Encrypted` is omitted, the default behavior is `false`. For key management, set `KmsKeyId` to a customer-managed KMS key ARN or alias when you require control over encryption keys. If omitted, AWS will use the AWS-managed key.

Secure configuration example:

```yaml
MyRedshiftCluster:
  Type: AWS::Redshift::Cluster
  Properties:
    ClusterType: single-node
    NodeType: dc2.large
    DBName: mydb
    MasterUsername: masteruser
    MasterUserPassword: ReplaceWithSecureValue
    Encrypted: true
    KmsKeyId: arn:aws:kms:us-east-1:123456789012:key/abcd-1234-efgh-5678
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-11
Description: Redshift Stack2
Resources:
  RedshiftCluster2:
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
      Encrypted: true
  DataBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub ${DataBucketName}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-11T00:00:00Z",
  "Description": "Redshift Stack2",
  "Resources": {
    "RedshiftCluster2": {
      "Properties": {
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
        "IamRoles": [
          "RawDataBucketAccessRole.Arn"
        ],
        "NodeType": "dc1.large",
        "PreferredMaintenanceWindow": "Sun:09:15-Sun:09:45",
        "Encrypted": true,
        "ClusterSubnetGroupName": "RedshiftClusterSubnetGroup",
        "MasterUsername": "MasterUsername",
        "PubliclyAccessible": true,
        "Port": 5439,
        "VpcSecurityGroupIds": [
          "${RedshiftSecurityGroup}"
        ],
        "MasterUserPassword": "MasterUserPassword"
      },
      "Type": "AWS::Redshift::Cluster"
    },
    "DataBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "${DataBucketName}"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-11
Description: Redshift Stack2
Resources:
  RedshiftCluster2:
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
      Encrypted: false
  DataBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub ${DataBucketName}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "Redshift Stack",
  "Resources": {
    "RedshiftCluster": {
      "Type": "AWS::Redshift::Cluster",
      "Properties": {
        "IamRoles": [
          "RawDataBucketAccessRole.Arn"
        ],
        "MasterUserPassword": "MasterUserPassword",
        "PubliclyAccessible": true,
        "NodeType": "dc1.large",
        "VpcSecurityGroupIds": [
          "${RedshiftSecurityGroup}"
        ],
        "PreferredMaintenanceWindow": "Sun:09:15-Sun:09:45",
        "ClusterSubnetGroupName": "RedshiftClusterSubnetGroup",
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
        "MasterUsername": "MasterUsername",
        "Port": 5439
      }
    },
    "DataBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "${DataBucketName}"
      }
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-11T00:00:00Z",
  "Description": "Redshift Stack2",
  "Resources": {
    "RedshiftCluster2": {
      "Type": "AWS::Redshift::Cluster",
      "Properties": {
        "MasterUserPassword": "MasterUserPassword",
        "PubliclyAccessible": true,
        "NodeType": "dc1.large",
        "Port": 5439,
        "VpcSecurityGroupIds": [
          "${RedshiftSecurityGroup}"
        ],
        "PreferredMaintenanceWindow": "Sun:09:15-Sun:09:45",
        "ClusterSubnetGroupName": "RedshiftClusterSubnetGroup",
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
        "IamRoles": [
          "RawDataBucketAccessRole.Arn"
        ],
        "MasterUsername": "MasterUsername",
        "Encrypted": false
      }
    },
    "DataBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "${DataBucketName}"
      }
    }
  }
}
```
