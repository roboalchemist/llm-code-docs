# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/amazon_mq_broker_encryption_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/amazon_mq_broker_encryption_disabled.md

---
title: Amazon MQ broker encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Amazon MQ broker encryption disabled
---

# Amazon MQ broker encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `316278b3-87ac-444c-8f8f-a733a28da60f`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-encryptionoptions)

### Description{% #description %}

Amazon MQ brokers must have encryption options defined so message data, broker storage, and snapshots are encrypted at rest and protected from unauthorized access if storage media or backups are compromised. In CloudFormation, the `AWS::AmazonMQ::Broker` resource must include the `EncryptionOptions` property configured to enable AWS KMS encryption. For example, set `KmsKeyId` to a customer-managed KMS key or setting `UseAwsOwnedKey` to `true` to rely on an AWS-owned key. Resources missing the `EncryptionOptions` property will be flagged. Use a customer-managed KMS key (`KmsKeyId`) when you need full control over key rotation and access policies.

Secure configuration example (CloudFormation YAML):

```yaml
MyBroker:
  Type: AWS::AmazonMQ::Broker
  Properties:
    BrokerName: my-broker
    EngineType: ActiveMQ
    EngineVersion: 5.15.0
    HostInstanceType: mq.t3.micro
    EncryptionOptions:
      KmsKeyId: arn:aws:kms:us-east-1:123456789012:key/abcd-ef01-2345-6789
      UseAwsOwnedKey: false
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Create a basic ActiveMQ broker"
Resources:
  BasicBroker:
    Type: "AWS::AmazonMQ::Broker"
    Properties:
      AutoMinorVersionUpgrade: "false"
      BrokerName: MyBasicBroker
      DeploymentMode: SINGLE_INSTANCE
      EncryptionOptions:
        UseAwsOwnedKey: true
      EngineType: ActiveMQ
      EngineVersion: "5.15.0"
      HostInstanceType: mq.t2.micro
      PubliclyAccessible: "true"
      Users:
        -
          ConsoleAccess: "true"
          Groups:
            - MyGroup
          Password:
            Ref: "BrokerPassword"
          Username:
            Ref: "BrokerUsername"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Create a basic ActiveMQ broker",
  "Resources": {
    "BasicBroker": {
      "Type": "AWS::AmazonMQ::Broker",
      "Properties": {
        "BrokerName": "MyBasicBroker",
        "DeploymentMode": "SINGLE_INSTANCE",
        "EncryptionOptions": {
          "UseAwsOwnedKey": true
        },
        "EngineType": "ActiveMQ",
        "EngineVersion": "5.15.0",
        "HostInstanceType": "mq.t2.micro",
        "Users": [
          {
            "ConsoleAccess": "true",
            "Groups": [
              "MyGroup"
            ],
            "Password": {
              "Ref": "BrokerPassword"
            },
            "Username": {
              "Ref": "BrokerUsername"
            }
          }
        ],
        "AutoMinorVersionUpgrade": "false",
        "PubliclyAccessible": "true"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Create a basic ActiveMQ broker",
  "Resources": {
    "BasicBroker": {
      "Type": "AWS::AmazonMQ::Broker",
      "Properties": {
        "HostInstanceType": "mq.t2.micro",
        "PubliclyAccessible": "true",
        "Users": [
          {
            "ConsoleAccess": "true",
            "Groups": [
              "MyGroup"
            ],
            "Password": {
              "Ref": "BrokerPassword"
            },
            "Username": {
              "Ref": "BrokerUsername"
            }
          }
        ],
        "AutoMinorVersionUpgrade": "false",
        "BrokerName": "MyBasicBroker",
        "DeploymentMode": "SINGLE_INSTANCE",
        "EngineType": "ActiveMQ",
        "EngineVersion": "5.15.0"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Create a basic ActiveMQ broker"
Resources:
  BasicBroker:
    Type: "AWS::AmazonMQ::Broker"
    Properties:
      AutoMinorVersionUpgrade: "false"
      BrokerName: MyBasicBroker
      DeploymentMode: SINGLE_INSTANCE
      EngineType: ActiveMQ
      EngineVersion: "5.15.0"
      HostInstanceType: mq.t2.micro
      PubliclyAccessible: "true"
      Users:
        -
          ConsoleAccess: "true"
          Groups:
            - MyGroup
          Password:
            Ref: "BrokerPassword"
          Username:
            Ref: "BrokerUsername"
```
