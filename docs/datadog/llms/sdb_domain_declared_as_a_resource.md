# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/sdb_domain_declared_as_a_resource.md

---
title: SDB domain declared as a resource
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SDB domain declared as a resource
---

# SDB domain declared as a resource

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `6ea57c8b-f9c0-4ec7-bae3-bd75a9dee27d`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simpledb.html)

### Description{% #description %}

Declaring an AWS SimpleDB domain is discouraged because SimpleDB is a legacy service that lacks many modern security and operational controls. This increases the risk of data exposure and creates maintenance and compliance challenges.

CloudFormation resources with `Type: "AWS::SDB::Domain"` must not be defined. Any resource of that type will be flagged by this rule. Use supported services such as Amazon DynamoDB, Amazon RDS, or Amazon S3 with server-side encryption and appropriate IAM controls as secure alternatives.

Secure alternative (DynamoDB instead of SimpleDB):

```yaml
MyTable:
  Type: AWS::DynamoDB::Table
  Properties:
    TableName: my-table
    AttributeDefinitions:
      - AttributeName: id
        AttributeType: S
    KeySchema:
      - AttributeName: id
        KeyType: HASH
    BillingMode: PAY_PER_REQUEST
    SSESpecification:
      SSEEnabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "SDB Domain declared"
Resources:
  HostedZone:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: "HostedZone"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "SDB Domain declared",
  "Resources": {
    "HostedZone": {
      "Type": "AWS::Route53::HostedZone",
      "Properties": {
        "Name": "HostedZone"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "SDB Domain declared",
  "Resources": {
    "HostedZone": {
      "Type": "AWS::Route53::HostedZone",
      "Properties": {
        "Name": "HostedZone"
      }
    },
    "SBDDomain": {
      "Type": "AWS::SDB::Domain",
      "Properties": {
        "Description": "Some information"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "SDB Domain declared"
Resources:
  HostedZone:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: "HostedZone"
  SBDDomain:
    Type: AWS::SDB::Domain
    Properties:
      Description: "Some information"
```
