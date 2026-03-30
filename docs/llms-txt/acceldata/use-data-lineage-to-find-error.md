# Source: https://docs.acceldata.io/documentation/use-data-lineage-to-find-error.md

# Use Data Lineage to Find Errors

This guide is a practical walkthrough for using data lineage to diagnose a common data quality issue. The process involves starting from a known error in a final report and tracing it backward to its origin.

**Scenario:**
A critical dashboard shows incorrect sales figures. You have traced the source of the dashboard to a final data asset and suspect the error occurred in the pipeline _Gold Price Aggregation_ that produces it.

## 1. Locate the pipeline

First, you need to find the specific pipeline run that produced the incorrect data.

1. Navigate to the main **Pipelines** page.
2. Use the  **Search** bar to find the pipeline by its name.
3. Review the **Recent Runs** sparkline to identify the specific run where the error may have started. Click on the dot to view the execution details.
or
4. Click on the pipeline **Name** to open the **Pipeline Run Details** page for that specific execution.

## 2. Trace upstream data dependencies

The [Lineage Graph](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/understanding-the-pipeline-run-details#lineage-graph)  is your primary tool for this investigation. It shows the flow of data and processes from left to right.

1. Locate the final data asset on the right side of the graph (in this scenario, the node representing _Gold Price Aggregation_).
2. Trace dependencies backward from the final asset to find direct upstream jobs and data assets feeding the problematic table.

## 3. View lineage and investigate nodes

- **Check Policy Nodes:** Find Nodes with policy failures on data assets.
A failed policy check is a strong indicator of a data quality issue.
- **Inspect Data Assets:** Click on an **Asset Node**.
Open the  **Asset Nodes** side panel to view its metrics.
Look for anomalies in record counts, schema drift, or data quality scores.
- **Review Job Status:** Check the status of the white **Job Nodes**.
Even if the overall pipeline succeeded, an individual job might contain warnings or helpful logs.

## 4. Identify the root cause of data errors

By following the chain of dependencies in our scenario, you trace the lineage back several steps to an upstream asset. Here, you notice a Data Quality check has failed.

1. Click on the failed Policy Node to select it.
2. In the  **Details Panel** below the graph, open the **Automation Tab**.
3. Review the  **Executed Policies** list. You find the policy that ran on the upstream asset has a **Failed** or **Warning** status. The details show that the check for null values in a critical column failed.

**Conclusion:**

You have now identified the root cause: an early-stage data asset contained null values, which were then propagated through the pipeline, causing the incorrect final aggregation.