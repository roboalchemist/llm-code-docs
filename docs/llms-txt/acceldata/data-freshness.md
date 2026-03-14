# Source: https://docs.acceldata.io/api/data-freshness.md

# Source: https://docs.acceldata.io/documentation/data-freshness.md

# Data Freshness Policy

The **Data Freshness Policy** in ADOC helps you monitor how up-to-date and consistent your data assets are. It evaluates the timeliness of data ingestion, changes in dataset size or volume, and detects anomalies that may indicate delays or irregular data loads.
Freshness insights enable teams to enforce SLAs on data arrival and maintain trust in critical data pipelines.

A Data Freshness Policy measures when and how your data changes over time.
Using metadata collected directly from supported data sources, ADOC evaluates key freshness metrics such as the last update timestamp, asset size, and row count.
Policies can run automatically on a defined schedule or on demand, and leverage the **Pushdown Data Engine** for near real-time evaluation.

**When to use it?**

Use Data Freshness policies when you need to:

- Ensure daily sales data loads before morning business meetings
- Monitor that real-time sensor data isn't delayed
- Verify hourly customer activity feeds are arriving on schedule
- Detect when upstream data pipelines are failing silently
- Alert when data hasn't been updated within expected intervals

---

## Key Capabilities

- **Independent Execution:** Freshness policies run independently of system cadence and can be scheduled or executed manually.
- **Custom Scheduling:** Define when policies should run—hourly, daily, or at specific times.
- **On-Demand Runs:** Execute policies instantly to check current data conditions.
- **Granular Control:** Configure policies at the table level and run them individually.
- **Machine Learning–Based Anomaly Detection:** Identify unusual data update patterns automatically.
- **Multi-Metric Monitoring:** Track multiple freshness dimensions in one policy.
- **Near Real-Time Insights:** Uses the **Pushdown Engine** to collect metadata directly from the source, improving speed and reliability.

---

## Supported Metrics

Each policy can track one or more of the following metrics:

| Metric | Description | Example | 
| ---- | ---- | ---- | 
| **Data Freshness** | Time since the table was last updated. | “Table should update within 24 hours.” | 
| **Change in Asset Size** | Variation in data size between consecutive runs. | “Alert if table size changes by more than 10 %.” | 
| **Absolute Asset Size** | Total size of the dataset. | “Asset should remain under 2 GB.” | 
| **Change in Row Count** | Percentage or absolute difference in row count between runs. | “Row count should increase by 5 % daily.” | 
| **Absolute Row Count** | Current number of rows. | “Record count should be between 100 K – 120 K.” | 


---

## Monitoring Types

A freshness policy can use either of the following approaches:

- **Manual SLA Contracts:**
Define explicit business rules such as update frequency or row count limits.
- **Anomaly Detection:**
Allow ADOC to automatically identify unexpected changes or delays based on historical data patterns.

---

## Configuring a Data Freshness Policy

You can create and customize a Data Freshness Policy directly from the **Discover Assets** page under **Reliability**.

Follow these steps to define thresholds, alerts, and scheduling preferences for your asset.

1. Navigate to **Reliability** &gt; **Discover Assets.**
2. In the **Asset** table, locate the desired asset and click the **(–)** icon under the **Freshness** column. The **Create Data Cadency Policy** page is displayed.
3. **Enable Freshness Monitoring**
    1. Turn on the **Freshness & Volume Scoring** toggle.
    2. Select one or more anomaly types to include when scoring and alerting on data freshness and volume:
        1. Data Freshness
        2. Change in Asset Size
        3. Absolute Asset Size
        4. Change in Row Count
        5. Absolute Row Count

4. **Configure Thresholds**
    1. Click **Configure Thresholds**.
    2. In the **Metric Thresholds** section, click **Add Setting** for each selected metric.
    3. Manually define success and warning threshold values to determine when alerts are triggered.
    4. Use the dropdown to select when anomalies should be included in scoring: High, Medium or Low.

5. **Configure Alerts and Notifications (Optional)**
    1. **Alerts:** Choose one or more alert severities — _Critical_, _High_, _Medium_, _Low_.
    2. **Notifications:**
        1. Select a notification channel.
        2. (Optional) Enable **Notify on Success** or **Notify on Warning**.
        3. Configure re-notification behavior:
            1. _Reduce Noise: Never_
            2. _Reduce Noise: Send notification every n failed policy runs_ (enter n value)
            3. _Notify every time_

6. **Advanced Freshness Settings (Optional)**
    1. Configure model training parameters for anomaly detection:
    2. **Training Window Minimum:** Enter number of days to consider for model training.
    3. **Model Sensitivity:** Choose _High_, _Medium_, or _Low_ to adjust anomaly detection sensitivity.

