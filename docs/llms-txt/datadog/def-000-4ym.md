# Source: https://docs.datadoghq.com/security/default_rules/def-000-4ym.md

---
title: Google Security Command Center
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Security Command Center
---

# Google Security Command Center
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when [Google Security Command Center](https://cloud.google.com/security-command-center/docs) raises an active threat finding.

## Strategy{% #strategy %}

Google Security Command Center helps you strengthen your security posture by evaluating your security and data attack surface; providing asset inventory and discovery; identifying misconfigurations, vulnerabilities and threats; and helping you mitigate and remediate risks.

This detection rule filters for [threat findings](https://cloud.google.com/security-command-center/docs/finding-classes#threat_class) which have not been muted. Findings in the Threat class identify a potential active attack or other unwanted or malicious activity.

## Triage and response{% #triage-and-response %}

1. Investigate the finding to determine if it is malicious or benign.
1. If the finding is deemed malicious, follow the [investigation and remediation guidance](https://cloud.google.com/security-command-center/docs/how-to-investigate-threats) provided by Google and also any internal incident response processes.
1. If the finding is a false positive, you can reduce false positives by:
   - [Muting findings in Security Command Center](https://cloud.google.com/security-command-center/docs/how-to-mute-findings)
   - [Disabling detectors](https://cloud.google.com/sdk/gcloud/reference/alpha/scc/settings/services/modules/disable)
   - [Adding assets to allowlists](https://cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#allowlist-assets)
