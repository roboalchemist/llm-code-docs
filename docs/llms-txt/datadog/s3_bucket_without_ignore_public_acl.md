# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_without_ignore_public_acl.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_without_ignore_public_acl.md

---
title: S3 bucket without ignore public ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket without ignore public ACL
---

# S3 bucket without ignore public ACL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `6c8d51af-218d-4bfb-94a9-94eabaa0703a`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html)

### Description{% #description %}

S3 buckets should ignore public ACLs to prevent object or bucket-level ACLs from granting unintended public access. Public ACLs can lead to accidental data exposure.

In CloudFormation, the `AWS::S3::Bucket` resource must include `PublicAccessBlockConfiguration.IgnorePublicAcls` and it must be set to `true`. Resources missing `PublicAccessBlockConfiguration`, missing the `IgnorePublicAcls` property, or with `IgnorePublicAcls: false` will be flagged.

Secure configuration example:

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: my-bucket
    PublicAccessBlockConfiguration:
      IgnorePublicAcls: true
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
          "IgnorePublicAcls": false,
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
        RestrictPublicBuckets : true
---
Resources:
  Bucket13:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy     : true
        IgnorePublicAcls      : false
        RestrictPublicBuckets : true                
```
