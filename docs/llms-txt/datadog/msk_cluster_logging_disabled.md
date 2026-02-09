# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/msk_cluster_logging_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/msk_cluster_logging_disabled.md

---
title: MSK cluster logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > MSK cluster logging disabled
---

# MSK cluster logging disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fc7c2c15-f5d0-4b80-adb2-c89019f8f62b`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html)

### Description{% #description %}

MSK clusters must have broker logging enabled to provide audit and operational visibility. Without broker logs, you may be unable to detect or investigate security incidents, troubleshoot cluster issues, or meet logging retention and compliance requirements. In AWS CloudFormation, the `AWS::MSK::Cluster` resource must include the `LoggingInfo` property with `BrokerLogs` configured to specify at least one destination (`CloudWatchLogs`, `Firehose`, or `S3`). The selected destination entry must have `Enabled` set to `true`. Resources missing `LoggingInfo`, missing all three broker log destinations, or where none of the `BrokerLogs` entries have `Enabled` set to `true` will be flagged.

Secure configuration example (CloudFormation YAML):

```yaml
MyMSKCluster:
  Type: AWS::MSK::Cluster
  Properties:
    ClusterName: my-msk-cluster
    KafkaVersion: "2.8.1"
    NumberOfBrokerNodes: 3
    BrokerNodeGroupInfo:
      InstanceType: kafka.m5.large
      ClientSubnets: [subnet-12345, subnet-67890]
      SecurityGroups: [sg-012345]
    LoggingInfo:
      BrokerLogs:
        CloudWatchLogs:
          Enabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: MSK Cluster with required properties.
Resources:
  TestCluster:
    Type: 'AWS::MSK::Cluster'
    Properties:
      ClusterName: ClusterWithRequiredProperties
      KafkaVersion: 2.2.1
      LoggingInfo:
         BrokerLogs:
          CloudWatchLogs:
            Enabled: true
            LogGroup: aws_cloudwatch_log_group.test.name
      NumberOfBrokerNodes: 3
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - ReplaceWithSubnetId1
          - ReplaceWithSubnetId2
          - ReplaceWithSubnetId3
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "MSK Cluster with required properties.",
  "Resources": {
    "TestCluster4": {
      "Type": "AWS::MSK::Cluster",
      "Properties": {
        "ClusterName": "ClusterWithRequiredProperties",
        "KafkaVersion": "2.2.1",
        "LoggingInfo": {
          "BrokerLogs": {
            "CloudWatchLogs": {
              "Enabled": false,
              "LogGroup": "aws_cloudwatch_log_group.test.name"
            },
            "S3": {
              "Enabled": true,
              "LogGroup": "s3.test.name"
            }
          }
        },
        "NumberOfBrokerNodes": 3,
        "BrokerNodeGroupInfo": {
          "InstanceType": "kafka.m5.large",
          "ClientSubnets": [
            "ReplaceWithSubnetId1",
            "ReplaceWithSubnetId2",
            "ReplaceWithSubnetId3"
          ]
        }
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: MSK Cluster with required properties.
Resources:
  TestCluster2:
    Type: 'AWS::MSK::Cluster'
    Properties:
      ClusterName: ClusterWithRequiredProperties
      KafkaVersion: 2.2.1
      LoggingInfo:
         BrokerLogs:
          CloudWatchLogs:
            Enabled: false
            LogGroup: aws_cloudwatch_log_group.test.name
          S3:
            Enabled: true
            LogGroup: s3.test.name
      NumberOfBrokerNodes: 3
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - ReplaceWithSubnetId1
          - ReplaceWithSubnetId2
          - ReplaceWithSubnetId3
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: MSK Cluster with required properties.
Resources:
  TestCluster6:
    Type: 'AWS::MSK::Cluster'
    Properties:
      ClusterName: ClusterWithRequiredProperties
      KafkaVersion: 2.2.1
      LoggingInfo:
         BrokerLogs:
          CloudWatchLogs:
            Enabled: false
            LogGroup: aws_cloudwatch_log_group.test.name
          Firehose:
            Enabled: false
            LogGroup: firehose.test.name
          S3:
            Enabled: false
            LogGroup: s3.test.name
      NumberOfBrokerNodes: 3
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - ReplaceWithSubnetId1
          - ReplaceWithSubnetId2
          - ReplaceWithSubnetId3
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: MSK Cluster with required properties.
Resources:
  TestCluster7:
    Type: 'AWS::MSK::Cluster'
    Properties:
      ClusterName: ClusterWithRequiredProperties
      KafkaVersion: 2.2.1
      LoggingInfo:
         BrokerLogs:
          CloudWatchLogs:
            Enabled: false
            LogGroup: aws_cloudwatch_log_group.test.name
      NumberOfBrokerNodes: 3
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - ReplaceWithSubnetId1
          - ReplaceWithSubnetId2
          - ReplaceWithSubnetId3
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "MSK Cluster with required properties.",
  "Resources": {
    "TestCluster9": {
      "Type": "AWS::MSK::Cluster",
      "Properties": {
        "ClusterName": "ClusterWithRequiredProperties",
        "KafkaVersion": "2.2.1",
        "LoggingInfo": {
          "BrokerLogs": {
            "CloudWatchLogs": {
              "Enabled": false,
              "LogGroup": "aws_cloudwatch_log_group.test.name"
            },
            "Firehose": {
              "Enabled": false,
              "LogGroup": "firehose.test.name"
            },
            "S3": {
              "Enabled": false,
              "LogGroup": "s3.test.name"
            }
          }
        },
        "NumberOfBrokerNodes": 3,
        "BrokerNodeGroupInfo": {
          "InstanceType": "kafka.m5.large",
          "ClientSubnets": [
            "ReplaceWithSubnetId1",
            "ReplaceWithSubnetId2",
            "ReplaceWithSubnetId3"
          ]
        }
      }
    }
  }
}
```
