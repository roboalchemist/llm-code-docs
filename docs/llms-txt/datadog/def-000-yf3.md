# Source: https://docs.datadoghq.com/security/default_rules/def-000-yf3.md

---
title: Salesforce previously unseen network for application OAuth token login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Salesforce previously unseen network
  for application OAuth token login
---

# Salesforce previously unseen network for application OAuth token login
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detects Salesforce OAuth token authentication from previously unseen network domains.

## Strategy{% #strategy %}

This rule monitors Salesforce login events where `@evt.name` is `Login` or `LoginEvent` with `@login_sub_type` containing `oauthrefreshtoken` or `OAuth Refresh Token` and `@login_type` is `Remote Access 2.0`. It uses new value detection to identify when applications authenticate from network domains `@network.client.geoip.as.domain` that have not been previously observed for that specific application. OAuth refresh tokens are long-lived credentials that allow applications to maintain access without user interaction, making them attractive targets for attackers who have compromised application credentials or stolen tokens from legitimate applications.

## Triage & Response{% #triage--response %}

- Examine the network domain and geographic location associated with the new OAuth token usage for `{{@application}}` to determine if it represents a legitimate deployment or suspicious activity.
- Review the application's typical usage patterns and authorized deployment locations to verify if the new network is expected.
- Check if there have been recent changes to the application's infrastructure, deployment, or hosting providers that would explain the new network domain.
- Analyze the timing of the OAuth token usage to identify any correlation with suspicious user activity or potential credential compromise.
- Verify with the application owner or development team whether the OAuth token usage from the new network domain was authorized.

*This detection is based on data from [Drift/Salesforce Security Update](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update) and [Widespread Data Theft Targets Salesforce Instances via Salesloft Drift](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift).*
