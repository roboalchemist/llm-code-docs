# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/secure_ciphers_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/secure_ciphers_disabled.md

---
title: Secure ciphers disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Secure ciphers disabled
---

# Secure ciphers disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `be96849c-3df6-49c2-bc16-778a7be2519c`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html)

### Description{% #description %}

CloudFront distributions that use a custom TLS certificate should enforce a modern TLS protocol version. This prevents negotiation of weak or deprecated protocols that enable downgrade attacks or compromise confidentiality and integrity.

For `AWS::CloudFront::Distribution` resources where `ViewerCertificate.CloudFrontDefaultCertificate` is `false`, `ViewerCertificate.MinimumProtocolVersion` must be set to `TLSv1.1` or `TLSv1.2`. Resources missing `MinimumProtocolVersion`, or configured with any other value, will be flagged. Distributions using the default CloudFront certificate (`CloudFrontDefaultCertificate: true`) are not evaluated by this rule.

Secure configuration example:

```yaml
MyDistribution:
  Type: AWS::CloudFront::Distribution
  Properties:
    DistributionConfig:
      Enabled: true
      Origins: []
      DefaultCacheBehavior:
        TargetOriginId: origin1
        ViewerProtocolPolicy: allow-all
    ViewerCertificate:
      CloudFrontDefaultCertificate: false
      MinimumProtocolVersion: TLSv1.2
      AcmCertificateArn: arn:aws:acm:region:account:certificate/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  cloudfrontdistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: viewer-request
                LambdaFunctionARN: examp
        DefaultCacheBehavior:
          LambdaFunctionAssociations:
            - EventType: viewer-request
              LambdaFunctionARN: examp
        IPV6Enabled: true
        Origins:
          - CustomOriginConfig:
              OriginKeepaliveTimeout: 60
              OriginReadTimeout: 30
      Tags:
        - Key: name
          Value: example
      ViewerCertificate:
        CloudFrontDefaultCertificate: true
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "cloudfrontdistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "CacheBehaviors": [
            {
              "LambdaFunctionAssociations": [
                {
                  "EventType": "viewer-request",
                  "LambdaFunctionARN": "examp"
                }
              ]
            }
          ],
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "LambdaFunctionARN": "examp",
                "EventType": "viewer-request"
              }
            ]
          },
          "IPV6Enabled": true,
          "Origins": [
            {
              "CustomOriginConfig": {
                "OriginKeepaliveTimeout": 60,
                "OriginReadTimeout": 30
              }
            }
          ]
        },
        "Tags": [
          {
            "Key": "name",
            "Value": "example"
          }
        ],
        "ViewerCertificate": {
          "CloudFrontDefaultCertificate": true
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
    "cloudfrontdistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Origins": [
            {
              "CustomOriginConfig": {
                "OriginKeepaliveTimeout": 60,
                "OriginReadTimeout": 30
              }
            }
          ],
          "CacheBehaviors": [
            {
              "LambdaFunctionAssociations": [
                {
                  "EventType": "viewer-request",
                  "LambdaFunctionARN": "examp"
                }
              ]
            }
          ],
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "EventType": "viewer-request",
                "LambdaFunctionARN": "examp"
              }
            ]
          },
          "IPV6Enabled": true
        },
        "Tags": [
          {
            "Key": "name",
            "Value": "example"
          }
        ],
        "ViewerCertificate": {
          "CloudFrontDefaultCertificate": false,
          "MinimumProtocolVersion": "SSLv3"
        }
      }
    }
  }
}
```

```yaml
#this is a problematic code where the query should report a result(s)
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  cloudfrontdistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: viewer-request
                LambdaFunctionARN: examp
        DefaultCacheBehavior:
          LambdaFunctionAssociations:
            - EventType: viewer-request
              LambdaFunctionARN: examp
        IPV6Enabled: true
        Origins:
          - CustomOriginConfig:
              OriginKeepaliveTimeout: 60
              OriginReadTimeout: 30
      Tags:
        - Key: name
          Value: example
      ViewerCertificate:
        CloudFrontDefaultCertificate: false
        MinimumProtocolVersion: SSLv3
```
