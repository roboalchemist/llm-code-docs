# Source: https://docs.acceldata.io/documentation/schema-drift-policy.md

# Schema Drift Policy

Schema Drift policies detect unexpected changes in your data structure (schema) by comparing the current schema against a baseline. They catch when columns are added, removed, renamed, or when data types change.

A **policy** is a set of rules that define the expected schema. A **drift event** occurs when a column is added, removed, or modified compared to the previously crawled schema.

Schema Drift policies run automatically every time a **crawler** is executed on the data source.

**Example:**

- A Customer Table Schema Drift Policy might include:
    - “Alert if new column `customer_status` is added.”
    - “Alert if data type of `customer_id` changes.”
    - “Alert if the `email` column is removed.”

**When to use it?**

Use Schema Drift policies when you need to:

- Prevent breaking changes from affecting downstream analytics
- Detect when developers modify database schemas without coordination
- Ensure data pipeline compatibility when source systems change
- Catch accidental schema modifications in production
- Monitor API data contracts for unexpected structure changes

## Creating a Schema Drift Policy

You can create a Schema Drift Policy in two main ways:

### Option 1: Through Manage Policies

1. Navigate to **Data Reliability &gt; Manage Policies**.
2. Click **Add New Policy** (top-right).
3. Select **Schema Drift** as the policy type.
4. Choose the dataset (asset) to monitor.
5. The **Create Schema Drift Policy** page opens for configuration.

### Option 2: Through the Asset Details Page

**Overview Tab**

1. Open the dataset in the **Asset Details** page.
2. In the Overview tab, click **Actions &gt; Add Schema Drift Policy**.

**Policies Tab**

1. Navigate to the **Policies** tab.
2. Click **Add Policy** or use the **Actions** button and select **Schema Drift**.

## Schema Configuration

Schema configuration defines which types of changes will trigger alerts.

### Step 1: Select Drift Alerts

Enable one or more of the following toggles:

- **Alert on Column Additions** – Notifies when new columns appear.
- **Alert on Column Removals** – Notifies when columns are deleted.
- **Alert on Column Metadata Changes** – Notifies when metadata of existing columns changes.

### Step 2: Edit Metadata (Optional)

Click **Edit Metadata** to select which metadata changes should be monitored.

- **Standard Metadata**: Data type changes.
- **Relationships**: Changes to foreign keys or references.
- **Additional Metadata**: Monitor advanced attributes such as column default, nullability, or interval type.

Click **Done** to save your selection.

## Alerts & Notifications (Optional)

Define how and where alerts should be sent when schema drift is detected.

1. **Severity Levels:** Critical, High, Medium, Low.
2. **Notification Channels:** Email, Slack, Microsoft Teams, Webhook, ServiceNow, Chat.
3. **Notify on Success:** Optionally enable notifications for successful runs.
4. **Re-notification Preferences:**
    - Never: Suppress repeated alerts.
    - After _n_ failed runs:  Reduce noise by grouping violations.
    - Every time: Notify on each drift event.

## Summary & Save

In the **Summary** section, review and confirm:

- Selected drift alerts and metadata options.
- Severity and notification channels.
- Success notification preference.

Click **Save Policy** to activate the Schema Drift Policy.

## Executing a Schema Drift Policy

- A Schema Drift Policy **cannot be run manually**.
- It executes automatically each time the **crawler** runs on the dataset.
- When drift is detected, alerts are sent to configured channels.

**Examples:**

- **Slack:** Instant notification with details of schema changes.
- **Email:** Preview with a summary of added, removed, or modified columns.

## Real-world Use Case

**Scenario:** Your business intelligence team spends every Monday morning troubleshooting broken reports. The issue: A supplier management application team frequently adds and removes columns from their customer database without notifying anyone. These changes break SQL queries in your analytics pipeline, causing cascading failures.

**Solution:** Create a Schema Drift policy on the customer table that alerts on any column additions, removals, or data type changes. Configure it to notify both the source system team and the BI team immediately when drift occurs, allowing proactive communication before reports break.

### Step-by-step Guide

**Step 1: Understand how schema drift detection works**

Schema Drift policies are **event-triggered** - they run automatically after ADOC crawls your data source and discovers metadata changes. The policy compares:

- **Baseline schema:** The schema from the previous crawl
- **Current schema:** The schema from the most recent crawl

**Step 2: Enable schema monitoring**

1. Navigate to your data source or specific asset
2. Go to **Asset Settings** or **Data Source Configuration**
3. Enable **Schema Drift Monitoring**
4. Choose the **asset level** to monitor:
    - **Database level:** Detect table additions/removals
    - **Schema level:** Detect table additions/removals within schemas
    - **Table level:** Detect column additions/removals/modifications

