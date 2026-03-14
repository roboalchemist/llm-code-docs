# Source: https://docs.acceldata.io/documentation/alerts.md

# Alerts

The **Alerts page** in ADOC is your central hub for tracking issues across pipelines, compute, and data reliability. An **alert** is automatically generated whenever a monitoring rule or policy condition is breached. These alerts allow you to catch problems early, before they impact operations, budgets, or decision-making.

By reviewing alerts, you can:

- Detect pipeline failures or performance slowdowns in real time.
- Identify data quality issues such as missing values, schema changes, or anomalies.
- Monitor compute usage and costs to avoid overruns.
- Maintain a complete audit trail of all issues across your environment.

## Alerts vs Notifications

While closely related, alerts and notifications serve different purposes in ADOC:

- **Alert**:
    - An event created every time a rule is triggered.
    - Logged in ADOC to ensure a full audit trail.
    - **Examples**: A pipeline fails, sales data arrives late, or compute costs exceed budget.

- **Notification**:
    - The message that informs you about an alert.
    - Delivered via Slack, Teams, email, or other channels.
    - Configurable—so you can choose when and how often you’re notified.
    - **Example**: “Notify me only the first time a freshness policy fails.”

This separation ensures that all issues are tracked, but teams only get the right notifications at the right time, reducing noise while improving accountability.

## How Alerts are Created in ADOC

You don’t create alerts directly. Alerts are **automatically generated** whenever a monitoring rule or policy condition is breached. This could be from:

- **Policies** (data quality, freshness, anomaly, drift, reconciliation)
- **Pipelines** (failures, SLA breaches, long runtimes)
- **Compute/Budgets** (cost thresholds, warehouse usage, suspend times)

## Example: Creating a Data Quality Alert

1. Go to **Data Reliability &gt; Manage Policies** and click **Add New**.
2. Choose **Data Quality** and set up your rule (e.g., `email IS NOT NULL`).
3. In the **Alerts & Notifications** step:
    1. Pick a severity level (Critical, High, Medium, Low).
    2. Choose a Notification Group (e.g., Slack, Teams, Email).

4. Save the policy and run it. If the rule fails, ADOC creates an alert and sends a notification to your chosen channel.

## Types of Alerts

ADOC generates alerts across three key domains:

- **Pipeline Alerts**
    - Track execution and performance of pipelines.
    - **Example**: Alerts for failed jobs, long runtimes, or critical errors.

- **Reliability Alerts**
    - Triggered by Data Reliability policies to ensure trustworthy data.
    - **Example**: Alerts for duplicate rows, missing values, or unusual statistical patterns.

- **Compute Alerts**
    - Monitor usage, health, and costs of compute environments.
    - **Example**: Alerts for warehouse suspends, high resource utilization, or budget threshold breaches.

## Alert Lifecycle

Each alert progresses through a lifecycle, indicated by its **status**. Understanding these statuses helps your team coordinate effectively and maintain accountability.

| **Status** | **Description** | **How It's Set** | 
| ---- | ---- | ---- | 
| Open | Default state of a newly generated alert. The issue has been detected but not yet reviewed. | Automatically when a monitoring condition is breached. | 
| Acknowledged | Indicates the alert has been reviewed and assigned for follow-up. | Manually by a user. | 
| In Progress | Work to investigate or resolve the issue is actively underway. | Manually by a user. | 
| Dismissed | The alert does not require action (e.g., known issue, low priority, or automatically cleared after a monitor update). | Manually by a user, or automatically by ADOC if the parent monitor changes. | 
| Resolved | The issue has been fixed or the condition is no longer met. | Automatically if the monitor rerun succeeds, or manually by a user once a fix is applied. | 


## Alert Lists

The **Listing** tab on the Alerts page provides a complete, filterable table of all alerts generated in ADOC. This is your central workspace for investigating, assigning, and managing alerts.

### Finding and Filtering Alerts

The toolbar at the top of the page makes it easy to narrow down alerts and focus on what matters most:

| **Filter** | **Description** | **Example** | 
| ---- | ---- | ---- | 
| Date Range | By default, alerts from the last 7 days are shown. Click the calendar icon to adjust the time frame. | Last 30 days | 
| Datasource | Limit alerts to a specific data source. | Snowflake, MongoDB | 
| Type | Filter by where the alert originated. | Pipeline, Compute, Reliability | 
| Status | Show alerts by lifecycle state. | Show only alerts in a certain state, such as _Open_ or _Resolved_. | 
| Severity | Focus on alerts by priority level. | Critical, High, Medium, Low | 
| Assignee | View alerts assigned to a particular user. | User A | 
| Search | Find alerts by name. | “ETL Failure” | 
| Refresh | Reload alerts with latest data without clearing filters. |  | 
| Reset | Clear all filters and return to default view. | Default 7-day view | 


### Alerts List Details

Each row in the Alerts List represents a single alert, providing quick visibility into its context:

| **Column** | **Description** | 
| ---- | ---- | 
| Name | The alert name, often tied to the policy or pipeline that generated it. | 
| Severity | Assigned impact level (Critical, High, Medium, Low). | 
| Type | The alert’s category (e.g., Pipeline, Reliability, Compute). | 
| Status | Where the alert is in its lifecycle (Open or Resolved). | 
| Raised | Date and time the alert was first triggered. | 
| Tags | Any custom tags used for categorization. | 
| Occurrence Count | How many times the same alert has been triggered. | 
| Assignee | The user or team responsible for resolving it. | 
| Updated By | The user who last changed the alert’s state. | 
| Last Updated At | Timestamp of the most recent change. | 
