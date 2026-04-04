# Source: https://docs.datadoghq.com/security/default_rules/wiz-kf3-3yo.md

---
title: Okta policy rule deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Okta policy rule deleted
---

# Okta policy rule deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when an Okta policy rule is deleted.

## Strategy{% #strategy %}

This rule lets you monitor the following Okta event to detect when a policy rule is deleted:

- `policy.rule.delete`

## Triage and response{% #triage-and-response %}

1. Contact the Okta administrator to confirm that the user: `{{@usr.email}}` should be deleting policy rules.
1. If the change was **not** authorized, verify there are no other signals from the user: `{{@usr.email}}`.
