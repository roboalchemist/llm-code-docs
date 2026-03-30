# Source: https://docs.acceldata.io/documentation/policy-evaluation-usage.md

# Policy Evaluation Usage

Policy Evaluations (PE) Usage helps you understand how often governance policies run in your environment. Each time a policy rule runs successfully on your data, it generates Policy Evaluations (PEs). 

PE Usage:

- Shows how frequently policies are executed
- Helps you monitor governance activity
- Forms the basis for usage-based billing

The PE Usage page provides a clear view of how PEs are consumed across time and policy types.

## What Is a Policy Evaluation (PE)?

A **Policy Evaluation (PE)** is recorded when: **One rule runs successfully on one data entity.**

### What is a data entity?

A data entity is the smallest unit a policy evaluates. It can be:

- A row in a database table or file
- A record in a stream or queue
- An element in a pipeline

## How PE Counting Works

PEs are calculated using simple rules:

| Rules | Examples | 
| ---- | ---- | 
| **One rule × one data entity = one PE** | If one rule runs on 10 million rows → **10 million PEs** | 
| **Multiple rules are counted separately** | If 3 rules run on 1 row → **3 PEs**\n\n\n\nIf 3 rules run on 1,000 rows → **3,000 PEs** | 
| **Each execution is counted** | If a policy runs multiple times (for example, in scheduled pipelines), each successful run generates PEs. | 
| **Only successful executions are counted** | PEs are recorded only when a policy executes successfully — regardless of whether the result is pass or fail.\n\n\n\nIf a policy fails to execute, no PEs are counted. | 


## PE Calculation by Policy Type

| **Policy Type** | **How PEs are Calculated** | 
| ---- | ---- | 
| **Data Quality** | Rows scanned × Number of rules | 
| **Reconciliation - Row Count** | 1 PE per execution | 
| **Reconciliation - Equality** | Rows scanned × Number of rules | 
| **Data Cadence (Freshness)** | Number of rules | 
| **Data Drift** | Rows profiled × Number of rules | 
| **Data Anomaly** | Rows profiled × Number of selected columns | 
| **Schema Drift** | 1 PE per execution | 
| **Composite** | Counted within Data Quality rules | 
| **Auto Anomaly** | Rows scanned | 
| **Pipeline Policy** | 1 PE per execution | 


## Why PE Usage Matters?

PE Usage helps you:

- **Understand Your Usage**: See exactly how often policies run and how many PEs are generated.
- **Monitor Governance Activity**: Track enforcement across datasets, pipelines, and systems.
- **Forecast and Manage Costs**: Since billing is based on PEs, usage visibility helps you plan and optimize.
- **Reconcile Billing with Activity**: Match PE consumption with actual policy execution patterns.

## Accessing PE Usage Page

To access the **PE Usage** page:

1. Navigate to the **Settings** page from the main navigation menu.
2. Select **PE Usage** under the **Usage** category.

## Understanding the PE Usage Page

The PE Usage page includes the following sections:

### Usage By Time

The **Usage By Time** chart shows PE consumption for the selected time range.

You can select:

- Weekly
- Monthly
- Yearly
- Custom

To compare periods (for example, this week vs. last week), enable the **Day Over Day** option. This allows you to compare the current period with the previous period.

### Total PE Consumed

The **Total PE Consumed** section displays:

- The total number of PEs used
- The percentage increase or decrease compared to the previous period

This gives a quick summary of overall usage trends.

### Breakdown by Type

The **Breakdown by Type** table shows PE consumption by policy type for the selected time period.

Each row includes:

- Policy Type
- PE Usage
- Percentage of Total Usage
- Trend (last 7 days)

This helps identify which policy types contribute most to PE consumption.

### Download Audit Report

You can download a summary of PE usage as a PDF.

The **Audit Report** includes:

- Total PEs consumed during the selected date range
- A summary of policy activity

To download:

1. Click **Audit Report**.
2. Select a **From** date and a **To** date.
3. Click **Download PDF**. The PDF is download to your system.

## FAQs

**Q: Does each rule within a policy count as a separate PE?** 

**A: Yes**. PEs are calculated based on:

- The number of rules
- The number of data entities processed

Example:
If a policy has 3 rules and scans 1,000 rows → **3,000 PEs**

**Q: Are PEs counted if a policy fails to execute?** 

**A: No**. Only successful policy executions generate PEs.

**Q: Can I export PE usage data?** 

**A: Yes**. You can download a PDF report using the **Audit Report** button.

## Optimizing PE Usage

To manage and optimize PE consumption:

- Review the number of rules in your policies
- Limit large-scale scans when not necessary
- Avoid redundant or overlapping policies
- Review scheduled policy frequency

Monitoring the **Breakdown by Type** table can help identify high-usage policy categories.