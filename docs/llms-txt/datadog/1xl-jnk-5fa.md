# Source: https://docs.datadoghq.com/security/default_rules/1xl-jnk-5fa.md

---
title: The default network access rule for Storage Accounts should be set to deny
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The default network access rule for
  Storage Accounts should be set to deny
---

# The default network access rule for Storage Accounts should be set to deny
 
## Description{% #description %}

Configure storage accounts to deny access to traffic from all networks (including internet traffic). Grant access to traffic from specific Azure Virtual networks, allowing a secure network boundary for specific applications to be built. Access can also be granted to public internet IP address ranges, to enable connections from specific internet or on-premises clients. When network rules are configured, only applications from allowed networks can access a storage account. When calling from an allowed network, applications continue to require proper authorization (a valid access key or SAS token) to access the storage account.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Storage Accounts**.
1. For each storage account, click on the **Networking** blade.
1. Click the **Firewalls and virtual networks** heading.
1. Ensure that you have elected to **allow access from Selected networks**.
1. Add rules to allow traffic from specific networks and click **Save** to apply your changes.
