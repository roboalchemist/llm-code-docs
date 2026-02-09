# Source: https://docs.datadoghq.com/security/default_rules/def-000-fnn.md

---
title: Attempt to modify a 1Password item by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Attempt to modify a 1Password item by
  user
---

# Attempt to modify a 1Password item by user
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detect when a 1Password user attempts to modify an item.

## Strategy{% #strategy %}

This rule monitors 1Password audit logs to determine when the the [enter-item-edit-mode](https://developer.1password.com/docs/events-api/item-usage-actions/#enter-item-edit-mode) item usage action occurs. This could indicate an attempt to modify an item.

## Triage & response{% #triage--response %}

1. Investigate the `{{@usr.email}}` attempting to modify item `{{@item_uuid}}` within vault `{{@vault_uuid}}`.
1. If this action was unintend by the user:
   - Rotate the user's 1Password master password
   - Identify all the items that were modified and rotate the necessary authentication credentials
