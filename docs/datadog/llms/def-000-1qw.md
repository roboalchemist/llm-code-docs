# Source: https://docs.datadoghq.com/security/default_rules/def-000-1qw.md

---
title: Google Compute Engine image created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Compute Engine image created
---

# Google Compute Engine image created
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496)
## Goal{% #goal %}

Detect when a Google Compute Engine image is created.

## Strategy{% #strategy %}

Monitor Google Cloud Audit Logs to determine when the following method is invoked from an external IP adddress:

- `v*.compute.images.insert`

## Triage and response{% #triage-and-response %}

1. Investigate the user (`{{@usr.id}}`) and IP address (`{{@network.client.ip}}`) where the image creation activity originated from and determine whether they are authorised to perform this activity.
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - User Investigation dashboard to see if the user `{{@usr.id}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
