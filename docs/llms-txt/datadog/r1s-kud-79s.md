# Source: https://docs.datadoghq.com/security/default_rules/r1s-kud-79s.md

---
title: IAM access keys that are inactive and older than 1 year should be removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM access keys that are inactive and
  older than 1 year should be removed
---

# IAM access keys that are inactive and older than 1 year should be removed
 
## Description{% #description %}

This rule identifies IAM access keys that are older than one year and have not been used in the past 30 days.

## Rationale{% #rationale %}

This is a good indicator that an access key or IAM user that is not used anymore, and raises a security risk. IAM access keys are static secrets that do not change. This leak represents a common cause for cloud security breaches.

## Remediation{% #remediation %}

- Verify that the IAM user is still actively used or if it can be removed.
- Verify that the IAM access key is still actively used or if it can be removed.
- If the IAM user is still needed, rotate the access key. For more information, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey).

### From the console{% #from-the-console %}

Follow the [Rotating IAM user access keys (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console) AWS documentation to rotate access keys.

### From the command line{% #from-the-command-line %}

Follow the [Rotating IAM user access keys (AWS CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_cli) AWS documentation to rotate access keys.
