# Source: https://docs.datadoghq.com/security/default_rules/v5u-24i-koa.md

---
title: Brute forced ConsoleLogin event correlates with an assumed role event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Brute forced ConsoleLogin event
  correlates with an assumed role event
---

# Brute forced ConsoleLogin event correlates with an assumed role event
Classification:attack
## Goal{% #goal %}

Correlate a bruteforce login with a user attempting to assume an anomalous number of roles.

## Strategy{% #strategy %}

Correlate the [Potential brute force attack on AWS ConsoleLogin](https://docs.datadoghq.com/security/default_rules/aws-iam-brute-force-consolelogin/) and [Anomalous number of assumed roles from user](https://docs.datadoghq.com/security/default_rules/cloudtrail-aws-user-attempted-to-assumerole-anomaly) signals based on the ARN: `{{@userIdentity.arn}}`.

## Triage and response{% #triage-and-response %}

1. Set signal triage state to `Under Review`.
1. Determine if the brute force attack was successful.
   - If the login was not legitimate:
     - Investigate the user using the `User Investigation Dashboard`
     - Rotate credentials on the brute forced account
     - Enable MFA if it is not already enabled
   - If the login was legitimate:
     - Triage the signal as a false positive
