# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudfront_without_minimum_protocol_tls_1.2.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/cloudfront_without_minimum_protocol_tls_1.2.md

---
title: CloudFront without minimum protocol TLS 1.2
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudFront without minimum protocol TLS 1.2
---

# CloudFront without minimum protocol TLS 1.2

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dc17ee4b-ddf2-4e23-96e8-7a36abad1303`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)

### Description{% #description %}

CloudFront distributions must define a `ViewerCertificate` and enforce a minimum TLS version of 1.2 to prevent the use of weak SSL/TLS protocols that can enable downgrade attacks and interception of client connections.

For `AWS::CloudFront::Distribution` resources, ensure `Properties.DistributionConfig.ViewerCertificate` is present and its `MinimumProtocolVersion` is set to a TLS 1.2 family value (for example, `TLSv1.2_2018` or `TLSv1.2_2019`). Also include an appropriate certificate reference (such as `ACMCertificateArn`) and `SslSupportMethod`.

This check only applies to distributions that are enabled (`DistributionConfig.Enabled` not set to `false`). Resources missing `ViewerCertificate` or with `MinimumProtocolVersion` lower than TLS 1.2 will be flagged.

Secure CloudFormation example:

```yaml
MyDistribution:
  Type: AWS::CloudFront::Distribution
  Properties:
    DistributionConfig:
      Enabled: true
      ViewerCertificate:
        ACMCertificateArn: arn:aws:acm:us-east-1:123456789012:certificate/abcdef01-2345-6789-abcd-ef0123456789
        SslSupportMethod: sni-only
        MinimumProtocolVersion: TLSv1.2_2019
      Origins:
        - Id: myOrigin
          DomainName: example.com
          CustomOriginConfig:
            HTTPPort: 80
            HTTPSPort: 443
            OriginProtocolPolicy: https-only
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  cloudfrontdistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: string-value
                LambdaFunctionARN: string-value
        DefaultCacheBehavior:
          LambdaFunctionAssociations:
            - EventType: string-value
              LambdaFunctionARN: string-value
        IPV6Enabled: boolean-value
        Origins:
          - CustomOriginConfig:
              OriginKeepaliveTimeout: integer-value
              OriginReadTimeout: integer-value
        ViewerCertificate:
            AcmCertificateArn: String
            CloudFrontDefaultCertificate: true
            IamCertificateId: String
            MinimumProtocolVersion: "TLSv1.2_2018"
            SslSupportMethod: String
      Tags:
        - Key: string-value
          Value: string-value
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "cloudfrontdistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "CacheBehaviors": [
            {
              "LambdaFunctionAssociations": [
                {
                  "EventType": "string-value",
                  "LambdaFunctionARN": "string-value"
                }
              ]
            }
          ],
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "EventType": "string-value",
                "LambdaFunctionARN": "string-value"
              }
            ]
          },
          "IPV6Enabled": "boolean-value",
          "Origins": [
            {
              "CustomOriginConfig": {
                "OriginKeepaliveTimeout": "integer-value",
                "OriginReadTimeout": "integer-value"
              }
            }
          ],
          "ViewerCertificate": {
            "IamCertificateId": "String",
            "MinimumProtocolVersion": "TLSv1.2_2018",
            "SslSupportMethod": "String",
            "AcmCertificateArn": "String",
            "CloudFrontDefaultCertificate": true
          }
        },
        "Tags": [
          {
            "Key": "string-value",
            "Value": "string-value"
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
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "cloudfrontdistribution": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Enabled": true,
          "ViewerCertificate": {
            "IamCertificateId": "String",
            "MinimumProtocolVersion": "TLSv1.1_2016",
            "SslSupportMethod": "String",
            "AcmCertificateArn": "String",
            "CloudFrontDefaultCertificate": true
          },
          "CacheBehaviors": [
            {
              "LambdaFunctionAssociations": [
                {
                  "EventType": "string-value",
                  "LambdaFunctionARN": "string-value"
                }
              ]
            }
          ],
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "EventType": "string-value",
                "LambdaFunctionARN": "string-value"
              }
            ]
          },
          "IPV6Enabled": "boolean-value",
          "Origins": [
            {
              "CustomOriginConfig": {
                "OriginKeepaliveTimeout": "integer-value",
                "OriginReadTimeout": "integer-value"
              }
            }
          ]
        },
        "Tags": [
          {
            "Key": "string-value",
            "Value": "string-value"
          }
        ]
      }
    },
    "cloudfrontdistribution2": {
      "Type": "AWS::CloudFront::Distribution",
      "Properties": {
        "DistributionConfig": {
          "Enabled": true,
          "Origins": [
            {
              "CustomOriginConfig": {
                "OriginKeepaliveTimeout": "integer-value",
                "OriginReadTimeout": "integer-value"
              }
            }
          ],
          "CacheBehaviors": [
            {
              "LambdaFunctionAssociations": [
                {
                  "EventType": "string-value",
                  "LambdaFunctionARN": "string-value"
                }
              ]
            }
          ],
          "DefaultCacheBehavior": {
            "LambdaFunctionAssociations": [
              {
                "LambdaFunctionARN": "string-value",
                "EventType": "string-value"
              }
            ]
          },
          "IPV6Enabled": "boolean-value"
        },
        "Tags": [
          {
            "Key": "string-value",
            "Value": "string-value"
          }
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  cloudfrontdistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: string-value
                LambdaFunctionARN: string-value
        DefaultCacheBehavior:
          LambdaFunctionAssociations:
            - EventType: string-value
              LambdaFunctionARN: string-value
        IPV6Enabled: boolean-value
        Origins:
          - CustomOriginConfig:
              OriginKeepaliveTimeout: integer-value
              OriginReadTimeout: integer-value
        ViewerCertificate:
            AcmCertificateArn: String
            CloudFrontDefaultCertificate: true
            IamCertificateId: String
            MinimumProtocolVersion: "TLSv1.1_2016"
            SslSupportMethod: String
      Tags:
        - Key: string-value
          Value: string-value
  cloudfrontdistribution2:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        CacheBehaviors:
          - LambdaFunctionAssociations:
              - EventType: string-value
                LambdaFunctionARN: string-value
        DefaultCacheBehavior:
          LambdaFunctionAssociations:
            - EventType: string-value
              LambdaFunctionARN: string-value
        IPV6Enabled: boolean-value
        Origins:
          - CustomOriginConfig:
              OriginKeepaliveTimeout: integer-value
              OriginReadTimeout: integer-value
      Tags:
        - Key: string-value
          Value: string-value
```
