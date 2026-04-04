# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_with_all_permissions.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_with_all_permissions.md

---
title: S3 bucket with all permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket with all permissions
---

# S3 bucket with all permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4ae8af91-5108-42cb-9471-3bdbe596eac9`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)

### Description{% #description %}

S3 bucket policies must not grant `Allow` for all actions to all principals. This creates public full access to the bucket and can result in data exposure, tampering, or deletion.

Check `AWS::S3::BucketPolicy` resources' `Properties.PolicyDocument.Statement` entries and flag any statement where `Effect: "Allow"`, `Action: "*"`, and `Principal: "*"`. Statements matching these conditions will be reported. Restrict principals to specific AWS account IDs/ARNs or services and limit `Action` to the minimum required S3 operations instead of using wildcards.

Secure example limiting access to a specific account and action:

```yaml
MyBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: !Ref MyBucket
    PolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            AWS: arn:aws:iam::123456789012:root
          Action:
            - s3:GetObject
          Resource: !Sub '${MyBucket.Arn}/*'
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
Resources:
  SampleBucketPolicy1:
    Type: 'AWS::S3::BucketPolicy'
    Properties:
      Bucket: !Ref DOC-EXAMPLE-BUCKET
      PolicyDocument:
        Statement:
          - Action:
              - 's3:GetObject'
            Effect: Deny
            Resource: '*'
            Principal: '*'
            Condition:
              StringLike:
                'aws:Referer':
                  - 'http://www.example.com/*'
                  - 'http://example.net/*'
```

```json
{
  "Resources": {
    "SampleBucketPolicy2": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": {
          "Ref": "DOC-EXAMPLE-BUCKET"
        },
        "PolicyDocument": {
          "Statement": [
            {
              "Action": [
                "s3:GetObject"
              ],
              "Effect": "Deny",
              "Resource": "*",
              "Principal": "*",
              "Condition": {
                "StringLike": {
                  "aws:Referer": [
                    "http://www.example.com/*",
                    "http://example.net/*"
                  ]
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "SampleBucketPolicy4": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": {
          "Ref": "DOC-EXAMPLE-BUCKET"
        },
        "PolicyDocument": {
          "Statement": [
            {
              "Action": "*",
              "Effect": "Allow",
              "Resource": "*",
              "Principal": "*",
              "Condition": {
                "StringLike": {
                  "aws:Referer": [
                    "http://www.example.com/*",
                    "http://example.net/*"
                  ]
                }
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
Resources:
  SampleBucketPolicy3:
    Type: 'AWS::S3::BucketPolicy'
    Properties:
      Bucket: !Ref DOC-EXAMPLE-BUCKET
      PolicyDocument:
        Statement:
          - Action: "*"
            Effect: Allow
            Resource: "*"
            Principal: "*"
            Condition:
              StringLike:
                'aws:Referer':
                  - 'http://www.example.com/*'
                  - 'http://example.net/*'
```
