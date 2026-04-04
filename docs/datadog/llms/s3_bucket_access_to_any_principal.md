# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/s3_bucket_access_to_any_principal.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_access_to_any_principal.md

---
title: S3 bucket access to any principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket access to any principal
---

# S3 bucket access to any principal

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7772bb8c-c0f3-42d4-8e4e-f1b8939ad085`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)

### Description{% #description %}

Allowing any principal in an S3 bucket policy grants public (or universally authorized) access to the bucket. This can lead to data exposure, unintended read/write access, and unauthorized modifications. This rule checks `AWS::S3::Bucket` resources that have an associated `AWS::S3::BucketPolicy`. The rule flags bucket policies where `Properties.PolicyDocument.Statement` includes `Effect: "Allow"` and a wildcard principal (for example, `Principal: "*"`, or `Principal: { AWS: "*" }`). Bucket policy statements that explicitly list allowed principals (for example, an AWS account ARN or a specific IAM role) are acceptable. Statements with `Principal` as `*` (or equivalent) will be flagged as insecure.

Secure example with an explicit principal:

```yaml
MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: my-bucket

MyBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: !Ref MyBucket
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Principal:
            AWS: "arn:aws:iam::123456789012:root"
          Action: "s3:GetObject"
          Resource: !Sub "${MyBucket.Arn}/*"
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  Bucket:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy: false
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref Bucket
      PolicyDocument:
        Statement:
        - Effect: Allow
          Principal:
            AWS:
            - arn:aws:iam::111122223333:user/Alice
            - arn:aws:iam::111122223333:user/foo
          Action: s3:GetObject
          Resource: arn:aws:s3:::DOC-EXAMPLE-BUCKET/*
          Condition:
            StringLike:
              'aws:Referer':
                - 'http://www.example.com/*'
                - 'http://example.net/*'
```

```json
{
  "Resources": {
    "Bucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "PublicAccessBlockConfiguration": {
          "BlockPublicAcls": false,
          "BlockPublicPolicy": false,
          "IgnorePublicAcls": true,
          "RestrictPublicBuckets": true
        }
      }
    },
    "BucketPolicy": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "PolicyDocument": {
          "Statement": [
            {
              "Condition": {
                "StringLike": {
                  "aws:Referer": [
                    "http://www.example.com/*",
                    "http://example.net/*"
                  ]
                }
              },
              "Effect": "Allow",
              "Principal": {
                "AWS": [
                  "arn:aws:iam::111122223333:user/Alice",
                  "arn:aws:iam::111122223333:user/foo"
                ]
              },
              "Action": "s3:GetObject",
              "Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
            }
          ]
        },
        "Bucket": "Bucket"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "Bucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "PublicAccessBlockConfiguration": {
          "BlockPublicAcls": false,
          "BlockPublicPolicy": false,
          "IgnorePublicAcls": true,
          "RestrictPublicBuckets": false
        }
      }
    },
    "BucketPolicy": {
      "Properties": {
        "PolicyDocument": {
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": [
                  "*"
                ]
              },
              "Action": "s3:GetObject",
              "Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
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
        },
        "Bucket": "Bucket"
      },
      "Type": "AWS::S3::BucketPolicy"
    },
    "Bucket2": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "PublicAccessBlockConfiguration": {
          "BlockPublicAcls": false,
          "BlockPublicPolicy": false,
          "IgnorePublicAcls": false,
          "RestrictPublicBuckets": true
        }
      }
    },
    "BucketPolicy2": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": "Bucket2",
        "PolicyDocument": {
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": [
                  "*"
                ]
              },
              "Action": "s3:GetObject",
              "Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
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
Resources:
  Bucket:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy: false
        IgnorePublicAcls: true
        RestrictPublicBuckets: false
  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref Bucket
      PolicyDocument:
        Statement:
        - Effect: Allow
          Principal:
            AWS:
            - "*"
          Action: s3:GetObject
          Resource: arn:aws:s3:::DOC-EXAMPLE-BUCKET/*
          Condition:
            StringLike:
              'aws:Referer':
                - 'http://www.example.com/*'
                - 'http://example.net/*'
  Bucket2:
    Type: AWS::S3::Bucket
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: false
        BlockPublicPolicy: false
        IgnorePublicAcls: false
        RestrictPublicBuckets: true
  BucketPolicy2:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref Bucket2
      PolicyDocument:
        Statement:
        - Effect: Allow
          Principal:
            AWS:
            - "*"
          Action: s3:GetObject
          Resource: arn:aws:s3:::DOC-EXAMPLE-BUCKET/*
          Condition:
            StringLike:
              'aws:Referer':
                - 'http://www.example.com/*'
                - 'http://example.net/*'
```
