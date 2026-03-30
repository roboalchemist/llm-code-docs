# Source: https://docs.datadoghq.com/security/default_rules/def-000-ptj.md

---
title: Attempt to exfiltrate a 1Password item by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Attempt to exfiltrate a 1Password item
  by user
---

# Attempt to exfiltrate a 1Password item by user
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555)
## Goal{% #goal %}

Detect possible exfiltration attempts from 1Password through an item export.

## Strategy{% #strategy %}

This rule monitors 1Password audit logs to determine when the [export](https://developer.1password.com/docs/events-api/item-usage-actions/#export) item usage action occurs. This could indicate exfiltration attempts from 1Password by downloading or exporting items.

## Triage & response{% #triage--response %}

1. Investigate the `{{@usr.email}}` attempting to download or export item `{{@item_uuid}}` from vault `{{@vault_uuid}}`.
1. If this action was unintend by the user:
   - Rotate the user's 1Password master password
   - Identify all the items that were exported and rotate the necessary authentication credentials
