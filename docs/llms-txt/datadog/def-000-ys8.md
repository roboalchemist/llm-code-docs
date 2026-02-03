# Source: https://docs.datadoghq.com/security/default_rules/def-000-ys8.md

---
title: User agent associated with penetration testing tool observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > User agent associated with penetration
  testing tool observed
---

# User agent associated with penetration testing tool observed
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059) 
## Goal{% #goal %}

Detect when a penetration testing tool user agent is observed.

## Strategy{% #strategy %}

This rule monitors cloud audit logs for requests with a user agent correlating to a penetration testing tool. While these tools may be used legitimately by an organization to assess their security posture, they can also be used by attackers as a means of discovery once they have gained unauthorized access to your cloud environment.

## Triage and response{% #triage-and-response %}

1. Determine if your organization used any of the tools observed for its own security assessment.
1. If the tool was used by your organization, consider adding a suppression for the penetration tool's identity or IP address. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the tool was not used by your organization, begin your company's incident response process and an investigation.
   - If appropriate, disable or rotate the affected credential or identity.
   - Investigate any actions taken by the identity.

## Changelog{% #changelog %}

- 23 July 2025 - Update case naming to indicate cloud provider in the signal naming.
