# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-structured-data.md

# Processing structured data

Perform the following steps to process the structured data:

You must perform **Metadata Ingest**, **Data Profiling**, **Data Identification**, and **PII Detection** to process structured data. See [Processing data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data) to know more about the process.

1. Select the structured resource you want to investigate in Data Canvas.

   This can be a table or column.
2. Under the **Process** menu, choose **Process**.

   The Choose Process page opens with **Metadata Ingest**, **Data Profiling**, and **Data Identification** options. In addition, for Microsoft SQL, Oracle, and Snowflake databases, you see an additional option, **Usage Statistics**.
3. In the Metadata Ingest card, click **Start** to begin the metadata ingest process.

   You can view the status of metadata ingest on the **Manage Workers** page.

   **Note:** If you have already scanned more than 75% of your data quota, you see a message when you start the scan. Even if you cannot scan new data, you still can run Data Discovery or Data Identification on data you have already scanned. Databases do not have a data scan quota.
4. To perform the data profiling, click the **Data Profiling** card.

   The Profiling page opens with the following additional options to configure data profiling.

   **Note:** When configuring data profiling, it is considered a best practice to use the default settings as they are suitable for most situations. With the default settings, the data profiling is limited to 500,000 rows.

<table><thead><tr><th width="222.88885498046875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Extract samples</strong></td><td>Extracts a small random sample of data (typically ~200 rows) for preview and validation during profiling and displays it in the summary tab. It is generally used internally.</td></tr><tr><td><strong>Skip Recent (days)</strong></td><td>Skips profiling for recently profiled tables. For example, if the days field is set to 7, any table profiled within the last 7 days is skipped.</td></tr><tr><td><strong>Sample Type</strong></td><td><p>Defines how data is subset or filtered during profiling or ingestion, especially for large tables containing millions or billions of rows to improve performance and reduce storage requirements for data fingerprints, such as BitSets and HyperLogLog (HLL) structures.</p><p><strong>Note:</strong> The HLL structure has a fixed size of approximately 15–20 KB and is disabled by default.</p><ul><li><strong>Sample Clause</strong>: Profiles the sample data based on the <strong>percentage</strong> or <strong>rows</strong>*.</li><li><strong>First N Rows</strong>: Profiles the first N rows of the data resource.</li><li><strong>Every Nth Row</strong>: Profiles every Nth row of the data resource.</li><li><p><strong>Filter</strong>: Profiles data using a custom SQL <code>WHERE</code> clause, that helps to target specific subsets of data based on user-defined conditions.</p><ul><li><strong>Where Clause</strong>#: SQL condition used for data selection when Filter is enabled. For example, <code>country = 'USA'.</code></li></ul></li><li><strong>Clear</strong>: Resets the sampling configuration.</li></ul></td></tr><tr><td><strong>Split Job by Columns</strong></td><td>Splits profiling jobs by columns, allowing parallel processing for wide tables.</td></tr><tr><td><strong>Columns Per Job</strong></td><td>When splitting by columns is enabled, specifies the number of columns included in each job.</td></tr><tr><td><strong>Number of Tables Per Job</strong></td><td>Specifies the number of tables included in a single profiling job.</td></tr><tr><td><strong>Persist Threads</strong></td><td>Defines the number of threads used for persisting profiling results to improve performance.</td></tr><tr><td><strong>Persist File Threads</strong></td><td>Sets the number of threads for persisting profiling data into files for large datasets.</td></tr><tr><td><strong>Profile Threads</strong></td><td>Indicates the number of threads allocated for profiling tasks, enabling parallel task execution.</td></tr></tbody></table>

\*The **Sample Clause > Rows** option is supported only for the Microsoft SQL and Snowflake data sources.

\#The **Where Clause** feature is not supported for data sources using PostgreSQL. Additionally, The **Where Clause** does not support subqueries that reference different tables. Example:

```
SELECT * FROM commktg.cost_center_master WHERE cost_center_id IN (SELECT cost_center_id FROM commktg.dim_cost_center WHERE region_nm LIKE 'Da%')
```

5\. After you have updated the options as required, click **Start** to begin the profiling of the data.\
After profiling, you can go to the Summary tab to review extracted samples.

6\. To perform data identification, click the **Data Identification** card.\
**Important:** You must perform data profiling before proceeding with data identification. If data profiling was not done previously, Data Catalog highlights it as **Required**. You can start data profiling from the Data Identification card by clicking **Start**.

7\. Click **Select Methods** and select the **Dictionaries** and **Patterns**, click **Apply**, and then click **Start**.\
You can view the status of data identification on the Manage Workers page.

8\. (Optional) If you're working with Microsoft SQL, Oracle, or Snowflake databases and want to collect usage statistics, click the **Usage Statistics** card, choose a date range, and then click **Start**.\
You can view the status of the **Entity Usage** process on the **Manage Workers** page. After completion, the gathered information is accessible in the **Usage Statistics View** collection within Business Intelligence Database.

You have successfully profiled the data resource.

After **Data Profiling** and **Data Identification** is completed, go to Data Canvas to view the result of data profiling, such as:

* Statistical insights, such as the number of rows, unique values, null values, and duplicates in each column, and basic data distributions, such as the range and frequency of values.
* Better tagging and classification of data based on patterns, dictionaries, and rules.
* Detection of patterns, outliers, and anomalies within the data columns.

## Abilityto fetch profile results based on profiled status

It is possible to have an API to fetch by profiled status and another API to fetch by resource

* You can execute a query to retrieve entities information based on the profiledAt value.
* You can execute a query to retrive entities information information based on the profiling status: Success, failure, error state.

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2F69LPs8MJ1mZAlBhQzoL2%2Fimage.png?alt=media&#x26;token=7d60031c-3e07-46f2-9db9-387db2506f57" alt=""><figcaption></figcaption></figure>

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FWhQHjkfKs5PzpqbBAqTi%2Fimage.png?alt=media&#x26;token=c480c7b7-1f73-4991-85a6-d6f99d6422e0" alt=""><figcaption></figcaption></figure>

## PII Detection

Data Catalog supports the identification of Personally Identifiable Information (PII) columns in the JDBC Tables and CSV/TSV files using the PII Detection feature. Currently, it only supports Japanese and Korean languages. To know more, see PII Detection in [Processing data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data).

Perform the following procedure to identify PII data:

Before running the PII Detection process, ensure that you have executed the **Metadata Ingest** process for the selected JDBC table. This is required to make the schema and column-level metadata available for PII analysis.

1. In the left navigation menu, select **Data Canvas**.

   The Explore your data page opens, showing a list of available data sources and their respective data assets.
2. Select the structured resource (JDBC tables,CSV,TSV files) you want to investigate.

   **Note:** This feature currently supports only JDBC tables and CSV/TSV files  which has the content in the Korean and Japanese language.
3. Under the **Actions** menu, choose **Process**.

   The Choose Process page opens with **Metadata Ingest**, **Data Profiling**, **Data Identification**, and **PII Detection** options.
4. Click the **PII Detection** card, select **Japanese** or **Korean** from the **PII Detection Language** menu, and click **Start**.

   The PII Detection process starts. Data Catalog scans the selected JDBC tables or CSV/TSV files for column names that contain PII entities. You can view the worker status on the ManageWorkers page.

When the process is complete, and if PII data is identified:

* A new glossary titled **ML\_PII** is automatically created (if it does not already exist). If the **ML\_PII** glossary already exists, newly identified PII terms are added to it.
* Detected PII entities are tagged with relevant business terms from the **ML\_PII** glossary.
* These tags appear in the Business Terms panel of the respective columns.
