# Source: https://docs.datadoghq.com/security/default_rules/def-000-lvs.md

---
title: Salesforce discovery of populated tables from unseen network and device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Salesforce discovery of populated
  tables from unseen network and device
---

# Salesforce discovery of populated tables from unseen network and device
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1087-account-discovery](https://attack.mitre.org/techniques/T1087) 
## Goal{% #goal %}

Detects Salesforce users performing database discovery queries to identify populated tables from previously unseen network locations and devices.

## Strategy{% #strategy %}

This rule monitors Salesforce API events where `@evt.name` is `ApiEvent` and `@operation` is `Query` containing `SELECT COUNT() FROM` statements. It uses new value detection to identify when users execute count queries from network domains `@network.client.geoip.as.domain` and user agents `@http.useragent` that have not been previously observed for that user. Count queries are commonly used during reconnaissance phases to identify which database tables contain data without retrieving the actual records. This technique allows attackers to efficiently map the data landscape and prioritize tables for subsequent data extraction while minimizing their footprint.

## Triage & Response{% #triage--response %}

- Examine the specific count queries executed by `{{@usr.id}}` to determine which tables were being surveyed and whether this aligns with their job responsibilities.
- Review the new network domain and user agent combination to identify if it represents a legitimate new device or location for the user.
- Analyze the sequence and timing of the discovery queries to determine if they follow a systematic reconnaissance pattern.
- Check if the user has recently changed roles, received new system access, or is working on legitimate data analysis projects that would require table discovery.
- Verify with the user whether they initiated these queries from the new location and device, or if their account may be compromised.

*This detection is based on data from [Drift/Salesforce Security Update](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update) and [Widespread Data Theft Targets Salesforce Instances via Salesloft Drift](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift).*
