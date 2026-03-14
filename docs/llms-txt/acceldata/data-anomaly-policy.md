# Source: https://docs.acceldata.io/documentation/data-anomaly-policy.md

# Data Anomaly Policy

Profile Anomaly policies detect unusual patterns in your data's statistical profile metrics. While Data Drift policies identify changes in distributions, Profile Anomaly policies use machine learning to detect unexpected values in metrics like null percentages, distinct counts, min/max values, and statistical measures.

**When to use it?**

Use Profile Anomaly policies when you need to:

- Detect sudden spikes in null values that could indicate data quality issues
- Identify unexpected changes in distinct count (potential duplicate or missing data)
- Catch unusual min/max values that suggest data errors or outliers
- Monitor row count changes that don't follow normal patterns
- Detect gradual degradation in data quality before it impacts business

## Creating a Data Anomaly Policy

Create a Data Anomaly Policy from:

### Option 1: Through Manage Policies

1. Navigate to **Data Reliability &gt; Manage Policies**.
2. Click **Add Policy** (top-right).
3. Select **Anomaly** as the policy type.
4. Choose the dataset (asset) to monitor.
5. The **Create Data Anomaly Policy** page opens for configuration.

### Option 2: Through the Asset Details Page

**Overview Tab** 

1. Open the dataset in the **Asset Details** page.
2. In the **Overview** tab, click **Actions &gt; Add Data Anomaly Policy**.

or

**Policies Tab**

1. Navigate to the **Policies** tab.
2. Click **Add Policy** or use the **Actions** button and select **Data Anomaly**.

## Policy Configuration Steps

### Step 1: Policy Details

1. **Processing Engine:** Choose either **Spark** or **Pushdown** as the processing engine.
2. Click **Show Columns** to view the dataset schema.

### Step 2: Select Data Columns

By default, **all columns** are included for profiling. To enable anomaly detection for specific columns:

1. Check the box under the **Data Anomaly** column.
2. Click **Configure Anomaly** to continue.

### Step 3: Configure Anomaly Rules

#### Policy Scoring

1. **Policy Thresholds**:
    - **Success Threshold (0–100):** Minimum score for passing.
    - **Warning Threshold (0–100):** Trigger a warning if the score drops below this value.

2. **Anomaly Strength Inclusion**:
    - Select the minimum anomaly strength to include in scoring (**High, Medium, Low**).
    - Example: Only include anomalies with strength &gt;= HIGH.

#### Alerts & Notifications

Define how ADOC notifies you when anomalies are detected.

1. **Severity Levels:** Critical, High, Medium, Low.
2. **Notification Channels:** Email, Slack, MS Teams, ServiceNow, Webhook, Chat.
3. **Notify on Success:** Optionally enable success alerts.
4. **Re-notification Preferences:**
5. **Reduce Noise (Never):** One-time alerts only.
6. **Send Every [X] Failed Runs:** Alerts after repeated violations.
7. **Notify Every Time:** Alerts triggered for every violation.

#### Anomaly Detection Settings

Fine-tune anomaly detection behavior:

| **Setting** | **Description** | **Example / Options** | 
| ---- | ---- | ---- | 
| **Training Window Minimum** | Minimum history required for training | At least 3 executions, default: 7 days | 
| **Model Sensitivity** | Adjusts anomaly detection tolerance | High (catch subtle anomalies), Medium (default), Low (only major deviations) | 


#### Advanced Performance Settings

Optimize profiling for large or wide datasets.

1. **Processing Batch Size:**
    - Default: 30
    - Adjust only under support guidance.

2. **Optimize Data Load with Batches:**
    - Loads data in smaller chunks instead of all at once.
    - Useful for **wide tables with frequent updates**.
    - May introduce slight inconsistencies in results.

### Step 4: Summary

1. Review policy details, thresholds, alerts, and performance settings.
2. Click **Save Policy** to finalize.

## Executing Data Anomaly Policies

Once created, anomaly policies are executed during **asset profiling**.

### Method 1: From Manage Policies &gt; Profiles (Beta)

1. Go to **Profiles**.
2. Search for the asset with the policy applied.
3. In the Profiles table, click  **Play**.
4. Profiling begins and the **Data Anomaly Policy executes automatically**.

### Method 2: From Asset Details Page

