# Source: https://docs.datadoghq.com/security/default_rules/def-000-rcr.md

---
title: Cloudtrail SecretsManager secret retrieved from AWS CloudShell environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cloudtrail SecretsManager secret
  retrieved from AWS CloudShell environment
---

# Cloudtrail SecretsManager secret retrieved from AWS CloudShell environment
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555)
## Goal{% #goal %}

Detect when an AWS secret is retrieved from an AWS CloudShell environment.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when an AWS secret is retrieved from an AWS CloudShell environment. The threat group [LUCR-3](https://permiso.io/blog/lucr-3-scattered-spider-getting-saas-y-in-the-cloud) uses AWS CloudShell in the AWS management console to carry out activities that require direct interaction with the AWS API, such as the retrieval of secrets.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have carried out this operation.
1. If the API calls were not made by the user:

- Rotate user credentials.
- Rotate the secrets retrieved by the identity, if feasible.
- Determine what other API calls were made by the user.
- Begin your organization's incident response process and investigate.
