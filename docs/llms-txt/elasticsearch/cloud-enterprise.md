# Source: https://www.elastic.co/docs/troubleshoot/deployments/cloud-enterprise/cloud-enterprise

﻿---
title: Troubleshoot Elastic Cloud Enterprise
description: When you first install Elastic Cloud Enterprise and log into the Cloud UI, three system deployments are already in place. After creating your first deployments,...
url: https://www.elastic.co/docs/troubleshoot/deployments/cloud-enterprise/cloud-enterprise
products:
  - Elastic Cloud Enterprise
applies_to:
  - Elastic Cloud Enterprise: Generally available
---

# Troubleshoot Elastic Cloud Enterprise
## Finding deployments

When you first install Elastic Cloud Enterprise and [log into the Cloud UI](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/log-into-cloud-ui), three [system deployments](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/system-deployments-configuration) are already in place. After [creating your first deployments](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/create-deployment), you may still be managing only a few. But in a production environment with hundreds or even thousands of deployments, identifying those that require attention becomes critical.
The **Deployments** page in the Cloud UI provides several ways to find deployments that might need your attention, whether you’re troubleshooting, planning upgrades, or performing routine maintenance. You can:
- Use the visual indicators to review the health of your deployments at a glance.
- Search by full or partial deployment names or IDs.
- Use the **Health** and **Version** dropdown filters to narrow the list of deployments shown. These filters help you find deployments by version, configuration status, or other attributes, making it easier to identify those that require upgrades, are undergoing changes, or match specific operational criteria.

<admonition title="Simplify monitoring with AutoOps">
  AutoOps is a monitoring tool that simplifies cluster management through performance recommendations, resource utilization visibility, and real-time issue detection with resolution paths. Learn more about [AutoOps](https://www.elastic.co/docs/deploy-manage/monitor/autoops).
</admonition>