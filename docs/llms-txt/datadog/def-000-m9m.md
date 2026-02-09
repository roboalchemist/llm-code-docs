# Source: https://docs.datadoghq.com/security/default_rules/def-000-m9m.md

---
title: Microsoft Defender for Cloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Microsoft Defender for Cloud
---

# Microsoft Defender for Cloud
Classification:attack 
## Goal{% #goal %}

Detect when [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) raises an alert.

## Strategy{% #strategy %}

Defender for Cloud collects, analyzes, and integrates log data from your Azure, hybrid, and multicloud resources, the network, and connected partner solutions, such as firewalls and endpoint agents. Defender for Cloud uses the log data to detect real threats and reduce false positives. A list of prioritized security alerts is shown in Defender for Cloud, along with the information you need to quickly investigate the problem and take steps to remediate an attack.

Microsoft provides an [alert reference guide](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-reference) for understanding each type of alert generated.

## Triage and response{% #triage-and-response %}

1. Investigate the Microsoft Defender for Cloud alert to determine if it is malicious or benign.
1. If the finding is deemed malicious, follow the [remediation guidance](https://learn.microsoft.com/en-us/azure/defender-for-cloud/managing-and-responding-alerts) provided by Microsoft and also any internal incident response processes.
1. A [suppression rule](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-suppression-rules) can be created to manage noisy or false positive alerts.
