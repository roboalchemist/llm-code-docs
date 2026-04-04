# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/guardduty_detector_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/guardduty_detector_disabled.md

---
title: GuardDuty detector disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > GuardDuty detector disabled
---

# GuardDuty detector disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a25cd877-375c-4121-a640-730929936fac`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)

### Description{% #description %}

Amazon GuardDuty must be enabled to provide continuous threat detection and alerting. Disabling it can allow malicious activity to go undetected and delay incident response.

The `Enable` property on `AWS::GuardDuty::Detector` resources must be set to `true`. This rule flags `AWS::GuardDuty::Detector` resources where `Enable` is explicitly set to `false`.

Secure configuration example:

```yaml
MyDetector:
  Type: AWS::GuardDuty::Detector
  Properties:
    Enable: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
    mydetector:
      Type: AWS::GuardDuty::Detector
      Properties:
          Enable: True
          FindingPublishingFrequency: FIFTEEN_MINUTES
```

```json
{
  "document": [
    {
      "AWSTemplateFormatVersion": "2010-09-09",
      "Resources": {
        "mydetector2": {
          "Properties": {
            "Enable": true,
            "FindingPublishingFrequency": "FIFTEEN_MINUTES"
          },
          "Type": "AWS::GuardDuty::Detector"
        }
      },
      "id": "f63e21c6-c58e-45cf-b7b4-6b548d9f7674",
      "file": "C:\\Users\\foo\\Desktop\\Data\\yaml\\yaml.yaml"
    }
  ]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "mydetector4": {
      "Properties": {
        "Enable": false,
        "FindingPublishingFrequency": "FIFTEEN_MINUTES"
      },
      "Type": "AWS::GuardDuty::Detector"
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  mydetector3:
    Type: AWS::GuardDuty::Detector
    Properties:
        Enable: False
        FindingPublishingFrequency: FIFTEEN_MINUTES
```
