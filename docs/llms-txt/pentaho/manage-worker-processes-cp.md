# Source: https://docs.pentaho.com/pdc-admin/manage-worker-processes-cp.md

# Manage worker processes

Pentaho Data Catalog uses worker processes to execute nearly all data analytics operations. Most worker processes consist of a single primary worker that is triggered by a user action or a scheduled task. In some cases, a primary worker may initiate secondary worker processes to complete the operation.

## Worker processes

The following table lists the worker processes:

<table><thead><tr><th width="147.888916015625">Process</th><th>Description</th><th>Actions performed</th></tr></thead><tbody><tr><td>Test Connection</td><td>Returns detailed success or failure information for each step of the test. Data Catalog starts this worker process when you configure or update a data source connection. Data Catalog marks the data source “OFFLINE” until a successful test completes.</td><td><ul><li>Connect to data source</li><li>Authenticate</li><li>Retrieve list of schemas and store in MongoDB</li></ul></td></tr><tr><td>Metadata Ingest</td><td>Ingests the metadata for one or more schemas.<br><strong>Note:</strong> Your license agreement determines the amount of data you can scan. Databases do not have a data scan quota.</td><td><ul><li>Read schema from data source and store in MongoDB</li></ul></td></tr><tr><td>Data Profiling</td><td>Generates a variety of statistics and intermediate data with a single pass through the source data.<br>Typically, this is the first process you run on your data.</td><td><ul><li>Create bitset</li><li>Create HyperLogLogs (HLL) for full data</li><li>Generate statistics (numeric and string related)</li><li>Generate data patterns</li><li>Lucene Indexing (optional)</li><li>Extract samples for viewing (&#x3C;100)</li></ul></td></tr><tr><td>Data Identification</td><td>Identifies and tags columns and tables using ontology information (dictionaries, aliases), along with underlying data and metadata.</td><td><ul><li>Tag columns based on dictionaries</li><li>Tag columns based on metadata and aliases</li></ul></td></tr><tr><td>Key Discovery</td><td>Performs a variety of key discovery actions. Foreign key discovery requires that Data Profiling of the data sources has completed.</td><td><ul><li>Foreign key discovery</li><li>Superkey identification</li><li>Composite key discovery</li><li>Compound key discovery</li><li>Secondary key discovery</li><li>Natural and Surrogate key identification</li></ul></td></tr><tr><td>Data Quality</td><td>Performs a full data quality (DQ) analysis on the underlying data, using regular expressions and other configurable business rules.</td><td><ul><li>RegEx matching</li><li>Data pattern analysis</li><li>Update column statistics</li><li>Evaluate column DQ rules</li><li>Evaluate row-relative DQ rules</li></ul></td></tr><tr><td>Sensitive Data Discovery (SDD)</td><td>Performs the tasks beyond data identification for SDD. This process uses flows, lineage, Foreign Keys, and more to put together the items comprising PI and PII.</td><td><ul><li>Generate separate SDD Lucene Index which cross- references data</li></ul></td></tr></tbody></table>

## Monitor worker status

From the **Manage Your Environment** page, you can see the number of completed worker processes and the number of worker alerts on the **Workers** card.

**Note:** You may be able to see a **Processed Items** region on your Home page, if your Landing page options window has the **Processed Items** check box selected.

Perform the following steps to monitor the status of a worker process:

1. From the **Manage Your Environment** page, click **View Workers**.\
   The **Workers** page opens, showing all in-progress and completed jobs.
2. Review the **Status** column to see the current state of each worker.
3. Click the expand arrow (▸) at the beginning of the worker process row to view additional information such as job parameters, start and end times, and worker logs.\
   **Note**: You can now apply column-level filters and narrow the workers list. Each column header includes a filter box to refine results dynamically.

## View worker process details

Perform the following steps to view details for a specific worker process, including parameters, logs, and exceptions:

1. From the **Manage Your Environment** page, click **View Workers**.\
   The **Workers** page opens, showing all in-progress and completed jobs.
2. On the **Workers** page, locate the worker process for which you want more information.\
   **Note**: You can now apply column-level filters and narrow the workers list. Each column header includes a filter box to refine results dynamically.
3. If an up arrow is visible at the beginning of the row for the worker process, click the arrow to expand the information.
4. Click the **View Details** icon (**>**) at the end of the row.

   The View Worker Details window opens. If the process failed, an **Exception** tab might be available, in addition to the **Details** tab.
5. Click **Close** to close the View Worker Details window.

## Cancel a worker process

Perform the following steps to cancel a worker process:

1. From the **Manage Your Environment** page, click **View Workers**.\
   The **Workers** page opens, showing all in-progress and completed jobs.
2. While a worker process is running, locate the worker process you want to cancel.\
   **Note**: You can now apply column-level filters and narrow the workers list. Each column header includes a filter box to refine results dynamically.
3. Click **Cancel** at the end of the row.

   Data Catalog cancels the worker process and displays `Cancelling` in the **Job Status** column.

## Search for a worker process on the Workers page

Perform the following steps to search for a specific worker process on the **Workers** page while worker processes are running:

1. Go to **Management** in the left navigation menu.
2. On the **Workers** card, click **View Workers**.\
   The **Workers** page opens.
3. In the **Workers** table, go to the column-level filter for the field you want to search (for example, *Worker Name* or *Status*).
4. Enter a keyword in the filter field.\
   The table updates to display only those worker processes that match your search criteria.

The worker processes matching your filter keyword are displayed in the **Workers** table.&#x20;

## Resubmit jobs from the workers queue

When you want to reprocess the same task, you can resubmit a completed job from the **Workers** page to run it again. Perform the following steps to resubmit a job from worker process:

1. Go to **Management** in the left navigation menu.
2. On the **Workers** card, click **View Workers**.\
   The **Workers** page opens.
3. Locate the completed worker process that you want to re-run. At the end of the row, click **Re-run**.\
   **Note**: You can now apply column-level filters and narrow the workers list. Each column header includes a filter box to refine results dynamically.

Data Catalog re-submits the selected worker process and the **Job Status** column updates to display **Running**.
