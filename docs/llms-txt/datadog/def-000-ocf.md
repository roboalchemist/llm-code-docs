# Source: https://docs.datadoghq.com/security/default_rules/def-000-ocf.md

---
title: Commercial vulnerability scanner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Commercial vulnerability scanner
---

# Commercial vulnerability scanner
Tactic:[TA0043-reconnaissance](https://attack.mitre.org/tactics/TA0043)Technique:[T1595-active-scanning](https://attack.mitre.org/techniques/T1595) 
### Goal{% #goal %}

Detects when a commercial vulnerability scanner is performing a scan against your services.

### Strategy{% #strategy %}

The detection rule leverages fingerprints from known security companies to identify activity as a commercial scanner.

The signal is set to `LOW` severity as the occurrence of spoofing commercial vulnerability scanners is rare, but possible. Detection results from authorized vulnerability scans are typically shared with the customer directly from the vendor or vulnerability management team.

### Triage and response{% #triage-and-response %}

Validate that the commercial vulnerability scanner is authorized to scan your systems and the scans are originating from an expected source IP address. Many commercial scans originate from a source IP address published by the vendor.

If the scan is not authorized:

1. Block the attacking IP(s) temporarily to limit vulnerability discovery and service load.
1. If the scans are originating from a vendor published source IP address, reach out to the vendor to determine the cause of the scan.
