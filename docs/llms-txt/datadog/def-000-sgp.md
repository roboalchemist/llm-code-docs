# Source: https://docs.datadoghq.com/security/default_rules/def-000-sgp.md

---
title: Cisco Meraki organization appliance security IDS events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Meraki organization appliance
  security IDS events
---

# Cisco Meraki organization appliance security IDS events
Classification:attack 
## Goal{% #goal %}

Detect when intrustion detection system (IDS) alerts are created by the Meraki MX Security Appliance.

## Strategy{% #strategy %}

The Cisco Meraki MX Security Appliance [threat protection](https://documentation.meraki.com/MX/Content_Filtering_and_Threat_Protection/Threat_Protection) is comprised of the Sourcefire SNORT intrusion detection engine and anti-malware technology. Advanced malware prevention (AMP) inspects HTTP file downloads through the MX Security Appliance and blocks or allows file downloads based on threat intelligence retrieved from the AMP cloud. The intrusion detection engine monitors the network to detect malicious or anomalous behaviours, and then raises an alert. The security appliance can also be used as an Intrusion Prevention System (IPS) blocking malicious packets.

**Note:** This detection filters for IDS alerts.

## Triage and response{% #triage-and-response %}

1. Investigate the SNORT alert to determine if it is malicious or benign:
   - Have the malicious packets been blocked `@blocked:true`?
   - Are there other security signals related to the affected internal host?
   - Does the internal host run the affected technology specified in the SNORT alert.
1. If it is determined to be benign, consider including an attribute in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If it is determined to be malicious, begin your organization's incident response process and investigate.
