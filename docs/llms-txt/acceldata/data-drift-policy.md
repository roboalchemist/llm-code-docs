# Source: https://docs.acceldata.io/documentation/data-drift-policy.md

# Data Drift Policy

Data Drift policies identify statistical changes in your data distributions over time. Unlike Data Quality policies that check if data meets rules, Data Drift policies detect if the characteristics of your data have changed compared to historical patterns.

A **policy** is a set of rules that define expected stability for a dataset. A **rule** is a specific check that monitors how much a column’s values or metrics deviate compared to the baseline profile.

A Data Drift Policy automatically executes after each **profiling run** of the dataset. It cannot be run manually.

Note Only one Data Drift Policy can exist per dataset.

**Example:** A Customer Table Drift Policy might include:

- “The average age should not drift by more than 5%.”
- “Distinct values in the region column must remain within 10% of baseline.”
- “% of nulls in the email column must not increase beyond 2%.”

**When to use it?**

Use Data Drift policies when you need to:

- Detect shifts in customer behavior patterns
- Identify when sales distributions change unexpectedly
- Monitor machine learning model input data for drift
- Catch demographic changes in user populations
- Detect seasonal patterns or trend breaks in time-series data
- Identify when data collection processes have changed

## Creating a Data Drift Policy

Before creating a Data Drift Policy, make sure the asset has been **profiled at least once**.

You can create a Data Drift Policy in two main ways:

### Option 1: Through Manage Policies

1. Navigate to **Data Reliability &gt; Manage Policies**.
2. Click **Add New Policy** (top-right).
3. Select **Data Drift** as the policy type.
4. Choose the dataset (asset) to monitor.
5. The **Create Data Drift Policy** page opens for configuration.

### Option 2: Through the Asset Details Page

**Overview Tab**

- Open the dataset in the **Asset Details** page.
- In the Overview tab, click **Actions &gt; Add Data Drift Policy**.

**Policies Tab**

- Navigate to the **Policies** tab.
- Click **Add Policy** or use the **Actions** button and select **Data Drift**.

## Policy Details

- **Name**: Provide a unique name.
- **Description**: Describe the purpose of the policy.
- **Policy Group (optional)**: Assign the policy to an existing group.
- **Tags (optional)**: Add metadata tags for search and organization.

## Configure Rules

Rules define which metrics to track for drift and how much deviation is acceptable.

### Step 1: Select Columns

Choose columns to monitor. Columns can be filtered by type:

- String
- Integral
- Fractional
- Date

### Step 2: Select Metrics

For each column, choose the metrics to evaluate. Examples:

- **String Columns**
    - % Not Null
    - Distinct Values
    - Average Length, Max Length, Min Length
    - Upper Case / Lower Case / Mixed Case ratio

- **Numeric Columns (Integer / Fractional)**
    - Average
    - Maximum / Minimum
    - Standard Deviation

- **Date Columns**
    - Distinct Values
    - Distribution shifts

### Step 3: Define Rule Thresholds

For each rule, specify:

- **Threshold (%)**: The acceptable level of drift.
- **Weightage**: Importance of the metric in overall evaluation.

## Step 4: Set Success Criteria

- **Success Threshold (0–100%)** – Minimum pass percentage.
- **Warning Threshold (0–100%)** – Below this, the policy raises a warning.
- **Interval (days)** – Frequency at which drift is checked after profiling.

## Alerts & Notifications (Optional)

Alerts notify you when drift exceeds thresholds.

- **Severity Levels:** Critical, High, Medium, Low.
- **Notification Channels:** Email, Slack, Microsoft Teams, Webhook, ServiceNow, Chat.
- **Notify on Success / Warning:** Optional.
- **Re-notification Preferences:**
    - Never
    - After _n_ failed runs
    - Every time

## Summary & Save

- **Overview:** Confirm name and description.
- **Rules Configuration:** Check selected metrics and thresholds.
- **Alerts & Notifications:** Validate severity and channels.
- **Enable Policy:** Toggle on to activate.

