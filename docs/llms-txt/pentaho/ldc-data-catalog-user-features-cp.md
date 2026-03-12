# Source: https://docs.pentaho.com/pdc-use/ldc-data-catalog-user-features-cp.md

# Data Catalog user features

This article describes the Pentaho Data Catalog user interface and the tasks non-admin users can perform. Before proceeding, make sure that a Data Catalog service user or administrator has set up your catalog for you. Data Catalog builds a complete inventory of data assets in a data warehouse, automatically and securely. It provides:

* exact data discovery and faster delivery to an authenticated user.
* improved and simplified understanding of data quality.
* an inventory of all assets for efficient data repository governance.

Data Catalog complements data visualization, data discovery, and data wrangling tools by streamlining the collection and initial data quality checks of the data repository, making the data repository available to those tools for further processing.

## Data self-service

Data Catalog provides a rich interface for data self-service to help you find the best instances of the integrated data you are looking for. These services include:

### **Role-based access control**

Data Catalog roles give users the ability to perform specific actions, especially edit actions, and allow lines of business to restrict access to sensitive or confidential information. You can create named communities, such as US Business Users or Commercial Lending Business Users to fine-tune the actions users can perform, as well as to allow access to a subset of glossaries and data sources.

**Note:** The number of data sources you can add is limited by your license.

### **Business Terms**

You can discover metadata about files and fields and have Data Catalog associate fields to customer's business terms. You can associate business terms with data elements, business rules, related terms, and custom properties to form a comprehensive view of the organization’s business concepts and data landscape.

### **Data quality metrics and statistics**

Data Catalog's profiling processes produce and present detailed data quality metrics and statistics that help you decide if the data is useful, valid, and complete, without having to write code to graph each field in the file.

### **User roles**

User roles in Data Catalog are used for access control and permissions management. They help control who can view, edit, or delete items in the Data Catalog and ensure data security.

**Note:** The number of Expert user roles you can assign to users is limited by your license. The Expert user roles are:

* Business Steward
* Data Steward
* Admin
* Data Developer

### **Table creation**

When you find a file you are interested in, you can create a table for that file. This ability is useful for non-technical users to find the files that contain the data that they need, create a table and use a tool like Grafana to visualize the data without any added efforts.

## Data inventory

Behind Data Catalog’s self-service user interface is an engine that profiles the data repository and enriches it by propagating terms created by users. Data Catalog identifies the formats of the resources and profiles their contents, creating an inventory of data assets in the data warehouse securely.

### **Profiling**

Most of the data-curation process entails writing code to profile and graph data. Data Catalog automates this process, improving the productivity of data engineers and data scientists.

Data profiling and discovery are the processes in which Data Catalog examines file data and gathers statistics about the data. It profiles data in the cluster, and uses its algorithms to compute detailed properties, including field-level data quality metrics, and data statistics. The resulting inventory includes rich metadata for delimited files, like JSON, and Parquet, and files compressed with supported compression algorithms such as gzip.

**Note:** The amount of data you can scan is limited by your license. Databases do not have a data scan quota.

### **Sensitive data discovery**

Sensitive data residing in the data cluster presents a sizable liability if it is not protected and managed. The algorithms in Data Catalog identify sensitive data throughout the data clusters as a part of profiling with minimal additional processing overhead. Identification is the first step, and often the most difficult step in the process of protecting sensitive data. You cannot protect sensitive data unless you know where it resides. Data Catalog identifies sensitive data and facilitates the next step of protecting it through masking, encryption, or quarantine.

## Data quality

You can discover data quality metrics automatically using large-scale profiling, such as discovering the number of nulls in a data column or cardinality. For example, you can assess the number of values that should be in a field versus the actual numbers that have been profiled.

**Note:** Data Catalog writes profiling process notifications to the log files.

## Data governance

Data Catalog provides data governance by securing access to the data, by managing metadata creation, enrichment, and approval, and by linking physical data to business-related terminology.

### Securing access to data

In Data Catalog, you can protect resources with secured access using glossaries. A glossary is a logical grouping of business terms that you can assign to a specific project user group. Once you have set up roles for glossaries, you can use them to limit access to data via specific roles and users.

### Managing metadata creation, enrichment, and approval

By default, users with the Data Steward role can only associate terms with data, while users with the Business Steward role can create new metadata by adding business terms, term hierarchies, and custom properties. Users with the Business Steward role can also perform these functions.

### Linking physical data to business-defined terms

