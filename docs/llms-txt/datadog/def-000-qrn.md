# Source: https://docs.datadoghq.com/security/default_rules/def-000-qrn.md

---
title: Windows DNS query to Tor Onion address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows DNS query to Tor Onion address
---

# Windows DNS query to Tor Onion address

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Detects when a Windows host makes DNS queries to Tor onion addresses.

## Strategy{% #strategy %}

This detection monitors DNS event logs where the query name contains ".onion" domains, which are specific to Tor hidden services. The detection looks for Event ID 3008 containing `*.onion*` in the `QueryName` field.

DNS queries for these addresses could indicate the presence of Tor software or specially configured applications attempting to access hidden services. This activity is notable as Tor can be leveraged by threat actors to hide command and control communications, or access underground marketplaces.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` system that made DNS queries to Tor onion addresses.
- Examine the specific .onion domain queried to determine if it's associated with known malicious services.
- Determine which process initiated the DNS query by correlating with process creation events.
- Review user activity on the system around the time of the query to identify who was using the system.
- Check for installed Tor browser or other Tor-related software on the system.
- Examine network connections from the same host to identify if successful connections were established.
- Look for any data transfer patterns that might indicate exfiltration attempts.
