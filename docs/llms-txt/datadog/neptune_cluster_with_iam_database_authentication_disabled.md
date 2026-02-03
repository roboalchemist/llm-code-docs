# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/neptune_cluster_with_iam_database_authentication_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/neptune_cluster_with_iam_database_authentication_disabled.md

---
title: Neptune cluster with IAM database authentication disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Neptune cluster with IAM database
  authentication disabled
---

# Neptune cluster with IAM database authentication disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a3aa0087-8228-4e7e-b202-dc9036972d02`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-iamauthenabled)

### Description{% #description %}

Neptune DB clusters must have IAM database authentication enabled to centralize credential management and enable IAM-based access control and auditing. This reduces reliance on static database passwords that can be leaked or become stale. In AWS CloudFormation, the `AWS::Neptune::DBCluster` resource must include the `IamAuthEnabled` property set to `true`. Resources that omit this property or set `IamAuthEnabled` to `false` will be flagged.

Secure configuration example:

```yaml
MyNeptuneCluster:
  Type: AWS::Neptune::DBCluster
  Properties:
    DBClusterIdentifier: my-neptune-cluster
    IamAuthEnabled: true
    # other required properties...
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
  NeptuneDBCluster3:
    Type: AWS::Neptune::DBCluster
    Properties:
      IamAuthEnabled: true
      StorageEncrypted: true
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "A sample template",
  "Resources": {
    "NeptuneDBCluster3": {
      "Type": "AWS::Neptune::DBCluster",
      "Properties": {
        "IamAuthEnabled": true,
        "StorageEncrypted": true
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "A sample template",
  "Resources": {
    "NeptuneDBCluster": {
      "Type": "AWS::Neptune::DBCluster",
      "Properties": {
        "IamAuthEnabled": false,
        "StorageEncrypted": true
      }
    },
    "NeptuneDBCluster2": {
      "Type": "AWS::Neptune::DBCluster",
      "Properties": {
        "IamAuthEnabled": false,
        "StorageEncrypted": true
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      IamAuthEnabled: false
      StorageEncrypted: true
  NeptuneDBCluster2:
    Type: AWS::Neptune::DBCluster
    Properties:
      IamAuthEnabled: false
      StorageEncrypted: true
```