1. Open the **Asset Details** page.
2. Click **Actions**.
3. Select profiling type (**Full** or **Selective**).
4. Profiling triggers the anomaly policy.

## Real-world Use Case

**Scenario:** Your customer data table has been reliable for years, but recently, analytics reports show incomplete customer profiles. After investigation, you discover that the percentage of null values in the phone number column suddenly jumped from 5% to 35%. An upstream system change caused phone numbers to be lost during integration, but the issue went unnoticed for weeks because row counts stayed normal.

**Solution:** Create a Profile Anomaly policy that monitors profile metrics including null percentages, distinct counts, and row counts for the customer table. The ML-based anomaly detection learns normal patterns and immediately alerts when null percentages spike abnormally, catching the issue within hours instead of weeks.

### Step-by-step Guide

**Step 1: Understand how profile anomaly detection works**

Profile Anomaly policies are **event-triggered** - they run automatically after ADOC profiles your asset. The policy:

1. Collects profile metrics during each profiling run
2. Trains ML models to understand normal patterns
3. Detects when current metrics deviate from expected patterns
4. Generates alerts for significant anomalies

**Step 2: Enable profiling for your asset**

1. Navigate to your asset (table)
2. Go to **Profile Settings**
3. Enable **Scheduled Profiling**
    - **Recommended frequency:**
        - Critical tables: Daily or more frequent
        - Standard tables: Weekly
        - Archive tables: Monthly

4. **Select profiling type:**
    - **Full profile:** Analyze entire table
    - **Incremental profile:** Analyze only new/changed data
    - **Sampled profile:** Analyze representative sample

**Step 3: Select columns for anomaly detection**

1. Click on **Profile Settings** for the asset
2. Enable **Profile Anomaly Detection**
3. **Select columns to monitor:**

**High-value columns to monitor:**

- **Business-critical columns:** Customer ID, Order ID, Transaction Amount
- **Frequently used in analytics:** Status, Category, Region
- **Join keys:** Foreign keys used to link tables
- **Nullable columns:** Fields that should have low null rates

**What gets monitored per column:**

- Null value percentage
- Distinct count
- Minimum value
- Maximum value
- Mean (for numeric)
- Standard deviation (for numeric)
- Top value frequency (for categorical)

**Step 4: Configure anomaly detection settings**

**1. Training window:**

- **Minimum data points:** How many profile runs before detecting anomalies
    - **Recommended:** 7-14 profile runs
    - **Fast-changing data:** 5-7 runs
    - **Stable data:** 14-30 runs

**2. Sensitivity level:**

- **High:** Detects small deviations, more alerts
    - Use for: Critical data, regulatory compliance data

- **Medium:** Balanced approach (recommended starting point)
    - Use for: Most business-critical tables

- **Low:** Only major deviations, fewer alerts
    - Use for: Exploratory data, highly variable data

**3. Metrics to monitor:**

Select which metrics to monitor per column:

- Null percentage
- Distinct count
- Min/Max values
- Mean
- Standard deviation
- Row count (table level)

**Step 5: Review automatic policy creation**

When you enable Profile Anomaly Detection and select columns, ADOC automatically creates a Profile Anomaly Policy with:

- **Policy name:** `{asset_name}-profile-anomaly-policy`
- **Monitored columns:** All selected columns
- **Monitored metrics:** All enabled profile metrics
- **Execution:** Automatic after each profiling run

**Step 6: Configure scoring thresholds**

The Profile Anomaly policy score is calculated as:

    Total Evaluations = Total columns selected × Profile metrics captured per column

    Failed Evaluations = Total profile metrics with anomaly detected

    Score = ((Total Evaluations - Failed Evaluations) / Total Evaluations) × 100

**Example:**

- Monitoring 5 columns
- Each column has 4 profile metrics (null %, distinct count, min, max)
- Total Evaluations = 5 × 4 = 20
- 2 metrics show anomalies (null % in column A, distinct count in column B)
- Failed Evaluations = 2
- Score = (20 - 2)/20 × 100 = **90%**

**Configure thresholds:**

- **Success Threshold:** Minimum score for policy to pass (e.g., 95%)
- **Warning Threshold:** Score that triggers warning (e.g., 85%)

**Step 7: Set up alerts and notifications**

