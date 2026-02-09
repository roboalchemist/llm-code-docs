# Source: https://docs.datadoghq.com/security/default_rules/def-000-p2e.md

---
title: LastPass vault content export attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > LastPass vault content export attempt
---

# LastPass vault content export attempt
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detect possible exfiltration attempts from LastPass through a vault export.

## Strategy{% #strategy %}

This rule monitors LastPass event logs to determine when a vault has been exported. This could indicate exfiltration attempts from LastPass by downloading or exporting items within a vault.

## Triage & response{% #triage--response %}

1. Investigate the `{{@usr.name}}` attempting to download or export the vault.
1. If this action was unintended by the user:
   - Rotate the user's LastPass master password.
   - Identify all the items within the vault that were exported and rotate the necessary authentication credentials.
