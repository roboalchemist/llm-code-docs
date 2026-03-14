# Source: https://docs.acceldata.io/documentation/managing-alerts.md

# Manage Alerts

Once you understand how alerts are generated, the next step is learning how to **work with them effectively**. ADOC provides tools to help you quickly assess, prioritize, and resolve alerts, whether individually or in bulk.

## 1. Managing Alerts in Bulk

When you need to act on multiple alerts at once, bulk actions streamline the process.

| **Step** | **Action** | **Notes** | 
| ---- | ---- | ---- | 
| **1** | Select alerts | Use the checkboxes next to each alert in the list. To select all visible alerts, use the global checkbox at the top. | 
| **2** | Choose an action | A bulk action bar appears at the top once alerts are selected. | 
| **3** | Apply changes | Options include: \n\n\n\n**Change Status** (Acknowledge, In Progress, Dismiss), requires a comment for the audit trail. \n\n\n\n**Change Severity** (Critical, High, Medium, Low). \n\n\n\n**Assign Alerts** to a user for investigation. | 


Bulk actions are useful for clearing large volumes of low-priority alerts, or for assigning related issues to the same owner.

## 2. Investigating a Single Alert

For critical or recurring issues, you’ll want to drill into the details of a specific alert.

| Step | Action | What You’ll See | 
| ---- | ---- | ---- | 
| **1** | Click the **Alert Name** in the list | Opens the **Alert Details** page. | 
| **2** | Review the **Overview tab** | Key details: what triggered the alert, execution summary, impacted assets, and related links (e.g., to Pipeline Details). | 
| **3** | Explore the **Lineage tab** | Visual graph showing upstream dependencies and downstream impact. | 
| **4** | Check the **History tab** | Log of past occurrences, scores, and reasons for closure. Useful for spotting recurring issues. | 


## 3. Taking Action on an Alert

At the top of the Alert Details page, the **action bar** gives you direct controls to manage the alert’s lifecycle:

| **Action** | **Purpose** | **Example** | 
| ---- | ---- | ---- | 
| **Assign** | Delegate ownership to a specific user | Assign a pipeline failure alert to the Data Engineering team | 
| **Update Status** | Track lifecycle stage | Move from _Open → In Progress_ | 
| **Change Severity** | Adjust impact level | Downgrade from Critical to Medium after triage | 
| **Snooze** | Pause notifications temporarily | Silence a recurring alert for 24 hours | 
| **Feedback** | Mark alert as relevant/irrelevant | Helps ADOC improve recommendations | 
| **View Monitor** | Jump to the monitor that generated the alert | Go straight to Pipeline Monitor for debugging | 


## 4. Monitoring Trends in the Alerts Dashboard

Individual alerts tell you what happened, but the **Alerts Dashboard** shows you patterns and trends across your entire data environment.

| Dashboard Element | Description | Use Case | 
| ---- | ---- | ---- | 
| **Summary Metrics** | Active vs. total alerts\n\nActive vs. total policies | See overall environment health at a glance | 
| **Severity Trend** | Stacked area chart of alerts over time by severity | Spot spikes in Critical alerts | 
| **Status Trend** | Alerts over time by status (Open, In Progress, Resolved) | Measure how quickly teams respond and resolve issues | 
| **Datasource Breakdown** | Bar chart of alerts by datasource, segmented by severity | Identify which systems are most error-prone | 


The dashboard helps you prioritize effort, for example, focusing first on a datasource generating the highest number of Critical alerts.