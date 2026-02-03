# Source: https://docs.datadoghq.com/security/default_rules/def-000-rtx.md

---
title: Malicious authentication attempt detected by Okta ThreatInsight
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Malicious authentication attempt
  detected by Okta ThreatInsight
---

# Malicious authentication attempt detected by Okta ThreatInsight
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect malicious Okta authentication attempts based on Okta ThreatInsight.

## Strategy{% #strategy %}

This rule lets you monitor Okta authentication attempts where the `@evt.name` is `security.threat.detected` and the `@debugContext.debugData.threatSuspected` value is `true`.

[Okta ThreatInsight](https://help.okta.com/en-us/Content/Topics/Security/threat-insight/configure-threatinsight-system-log.htm) uses these attributes to flag authentication attempts that are deemed as threats.

## Triage and response{% #triage-and-response %}

1. Determine if the source IP `{{@network.client.ip}}` is anomalous within the organization:
   - Does threat intelligence indicate that this IP has been associated with malicious activity?
   - Is the geo-location, ASN, or domain uncommon for the organization?
   - Use the Cloud SIEM - IP Investigation dashboard to see if the IP address has taken other actions.
1. Investigate the `debugContext.debugData.threatDetections` field to determine the threat reason and level.
1. If the IP is deemed malicious:
   - Confirm that no successful authentication attempts have been made.
   - If a successful authentication attempt is observed, begin your company's incident response process.

## Changelog{% #changelog %}

- 13 September 2023 - Updated `critical` case severities to `medium` and `medium` case severities to `low`.
