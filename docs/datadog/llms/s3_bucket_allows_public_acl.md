# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_allows_public_acl.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_allows_public_acl.md

---
title: S3 bucket allows public ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket allows public ACL
---

# S3 bucket allows public ACL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `48f100d9-f499-4c6d-b2b8-deafe47ffb26`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html)

### Description{% #description %}

S3 buckets should block public ACLs to prevent objects from being granted public access via ACLs. Public ACLs can lead to unintended data exposure. For `AWS::S3::Bucket` resources, `Properties.PublicAccessBlockConfiguration.BlockPublicAcls` must be set to `true`. Resources missing `PublicAccessBlockConfiguration`, or with `BlockPublicAcls: false`, will be flagged. Consider also enabling other `PublicAccessBlockConfiguration` flags (for example, `IgnorePublicAcls`, `BlockPublicPolicy`, and `RestrictPublicBuckets`) for broader protection.

Secure configuration example:

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: my-bucket
    PublicAccessBlockConfiguration:
      BlockPublicAcls: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  Bucket1:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls       : true
        BlockPublicPolicy     : true
        IgnorePublicAcls      : true
        RestrictPublicBuckets : true
```

```json
{
  "Resources": {
    "Bucket1": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "PublicAccessBlockConfiguration": {
          "BlockPublicAcls": true,
          "BlockPublicPolicy": true,
          "IgnorePublicAcls": true,
          "RestrictPublicBuckets": true
        },
        "AccessControl": "Private"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "Bucket1": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "PublicAccessBlockConfiguration": {
          "BlockPublicAcls": false,
          "BlockPublicPolicy": true,
          "IgnorePublicAcls": true,
          "RestrictPublicBuckets": true
        },
        "AccessControl": "Private"
      }
    }
  }
}
```

```yaml
Resources:
  Bucket11:
    Type: AWS::S3::Bucket
    Properties:
---
Resources:
  Bucket12:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicPolicy     : true
        IgnorePublicAcls      : true
        RestrictPublicBuckets : true
---
Resources:
  Bucket13:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy     : true
        IgnorePublicAcls      : true
        RestrictPublicBuckets : true
```
