# Source: https://docs.datadoghq.com/security/default_rules/def-000-p3z.md

---
title: GitHub secret scanning alert generated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > GitHub secret scanning alert generated
---

# GitHub secret scanning alert generated

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552) 
## Goal{% #goal %}

Detect when a GitHub scan detects a secret stored in a repository.

## Strategy{% #strategy %}

Secret scanning is a security feature that helps detect and prevent the accidental inclusion of sensitive information such as API keys, passwords, tokens, and other secrets in your repository. When enabled, secret scanning scans commits in repositories for known types of secrets and alerts repository administrators upon detection.

Secret scanning scans your entire Git history on all branches present in your GitHub repository for secrets. GitHub will also periodically run a full Git history scan of existing content in public repositories where secret scanning is enabled.

If a scan results in a potential secret, Github generates a secret scanning alert to notify repository administrators.

## Triage and response{% #triage-and-response %}

1. Determine if the detected secret is considered sensitive for your environment.
1. If the publishing of the detected secret poses a risk to other systems, begin your incident response process and investigate.
