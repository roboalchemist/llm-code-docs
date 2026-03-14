# Source: https://docs.acceldata.io/documentation/reliability-reports.md

# Reliability Reports

Before you create a report, you need to have **data reliability policies**—such as **Data Quality, Reconciliation, Schema Drift, Freshness, or Data Anomaly**—already applied to your data sources. These policies generate the reliability scores, execution results, and trends that reports summarize and share.

**Data Reliability Reports** are the next step in the workflow: they bring together the results of those policies so you can:

- Track how your data reliability changes over time.
- Compare assets, databases, or sources based on their reliability scores.
- Show where policies are failing or producing warnings.
- Share insights with business stakeholders through scheduled delivery.

For example, after setting up reconciliation and schema drift policies on a Snowflake warehouse, a data operations lead can create a monthly report to show:

- Overall reliability score trends.
- Policy execution breakdowns by type and status.
- A ranked list of assets with the lowest average scores.

## What you can do with reports

Reports go beyond one-time snapshots—they provide a **continuous view** of your data’s health and the policies governing it. With reports, you can:

- **Monitor reliability scores** over time, across different sources, tags, or dimensions.
- **Identify weak points** by reviewing which policies or rules fail most often.
- **Focus on what matters** by filtering by source type, data source, policy type, or business tags.
- **Communicate clearly** by scheduling automated delivery of reports to stakeholders via email, Slack, or Teams.
- **Show accountability** by branding reports with your organization’s name and logo.

For example, a data operations lead monitoring critical Snowflake sources might create a monthly report showing policy execution counts, reliability scores, and a ranked list of assets with the lowest scores. This enables the team to take targeted action and demonstrate measurable improvements.

### Reporting Service Behavior

Reliability Reports run on the Reporting Service, which governs scheduling, notification delivery, and permission enforcement.

- Reports created in version **26.1.0 or later** automatically follow the current scheduling behavior.
- Reports created in earlier versions begin scheduling under the current behavior after they are **edited and saved once**.
- No configuration changes are required beyond saving the report.

Note  If an existing report does not appear to run as expected, opening it and saving it ensures it follows the current scheduling behavior.

### Notification Delivery Support

Reliability Reports support delivery through Email, Slack, and Microsoft Teams.

- **Email delivery is available only for reports running on the current Reporting Service**.
- Reports created or updated after version 26.1.0 support Email delivery.
- Reports that have not been saved since upgrading do not deliver Email notifications.

Recommendation  If Email delivery is required, verify that the report has been saved after upgrade.

### Score Aggregation Methodology

You have flexibility in how **quality scores** are displayed by choosing between two scoring aggregation methods by navigating to **Settings &gt; Score Aggregation Methodology**:

- **Policy-Based Simple Averaging**: Asset scores are computed by averaging the scores of all policies under the asset.
- **Rule-Based Row Weighted Averaging**:
Asset scores are calculated using a row-weighted method (ignoring rule weights). The score is determined by dividing the total number of rows that passed validation by the total number of rows processed. When you select this method, the **Reporting** page provides two report types:
    - **Rules Report** – reliability at the rule level.
    - **Column Report** – reliability at the column level.

Scoring based on both the aggregation methods are precomputed —the setting only controls which version is shown in reports. This means you can choose the scoring approach that best reflects your business needs.

## Permissions for Viewing and Managing Reports

### Required Permissions

Access to Reliability Reports is governed by both **Domain roles** and **Tenant roles**.

**Domain Role Permissions**

| **Capability Area** | **Permission** | 
| ---- | ---- | 
| Asset Management | Asset Management – **View** | 
| Asset Metadata | Asset Metadata – **View** | 
| Policies | **View** | 
| Reports | Report Management – **View** | 


**Tenant Role Permissions**

| **Capability Area** | **Permission** | 
| ---- | ---- | 
| General | DataSource – **View** | 
| Infrastructure | Resource Groups Management – **View** | 
| Reliability | Reliability Reports – **Create** | 
| Reliability | Data Reliability Settings – **View** | 


Note Users must meet both Domain and Tenant permission requirements to view or create Reliability Reports.

### Operational Guidance

- Review existing reports after platform upgrades and save them once to align with current scheduling behavior.
- Confirm notification channels, especially when Email delivery is required.
- Verify permissions if reports are visible but contain no data.

## How to create, schedule and deliver reports

### 1. Create a report

- Decide the scoring aggregation method (simple average or row-weighted).
- Apply filters (such as time range, source type, tags, or policy type) to focus on the data you care about.
- Save the report with a clear name and optional description.

Warning Deleting a widget is permanent. You cannot recover it, and you will need to create a new report from scratch.

### 2. Schedule the report

- Choose how often the report should run (daily, weekly, monthly).
- Set the time zone and preferred times.
- Add multiple execution times if needed.

### 3. Deliver the report

- Select notification channels. For information on how to create a notification channel, refer to this @Notif
- Share with individuals, groups, or distribution lists.
- Confirm delivery so stakeholders automatically receive updates.

### 4. Brand the report (optional)

- Add your organization’s name and logo in **Settings &gt; Report Configuration**.
- Ensure all distributed reports reflect your brand identity.

## Best practices

- Use **Watched assets** to focus on critical objects
- Group by **Policy type** to isolate issues such as Schema Drift
- Compare **high and low scores** to identify unstable periods
- Sort the **Assets table** to find assets with the lowest scores or highest execution volume

## Next steps

With reports, you can:

- Track reliability trends
- Measure policy coverage
- Identify weak assets
- Automate delivery to stakeholders

This ensures your organization treats data reliability as a **measurable, visible, and shared responsibility**.