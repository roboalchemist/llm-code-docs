# Source: https://docs.datadoghq.com/security/default_rules/def-000-twy.md

---
title: Keeper high risk password detected for user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Keeper high risk password detected for
  user
---

# Keeper high risk password detected for user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Flag users with high-risk passwords stored in Keeper.

## Strategy{% #strategy %}

This rule allows monitoring of events where Keeper has detected high risk password stored by user in Keeper.

## Triage and response{% #triage-and-response %}

- Reach out to the user with email: `{{@usr.email}}` in enterprise id: `{{@enterprise_id}}`.
- Ensure the user rotates the password on all accounts where they may have reused this password.
- Ensure the user is aware of strong password guidelines.
