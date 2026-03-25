# Source: https://docs.snowflake.com/en/migrations/guides/azuresynapse.md

# **Azure Synapse to Snowflake Migration Guide**

## **Snowflake Migration Framework**

A typical Azure Synapse-to-Snowflake migration can be broken down into nine key phases. This guide provides a comprehensive framework to navigate the technical and strategic challenges involved, ensuring a smooth transition from Azure’s analytics platform to Snowflake’s cloud data platform.

## **Migration Phases**

### **Phase 1: Planning and Design**

This initial phase is critical for establishing the foundation of a successful migration. Migrating from Azure Synapse requires a clear understanding of its integrated components and a thorough plan to align stakeholders, define scope, and prevent budget overruns.

**Your Actionable Steps:**

* **Conduct a Thorough Assessment of Your Synapse Environment:**

  * **Inventory & Analyze:** Catalog all objects within your Synapse workspace, including dedicated SQL pool tables, serverless SQL pool views, schemas, T-SQL stored procedures, functions, and views. Use Synapse’s system views (e.g., sys.tables, sys.procedures) to gather metadata.
  * **Analyze Workloads:** Use Azure Monitor and Synapse’s Dynamic Management Views (DMVs) to identify query patterns, user concurrency, resource utilization (DWUs), and performance bottlenecks. This data is crucial for designing your Snowflake virtual warehouse strategy.
  * **Identify Dependencies:** Map all upstream data sources, especially Azure Data Factory (ADF) pipelines, and downstream consumers like Power BI reports, Azure Machine Learning models, and other applications.
* **Define the Migration Scope and Strategy:**

  * **Prioritize Workloads:** Classify workloads by business impact and technical complexity. Start with a high-impact, low-complexity workload (e.g., a specific data mart) to demonstrate value and build momentum.
  * **Choose a Migration Approach:** Decide between a “lift and shift” for a faster migration or a re-architecture approach to modernize data models and pipelines.
* **Develop the Project Plan:**

  * **Establish a Team:** Create a migration team with clear roles (Project Manager, Data Engineer, Synapse/SQL DBA, Snowflake Architect, Security Admin, Business Analyst).
  * **Create a Timeline:** Define realistic timelines and milestones for each of the nine phases.
  * **Define Success Metrics:** Establish clear KPIs to measure success, such as cost reduction, query performance improvement, and user satisfaction.

### **Phase 2: Environment and Security**

With a solid plan, the next step is to prepare the Snowflake environment and translate Azure’s security model. Hosting Snowflake on Azure is highly recommended to simplify data transfer and network integration.

**Your Actionable Steps:**

* **Set Up Your Snowflake Account:**

  * **Choose Edition and Cloud Provider:** Select the Snowflake edition (e.g., Standard, Enterprise, Business Critical) that meets your needs. **Choose Azure as the cloud provider** and select the same region as your Azure Data Lake Storage (ADLS Gen2) to minimize data transfer costs and latency.
  * **Design a Warehouse Strategy:** Based on the workload analysis from Phase 1, create an initial set of virtual warehouses. Isolate different workloads (e.g., WH_LOADING, WH_TRANSFORM, WH_BI_ANALYTICS) to prevent resource contention. Start with T-shirt sizes (e.g., X-Small, Small) and plan to resize them based on performance testing.
* **Implement the Security Model:**

  * **Map Azure AD Principals to Snowflake Roles:** Translate Azure Active Directory (AAD) users and groups into Snowflake’s hierarchical Role-Based Access Control (RBAC) model. Create a hierarchy of functional roles (SYSADMIN, SECURITYADMIN) and access roles (BI_READ_ONLY, ETL_READ_WRITE).
  * **Configure Network Policies and Authentication:** Set up network policies to restrict access to trusted IP addresses via Azure Private Link for a secure connection. Configure SSO by setting up Snowflake as an Enterprise Application in Azure AD.

### **Phase 3: Database Code Conversion**

This phase involves converting Synapse’s T-SQL based DDL, DML, and procedural code to be compatible with Snowflake. Automation tools can accelerate this process, but manual review is essential.

**Your Actionable Steps:**

* **Convert DDL (Data Definition Language):**

  * **Tables and Views:** Extract CREATE TABLE and CREATE VIEW statements from Synapse. Convert Synapse-specific data types to their Snowflake equivalents (see Appendix 2).
  * **Remove Synapse-Specific Clauses:** Eliminate Synapse-specific physical distribution clauses like DISTRIBUTION (e.g., ROUND_ROBIN, HASH) and indexing strategies like CLUSTERED COLUMNSTORE INDEX. Snowflake manages data distribution and storage automatically.
  * **Re-implement Constraints:** Snowflake only enforces NOT NULL constraints. PRIMARY KEY and UNIQUE constraints are informational. All other data integrity logic must be moved into your ETL/ELT processes.
