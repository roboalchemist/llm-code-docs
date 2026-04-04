# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/dynamodb_table_not_encrypted.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/dynamodb_table_not_encrypted.md

---
title: DynamoDB table not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DynamoDB table not encrypted
---

# DynamoDB table not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4bd21e68-38c1-4d58-acdc-6a14b203237f`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html)

### Description{% #description %}

DynamoDB tables must have server-side encryption enabled to protect data at rest and prevent unauthorized access to table contents, backups, and snapshots. In CloudFormation, the `AWS::DynamoDB::Table` resource must set `Properties.SSESpecification.SSEEnabled` to `true`. Resources that omit `SSESpecification.SSEEnabled` or have `SSEEnabled` set to `false` will be flagged.

Secure configuration example:

```yaml
MyDynamoTable:
  Type: AWS::DynamoDB::Table
  Properties:
    TableName: my-table
    SSESpecification:
      SSEEnabled: true
      SSEType: AES256
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: my-table
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: N
        - AttributeName: name
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
      SSESpecification:
        SSEEnabled: true
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: my-table
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: N
        - AttributeName: name
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
      SSESpecification:
        SSEType: KMS
```

```yaml
Resources:
  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: my-table
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: N
        - AttributeName: name
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
      SSESpecification:
        SSEEnabled: false
```
