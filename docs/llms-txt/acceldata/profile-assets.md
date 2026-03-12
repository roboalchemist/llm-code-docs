# Source: https://docs.acceldata.io/documentation/profile-assets.md

# Profile Assets

Profiling is the process of examining a dataset to understand its structure and content. It is the first essential step before you apply monitoring rules or policies in ADOC. Without profiling, you may know a dataset exists, but you would not know whether it is reliable or ready for analytics.

ADOC supports profiling for both **structured** (tables, numeric/text/date columns) and **semi-structured** data (arrays, structs, nested fields). This ensures that even complex datasets from systems like Snowflake, BigQuery, or S3 can be analyzed and made trustworthy.

## Why Profiling Matters

- **Baseline Understanding**: See row counts, distinct values, null percentages, and update frequency.
- **Issue Detection**: Identify missing data, anomalies, or unusual distributions early.
- **Policy Preparation**: Use profiling results to decide which rules (Data Quality, Freshness, Reconciliation, etc.) make sense for that dataset.

**Example**: If you profile the `EMPLOYEES` table, you might learn:

- It has **2,976,508 rows**.
- Around **5% of email addresses are null**.
- Updates happen daily, but not on weekends.

From this, you might apply a Data Quality policy (no missing emails) and a Freshness policy (daily updates).

## How Profiling Fits into the Flow

1. **Discover Assets**: See what datasets exist.
2. **Profile Assets**: Understand their shape, quality, and anomalies.
3. **Apply Policies**:  Define standards for “good data.”
4. **Monitor Continuously**: ADOC watches for policy violations and new anomalies.

Without profiling, policies cannot be applied effectively. Profiling is the **bridge between discovery and monitoring**.

## Starting a Profile

To profile an asset:

1. In the **Discover Assets** page, locate and select the dataset you want to profile (e.g., `EMPLOYEES`). This opens the **Asset Details page**.
2. In the **Asset Details page**, click the **Actions** button (top right).
3. Select a profiling mode:
    - **Full Profile**: Scans the entire dataset for complete statistics.
    - **Selective Profile**: Profiles a sample of data. Faster, ideal for large datasets.
    - **Incremental Profile**: Profiles only new data since the last run.

Once profiling completes, the **Profile** tab in the Asset Details page shows the results.

## Profile Execution Details

Every profile captures metadata about when and how it was run.

| **Property** | **Definition** | **Example** | 
| ---- | ---- | ---- | 
| **Executed Profile** | Most recent date/time profiling ran. Use the dropdown to view older results. | Aug 24, 2023, 8:26 PM | 
| **Rows Profiled** | Number of rows included in the profile. | 2,976,508 | 
| **Profiling Type** | Full, Incremental, or Selective. | FULL | 
| **Start/End Time** | When profiling began and ended. | Aug 24, 2023, 8:26–8:27 PM | 
| **Start/End Value** | Internal markers for tracking profile execution. | 169271…114824 | 


You can also use the **Compare Profiles** feature to check how values have changed over time.

## Column-Level Metrics

Profiling generates **statistics per column**, based on data type.

### Structured Data

| Data Type | Statistical Measures | 
| ---- | ---- | 
| **String** | % Not Nulls, Distinct, Min/Avg/Max Length, Case Count | 
| **Integral (Int)** | % Not Nulls, Distinct, Min, Mean, Max, StdDev | 
| **Fractional (Decimal/Float)** | % Not Nulls, Distinct, Min, Mean, Max, StdDev | 
| **Timestamp** | % Not Nulls, Distinct | 
| **Boolean** | % Not Nulls, Distinct | 


### Semi-Structured Data

| Data Type | Statistical Measures | 
| ---- | ---- | 
| **Struct** | % Not Nulls, Distinct, Min/Max/Avg Keys | 
| **Array[String]** | % Not Nulls, Distinct, Array Length (Min/Max/Avg), Element Length (Min/Max/Avg), Patterns, Top Values | 
| **Array[Integral/Fractional]** | % Not Nulls, Distinct, Array Lengths, Value Ranges, Patterns, Top Values | 
| **Array[Boolean]** | % Not Nulls, Distinct, Array Lengths, Top Values | 
| **Array[Struct]** | % Not Nulls, Distinct, Array Lengths, Struct Keys (Min/Max/Avg) | 


**Recommendation**: If a column is semi-structured (e.g., `Array`, `Map`, or `Struct`), click **Expand** to drill into sub-columns and nested fields.

## Column Insights

For each column, click its name to explore:

- **Column Statistics**: See % null, % unique, and distributions (with bar charts).
- **Most Frequent Values**: Quickly identify dominant entries.
- **Detected Patterns**: Common string or numeric patterns in the data.
- **Anomalies & Trends**: Graphs that highlight unusual changes over time.

## Anomaly Detection

When profiling runs over time, ADOC records a data point for each metric (per column). Using these data points, ADOC plots **upper and lower bounds** to detect anomalies.

- If a value lies **between the bounds**: Non-anomalous.
- If a value lies **outside the bounds**: Anomalous.

For anomaly detection, the following settings must be configured:

- **Historical Metrics Interval for Detection**
- **Minimum Historical Metrics Required**

## Known Limitations

- Complex sub-columns (in arrays, maps, structs) that are not string/numeric/boolean are treated as strings.
- For array columns:
    - Pattern profile & top values show values only (counts not displayed).
    - Non-null counts are not displayed.

- Nested columns currently do not support anomaly detection.
- By default, ADOC supports profiling up to **5 levels deep** in nested structures. This can be changed using the `PROFILE_DATATYPE_COMPLEX_SUPPORTED_LEVEL` setting.