# Source: https://docs.datadoghq.com/cloud_cost_management/reporting/scheduled_reports.md

---
title: Scheduled Reports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloud Cost Management > Cost Reports > Scheduled Reports
source_url: https://docs.datadoghq.com/reporting/scheduled_reports/index.html
---

# Scheduled Reports

## Overview{% #overview %}

Scheduled Cloud Cost (CCM) Reports let you automatically receive recurring cost reports through email or Slack. This feature supports finance, engineering, and executive stakeholders by delivering periodic snapshots of cost metrics, without needing to log into the Datadog platform. Reports are sent as PDFs to your chosen Slack channels or email addresses.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/cost_reports/cloud-cost-scheduled-report-1.2158eb6d7a4f627c1dbaec778926826b.png?auto=format"
   alt="Schedule Cost Report." /%}

Below is an example of a report sent to a Slack channel.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/cost_reports/cost-report-slack-1.2a6b3bd0b7576efac45f37b9eb2aafb2.png?auto=format"
   alt="A report that has been sent to a Slack channel based on a schedule" /%}

For emails, the report PDF is included as an email attachment and/or as a link, depending on its size.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/cost_reports/cost-report-email.d1acc8dccd4f95511cb2b983d58cd8de.png?auto=format"
   alt="A report that has been sent as an email based on a schedule" /%}

## Schedule a CCM report{% #schedule-a-ccm-report %}

1. Go to [**Cloud Cost > Analyze > Reports**](https://app.datadoghq.com/cost/analyze/reports) in Datadog.

1. [Create a report](https://docs.datadoghq.com/cloud_cost_management/reporting) or select an existing report.

1. Click **Share**, then **Schedule Report**.

   {% image
      source="https://datadog-docs.imgix.net/images/cloud_cost/cost_reports/share_scheduled_report-1.65f5c28c9dbd75c684b34892d60bfa67.png?auto=format"
      alt="Click the Share button and Schedule Report on an individual report page." /%}



1. In the configuration modal that opens:

   - Set your schedule (when and how often the report should be sent)
   - Enter a title for your schedule

1. Add recipients:

   - **Email recipients**: Enter email addresses. Your Datadog account is automatically added, but you can remove it by hovering over it and clicking the trash icon.

**Note:** Enterprise and Pro accounts can send reports to recipients outside of their organizations. You can control which email domains are able to receive reports by configuring your [domain allowlist](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist/).

   - **Slack recipients**: Select your Slack workspace and channel from the dropdowns. If no workspaces appear, make sure you have the Datadog [Slack Integration](https://docs.datadoghq.com/cloud_cost_management/reporting) installed. All public channels within the Slack workspace are listed automatically. For private channels, invite the Datadog Slack bot first. You can test the connection by clicking the **Send Test Message** button.

## Managing schedules{% #managing-schedules %}

A single Cloud Cost (CCM) Report can have multiple schedules with different settings, allowing you to inform different stakeholder groups interested in the same cost data. To view existing schedules, click **Share** and select **Manage Schedules**.

From the configuration modal that opens, you can:

- Pause existing schedules
- Create new schedules
- Edit schedule details
- Delete schedules

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/cost_reports/manage-cost-report-schedules-2.391bf419df7113183d3f3cc96550c746.png?auto=format"
   alt="Manage a Cost Report's Schedule." /%}

## Viewing schedules{% #viewing-schedules %}

To see all Cloud Cost (CCM) Report schedules across your organization:

1. Navigate to [**Cloud Cost > Analyze > Reports**](https://app.datadoghq.com/cost/analyze/reports) and click the **Report Schedules** tab.
1. Use the "My schedules" toggle to switch between your personal schedules and all organization schedules.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/cost_reports/cost-report-schedules-view-4.e931a34254fcfd25bc00cacbb1b8a462.png?auto=format"
   alt="View all Cost Report Schedules." /%}

## Permissions{% #permissions %}

| Action                       | Required Permission                                                     |
| ---------------------------- | ----------------------------------------------------------------------- |
| View schedules               | Cloud Cost Report Schedules Write OR Cloud Cost Report Schedules Manage |
| Create/modify your schedules | Cloud Cost Report Schedules Write OR Cloud Cost Report Schedules Manage |
| Modify others' schedules     | Cloud Cost Report Schedules Manage                                      |

After a report is created, you can subscribe, unsubscribe, edit schedules, and delete reports (assuming you have the appropriate permissions). **Note:** Only Datadog users can unsubscribe directly from the email. External recipients (including group email addresses) must contact the report schedule owner to unsubscribe, as Datadog cannot distinguish between group emails and individual external emails.

## Further reading{% #further-reading %}

- [Learn about Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
- [Learn about scheduled dashboard reports](https://docs.datadoghq.com/dashboards/sharing/scheduled_reports)
