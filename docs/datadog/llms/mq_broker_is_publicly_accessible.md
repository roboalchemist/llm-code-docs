# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/mq_broker_is_publicly_accessible.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/mq_broker_is_publicly_accessible.md

---
title: Amazon MQ broker is publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Amazon MQ broker is publicly accessible
---

# Amazon MQ broker is publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `68b6a789-82f8-4cfd-85de-e95332fe6a61`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-publiclyaccessible)

### Description{% #description %}

Amazon MQ brokers must not be publicly accessible because exposing a broker to the public internet increases the attack surface and can allow unauthorized access to messages and management interfaces. Check the `PubliclyAccessible` property on `AWS::AmazonMQ::Broker` resources. It must be omitted or set to `false`. Resources with `PubliclyAccessible` set to `true` will be flagged as a security risk.

Secure CloudFormation example:

```yaml
MyBroker:
  Type: AWS::AmazonMQ::Broker
  Properties:
    BrokerName: my-broker
    EngineType: ActiveMQ
    EngineVersion: "5.15.6"
    PubliclyAccessible: false
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
      PubliclyAccessible: false
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
    "BasicBroker2": {
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
        "AutoMinorVersionUpgrade": "false"
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
    "BasicBroker2": {
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
        "PubliclyAccessible": true
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
      EncryptionOptions:
        UseAwsOwnedKey: true
      EngineType: ActiveMQ
      EngineVersion: "5.15.0"
      HostInstanceType: mq.t2.micro
      PubliclyAccessible: true
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
