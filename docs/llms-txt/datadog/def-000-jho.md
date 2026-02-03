# Source: https://docs.datadoghq.com/security/default_rules/def-000-jho.md

---
title: GitHub repository activity from suspicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub repository activity from
  suspicious IP
---

# GitHub repository activity from suspicious IP
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detects GitHub repository activities performed from IP addresses flagged as suspicious or malicious by threat intelligence.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for repository-related activities including `repo.push`, `reference.update`, `branch.create`, `branch.delete`, `repo.create`, `repo.destroy`, `repo.rename`, `repo.transfer`, and `repo.edit` actions. The detection correlates these activities with threat intelligence data where `@threat_intel.results.intention` is marked as suspicious or malicious.

## Triage and response{% #triage-and-response %}

- Examine the specific repository actions performed by `{{@github.actor}}` to determine the scope and nature of the suspicious activity.
- Review the geographic location and reputation of the source IP address to assess the legitimacy of the access.
- Verify if the GitHub user account has legitimate business reasons to access repositories from the flagged IP address.
- Check for any unauthorized code changes, new branches, or repository configuration modifications that could indicate malicious intent.
- Determine if any sensitive data, credentials, or proprietary code may have been accessed or exfiltrated during the suspicious activity.
