# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/access_key_not_rotated_within_90_days.md

---
title: High access key rotation period
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > High access key rotation period
---

# High access key rotation period

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `800fa019-49dd-421b-9042-7331fdd83fa2`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.amazonaws.cn/en_us/config/latest/developerguide/access-keys-rotated.html)

### Description{% #description %}

IAM access keys must be rotated regularly to reduce the risk from long-lived credentials and limit the exposure window if a key is compromised. Ensure an `AWS::Config::ConfigRule` resource exists with `Source.SourceIdentifier` set to `ACCESS_KEYS_ROTATED` and that its `InputParameters` contain a `maxAccessKeyAge` value less than or equal to `90` (days). Resources missing this ConfigRule, missing `InputParameters`, or with `maxAccessKeyAge` > `90` will be flagged; `maxAccessKeyAge` is evaluated numerically and is often provided as a string.

Secure configuration example (CloudFormation):

```yaml
AccessKeyRotationRule:
  Type: AWS::Config::ConfigRule
  Properties:
    ConfigRuleName: enforce-access-key-rotation
    Source:
      Owner: AWS
      SourceIdentifier: ACCESS_KEYS_ROTATED
    InputParameters: '{"maxAccessKeyAge":"90"}'
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
        SourceIdentifier: ACCESS_KEYS_ROTATED
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
          "SourceIdentifier": "ACCESS_KEYS_ROTATED",
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
