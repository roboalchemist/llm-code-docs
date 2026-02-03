# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_allows_restore_actions_from_all_principals.md

---
title: S3 bucket allows restore actions from all principals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket allows restore actions from all
  principals
---

# S3 bucket allows restore actions from all principals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `456b00a3-1072-4149-9740-6b8bb60251b0`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)

### Description{% #description %}

S3 bucket policies must not allow restore actions to all principals (`*`). A public `Allow` on restore operations lets anyone trigger restores of archived objects, risking exposure of sensitive archived data and unexpected costs. Check `AWS::S3::BucketPolicy` resources' `Properties.PolicyDocument.Statement` entries and flag any statement where `Effect: "Allow"`, `Principal: "*"`, and `Action` includes restore operations such as `s3:RestoreObject`.

To remediate, restrict `Principal` to explicit AWS principals (account IDs, ARNs, or specific roles), or remove restore actions from publicly allowed statements.

Secure configuration example restricting restore actions to a specific role:

```yaml
MyBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: my-bucket
    PolicyDocument:
      Statement:
        - Sid: AllowRestoreForRestoreRole
          Effect: Allow
          Principal:
            AWS: arn:aws:iam::123456789012:role/RestoreRole
          Action:
            - s3:RestoreObject
          Resource: arn:aws:s3:::my-bucket/* 
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
              - 's3:RestoreObject'
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
                "s3:RestoreObject"
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
    "SampleBucketPolicy5": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": {
          "Ref": "DOC-EXAMPLE-BUCKET"
        },
        "PolicyDocument": {
          "Statement": [
            {
              "Action": "RestoreObject",
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
    },
    "SampleBucketPolicy6": {
      "Type": "AWS::S3::BucketPolicy",
      "Properties": {
        "Bucket": {
          "Ref": "DOC-EXAMPLE-BUCKET"
        },
        "PolicyDocument": {
          "Statement": [
            {
              "Action": [
                "RestoreObject",
                "GetObject"
              ],
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
          - Action: "RestoreObject"
            Effect: Allow
            Resource: "*"
            Principal: "*"
            Condition:
              StringLike:
                'aws:Referer':
                  - 'http://www.example.com/*'
                  - 'http://example.net/*'
  SampleBucketPolicy4:
    Type: 'AWS::S3::BucketPolicy'
    Properties:
      Bucket: !Ref DOC-EXAMPLE-BUCKET
      PolicyDocument:
        Statement:
          - Action:
              - "RestoreObject"
              - "GetObject"
            Effect: Allow
            Resource: "*"
            Principal: "*"
            Condition:
              StringLike:
                'aws:Referer':
                  - 'http://www.example.com/*'
                  - 'http://example.net/*'
```
