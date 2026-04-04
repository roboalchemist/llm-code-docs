# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/vulnerable_default_ssl_certificate.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/vulnerable_default_ssl_certificate.md

---
title: Vulnerable default SSL certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Vulnerable default SSL certificate
---

# Vulnerable default SSL certificate

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b4d9c12b-bfba-4aeb-9cb8-2358546d8041`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)

### Description{% #description %}

CloudFront distributions should use a custom SSL/TLS certificate for custom domain names so you control certificate trust and can enforce strong TLS protocol and SNI settings.

For `AWS::CloudFront::Distribution` resources, `ViewerCertificate.CloudFrontDefaultCertificate` must be omitted or set to `false`. When a custom certificate is used via `ViewerCertificate.AcmCertificateArn` or `ViewerCertificate.IamCertificateId`, the `ViewerCertificate.SslSupportMethod` and `ViewerCertificate.MinimumProtocolVersion` properties must be defined. Resources with `CloudFrontDefaultCertificate` set to `true` will be flagged. Distributions that specify an ACM or IAM certificate but omit `SslSupportMethod` or `MinimumProtocolVersion` will also be flagged as misconfigured.

Secure configuration example:

```yaml
MyDistribution:
  Type: AWS::CloudFront::Distribution
  Properties:
    DistributionConfig:
      ViewerCertificate:
        AcmCertificateArn: arn:aws:acm:us-east-1:123456789012:certificate/abcdefg-1234-5678-90ab-cdef12345678
        SslSupportMethod: sni-only
        MinimumProtocolVersion: TLSv1.2_2019
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myDistribution:
    Type: 'AWS::CloudFront::Distribution'
    Properties:
      DistributionConfig:
        ViewerCertificate:
          AcmCertificateArn: arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
          MinimumProtocolVersion: TLS1.2_2019
          SslSupportMethod: sni_only
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Enabled": "true"
        }
      }
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "ViewerCertificate": {
            "AcmCertificateArn": "some arn",
            "MinimumProtocolVersion": "TLS1.2_2019",
            "SslSupportMethod": "sni_only"
          }
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        ViewerCertificate:
          AcmCertificateArn: arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        ViewerCertificate:
          CloudfrontDefaultCertificate: true
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "ViewerCertificate": {
            "AcmCertificateArn": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
          }
        }
      }
    }
  }
}
```
