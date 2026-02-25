# Source: https://docs.datadoghq.com/security/default_rules/em5-2ya-8se.md

---
title: Azure disk export URI created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure disk export URI created
---

# Azure disk export URI created
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1074-data-staged](https://attack.mitre.org/techniques/T1074)
## Goal{% #goal %}

Detect when an Azure disk is successfully exported. Export URLs generated in Azure are accessible to anyone with the URI. This could be utilized as an exfiltration method that would allow an attacker to download an Azure Compute VM's disk as a VHD file.

## Strategy{% #strategy %}

Monitor Azure logs where `@evt.name` is `"MICROSOFT.COMPUTE/DISKS/BEGINGETACCESS/ACTION"` and `@evt.outcome` is `Success`.

## Triage and response{% #triage-and-response %}

1. Verify the disk (`{{@resourceId}}`) has a legitimate reason for being exported.
1. If the activity is not expected, investigate the activity around the IP (`{{@network.client.ip}}`) creating the export URI.

## Changelog{% #changelog %}

2 November 2022 - Updated strategy.
