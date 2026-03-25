# Source: https://docs.acceldata.io/documentation/lineage.md

# Lineage

Lineage provides a unified view of how data moves across systems, from raw sources to transformed datasets, models, and downstream reports. It helps users understand dependencies, trace data transformations, and analyze the impact of changes at any point in the data flow.

By visualizing both upstream and downstream relationships, Lineage enables teams to troubleshoot faster, maintain trust in data, and ensure reliability across their analytics ecosystem.

### Why Lineage Matters

- **End-to-End Visibility:** See where data originates, how it is transformed, and where it’s consumed.
- **Impact Analysis:** Identify which assets (reports, dashboards, or datasets) are affected by upstream failures or schema changes.
- **Column-Level Insight:** Trace data lineage down to individual columns, with visibility into data types and quality scores.
- **Faster Troubleshooting:** Quickly pinpoint root causes and prioritize remediation based on downstream impact.

## Types of Lineage Creation

Lineage in the platform can be created in two ways: **Manual Lineage** and **Dynamic Lineage**.

### Manual Lineage

Manual lineage allows users to define and build lineage paths manually through the **UI** or **APIs**.
This approach is useful when:

- The source systems do not automatically support dynamic lineage.
- You need to define custom relationships between assets that are not connected through built-in integrations.
- Teams want to enrich existing lineage with additional business logic or external data flow links.

Manual lineage can be created by:

- Using the **Add Lineage** option in the Lineage view to link assets.
- Leveraging **public APIs** to define relationships programmatically between upstream and downstream assets.

This gives teams full flexibility to model complex or proprietary data flows that go beyond automated system connections.

#### Adding Manual Lineage

You can manually define relationships between assets when automatic lineage is not available or when custom process mapping is required.

**To add lineage:**

1. Navigate to the **Lineage** tab of the target asset.
2. Click **Add Lineage**. The **Add Lineage** dialog opens.
3. Under **Lineage Type**, select the direction of the relationship:
    - **Upstream:** Specifies that the selected asset depends on another source asset.
    - **Downstream:** Specifies that other assets depend on the selected one.

4. Click **Add Asset** and choose the related source or target data asset.
5. (Optional) Enter a **Process Name** and **Process Description** to document the transformation or logic between the assets.
6. Click **Add** to create the lineage connection.

The new link appears in the **Lineage** view, visually connecting the assets.

Recommendation Use clear, descriptive process names and summaries to make manual lineage easy to interpret for governance and auditing purposes.

### Dynamic Lineage

Dynamic lineage is automatically derived from supported source connections through **asset fingerprinting** and metadata analysis. When the platform connects to compatible systems (for example, **Snowflake**, **BigQuery**, **Databricks**, **Power BI**, **Tableau**, and others), it analyzes the metadata to infer relationships across systems.

#### Imprint-Based Asset Inference for Power BI Assets

Dynamic lineage for Power BI relies on **imprint-based asset inference**, which connects Power BI assets with underlying physical data sources such as Snowflake or BigQuery.

Here’s how it works:

- Crawling of Snowflake or other physical data sources generates **imprints** in the format native to each source type.
- Crawling of Power BI assets generates **additional custom metadata** for:
- Power BI **Semantic Model Tables** and **Columns**
- Power BI **Dataflow Entities** and **Attributes**
- When the Power BI crawler finishes, an **imprint matching job** is triggered asynchronously. This job matches Power BI imprints against Snowflake or other physical data source assets to infer lineage automatically.

This imprint-based approach ensures that lineage between Power BI and its data sources is created dynamically, accurately mapping transformations and relationships down to the column level.

## Lineage Views

Lineage includes two complementary views that serve different purposes: **Lineage** and **Relationships**.

| View | Purpose | Best For | 
| ---- | ---- | ---- | 
| **Lineage Tab** | Visualizes the actual flow of data between assets. | Root cause analysis, dependency tracing, impact analysis. | 
| **Relationships Tab** | Displays the logical grouping and hierarchy of assets. | Navigating data organization, ownership, and structure. | 


### Lineage Tab

The Lineage tab focuses on the movement of data across connected systems and assets.

**Key capabilities include:**

- Directed flow graph showing upstream and downstream paths.
- Column-level tracing across datasets, models, and reports.
- Contextual details like column names, data types, and quality metrics.
- Impact Analysis visualization — highlighting affected downstream assets when upstream issues occur.

This view answers questions like:

“Where does this data come from?”
“Which reports depend on this dataset?”
“What will break if this table fails?”

#### Cross-System Lineage

The platform supports **end-to-end, column-level lineage** across multiple systems. This includes visibility into how data flows between BI tools, transformation layers, and data warehouses.

Supported examples:

- **Power BI → Snowflake / Databricks / BigQuery / other supported sources**
- **Tableau → Snowflake / Databricks / BigQuery / other supported sources**

Lineage across these platforms is derived using **DBT model mappings** and **imprint-based inference**, providing a complete picture of how data moves from source to visualization.

**Key benefits:**

- Trace BI fields all the way back to their source columns.
- View transformation logic, relationships, and calculated field expressions (such as DAX or Tableau Calculations).
- Identify the downstream impact of data changes across systems.
- Build confidence in report accuracy with detailed, system-level metadata mappings.

#### Backward Lineage from Power BI to Redshift

Backward lineage from **Power BI to Redshift** allows users to trace data flow from Power BI dashboards and reports back into Redshift assets. This capability extends cross-system lineage coverage, providing complete end-to-end traceability for Power BI assets across all major warehouse sources.

**Key benefits:**

- Provides lineage visibility from Power BI to Redshift, similar to existing support for Snowflake, Databricks, and BigQuery.
- Enables end-to-end traceability of metrics and fields from visualization layers to Redshift datasets.
- Supports governance and root cause analysis workflows in environments using multiple warehouse systems.

**How It Works**
 Backward lineage between Power BI and Redshift is derived through the existing imprint-based asset inference process. When both Power BI and Redshift sources are crawled, their metadata is matched automatically to establish table- and column-level lineage, consistent with how lineage is inferred for Snowflake, Databricks, and BigQuery.

### Relationships Tab

The **Relationships Tab** provides a **high-level, structural view** of how assets are organized and logically related. Unlike the Lineage Tab, which focuses on data flow, the Relationships Tab helps users understand **how assets are grouped, owned, and connected** within the platform.

**Key capabilities include:**

- Displays **parent-child hierarchies**, such as:
- Workspace → Report → Semantic Model → Dataset
- Project → Schema → Table → Column
- Shows **ownership and logical grouping** of assets within domains, projects, or workspaces.
- Helps users **navigate the data structure** in large environments where lineage graphs may be extensive.
- Provides insight into **organizational and contextual relationships**, complementing the data flow view.

**Use the Relationships Tab to answer questions like:**

“Which workspace or project does this asset belong to?”
“Which reports and dashboards are grouped under a workspace?”
“How are datasets and assets organized across domains?”

## Accessing Lineage

1. Navigate to **Discover Assets** under the **Reliability** section in the navigation menu.
2. Use the search bar to find a data asset by name or data source.
3. Select the asset to open its details.
4. Choose the **Lineage** tab to explore data flow or the **Relationships** tab for structural context.

### Working with the Lineage View

In the Lineage view, you can:

- Visualize data flow between systems and downstream assets.
- Explore column-level lineage with names, data types, and quality scores.
- Search within tables or columns using the built-in search bar.
- Add custom or missing lineage connections.
- View asset metadata, related assets, and dependency trees via the Relationships tab.