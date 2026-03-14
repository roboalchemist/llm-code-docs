# Source: https://docs.acceldata.io/documentation/asset-details.md

# Asset Details

The **Asset Details** page provides a detailed view of a dataset’s reliability, quality, and freshness. It brings together profiling results, applied policies, and trend analysis to help users understand how data performs over time and which fields may need attention.

## Accessing Asset Details

To open the Asset Details page:

1. Navigate to **Data Reliability -&gt; Discover Assets**.
2. Search for or select the dataset you want to explore.
3. Click the dataset name to open its details view.

## Overview Tab

The **Overview** tab gives a high-level summary of the dataset’s current health and performance trends.

### Key Metrics

At the top of the page, the following scores are displayed:

- **Data Reliability Score:** The overall dataset health, aggregated from data quality, freshness, and reconciliation results.
- **Data Freshness:** How up to date the dataset is compared to its expected schedule.
- **Data Quality:** Aggregated score based on rule evaluation and policy success rates.
- **Other Indicators:** Include Data Drift, Schema Drift, and Reconciliation (if configured).

### Trend Charts

- **Performance Trend:** Visualizes changes in the dataset’s reliability score over time.
- **Freshness Trend:** Displays data freshness intervals, showing how frequently the dataset was updated and when delays occurred.

These trends help identify recurring issues, degradation, or improvements in data quality.

### Column-Level Data Quality Reporting

The **Column Details** section extends asset-level analysis to individual fields, offering granular visibility into data health at the column level.

#### Behavior

- Column-level results appear after a policy execution run completes.
- Only columns that are part of an active Data Quality policy display rule counts and reliability scores.
- The table reflects the most recently profiled version of the dataset.
- Metrics automatically refresh when new profiling or policy runs complete.

#### Example

In the **EMPLOYEES** dataset:

- The **Performance Trend** shows changes in reliability over time.
- The **Freshness Trend** tracks when data was last updated.
- The **Column Details** table lists fields such as _BIRTHDATE_, _EMAIL_, _ID_, and _NAME_, along with data types and quality metrics.

#### Benefits

- Enables fine-grained visibility into data health at the field level.
- Helps identify which columns affect overall reliability scores.
- Supports faster troubleshooting and more precise policy adjustments.
- Combines asset-level and column-level insights in a single view.

## Navigation Tabs

In addition to **Overview**, the Asset Details page includes several tabs that provide specific operational insights:

| **Tab** | **Purpose** | 
| ---- | ---- | 
| Policies | Lists all applied data quality, freshness, reconciliation, anomaly, and schema drift policies. Includes details such as policy status, quality score, open alerts, and execution history. | 
| Cadence | Shows the frequency and trend of dataset updates over time. Also includes derived metrics such as change in asset size, row count, and rows added per hour. | 
| Profile | Displays profiling statistics for each column, such as distinct counts, null percentages, patterns, and data type–specific metrics. Helps assess data structure and quality readiness. | 
| Sample Data | Provides a preview of the dataset’s sample records for quick validation. Users can refresh cached data or retry fetching samples if unavailable. | 
| Segments | Allows creation and management of column-based segments by selecting distinct column values. Useful for analyzing specific data subsets. | 
| Lineage | Displays upstream and downstream data relationships. Users can manually add lineage by specifying lineage type, target asset, and process details. | 
| Relationships | Visualizes logical asset hierarchies and parent-child connections, such as source → database → schema → table. Helps in navigating organizational data structures. | 
| Schema Changes | Tracks and compares schema snapshots over time to detect column additions, deletions, or modifications. | 
| Metadata | Displays and manages metadata, including owner, team, description, tags, labels, and user-defined template (UDT) variables. Supports automated description generation. | 
| Settings | Provides profiling configuration options such as engine selection, column scope, pattern detection, notifications, scheduling, and advanced performance settings. | 
| Recommendations | Suggests optimization or configuration actions (for example, adding missing policies or enabling profiling) to improve data reliability and monitoring coverage. | 
| Query Logs | Lists query activity for the dataset, including query text, timestamp, type, and user. Includes access information, row count trends, and most associated tables. | 
| [Asset Similarity](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/asset-similarity) | Lists datasets with similar schema or content, along with a similarity score. Helps identify redundant or related assets for governance and optimization. | 
