# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/dynamodb_table_point_in_time_recovery_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/dynamodb_table_point_in_time_recovery_disabled.md

---
title: DynamoDB table point-in-time recovery disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DynamoDB table point-in-time recovery disabled
---

# DynamoDB table point-in-time recovery disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `0f04217d-488f-4e7a-bec8-f16159686cd6`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html)

### Description{% #description %}

DynamoDB tables must have point-in-time recovery (PITR) enabled to allow restoration to a prior consistent state after accidental deletes, overwrites, or data corruption. Without PITR, you cannot restore to recent points in time, increasing the risk of permanent data loss and extended recovery time. Check `AWS::DynamoDB::Table` resources and ensure the `Properties.PointInTimeRecoverySpecification.PointInTimeRecoveryEnabled` property is defined and set to `true`. Resources missing `PointInTimeRecoverySpecification`, missing the `PointInTimeRecoveryEnabled` field, or with `PointInTimeRecoveryEnabled` set to `false` will be flagged.

Secure configuration example:

```yaml
MyDynamoTable:
  Type: AWS::DynamoDB::Table
  Properties:
    TableName: MyTable
    AttributeDefinitions:
      - AttributeName: id
        AttributeType: S
    KeySchema:
      - AttributeName: id
        KeyType: HASH
    BillingMode: PAY_PER_REQUEST
    PointInTimeRecoverySpecification:
      PointInTimeRecoveryEnabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
```

```json
{
  "Resources": {
    "DynamoDBOnDemandTable1": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "BillingMode": "PAY_PER_REQUEST",
        "PointInTimeRecoverySpecification" : {
          "PointInTimeRecoveryEnabled" : true
        }
      }
    },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Sample CloudFormation template for DynamoDB with customer managed CMK"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: my-table
```

```json
{
  "Resources": {
    "DynamoDBOnDemandTable1": {
      "Type": "AWS::DynamoDB::Table",
      "Properties": {
        "BillingMode": "PAY_PER_REQUEST",
        "PointInTimeRecoverySpecification" : {
          "PointInTimeRecoveryEnabled" : false
        }
      }
    },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Sample CloudFormation template for DynamoDB with customer managed CMK"
  }
}
```

```yaml
Resources:
  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      PointInTimeRecoverySpecification: {}
```