7. **Execution Details (Optional)**
8. **Enable** **Schedule Policy Execution** to run the policy automatically.
9. **Configure**:
    1. Frequency — _Every hour_, _day_, _week_, or _month_. 
    2. Time zone.
        - Minute offset (value past the hour).
        - If left disabled, the policy can be executed manually on demand.

10. Review all configuration settings in the summary view before saving.
11. Click **Save Policy** to create and activate the Data Freshness Policy.

---

## Viewing Policy Results

You can view, track, and analyze the execution results of all configured Data Freshness Policies directly from the **Reliability** section.

1. Navigate to **Reliability** &gt; **Manage Policies**.
2. Select the **Policies** tab.
3. Filter the table by **Freshness Policy**. The table displays all existing Data Freshness policies, along with key details such as Policy Name, Policy Type, Tags, Quality Score, Overall Status, Last Execution Time etc.
4. Click on a **Policy Name** to open its **Execution Summary** page. This page lists all policy executions for the selected asset and provides detailed evaluation results.

### Understanding the Execution Summary

Each execution entry includes:

- **Overall Summary**: Total number of evaluations and their pass/fail status.
- **Evaluation Metrics**: Each configured metric (e.g., _Data Freshness_, _Change in Row Count_) is listed with corresponding anomaly and SLA evaluation results.
- **Expected Range**:The defined acceptable range or SLA for each metric.
- **Actual Value**: The latest observed value from the data source.
- **Anomalous / SLA Status**: Indicates if the metric breached thresholds or triggered anomalies.
- **Strength**: Displays anomaly confidence where applicable.
- **Feedback**: Users can provide a thumbs-up/down rating to refine model accuracy.

### Visual Insights

Below the summary, a **trend graph** visualizes metric performance (e.g., _Data Freshness_ over time).
This allows you to monitor how values change across runs, helping identify drifts, late data arrivals, or abnormal spikes.

---

## Real-world Use Case

**Scenario**: Your executive dashboard shows yesterday's sales data every morning at 8 AM. Recently, executives have made business decisions based on stale data because the overnight ETL occasionally fails silently, and no one notices until hours later when decisions have already been made.

**Solution**: Create a Data Freshness policy that checks if the sales data was updated within the last 8 hours (with anomaly detection enabled). Schedule an alert to notify the data team by 7 AM if data is stale, giving them time to fix issues before executives access the dashboard.

### Step-by-step Guide

**Step 1: Understand how data freshness works**

Data Freshness policies:

- **Scheduled** at a defined frequency
- **Manually triggered** on demand

You can configure:

- **Execution schedule** (optional): Define how often the policy should run
- **SLA breach thresholds**: How long data can remain stale before triggering an alert
- **Anomaly detection settings**: Detect unusual delays in data updates

**Step 2: Enable freshness monitoring**

1. Navigate to your asset (table, file, dataset)
2. Go to **Asset Settings** or **Configuration**.
3. Enable **Data Freshness Monitoring**

**Step 3: Configure SLA breach rules**

Define when your data should be updated:

**Common SLA configurations**:

- **Real-time streaming data**: 1-4 hours
- **Hourly batch jobs**: 2-4 hours
- **Daily overnight loads**: 12-24 hours
- **Weekly aggregations**: 7-8 days

**Example configurations**:  

| **Data Type** | **Update Frequency** | **SLA Breach Threshold** | 
| ---- | ---- | ---- | 
| Sales transactions | Hourly | 2 hours | 
| Customer master data | Daily | 26 hours | 
| Financial reports | Daily | 30 hours | 
| Sensor readings | Every 15 min | 30 minutes | 


**Step 4: Enable anomaly detection**

Anomaly detection learns your data's arrival patterns and alerts when delays are unusual, even if they don't breach the SLA.

**Configuration options:**

- **Sensitivity:** Low, Medium, or High
    - **Low:** Only alert on significant deviations
    - **Medium:** Balance between noise and coverage
    - **High:** Alert on small deviations

- **Training window:** Minimum data points needed before detection starts (typically 3-7 days)

**When to enable anomaly detection:**

- Data has regular patterns (daily loads at same time)
- You want early warning before SLA breach
- Delays have business impact even within SLA

**Step 5: Configure freshness policy scoring**

The policy score is calculated as:

Total Evaluations = (SLA breach configs with Anomaly enabled) + (SLA breach configs)

    Total Failed = (Anomalies detected) + (SLA breaches)

    Score = ((Total Evaluations - Total Failed) / Total Evaluations) × 100
    Score = ((Total Evaluations - Total Failed) / Total Evaluations) × 100

**Example:**

- You configure 1 SLA breach threshold (24 hours)
- You enable anomaly detection for this threshold
- Total Evaluations = 1 + 1 = 2

**If data arrives on time with no anomaly:**

