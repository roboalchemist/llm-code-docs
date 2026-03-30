# Source: https://docs.datadoghq.com/security/default_rules/def-000-nns.md

---
title: >-
  Google Cloud BigQuery results saved to cloud storage by a previously unseen
  user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud BigQuery results saved to
  cloud storage by a previously unseen user
---

# Google Cloud BigQuery results saved to cloud storage by a previously unseen user
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1537-transfer-data-to-cloud-account](https://attack.mitre.org/techniques/T1537)
## Goal{% #goal %}

Detect when a previously unseen user attempts to export Google Cloud BigQuery results to cloud storage.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when a previously unseen user attempts to export Google Cloud BigQuery results to cloud storage. An attacker who has already gained initial access may try to exfiltrate data by saving BigQuery results to external cloud storage outside of the compromised organization.

**Notes:**

- This rule uses the `New Value` detection method, to determine when a previously unseen user performs this action.

## Triage and response{% #triage-and-response %}

1. Reach out to the user or owner of the service account to determine if this action is legitimate.
1. If the action is legitimate, consider including the IP address or ASN in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - IP Investigation dashboard to see if the IP address: `{{@network.client.ip}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and investigate.
