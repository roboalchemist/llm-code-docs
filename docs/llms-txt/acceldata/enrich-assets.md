# Source: https://docs.acceldata.io/documentation/enrich-assets.md

# Enrich Assets

Enrichment in ADOC means extending the value of your existing datasets without physically altering them. Instead of stopping at raw discovery, you can _enrich_ assets by:

- Creating **virtual assets** that combine or transform data logically for deeper analysis.
- Building **query lineage** to trace how data flows, transforms, and connects across systems.

By enriching assets, you turn raw datasets into more meaningful, reusable, and trustworthy resources for analytics, monitoring, and decision-making—without the overhead of duplicating or moving data.

## Virtual Assets

In ADOC, **virtual assets** are assets that **do not exist as physical tables** but behave like standard data assets. They are defined using **SQL queries** or **visual graphs**, allowing you to model complex data logic without duplicating physical data.

**Key Benefits of Virtual Assets:**

- Combine data from multiple sources without creating new tables
- Apply **data quality policies**, profiling, and monitoring as if it were a physical asset
- Simplify reporting and analytics workflows by creating reusable datasets
- Reduce storage and maintenance overhead since the data is computed dynamically

Virtual assets come in two main types: **SQL Views** and **Visual Views**.

### 1. SQL View

An **SQL View** is a virtual asset defined by a **custom SQL query**. Instead of referencing a physical table, the asset dynamically computes its content using the query provided.

**Use Cases:**

- Joining multiple tables for analysis
- Aggregating metrics like total sales or customer counts
- Applying filters to focus on specific segments

#### Steps to Create an SQL View

1. Click the ⌘ **Actions** button and select **Add SQL View**.
2. Enter a **Name** for your SQL View.
3. Select the **Data Source** and **Database**.
4. Enter a **Description** explaining the purpose of the view.
5. Enter the **SQL Query** that defines the virtual asset.
6. Click **Preview** to check sample results.
7. Click **Save**.

**Example:**

```sql
SELECT customer_id, email, SUM(order_total) AS total_spent
FROM orders
WHERE order_date >= '2025-01-01'
GROUP BY customer_id, email;
```



This SQL View aggregates total spending per customer without creating a new physical table.

### 2. Visual View

A **Visual View** is a **graphical representation of a virtual asset**. It allows you to visually define joins, transformations, and aggregations across multiple datasets.

**Use Cases:**

- Quickly combining tables from different sources
- Visualizing relationships between datasets
- Creating reusable virtual datasets for monitoring and analytics

#### Steps to Create a Visual View

1. Click **Actions -&gt; Add Visual View**.
2. Enter a **Name** and **Description**.
3. Select a **Data Source**.
4. Click **Next** to open an empty canvas.
5. Click **Add Asset** to bring in tables or datasets.
6. Define joins, transformations, and relationships using the visual editor.
7. Click **Validate** to check syntax and preview result data.
8. Click **Save** to store the virtual asset.

#### Editing a Visual View:

1. Open the Visual View asset.
2. Click the **Edit icon** to modify the canvas.
3. Update joins, filters, or transformations as needed.
4. Click **Validate** and then **Save Changes** to apply updates.

## 3. Query Lineage

Query Lineage helps you visualize how data flows into and out of an asset. It automatically identifies upstream and downstream dependencies based on your SQL queries—capturing how data is transformed, joined, or aggregated before it reaches its final form.

You can add lineage by uploading a query file for ADOC to analyze. Once created, the lineage is visible directly within the asset’s **Lineage** tab.

### Adding Query Lineage

1. Navigate to **Reliability** **-&gt;** **Discover Assets**.
2. Click **Actions -&gt; Add Query Lineage**.
3. Provide the following details:
    - **Data Source**: Select the data source where the query runs.
    - **Database**: Choose the relevant database name.
    - **Schema**: Select the schema containing the referenced objects.
    - **SQL Query**:  **Upload a SQL file** to support large or complex multi-statement queries.

4. Click **Save** to analyze the query and register the lineage.

Note Ensure all SQL statements are valid and reference existing tables or views. Syntax errors or inaccessible objects may prevent lineage extraction.

### Viewing Lineage

After a lineage has been created, you can view its details directly from the asset’s page.

1. Navigate to **Reliability -&gt; Discover Assets**.
2. Locate and click the **asset name** to open its **Asset Details** page.
3. From the left-side navigation menu, select **Lineage**.
4. The **Lineage tab** displays a graphical view showing:
    - **Upstream dependencies** (data sources feeding into the asset)
    - **Downstream dependencies** (assets or dashboards using this data)
    - **Transformation paths** inferred from SQL queries
    - **Related systems** (such as Snowflake, BigQuery, Tableau, etc.)

Use zoom, pan, or filter controls to focus on specific parts of the lineage graph. For more information, see [Lineage](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/lineage).

**Best Practices & Use Cases:**

- **Trace data origins and dependencies:** Understand which upstream tables feed into a given asset.
- **Impact analysis:** Identify downstream dependencies affected by schema or data changes.
- **Governance and auditing:** Verify that data transformations align with business rules or compliance requirements.
- **Complex pipelines:** Upload multi-step SQL workflows (including CTEs, joins, and unions) to infer lineage across systems.