**Step 3: Configure what to detect**

Select which types of schema changes should trigger alerts:

**For Database/Schema level:**

- **Table Addition:** Alert when new tables appear
- **Table Removal:** Alert when tables are deleted
- **Table Metadata Changes:** Alert when table properties change

**For Table level:**

- **Column Addition:** Alert when new columns appear
- **Column Removal:** Alert when columns are deleted
- **Column Data Type Change:** Alert when column types change (e.g., INT to VARCHAR)
- **Column Rename:** Alert when columns are renamed
- **Column Position Change:** Alert when column order changes

**Step 4: Create the schema drift policy**

1. Navigate to **Manage Policies**
2. Click **Actions** &gt; **Create Policy**
3. Select the asset to monitor
4. Choose **Schema Drift Policy**

The policy is automatically configured to:

- Run after each data source crawl
- Compare against the previous baseline
- Generate a score based on detected changes

**Step 5: Configure detection rules**

Define your tolerance for different types of changes:

**Strict Configuration (for production critical tables):**

    Column Addition: CRITICAL
    
    Column Removal: CRITICAL  
    
    Data Type Change: CRITICAL
    
    Column Rename: CRITICAL
    
    Column Position Change: WARNING
    

**Flexible Configuration (for development/staging):**

    Column Addition: WARNING
    
    Column Removal: HIGH
    
    Data Type Change: HIGH
    
    Column Rename: MEDIUM
    
    Column Position Change: LOW 

**Step 6: Set scoring thresholds**

- **Success Threshold:** Usually **100** (no drift detected)
- **Warning Threshold:** Usually **0** (any drift triggers warning)

**Why?** Schema changes are typically binary - the schema either changed or it didn't. Unlike data quality where partial failures are common, schema drift is usually an "all or nothing" event.

**Step 7: Configure alerts and notifications**

1. **Alert severity:** 
    - **Critical:** Production analytics tables
    - **High:** Shared data models
    - **Medium:** Department-specific tables
    - **Low:** Development/test environments

2. **Notification strategy:**
    - **Immediate notifications:** Send to both source system team and data consumers
    - **Digest notifications:** Daily summary for low-priority assets

3. **Response workflows:**
    - Include schema change approval process in notification
    - Link to change request documentation
    - Provide rollback procedures

## Best Practices

1. **Start at table level, not database level**
    - Focus on critical tables first
    - Expand to database-wide monitoring gradually

2. **Configure different policies for different assets**
    - Strict policies for production data models
    - Flexible policies for landing/staging areas

3. **Coordinate with source system teams**
    - Share schema drift alerts with upstream data owners
    - Establish change communication protocols
    - Document approved schema evolution patterns

4. **Use schema drift for change management**
    - Treat schema changes as formal change requests
    - Require impact analysis before approval
    - Track drift patterns to identify problematic systems

5. **Don't alert on expected changes**
    - Pause policies during planned maintenance windows
    - Document temporary schemas (staging tables)
    - Exclude auto-generated or temporary tables

## Common Pitfalls to Avoid

- Monitoring temporary or staging tables (too much noise)
- Not distinguishing between backward-compatible and breaking changes
- Alerting the wrong teams (notify both source and consumers)
- Treating all schema changes equally (column addition ≠ column removal)
- Not having a response process after detecting drift
- Monitoring every table in the organization initially (start focused)

## Understanding Schema Drift Results

When a schema drift policy runs, the results show:

**Added Columns:**

    Column: customer_segment
    
    Type: VARCHAR(50)
    
    Position: 15

**Removed Columns:**

    Column: legacy_customer_id  
    
    Type: INTEGER
    
    Position: 8

**Modified Columns:**

    Column: order_amount
    
    Change: INT → DECIMAL(10,2)

**What to do with results:**

1. **Verify if change was intentional**
    - Check with source system team
    - Review change management records

2. **Assess impact**
    - Identify downstream dependencies
    - Check if queries will break
    - Evaluate data pipeline compatibility

3. **Take action**
    - Update affected queries and transformations
    - Notify impacted teams
    - Document the schema change
    - Update data dictionaries and documentation

## Troubleshooting Schema Drift Detection

**Policy shows drift, but schema hasn't changed:**

- Check if ADOC crawler permissions changed
- Verify that different crawler is seeing different schema views
- Confirm timezone or metadata caching isn't causing false positives

**Known schema changes not detected:**

- Verify schema drift monitoring is enabled
- Check that crawler ran after the schema change
- Confirm the changed table is included in monitoring scope

**Too many alerts from legitimate changes:**

- Refine monitoring scope to critical tables only
- Increase notification threshold
- Use warning level instead of critical for expected changes