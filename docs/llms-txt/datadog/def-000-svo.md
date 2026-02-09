# Source: https://docs.datadoghq.com/security/default_rules/def-000-svo.md

---
title: Netskope detected JA3 hash from multiple client IPs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Netskope detected JA3 hash from
  multiple client IPs
---

# Netskope detected JA3 hash from multiple client IPs

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Detects when the same SSL/TLS client fingerprint (JA3 hash) is observed from multiple distinct client IP addresses in Netskope traffic.

## Strategy{% #strategy %}

This rule monitors Netskope SSL traffic where the same `@x-cs-ssl-ja3` fingerprint appears across multiple client IP addresses. JA3 is a fingerprinting method that creates a unique identifier based on SSL/TLS client handshake characteristics including cipher suites, extensions, and supported curves. Typically, different systems generate unique JA3 hashes due to variations in client software versions, operating systems, and SSL/TLS library implementations. When identical JA3 hashes appear from multiple different source IPs, this indicates the same specific client software or tool is being used across those systems. This pattern can reveal adversary activity where threat actors deploy the same command and control tooling, post-exploitation frameworks, or data exfiltration utilities across compromised endpoints, enabling detection of coordinated campaigns that might otherwise appear as isolated incidents.

## Triage & Response{% #triage--response %}

- Examine the JA3 hash value `{{@x-cs-ssl-ja3}}` against known threat intelligence sources to determine if it has been associated with malicious activity.
- Identify all client IP addresses where this JA3 hash was observed and determine if they belong to authorized systems or user devices in your environment.
- Review the destination domains and URLs accessed by connections using this JA3 fingerprint to assess whether the traffic patterns are legitimate.
- Check if the affected client systems share common software installations, security tools, or deployment configurations that would explain the identical fingerprint.
- Investigate recent user activity and application usage on systems associated with the identified client IPs to identify potential malware or unauthorized tools.
