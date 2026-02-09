# Source: https://docs.datadoghq.com/security/default_rules/def-000-ma8.md

---
title: >-
  Storage containers storing activity logs should only be accessible by
  authorized personnel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Storage containers storing activity
  logs should only be accessible by authorized personnel
---

# Storage containers storing activity logs should only be accessible by authorized personnel
 
## Description{% #description %}

Storage account containers containing activity log exports should not be publicly accessible. Allowing public access to activity log content may help an adversary identify weaknesses in the affected account's usage or configuration.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Search for **Storage Accounts** in the Azure Portal.
1. Click on the storage account name.
1. Click **Configuration** under **Settings**.
1. Select **Enabled** under **Allow Blob public access**.
1. Click **Containers** under **Data Storage** on the side panel.
1. Select the `insights-activity-logs` container.
1. Click **Change access level** and set it to **Private (no anonymous access)**, then click **OK**.
