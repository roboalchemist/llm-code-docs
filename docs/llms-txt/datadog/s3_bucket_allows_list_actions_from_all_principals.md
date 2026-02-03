# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/s3_bucket_allows_list_actions_from_all_principals.md

---
title: S3 bucket allows list action from all principals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > S3 bucket allows list action from all
  principals
---

# S3 bucket allows list action from all principals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `faa8fddf-c0aa-4b2d-84ff-e993e233ebe9`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)

### Description{% #description %}

Bucket policies that grant list actions to all principals (`*`) allow anyone to enumerate a bucket's contents and metadata. This can expose sensitive filenames and enable targeted data discovery or exfiltration. For CloudFormation, inspect `AWS::S3::BucketPolicy` resources' `Properties.PolicyDocument.Statement` entries. Ensure no statement has `Effect: "Allow"` with `Principal: "*"` (or including `*`) while `Action` includes list operations such as `s3:ListBucket`. Resources missing the policy document, or containing statements that allow list actions to wildcard principals, will be flagged. Restrict listing permissions to specific AWS account IDs, IAM roles, or ARNs, or remove list permissions for public principals.

Secure example restricting list actions to a specific principal:

```yaml
MyBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: !Ref MyBucket
    PolicyDocument:
      Statement:
        - Effect: Allow
          Principal:
            AWS: arn:aws:iam::123456789012:role/AllowedRole
          Action: s3:ListBucket
          Resource: !Sub arn:aws:s3:::${MyBucket}
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
              - 's3:ListObject'
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
                "s3:ListObject"
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
              "Action": "ListObject",
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
                "ListObject",
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
          - Action: "ListObject"
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
              - "ListObject"
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
