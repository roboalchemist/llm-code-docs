# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_static_website_host_enabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_static_website_host_enabled.md

---
title: S3 static website host enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 static website host enabled
---

# S3 static website host enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `90501b1b-cded-4cc1-9e8b-206b85cda317`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html)

### Description{% #description %}

S3 buckets configured for static website hosting expose content via the S3 website endpoint. These endpoints do not support HTTPS, and website hosting is frequently paired with public access. This increases the risk of accidental data exposure, content tampering, and man-in-the-middle attacks.

The `WebsiteConfiguration` property on `AWS::S3::Bucket` resources indicates static website hosting and must not be defined. This rule flags any resource where `Resources.<name>.Properties.WebsiteConfiguration` is present.

If you require public web content, serve it through a CDN (for example, CloudFront) and restrict bucket access via policies and PublicAccessBlock rather than enabling S3 website hosting. Ensure HTTPS is enforced at the CDN. Resources with `WebsiteConfiguration` defined will be flagged so you can remove the property or replace direct website hosting with a secured delivery approach.

Secure example (CloudFormation - no `WebsiteConfiguration` and public access blocked):

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    AccessControl: Private
    PublicAccessBlockConfiguration:
      BlockPublicAcls: true
      IgnorePublicAcls: true
      BlockPublicPolicy: true
      RestrictPublicBuckets: true
    BucketEncryption:
      ServerSideEncryptionConfiguration:
        - ServerSideEncryptionByDefault:
            SSEAlgorithm: AES256
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
    "Bucket2": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "AccessControl": "PublicRead",
        "WebsiteConfiguration": {
          "IndexDocument": "index.html",
          "ErrorDocument": "error.html"
        }
      }
    }
  }
}
```

```yaml
Resources:
  Bucket2:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: PublicRead
      WebsiteConfiguration:
        IndexDocument: index.html
        ErrorDocument: error.html
```