Click **Save Policy** to finalize.

## Executing a Data Drift Policy

- A Data Drift policy **cannot be executed manually**.
- It runs automatically after each **profiling job** on the asset.
- Execution modes follow the profiling mode:
    - **Full**: Run on the entire dataset.
    - **Incremental**: Run based on incremental strategy.
    - **Selective**: Run on a subset (ID or datetime range).

Note

- Selective execution auto-fills parameters from the last successful run.
- If unavailable, defaults to incremental strategy or asset-level configuration.
- Currently supported for **Snowflake** and **BigQuery** (for datetime-based drift).

## Monitoring Data Drift

When execution completes, view results in the **Execution Details** page.

- **Status Indicators:**
    - Reliable = Passed
    - Unreliable (Orange) = Warning
    - Unreliable (Red) = Failed

- **Execution Details include:**
    - Rule pass/fail status
    - Drift percentages
    - Data quality score trends

## Real-world Use Case

**Scenario:** Your marketing team uses a predictive model to identify high-value customers. The model's accuracy has been declining for weeks, but no one knows why. After investigation, you discover that the customer age distribution in your database has shifted dramatically - your mobile app redesign attracted a younger demographic, but your model was trained on older customer data.

**Solution:** Create a Data Drift policy that monitors the statistical distribution of customer age, income, and purchase frequency. When the model input data drifts significantly from the training data distribution, the policy alerts the data science team to retrain the model.

### Step-by-step Guide

**Step 1: Understand how data drift detection works**

Data Drift policies are **event-triggered** - they run automatically after ADOC profiles your asset. The policy:

1. Captures statistical distributions during profiling
2. Compares current distributions against historical baselines
3. Detects significant statistical changes using various tests

**Step 2: Profile your data**

Before creating a Data Drift policy, you must profile your asset:

1. Navigate to your asset (table)
2. Click **Profile Now** or set up **Scheduled Profiling**
3. Wait for profiling to complete (creates baseline)

**Profiling captures:**

- Column distributions (histograms)
- Statistical measures (mean, median, standard deviation)
- Cardinality and uniqueness
- Null percentages
- Min/max values

**Step 3: Create the data drift policy**

1. Go to **Manage Policies**
2. Click **Actions** → **Create Policy**
3. Select your profiled asset
4. Choose **Data Drift Policy**

**Step 4: Select columns to monitor**

Choose columns where distribution changes matter:

**Good candidates for drift monitoring:**

- Numeric columns with business meaning (age, price, quantity)
- Categorical columns with limited values (status, category, region)
- Columns used in machine learning models
- Key business metrics (revenue, orders, sessions)

**Poor candidates:**

- Unique identifiers (customer_id, order_id)
- Free-text fields
- Timestamps or dates
- Columns with mostly null values

**Step 5: Configure drift detection rules**

For each column, specify:

**1. Statistical test to use:**

- **KS Test (Kolmogorov-Smirnov):** Compares overall distributions (good for numeric data)
- **Chi-Square Test:** Compares categorical distributions
- **Population Stability Index (PSI):** Measures stability over time
- **Custom threshold:** Compare specific statistics (mean, median, std dev)

**2. Drift threshold:**

- **Low sensitivity:** Alert only on major distribution shifts (use for exploratory data)
- **Medium sensitivity:** Alert on moderate changes (use for important features)
- **High sensitivity:** Alert on small changes (use for critical model inputs)

**3. Comparison baseline:**

- **Previous profile:** Compare against last profiling run
- **Historical average:** Compare against average of last N profiles
- **Specific date:** Compare against profile from a chosen date (e.g., model training date)

**Step 6: Set policy thresholds**

The Data Drift policy score is calculated as:

    Score = ((Total Columns Monitored - Columns with Drift) / Total Columns Monitored) × 100
    

**Configure:**

- **Success Threshold:** Percentage of columns that must be drift-free (e.g., 90%)
    - All columns stable: 100%
    - Most columns stable: 90%
    - Major drift acceptable: 70%

