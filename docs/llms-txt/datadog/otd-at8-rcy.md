# Source: https://docs.datadoghq.com/security/default_rules/otd-at8-rcy.md

---
title: Encrypted administrator password retrieved for Windows EC2 instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Encrypted administrator password
  retrieved for Windows EC2 instance
---

# Encrypted administrator password retrieved for Windows EC2 instance
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555)
## Goal{% #goal %}

Detect a user attempting to retrieve the encrypted Administrator password for a Windows EC2 instance.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect if an attacker has attempted to retrieve the encrypted Administrator password for a Windows EC2 instance using the [`GetPasswordData`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) API call.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
If the API call was made by the user:
- Determine if this user should be accessing this EC2 instance.
- If Yes, advise the user to speak with the instance owner to resolve the error.
- If No, see if other API calls were made by the user and determine if they warrant further investigation.