1. **Alert severity:**
    - **Critical:** Production databases feeding real-time systems
    - **High:** Customer data, financial data
    - **Medium:** Analytics tables
    - **Low:** Development/test data

2. **Notification channels:**
    - Data engineering team (for data quality issues)
    - Data platform team (for system issues)
    - Business stakeholders (for critical table anomalies)

3. **Alert content should include:**
    - Which column(s) showed anomalies
    - Which metric(s) were anomalous (null %, distinct count, etc.)
    - Current value vs expected range
    - Severity of deviation
    - Link to detailed profile comparison

## Best Practices

1. **Start with table-level metrics**
    - Row count anomalies
    - Overall profile statistics
    - Expand to column-level gradually

2. **Profile at appropriate frequencies**
    - Match profiling frequency to data update frequency
    - Daily updates → Daily profiling
    - Weekly loads → Weekly profiling

3. **Allow sufficient training period**
    - Don't trust anomaly detection immediately
    - Let models learn for 2-4 weeks
    - Manually review initial anomalies

4. **Tune sensitivity based on false positives**
    - Start with medium sensitivity
    - Increase if missing real issues
    - Decrease if getting too many false alarms

5. **Monitor complementary metrics together**
    - Null percentage + Distinct count
    - Min + Max values
    - Row count + Data volume

6. **Use feedback mechanism**
    - Mark false positives to improve model
    - Confirm true positives
    - Help system learn your data patterns

## Common Pitfalls to Avoid

- Monitoring too many columns initially (start with 5-10 most critical)
- Setting high sensitivity before model is trained (wait for training period)
- Not distinguishing seasonal patterns from anomalies
- Ignoring minor anomalies (they can indicate early problems)
- Not investigating anomaly root causes (defeats purpose)
- Expecting perfect anomaly detection immediately (models need time to learn)

## Understanding Anomaly Detection Results

When an anomaly is detected, examine:

**1. Anomaly type:**

- **Null percentage spike:** Data collection issue, upstream failure
- **Distinct count drop:** Duplicate data, data loss
- **Min/Max out of bounds:** Data entry errors, schema changes
- **Mean shift:** Population change, calculation errors

**2. Anomaly severity:**

- **Minor (1-2 std dev):** Monitor, may be natural variation
- **Moderate (2-3 std dev):** Investigate cause
- **Severe (&gt;3 std dev):** Immediate action required

**3. Anomaly pattern:**

- **Sudden spike:** System failure, data pipeline issue
- **Gradual drift:** Process degradation, slow data quality decline
- **Cyclical:** May be seasonal, check historical patterns

### Response Procedures

**When anomaly is detected:**

1. **Confirm it's real**
    - Check if metric calculation is correct
    - Verify profile ran successfully
    - Compare with raw data queries

2. **Investigate cause**
    - Check data source for issues
    - Review recent pipeline changes
    - Look for upstream system changes
    - Check for schema modifications

3. **Assess impact**
    - Identify downstream consumers
    - Check if reports are affected
    - Verify machine learning models
    - Contact business stakeholders

4. **Remediate**
    - Fix data quality issues at source
    - Reprocess affected data if possible
    - Update documentation
    - Communicate to affected parties

5. **Prevent recurrence**
    - Add Data Quality rules to prevent issue
    - Improve upstream validation
    - Update data pipeline monitoring
    - Document lessons learned

## Troubleshooting Profile Anomaly Detection

**Too many false positives:**

- Reduce sensitivity level (high → medium → low)
- Increase training window (more data points for baseline)
- Exclude highly variable columns from monitoring
- Check if data has natural cyclical patterns
- Provide feedback on false positives to improve model

**Missing real anomalies:**

- Increase sensitivity level
- Reduce training window if data patterns change frequently
- Verify profiling is running at appropriate frequency
- Check that affected columns are included in monitoring
- Ensure metric calculations include full data range

**Anomaly detected but cause unclear:**

- Run Data Quality policies to check for violations
- Compare with Data Drift policy results
- Check Schema Drift for structural changes
- Profile with finer granularity (add segments)
- Review data lineage for upstream changes

**Anomalies on every profile run:**

- Data may be genuinely unstable (not anomalous)
- Training data may have been during abnormal period
- Consider resetting baseline or adjusting sensitivity
- May need different monitoring approach (thresholds instead of anomaly detection)