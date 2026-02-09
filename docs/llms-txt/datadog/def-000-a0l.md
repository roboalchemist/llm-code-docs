# Source: https://docs.datadoghq.com/security/default_rules/def-000-a0l.md

---
title: GitHub review settings altered to skip review after PR push
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub review settings altered to skip
  review after PR push
---

# GitHub review settings altered to skip review after PR push
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

This detection alerts when one of the following GitHub branch protection settings were disabled on a repository:

- Dismiss stale pull request approvals when new commits are pushed.
- Require approval of the most recent reviewable push.

## Strategy{% #strategy %}

These protections ensure that a second GitHub review is needed on a pull request if a commit gets added after the first approval. By disabling one of these settings, an actor is now able to merge code without any peer-review on a PR that was previously approved - the new code wouldn't get reviewed, allowing an attacker to introduce a backdoor or malicious code.

## Triage and response{% #triage-and-response %}

1. Reach out to the user `{{@github.actor}}` (`{{@external_identity_nameid}}`) and confirm the activity is recognized.
1. If the activity is suspicious:
   - [Block the user in GitHub](https://docs.github.com/en/enterprise-cloud@latest/communities/maintaining-your-safety-on-github/blocking-a-user-from-your-organization#blocking-a-user-in-the-organization-settings) to prevent further access.
   - Begin your organization's incident response process and investigate.
