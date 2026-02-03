# Source: https://docs.datadoghq.com/security/default_rules/4xt-j23-jnb.md

---
title: Google Cloud Project external principal added as project owner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud Project external principal
  added as project owner
---

# Google Cloud Project external principal added as project owner
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect an attempt to add an external principal as a Google Cloud project owner.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when an attempt to add an external principal as a Google Cloud project owner has occurred. An attacker who has already gained initial access may try to maintain access by adding an external principal to the project as an owner.

**Notes:**

- This rule triggers when a principal with an email address with the domain of `gmail.com` or `googlemail.com` is added to a project.

## Triage and response{% #triage-and-response %}

1. Reach out to the user or owner of the service account to determine if this action is legitimate.
1. If the action is legitimate, consider including the user or service account in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - User Investigation dashboard to see if the user or service account `{{@usr.email}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and investigate.
