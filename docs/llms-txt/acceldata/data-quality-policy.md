# Source: https://docs.acceldata.io/documentation/data-quality-policy.md

# Data Quality Policy

**Data Quality** policies validate your data against predefined quality rules to ensure accuracy, completeness, and consistency. These policies check individual data points to identify good and bad records based on the rules you define.

- A **policy** is a set of [rules](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/rules-and-rulesets) that define your expectations for a dataset.
- A **rule** is a specific condition or check that must be met for the data to be considered “good.” Each rule focuses on a particular aspect of data quality, such as **null values, data type consistency, value ranges, uniqueness, or patterns**.

**When to use it?**

Use Data Quality policies when you need to:

- Ensure customer data completeness before sending to downstream systems
- Validate that financial transaction amounts fall within expected ranges
- Check that email addresses and phone numbers follow proper formats
- Identify null values in critical columns like customer IDs or order numbers
- Enforce business rules like "order dates cannot be in the future"

## Creating a Data Quality Policy

### 1. Start Policy Creation

You can create a Data Quality Policy in **two main ways**: via **Manage Policies** or via the **Asset Details page**.

#### Option 1: Through Manage Policies

1. Navigate to **Data Reliability &gt; Manage Policies** from the left menu.
2. Click **Add Policy** (top-right).
3. Select **Data Quality** as the policy type.
4. Choose the dataset(s) (assets) you want to monitor.
5. The **Create Data Quality Policy** page opens for configuration.

#### Option 2: Through the Asset Details Page

There are **two ways to start a Data Quality Policy from the Asset Details page**:

**Overview Tab**

1. Open the dataset in the **Asset Details page**.
2. In the **Overview tab**, click the **Actions button** and select **Add Data Quality Policy**.

**Policies Tab**

1. Navigate to the **Policies tab** in the Asset Details page.
2. Click **Add Policy** or use the **Actions button**, then select **Data Quality**.

In both cases, the **Create Data Quality Policy** page opens for configuration.

### 2. Configure Data Selection

Before defining rules, ADOC must know which part of the dataset needs to be evaluated. There are two ways to select data:

#### 1. Column-Based Selection

- Select one or more columns directly from the dataset.
- ADOC will apply rules only to these selected columns.
- Best for simple checks or when you only need to monitor specific fields.

#### 2. SQL-Based Selection

- Enter a custom SQL query to define the data subset.
- Use the placeholders:
    - `{{{lower_bound}}}` : replaced with the starting value for incremental or selective runs.
    - `{{{upper_bound}}}` : replaced with the ending value for incremental or selective runs.

- Click **Validate** to check that your query is correct before proceeding.

Note

- If using Native SQL (checkbox unchecked), follow the syntax of your underlying data platform (Snowflake, BigQuery, etc.), which may differ from Spark SQL.
- Some incremental features require that the column being incremented is included in the query’s SELECT statement.
- Older Dataplane versions may not support placeholders in SQL; upgrade to **ADOC** **v4.3.0** or later if needed.

### 3. Choose Execution Engine

- **Spark (default)**: Runs jobs in ADOC’s Spark engine. Good for standard profiling and complex rule execution.
- **Pushdown**: Lets queries run directly on the data source, reducing data movement. Best for very large datasets.

Important

- Some incremental or advanced options (like certain segment selections) are only available depending on the data engine selected.
- If Pushdown is selected, **persistence of records** and some Spark job settings are disabled.

### Example

- **Column-Based**: Monitor `customer_email` for null values.
- **SQL-Based**: `SELECT customer_id, email, signup_date FROM customers WHERE signup_date >= {{{lower_bound}}} AND signup_date < {{{upper_bound}}}`

### Real-world Use Case

**Scenario**: Your sales reporting dashboard is showing incorrect revenue figures. After investigation, you discover that the sales data contains future dates in the transaction date column, causing inaccurate monthly aggregations.

**Solution**: Create a Data Quality policy with a range check rule to ensure all transaction dates are between the earliest valid date and today's date, preventing future dates from entering your analytics pipeline.

#### Step-by-step Guide

**Step 1: Configure your data source**

