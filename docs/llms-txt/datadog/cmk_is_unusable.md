# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cmk_is_unusable.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/cmk_is_unusable.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/cmk_is_unusable.md

---
title: CMK is unusable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CMK is unusable
---

# CMK is unusable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2844c749-bd78-4cd1-90e8-b179df827602`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html)

### Description{% #description %}

AWS KMS Customer Master Keys (CMKs) used by your stack must be usable so encrypted data can be decrypted and cryptographic operations succeed. Disabled keys or keys scheduled for deletion can lead to decryption failures, service outages, or permanent data loss.

In CloudFormation, `AWS::KMS::Key` resources must have `Properties.Enabled` set to `true` and must not define the `Properties.PendingWindowInDays` property. Resources missing `Enabled` or with `Enabled` set to `false` will be flagged as unusable. Any resource that defines `PendingWindowInDays` will be flagged because that indicates the key is scheduled for deletion.

Secure example (enable the key and omit pending-deletion settings):

```yaml
MyKey:
  Type: AWS::KMS::Key
  Properties:
    Enabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
Resources:
  myKey:
    Type: AWS::KMS::Key
    Properties:
      Enabled: true
      KeyPolicy:
        Version: '2012-10-17'
        Id: key-default-1
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Join:
              - ''
              - - 'arn:aws:iam::'
                - Ref: AWS::AccountId
                - :root
          Action: kms:*
          Resource: '*'
      Tags:
      - Key:
          Ref: Key
        Value:
          Ref: Value
Parameters:
  Key:
    Type: String
  Value:
    Type: String
```

```json
{
  "Resources": {
    "myKey": {
      "Type": "AWS::KMS::Key",
      "Properties": {
        "Enabled": true,
        "KeyPolicy": {
          "Version": "2012-10-17",
          "Id": "key-default-1",
          "Statement": [
            {
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:iam::",
                      {
                        "Ref": "AWS::AccountId"
                      },
                      ":root"
                    ]
                  ]
                }
              },
              "Action": "kms:*",
              "Resource": "*"
            }
          ]
        },
        "Tags": [
          {
            "Key": {
              "Ref": "Key"
            },
            "Value": {
              "Ref": "Value"
            }
          }
        ]
      }
    }
  },
  "Parameters": {
    "Key": {
      "Type": "String"
    },
    "Value": {
      "Type": "String"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "myKey": {
      "Type": "AWS::KMS::Key",
      "Properties": {
        "Enabled": false,
        "KeyPolicy": {
          "Id": "key-default-1",
          "Statement": [
            {
              "Resource": "*",
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:iam::",
                      {
                        "Ref": "AWS::AccountId"
                      },
                      ":root"
                    ]
                  ]
                }
              },
              "Action": "kms:*"
            }
          ],
          "Version": "2012-10-17"
        },
        "Tags": [
          {
            "Key": {
              "Ref": "Key"
            },
            "Value": {
              "Ref": "Value"
            }
          }
        ]
      }
    },
    "myKey2": {
      "Type": "AWS::KMS::Key",
      "Properties": {
        "Tags": [
          {
            "Key": {
              "Ref": "Key"
            },
            "Value": {
              "Ref": "Value"
            }
          }
        ],
        "Enabled": true,
        "PendingWindowInDays": 7,
        "KeyPolicy": {
          "Version": "2012-10-17",
          "Id": "key-default-1",
          "Statement": [
            {
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": {
                  "Fn::Join": [
                    "",
                    [
                      "arn:aws:iam::",
                      {
                        "Ref": "AWS::AccountId"
                      },
                      ":root"
                    ]
                  ]
                }
              },
              "Action": "kms:*",
              "Resource": "*"
            }
          ]
        }
      }
    },
    "Parameters": {
      "Key": {
        "Type": "String"
      },
      "Value": {
        "Type": "String"
      }
    }
  }
}
```

```yaml
#this is a problematic code where the query should report a result(s)
Resources:
  myKey:
    Type: AWS::KMS::Key
    Properties:
      Enabled: false
      KeyPolicy:
        Version: '2012-10-17'
        Id: key-default-1
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Join:
              - ''
              - - 'arn:aws:iam::'
                - Ref: AWS::AccountId
                - :root
          Action: kms:*
          Resource: '*'
      Tags:
      - Key:
          Ref: Key
        Value:
          Ref: Value
  myKey2:
    Type: AWS::KMS::Key
    Properties:
      Enabled: true
      PendingWindowInDays: 7
      KeyPolicy:
        Version: '2012-10-17'
        Id: key-default-1
        Statement:
        - Sid: Enable IAM User Permissions
          Effect: Allow
          Principal:
            AWS:
              Fn::Join:
              - ''
              - - 'arn:aws:iam::'
                - Ref: AWS::AccountId
                - :root
          Action: kms:*
          Resource: '*'
      Tags:
      - Key:
          Ref: Key
        Value:
          Ref: Value
Parameters:
  Key:
    Type: String
  Value:
    Type: String
```
