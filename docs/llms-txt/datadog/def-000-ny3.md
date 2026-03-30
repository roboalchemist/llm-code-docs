# Source: https://docs.datadoghq.com/security/default_rules/def-000-ny3.md

---
title: Known compromised IAM users should not be present in the account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Known compromised IAM users should not
  be present in the account
---

# Known compromised IAM users should not be present in the account

## Description{% #description %}

Ensure that no known compromised IAM users are present in your AWS account. When AWS identifies compromised AWS IAM user credentials, it attaches the managed policy [AWSCompromisedKeyQuarantineV2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCompromisedKeyQuarantineV2.html) that blocks commonly abused actions, and typically opens a support case. When this happens, it's important to make sure that the user is removed, or its credentials are disabled.

**Note**: This rule only triggers if the IAM user has active programmatic credentials.

## Remediation{% #remediation %}

Follow the [Rotating access keys AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console) to disable the compromised access key, and create a new one. You can also follow the [AWS incident response playbook](https://github.com/aws-samples/aws-customer-playbook-framework/blob/main/docs/Compromised_IAM_Credentials.md) and the [AWS incident response guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/technique-access-containment.html) to assess the impact of the compromised credentials.