* **Convert DML (Data Manipulation Language) and Procedural Code:**

  * **Rewrite T-SQL Stored Procedures:** Synapse’s T-SQL stored procedures must be rewritten into a language supported by Snowflake, such as Snowflake Scripting (SQL), JavaScript, or Python.
  * **Translate SQL Functions:** Map Synapse/T-SQL specific functions to their Snowflake counterparts (e.g., GETDATE() becomes CURRENT_TIMESTAMP(), ISNULL() becomes IFNULL()). See Appendix 3 for common mappings.

### **Phase 4: Data Migration**

This phase focuses on the physical movement of historical data from your Synapse SQL pools to Snowflake tables. The most efficient method leverages Azure Data Lake Storage (ADLS Gen2) as an intermediate staging area.

**Your Actionable Steps:**

* **Unload Data from Synapse to ADLS Gen2:**

  * Use the CREATE EXTERNAL TABLE AS SELECT (CETAS) command in Synapse to export data from tables into a designated container in your ADLS Gen2 account.
  * Format data as Parquet or compressed CSV for optimal loading performance into Snowflake.
* **Load Data from ADLS Gen2 into Snowflake:**

  * **Create an External Stage:** In Snowflake, create a storage integration object to securely connect to ADLS Gen2, then create an external stage that points to the container with your unloaded data.
  * **Use the COPY INTO Command:** Use Snowflake’s COPY INTO <table> command to load the data from the ADLS stage into the target Snowflake tables.
  * **Leverage a Sized-Up Warehouse:** Use a dedicated, larger virtual warehouse for the initial data load to accelerate the process, then scale it down or suspend it afterward.

### **Phase 5: Data Ingestion**

Once the historical data is migrated, you must re-engineer your ongoing data ingestion pipelines, most commonly in Azure Data Factory, to feed data into Snowflake.

**Your Actionable Steps:**

* **Migrate Azure Data Factory (ADF) Pipelines:**

  * In your ADF pipelines, replace Synapse datasets and activities with their Snowflake equivalents. Use Snowflake’s native connector in ADF for both source and sink activities.
  * Update any Lookup or Script activities to use Snowflake’s SQL dialect.
* **Implement Continuous Ingestion with Snowpipe:**

  * For continuous data streams landing in ADLS Gen2, configure Snowpipe. Snowpipe automatically and efficiently loads new data files into Snowflake tables as they arrive, providing a near-real-time ingestion solution. This can be triggered by Azure Event Grid notifications.
* **Utilize the Snowflake Ecosystem:**

  * Explore Snowflake’s native connectors for platforms like Kafka and Spark to simplify direct data streaming.

### **Phase 6: Reporting and Analytics**

This phase involves redirecting all downstream applications, particularly Power BI, to query data from Snowflake.

**Your Actionable Steps:**

* **Update Connection Drivers:** Ensure Power BI Desktop and the On-premises data gateway have the latest Snowflake drivers.
* **Redirect Power BI Reports:**

  * In Power BI, edit the data source for each report, switching the connection from Azure Synapse to Snowflake. Snowflake’s native Power BI connector is certified and highly recommended.
  * Test all critical reports and dashboards. Pay close attention to reports using DirectQuery, as performance characteristics will change.
* **Review and Optimize Queries:**

  * Some reports may contain native T-SQL queries. These must be refactored to use Snowflake’s SQL dialect. Use the Query Profile tool in Snowflake and the Performance Analyzer in Power BI to optimize slow-running reports.

### **Phase 7: Data Validation and Testing**

Rigorous testing is essential to build business confidence in the new platform and ensure data integrity and performance meet expectations.

**Your Actionable Steps:**

* **Perform Data Validation:**

  * **Row Counts:** Compare row counts between source tables in Synapse and target tables in Snowflake.
  * **Cell-Level Validation:** For critical tables, perform a deeper validation by comparing aggregated values (SUM, AVG, MIN, MAX) on key columns.
* **Conduct Query and Performance Testing:**

  * **Benchmark Queries:** Execute a representative set of queries against both Synapse and Snowflake and compare results and performance.
  * **BI Tool Performance:** Test the load times and interactivity of key Power BI dashboards connected to Snowflake.
* **User Acceptance Testing (UAT):**

  * Involve business users to validate their reports and perform their daily tasks using the new Snowflake environment.

### **Phase 8: Deployment**

Deployment is the final cutover from Azure Synapse to Snowflake. This process should be carefully managed to minimize disruption to business operations.

**Your Actionable Steps:**

* **Develop a Cutover Plan:**

  * Define the sequence of events for the cutover. This includes pausing ADF pipelines pointing to Synapse, performing a final data sync, redirecting all connections, and validating system health.
* **Execute the Final Data Sync:**

  * Perform one last incremental data load to capture any data changes that occurred during the testing phase.
* **Go Live:**

  * Switch all production data pipelines and user connections from Synapse to Snowflake.
  * Keep the Synapse environment available (but paused, if possible) for a short period as a fallback before decommissioning.
* **Decommission Synapse:**

  * Once the Snowflake environment is stable and validated in production, you can decommission your Synapse SQL pools to stop incurring costs.

### **Phase 9: Optimize and Run**

This final phase is an ongoing process of managing performance, cost, and governance in your new Snowflake environment.

**Your Actionable Steps:**

