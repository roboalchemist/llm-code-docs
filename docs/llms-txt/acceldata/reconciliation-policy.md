# Source: https://docs.acceldata.io/documentation/reconciliation-policy.md

# Reconciliation Policy

**Reconciliation policies** compare data between a source and target system to ensure data integrity during movement or transformation. They verify that data copied from one location to another remains accurate and complete.

A **policy** is a set of rules that define how two datasets (a source and a sink) should be compared. A **rule** is a specific condition or check applied during reconciliation, for example, comparing row counts, validating column equality, or using hashed row checks.

A reconciliation policy passes only if all its rules are satisfied. Policies can be executed manually or scheduled, and results are tracked to ensure ongoing consistency across systems.

**Example:**

- Compare a staging orders table with the production orders table.
- Rules might include:
    - “Row counts must match between source and sink.” (Row Count Match)
    - “Order IDs in the source must equal Order IDs in the sink.” (Data Equality)
    - “Hashed rows between source and sink must match.” (Hashed Data Equality)

**When to use it?**

Use Reconciliation policies when you need to:

- Verify data accuracy after ETL processes complete
- Confirm that data migration to a new system was successful
- Ensure data replication between production and analytics databases is complete
- Validate that aggregation jobs produce correct results
- Check data consistency between cloud and on-premise systems

## Creating a Reconciliation Policy

You can create a Reconciliation Policy in two main ways:

### Option 1: Through Manage Policies

1. Navigate to **Data Reliability &gt; Manage Policies**.
2. Click **Add Policy** (top-right).
3. Select **Reconciliation** as the policy type.
4. Choose your source asset and sink asset.
5. The **Create Reconciliation Policy** page opens for configuration.

### Option 2: Through the Asset Details Page

There are two ways to create a Reconciliation Policy from the Asset Details page: 

**Overview Tab**

1. Open the dataset in the **Asset Details** page.
2. In the Overview tab, click **Actions &gt; Add Reconciliation Policy.**

**Policies Tab**

1. Navigate to the **Policies** tab.
2. Click **Add Policy** or use the **Actions** button and select **Reconciliation**.

In both cases, the **Create Reconciliation Policy** page opens for configuration.

### Configure Data Selection

Before defining reconciliation rules, refine **what data will be compared** between the source and sink assets. 

ADOC supports two ways to define reconciliation input:

1. **Source Asset SQL Filter**: Narrow down the dataset from the source asset.
    - **Example**: `region = 'APAC'`

2. **Sink Asset SQL Filter** – Narrow down the dataset from the sink asset.
    - **Example**: `status = 'Active'`

#### Option 1: Asset-Based Selection (Default)

This is the most common configuration.

You select:

- A **source asset**
- A **sink asset**
- Optional SQL filters on each side

**Source Asset SQL Filter**: Narrows the dataset from the source asset. Example: region = 'APAC'

**Sink Asset SQL Filter**: Narrows the dataset from the sink asset. Example: status = 'Active'

**Recommendation**

Use valid column names from the selected assets. Filters must follow Spark SQL syntax.

This option is ideal when:

- Source and sink datasets have similar schemas
- You want row-level comparison
- No aggregation or transformation is required

#### **Option 2: Custom SQL–Based Data Selection (Advanced)**

For more complex reconciliation scenarios, ADOC supports **Custom SQL–based reconciliation**.

Instead of comparing entire assets with simple filters, you can define **custom SQL queries** on both the source and sink systems. Reconciliation is then performed on the **query results**, not the raw tables.

This enables reconciliation of **derived datasets**, including:

- Aggregated metrics
- Transformed values
- Normalized schemas
- Business-specific logic
- Joins using Native SQL query dialect.

**When to Use Custom SQL Reconciliation**

Use Custom SQL when:

- Source and sink schemas are different
- Aggregation is required (daily, monthly, customer-level)
- Business logic must be applied before comparison
- Raw row-level reconciliation is impractical due to data volume
- Downstream systems already contain transformed data

**How It Works**

When Custom SQL is configured:

1. ADOC executes the **source SQL query** on the source system
2. ADOC executes the **target SQL query** on the sink system
3. Query outputs are treated as logical datasets
4. Join keys and reconciliation rules are applied to the query results

Reconciliation rules operate on **query output columns**, not physical table columns.

#### Example Use Case: Aggregated Usage vs Billing

Instead of reconciling millions of raw usage events, teams reconcile aggregated business metrics.

**Source (Usage System):**

- Raw usage events (e.g., CDRs)

**Target (Billing System):**

- Monthly billed usage per customer

The reconciliation compares **monthly usage totals per customer**, allowing detection of:

- Missing usage records
- Pipeline delays
- Transformation or rounding discrepancies

This approach is critical for large-scale enterprise systems where row-level reconciliation is infeasible.

#### Supported Sources

Custom SQL-based data selection is supported for:

- **SQL databases**
- **File-based data sources**
- **Streaming sources (Spark engine only):**
    - **Apache Kafka**
    - **Google Pub/Sub**

