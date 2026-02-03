# Source: https://docs.datadoghq.com/security/default_rules/def-000-wnp.md

---
title: Datadog Malicious PR Protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Datadog Malicious PR Protection
---

# Datadog Malicious PR Protection
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detect malicious code contributions to repositories.

## Strategy{% #strategy %}

This rule uses an LLM to scan the context of the pull request to detect changes with intent to cause harm (not accidental vulnerabilities).

## Triage and Response{% #triage-and-response %}

Pull request {{@malicious_pr_protection.repo.pull_request.url}} was flagged as **{{@malicious\_pr\_protection.scan.verdict}}**.

**Reason:**

{{#if @malicious_pr_protection.__dd_internal.reason_pt1}}{{@malicious_pr_protection.__dd_internal.reason_pt1}}{{#if @malicious_pr_protection.__dd_internal.reason_pt2}}{{@malicious_pr_protection.__dd_internal.reason_pt2}}{{/if}}{{#if @malicious_pr_protection.__dd_internal.reason_pt3}}{{@malicious_pr_protection.__dd_internal.reason_pt3}}{{/if}}{{/if}}{{#unless @malicious_pr_protection.__dd_internal.reason_pt1}}{{@malicious_pr_protection.scan.reason}}{{/unless}}

*Scan performed at head commit: {{@malicious\_pr\_protection.repo.pull\_request.head\_commit\_sha}}*

{{#is_match "case_name" "PR flagged as Malicious"}}- Review the PR and act accordingly. To do so:

1. **Triage**: Mark the signal as "Under Review"
   - Read the reason (`@malicious_pr_protection.scan.reason`) attribute: *Does it seem justified by itself?*
   - Review the change under {{@malicious_pr_protection.repo.pull_request.url}}: *Do the verdict and reason seem accurate?*
   - Consider context: *Does further context (author, linked tickets, commits, or comments) indicate benign actions or malicious actions?*
1. **Respond**: Create a case for further inspection, declare an incident, or archive this signal.

### Details{% #details %}

Certain conditions can closely resemble behavior of attackers (for example, assignment of admin privileges or handling of secrets), and are known to introduce false positives. {{/is_match}}
