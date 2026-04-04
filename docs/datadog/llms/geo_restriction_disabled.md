# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/geo_restriction_disabled.md

---
title: Geo restriction disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Geo restriction disabled
---

# Geo restriction disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7f8843f0-9ea5-42b4-a02b-753055113195`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html)

### Description{% #description %}

Geo restriction must be enabled to limit which geographic locations can access your content. Without it, content can be served globally, increasing attack surface and risking data residency or compliance violations.

In CloudFormation, the `AWS::CloudFront::Distribution` resource's `Properties.DistributionConfig.Restrictions.GeoRestriction.RestrictionType` must be set to either `whitelist` or `blacklist`. Resources that omit this property or set it to `none` (or any value not containing `whitelist` or `blacklist`) will be flagged. When using `whitelist` or `blacklist`, populate the `Locations` array with the appropriate ISO 3166-1 alpha-2 country codes.

Secure configuration example:

```yaml
MyDistribution:
  Type: AWS::CloudFront::Distribution
  Properties:
    DistributionConfig:
      Enabled: true
      Restrictions:
        GeoRestriction:
          RestrictionType: whitelist
          Locations:
            - US
            - CA
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Logging:
          IncludeCookies: 'false'
          Bucket: mylogs.s3.amazonaws.com
          Prefix: myprefix
        Restrictions:
          GeoRestriction:
            RestrictionType: whitelist
            Locations:
            - AQ
            - CV
        ViewerCertificate:
          CloudFrontDefaultCertificate: 'true'
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Logging": {
            "IncludeCookies": "false",
            "Bucket": "mylogs.s3.amazonaws.com",
            "Prefix": "myprefix"
          },
          "Restrictions": {
            "GeoRestriction": {
              "RestrictionType": "whitelist",
              "Locations": [
                "AQ",
                "CV"
              ]
            }
          },
          "ViewerCertificate": {
            "CloudFrontDefaultCertificate": "true"
          }
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myDistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Logging": {
            "IncludeCookies": "false",
            "Bucket": "mylogs.s3.amazonaws.com",
            "Prefix": "myprefix"
          },
          "Restrictions": {
            "GeoRestriction": {
              "RestrictionType": "none"
            }
          },
          "ViewerCertificate": {
            "CloudFrontDefaultCertificate": "true"
          }
        }
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Logging:
          IncludeCookies: 'false'
          Bucket: mylogs.s3.amazonaws.com
          Prefix: myprefix
        Restrictions:
          GeoRestriction:
            RestrictionType: none
        ViewerCertificate:
          CloudFrontDefaultCertificate: 'true'
```
