# Source: https://docs.datadoghq.com/security/default_rules/def-000-mtq.md

---
title: Salesforce unusual CLI activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Salesforce unusual CLI activity
---

# Salesforce unusual CLI activity
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects unusual Salesforce CLI tool usage.

## Strategy{% #strategy %}

This rule monitors Salesforce events containing user agent strings `Salesforce-Multi-Org-Fetcher/1.0` or `Salesforce-CLI/1.0`. These user agents are associated with Salesforce command-line interface tools and multi-organization management utilities that provide programmatic access to Salesforce data and configuration. While these tools have legitimate administrative uses, they can also be leveraged by attackers for automated data extraction, configuration changes, or reconnaissance activities. The detection triggers on any usage of these CLI tools, as they represent elevated access capabilities that should be carefully monitored.

## Triage & Response{% #triage--response %}

- Examine the specific activities performed by `{{@usr.id}}` using the Salesforce CLI tools to determine if they align with authorized administrative tasks.
- Review the user's role and permissions to verify if they have legitimate reasons to use command-line tools for Salesforce administration.
- Analyze the timing and frequency of the CLI usage to identify potential automated or scripted activities that may indicate malicious intent.
- Check if the CLI usage correlates with any recent system changes, data migrations, or administrative projects that would justify the tool usage.
- Verify with the user and their supervisor whether the CLI tool usage was authorized and part of legitimate business operations.

*This detection is based on data from [Drift/Salesforce Security Update](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update) and [Widespread Data Theft Targets Salesforce Instances via Salesloft Drift](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift).*
