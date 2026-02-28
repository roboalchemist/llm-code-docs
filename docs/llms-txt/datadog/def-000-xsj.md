# Source: https://docs.datadoghq.com/security/default_rules/def-000-xsj.md

---
title: Google Compute Engine service account used outside of Google Cloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Compute Engine service account
  used outside of Google Cloud
---

# Google Compute Engine service account used outside of Google Cloud
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a [Google Compute Engine default service account](https://cloud.google.com/iam/docs/service-account-types#default) is used outside of Google Cloud.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when a Google Compute Engine default service account is used from outside a Google Cloud environment. The usage of a Google Cloud default service account, such as the Compute Engine service account, from outside the Google Cloud environment, could serve as an indicator that the credentials of the service account have been compromised.

## Triage and response{% #triage-and-response %}

1. Determine if the actions `{{@evt.name}}` taken by the Compute Engine default service account `{{@usr.id}}` are legitimate by looking at past activity and the type of API calls occurring.
1. If the action is legitimate, consider including the IP address or ASN in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - IP Investigation dashboard to see if the IP address: `{{@network.client.ip}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and investigate.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
