# Source: https://docs.datadoghq.com/security/default_rules/mpx-tee-gng.md

---
title: '''Trusted Microsoft Services'' should be enabled for Storage Account access'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Trusted Microsoft Services' should be
  enabled for Storage Account access
---

# 'Trusted Microsoft Services' should be enabled for Storage Account access

## Description{% #description %}

Enabling firewall rules for a storage account restricts incoming data requests, including those from other Azure services, such as using the portal or writing logs. However, by enabling Trusted Microsoft Services through exceptions, you can regain access to services like Monitor, Networking, Hubs, and Event Grid. Additionally, this exception allows for backing up and restoring virtual machines using unmanaged disks in storage accounts with network rules applied. To ensure smooth operation of these services, it is recommended to enable the exception for Trusted Microsoft Services.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Storage Accounts**
1. For each storage account, click on the **settings** menu called **Firewalls and Virtual Networks**.
1. Ensure that **Allow access from selected networks** is `enabled`.
1. Enable **Allow trusted Microsoft services to access this storage account**.
1. Click **Save** to apply your changes.
