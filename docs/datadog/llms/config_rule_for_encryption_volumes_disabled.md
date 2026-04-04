# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/config_rule_for_encryption_volumes_disabled.md

---
title: Config rule for encrypted volumes disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Config rule for encrypted volumes disabled
---

# Config rule for encrypted volumes disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1b6322d9-c755-4f8c-b804-32c19250f2d9`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source)

### Description{% #description %}

AWS Config should include the managed rule that detects unencrypted EBS volumes so that unencrypted volumes, snapshots, and backups are identified and remediated to prevent data exposure if storage media or snapshots are compromised.

This check looks for an `AWS::Config::ConfigRule` resource with `Properties.Source.SourceIdentifier` set to `ENCRYPTED_VOLUMES`. Resources missing this config rule or with a different `SourceIdentifier` will be flagged.

Ensure a config rule with `SourceIdentifier` set to `ENCRYPTED_VOLUMES` (typically `Owner` set to `AWS` for the managed rule) is defined and enabled in your CloudFormation template.

Secure CloudFormation example:

```yaml
EncryptedVolumesConfigRule:
  Type: AWS::Config::ConfigRule
  Properties:
    ConfigRuleName: encrypted-volumes
    Source:
      Owner: AWS
      SourceIdentifier: ENCRYPTED_VOLUMES
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  ConfigRule:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: access-keys-rotated
      InputParameters:
        maxAccessKeyAge: 90
      Source:
        Owner: AWS
        SourceIdentifier: ENCRYPTED_VOLUMES
      MaximumExecutionFrequency: TwentyFour_Hours
```

```json
{
  "Resources": {
    "ConfigRule": {
      "Type": "AWS::Config::ConfigRule",
      "Properties": {
        "MaximumExecutionFrequency": "TwentyFour_Hours",
        "ConfigRuleName": "access-keys-rotated",
        "InputParameters": {
          "maxAccessKeyAge": 90
        },
        "Source": {
          "SourceIdentifier": "ENCRYPTED_VOLUMES",
          "Owner": "AWS"
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
    "ConfigRule": {
      "Type": "AWS::Config::ConfigRule",
      "Properties": {
        "ConfigRuleName": "access-keys-rotated",
        "InputParameters": {
          "maxAccessKeyAge": 100
        },
        "Source": {
          "Owner": "AWS",
          "SourceIdentifier": "ACCESS_KEYS_ROTATED"
        },
        "MaximumExecutionFrequency": "TwentyFour_Hours"
      }
    }
  }
}
```

```yaml
Resources:
  ConfigRule:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: access-keys-rotated
      InputParameters:
        maxAccessKeyAge: 100
      Source:
        Owner: AWS
        SourceIdentifier: ACCESS_KEYS_ROTATED
      MaximumExecutionFrequency: TwentyFour_Hours
```