Note  Reconciliation involving Kafka or Google Pub/Sub using Custom SQL is supported only with the **Spark engine**.

#### Custom SQL for Kafka & Google Pub/Sub (Spark Engine)

When either the **source** or **sink** asset is a Kafka topic or a Google Pub/Sub topic, ADOC uses the **Spark engine** to read topic data and execute the custom query.

**How It Works**

- Topic data is read into the configured Spark data plane.
- The topic is registered as a temporary Spark view.
- The user-provided query is executed using **Spark SQL**.
- Reconciliation is performed on the **result set of the Spark SQL query**, not directly on the raw topic.

**Query Requirements**

- Queries must use **Spark SQL syntax**.
- You can:
    - Select specific columns
    - Reorder columns
    - Apply filters (`WHERE`)
    - Perform transformations or derived column creation
    - Use aggregations if required

This enables reconciliation between Kafka and Google Pub/Sub topics by defining the exact column structure to be compared before applying row count or data equality reconciliation.

> Use valid column names from the chosen assets. Filters must follow Spark SQL syntax.

### Configure Rules

Reconciliation rules define **how the selected datasets are compared**, regardless of whether asset-based or Custom SQL selection is used.

You can configure one or more rule types.

| **Rule Type** | **Description** | **When to Use** | 
| ---- | ---- | ---- | 
| **Data Equality (Most Common)** | Compare values in source vs. sink columns. | You need to verify specific fields match exactly.\n\n\n\n**Example Scenario**: Ensure customer_id in source matches client_id in target | 
| **Hashed Data Equality (Most Comprehensive)** | Compare hashed rows for integrity. | You need to verify complete row integrity.\n\n\n\n**Example Scenario**: Ensure entire order records (all fields) match between systems | 
| **Row Count Match** | Compare total row counts. | You only need to verify data volume, not content.\n\n\n\n**Example Scenario**: After copying 1 million customer records, verify both systems have 1 million records | 


Each rule includes parameters:

- **Left Column (source)** and **Right Column (sink)**
- **Operator** (`=`, `!=`, `<`, `>`)
- **Ignore Null Values** (optional)
- **Success Threshold (0–100%)**
- **Warning Threshold (0–100%)**

**Example Rule Table:**

| **Match Type** | **Left Column** | **Right Column** | **Operator** | **Ignore Null** | **Success Threshold** | **Warning Threshold** | 
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| Data Equality | customer_id | client_id | = | Yes | 100 | 90 | 
| Hashed Data Equality | order_hash | order_hash | = | No | 100 | 95 | 
| Row Count Match | – | – | – | – | 100 | 95 | 


Example scenarios:

- Ensure **customer_id** in source matches **client_id** in target
- Ensure all order records match exactly between systems
- Verify record counts after large data movement

> **Hashed Data Equality reconciliation is deprecated.**> > Customers are encouraged to migrate to:> > - **Data Equality rules** for field-level validation> - **Custom SQL reconciliation** for full-record and aggregated validation> > Custom SQL provides greater flexibility and supports modern enterprise reconciliation use cases more effectively.

## Scheduling and Incremental Checks (Optional)

- **Incremental Strategy**: Track changes using an ID, datetime, or partition column.
- **Auto Increment Column**: Select the column for incremental runs.
- **Initial Offset**: Define the starting marker for the first run.
- **Schedule**: Run hourly, daily, weekly, or monthly, with time zone selection.

**Example:** Run reconciliation daily at midnight, comparing only records where `transaction_date` is greater than the last successful run.

## Incremental and Selective Execution

ADOC v4.7.0 introduces enhanced flexibility in **Reconciliation policies** through new **Incremental** and **Selective Execution** strategies. These updates improve performance, reduce cost, and allow users to run targeted reconciliation checks instead of processing entire datasets.

### Data Equality Reconciliation

I**ncremental Execution**

- Previously available only for the **source (left)** asset.
- Now supports **incremental configuration for both source and sink (right)** assets.
- Supported Engine: **Spark only.**
- Configuring the sink asset is optional.

**Selective Execution**

- Incremental strategies can now be applied to both **source and sink assets** during selective runs.

### Row Count Match Reconciliation

**Incremental Execution**

- Incremental strategies are now supported for **Row Count** reconciliation policies.
- Supported Engines:
    - **Spark**,
    - **Pushdown**, and
    - **Mixed-mode** (e.g., Spark for source, Pushdown for sink).

- Both **source and sink** assets must have strategies configured if incremental execution is enabled.

**Selective Execution**

- Incremental strategies can be applied to both assets during selective runs, ensuring flexible and efficient reconciliation operations.

## Custom SQL reconciliation

- Supports scheduled execution
- Can be used with selective execution
- Can be combined with incremental strategies where supported by the execution engine

Incremental execution behavior follows the same engine constraints as standard reconciliation.

## Alerts & Notifications (Optional)