- Failed Evaluations = 0 + 0 = 0
- Score = (2 - 0)/2 × 100 = **100%**

**If data is delayed but within SLA:**

- Failed Evaluations = 1 + 0 = 1 (anomaly detected)
- Score = (2 - 1)/2 × 100 = **50%**

**Step 6: Set thresholds**

- **Success Threshold:** Minimum score to consider policy passing (e.g., 100%)
- **Warning Threshold:** Score that triggers warning (e.g., 50%)

**Recommended thresholds:**

- **Critical data:** Success = 100%, Warning = 50%
- **Important data:** Success = 100%, Warning = 100%
- **Nice-to-have data:** Success = 50%, Warning = 0%

**Step 7: Configure alerts**

1. **Alert severity:** Match to business impact
    - **Critical:** Revenue-impacting data
    - **High:** Customer-facing data
    - **Medium:** Internal analytics
    - **Low:** Nice-to-have reports

2. **Notification channels:** 
    - Email for daily batch jobs
    - Slack/Teams for near-real-time data
    - PagerDuty for critical services

3. **Alert timing:**
    - Enable **Notify on Warning** for early warning
    - Enable **Notify on Success** after resolving issues

---

## Supported Data Sources

Data Freshness policies support pushdown-based execution across major relational and warehouse systems, including:

- Snowflake
- BigQuery
- Redshift
- Databricks
- PostgreSQL
- MySQL
- Oracle
- Azure Synapse

Note For Hive and file-based data sources, ADOC continues to use the Spark engine for freshness evaluation.

---

## Best Practices

1. **Set SLA based on business needs, not technical ideals**
    - Ask: "When do users need this data?"
    - Add buffer time for troubleshooting

2. **Use anomaly detection for variable schedules**
    - Data that arrives at slightly different times daily
    - Gradual degradation in pipeline performance

3. **Start with longer SLA windows, then tighten**
    - Begin at 2x expected delay
    - Reduce as you gain confidence

4. **Monitor multiple assets in data chain**
    - Source data freshness
    - Intermediate transformation tables
    - Final analytics tables

5. **Adjust sensitivity based on data patterns**
    - Regular daily loads: Medium sensitivity
    - Variable timing: Low sensitivity
    - Critical real-time: High sensitivity

---

## Common Pitfalls to Avoid

- Setting SLA threshold equal to expected arrival time (no buffer for normal variation)
- Enabling high sensitivity on data with irregular patterns (too many false alerts)
- Not accounting for weekends and holidays in daily data expectations
- Alerting on freshness without considering upstream dependencies
- Forgetting that cadence checks run hourly (can't catch issues faster than that)
- Not adjusting thresholds after data pipeline changes

### Troubleshooting freshness issues

**Alert says data is stale, but it looks current:**

- Check if ADOC's cadence job ran successfully
- Verify the timestamp column ADOC is monitoring
- Confirm timezone settings match your data

**Getting too many false positive alerts:**

- Increase SLA threshold or reduce anomaly sensitivity
- Check if data arrival times naturally vary
- Verify training window has enough data points

**No alerts despite data being stale:**

- Confirm Data Freshness monitoring is enabled on the asset
- Check that cadence jobs are running hourly
- Verify notification channels are configured correctly

---

## Execution Engine

Freshness policies run on the **Pushdown Data Engine**, which evaluates data directly at the source for higher performance and faster metadata retrieval.
For more information, see [Pushdown Data Engine](https://docs.acceldata.io/documentation/pushdown-data-engine).

---

##  Deprecation Notice: Datasource-Level Freshness and Schema Drift Monitoring

As part of the **Data Freshness Policy redesign (v4.9.0)**, the following datasource-level monitoring options have been **deprecated and removed** from the data source registration flow:

- **Enable Schema Drift Monitoring**
- **Enable Data Freshness Monitoring**

### Reason for Removal

Previously, these configurations were tied to internal flags that allowed bulk policy creation at the datasource level.

With the introduction of the **Pushdown-based freshness architecture**, datasource-level monitoring is no longer compatible and could cause duplicate or conflicting policy creation.

To ensure consistency and better control, **all freshness policies must now be configured at the asset level** (for individual tables or datasets).

### Impact

- Existing policies remain unaffected.
- Users can no longer create freshness or schema drift policies in bulk during data source onboarding.
- This change does not impact other policy creation workflows within ADOC.

### Action Required

No user action is needed.

If you previously enabled datasource-level freshness or drift monitoring, those options have been automatically disabled and removed from the UI.

---

## Limitations and Notes

- Pushdown-based freshness is supported only for compatible data sources.
- The first policy run establishes baseline values; change metrics start from the second run.
- Metric units (bytes, KB, MB) depend on the source system.
- File and Hive sources use the Spark-based engine.
- ADOC does not automatically remediate data lag; alerts are for detection and monitoring.