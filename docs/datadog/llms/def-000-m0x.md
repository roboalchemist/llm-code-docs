# Source: https://docs.datadoghq.com/security/default_rules/def-000-m0x.md

---
title: GitHub repository created with suspicious naming convention
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub repository created with
  suspicious naming convention
---

# GitHub repository created with suspicious naming convention
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detects newly created GitHub repositories with suspicious naming patterns that may indicate a ransom notice.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for repository creation events where the event is `repo.create`.

## Triage & Response{% #triage--response %}

- Examine the newly created repository `{{@github.repository}}` to determine whether it contains legitimate backup data or potential attacker content.
- Review the repository contents and commit history to understand when the repository was generated and what content exists.
- Check for any corresponding repository downloads, deletions, or modifications that occurred around the same time as the backup creation.
- Determine if the repository naming pattern matches known ransomware indicators and assess for potential compromise.