1. Navigate to the asset you want to monitor (e.g., your sales transactions table)
2. Click the **Actions** button and select **Create Policy**
3. Choose **Data Quality Policy**
4. Select your execution engine:
    1. **Spark Engine**: Best for complex transformations and when you need to persist good/bad records
    2. **Pushdown Engine**: Faster for simple checks, processes data directly in your source database

**Step 2: Select and filter your data**

- **Standard selection**: Choose your table directly
- **Custom SQL**: Write custom queries if you need to join tables or apply complex filters
- **Apply filters**: Narrow down data (e.g., only check records from the last 7 days)
- **Use segments**: Analyze specific portions of your data (e.g., check quality by region)

**Step 3: Configure quality rules**

Choose the [rules](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy#configure-rules) that match your business needs.

**For each rule, you can:**

- Set absolute threshold values (e.g., between 100 and 1000)
- Compare against historical trends (e.g., "increases by 5% compared to last 5 days")
- Use anomaly detection with sensitivity levels (low, medium, high)

**Step 4: Set success threshold**s

- **Success Threshold**: The minimum score (0-100) for the policy to pass (e.g., 95%)
- **Warning Threshold**:The score that triggers a warning (e.g., 85%)
- **Policy passes only if**: All rules meet their individual thresholds

**Step 5: Configure alerts (optional but recommended)**

1. Select alert severity: Critical, High, Medium, or Low
2. Choose notification channels (email, Slack, PagerDuty, etc.)
3. Enable **Notify on Success** if you want confirmation when checks pass
4. Enable **Notify on Warning** to catch issues before they become critical

**Step 6: Schedule execution**

- **Run Now**: Execute immediately after creation
- **Schedule**: Set up recurring execution
    - Daily at specific time
    - Weekly on selected days
    - Monthly on specific dates
    - Custom cron expression for advanced scheduling

- **Execution timeout**: Set maximum time (default: 60 minutes)

**Step 7: Advanced settings (Spark engine only)**

- **Resource Strategy**: Specify custom Spark resources (executors, memory, cores)
- **Persist Good/Bad Records**: Store records that pass or fail for later analysis
    - Set retention period
    - Limit sample size for large datasets

## Configure Rules

You can choose from many pre-defined or custom rules to enforce data quality. Each rule has options to include or exclude nulls or empty values:

| **Rule** | **Description** | **Example** | 
| ---- | ---- | ---- | 
| **Null Values** | Checks if columns contain null values. | Customer email should never be null. | 
| **Schema Match** | Validates column data types. | Customer ID column must be integer. | 
| **Pattern Match (Regex)** | Ensures values follow a pattern. | Emails must match `^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`. | 
| **Enumerations** | Checks if values belong to a defined list. | The status column must be “Active”, “Inactive”, or “Pending”. | 
| **Tags Match** | Validates values against tags provided. | Product categories must match predefined tags. | 
| **Range Match** | Checks if values fall within a range. | Order total between 0 and 10,000. | 
| **Duplicate Row Check** | Ensures values are unique. | The customer ID column must be distinct. | 
| **Row Count Check** | Validates total rows fall within expected limits. | The dataset should have 10,000–12,000 rows. | 
| **Metric Check** | Validates aggregate metrics (SUM, AVG, MIN, MAX). | Average salary between 25,000–60,000. | 
| **SQL Metric Check** | Advanced numeric checks using custom SQL expressions. | `avg(emp_salary) - 10000` must be between 25,000–60,000. | 
| **Freshness Check** | Check if the latest data arrived on time. Supports anomaly detection. | Sales data must refresh daily by 6 AM. | 
| **User-Defined / Lookup** | Custom code or reference-based validation. | Validate IDs against reference table. | 


## Rule Evaluation and Thresholds

Each data quality policy consists of one or more rules. Rules evaluate data quality metrics and determine whether the results meet defined thresholds.

### Rule Evaluation States

Rules can now evaluate to one of the following states:

- **Success** – The metric meets the expected threshold.
- **Warning** – The metric shows early signs of degradation but has not crossed the failure threshold.

- **Failure** – The metric violates the defined failure threshold.

The **Warning** state is optional. If no warning threshold is configured, the rule continues to evaluate using **Success** and **Failure** only, with no change in behavior from previous releases.

## Configuring Rule Thresholds

When creating or editing a data quality policy, thresholds define how rule results are evaluated. Rule-level thresholds now support clearer evaluation semantics to match policy-level behavior.

### Threshold Direction

For rules using **Absolute evaluation**, users can define how a metric should be interpreted using one of the following directions:

- **Above**
 
 Use when higher values indicate better data quality (for example, percentage of valid rows).

- **Below**
 
 Use when lower values indicate better data quality (for example, error counts).

- **Range**
 
 Use when acceptable values must fall within a specific range (for example, expected row counts).

This makes it explicit whether higher, lower, or in-range values represent good data quality.

> For row-based rules, ADOC assumes that higher scores indicate better data quality. The threshold direction is therefore set to **Above** by default, matching existing evaluation behavior. Users can optionally add warning thresholds. For Aggregate rules, users can select a direction from the given drop-down.

## Warning Threshold (Optional)

In addition to defining a success threshold or range, rules can optionally include a **Warning threshold**.

- Results that meet the success threshold are marked **Success**.
- Results that fall between the success and failure thresholds are marked **Warning**.

- Results that cross the failure threshold are marked **Failure**.

If a warning threshold is not defined, the rule evaluates strictly as **Success or Failure**, preserving previous behavior.

## Relative Rule Evaluation

Relative rules compare the current rule result against previous executions using a configured lookback window.

Relative rule evaluation follows the same three-state model:

- **Success** – Change is within acceptable limits.
- **Warning** – Change exceeds the warning threshold but not the failure threshold.

- **Failure** – Change exceeds the failure threshold.

Warning thresholds for relative evaluation are optional. If not configured, relative rules continue to evaluate using binary logic.

## Policy Status Determination

Policy status determination depends on the selected **Policy Evaluation Strategy**.

### Policy Evaluation Strategy = Rules

When the policy is evaluated based on **Rules**, the policy status is derived directly from the status of individual rules:

- If **any rule** evaluates to **Failure**, the policy is marked **Failure**.
- If no rules fail and **at least one rule** evaluates to **Warning**, the policy is marked **Warning**.

- The policy is marked **Success** only when **all rules** evaluate to **Success**.

This strategy provides a strict rule-driven evaluation, where the lowest rule status determines the overall policy status.

### Policy Evaluation Strategy = Weightage

When the policy is evaluated based on **Weightage**, the policy status is determined using **policy-level thresholds** instead of individual rule statuses:

- Each rule contributes to an overall **Policy Score** based on its assigned weight.
- Users configure **Success** and **Warning** thresholds at the policy level.

- The policy status is determined by comparing the Policy Score against these thresholds.

Rule-level Success, Warning, and Failure states are still calculated for visibility, but the **final policy status is based on the policy-level thresholds**.

## Example 1: Row-Based Rule (Higher Is Better)

### Use Case

Validate that a critical column has very few null values.

### Rule Type

**Row-Based Rule** – Null value check

### Scenario

A business user wants to ensure that the customer_email column is mostly populated.

### Threshold Configuration

- **Evaluation Type:** Absolute
- **Direction:** **Above** (default for row-based rules)

- **Success Threshold:** 95%
- **Warning Threshold:** 85% (optional)

### How the Rule Is Evaluated

| % Non Null Values | Rule Result | 
| ---- | ---- | 
| 98% | Success | 
| 90% | Warning | 
| 80% | Failure | 


### Why This Works

Row-based rules typically return a **percentage score (0–100)** where **higher values indicate better data quality**, so “Above” is the natural and default choice.

## Example 2: Aggregate Rule (Range Is Better)

### Use Case

Ensure daily data volume stays within an expected range.

### Rule Type

**Aggregate Rule** – Row count check

### Scenario

A data pipeline is expected to produce approximately 10,000 records per day.

### Threshold Configuration

- **Evaluation Type:** Absolute
- **Direction:** **Range**
 

- **Success Range:** 9,000 – 11,000 rows
- **Warning Range:** 8,000 – 12,000 rows (optional)

### How the Rule Is Evaluated

| Daily Row Count | Rule Result | 
| ---- | ---- | 
| 10,200 | Success | 
| 11,500 | Warning | 
| 13,000 | Failure | 


### Why This Works

Aggregate rules often validate **expected bounds**, where both unusually low and unusually high values can indicate issues. The **Range** direction makes these expectations explicit.

> All existing data quality policies are automatically migrated during upgrade to **ADOC v26.1.0**.> > - Existing rule thresholds are preserved.> - Warning thresholds are not set by default.> > Rule and policy evaluation results remain unchanged after upgrade.

## Thresholds

- **Success Threshold:** 0–100%
- **Warning Threshold:** 0–100%

> **Use a Data Policy Template for Faster Setup** > Instead of adding rules one by one, you can apply a [Data Policy Template](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-policy-template). A template is a reusable collection of rule definitions that represent a common set of data quality checks. When you apply a template to your policy, all rules in the template are automatically included and evaluated.> > - **Example:** A “Customer Data Template” might include rules for email null checks, customer ID uniqueness, and phone number pattern validation.> - **Benefit**: Templates save time, ensure consistent data quality standards across datasets, and reduce manual configuration.

## Configure Alerts & Notifications (Optional)

Alerts let you know when a policy **fails or needs attention**, so you can act before issues impact reports or analytics.

1. **Severity Levels**: Define how serious the alert is:
    - **Critical:** Immediate attention needed
    - **High:** Important, but not urgent
    - **Medium:** Monitor for trends
    - **Low:** Informational

2. **Notification Channels**: Choose where to receive alerts:
    - Email, Slack, Microsoft Teams, Webhook, ServiceNow, or Chat

3. **Notify on Success / Warning**: Optional toggles:
    - **Notify on Success**: Get notified when a policy passes successfully
    - **Notify on Warning:** Get notified if a policy raises a warning

4. **Re-notification Options**: Control how often you are notified:
    - **Never**: Only receive the first alert
    - **After n failed runs:** Reduce noise; notify after a set number of failures 
    - **Every time:** Receive an alert each time the policy fails

**Example:**

- A critical alert is sent via Slack if daily sales data hasn’t arrived by 6 AM.
- Warnings are emailed if less than 95% of customer emails are valid.

## Execution Settings (Optional)

Execution settings control **how and when your policy runs**, and where results are stored.

1. **Incremental Strategy**: Check only new or changed data:
    - Choose a column (ID, datetime, or partition) to track incremental updates.
    - Reduces processing time for large datasets.

2. **Scheduling**: Decide when the policy runs:
    - Hourly, daily, weekly, monthly, or yearly
    - Choose your time zone

3. **Resource Strategy**: Determine computing resources for execution:
    - Small, Medium, Large, Global, or Custom

4. **Persistence**: Decide how to store policy results:
    - **Good Records**: Data that passed all rules
    - **Bad Records:** Data that failed rules
    - Standardized folder paths make results easy to find and query:

```sql
Bad Records: s3a://<bucket>/data-quality-<policy-name>/<date>/<execution-id>/errorrecords
Good Records & Summary: s3a://<bucket>/data-quality-<policy-name>/<date>/<execution-id>/summary
```



5. **Timeouts**: Limit execution time:
    - **Run timeout**: Maximum time for the job itself
    - **Total timeout:** Maximum time including retries

**Example:** Daily incremental check on `customer_signups` table, storing failed rows for review, scheduled at 2 AM using Medium resources.

## Dynamic Column Mapping for SQL Rules and UDFs

Dynamic column mapping helps **apply the same rule across multiple datasets** even if column names differ.

1. Use **placeholders** `${column}` or `${table}` in your SQL rules or UDFs.
2. Tag columns or tables with descriptive tags (e.g., `customer_id`).
3. When the policy runs, ADOC automatically maps the rule to all columns or tables with the matching tag.

**Example:** Tables with columns `customer_id`, `cust_id`, and `client_id` can all be checked using one dynamic rule tagged `customer_id`.

**Benefit:** Saves time and ensures consistent data quality checks across datasets with similar but differently named columns.

## Executing a Data Quality Policy

1. Navigate to **Data Reliability &gt; Manage Policies**.
2. Find your policy and click the  **Play icon**.
3. Choose an execution mode:
    - **All Your Data**:  Run on the entire dataset
    - **Incremental**: Run based on incremental strategy
    - **Selective:** Run on a subset filtered by ID or datetime

4. Click **Execute**.
5. Review results in the **Policy Execution Details** page.

From v4.10.0, ADOC allows you to manually run Data Quality policies—even if they are already scheduled to run automatically. This includes policies that normally process only new or incremental data. Previously, manual (adhoc) execution was blocked to avoid interfering with scheduled runs.

This enhancement gives you more flexibility for troubleshooting, validation, or running checks on demand.

### How Different Adhoc Run Types Work

- **Full Run or Selective Run:** These runs _do not change_ the “last processed point” (incremental marker). Your scheduled policy will continue from where it left off.
- **Incremental Run:** This run _does update_ the incremental marker. Your next scheduled run will process data from the updated point.

Note If you perform a policy execution on all your data, that is usually incremental, the next scheduled incremental run may reprocess some of the same data.

#### When the Policy Is Already Running

Execution conflicts can occur when a new run is triggered while a previous run is still in progress. The behavior differs slightly for **non-scheduled** and **scheduled** policies.

**Non-Scheduled Policies**

- If a user tries to trigger a manual run while another manual execution is still running, the system stops the new request and displays a popup:
- _“Another execution is already running.”*_
- No additional job entry is created.

**Scheduled Policies**

Execution conflicts may happen in two situations:

1. **A scheduled execution starts while a previous scheduled run is still running**
    - The new run is skipped. 
    - An entry is now recorded with the status **Skipped** in both the **Jobs Listing** and **Executions** views.
_(This is new behavior—previously the run was skipped silently with no entry.)_

2. **A user tries to run the policy manually while a scheduled run is still running**
    - Manual runs are now allowed. 
    - If a scheduled run is still in progress, the manual attempt is blocked with the same popup used for non-scheduled policies:
**“Another execution is already running.”**
    - No skipped entry is created because the trigger came from a user action, not the system.

#### Impact on Scoring and Thresholds

- **If you choose “Include in Overall Reliability Score Calculation” on an adhoc run:**
    - The run will _not_ change any data quality scores.
    - It will _not_ influence future anomaly or threshold calculations.

- **If you do NOT choose “Skip Scoring”:**
    - The results of the adhoc run _will_ affect scores and anomaly models.
    - These results cannot be excluded later.

### Data Quality Policy Execution Details

The execution page provides insights into the policy run:

| **Panel / Tab** | **Description** | 
| ---- | ---- | 
| Execution History | Shows details for each run (start/end time, engine, rules configured/passed). | 
| Overall Quality Score | Summary of data quality performance. | 
| Execution Details Panel | Key metrics like rows scanned, rules passed, and processing engine. | 
| Filter Panel | Displays SQL filters used for execution. | 
| Execution Summary Tab | Shows rules, status (pass/fail), success rate, weightage, thresholds. | 
| Segmented Analysis Tab | Breaks down rules and rows by dataset segments. | 
| Quality Summary Tab | Summarizes data quality dimensions for the asset. | 


## Best Practices

1. **Start simple**: Begin with 3-5 critical rules, then expand as needed
2. **Set realistic thresholds**: Base success thresholds on historical performance, not ideal targets
3. **Use appropriate execution engines**:
    1. Pushdown for simple, real-time checks on large databases
    2. Spark when you need good/bad record tracking or complex SQL transformations

4. **Monitor regularly**: Schedule checks to run after your data pipelines complete
5. **Group related rules**: Create separate policies for different data quality dimensions
6. **Review bad records**: Use persisted bad records to identify root causes

## Common Pitfalls to Avoid

- Setting success thresholds too high initially (start at 80-85%, then increase)
- Not testing rules on sample data before full deployment
- Creating too many overlapping rules that slow down execution
- Forgetting to adjust thresholds after data patterns change
- Not configuring timeout appropriately for large datasets