# Source: https://docs.datadoghq.com/security/default_rules/def-000-mfm.md

---
title: Anomalous number of secrets retrieved from AWS Secrets Manager
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of secrets retrieved
  from AWS Secrets Manager
---

# Anomalous number of secrets retrieved from AWS Secrets Manager
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555)
## Goal{% #goal %}

Detect when an anomalous number of secrets are retrieved from AWS Secrets Manager.

## Strategy{% #strategy %}

This rule lets you monitor the [`GetSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) CloudTrail API call to detect when a secret is retrieved. The anomaly detection generates a security signal when a user deviates from their baseline.

For more information about the anomaly detection method, see [Detect security threats with anomaly detection rules](https://www.datadoghq.com/blog/anomaly-detection-rules-datadog/).

## Triage and response{% #triage-and-response %}

1. Determine whether the identity: `{{@userIdentity.arn}}` is expected to access the AWS Secrets Manager and the secret values within `@requestParameters.secretId`.
1. If the activity is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the activity is unusual:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process as well as an investigation.