Alerts help you respond quickly to reconciliation issues.

- **Severity Levels:** Critical, High, Medium, Low.
- **Channels:** Email, Slack, Microsoft Teams, Webhook, ServiceNow, Chat.
- **Notify on Success / Warning:** Optional toggles.
- **Re-notification Options:**
    - Never
    - After _n_ failed runs
    - Every time

**Example:** Send a Slack alert if the row count mismatch exceeds 5%.

## Advanced Policy Configuration (Optional)

- **Persistence:** Store Good and Bad records for analysis.
- **Timeouts:** Define run timeout and total timeout.
- **Execution Engine:**
    - **Spark (default):** For non-SQL or file-based sources.
    - **Pushdown:** For SQL-based sources, runs directly in the database engine for faster performance.

- **Resource Strategy:** Small, Medium, Large, Global, or Custom (define Spark resources manually).

> Use Pushdown whenever possible to reduce resource overhead.

## Executing a Reconciliation Policy

1. Navigate to **Data Reliability &gt; Manage Policies**.
2. Find your policy and click the  **Play** icon.
3. Choose execution type: 
    - **All Data**: Compare the entire dataset. 
    - **Incremental**: Use the defined incremental strategy.
    - **Selective**: Compare data within a specific ID or date range.

## Monitoring a Reconciliation Policy

- View results in the **Execution Details** page.
- Review pass or fail status for each rule.
- Check overall data quality scores.
- Policies using **Pushdown** and **Spark** appear together for easy comparison.

## Real-world Use Case

**Scenario**: Your nightly ETL process copies customer orders from the operational database to the data warehouse. Business users report that some orders appear to be missing in their morning reports, causing incorrect inventory calculations.

**Solution**: Create a Reconciliation policy that compares row counts and key column values between the source orders table and the warehouse orders table. Run this policy after your ETL completes to catch discrepancies immediately.

### Step-by-step Guide

**Step 1: Identify source and target assets**

1. Navigate to **Manage Policies** in Data Reliability
2. Click **Actions** &gt; **Reconciliation**
3. **Select source asset**:The original data location (e.g., production database orders table)
4. **Select target asset**: The destination after data movement (e.g., data warehouse orders table)

**Step 2: Provide policy details**

- **Name:** Use a descriptive name (e.g., "Orders ETL Reconciliation")
- **Description**: Document what you're checking and why
- **Policy group, labels, tags**: Organize policies for easy management

**Step 3: Configure preprocessing (optional)**

Apply filters to narrow down the comparison:

```sql
-- Source filter example
order_date >= CURRENT_DATE - INTERVAL '7 days'

-- Target filter example  
load_date >= CURRENT_DATE - INTERVAL '7 days'
```



**Why use preprocessing?**

- Focus on recently changed data
- Exclude archived or deleted records
- Compare specific data segments

**Step 4: Choose reconciliation type**

Select the [appropriate match type](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reconciliation-policy#configure-rules)  for your use case.

**Step 5: Set thresholds**

- **Success Threshold**: Percentage of matching records needed to pass (e.g., 100% for critical data)
- **Warning Threshold**: Percentage that triggers a warning (e.g., 98%)
- **Threshold guidelines**:
    - Financial/compliance data: 100%
    - Customer master data: 99-100%
    - Analytical data: 95-98%
    - Log/event data: 90-95%

**Step 6: Configure scheduling and incremental checking**

**Incremental Check Options:**

- **Auto Increment Column**: Select a column that increases monotonically (e.g., order_id, timestamp)
- **Initial Offset**: Starting point for first check
- **Schedule**: Set to run after your data pipelines complete
    - After ETL: Run 30 minutes after expected completion
    - Real-time replication: Run every hour
    - Batch processing: Run daily at specific time

**Step 7: Set up alerts**

1. Choose severity based on business impact:
    1. **Critical**: Financial data, compliance data
    2. **High**: Customer-facing data
    3. **Medium**: Internal analytics
    4. **Low**: Non-critical reports

2. Select notification channels
3. Enable **Notify on Success** for high-value processes
4. Configure re-notification frequency

## Best Pactices

1. **Start with row count checks**: Quick validation before detailed comparison
2. **Use appropriate reconciliation types**:
    1. Row Count: Initial validation, quick health check
    2. Data Equality: Specific business-critical fields
    3. Hashed Equality: Complete record validation for compliance

3. **Schedule strategically**: Run after data loads complete, not during
4. **Set realistic thresholds**: Account for legitimate timing differences
5. **Document preprocessing filters**: Make it clear what data is excluded and why
6. **Monitor execution time**: Large dataset comparisons may need timeout adjustments

## Common Pitfalls to Avoid

- Comparing tables with different column names (use field mapping correctly)
- Not accounting for timezone differences in timestamp columns
- Setting 100% threshold when legitimate timing differences exist
- Forgetting to filter out soft-deleted records
- Not handling null values appropriately
- Comparing floating-point numbers without rounding tolerance