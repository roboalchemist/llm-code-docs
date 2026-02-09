# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/connection_between_cloudfront_origin_not_encrypted.md

---
title: Connection between CloudFront origin not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Connection between CloudFront origin not
  encrypted
---

# Connection between CloudFront origin not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a5366a50-932f-4085-896b-41402714a388`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)

### Description{% #description %}

CloudFront distributions must require or redirect viewers to HTTPS to prevent plaintext HTTP traffic that can expose sensitive data in transit and enable interception or downgrade attacks. In `AWS::CloudFront::Distribution` resources, set `DistributionConfig.DefaultCacheBehavior.ViewerProtocolPolicy` and each `DistributionConfig.CacheBehaviors[].ViewerProtocolPolicy` to `https-only` or `redirect-to-https`. Resources missing these properties or configured with `allow-all` (which permits HTTP) will be flagged as insecure.

Secure configuration example:

```yaml
MyDistribution:
  Type: AWS::CloudFront::Distribution
  Properties:
    DistributionConfig:
      Enabled: true
      DefaultCacheBehavior:
        TargetOriginId: myOrigin
        ViewerProtocolPolicy: redirect-to-https
      CacheBehaviors:
        - PathPattern: '/images/*'
          TargetOriginId: myOrigin
          ViewerProtocolPolicy: https-only
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
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "cloudfrontdistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "EventType": "viewer-request",
                "LambdaFunctionARN": "examp"
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
          ]
        },
        "Tags": [
          {
            "Key": "name",
            "Value": "example"
          }
        ]
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
    "cloudfrontdistribution_1": {
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
            "ViewerProtocolPolicy": "allow-all",
            "LambdaFunctionAssociations": [
              {
                "EventType": "viewer-request",
                "LambdaFunctionARN": "examp"
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
        ]
      }
    },
    "cloudfrontdistribution_2": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Tags": [
            {
              "Key": "name",
              "Value": "example"
            }
          ],
          "CacheBehaviors": {
            "ViewerProtocolPolicy": "allow-all",
            "LambdaFunctionAssociations": [
              {
                "EventType": "viewer-request",
                "LambdaFunctionARN": "examp"
              }
            ]
          },
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "EventType": "viewer-request",
                "LambdaFunctionARN": "examp"
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
  cloudfrontdistribution_1:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: viewer-request
                LambdaFunctionARN: examp
        DefaultCacheBehavior:
          ViewerProtocolPolicy: allow-all
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
  cloudfrontdistribution_2:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        CacheBehaviors:
          ViewerProtocolPolicy: allow-all
          LambdaFunctionAssociations:
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
```
