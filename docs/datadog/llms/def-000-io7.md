# Source: https://docs.datadoghq.com/security/default_rules/def-000-io7.md

---
title: Slack IdP configuration changed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Slack IdP configuration changed
---

# Slack IdP configuration changed
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when there has been a modification to a Slack [identity provider](https://slack.com/intl/en-gb/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) (IdP) configuration setting.

## Strategy{% #strategy %}

This rule monitors Slack audit logs for when a configuration has been modified in Slack's IdP settings. Attackers may try to modify authentication processes to access user credentials or gain unauthorized access to other accounts.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@usr.email}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.
