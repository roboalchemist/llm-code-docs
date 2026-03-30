# Source: https://docs.acceldata.io/documentation/understanding-the-pipeline-run-details.md

# Understanding the Pipeline Run Details

Clicking a pipeline name in the pipeline list directs you to the pipeline run details page.

This page provides you: 

- in-depth view of historical run
- inspect the pipeline structure
- review associated events and automations

The page is composed of three main areas

- [Header](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/understanding-the-pipeline-run-details#header): An at-a-glance summary of the pipeline run
- [Lineage Graph](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/understanding-the-pipeline-run-details#lineage-graph): A visual presentation of the pipeline’s structure and data flow
- [Details Panel (Timeline and Automations)](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/understanding-the-pipeline-run-details#details-panel-timeline-and-automations)**:** A tabbed section with detailed timelines(span) and automations

## Summary Panel

The header at the top of the page provides the most critical information about this specific run:

| **Column Name** | **Description** | 
| ---- | ---- | 
| **Pipeline Name** | The name of the pipeline being viewed. | 
| **Run Timestamp** | Displays the date and time the last run was executed.\n\nClick the timestamp. It opens the **Pipeline Run History** dropdown. It enables selection and comparison of two runs. | 
| **Execution time** | The total duration of the run, along with a comparison to its historical baseline. | 
| **Data Reliability Policies** | Ratio of passed to total data reliability checks during run. | 


---

## Lineage Graph

The central part of the page is the interactive lineage graph. It visually maps out the jobs and data assets involved in the pipeline run.

| **Pipeline Element /Actions** | **Description** | 
| ---- | ---- | 
| **Nodes** | The graph consists of nodes representing **Jobs** (white icons) and **Data Assets** (blue icons). | 
| **Interaction** | You can click, pan, and zoom to explore the graph.\n\nClicking on a specific node often highlights it and reveals more information in the side panels. | 
| **Controls** | On the top right, you have controls to zoom in/out, reset the view.\n\nToggle for **Show only job nodes** to simplify the graph by hiding data assets. | 
| **Side panels** | On the left side of the lineage graph, you will find icons to open different informational panels.\n\nIt includes, Job nodes, Asset nodes, and Alerts. | 
| **Job Nodes** | These represent the primary processing steps or tasks in your pipeline. It lists all the individual jobs that are part of the pipeline, along with their status and execution time.\n\nClick on the Job node to see the details in the details panel. | 
| **Asset Nodes** | Lists all the data assets that were read from or written to during the pipeline run. It provides a quick overview of quality, drift, record, and schema metrics for each asset.\n\nClick on the Asset node to see the details in the details panel. | 
| **Linked Assets** | **Linked Pipelines** shows all pipelines (DAGs) that read from or write to the same underlying asset (for example, a CSV file). This helps you understand how multiple pipelines interact with and impact a shared dataset, providing asset-centric control flow visibility. | 


---

## Details Panel (Timeline and Automations)

Below the lineage graph is a powerful panel with multiple tabs that provide detailed, time-series information and logs.

| **Tabs** | **Description** | 
| ---- | ---- | 
| **Timeline** | The span timeline chart visualizes the duration and sequence of each job or span within the pipeline, making it easy to spot bottlenecks or long-running processes. | 
| **Event List** | Click on **View all events**, in the timeline tab. You will see a detailed, time-stamped list of all events that occurred during the run. | 
| **Automation Tab** | This tab lists all the data reliability automations that were executed during the specific automation runs. | 
| **Executed Policies** | Shows any data profiling automations that were run. | 
