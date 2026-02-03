# Source: https://docs.datadoghq.com/security/cloud_siem/guide/oci-config-guide-for-cloud-siem.md

---
title: OCI Configuration Guide for Cloud SIEM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Cloud SIEM Guides > OCI Configuration
  Guide for Cloud SIEM
---

# OCI Configuration Guide for Cloud SIEM

## Overview{% #overview %}

Cloud SIEM applies detection rules to all processed logs in Datadog to detect threats such as targeted attacks, communication with threat intel-listed IPs, or insecure resource modifications. Detected threats are surfaced as Security Signals in the Security Signals Explorer for triage.

This guide walks you through the following steps to start detecting threats with your OCI Audit logs:

1. Set up Datadog's OCI integration
1. Enable log collection
1. Use Cloud SIEM to triage Security Signals

## Set up Datadog's OCI integration{% #set-up-datadogs-oci-integration %}

Set up Datadog's [OCI integration](https://docs.datadoghq.com/integrations/oracle-cloud-infrastructure/?tab=createvcnrecommended) using either the QuickStart (recommended) or the Terraform method.

## Enable log collection{% #enable-log-collection %}

Ensure that log collection is enabled in the Datadog OCI integration tile:

{% image
   source="https://datadog-docs.imgix.net/images/security/cloud_siem/guide/oci_config_guide/oci_logs_enabled.c1302cd79347aadee5549b396f646a09.png?auto=format"
   alt="The OCI integration tile in Datadog with log collection enabled" /%}

## Use Cloud SIEM to triage Security Signals{% #use-cloud-siem-to-triage-security-signals %}

Cloud SIEM applies out-of-the-box detection rules to all processed logs, including your OCI Audit logs. When a threat is detected with a detection rule, a Security Signal is generated and can be viewed in the Security Signals Explorer.

- Go to the [Cloud SIEM Signals Explorer](https://app.datadoghq.com/security/siem/signals) to view and triage threats. See [Investigate Security Signals](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals/) for further details.
- See [out-of-the-box detection rules](https://docs.datadoghq.com/security/default_rules/#cat-cloud-siem) that are applied to your logs.
- [Create rules](https://docs.datadoghq.com/security/detection_rules/#create-detection-rules) to detect threats that match your specific use case.

## Further reading{% #further-reading %}

- [Explore Cloud SIEM default detection rules](https://docs.datadoghq.com/security/default_rules/#cat-cloud-siem-log-detection)
- [Learn about the Security Signals Explorer](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals)
- [Create new detection rules](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/)