* **Implement Performance and Cost Optimization:**

  * **Right-Size Warehouses:** Continuously monitor workload performance and adjust virtual warehouse sizes. This replaces the concept of scaling Synapse DWUs.
  * **Set Aggressive Auto-Suspend Policies:** Set the auto-suspend timeout for all warehouses to 60 seconds to avoid paying for idle compute time.
  * **Use Clustering Keys:** For very large tables (multi-terabyte), define clustering keys to improve the performance of highly filtered queries.
* **Establish Long-Term FinOps and Governance:**

  * **Monitor Costs:** Use Snowflake’s ACCOUNT_USAGE schema and resource monitors to track credit consumption.
  * **Refine Security:** Regularly audit roles and permissions. Implement advanced security features like Dynamic Data Masking and Row-Access Policies for sensitive data.

## **Appendix**

### **Appendix 1: Snowflake vs. Azure Synapse Architecture**

| Feature | Azure Synapse Analytics | Snowflake |
| --- | --- | --- |
| **Architecture** | Control Node + Compute Nodes (MPP for Dedicated Pools). Decoupled storage but coupled compute within a pool. | Decoupled compute, storage, and cloud services (Multi-cluster, Shared Data). |
| **Storage** | Data stored in Azure Data Lake Storage, managed by the SQL pool. | Centralized object storage (Azure Blob) with automatic micro-partitioning. |
| **Compute** | Provisioned Dedicated SQL Pools (scaled by DWUs) or Serverless SQL Pools (pay-per-query). | Elastic, on-demand virtual warehouses (compute clusters). |
| **Concurrency** | Limited by DWU size and max concurrent query slots (128) in a dedicated pool. | High concurrency via multi-cluster warehouses that spin up automatically. |
| **Scaling** | Scale dedicated pools by changing DWUs (can take several minutes). Can be paused. | Instantly scale compute up/down/out (seconds); storage scales automatically. |
| **Maintenance** | Requires manual maintenance of statistics. Indexing strategies need management. | Fully managed; maintenance tasks like statistics and compaction are automated. |

### **Appendix 2: Data Type Mappings**

| Azure Synapse (T-SQL) | Snowflake | Notes |
| --- | --- | --- |
| bigint | BIGINT / NUMBER(19,0) |  |
| int | INT / NUMBER(10,0) |  |
| smallint | SMALLINT / NUMBER(5,0) |  |
| tinyint | TINYINT / NUMBER(3,0) |  |
| bit | BOOLEAN |  |
| decimal(p,s) / numeric(p,s) | NUMBER(p,s) |  |
| money / smallmoney | NUMBER(19,4) / NUMBER(10,4) | Best practice is to map to NUMBER. |
| float / real | FLOAT |  |
| date | DATE |  |
| datetime / datetime2 | DATETIME / TIMESTAMP_NTZ | TIMESTAMP_NTZ is often the preferred target. |
| datetimeoffset | TIMESTAMP_TZ |  |
| smalldatetime | DATETIME / TIMESTAMP_NTZ |  |
| time | TIME |  |
| char(n) / varchar(n) | VARCHAR(n) |  |
| nchar(n) / nvarchar(n) | VARCHAR(n) | Snowflake uses UTF-8 by default, so N prefix types are not needed. |
| text / ntext | VARCHAR | Deprecated types; map to VARCHAR. |
| binary(n) / varbinary(n) | BINARY(n) |  |
| uniqueidentifier | VARCHAR(36) | Store as a string and use UUID_STRING() if needed. |

### **Appendix 3: SQL & Function Differences**

| Azure Synapse (T-SQL) | Snowflake | Notes |
| --- | --- | --- |
| GETDATE() | CURRENT_TIMESTAMP() | Snowflake has several functions for current date/time. |
| ISNULL(expr1, expr2) | IFNULL(expr1, expr2) | COALESCE is the ANSI standard and works in both. |
| TOP (n) | LIMIT n | Snowflake uses LIMIT clause at the end of the query. |
| IIF(bool, true, false) | IFF(bool, true, false) | Functionality is identical, name is slightly different. |
| DATEADD(part, num, date) | DATEADD(part, num, date) | Supported, but date/time parts may have different names (e.g., dd vs day). |
| DATEDIFF(part, start, end) | DATEDIFF(part, start, end) | Supported, but date/time parts may have different names. |
| STRING_SPLIT | SPLIT_TO_TABLE / SPLIT | Snowflake has more powerful functions for splitting strings. |
| **Procedural Language** | T-SQL (Stored Procedures) | Snowflake Scripting, JavaScript, Java, Python |
| **DDL Clauses** | DISTRIBUTION, CLUSTERED COLUMNSTORE INDEX | None. Replaced by automatic micro-partitioning and optional Clustering Keys. |
| **Temp Tables** | #temptable | CREATE TEMPORARY TABLE |
| **Transactions** | BEGIN TRAN, COMMIT, ROLLBACK | BEGIN, COMMIT, ROLLBACK |
| **Error Handling** | TRY…CATCH | BEGIN…EXCEPTION…END |
