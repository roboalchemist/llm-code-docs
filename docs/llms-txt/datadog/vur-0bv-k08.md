# Source: https://docs.datadoghq.com/security/default_rules/vur-0bv-k08.md

---
title: ConsoleLogin event correlates privileged policy applying to a role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ConsoleLogin event correlates
  privileged policy applying to a role
---

# ConsoleLogin event correlates privileged policy applying to a role
Classification:attack 
## Goal{% #goal %}

Correlate a brute force login with a privileged policy being applied to a role.

## Strategy{% #strategy %}

Correlate the [Potential brute force attack on AWS ConsoleLogin](https://docs.datadoghq.com/security/default_rules/aws-iam-brute-force-consolelogin/) and [cloudtrail AWS IAM AdministratorAccess policy was applied to a role](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-iam-apply-privilegedpolicy-to-role/) signals based on the ARN: `{{@userIdentity.arn}}`.

## Triage and response{% #triage-and-response %}

1. Set signal triage state to `Under Review`.
1. Determine if the brute force attack was successful.
   - If the login was not legitimate:
     - Revert the privileged policy change
     - Rotate credentials on the brute forced account
     - Enable MFA if it is not already
   - If the login was legitimate:
     - Triage the signal as a false positive
