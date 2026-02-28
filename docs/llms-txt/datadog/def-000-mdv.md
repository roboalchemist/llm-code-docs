# Source: https://docs.datadoghq.com/security/default_rules/def-000-mdv.md

---
title: Anomalous number of Auth0 Attack Protection events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of Auth0 Attack
  Protection events
---

# Anomalous number of Auth0 Attack Protection events
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect an anomalous number of [Attack Protection](https://auth0.com/docs/secure/attack-protection) events for a hostname.

## Strategy{% #strategy %}

This rule allows you to monitor Auth0 logs and detect when there is an anomalous number of Attack Protection events for a host. Attack Protection is a feature that Auth0 provides to detect and mitigate attacks, including brute-force protection, suspicious IP throttling, breached password detection, bot detection, and adaptive multi-factor authentication. Abnormally high volumes of attack protection events may be an indicator of an ongoing credential based attack like credential stuffing.

## Triage and response{% #triage-and-response %}

1. Determine if the spike in Attack Protection events are abnormal for your application:
   - Is the spike related to a single IP (`@network.client.ip`) or user agent (`@http.useragent`)?
   - Is it coming from unexpected geo-locations (`@network.client.geoip.country.name`) for your application?
   - Is it comming from a set of unexpected autonomous systems (AS)?
1. If it's deemed to be an attack:
   - Filter for any successful authentications (`@evt.name:success_login`) from the attackers infrastructure.
   - If any accounts have been compromised, begin your organization's incident response process and investigate.