In Data Catalog, with applicable permissions, you can manually tag data directly in the user interface. To learn more about this process, see the [**Administer Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

## Reporting and data visualization

Reporting in Data Catalog usually is done through dashboards using third-party BI tools. Dashboards further extend the visual discovery and relationship discovery capabilities of the Data Catalog in several ways. They also provide a means to add customized insight assets unique to the organization.

### Business Intelligence Database

Data Catalog includes the **Business Intelligence Database (BIDB)**, which stores aggregated metadata from connected sources. BIDB enables you to query, analyze, and create dashboards by connecting through standard BI tools using **JDBC** or **ODBC**.

PDC has two different implementations of BIDB depending on the version:

* [**PostgreSQL-based BIDB**](#bidb-in-pdc-10.2.5-and-later-postgresql-based) in **PDC 10.2.5 and later**.
* [**MongoDB-based BIDB**](#bidb-in-versions-prior-to-pdc-10.2.5-mongodb-based) in versions earlier than **PDC 10.2.5**

For more information on how to connect to BIDB, see [Connect to Business Intelligence Database (BIDB)](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#connect-to-business-intelligence-database-bidb) in the [Advanced configuration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp) section in [Administer Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/) guide.

### BIDB in PDC 10.2.5 and later (PostgreSQL-based) <a href="#bidb-in-pdc-10.2.5-and-later-postgresql-based" id="bidb-in-pdc-10.2.5-and-later-postgresql-based"></a>

Starting with **PDC 10.2.5**, BIDB uses **PostgreSQL** as its underlying database. This simplifies connectivity because only standard **PostgreSQL authentication** is required. The services used in earlier versions (BIDB - MongoDB prior PDC 10.2.5), such as **bi-mongo** and **mongo-bi-connector**, are no longer part of the architecture. Instead, users connect directly to BIDB using JDBC or ODBC drivers for PostgreSQL. This streamlined setup provides easier integration while maintaining full compatibility with BI tools for reporting, data access, and dashboard creation.

The PostgreSQL-based BIDB contains a rich set of **tables and views** that organize aggregated metadata collected from data sources. These objects are structured into logical categories to simplify navigation and analysis. Each category focuses on a specific aspect of catalog operations, such as core entity definitions, relationships, cross-references, control and configuration, usage statistics, and analysis/monitoring.

#### Analysis and monitoring <a href="#analysis-and-monitoring" id="analysis-and-monitoring"></a>

The tables or views in the Analysis and monitoring category provides insights into data quality, duplication, file characteristics, and usage patterns within Pentaho Data Catalog (PDC). These views are designed to help administrators, data stewards, and analysts understand how data is distributed, identify anomalies, and monitor health at scale.

The following views and tables belong to this category:

* Checksum Aggregated View
* Duplicate Files View
* Entities Extension Count View
* Entities Temperature Count View

**Checksum Aggregated View**

The `checksum_aggregated_view` is a summarized view that reports, per entity, the number of duplicate files detected and their combined size. It’s populated from the entity-level checksums calculated during unstructured-content processing. With the `checksum_aggregated_view` you can:

* Quickly quantify duplicate-file impact by entity (for example, application, project, owner).
* Prioritize cleanup or tiering by targeting entities with the largest duplicate footprint.
* Feed storage dashboards or alerts to show rising duplication over time.

The following table shows the details of the data available in `checksum_aggregated_view`.

<table><thead><tr><th>Field</th><th width="298">Description</th><th width="99">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Identifier of the entity the duplication stats are calculated for (derived from <code>entities_master_view</code>).</td><td>String</td><td><code>263481a48eb70e8e9b0cf983b0576b1c</code></td></tr><tr><td><code>duplicateFilesCount</code></td><td>Total number of duplicate files detected for the entity.</td><td>Integer</td><td><code>5</code></td></tr><tr><td><code>duplicateFilesSize</code></td><td>Sum of the sizes (in bytes) of all duplicate files for the entity.</td><td>Integer</td><td><code>9519205</code></td></tr></tbody></table>

* `duplicateFilesSize` is in bytes; convert to MB/GB when presenting to end users.
* There is one row per entity. Use the `_id` to join back to entity details (name, path, owner) from `entities_master_view`.

**Duplicate Files View**

The `duplicate_files_view` is a detailed view listing duplicate files detected in Data Catalog. Each row represents an individual duplicate file, including its unique identifier, the group of duplicates it belongs to, and file-level metadata such as size and Timestamps. The `duplicate_files_view`:

* Provides file-level visibility into duplicates, beyond aggregated stats.
* Allows investigation into which specific files are duplicates and how they are grouped.
* Supports actions such as cleaning up redundant files or analyzing duplicate storage consumption.
* Can be joined with `entities_master_view` or `checksum_aggregated_view` for entity-level reporting.

The following table shows the details of the data available in `duplicate_files_view`.

<table><thead><tr><th width="121">Field</th><th width="302">Description</th><th width="127">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Internal identifier for the duplicate file record.</td><td>String (UUID)</td><td><code>1</code></td></tr><tr><td><code>EntityId</code></td><td>Identifier of the entity (from <code>entities_master_view</code>) that the file belongs to.</td><td>String (UUID)</td><td><code>83d3a83c-0548-46ef-80f4-3000e18680ca</code></td></tr><tr><td><code>GroupId</code></td><td>Identifier for the duplicate group. All files with the same checksum share the same group ID.</td><td>String</td><td><code>263481a48eb70e8e9b0cf983b0576b1c</code></td></tr><tr><td><code>FileCount</code></td><td>Number of files in the duplicate group.</td><td>Integer</td><td><code>5</code></td></tr><tr><td><code>Size</code></td><td>Size of the duplicate file (in bytes).</td><td>Integer</td><td><code>670</code></td></tr><tr><td><code>CreatedAt</code></td><td>Timestamp when the record was created.</td><td>Timestamp</td><td><code>2025-02-25 10:59:50.000 +0530</code></td></tr><tr><td><code>ModifiedAt</code></td><td>Timestamp when the record was last updated.</td><td>Timestamp</td><td><code>2025-02-25 10:59:50.000 +0530</code></td></tr></tbody></table>

* Use `GroupId` to group files together and identify all duplicates of a given checksum.
* Combine with `checksum_aggregated_view` to compare group-level totals with individual file records.
* `EntityId` can be joined with `entities_master_view` to resolve details like entity name, type, and owner.

**Entities Extension Count View**

The `entities_extension_count_view` is a BIDB analysis table that summarizes how many files of each extension exist per entity. It’s built so you (or reporting tools) can quickly answer questions like “how many PDFs do we have for this application?” without rescanning raw files. The `entities_extension_count_view` you can:

* Spot risky or unwanted types (for example, too many `.exe`, `.bat`, `.js`).
* Prioritize cleanup or archiving based on the mix of extensions.
* Track normalization efforts (for example, converting many small `.xls` to `.xlsx`/`.csv`).
* Feed dashboards with extension distribution by entity, application, or business area.

The following table shows the details of the data available in `duplicate_files_view`.

<table><thead><tr><th width="141">Field</th><th width="281">Description</th><th width="147">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>entity_id</code></td><td>The PDC entity identifier this row summarizes (dataset/folder/report, and so on).</td><td>UUID (String in some tools)</td><td><code>83d3a83c-0548-46ef-80f4-3000e18680ca</code></td></tr><tr><td><code>extension</code></td><td>Normalized file extension (lowercase, no leading dot).</td><td>String</td><td><code>pdf</code></td></tr><tr><td><code>file_count</code></td><td>Count of files of this extension within the entity.</td><td>Integer</td><td><code>127</code></td></tr><tr><td><code>total_size_bytes</code>*</td><td>Sum of sizes of those files (if available in your deployment).</td><td>Integer</td><td><code>15432987</code></td></tr><tr><td><code>created_at</code>*</td><td>When this summary row was first created.</td><td>Timestamp with time zone</td><td><code>2025-02-25 10:59:48+05:30</code></td></tr><tr><td><code>updated_at</code>*</td><td>When this summary row was last refreshed.</td><td>Timestamp with time zone</td><td><code>2025-03-06 15:44:46+05:30</code></td></tr></tbody></table>

*\* Optional columns, present in many installations, but not strictly required for using the view.*

**Entities Temperature Count View**

The `entities_temperature_count_view` is a summary view that counts the number of files grouped by their temperature classification (for example, hot, warm, cold) for each entity. Temperature represents data access frequency or recency; hot files are frequently accessed, while cold files are rarely used. The `entities_temperature_count_view`:

* Gives visibility into how active or dormant data is within each entity.
* Helps prioritize storage optimization: cold data can be archived or tiered to cheaper storage.
* Supports governance and lifecycle management by quantifying “stale” vs. “active” content.
* Is useful for dashboards showing entity-level data temperature distribution.

The following table shows the details of the data available in `entities_temperature_count_view`.

<table><thead><tr><th width="147">Field</th><th width="260">Description</th><th width="143">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>entity_id</code></td><td>Identifier of the entity this temperature count belongs to.</td><td>UUID</td><td><code>83d3a83c-0548-46ef-80f4-3000e18680ca</code></td></tr><tr><td><code>temperature</code></td><td>Data temperature classification (for example, <code>hot</code>, <code>warm</code>, <code>cold</code>).</td><td>String</td><td><code>cold</code></td></tr><tr><td><code>file_count</code></td><td>Number of files in the entity that fall into this temperature.</td><td>Integer</td><td><code>1572</code></td></tr><tr><td><code>created_at</code>*</td><td>When this summary row was created.</td><td>Timestamp with time zone</td><td><code>2025-02-25 10:59:48+05:30</code></td></tr><tr><td><code>updated_at</code>*</td><td>When this summary row was last updated.</td><td>Timestamp with time zone</td><td><code>2025-03-06 15:44:46+05:30</code></td></tr></tbody></table>

<sup>\*</sup>Optional columns depending on your deployment.

#### Control and configuration <a href="#control-and-configuration" id="control-and-configuration"></a>

The tables or views in the Control and configuration category, manage system-level settings, reference mappings, and classification rules within Data Catalog. These objects provide supporting metadata that helps standardize costs, organize data sources, and enable user-defined categorizations.

The following views and tables belong to this category:

* Currency Exchange Rates
* Datasource Category Mapping
* Entities Custom Categorization

**Currency Exchange Rates**

The `currency_exchange_rates` is a reference table in BIDB that stores currency exchange rates used for normalizing costs, sizes, or policy values to a common standard (USD). This allows consistent reporting across entities or applications regardless of local currency usage. The `currency_exchange_rates`:

* Provides a single source of truth for currency conversions.
* Enables dashboards to show monetary values in a consistent currency.
* Supports analysis where datasets or policies originate from multi-currency environments.
* Helps with global governance, chargeback, or cost-allocation use cases.

The following table shows the details of the data available in `currency_exchange_rates`.

| Field                 | Description                                                 | Data Type | Example Value         |
| --------------------- | ----------------------------------------------------------- | --------- | --------------------- |
| `currency_symbol`     | Currency symbol or code identifying the currency.           | String    | `$`, `€`, `¥`         |
| `ConversionRateToUSD` | Conversion multiplier to USD. Always relative to 1 USD = 1. | Float     | `1`, `1.08`, `0.0064` |

**Data Source Category Mapping**

The `datasource_category_mapping` is a BIDB configuration table that maps each data source type (for example, FS, SMB, ORACLE) to a logical category. This categorization enables Data Catalog to organize diverse data sources into higher-level groups, such as File Servers, Databases, HDFS, and others. The `datasource_category_mapping`:

* Simplifies filtering and reporting by grouping similar data source types together.
* Supports governance and lineage views by showing data source categories instead of raw connection types.
* Enables dashboards and policy rules to apply at a category level (for example, treat all File Servers the same regardless of FS, SMB, or NFS).
* Provides flexibility to add or extend categories when integrating new technologies.

The following table shows the details of the data available in `datasource_category_mapping`.

<table><thead><tr><th width="145">Field</th><th width="266">Description</th><th width="104">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>DataSourceType</code></td><td>Internal identifier of the specific data source type.</td><td>String</td><td><code>FS</code>, <code>SMB</code>, <code>NFS</code>, <code>ORACLE</code></td></tr><tr><td><code>category</code></td><td>Logical grouping of the data source type.</td><td>String</td><td><code>File Servers (On-Prem / Cloud)</code>, <code>Databases (On-Prem / Cloud)</code></td></tr></tbody></table>

**Entities Custom Categorization**

The `entities_custom_categorization` is a reference (master) table that lets you define your own high‑level categories for entities (for example, *Temperature*, *PII*) and map each category to one or more Business Glossaries or Glossary Categories by name. The `entities_custom_categorization`:

* Drives consistent, business‑friendly grouping in dashboards and views (for example, “Temperature terms across glossaries”).
* Enables lightweight governance, admins can steer which glossaries (or sub‑categories) roll up into organizational buckets like *PII* or *Financials*.
* Keeps the mapping externalized, so you can update categorizations without touching source entities.

The following table shows the details of the data available in `entities_custom_categorization`.

<table><thead><tr><th width="144">Field</th><th width="291">Description</th><th width="102">Data type</th><th>Example value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Row identifier for the mapping record. Can be natural (e.g., “ec001”).</td><td>String</td><td><code>ec001</code></td></tr><tr><td><code>EntityCategory</code></td><td>Your business bucket that entities/terms should roll up to.</td><td>String</td><td><code>Temperature</code></td></tr><tr><td><code>GlossaryName</code></td><td>Name of the glossary <strong>or</strong> glossary category that participates in the category.</td><td>String</td><td><code>Business</code>, <code>Sensitive Data</code>, <code>Temperature Hierarchy</code></td></tr><tr><td><code>GlossaryType</code></td><td>What <code>GlossaryName</code> refers to: <code>glossary</code> (a whole glossary) or <code>category</code> (a category under a glossary).</td><td>String</td><td><code>glossary</code>, <code>category</code></td></tr></tbody></table>

* Keep `GlossaryType` accurate (`glossary` vs `category`) to avoid over/under‑matching.
* Treat `_id` as a stable key so downstream references don’t break when names change.
* Consider a unique constraint on (`EntityCategory`,`GlossaryName`,`GlossaryType`) to prevent duplicates.

#### Core entity tables <a href="#core-entity-tables" id="core-entity-tables"></a>

The tables or views in the Core entity tables category, are the foundational views that store and summarize metadata for all entities ingested into Pentaho Data Catalog (PDC). These tables provide the central reference point for entity definitions, attributes, statistics, and aggregations across structured and unstructured data sources.

The following tables and views belong to this category:

* Entities Aggregated View
* Entities Master View
* Entities Summary View

**Entities Aggregated View**

The `entities_aggregated_view` is a summary view in BIDB that provides aggregated statistics for both structured and unstructured entities. Instead of showing row-level detail, it consolidates information such as counts of objects, data sources, files, file formats, and size statistics. This view is designed to power dashboards and high-level reporting without repeatedly scanning raw entity data. With the `entities_aggregated_view` you can:

* Quickly compare structured vs. unstructured data volumes.
* Understand storage footprint (average and maximum resource sizes).
* Track discovery metrics (tables, parent paths, data sources, collections).
* Feed governance reports with overall trends instead of record-level data.
* Identify changes over time by monitoring “last modified” metadata.

The following table shows the details of the data available in `entities_aggregated_view`.

<table><thead><tr><th width="108">Field</th><th width="317">Description</th><th width="112">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>Attribute</code></td><td>The type of metric being tracked (for example, <code>Object Ids</code>, <code>Files</code>, <code>DataSources</code>).</td><td>String</td><td><code>Files</code></td></tr><tr><td><code>Type</code></td><td>Indicates whether the metric applies to <strong>Structured</strong> or <strong>Unstructured</strong> data.</td><td>String</td><td><code>Structured</code> / <code>Unstructured</code></td></tr><tr><td><code>Value</code></td><td>The aggregated value for the attribute and type.</td><td>Alphanumeric</td><td><code>4920</code>, <code>1665124</code>, <code>"2025-08-19T12:09:14.000+00:00"</code></td></tr></tbody></table>

Following are the some of the common attributes present in the `entities_aggregated_view`:

* **Object Ids**: Count of unique object identifiers.
* **DataSources**: Number of connected data sources contributing entities.
* **Parent Paths**: Number of parent paths (directories, schemas).
* **Tables**: Number of structured database tables.
* **Files**: Count of files discovered.
* **File Extensions**: Number of unique file extensions.
* **File Formats**: Number of unique file formats.
* **Discovered Collections**: Number of PDC collections discovered automatically.
* **Average Resource Size**: Average size of resources within category.
* **Maximum Resource Size**: Maximum size observed for a resource.
* **Last Created**: Timestamp of last created unstructured resource.
* **Last Modified**: Timestamp of last modification for unstructured resource.
* **Last Accessed**: Timestamp of last access (if tracked).

{% hint style="info" %}
Because values in this view are aggregated, they are best for dashboards and summaries. For detailed drill-down (e.g., which files or entities are biggest), join with entities\_master\_view or other detailed tables.
{% endhint %}

**Entities Master View**

The `entities_master_view` is the primary entity table in BIDB that stores comprehensive metadata about every discovered entity in PDC, including files, tables, schemas, and unstructured resources. It consolidates identifiers, data source info, profiling details, lineage-related attributes, and system metadata (size, Timestamps, ownership). This view is the foundation for all reporting, profiling, and lineage features in Data Catalog. The `entities_master_view`:

* Provides a single source of truth for all discovered entities across structured and unstructured data.
* Enables detailed profiling queries (row counts, null counts, min/max/avg values, etc.).
* Facilitates lineage and governance tracking with attributes like Parent, ParentPath, DataSourceId, and FQDN.
* Supports search, categorization, and monitoring in dashboards.
* Allows users to drill down from aggregated views (`entities_summary_view`, `entities_aggregated_view`) to entity-level detail.

The following table shows the details of the data available in `entities_master_view`.

<table><thead><tr><th width="147">Field Name</th><th width="306">Description</th><th width="109">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Unique identifier of the entity</td><td>UUID</td><td><code>e34d9ffb-5095-49c0-8545-f9d14c14c7d4</code></td></tr><tr><td><code>Name</code></td><td>Name of the entity (file, table, object)</td><td>String</td><td><code>Test_1MB_12659.dat</code></td></tr><tr><td><code>Type</code></td><td>Type of entity (FILE, TABLE, VIEW, etc.)</td><td>String</td><td><code>FILE</code></td></tr><tr><td><code>Parent</code></td><td>Parent entity identifier</td><td>UUID</td><td><code>af8064fa-af85-43fe-baf3-5fee11590301</code></td></tr><tr><td><code>ResourceType</code></td><td>Whether entity is Structured or Unstructured</td><td>String</td><td><code>Unstructured</code></td></tr><tr><td><code>DataSourceId</code></td><td>ID of the data source</td><td>UUID</td><td><code>68a567f3010fdaaed8384df4</code></td></tr><tr><td><code>DataSourceName</code></td><td>Name of the data source</td><td>String</td><td><code>AWS_S3_1</code></td></tr><tr><td><code>DataSourceType</code></td><td>Type of source system</td><td>String</td><td><code>AWS</code></td></tr><tr><td><code>DataSourceCostPerTbCurrency</code></td><td>Currency for cost tracking</td><td>String</td><td><code>$</code></td></tr><tr><td><code>DataSourceCostPerTbPrice</code></td><td>Cost per TB in source</td><td>Integer</td><td><code>0</code></td></tr><tr><td><code>DataSourceAffinityId</code></td><td>Affinity group for source</td><td>String</td><td><code>DEFAULT</code></td></tr><tr><td><code>DataProfileStatus</code></td><td>Status of profiling</td><td>String</td><td><code>Completed</code></td></tr><tr><td><code>DataProfiled</code></td><td>Indicates if profiling is done</td><td>Boolean</td><td><code>FALSE</code></td></tr><tr><td><code>LastUpdate</code></td><td>Last update Timestamp</td><td>Timestamp</td><td><code>2025-08-20 11:54:20.533 +0530</code></td></tr><tr><td><code>ProductName</code></td><td>Product associated</td><td>String</td><td>PDC</td></tr><tr><td><code>ProductVersion</code></td><td>Version of product</td><td>String</td><td>10.2</td></tr><tr><td><code>DriverName</code></td><td>Driver used</td><td>String</td><td><code>com.mysql.jdbc.Driver</code></td></tr><tr><td><code>Url</code></td><td>Connection URL</td><td>String</td><td><code>migration_020125191846</code></td></tr><tr><td><code>ParentName</code></td><td>Name of parent</td><td>String</td><td>RetailDB</td></tr><tr><td><code>TotalTables</code></td><td>Total tables (for DB entities)</td><td>Integer</td><td><code>5</code></td></tr><tr><td><code>TotalColumns</code></td><td>Total columns</td><td>Integer</td><td><code>23</code></td></tr><tr><td><code>SchemaName</code></td><td>Schema name (if structured)</td><td>String</td><td><code>COMMKTG</code></td></tr><tr><td><code>DatabaseName</code></td><td>Database name (if structured)</td><td>String</td><td><code>Demo_DB</code></td></tr><tr><td><code>LastUpdateStatistics</code></td><td>Last time stats updated</td><td>Timestamp</td><td><code>2025-08-20 11:54:20.533 +0530</code></td></tr><tr><td><code>RowCount</code></td><td>Number of rows (structured)</td><td>BigInteger</td><td><code>116</code></td></tr><tr><td><code>NullCount</code></td><td>Null value count</td><td>BigInteger</td><td><code>3</code></td></tr><tr><td><code>Cardinality</code></td><td>Distinct values count</td><td>BigInteger</td><td><code>0</code></td></tr><tr><td><code>Hll</code></td><td>HyperLogLog cardinality estimate</td><td>BigInteger</td><td><code>0</code></td></tr><tr><td><code>BlankCount</code></td><td>Count of blanks</td><td>BigInteger</td><td><code>5</code></td></tr><tr><td><code>Min</code></td><td>Minimum value (numeric/date)</td><td>String</td><td><code>24</code></td></tr><tr><td><code>Max</code></td><td>Maximum value</td><td>String</td><td><code>1145</code></td></tr><tr><td><code>AvgValue</code></td><td>Average value</td><td>NUMERIC</td><td><code>125</code></td></tr><tr><td><code>MinWidth</code></td><td>Minimum width (for strings)</td><td>Integer</td><td><code>13</code></td></tr><tr><td><code>MaxWidth</code></td><td>Maximum width</td><td>Integer</td><td><code>56</code></td></tr><tr><td><code>AvgWidth</code></td><td>Average width</td><td>Integer</td><td><code>34</code></td></tr><tr><td><code>ColumnsCount</code></td><td>Number of columns</td><td>Integer</td><td><code>12</code></td></tr><tr><td><code>CheckClause</code></td><td>Constraint details</td><td>String</td><td><code>CHECK (Age >= 18)</code></td></tr><tr><td><code>TableName</code></td><td>Table name (if structured)</td><td>String</td><td><code>DIM_CUSTOMER</code></td></tr><tr><td><code>DataType</code></td><td>Data type of column</td><td>String</td><td><code>String</code></td></tr><tr><td><code>TypeName</code></td><td>Database column type</td><td>String</td><td><code>nvarchar</code></td></tr><tr><td><code>ColumnSize</code></td><td>Size of column</td><td>Integer</td><td>11<br><br></td></tr><tr><td><code>BufferLength</code></td><td>Buffer length</td><td>Integer</td><td><code>18</code></td></tr><tr><td><code>DecimalDigits</code></td><td>Decimal precision</td><td>Integer</td><td><code>2</code></td></tr><tr><td><code>NumPrecRadix</code></td><td>Precision radix</td><td>Integer</td><td><code>0</code></td></tr><tr><td><code>IsNullable</code></td><td>Whether column accepts null</td><td>Boolean</td><td><code>FALSE</code></td></tr><tr><td><code>OrdinalPosition</code></td><td>Column position</td><td>Integer</td><td><code>-1</code></td></tr><tr><td><code>IsPrimaryKey</code></td><td>If column is primary key</td><td>Boolean</td><td><code>FALSE</code></td></tr><tr><td><code>IsForeignKey</code></td><td>If column is foreign key</td><td>Boolean</td><td><code>FALSE</code></td></tr><tr><td><code>Path</code></td><td>Path of entity (filesystem/db)</td><td>String</td><td><code>data-service-test/.../Test_1MB_12659.dat</code></td></tr><tr><td><code>ParentPath</code></td><td>Parent path</td><td>String</td><td><code>data-service-test/pentaho_migration/migration_020125191846</code></td></tr><tr><td><code>PathType</code></td><td>Path type (FILE/FOLDER)</td><td>String</td><td><code>FILE</code></td></tr><tr><td><code>FileExtension</code></td><td>File extension</td><td>String</td><td><code>dat</code></td></tr><tr><td><code>Size</code></td><td>File size</td><td>BigInteger</td><td><code>1064000</code></td></tr><tr><td><code>Flags</code></td><td>Flags if any</td><td>Integer</td><td><code>1</code></td></tr><tr><td><code>Owner</code></td><td>File/DB owner</td><td>String</td><td><code>dbo</code></td></tr><tr><td><code>Group</code></td><td>File group</td><td>String</td><td><code>finance-team</code></td></tr><tr><td><code>SymLinkTarget</code></td><td>Symlink target</td><td>String</td><td><code>/mnt/shared/finance/customers.csv</code></td></tr><tr><td><code>FileType</code></td><td>File type</td><td>String</td><td><code>dat</code></td></tr><tr><td><code>CreatedAt</code></td><td>Creation Timestamp</td><td>Timestamp</td><td><code>2025-01-03 00:49:02.000 +0530</code></td></tr><tr><td><code>ModifiedAt</code></td><td>Last modified Timestamp</td><td>Timestamp</td><td><code>2025-08-20 11:45:33.527 +0530</code></td></tr><tr><td><code>AccessedAt</code></td><td>Last accessed Timestamp</td><td>Timestamp</td><td><code>2025-08-21 11:45:33.527 +0530</code></td></tr><tr><td><code>ScannedAt</code></td><td>Time scanned by PDC</td><td>Timestamp</td><td><code>2025-08-20 11:45:33.527 +0530</code></td></tr><tr><td><code>IsSymlink</code></td><td>Whether entity is symlink</td><td>Boolean</td><td><code>TRUE</code></td></tr><tr><td><code>LinkType</code></td><td>Type of symlink</td><td>String</td><td><code>Soft Link</code></td></tr><tr><td><code>PhysicalLocation</code></td><td>Physical location path</td><td>String</td><td><code>/data/warehouse/customers.parquet</code></td></tr><tr><td><code>Title</code></td><td>Document title</td><td>String</td><td>Customer Profile Report</td></tr><tr><td><code>Author</code></td><td>Document author</td><td>String</td><td>John Doe</td></tr><tr><td><code>Subject</code></td><td>Document subject</td><td>String</td><td>Sutomer Segmentation</td></tr><tr><td><code>Application</code></td><td>Source application</td><td>String</td><td>Salesforce</td></tr><tr><td><code>Producer</code></td><td>Producer application</td><td>String</td><td>Informetica</td></tr><tr><td><code>Version</code></td><td>Document version</td><td>String</td><td>v2.1</td></tr><tr><td><code>DocumentSize</code></td><td>Document size</td><td>BigInteger</td><td><code>1245</code></td></tr><tr><td><code>PageSize</code></td><td>Page size</td><td>Integer</td><td><code>14</code></td></tr><tr><td><code>PageCount</code></td><td>Number of pages</td><td>Integer</td><td><code>15</code></td></tr><tr><td><code>Company</code></td><td>Company metadata</td><td>String</td><td>Company</td></tr><tr><td><code>Paragraphs</code></td><td>Count of paragraphs</td><td>Integer</td><td><code>78</code></td></tr><tr><td><code>Lines</code></td><td>Line count</td><td>Integer</td><td><code>178</code></td></tr><tr><td><code>Words</code></td><td>Word count</td><td>Integer</td><td><code>1567</code></td></tr><tr><td><code>Characters</code></td><td>Character count</td><td>Integer</td><td><code>16754</code></td></tr><tr><td><code>CharactersWithSpaces</code></td><td>Characters including spaces</td><td>Integer</td><td><code>1345</code></td></tr><tr><td><code>Language</code></td><td>Language detected</td><td>String</td><td><code>US</code></td></tr><tr><td><code>Checksum</code></td><td>Data checksum</td><td>String</td><td><code>f5a8d7e6c2b1a3d4</code></td></tr><tr><td><code>PropertiesChecksum</code></td><td>Property checksum</td><td>String</td><td><code>9c3b7d8a5f6e1c2d</code></td></tr><tr><td><code>ChildDirs</code></td><td>Number of child dirs</td><td>Integer</td><td>8<br><br></td></tr><tr><td><code>ChildFiles</code></td><td>Number of child files</td><td>Integer</td><td><code>24</code></td></tr><tr><td><code>ChildDirSize</code></td><td>Child directory size</td><td>BigInteger</td><td><code>1567</code></td></tr><tr><td><code>ChildFileSize</code></td><td>Child file size</td><td>BigInteger</td><td><code>1569</code></td></tr><tr><td><code>TotalChildDirs</code></td><td>Total child directories</td><td>Integer</td><td><code>134</code></td></tr><tr><td><code>TotalChildFiles</code></td><td>Total child files</td><td>Integer</td><td><code>1897</code></td></tr><tr><td><code>TotalChildDirSize</code></td><td>Total child dir size</td><td>BigInteger</td><td><code>1467</code></td></tr><tr><td><code>TotalChildFileSize</code></td><td>Total child file size</td><td>BigInteger</td><td><code>1897</code></td></tr><tr><td><code>LocationName</code></td><td>Location name</td><td>String</td><td><code>US</code></td></tr><tr><td><code>LocationStreetAddress</code></td><td>Street address</td><td>String</td><td>street address 1</td></tr><tr><td><code>LocationStreetAddress2</code></td><td>Street address 2</td><td>String</td><td>street address 2</td></tr><tr><td><code>LocationLocalityCity</code></td><td>City</td><td>String</td><td>Tempe</td></tr><tr><td><code>LocationStateProvince</code></td><td>State</td><td>String</td><td>AZ</td></tr><tr><td><code>LocationPostalCode</code></td><td>Postal code</td><td>String</td><td>85281</td></tr><tr><td><code>LocationCountry</code></td><td>Country</td><td>String</td><td><code>US</code></td></tr><tr><td><code>CostPerTbFrequency</code></td><td>Cost calculation frequency</td><td>String</td><td><code>month</code></td></tr><tr><td><code>TotalCapacity</code></td><td>Total capacity</td><td>BigInteger</td><td><code>0</code></td></tr><tr><td><code>FqdnDisplay</code></td><td>Fully qualified display name</td><td>String</td><td><code>AWS_S3_1/data-service-test/.../Test_1MB_12659.dat</code></td></tr><tr><td><code>OwnerFirstName</code></td><td>Owner’s first name</td><td>String</td><td>John</td></tr><tr><td><code>OwnerLastName</code></td><td>Owner’s last name</td><td>String</td><td>Doe</td></tr><tr><td><code>OwnerEmail</code></td><td>Owner email</td><td>String</td><td>John.Doe@abcd.com</td></tr><tr><td><code>OwnerUserName</code></td><td>Owner username</td><td>String</td><td>JDoe</td></tr><tr><td><code>OwnerIsDeleted</code></td><td>If owner deleted</td><td>Boolean</td><td><code>FALSE</code></td></tr><tr><td><code>UserAccessDetails</code></td><td>User access details JSON</td><td>JSON / Text</td><td> </td></tr><tr><td><code>Sensitivity</code></td><td>Data sensitivity classification</td><td>String</td><td>High. Low, Medium</td></tr><tr><td><code>Uniqueness</code></td><td>The Uniqueness of the values</td><td>Double precision</td><td>3.33</td></tr><tr><td><code>Density</code></td><td>Percentage of non-null and non-empty values in the field</td><td>Double precision</td><td>100</td></tr><tr><td><code>Selectivity</code></td><td>Average selectivity across all values</td><td>Double precision</td><td>6.75</td></tr><tr><td><code>LexicalMin</code></td><td>The Minimum value in string/text/VARCHAR values</td><td>String</td><td>00185faa-2760-4218-9bf5-db301acf8274</td></tr><tr><td><code>LexicalMax</code></td><td>The Maximum value in string/text/VARCHAR values</td><td>String</td><td>ffcfa457-00c2-4405-9837-ac2781549c7e</td></tr></tbody></table>

Because `entities_master_view` is very large, use filters (`WHERE`) whenever possible to avoid slow queries. It’s best joined with:

* `entities_summary_view` → for simplified reporting.
* `entities_aggregated_view` → for high-level stats.
* `duplicate_files_view` → for deduplication insights.

**Entities Summary View**

The `entities_summary_view` is a simplified entity view in BIDB that stores high-level metadata about entities such as files, tables, and datasets. Unlike `entities_master_view`, which contains comprehensive metadata, this view provides a lightweight snapsh**ot** focused on identifiers and classification attributes. The `entities_summary_view`:

* Provides quick lookups of entity metadata without querying the heavy master view.
* Useful for dashboards, counts, and reporting at the entity level.
* Supports relationship queries when joined with other views (for example, policies, applications).
* Reduces query execution time, making it suitable for frequent reporting and analytics jobs.

The following table shows the details of the data available in `entities_summary_view`.

<table><thead><tr><th width="134">Field</th><th width="330">Description</th><th width="94">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Primary key identifier for the entity.</td><td>String</td><td><code>e34d9ffb-5095-49c0-8545-f9d14c14c7d4</code></td></tr><tr><td><code>Name</code></td><td>Name of the entity.</td><td>String</td><td><code>Test_1MB_12659.dat</code></td></tr><tr><td><code>Type</code></td><td>Type of entity such as FILE, TABLE, DIRECTORY, etc.</td><td>String</td><td><code>FILE</code></td></tr><tr><td><code>Parent</code></td><td>Identifier of the parent entity.</td><td>String</td><td><code>af8064fa-af85-43fe-baf3-5fee11590301</code></td></tr><tr><td><code>FqdnDisplay</code></td><td>Fully Qualified Domain Name (FQDN) display for entity location.</td><td>String</td><td><code>AWS_S3_1/data-service-test/pentaho_migration/...</code></td></tr></tbody></table>

Use `entities_summary_view` when you need entity identifiers and basic metadata. For deep profiling, lineage, or detailed statistics, use `entities_master_view`.

#### Relationship tables <a href="#relationship-tables" id="relationship-tables"></a>

The view or tables in the Relationship tables category defines how entities in Data Catalog are enriched and connected to business metadata such as properties, applications, policies, and terms. Unlike summary or cross-reference views, these tables focus on the direct associations between entities and their contextual metadata.

The following views or tables are available in this category:

* Custom Properties View
* Entities Applications View
* Entities Policies View
* Terms View

**Custom Properties View**

The `custom_properties_view` is a BIDB relationship view that captures custom metadata properties assigned to entities. It links business-specific attributes (like tags, classifications, or business terms) to entities and makes them quarriable for reporting and governance. The `custom_properties_view`:

* Enables attaching business context (for example, department, project, domain) to data assets.
* Supports search, filtering, and reporting based on user-defined metadata.
* Helps in governance by associating policies, compliance terms, or classifications with datasets.
* Provides flexibility beyond system-generated metadata, allowing organizations to extend the catalog to fit business needs.

The following table shows the details of the data available in `custom_properties_view`.

| Field          | Description                                                               | Data Type | Example Value                          |
| -------------- | ------------------------------------------------------------------------- | --------- | -------------------------------------- |
| `EntityId`     | Unique identifier of the entity to which the custom property is assigned. | String    | `f8420f36-0985-41d0-90ec-b257fb4983ab` |
| `PropertyId`   | Unique identifier of the custom property.                                 | String    | `68a57f02010fdaaed8384f35`             |
| `Value`        | The assigned value of the custom property.                                | String    | `Hardware`                             |
| `PropertyName` | Name of the property (business term or category).                         | String    | `IT`                                   |
| `FqdnDisplay`  | Fully Qualified Domain Name (FQDN) path of the entity.                    | String    | `MSSQL_DS/iotadb/Chinook/Album`        |

Use `custom_properties_view` to add business-specific dimensions (like “Banking”, “IT”, “Education”) to your data catalog. This is especially powerful for governance dashboards and compliance-driven reports.

**Entities Applications View**

The `entities_applications_view` is a relationship view that links entities to applications in Data Catalog. Each row indicates that a given entity (file/table/dataset) is associated with an application. You can use it to slice entity inventories “by application” and to drive application‑centric governance reports. with the `entities_applications_view`, you can:

* Build application inventories of data assets.
* Join with entity tables to get paths, sizes, and freshness per application.
* Roll up duplicate/temperature/usage stats at the application level.

The following table shows the details of the data available in `entities_applications_view`.

<table><thead><tr><th width="136">Field</th><th width="324">Description</th><th width="94">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>EntityId</code></td><td>ID of the entity (join to <code>entities_summary_view._id</code> / <code>entities_master_view._id</code>).</td><td>UUID</td><td><code>97609adf-173c-411e-806f-32f73f2f7826</code></td></tr><tr><td><code>ApplicationId</code></td><td>ID of the application the entity belongs to.</td><td>UUID</td><td><code>ac2a0fac-5524-4680-8b23-e8e3b1778c4e</code></td></tr><tr><td><code>FqdnDisplay</code></td><td>FQDN-style path of the entity for readability.</td><td>String</td><td><code>MSSQL_DS/iotadb/synthea/allergies</code></td></tr></tbody></table>

* `ApplicationId` typically maps to your application catalog (if you maintain a separate applications dimension, join on that for names/owners).
* Use `entities_summary_view` for fast lookups; switch to `entities_master_view` when you need full metadata (size, Timestamps, owner, profiling stats).
* Combine with `terms_view` or `custom_properties_view` to analyze applications by business terms (for example, HOT/COLD, PII).

**Entities Policies View**

The `entities_policies_view` is a relationship view that connects entities (such as tables, files, or datasets) with policies that govern them. Each row identifies which policy is applied to which entity, enabling downstream governance and compliance tracking inside Data Catalog. The `entities_policies_view`:

* Provides a direct mapping of assets to policies, helping compliance teams validate enforcement.
* Enables policy-driven reporting (for example, “show all assets under data retention policies”).
* Supports governance frameworks by ensuring visibility into which controls are applied to which data assets.

The following table shows the details of the data available in `entities_policies_view`.

<table><thead><tr><th width="130">Field</th><th width="315">Description</th><th width="91">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>EntityId</code></td><td>ID of the entity the policy applies to. Join with <code>entities_summary_view._id</code> or <code>entities_master_view._id</code>.</td><td>UUID</td><td><code>c6bfb56c-451f-46ff-bef8-45a23f1d2eaa</code></td></tr><tr><td><code>PolicyId</code></td><td>Unique identifier of the policy.</td><td>UUID</td><td><code>ccffa343-ec11-4385-8e17-d68dc22e9f46</code></td></tr><tr><td><code>FqdnDisplay</code></td><td>FQDN-style path of the entity (data source/schema/table/file).</td><td>String</td><td><code>OracleDS/XE/COMMKTG/DIM_COST_CENTER</code></td></tr></tbody></table>

**Terms View**

The `terms_view` is a BIDB relationship table that links entities to business glossary terms. It shows which glossary term(s) are associated with which entity, helping organizations align business vocabulary with technical assets. The `terms_view`:

* Provides a clear bridge between business and technical metadata.
* Ensures consistency of terminology across the catalog.
* Enables impact analysis: users can see which entities are tied to specific glossary terms.
* Helps in data governance and compliance by associating regulated terms (for example, *Financial Information*) with datasets.

The following table shows the details of the data available in`terms_view`.

<table><thead><tr><th width="138">Field</th><th width="284">Description</th><th width="85">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>EntityId</code></td><td>Unique identifier of the entity linked to a glossary term.</td><td>String</td><td><code>3459ae2c-9ca5-486f-b35d-b117c5f59529</code></td></tr><tr><td><code>TermName</code></td><td>Business glossary term assigned to the entity.</td><td>String</td><td><code>WARM</code></td></tr><tr><td><code>GlossaryId</code></td><td>Unique identifier of the glossary where the term is defined.</td><td>String</td><td><code>24813366-5334-44aa-be22-d89c25c32242</code></td></tr><tr><td><code>TermId</code></td><td>Unique identifier of the glossary term.</td><td>String</td><td><code>e894eceb-3c52-448f-b695-2725ddfc3eb7</code></td></tr><tr><td><code>FqdnDisplay</code></td><td>Fully Qualified Domain Name (FQDN) path of the entity.</td><td>String</td><td><code>MSSQL_DS/iotadb/Chinook/Customer</code></td></tr></tbody></table>

The `terms_view` is especially useful when building business-facing dashboards or compliance mappings, as it allows users to see which data assets are tagged with key glossary terms like *Financial Information*, *BCI*, or *HOT/COLD data classifications*.

#### Usage Statistics <a href="#usage-statistics" id="usage-statistics"></a>

The view in the Usage Statistics category provides insights into how entities within Data Catalog are accessed and utilized. By capturing read, write, and alter operations, this category helps users and administrators monitor activity trends and optimize resource usage. Currently, the category contains the following view Usage Statistics View.

**Usage Statistics View**

The `usage_statistics_view` provides detailed usage metrics of entities (tables, schemas, and databases) ingested into Data Catalog. It captures read, write, and alter operations performed on data entities, along with activity Timestamps. This view enables administrators and data stewards to monitor how frequently specific data assets are accessed, modified, or updated, and supports governance, auditing, and optimization activities. The `usage_statistics_view`:

* Monitors data usage patterns across entities, helping identify the most frequently accessed tables and schemas.
* Supports performance optimization by showing read/write activity.
* Enables governance and auditing with historical records of access and modification.
* Assists impact analysis by identifying dependencies and heavily used data sources.

| Field Name         | Description                                             | Data Type    | Example Value                                           |
| ------------------ | ------------------------------------------------------- | ------------ | ------------------------------------------------------- |
| `EntityId`         | Unique identifier of the entity                         | String       | `484825ee-9265-49ad-80ec-9627add804f5`                  |
| `SchemaName`       | Name of the schema containing the entity                | VARCHAR(255) | `COMMKTG`                                               |
| `TableName`        | Name of the table                                       | VARCHAR(255) | `DIM_CUSTOMER`                                          |
| `FQDN`             | Fully Qualified Domain Name of the entity               | VARCHAR(512) | `687f5737e8bb866291f86088/DEMO_DB/COMMKTG/DIM_CUSTOMER` |
| `PeriodStartDate`  | Start date of the period when usage is recorded         | Timestamp    | `2025-07-21 00:00:00.000`                               |
| `PeriodEndDate`    | End date of the period when usage is recorded           | Timestamp    | `2025-07-22 10:34:23.290`                               |
| `LastReadTime`     | Timestamp of the last read operation                    | Timestamp    | `2025-07-22 09:03:11.311`                               |
| `LastWriteTime`    | Timestamp of the last write operation                   | Timestamp    | *(null)*                                                |
| `LastAlterTime`    | Timestamp of the last alter operation                   | Timestamp    | *(null)*                                                |
| `ReadCount`        | Number of read operations during the collection period  | Integer      | `12`                                                    |
| `WriteCount`       | Number of write operations during the collection period | Integer      | `0`                                                     |
| `AlterCount`       | Number of alter operations during the collection period | Integer      | `0`                                                     |
| `LastActivityTime` | Timestamp of the last activity (read/write/alter)       | Timestamp    | `2025-07-22 09:03:11.311`                               |
| `CollectionTime`   | Timestamp when usage statistics were collected in PDC   | Timestamp    | `2025-07-22 10:34:47.352`                               |

#### Cross-reference tables <a href="#cross-reference-tables" id="cross-reference-tables"></a>

The tables or view in the Cross-Reference Tables category, define the relationships between key metadata objects in Pentaho Data Catalog. Instead of storing descriptive details, these tables establish linkages that connect applications, glossary terms, and policies. They are essential for building a connected view of metadata across the catalog.

The following cross-reference tables are available:

* Applications Policies View
* Applications Terms View
* Terms Policies View

**Applications Policies View**

The `applications_policies_view` is a cross-reference table that links applications with the policies governing them. It provides visibility into which compliance or governance policies are applied to applications configured in Data Catalog. The `applications_policies_view`:

* Ensures applications adhere to governance and compliance rules.
* Provides a clear mapping of policies → applications for audits.
* Enables impact analysis (for example, when a policy changes, see which applications are affected).
* Supports reporting on governance coverage at the application level.

The following table shows the details of the data available in `applications_policies_view`.

<table><thead><tr><th width="142">Field</th><th width="280">Description</th><th width="93">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Internal surrogate key for the row.</td><td>Integer</td><td><code>1</code></td></tr><tr><td><code>ApplicationId</code></td><td>Unique identifier of the application. Join with <code>applications_dim.ApplicationId</code> or <code>entities_applications_view.ApplicationId</code>.</td><td>UUID</td><td><code>ac2a0fac-5524-4680-8b23-e8e3b1778c4e</code></td></tr><tr><td><code>PolicyId</code></td><td>Unique identifier of the policy applied to the application. Join with <code>policies_dim.PolicyId</code> or <code>entities_policies_view.PolicyId</code>.</td><td>UUID</td><td><code>ccffa343-ec11-4385-8e17-d68dc22e9f46</code></td></tr></tbody></table>

Since `applications_policies_view` is a cross-reference table, it works best when joined with `applications_dim` (or `entities_applications_view`) and `policies_dim` (or `entities_policies_view`).

**Applications Terms View**

The `applications_terms_view` is a cross-reference table that links applications with business glossary terms assigned to them. It provides traceability between glossary definitions and the applications consuming or producing related data. The `applications_terms_view`:

* Enforces consistent business terminology across applications.
* Helps analysts trace how glossary terms are implemented in different applications.
* Supports governance and impact analysis when terms change.
* Provides visibility for audits, compliance, and data literacy programs.

The following table shows the details of the data available in `applications_terms_view`.

<table><thead><tr><th width="140">Field</th><th width="323">Description</th><th width="88">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Internal surrogate key for the row.</td><td>Integer</td><td><code>1</code></td></tr><tr><td><code>ApplicationId</code></td><td>Unique identifier of the application. Join with <code>applications_dim.ApplicationId</code> or <code>entities_applications_view.ApplicationId</code>.</td><td>UUID</td><td><code>ce253775-4b73-4887-bd12-daf883c310cc</code></td></tr><tr><td><code>TermId</code></td><td>Unique identifier of the glossary term. Join with <code>terms_dim.TermId</code> or <code>terms_view.TermId</code>.</td><td>UUID</td><td><code>e894eceb-3c52-448f-b695-2725ddfc3eb7</code></td></tr></tbody></table>

Like `applications_policies_view`, this is a cross-reference table. It is most useful when joined with `applications_dim` and `terms_dim (or terms_view)` for details.

**Terms Policies View**

The `terms_policies_view` is a cross-reference table that maps business glossary terms to the policies that govern them. This enables visibility into which rules, compliance policies, or governance frameworks apply to specific terms. The `terms_policies_view`:

* Links glossary terms (like “Personal Data” or “Customer Information”) with the policies that control their handling.
* Provides a governance audit trail for compliance.
* Helps data stewards and compliance officers evaluate the policy coverage of business terms.
* Enables impact analysis when policies or terms are updated.

The following table shows the details of the data available in `terms_policies_view`.

<table><thead><tr><th width="100">Field</th><th width="307">Description</th><th width="100">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Internal surrogate key for the row.</td><td>Integer</td><td><code>1</code></td></tr><tr><td><code>TermId</code></td><td>Unique identifier of the glossary term. Join with <code>terms_dim.TermId</code> or <code>terms_view.TermId</code>.</td><td>UUID</td><td><code>8f7c2f5d-2617-433d-8519-1fc2ff80733e</code></td></tr><tr><td><code>PolicyId</code></td><td>Unique identifier of the policy. Join with <code>policies_dim.PolicyId</code> or <code>entities_policies_view.PolicyId</code>.</td><td>UUID</td><td><code>5937acef-1476-4f2d-af42-03673a21f841</code></td></tr></tbody></table>

The `terms_policies_view` is most useful when joined with `terms_dim (or terms_view)` for glossary details and `policies_dim` for policy details

#### Master summary views <a href="#master-summary-views" id="master-summary-views"></a>

The views categorized as Master Summary Views, provide a consolidated overview of the core metadata objects in Data Catalog. These views act as entry points for exploring applications, glossaries, and policies, offering high-level details before drilling down into relationships or usage statistics.

The following views are part of this category:

* Applications Summary View
* Glossary Summary View
* Policies Summary View

**Applications Summary View**

The `applications_summary_view` is a summary view that provides high-level metadata for applications registered in Data Catalog. It captures essential attributes such as application identifiers, names, parent hierarchy, FQDN path, and associated user access information. The `applications_summary_view`:

* Provides a cataloged overview of applications in the system.
* Enables quick discovery of application names and their parent group hierarchy.
* Facilitates access control auditing by showing users associated with applications.
* Acts as a base view to join with policies, entities, and terms for governance and impact analysis.

The following table shows the details of the data available in `applications_summary_view`.

<table><thead><tr><th width="160">Field</th><th width="280">Description</th><th width="101">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Unique identifier for the application.</td><td>UUID</td><td><code>cb04f8e9-b487-42f2-b66b-90551bff6134</code></td></tr><tr><td><code>Name</code></td><td>Display name of the application.</td><td>String</td><td><code>ComplexORC</code></td></tr><tr><td><code>Type</code></td><td>Type of record (application).</td><td>String</td><td><code>application</code></td></tr><tr><td><code>Parent</code></td><td>ID of the parent grouping or container for the application.</td><td>UUID</td><td><code>e6e1b7df-e3b2-4b13-9f99-df0072625f4a</code></td></tr><tr><td><code>Fqdn</code></td><td>Fully Qualified Domain Name path representing the application’s hierarchy in the catalog.</td><td>String</td><td><code>ORC/Group1/ComplexORC</code></td></tr><tr><td><code>UsersWithAccess</code></td><td>List of users/groups who have access to the application.</td><td>String</td><td><code>JohnDoe</code></td></tr></tbody></table>

The `applications_summary_view` is often used as a lookup table to provide application context when analyzing cross-reference tables such as:

* `applications_policies_view`
* `applications_terms_view`
* `entities_applications_view`

**Glossary Summary View**

The `glossary_summary_view` provides a summary of glossary terms and categories available in Data Catalog. It contains metadata about terms, their hierarchy, and their fully qualified domain names (FQDNs). The `glossary_summary_view`:

* Provides a structured catalog of glossary terms for consistent business terminology.
* Enables hierarchical navigation of glossaries (for example, Finance → FinanceDetailer).
* Supports data governance and stewardship by standardizing naming conventions.
* Acts as a reference for linking glossary terms with entities, applications, and policies.

The following table shows the details of the data available in `glossary_summary_view`.

<table><thead><tr><th width="90">Field</th><th width="310">Description</th><th width="111">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Unique identifier for the glossary term or category.</td><td>UUID</td><td><code>edd0ba23-cd83-42f9-9229-d04c57cdf636</code></td></tr><tr><td><code>Name</code></td><td>Display name of the glossary entry.</td><td>String</td><td><code>InsurancePolicy</code></td></tr><tr><td><code>Type</code></td><td>Classification of the entry (glossary or term).</td><td>String</td><td><code>term</code></td></tr><tr><td><code>Parent</code></td><td>Identifier of the parent glossary or category to which the entry belongs.</td><td>UUID</td><td><code>a0f291ac-c827-420f-b63d-95a28f10b743</code></td></tr><tr><td><code>Fqdn</code></td><td>Fully Qualified Domain Name representing the hierarchical path of the glossary term.</td><td>String</td><td><code>Insurance/InsurancePolicy</code></td></tr></tbody></table>

This `glossary_summary_view` works in conjunction with:

* `terms_view` (links terms to entities)
* `entities_custom_categorization` (categorizes entities under glossary terms)
* `terms_policies_view` (links terms to policies)

**Policies Summary View**

The `policies_summary_view` provides a summary of policies and their hierarchical structure in Data Catalog. It captures metadata about policy definitions, categories, and associated standards. The `policies_summary_view`:

* Centralizes all policy metadata for easy navigation.
* Shows policy hierarchy (for example, policy → standards).
* Supports governance, compliance, and categorization of entities under policies.
* Enables FQDN-based lookup for policy enforcement across datasets.

The following table shows the details of the data available in `policies_summary_view`.

<table><thead><tr><th width="87">Field</th><th width="329">Description</th><th width="104">Data Type</th><th>Example Value</th></tr></thead><tbody><tr><td><code>_id</code></td><td>Unique identifier for the policy or standard.</td><td>UUID</td><td><code>1a641946-a569-4f3e-8281-dcc64169d514</code></td></tr><tr><td><code>Name</code></td><td>Policy or standard name.</td><td>String</td><td><code>BikeModels</code></td></tr><tr><td><code>Type</code></td><td>Type of entry (policy, standard, or rule).</td><td>String</td><td><code>policy</code> / <code>standard</code></td></tr><tr><td><code>Parent</code></td><td>Reference to the parent policy (if applicable).</td><td>UUID</td><td><code>1a641946-a569-4f3e-8281-dcc64169d514</code></td></tr><tr><td><code>Fqdn</code></td><td>Fully Qualified Domain Name representing the hierarchical path.</td><td>String</td><td><code>BikeModels/Bajaj</code></td></tr></tbody></table>

This `policies_summary_view` is often used with:

* `entities_policies_view` (links entities to policies)
* `applications_policies_view` (links applications to policies)
* `terms_policies_view` (links glossary terms to policies)

### BIDB in versions prior to PDC 10.2.5 (MongoDB-based) <a href="#bidb-in-versions-prior-to-pdc-10.2.5-mongodb-based" id="bidb-in-versions-prior-to-pdc-10.2.5-mongodb-based"></a>

In earlier versions, BIDB used MongoDB as its underlying database. Several services, including bi-mongo and bi-views, were deployed during installation. The bi-views service periodically aggregated data from connected databases and stored it in BIDB, with the frequency controlled in the `.env` file (default: daily). The mongo-bi-connector, provided by the bi-mongo service, enabled JDBC/ODBC connectivity. BIDB data was made available on port 3307, allowing access and analysis in compatible BI tools.

#### Checksum Aggregated View

The **Checksum Aggregated View** collection contains a summary of duplicate files for a specific entity, including their count and total size. The following table shows the details of the data available in this collection.

| Field                 | Description                                      | Data Type | Example Value                      |
| --------------------- | ------------------------------------------------ | --------- | ---------------------------------- |
| `_id`                 | Checksum derived from `bi.entities_master_view`. | String    | “968dl402bd0ce783a573al4172c37690” |
| `duplicateFilesCount` | The total number of duplicate files identified.  | Integer   | 3                                  |
| `duplicateFilesSize`  | The total size of duplicate files.               | Integer   | 381                                |

#### Custom Properties View

The **Custom Properties View** collection contains the details of custom properties in an entity, including their values. The following table shows the details of the data available in this collection.

| Field          | Description                                        | Data Type | Example Value              |
| -------------- | -------------------------------------------------- | --------- | -------------------------- |
| `_id`          | A unique identifier for the custom property entry. | String    | “65dfc901d04619a9e6a8d62d” |
| `EntityId`     | A unique identifier for the entity.                | String    | "11"                       |
| `PropertyId`   | A unique identifier for the property.              | String    | "5"                        |
| `PropertyName` | The name of the custom property.                   | String    | "Name"                     |
| `Value`        | The assigned value of the custom property.         | String    | "John"                     |

#### Entities Aggregated View

The **Entities Aggregated View** collection includes the details of the key attributes and values of aggregated entities. The following table shows the details of the data available in this collection.

| Field       | Description                                     | Data Type | Example Value              |
| ----------- | ----------------------------------------------- | --------- | -------------------------- |
| `_id`       | A unique identifier for the entity aggregation. | String    | “65dfc901d04619a9e6a8d62d” |
| `attribute` | The attribute name of the entity.               | String    | "DataSources"              |
| `type`      | The data type of the attribute.                 | String    | "Structured"               |
| `value`     | The value associated with the attribute.        | String    | "34"                       |

#### Entities Extension Count View

The **Entities Extension Count** view collection includes extension details, such as the file count, data source, and date of recording for each extension. The following table shows the details of the data available in this collection.

| Field              | Description                                                               | Data Type | Example Value                                    |
| ------------------ | ------------------------------------------------------------------------- | --------- | ------------------------------------------------ |
| `_id`              | A unique identifier for the count entry.                                  | String    | “65c56b02250cc54a7b43943f”                       |
| `DataSourceFqdnId` | A fully qualified domain name identifier is required for the data source. | String    | "5"                                              |
| `Date`             | The date when the file count was recorded.                                | Date      | 2024-02-09T00:00:02.110+00:00                    |
| `Extension`        | The file extension.                                                       | String    | "text/plain; charset=IS0-8859-l;delimiter=comma” |
| `FileCount`        | The number of files with the specified extension.                         | Integer   | 1                                                |

#### Entities Master View

The Entities Master View contains the essential structure and data field details of an entity. The following table shows the details of the data available in this collection.

| Field                  | Description                                                        | Data Type | Example Value                      |
| ---------------------- | ------------------------------------------------------------------ | --------- | ---------------------------------- |
| `_id`                  | A unique identifier for the entity.                                | String    | "11"                               |
| `Name`                 | The name of the entity.                                            | String    | "customers"                        |
| `Type`                 | The type of the entity (for example, file, table).                 | String    | "Table"                            |
| `Parent`               | The parent entity identifier.                                      | String    | "12"                               |
| `DataSourceId`         | A unique identifier for the data source.                           | String    | "dataSource\_01"                   |
| `DataSourceName`       | The name of the data source.                                       | String    | "SalesDB"                          |
| `DataSourceType`       | The type of the data source (for example, SQL, NoSQL).             | String    | "SQL"                              |
| `ResourceType`         | The type of the resource.                                          | String    | "Database"                         |
| `DataProfileStatus`    | The status of data profiling (for example, Complete, In Progress). | String    | "Complete"                         |
| `DataProfiled`         | Whether the data has been profiled (True or False).                | Boolean   | True                               |
| `LastUpdate`           | The timestamp of the last update.                                  | Timestamp | "2023-12-14T15:05:00Z"             |
| `ProductName`          | The name of the product.                                           | String    | "MySQL"                            |
| `ProductVersion`       | A version of the product.                                          | String    | "8.0"                              |
| `DriverName`           | The name of the driver used.                                       | String    | "MySQL ODBC 8.0 Driver"            |
| `Url`                  | The URL associated with the entity.                                | String    | "jdbc:mysql://example.com/db"      |
| `ParentName`           | The name of the parent entity.                                     | String    | "SalesRegion"                      |
| `TotalTables`          | The total number of tables.                                        | Integer   | 12                                 |
| `TotalColumns`         | The total number of columns.                                       | Integer   | 120                                |
| `SchemaName`           | The name of the schema.                                            | String    | "public"                           |
| `DatabaseName`         | The name of the database.                                          | String    | "SalesDB"                          |
| `LastUpdateStatistics` | The timestamp of the last statistics update.                       | Timestamp | 2023-12-14T14:00:00Z               |
| `RowCount`             | Number of rows in the entity.                                      | Integer   | 10000                              |
| `NullCount`            | Number of nulls in the entity.                                     | Integer   | 50                                 |
| `Cardinality`          | The cardinality of the entity.                                     | Integer   | 9500                               |
| `Hll`                  | HyperLogLog of the entity.                                         | String    | "hll:6a9..."                       |
| `BlankCount`           | The number of blank entries in the entity.                         | Integer   | 20                                 |
| `Min`                  | The minimum value in the entity.                                   | String    | "1"                                |
| `Max`                  | The maximum value in the entity.                                   | String    | "10000"                            |
| `AvgValue`             | The average value of the entity.                                   | Float     | 5000.5                             |
| `MinWidth`             | The minimum width of the entity.                                   | Integer   | 1                                  |
| `MaxWidth`             | The maximum width of the entity.                                   | Integer   | 10                                 |
| `AvgWidth`             | The average width of the entity.                                   | Float     | 5.5                                |
| `ColumnsCount`         | The count of columns in the entity.                                | Integer   | 10                                 |
| `Path`                 | The path of the entity.                                            | String    | "/data/salesdb/customers"          |
| `CheckClause`          | Check the clause of the entity.                                    | String    | "age > 18"                         |
| `TableName`            | The name of the table.                                             | String    | "customers"                        |
| `DataType`             | The data type of the entity.                                       | String    | "VARCHAR"                          |
| `TypeName`             | The name of the entity type.                                       | String    | "varchar"                          |
| `ColumnSize`           | The size of the column.                                            | Integer   | 255                                |
| `BufferLength`         | The length of the buffer.                                          | Integer   | 256                                |
| `DecimalDigits`        | A number of decimal digits.                                        | Integer   | 2                                  |
| `NumPrecRadix`         | A numeric precision radix.                                         | Integer   | 10                                 |
| `IsNullable`           | Whether the entity is nullable (True or False).                    | Boolean   | True                               |
| `OrdinalPosition`      | Ordinal position of the entity.                                    | Integer   | 1                                  |
| `IsPrimaryKey`         | Whether the entity is a primary key (True or False).               | Boolean   | False                              |
| `IsForeignKey`         | Whether the entity is a foreign key (True or False).               | Boolean   | False                              |
| `ParentPath`           | The parent path of the entity.                                     | String    | "/data/salesdb"                    |
| `PathType`             | The path type of the entity.                                       | String    | "Directory"                        |
| `FileExtension`        | The file extension of the entity.                                  | String    | ".txt"                             |
| `Size`                 | The size of the entity.                                            | Integer   | 2048                               |
| `Flags`                | Flags associated with the entity.                                  | Integer   | 0                                  |
| `Owner`                | The owner of the entity.                                           | String    | "admin"                            |
| `Group`                | The group associated with the entity.                              | String    | "sales"                            |
| `SymLinkTarget`        | Symbolic link target of the entity.                                | String    | "/var/salesdb/link"                |
| `FileType`             | The file type of the entity.                                       | String    | "Text File"                        |
| `CreatedAt`            | The timestamp when the entity is created.                          | Timestamp | 2021-01-01T12:00:00Z               |
| `ModifiedAt`           | The timestamp when the entity is modified.                         | Timestamp | 2023-01-01T12:00:00Z               |
| `AccessedAt`           | The timestamp when the entity is accessed.                         | Timestamp | 2023-01-02T12:00:00Z               |
| `ScannedAt`            | The timestamp when the entity is scanned.                          | Timestamp | 2023-01-03T12:00:00Z               |
| `IsSymlink`            | Whether the entity is a symbolic link (True or False).             | Boolean   | False                              |
| `LinkType`             | The link type of the entity.                                       | String    | “\<example>”                       |
| `PhysicalLocation`     | The physical location of the entity.                               | String    | "ServerRoom1"                      |
| `Title`                | The title of the entity.                                           | String    | "2023 Sales Report"                |
| `Author`               | The author of the entity.                                          | String    | "John Doe"                         |
| `Subject`              | The subject of the entity.                                         | String    | "Sales Analysis"                   |
| `Application`          | An application associated with the entity.                         | String    | "Microsoft Excel"                  |
| `Producer`             | The producer of the entity.                                        | String    | "Microsoft"                        |
| `Version`              | A version of the entity.                                           | String    | "16.0"                             |
| `DocumentSize`         | The size of the document.                                          | Integer   | 102400                             |
| `PageSize`             | The size of the page.                                              | String    | "A4"                               |
| `PageCount`            | Number of pages in the entity.                                     | Integer   | 10                                 |
| `Company`              | The company associated with the entity.                            | String    | "Acme Corp"                        |
| `Paragraphs`           | The number of paragraphs in the entity.                            | Integer   | 50                                 |
| `Lines`                | The number of lines in the entity.                                 | Integer   | 200                                |
| `Words`                | The number of words in the entity.                                 | Integer   | 1000                               |
| `Characters`           | The number of characters in the entity.                            | Integer   | 5000                               |
| `CharactersWithSpaces` | The number of characters with spaces in the entity.                | Integer   | 6000                               |
| `Language`             | The language of the entity.                                        | String    | "English"                          |
| `Checksum`             | The checksum of the entity.                                        | String    | "e4d909c290d0fb1ca068ffaddf22cbd0" |
| `PropertiesChecksum`   | The checksum of the properties of the entity.                      | String    | "abcd1234efgh5678ijkl9012mnop3456" |
| `ChildDirs`            | The number of child directories.                                   | Integer   | 5                                  |
| `ChildFiles`           | The number of child files.                                         | Integer   | 20                                 |
| `ChildDirSize`         | The size of child directories.                                     | Integer   | 4096                               |
| `ChildFileSize`        | The size of child files.                                           | Integer   | 8192                               |
| `TotalChildDirs`       | The total number of child directories.                             | Integer   | 5                                  |
| `TotalChildFiles`      | The total number of child files.                                   | Integer   | 20                                 |
| `TotalChildDirSize`    | The total size of child directories.                               | Integer   | 4096                               |
| `TotalChildFileSize`   | The total size of child files.                                     | Integer   | 8192                               |

#### Entities Summary View

The **Entities Summary View** collection contains the details of an entity, such as type and the parent. The following table shows the details of the data available in this collection.

| Field    | Description                                        | Data Type | Example Value             |
| -------- | -------------------------------------------------- | --------- | ------------------------- |
| `_id`    | A unique identifier for the summary entry.         | String    | “11/XE/SYNTHEA/ALLERGIES” |
| `Name`   | The name of the entity.                            | String    | "ALLERGIES"               |
| `Type`   | The type of the entity (for example, file, table). | String    | "TABLE"                   |
| `Parent` | The parent entity identifier.                      | String    | "11/XE/SYNTHEA"           |

#### Entities Temperature Count View

The **Entities Temperature View** contains entity details emphasizing the categorization of data based on its temperature, which often indicates the frequency of access or modification, including the number of files. The following table shows the details of the data available in this collection.

| Field              | Description                                                                            | Data Type | Example Value                 |
| ------------------ | -------------------------------------------------------------------------------------- | --------- | ----------------------------- |
| `_id`              | A unique identifier for the temperature count entry.                                   | String    | "65d2f44dd30b49309488b9dd"    |
| `DataSourceFqdnId` | A fully qualified domain name identifier for the data source.                          | String    | "5"                           |
| `Date`             | The date when the file count and temperature were recorded.                            | String    | 2024-02-19TO6:25:17.918+00:00 |
| `FileCount`        | The number of files associated with the specified temperature.                         | String    | 2                             |
| `Temperature`      | The temperature category of the data (for example, unclassified, hot, warm, and cold). | String    | "unclassified"                |

#### Entity Usage Statistic View

The **Entity Usage Statistic View** collection includes a range of usage metrics, such as the number of times an entity is read, written to, and altered, along with the timestamp. The following table shows the details of the data available in this collection.

| Field             | Description                                                             | Data Type | Example Value             |
| ----------------- | ----------------------------------------------------------------------- | --------- | ------------------------- |
| `_id`             | A unique identifier for the statistics view entry.                      | String    | “11/XE/SYNTHEA/ALLERGIES” |
| `PeriodStartTime` | The start time of the entity's profiling period, in ISO format.         | Timestamp | 2023-12-14T15:00:00Z      |
| `PeriodEndTime`   | The end time of the entity's profiling period, in ISO format.           | Timestamp | 2023-12-14T15:05:00Z      |
| `EntityID`        | A unique identifier for the entity.                                     | String    | "12"                      |
| `DatabaseName`    | The name of the database where the entity is located.                   | String    | “Postgres”                |
| `SchemaName`      | The name of the schema within the database.                             | String    | “Chinook”                 |
| `TableName`       | The name of the table containing the entity.                            | String    | “Album”                   |
| `LastReadTime`    | The timestamp of the last read operation on the entity, in ISO format   | Timestamp | 2023-12-14T11:00:00Z      |
| `LastWriteTime`   | The timestamp of the last write operation on the entity, in ISO format. | Timestamp | 2023-12-14T11:50:00Z      |
| `LastAlterTime`   | The timestamp of the last modification to the entity in ISO format.     | Timestamp | 2023-12-14T11:20:00Z      |
| `ReadCount`       | The total number of times the entity has been read.                     | Integer   | 120                       |
| `WriteCount`      | The total number of times the entity has been written.                  | Integer   | 45                        |
| `AlterCount`      | The total number of times the entity has been altered.                  | Integer   | 3                         |
| `CollectionTime`  | The timestamp indicating when this data was collected, in ISO format.   | Timestamp | 2023-12-16T15:00:00Z      |

#### Terms View

The **Terms View** collection contains information of terms related to items. It gives a structured overview, linking terms to specific entities and domains. Each record uniquely identifies a term, its association with an entity, the domain it belongs to, and a unique term identifier, enabling a comprehensive semantic mapping of data assets. The following table shows the details of the data available in this collection.

| Field      | Description                                       | Data Type | Example Value                             |
| ---------- | ------------------------------------------------- | --------- | ----------------------------------------- |
| `_id`      | A unique identifier for the term entry.           | String    | "abc12345-d678-90ef-ghij-klmn01234567"    |
| `EntityId` | A unique identifier for the associated entity.    | String    | "entity78901-2345-6789-abcd-ef0123456789" |
| `TermName` | The name of the term.                             | String    | "Customer Satisfaction Index"             |
| `DomainId` | An identifier for the domain the term belongs to. | String    | "domain1234-5678-90ab-cdef-ghijklmnop"    |
| `TermId`   | A unique identifier for the term.                 | String    | "term5678-9012-3456-7890-abcd12345678"    |

## Pentaho Data Optimizer

If you have a license for Pentaho Data Optimizer, use Data Optimizer to inventory stored data, identify content, view usage, and tier files and objects into long term or deep archival storage. You can use rule-driven actions about data lifecycles to account for compliance, manage costs, and mitigate risks, using a set of convenient tools and self-service processes for sustainable improvements in data management.
