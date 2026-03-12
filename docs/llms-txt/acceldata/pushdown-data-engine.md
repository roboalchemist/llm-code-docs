# Source: https://docs.acceldata.io/documentation/pushdown-data-engine.md

# Pushdown Data Engine

## Overview

The Pushdown Data Engine in ADOC improves data processing by delegating compute tasks to the underlying data source, such as **Snowflake**, **SAP HANA,** and **Big Query**, rather than relying on an external engine like Spark. This strategy enhances performance, decreases data transportation, and maximizes resource use by exploiting the data source's intrinsic capabilities.

### Supported Data Sources

The following data sources support the use of the Pushdown data processing engine:

| Data Source | Pushdown Supported | 
| ---- | ---- | 
| [Google BigQuery](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/bigquery) | ✅ | 
| [Databricks](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/databricks-integration-for-data-reliability) | ✅ | 
| [SAP HANA](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/sap-hana) | ✅ | 
| [Snowflake](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/snowflake-reliability) | ✅ | 
| [Microsoft Azure Synapse](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/azure-synapse-analytics) | ✅ | 
| [Oracle](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/oracle) | ✅ | 
| [Microsoft Azure MSSQL](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/azure-mssql) | ✅ | 
| [Amazon Redshift](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/redshift) | ✅ | 
| [MySQL](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/mysql) | ✅ | 


> Pushdown Engine support requires Data Reliability Observability enabled during integration.

### Key Features

- **Faster Query Execution**: Pushdown minimizes latency by processing queries directly at the data source.
- **Reduced Data Movement:** By removing the need to transfer huge datasets between Snowflake and Spark, Pushdown improves performance.
- **Optimized Resource Utilization**: Using the data source's native processing capabilities improves resource management and reduces maintenance overhead.

---

### Configurations

#### Selecting Pushdown as the Dataplane Engine

- **New Data Source**: When configuring a new data source that supports Pushdown, choose Pushdown as the dataplane engine from the Connection Details page.

![](https://uploads.developerhub.io/prod/Yoq2/mse49to52yvqdkcixn87mab9l6hqtspfljn7ewplcad6293srz4fqukt4o9btgep.png)

- **Existing Data Source**: To change the dataplane engine from Spark to Pushdown, use the [Profile](https://docs.acceldata.io/adoc-v4.5.0/documentation/asset-details#profile) in the  for already installed data sources.

![](https://uploads.developerhub.io/prod/Yoq2/33uww3hgyzdkjae4vkz0wblbpzdhlq8ucionp1eycrb97n7pvycbc1b8smwcg3it.png)

> Auto-Tag and Patterns Features: These are not functional when Pushdown is selected as the Dataplane Engine due to compatibility issues.

![](https://uploads.developerhub.io/prod/Yoq2/n1udqfnil0dwaedefglay6568p6c9xp4wgeqeqwsli2u899e43uy5ylx0ooh8ly4.png)

#### Creating Data Quality Policies

When defining a data quality policy for a Snowflake asset, you can select Pushdown as the data processing engine. This can be done during the [Data Quality Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy) creation.

![](https://uploads.developerhub.io/prod/Yoq2/21wbgtcy5yqp5ccsb79wprbsu4qaqixjj8nrv76kxx9i5yqudxcq2sbufqnj2xev.png)

> While Pushdown offers significant advantages, certain features are currently not supported:&gt; &gt; 1. Persistence of Records and Spark Job Resources Configurations: These will be disabled.&gt; 2. Rule Definitions: Certain rule definitions, such as Data Policy Templates, SQ Rules, User Defined Rules, and Lookups, are not supported.

---

### Best Practices for Using Pushdown Data Engines

To maximize the benefits of the Pushdown Data Engine in ADOC,  it is essential to follow best practices that ensure optimal performance, effective resource utilization, and continuous improvement. Here are key strategies to consider:

#### Evaluate Workloads

- **Identify Optimal Workloads**: Concentrate on large datasets and sophisticated queries that benefit from less data movement and faster processing.
- **Leverage Native Capabilities**: Pushdown is best suited for workloads that make use of your data source's native processing capabilities, like Snowflake.

#### Monitor Performance

- **Set benchmarks**: Create performance measures to track efficiency improvements.
- **Utilize Monitoring Tools**: Monitor query execution times, resource utilization, and data transfer rates using ADOC's built-in features.
- **Identify and resolve bottlenecks**: analyze performance data on a regular basis and tweak configurations to achieve the best results.

#### Stay Updated

- **Follow ADOC Releases and Documentation**: Stay up to date on our new features and performance enhancements. Each update may include performance enhancements, new features, and bug fixes that can improve the efficiency of Pushdown.