- **Warning Threshold:** Percentage that triggers warning (e.g., 80%)

**Example:**

- Monitoring 10 columns
- 2 columns show drift
- Score = (10 - 2)/10 × 100 = **80%**
- If Success Threshold = 90%, policy fails
- If Warning Threshold = 80%, policy shows warning

**Step 7: Configure alerts**

1. **Alert severity based on business impact:**
    - **Critical:** ML model inputs, regulatory reporting data
    - **High:** Customer segmentation data, pricing data
    - **Medium:** Marketing analytics, trend analysis
    - **Low:** Exploratory data, low-impact reports

2. **Notification recipients:**
    - Data science teams (for ML features)
    - Business analysts (for KPI data)
    - Data engineering (for pipeline health)

3. **Alert content:**
    - Which columns drifted
    - Magnitude of drift
    - Statistical test results
    - Historical comparison charts

## Best Practices

1. **Profile regularly to establish baselines**
    - Daily profiling for fast-changing data
    - Weekly profiling for stable data
    - After major data loads or pipeline changes

2. **Start with critical columns**
    - Model features first
    - Key business metrics second
    - Expand monitoring gradually

3. **Use appropriate statistical tests**
    - Numeric data: KS Test
    - Categorical data: Chi-Square Test
    - Time-series: PSI (Population Stability Index)

4. **Set realistic thresholds**
    - Too sensitive: Alert fatigue from natural variation
    - Not sensitive enough: Miss important changes
    - Adjust based on false positive rate

5. **Document expected drift**
    - Seasonal variations (holiday shopping patterns)
    - Business changes (new products, market expansion)
    - Data collection improvements

6. **Investigate drift causes**
    - Data collection changes
    - Business model shifts
    - External factors (economy, trends)
    - Data quality issues upstream

## Common Pitfalls to Avoid

- Monitoring too many columns (start with 5-10 most important)
- Not profiling frequently enough (can't detect gradual drift)
- Using same sensitivity for all columns (customize by importance)
- Ignoring domain knowledge (some drift is expected and healthy)
- Not having response procedures (what to do when drift detected?)
- Comparing against single baseline only (use historical averages)

## Interpreting Drift Detection Results

When Data Drift is detected, examine:

**1. Magnitude of drift:**

- Small drift (5-10%): Natural variation, monitor
- Medium drift (10-30%): Investigate cause, assess impact
- Large drift (&gt;30%): Immediate action required

**2. Drift direction:**

- **Mean shift:** Average values changed (e.g., prices increased)
- **Variance change:** Spread of values changed (more or less diversity)
- **Distribution shape:** Pattern changed (e.g., bimodal to normal)

**3. Affected columns:**

- Single column: Likely data quality issue or specific change
- Multiple related columns: Business process change
- All columns: Systematic problem or major event

### Response Procedures

**When drift is detected:**

1. **Verify data quality**
    - Run Data Quality policies on drifted columns
    - Check for null value increases
    - Verify data types haven't changed

2. **Investigate root cause**
    - Check upstream data sources
    - Review recent pipeline changes
    - Consult business stakeholders about process changes

3. **Assess impact**
    - Identify downstream dependencies
    - Test machine learning models
    - Check analytics reports for anomalies

4. **Take corrective action**
    - Update model training data
    - Adjust business rules
    - Fix data quality issues
    - Communicate with affected teams

5. **Update baselines**
    - If drift is expected, update comparison baseline
    - Document new normal patterns
    - Adjust sensitivity thresholds

## Troubleshooting Drift Detection

**False positives (alerts but no real issue):**

- Reduce sensitivity level
- Use historical average baseline instead of previous profile
- Exclude known variable columns
- Increase profiling frequency for more stable baselines

**Missing real drift:**

- Increase sensitivity level
- Profile more frequently
- Check that affected columns are included
- Verify profiling is capturing full data sample

**Drift detected but cause unclear:**

- Profile more granularly (add segments)
- Compare with same period last year (seasonality)
- Check data quality policies for correlated issues
- Review data pipeline logs for changes