# Source: https://docs.acceldata.io/documentation/crawl-data-sources.md

# Crawl Data Sources

Crawling is the process of discovering and cataloging data assets from a connected data source. Once a connection is established, you can trigger a crawl job to scan the data source and identify all available datasets, such as databases, schemas, tables, or files.

The discovered assets are displayed in the **Discover Assets** page in ADOC for further exploration and analysis.

**Example**: If you connect Snowflake, you’ll see your databases, schemas, and tables listed on the **Discover Assets** page after the initial crawl.

## Types of Crawling

There are now two ways to crawl a data source:

1. **Full Crawling**: Scans all assets within a data source.
2. **Selective Crawling**: Lets you manually crawl specific assets within an existing data source.

## Full Crawling

A **Full Crawl** performs a comprehensive scan of all available assets in a connected data source. This is typically the first crawl performed after connecting the source. A full crawl collects metadata for:

- All databases or containers
- Schemas and folders
- Tables, views, or files

This ensures that the entire data source is registered and visible in **Discover Assets** in ADOC.

Note During the initial connection, there is no option to perform selective crawling. The full crawl must be completed first.

## Selective Crawling

After a full crawl is complete, you can now choose to **crawl specific assets** within a data source whenever needed. This helps reduce unnecessary scans, save time, and keep metadata up to date for assets that change frequently.

Selective Crawling is supported for the following data source:

- **ADLS (Azure Data Lake Storage)**
- **Snowflake**
- **Databricks**
- **BigQuery**
- **GCS (Google Cloud Storage)**
- **Amazon S3**

### When to Use Selective Crawling

Use selective crawling when:

- You only need to update metadata for a specific asset.
- You’ve recently added or modified a single database, schema, or table.
- You want to avoid re-crawling large sources with minimal changes.
- You’re troubleshooting data quality or lineage for a particular dataset.

### Example

If you’ve already performed a full crawl of your Snowflake source, you can later choose to crawl only **one specific database** instead of the entire connection.

This means:

- You don’t have to re-scan all schemas and tables.
- Only the selected database’s metadata is refreshed.
- The updated information appears in the **Discover Assets** view.

## How to Start Crawling

Follow these steps to start crawling a data source:

1. Navigate to **Register** from the left navigation panel and select the **Data Sources** tab.
2. Locate your data source card (for example, Snowflake or Databricks).
3. Click the  vertical ellipses icon on the data source card.
4. Select **Start Crawler**.
5. In the pop-up window, choose one of the following options:
    - **Full Crawl:** Perform a comprehensive scan of all assets.
    - **Selective Crawl:** (Enabled after the first full crawl) Crawl only selected assets for faster updates. This option is only available for some data sources (ADLS (Azure Data Lake Storage), Snowflake, Databricks, BigQuery, GCS (Google Cloud Storage), Amazon S3).

6. Click **Start Crawl** to begin.

Note You can perform selective crawling multiple times for different assets within the same data source, whenever needed.

During a selective crawl, any databases that have not been crawled before are automatically included. This ensures all newly discovered databases are registered in the system, even if you only select a subset of assets to crawl.

## Benefits of Selective Crawling

- **Efficiency:** Refresh only what’s needed instead of re-crawling everything.
- **Faster updates:** Quickly reflect recent changes in key datasets.
- **Flexibility:** Choose when and what to crawl based on business needs.
- **Accuracy:** Keep critical assets’ metadata up to date without impacting performance.