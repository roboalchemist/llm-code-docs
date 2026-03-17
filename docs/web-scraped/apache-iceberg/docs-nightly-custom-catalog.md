# Source: https://iceberg.apache.org/docs/nightly/custom-catalog/

Title: Java Custom Catalog - Apache Iceberg™

URL Source: https://iceberg.apache.org/docs/nightly/custom-catalog/

Markdown Content:
Java Custom Catalog - Apache Iceberg™
===============
- [x] - [x] 

[Skip to content](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-catalog)

[![Image 1: logo](https://iceberg.apache.org/assets/images/Iceberg-logo.svg)](https://iceberg.apache.org/ "Apache Iceberg™")

Apache Iceberg™

Apache Iceberg™

 Initializing search 

[](https://iceberg.apache.org/community/ "iceberg.apache.org")[](https://github.com/apache/iceberg "github.com")[](https://www.youtube.com/@ApacheIceberg "www.youtube.com")[](https://join.slack.com/t/apache-iceberg/shared_invite/zt-3kclosz6r-3heAW3d~_PHefmN2A_~cAg "join.slack.com")

*   [Home](https://iceberg.apache.org/)
*   [Quickstart](https://iceberg.apache.org/spark-quickstart/)
*   [Docs](https://iceberg.apache.org/docs/nightly/)
*   [Releases](https://iceberg.apache.org/releases/)
*   [Project](https://iceberg.apache.org/contribute/)
*   [Community](https://iceberg.apache.org/community/)
*   [Blog](https://iceberg.apache.org/blog/)
*   [Specification](https://iceberg.apache.org/terms/)

[![Image 2: logo](https://iceberg.apache.org/assets/images/Iceberg-logo.svg)](https://iceberg.apache.org/ "Apache Iceberg™") Apache Iceberg™  
*   [Home](https://iceberg.apache.org/)
*   - [x]  Quickstart   Quickstart  
    *   [Spark](https://iceberg.apache.org/spark-quickstart/)
    *   [Flink](https://iceberg.apache.org/flink-quickstart/)
    *   [Hive](https://iceberg.apache.org/hive-quickstart/)

*   - [x]  Docs   Docs  
    *   - [x]  Java   Java  
        *   - [x]  Nightly   Nightly  
            *   [Introduction](https://iceberg.apache.org/docs/nightly/)
            *   - [x]  Concepts   Concepts  
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/nightly/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/nightly/configuration/)
                    *   [Encryption](https://iceberg.apache.org/docs/nightly/encryption/)
                    *   [Evolution](https://iceberg.apache.org/docs/nightly/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/nightly/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/nightly/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/nightly/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/nightly/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/nightly/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/nightly/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/nightly/view-configuration/)

            *   - [x]  API   API  
                *   [Quickstart](https://iceberg.apache.org/docs/nightly/java-api-quickstart/)
                *   [API](https://iceberg.apache.org/docs/nightly/api/)
                *   [File I/O](https://iceberg.apache.org/docs/nightly/fileio/)
                *   [Javadoc](https://iceberg.apache.org/javadoc/nightly)

            *   - [x]  Integrations   Integrations  
                *   - [x]  Apache Spark   Apache Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/nightly/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/nightly/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/nightly/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/nightly/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/nightly/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/nightly/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/nightly/spark-writes/)

                *   - [x]  Apache Flink   Apache Flink  
                    *   [Getting Started](https://iceberg.apache.org/docs/nightly/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/nightly/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/nightly/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/nightly/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/nightly/flink-writes/)
                    *   [Flink TableMaintenance](https://iceberg.apache.org/docs/nightly/flink-maintenance/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/nightly/flink-configuration/)

                *   [Kafka Connect](https://iceberg.apache.org/docs/nightly/kafka-connect/)
                *   [Apache Hive](https://iceberg.apache.org/docs/nightly/hive/)

            *   - [x]  Migration   Migration  
                *   [Overview](https://iceberg.apache.org/docs/nightly/table-migration/)
                *   [Hive Migration](https://iceberg.apache.org/docs/nightly/hive-migration/)
                *   [Delta Lake Migration](https://iceberg.apache.org/docs/nightly/delta-lake-migration/)

            *   - [x]  Catalogs   Catalogs  
                *   [AWS Glue](https://iceberg.apache.org/docs/nightly/aws/#glue-catalog)
                *   [AWS DynamoDB](https://iceberg.apache.org/docs/nightly/aws/#dynamodb-catalog)
                *   [HadoopCatalog](https://iceberg.apache.org/javadoc/nightly/org/apache/iceberg/hadoop/HadoopCatalog.html)
                *   [HiveCatalog](https://iceberg.apache.org/docs/nightly/hive/#global-hive-catalog)
                *   [JDBC](https://iceberg.apache.org/docs/nightly/jdbc/)
                *   - [x]  Java Custom Catalog  [Java Custom Catalog](https://iceberg.apache.org/docs/nightly/custom-catalog/) Table of contents  
                    *   [Custom table operations implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-table-operations-implementation)
                    *   [Custom catalog implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-catalog-implementation)
                    *   [Custom file IO implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-file-io-implementation)
                    *   [Custom location provider implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-location-provider-implementation)
                    *   [Custom IcebergSource](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-icebergsource)

                *   [Nessie](https://iceberg.apache.org/docs/nightly/nessie/)

            *   - [x]  Storage   Storage  
                *   [AWS S3](https://iceberg.apache.org/docs/nightly/aws/#s3-fileio)
                *   [Dell ECS](https://iceberg.apache.org/docs/nightly/dell/)

        *   - [x]  Latest (1.10.1)   Latest (1.10.1)  
            *   [Introduction](https://iceberg.apache.org/docs/latest/)
            *   - [x]  Concepts   Concepts  
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/latest/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/latest/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/latest/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/latest/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/latest/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/latest/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/latest/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/latest/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/latest/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/latest/view-configuration/)

            *   - [x]  API   API  
                *   [Quickstart](https://iceberg.apache.org/docs/latest/java-api-quickstart/)
                *   [API](https://iceberg.apache.org/docs/latest/api/)
                *   [Javadoc](https://iceberg.apache.org/javadoc/latest)

            *   - [x]  Integrations   Integrations  
                *   - [x]  Apache Spark   Apache Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/latest/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/latest/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/latest/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/latest/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/latest/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/latest/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/latest/spark-writes/)

                *   - [x]  Apache Flink   Apache Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/latest/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/latest/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/latest/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/latest/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/latest/flink-writes/)
                    *   [Flink TableMaintenance](https://iceberg.apache.org/docs/latest/flink-maintenance/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/latest/flink-configuration/)

                *   [Kafka Connect](https://iceberg.apache.org/docs/latest/kafka-connect/)
                *   [Apache Hive](https://iceberg.apache.org/docs/latest/hive/)
                *   - [x]  Third-party   Third-party  
                    *   [Apache Amoro](https://iceberg.apache.org/docs/latest/amoro/)
                    *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                    *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                    *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                    *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                    *   [Apache Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                    *   [Apache Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                    *   [BladePipe](https://iceberg.apache.org/docs/latest/bladepipe/)
                    *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                    *   [Daft](https://iceberg.apache.org/docs/latest/daft/)
                    *   [Databend](https://docs.databend.com/guides/access-data-lake/iceberg)
                    *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                    *   [DuckDB](https://duckdb.org/docs/preview/core_extensions/iceberg/overview)
                    *   [Estuary](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
                    *   [Firebolt](https://docs.firebolt.io/reference-sql/functions-reference/table-valued/read_iceberg)
                    *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                    *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                    *   [Memiiso Debezium](https://memiiso.github.io/debezium-server-iceberg/)
                    *   [OLake](https://olake.io/docs)
                    *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                    *   [Redpanda](https://docs.redpanda.com/current/manage/iceberg/about-iceberg-topics)
                    *   [RisingWave](https://iceberg.apache.org/docs/latest/risingwave/)
                    *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                    *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                    *   [Tinybird](https://www.tinybird.co/docs/forward/get-data-in/table-functions/iceberg)
                    *   [Trino](https://trino.io/docs/current/connector/iceberg.html)

            *   - [x]  Catalogs   Catalogs  
                *   [AWS Glue](https://iceberg.apache.org/docs/latest/aws/#glue-catalog)
                *   [AWS DynamoDB](https://iceberg.apache.org/docs/latest/aws/#dynamodb-catalog)
                *   [Java Custom Catalog](https://iceberg.apache.org/docs/latest/custom-catalog/)
                *   [JDBC](https://iceberg.apache.org/docs/latest/jdbc/)
                *   [Nessie](https://iceberg.apache.org/docs/latest/nessie/)

            *   - [x]  Storage   Storage  
                *   [AWS S3](https://iceberg.apache.org/docs/latest/aws/#s3-fileio)
                *   [Dell ECS](https://iceberg.apache.org/docs/latest/dell/)

        *   - [x]  Previous   Previous  
            *   - [x]  1.10.0   1.10.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.10.0/)
                *   - [x]  Concepts   Concepts  
                    *   - [x]  Tables   Tables  
                        *   [Branching and Tagging](https://iceberg.apache.org/docs/1.10.0/branching/)
                        *   [Configuration](https://iceberg.apache.org/docs/1.10.0/configuration/)
                        *   [Evolution](https://iceberg.apache.org/docs/1.10.0/evolution/)
                        *   [Maintenance](https://iceberg.apache.org/docs/1.10.0/maintenance/)
                        *   [Metrics Reporting](https://iceberg.apache.org/docs/1.10.0/metrics-reporting/)
                        *   [Partitioning](https://iceberg.apache.org/docs/1.10.0/partitioning/)
                        *   [Performance](https://iceberg.apache.org/docs/1.10.0/performance/)
                        *   [Reliability](https://iceberg.apache.org/docs/1.10.0/reliability/)
                        *   [Schemas](https://iceberg.apache.org/docs/1.10.0/schemas/)

                    *   - [x]  Views   Views  
                        *   [Configuration](https://iceberg.apache.org/docs/1.10.0/view-configuration/)

                *   - [x]  API   API  
                    *   [Quickstart](https://iceberg.apache.org/docs/1.10.0/java-api-quickstart/)
                    *   [API](https://iceberg.apache.org/docs/1.10.0/api/)
                    *   [Javadoc](https://iceberg.apache.org/javadoc/latest/)

                *   - [x]  Integrations   Integrations  
                    *   - [x]  Apache Spark   Apache Spark  
                        *   [Getting Started](https://iceberg.apache.org/docs/1.10.0/spark-getting-started/)
                        *   [Configuration](https://iceberg.apache.org/docs/1.10.0/spark-configuration/)
                        *   [DDL](https://iceberg.apache.org/docs/1.10.0/spark-ddl/)
                        *   [Procedures](https://iceberg.apache.org/docs/1.10.0/spark-procedures/)
                        *   [Queries](https://iceberg.apache.org/docs/1.10.0/spark-queries/)
                        *   [Structured Streaming](https://iceberg.apache.org/docs/1.10.0/spark-structured-streaming/)
                        *   [Writes](https://iceberg.apache.org/docs/1.10.0/spark-writes/)

                    *   - [x]  Apache Flink   Apache Flink  
                        *   [Flink Getting Started](https://iceberg.apache.org/docs/1.10.0/flink/)
                        *   [Flink Connector](https://iceberg.apache.org/docs/1.10.0/flink-connector/)
                        *   [Flink DDL](https://iceberg.apache.org/docs/1.10.0/flink-ddl/)
                        *   [Flink Queries](https://iceberg.apache.org/docs/1.10.0/flink-queries/)
                        *   [Flink Writes](https://iceberg.apache.org/docs/1.10.0/flink-writes/)
                        *   [Flink TableMaintenance](https://iceberg.apache.org/docs/1.10.0/flink-maintenance/)
                        *   [Flink Configuration](https://iceberg.apache.org/docs/1.10.0/flink-configuration/)

                    *   [Kafka Connect](https://iceberg.apache.org/docs/1.10.0/kafka-connect/)
                    *   [Apache Hive](https://iceberg.apache.org/docs/1.10.0/hive/)
                    *   - [x]  Third-party   Third-party  
                        *   [Apache Amoro](https://iceberg.apache.org/docs/1.10.0/amoro/)
                        *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                        *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                        *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                        *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                        *   [Apache Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                        *   [Apache Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                        *   [BladePipe](https://iceberg.apache.org/docs/1.10.0/bladepipe/)
                        *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                        *   [Daft](https://iceberg.apache.org/docs/1.10.0/daft/)
                        *   [Databend](https://docs.databend.com/guides/access-data-lake/iceberg)
                        *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                        *   [DuckDB](https://duckdb.org/docs/preview/core_extensions/iceberg/overview)
                        *   [Estuary](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
                        *   [Firebolt](https://docs.firebolt.io/reference-sql/functions-reference/table-valued/read_iceberg)
                        *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                        *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                        *   [Memiiso Debezium](https://memiiso.github.io/debezium-server-iceberg/)
                        *   [OLake](https://olake.io/docs)
                        *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                        *   [Redpanda](https://docs.redpanda.com/current/manage/iceberg/about-iceberg-topics)
                        *   [RisingWave](https://iceberg.apache.org/docs/1.10.0/risingwave/)
                        *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                        *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                        *   [Tinybird](https://www.tinybird.co/docs/forward/get-data-in/table-functions/iceberg)
                        *   [Trino](https://trino.io/docs/current/connector/iceberg.html)

                *   - [x]  Catalogs   Catalogs  
                    *   [AWS Glue](https://iceberg.apache.org/docs/1.10.0/aws/#glue-catalog)
                    *   [AWS DynamoDB](https://iceberg.apache.org/docs/1.10.0/aws/#dynamodb-catalog)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.10.0/custom-catalog/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.10.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.10.0/nessie/)

                *   - [x]  Storage   Storage  
                    *   [AWS S3](https://iceberg.apache.org/docs/1.10.0/aws/#s3-fileio)
                    *   [Dell ECS](https://iceberg.apache.org/docs/1.10.0/dell/)

            *   - [x]  1.9.2   1.9.2  
                *   [Introduction](https://iceberg.apache.org/docs/1.9.2/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.9.2/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.2/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.9.2/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.9.2/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.9.2/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.9.2/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.9.2/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.9.2/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.9.2/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.2/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.9.2/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.2/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.9.2/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.9.2/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.9.2/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.9.2/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.9.2/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.9.2/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.9.2/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.9.2/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.9.2/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.9.2/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.9.2/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.9.2/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.9.2/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.9.2/daft/)
                *   [Estuary](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
                *   [RisingWave](https://iceberg.apache.org/docs/1.9.2/risingwave/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amoro](https://iceberg.apache.org/docs/1.9.2/amoro/)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.9.2/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.9.2/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.9.2/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.9.2/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.9.2/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.9.2/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.9.2/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.9.2/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/latest/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)
                *   [IcebergGo](https://pkg.go.dev/github.com/apache/iceberg-go/)

            *   - [x]  1.9.1   1.9.1  
                *   [Introduction](https://iceberg.apache.org/docs/1.9.1/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.9.1/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.1/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.9.1/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.9.1/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.9.1/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.9.1/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.9.1/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.9.1/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.9.1/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.1/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.9.1/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.1/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.9.1/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.9.1/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.9.1/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.9.1/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.9.1/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.9.1/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.9.1/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.9.1/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.9.1/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.9.1/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.9.1/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.9.1/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.9.1/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.9.1/daft/)
                *   [Estuary](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
                *   [RisingWave](https://iceberg.apache.org/docs/1.9.1/risingwave/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amoro](https://iceberg.apache.org/docs/1.9.1/amoro/)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.9.1/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.9.1/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.9.1/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.9.1/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.9.1/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.9.1/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.9.1/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.9.1/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/latest/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)
                *   [IcebergGo](https://pkg.go.dev/github.com/apache/iceberg-go/)

            *   - [x]  1.9.0   1.9.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.9.0/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.9.0/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.0/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.9.0/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.9.0/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.9.0/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.9.0/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.9.0/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.9.0/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.9.0/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.0/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.9.0/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.9.0/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.9.0/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.9.0/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.9.0/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.9.0/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.9.0/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.9.0/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.9.0/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.9.0/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.9.0/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.9.0/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.9.0/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.9.0/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.9.0/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.9.0/daft/)
                *   [Estuary](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
                *   [RisingWave](https://iceberg.apache.org/docs/1.9.0/risingwave/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amoro](https://iceberg.apache.org/docs/1.9.0/amoro/)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.9.0/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.9.0/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.9.0/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.9.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.9.0/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.9.0/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.9.0/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.9.0/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/latest/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)
                *   [IcebergGo](https://pkg.go.dev/github.com/apache/iceberg-go/)

            *   - [x]  1.8.1   1.8.1  
                *   [Introduction](https://iceberg.apache.org/docs/1.8.1/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.8.1/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.8.1/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.8.1/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.8.1/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.8.1/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.8.1/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.8.1/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.8.1/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.8.1/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.8.1/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.8.1/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.8.1/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.8.1/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.8.1/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.8.1/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.8.1/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.8.1/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.8.1/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.8.1/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.8.1/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.8.1/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.8.1/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.8.1/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.8.1/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.8.1/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.8.1/daft/)
                *   [RisingWave](https://iceberg.apache.org/docs/1.8.1/risingwave/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.8.1/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.8.1/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.8.1/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.8.1/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.8.1/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.8.1/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.8.1/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.8.1/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.8.1/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)
                *   [IcebergGo](https://pkg.go.dev/github.com/apache/iceberg-go/)

            *   - [x]  1.8.0   1.8.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.8.0/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.8.0/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.8.0/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.8.0/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.8.0/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.8.0/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.8.0/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.8.0/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.8.0/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.8.0/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.8.0/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.8.0/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.8.0/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.8.0/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.8.0/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.8.0/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.8.0/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.8.0/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.8.0/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.8.0/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.8.0/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.8.0/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.8.0/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.8.0/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.8.0/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.8.0/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.8.0/daft/)
                *   [RisingWave](https://iceberg.apache.org/docs/1.8.0/risingwave/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.8.0/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.8.0/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.8.0/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.8.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.8.0/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.8.0/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.8.0/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.8.0/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.8.0/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)
                *   [IcebergGo](https://pkg.go.dev/github.com/apache/iceberg-go/)

            *   - [x]  1.7.2   1.7.2  
                *   [Introduction](https://iceberg.apache.org/docs/1.7.2/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.7.2/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.2/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.7.2/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.7.2/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.7.2/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.7.2/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.7.2/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.7.2/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.7.2/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.2/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.7.2/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.2/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.7.2/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.7.2/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.7.2/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.7.2/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.7.2/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.7.2/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.7.2/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.7.2/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.7.2/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.7.2/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.7.2/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.7.2/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.7.2/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.7.2/daft/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.7.2/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.7.2/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.7.2/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.7.2/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.7.2/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.7.2/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.7.2/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.7.2/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.7.2)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.7.1   1.7.1  
                *   [Introduction](https://iceberg.apache.org/docs/1.7.1/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.7.1/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.1/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.7.1/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.7.1/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.7.1/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.7.1/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.7.1/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.7.1/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.7.1/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.1/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.7.1/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.1/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.7.1/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.7.1/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.7.1/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.7.1/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.7.1/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.7.1/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.7.1/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.7.1/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.7.1/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.7.1/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.7.1/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.7.1/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.7.1/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.7.1/daft/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.7.1/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.7.1/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.7.1/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.7.1/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.7.1/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.7.1/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.7.1/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.7.1/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.7.1)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.7.0   1.7.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.7.0/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.7.0/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.0/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.7.0/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.7.0/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.7.0/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.7.0/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.7.0/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.7.0/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.7.0/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.0/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.7.0/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.7.0/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.7.0/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.7.0/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.7.0/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.7.0/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.7.0/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.7.0/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.7.0/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.7.0/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.7.0/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.7.0/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.7.0/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.7.0/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.7.0/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.7.0/daft/)
                *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
                *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   [Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
                *   [Kafka Connect](https://iceberg.apache.org/docs/1.7.0/kafka-connect/)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.7.0/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.7.0/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.7.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.7.0/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.7.0/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.7.0/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.7.0/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.7.0/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.6.1   1.6.1  
                *   [Introduction](https://iceberg.apache.org/docs/1.6.1/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.6.1/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.6.1/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.6.1/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.6.1/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.6.1/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.6.1/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.6.1/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.6.1/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.6.1/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.6.1/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.6.1/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.6.1/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.6.1/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.6.1/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.6.1/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.6.1/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.6.1/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.6.1/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.6.1/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.6.1/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.6.1/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.6.1/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.6.1/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.6.1/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.6.1/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.6.1/daft/)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.6.1/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.6.1/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.6.1/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.6.1/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.6.1/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.6.1/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.6.1/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.6.1/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.6.0   1.6.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.6.0/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.6.0/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.6.0/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.6.0/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.6.0/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.6.0/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.6.0/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.6.0/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.6.0/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.6.0/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.6.0/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.6.0/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.6.0/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.6.0/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.6.0/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.6.0/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.6.0/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.6.0/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.6.0/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.6.0/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.6.0/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.6.0/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.6.0/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.6.0/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.6.0/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.6.0/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Daft](https://iceberg.apache.org/docs/1.6.0/daft/)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.6.0/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.6.0/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.6.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.6.0/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.6.0/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.6.0/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.6.0/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.6.0/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.5.2   1.5.2  
                *   [Introduction](https://iceberg.apache.org/docs/1.5.2/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.5.2/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.2/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.5.2/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.5.2/maintenance/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.5.2/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.5.2/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.5.2/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.5.2/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.2/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.5.2/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.2/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.5.2/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.5.2/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.5.2/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.5.2/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.5.2/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.5.2/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.5.2/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.5.2/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.5.2/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.5.2/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.5.2/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.5.2/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.5.2/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.5.2/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.5.2/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.5.2/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.5.2/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.5.2/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.5.2/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.5.2/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.5.2/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.5.1   1.5.1  
                *   [Introduction](https://iceberg.apache.org/docs/1.5.1/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.5.1/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.1/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.5.1/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.5.1/maintenance/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.5.1/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.5.1/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.5.1/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.5.1/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.1/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.5.1/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.1/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.5.1/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.5.1/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.5.1/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.5.1/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.5.1/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.5.1/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.5.1/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.5.1/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.5.1/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.5.1/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.5.1/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.5.1/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.5.1/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.5.1/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.5.1/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.5.1/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.5.1/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.5.1/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.5.1/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.5.1/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.5.1/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.5.0   1.5.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.5.0/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.5.0/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.0/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.5.0/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.5.0/maintenance/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.5.0/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.5.0/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.5.0/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.5.0/schemas/)

                *   - [x]  Views   Views  
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.0/view-configuration/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.5.0/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.5.0/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.5.0/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.5.0/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.5.0/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.5.0/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.5.0/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.5.0/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.5.0/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.5.0/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.5.0/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.5.0/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.5.0/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.5.0/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.5.0/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.5.0/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.5.0/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.5.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.5.0/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.5.0/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.5.0/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.5.0/custom-catalog/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.5.0/)
                *   [PyIceberg](https://py.iceberg.apache.org/)
                *   [IcebergRust](https://rust.iceberg.apache.org/)

            *   - [x]  1.4.3   1.4.3  
                *   [Introduction](https://iceberg.apache.org/docs/1.4.3/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.4.3/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.3/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.4.3/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.4.3/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.4.3/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.4.3/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.4.3/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.4.3/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.4.3/schemas/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.4.3/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.3/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.4.3/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.4.3/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.4.3/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.4.3/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.4.3/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.4.3/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.4.3/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.4.3/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.4.3/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.4.3/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.4.3/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.4.3/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.4.3/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.4.3/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.4.3/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.4.3/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.4.3/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.4.3/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.4.3/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.4.3/custom-catalog/)

                *   - [x]  Migration   Migration  
                    *   [Overview](https://iceberg.apache.org/docs/1.4.3/table-migration/)
                    *   [Hive Migration](https://iceberg.apache.org/docs/1.4.3/hive-migration/)
                    *   [Delta Lake Migration](https://iceberg.apache.org/docs/1.4.3/delta-lake-migration/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.4.3)
                *   [PyIceberg](https://py.iceberg.apache.org/)

            *   - [x]  1.4.2   1.4.2  
                *   [Introduction](https://iceberg.apache.org/docs/1.4.2/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.4.2/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.2/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.4.2/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.4.2/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.4.2/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.4.2/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.4.2/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.4.2/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.4.2/schemas/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.4.2/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.2/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.4.2/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.4.2/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.4.2/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.4.2/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.4.2/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.4.2/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.4.2/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.4.2/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.4.2/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.4.2/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.4.2/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.4.2/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.4.2/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.4.2/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.4.2/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.4.2/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.4.2/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.4.2/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.4.2/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.4.2/custom-catalog/)

                *   - [x]  Migration   Migration  
                    *   [Overview](https://iceberg.apache.org/docs/1.4.2/table-migration/)
                    *   [Hive Migration](https://iceberg.apache.org/docs/1.4.2/hive-migration/)
                    *   [Delta Lake Migration](https://iceberg.apache.org/docs/1.4.2/delta-lake-migration/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.4.2)
                *   [PyIceberg](https://py.iceberg.apache.org/)

            *   - [x]  1.4.1   1.4.1  
                *   [Introduction](https://iceberg.apache.org/docs/1.4.1/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.4.1/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.1/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.4.1/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.4.1/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.4.1/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.4.1/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.4.1/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.4.1/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.4.1/schemas/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.4.1/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.1/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.4.1/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.4.1/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.4.1/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.4.1/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.4.1/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.4.1/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.4.1/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.4.1/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.4.1/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.4.1/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.4.1/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.4.1/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.4.1/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.4.1/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.4.1/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.4.1/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.4.1/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.4.1/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.4.1/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.4.1/custom-catalog/)

                *   - [x]  Migration   Migration  
                    *   [Overview](https://iceberg.apache.org/docs/1.4.1/table-migration/)
                    *   [Hive Migration](https://iceberg.apache.org/docs/1.4.1/hive-migration/)
                    *   [Delta Lake Migration](https://iceberg.apache.org/docs/1.4.1/delta-lake-migration/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.4.1/)
                *   [PyIceberg](https://py.iceberg.apache.org/)

            *   - [x]  1.4.0   1.4.0  
                *   [Introduction](https://iceberg.apache.org/docs/1.4.0/)
                *   - [x]  Tables   Tables  
                    *   [Branching and Tagging](https://iceberg.apache.org/docs/1.4.0/branching/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.0/configuration/)
                    *   [Evolution](https://iceberg.apache.org/docs/1.4.0/evolution/)
                    *   [Maintenance](https://iceberg.apache.org/docs/1.4.0/maintenance/)
                    *   [Metrics Reporting](https://iceberg.apache.org/docs/1.4.0/metrics-reporting/)
                    *   [Partitioning](https://iceberg.apache.org/docs/1.4.0/partitioning/)
                    *   [Performance](https://iceberg.apache.org/docs/1.4.0/performance/)
                    *   [Reliability](https://iceberg.apache.org/docs/1.4.0/reliability/)
                    *   [Schemas](https://iceberg.apache.org/docs/1.4.0/schemas/)

                *   - [x]  Spark   Spark  
                    *   [Getting Started](https://iceberg.apache.org/docs/1.4.0/spark-getting-started/)
                    *   [Configuration](https://iceberg.apache.org/docs/1.4.0/spark-configuration/)
                    *   [DDL](https://iceberg.apache.org/docs/1.4.0/spark-ddl/)
                    *   [Procedures](https://iceberg.apache.org/docs/1.4.0/spark-procedures/)
                    *   [Queries](https://iceberg.apache.org/docs/1.4.0/spark-queries/)
                    *   [Structured Streaming](https://iceberg.apache.org/docs/1.4.0/spark-structured-streaming/)
                    *   [Writes](https://iceberg.apache.org/docs/1.4.0/spark-writes/)

                *   - [x]  Flink   Flink  
                    *   [Flink Getting Started](https://iceberg.apache.org/docs/1.4.0/flink/)
                    *   [Flink Connector](https://iceberg.apache.org/docs/1.4.0/flink-connector/)
                    *   [Flink DDL](https://iceberg.apache.org/docs/1.4.0/flink-ddl/)
                    *   [Flink Queries](https://iceberg.apache.org/docs/1.4.0/flink-queries/)
                    *   [Flink Writes](https://iceberg.apache.org/docs/1.4.0/flink-writes/)
                    *   [Flink Actions](https://iceberg.apache.org/docs/1.4.0/flink-actions/)
                    *   [Flink Configuration](https://iceberg.apache.org/docs/1.4.0/flink-configuration/)

                *   [Hive](https://iceberg.apache.org/docs/1.4.0/hive/)
                *   [Trino](https://trino.io/docs/current/connector/iceberg.html)
                *   [Clickhouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
                *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
                *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
                *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
                *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
                *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
                *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
                *   [Doris](https://doris.apache.org/docs/dev/lakehouse/datalake-analytics/iceberg)
                *   - [x]  Integrations   Integrations  
                    *   [AWS](https://iceberg.apache.org/docs/1.4.0/aws/)
                    *   [Dell](https://iceberg.apache.org/docs/1.4.0/dell/)
                    *   [JDBC](https://iceberg.apache.org/docs/1.4.0/jdbc/)
                    *   [Nessie](https://iceberg.apache.org/docs/1.4.0/nessie/)

                *   - [x]  API   API  
                    *   [Java Quickstart](https://iceberg.apache.org/docs/1.4.0/java-api-quickstart/)
                    *   [Java API](https://iceberg.apache.org/docs/1.4.0/api/)
                    *   [Java Custom Catalog](https://iceberg.apache.org/docs/1.4.0/custom-catalog/)

                *   - [x]  Migration   Migration  
                    *   [Overview](https://iceberg.apache.org/docs/1.4.0/table-migration/)
                    *   [Hive Migration](https://iceberg.apache.org/docs/1.4.0/hive-migration/)
                    *   [Delta Lake Migration](https://iceberg.apache.org/docs/1.4.0/delta-lake-migration/)

                *   [Javadoc](https://iceberg.apache.org/javadoc/1.4.0/)
                *   [PyIceberg](https://py.iceberg.apache.org/)

            *   [archive](https://iceberg.apache.org/archive/)

    *   - [x]  Other Implementations   Other Implementations  
        *   [Python](https://py.iceberg.apache.org/)
        *   [Rust](https://rust.iceberg.apache.org/)
        *   [Go](https://go.iceberg.apache.org/)
        *   [C++](https://cpp.iceberg.apache.org/)

    *   - [x]  Third-party   Third-party  
        *   - [x]  Catalogs   Catalogs  
            *   [Apache Gravitino](https://gravitino.apache.org/)
            *   [Apache Polaris](https://polaris.apache.org/)
            *   [Boring Catalog](https://github.com/boringdata/boring-catalog)
            *   [DataHub](https://docs.datahub.com/docs/iceberg-catalog)
            *   [Google BigLake metastore](https://cloud.google.com/bigquery/docs/blms-manage-resources)
            *   [Lakekeeper](https://github.com/lakekeeper/lakekeeper)

        *   - [x]  Integrations   Integrations  
            *   [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)
            *   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-destination.html)
            *   [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html)
            *   [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html)
            *   [Apache Amoro](https://iceberg.apache.org/integrations/amoro/)
            *   [Apache Doris](https://doris.apache.org/docs/dev/lakehouse/catalogs/iceberg-catalog)
            *   [Apache Druid](https://druid.apache.org/docs/latest/development/extensions-contrib/iceberg/)
            *   [Apache Fluss](https://fluss.apache.org/docs/next/streaming-lakehouse/integrate-data-lakes/iceberg/)
            *   [BladePipe](https://www.bladepipe.com/docs/dataMigrationAndSync/datasource_func/Iceberg/props_for_iceberg_ds)
            *   [ClickHouse](https://clickhouse.com/docs/en/engines/table-engines/integrations/iceberg)
            *   [Daft](https://iceberg.apache.org/integrations/daft/)
            *   [Databend](https://docs.databend.com/guides/access-data-lake/iceberg)
            *   [Dremio](https://docs.dremio.com/data-formats/apache-iceberg/)
            *   [DuckDB](https://duckdb.org/docs/preview/core_extensions/iceberg/overview)
            *   [Estuary](https://docs.estuary.dev/reference/Connectors/materialization-connectors/apache-iceberg/)
            *   [Firebolt](https://docs.firebolt.io/reference-sql/functions-reference/table-valued/read_iceberg)
            *   [Google BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables)
            *   [Impala](https://impala.apache.org/docs/build/html/topics/impala_iceberg.html)
            *   [Memiiso Debezium](https://memiiso.github.io/debezium-server-iceberg/)
            *   [Microsoft OneLake](https://aka.ms/onelakeircdocs)
            *   [Nimtable](https://github.com/nimtable/nimtable)
            *   [OLake](https://olake.io/docs)
            *   [Presto](https://prestodb.io/docs/current/connector/iceberg.html)
            *   [Redpanda](https://docs.redpanda.com/current/manage/iceberg/about-iceberg-topics)
            *   [RisingWave](https://iceberg.apache.org/integrations/risingwave/)
            *   [Ryft](https://docs.ryft.io/platform)
            *   [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg)
            *   [Starburst](https://docs.starburst.io/latest/connector/iceberg.html)
            *   [Starrocks](https://docs.starrocks.io/en-us/latest/data_source/catalog/iceberg_catalog)
            *   [Tinybird](https://www.tinybird.co/docs/forward/get-data-in/table-functions/iceberg)
            *   [Trino](https://trino.io/docs/current/connector/iceberg.html)

*   [Releases](https://iceberg.apache.org/releases/)
*   - [x]  Project   Project  
    *   [Contributing](https://iceberg.apache.org/contribute/)
    *   [Multi-engine support](https://iceberg.apache.org/multi-engine-support/)
    *   [Benchmarks](https://iceberg.apache.org/benchmarks/)
    *   [Security](https://iceberg.apache.org/security/)
    *   [How to release](https://iceberg.apache.org/how-to-release/)
    *   - [x]  ASF   ASF  
        *   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
        *   [Events](https://www.apache.org/events/current-event.html)
        *   [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
        *   [License](https://www.apache.org/licenses/)
        *   [Security](https://www.apache.org/security/)
        *   [Sponsors](https://www.apache.org/foundation/sponsors.html)

*   - [x]  Community   Community  
    *   [Community](https://iceberg.apache.org/community/)
    *   [Talks](https://iceberg.apache.org/talks/)
    *   [Vendors](https://iceberg.apache.org/vendors/)

*   [Blog](https://iceberg.apache.org/blog/)
*   - [x]  Specification   Specification  
    *   [Terms](https://iceberg.apache.org/terms/)
    *   [REST Catalog Spec](https://iceberg.apache.org/rest-catalog-spec/)
    *   [Table Spec](https://iceberg.apache.org/spec/)
    *   [View spec](https://iceberg.apache.org/view-spec/)
    *   [Puffin spec](https://iceberg.apache.org/puffin-spec/)
    *   [AES GCM Stream spec](https://iceberg.apache.org/gcm-stream-spec/)
    *   [UDF spec](https://iceberg.apache.org/udf-spec/)
    *   [Implementation status](https://iceberg.apache.org/status/)

 Table of contents  
*   [Custom table operations implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-table-operations-implementation)
*   [Custom catalog implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-catalog-implementation)
*   [Custom file IO implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-file-io-implementation)
*   [Custom location provider implementation](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-location-provider-implementation)
*   [Custom IcebergSource](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-icebergsource)

1.   [Home](https://iceberg.apache.org/)
2.   [Docs](https://iceberg.apache.org/docs/nightly/)
3.   [Java](https://iceberg.apache.org/docs/nightly/)
4.   [Nightly](https://iceberg.apache.org/docs/nightly/)
5.   [Catalogs](https://iceberg.apache.org/docs/nightly/aws/#glue-catalog)

Custom Catalog[🔗](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-catalog "Permanent link")
===========================================================================================================

It's possible to read an iceberg table either from an hdfs path or from a hive table. It's also possible to use a custom metastore in place of hive. The steps to do that are as follows.

*   [Custom TableOperations](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-table-operations-implementation)
*   [Custom Catalog](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-catalog-implementation)
*   [Custom FileIO](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-file-io-implementation)
*   [Custom LocationProvider](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-location-provider-implementation)
*   [Custom IcebergSource](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-icebergsource)

Note: To work with encrypted tables, custom catalogs must address a number of security [requirements](https://iceberg.apache.org/docs/nightly/encryption/#catalog-security-requirements).

### Custom table operations implementation[🔗](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-table-operations-implementation "Permanent link")

Extend `BaseMetastoreTableOperations` to provide implementation on how to read and write metadata

Example:

```
class CustomTableOperations extends BaseMetastoreTableOperations {
  private String dbName;
  private String tableName;
  private Configuration conf;
  private FileIO fileIO;

  protected CustomTableOperations(Configuration conf, String dbName, String tableName) {
    this.conf = conf;
    this.dbName = dbName;
    this.tableName = tableName;
  }

  // The doRefresh method should provide implementation on how to get the metadata location
  @Override
  public void doRefresh() {

    // Example custom service which returns the metadata location given a dbName and tableName
    String metadataLocation = CustomService.getMetadataForTable(conf, dbName, tableName);

    // When updating from a metadata file location, call the helper method
    refreshFromMetadataLocation(metadataLocation);

  }

  // The doCommit method should provide implementation on how to update with metadata location atomically
  @Override
  public void doCommit(TableMetadata base, TableMetadata metadata) {
    String oldMetadataLocation = base.location();

    // Write new metadata using helper method
    String newMetadataLocation = writeNewMetadata(metadata, currentVersion() + 1);

    // Example custom service which updates the metadata location for the given db and table atomically
    CustomService.updateMetadataLocation(dbName, tableName, oldMetadataLocation, newMetadataLocation);

  }

  // The io method provides a FileIO which is used to read and write the table metadata files
  @Override
  public FileIO io() {
    if (fileIO == null) {
      fileIO = new HadoopFileIO(conf);
    }
    return fileIO;
  }
}
```

A `TableOperations` instance is usually obtained by calling `Catalog.newTableOps(TableIdentifier)`. See the next section about implementing and loading a custom catalog.

### Custom catalog implementation[🔗](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-catalog-implementation "Permanent link")

Extend `BaseMetastoreCatalog` to provide default warehouse locations and instantiate `CustomTableOperations`

Example:

```
public class CustomCatalog extends BaseMetastoreCatalog {

  private Configuration configuration;

  // must have a no-arg constructor to be dynamically loaded
  // initialize(String name, Map<String, String> properties) will be called to complete initialization
  public CustomCatalog() {
  }

  public CustomCatalog(Configuration configuration) {
    this.configuration = configuration;
  }

  @Override
  protected TableOperations newTableOps(TableIdentifier tableIdentifier) {
    String dbName = tableIdentifier.namespace().level(0);
    String tableName = tableIdentifier.name();
    // instantiate the CustomTableOperations
    return new CustomTableOperations(configuration, dbName, tableName);
  }

  @Override
  protected String defaultWarehouseLocation(TableIdentifier tableIdentifier) {

    // Can choose to use any other configuration name
    String tableLocation = configuration.get("custom.iceberg.warehouse.location");

    // Can be an s3 or hdfs path
    if (tableLocation == null) {
      throw new RuntimeException("custom.iceberg.warehouse.location configuration not set!");
    }

    return String.format(
            "%s/%s.db/%s", tableLocation,
            tableIdentifier.namespace().levels()[0],
            tableIdentifier.name());
  }

  @Override
  public boolean dropTable(TableIdentifier identifier, boolean purge) {
    // Example service to delete table
    CustomService.deleteTable(identifier.namespace().level(0), identifier.name());
  }

  @Override
  public void renameTable(TableIdentifier from, TableIdentifier to) {
    Preconditions.checkArgument(from.namespace().level(0).equals(to.namespace().level(0)),
            "Cannot move table between databases");
    // Example service to rename table
    CustomService.renameTable(from.namespace().level(0), from.name(), to.name());
  }

  // implement this method to read catalog name and properties during initialization
  public void initialize(String name, Map<String, String> properties) {
  }
}
```

Catalog implementations can be dynamically loaded in most compute engines. For Spark and Flink, you can specify the `catalog-impl` catalog property to load it. Read the [Configuration](https://iceberg.apache.org/docs/nightly/configuration/#catalog-properties) section for more details. For MapReduce, implement `org.apache.iceberg.mr.CatalogLoader` and set Hadoop property `iceberg.mr.catalog.loader.class` to load it. If your catalog must read Hadoop configuration to access certain environment properties, make your catalog implement `org.apache.hadoop.conf.Configurable`.

### Custom file IO implementation[🔗](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-file-io-implementation "Permanent link")

Extend `FileIO` and provide implementation to read and write data files

Example:

```
public class CustomFileIO implements FileIO {

  // must have a no-arg constructor to be dynamically loaded
  // initialize(Map<String, String> properties) will be called to complete initialization
  public CustomFileIO() {
  }

  @Override
  public InputFile newInputFile(String s) {
    // you also need to implement the InputFile interface for a custom input file
    return new CustomInputFile(s);
  }

  @Override
  public OutputFile newOutputFile(String s) {
    // you also need to implement the OutputFile interface for a custom output file
    return new CustomOutputFile(s);
  }

  @Override
  public void deleteFile(String path) {
    Path toDelete = new Path(path);
    FileSystem fs = Util.getFs(toDelete);
    try {
        fs.delete(toDelete, false /* not recursive */);
    } catch (IOException e) {
        throw new RuntimeIOException(e, "Failed to delete file: %s", path);
    }
  }

  // implement this method to read catalog properties during initialization
  public void initialize(Map<String, String> properties) {
  }
}
```

If you are already implementing your own catalog, you can implement `TableOperations.io()` to use your custom `FileIO`. In addition, custom `FileIO` implementations can also be dynamically loaded in `HadoopCatalog` and `HiveCatalog` by specifying the `io-impl` catalog property. Read the [Configuration](https://iceberg.apache.org/docs/nightly/configuration/#catalog-properties) section for more details. If your `FileIO` must read Hadoop configuration to access certain environment properties, make your `FileIO` implement `org.apache.hadoop.conf.Configurable`.

### Custom location provider implementation[🔗](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-location-provider-implementation "Permanent link")

Extend `LocationProvider` and provide implementation to determine the file path to write data

Example:

```
public class CustomLocationProvider implements LocationProvider {

  private String tableLocation;

  // must have a 2-arg constructor like this, or a no-arg constructor
  public CustomLocationProvider(String tableLocation, Map<String, String> properties) {
    this.tableLocation = tableLocation;
  }

  @Override
  public String newDataLocation(String filename) {
    // can use any custom method to generate a file path given a file name
    return String.format("%s/%s/%s", tableLocation, UUID.randomUUID().toString(), filename);
  }

  @Override
  public String newDataLocation(PartitionSpec spec, StructLike partitionData, String filename) {
    // can use any custom method to generate a file path given a partition info and file name
    return newDataLocation(filename);
  }
}
```

If you are already implementing your own catalog, you can override `TableOperations.locationProvider()` to use your custom default `LocationProvider`. To use a different custom location provider for a specific table, specify the implementation when creating the table using table property `write.location-provider.impl`

Example:

```
CREATE TABLE hive.default.my_table (
  id bigint,
  data string,
  category string)
USING iceberg
OPTIONS (
  'write.location-provider.impl'='com.my.CustomLocationProvider'
)
PARTITIONED BY (category);
```

### Custom IcebergSource[🔗](https://iceberg.apache.org/docs/nightly/custom-catalog/#custom-icebergsource "Permanent link")

Extend `IcebergSource` and provide implementation to read from `CustomCatalog`

Example:

```
public class CustomIcebergSource extends IcebergSource {

  @Override
  protected Table findTable(DataSourceOptions options, Configuration conf) {
    Optional<String> path = options.get("path");
    Preconditions.checkArgument(path.isPresent(), "Cannot open table: path is not set");

    // Read table from CustomCatalog
    CustomCatalog catalog = new CustomCatalog(conf);
    TableIdentifier tableIdentifier = TableIdentifier.parse(path.get());
    return catalog.loadTable(tableIdentifier);
  }
}
```

Register the `CustomIcebergSource` by updating `META-INF/services/org.apache.spark.sql.sources.DataSourceRegister` with its fully qualified name

 Back to top 

#### Features

*   [Schema Evolution](https://iceberg.apache.org/docs/latest/evolution/#schema-evolution)
*   [Hidden Partitioning](https://iceberg.apache.org/docs/latest/partitioning/)
*   [Partition Evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution)
*   [Serializable Isolation](https://iceberg.apache.org/docs/latest/reliability/)
*   [Branching and Tagging](https://iceberg.apache.org/docs/latest/branching/)
*   [Optimistic Concurrency](https://iceberg.apache.org/docs/latest/reliability/#concurrent-write-operations)
*   [Advanced Filtering](https://iceberg.apache.org/docs/latest/performance/#data-filtering)
*   [Compute Engine Integrations](https://iceberg.apache.org/docs/latest/)
*   [REST Catalog](https://iceberg.apache.org/terms/#decoupling-using-the-rest-catalog)
*   [Multiple language APIs](https://iceberg.apache.org/docs/latest/api/)

#### Get Started

*   [Spark Quickstart](https://iceberg.apache.org/spark-quickstart)
*   [Hive Quickstart](https://iceberg.apache.org/hive-quickstart)
*   [Open Table Spec](https://iceberg.apache.org/spec/)
*   [Docs](https://iceberg.apache.org/docs/latest)
*   [Blog](https://iceberg.apache.org/blog/)
*   [Talks](https://iceberg.apache.org/talks/)

#### Community

*   [Support](https://iceberg.apache.org/community/#slack)
*   [Mailing Lists](https://iceberg.apache.org/community/#mailing-lists)
*   [Iceberg Events](https://iceberg.apache.org/community/#connect-with-community-events)
*   [Issues](https://iceberg.apache.org/community/#issues)
*   [Contribute](https://iceberg.apache.org/contribute)
*   [Guidelines](https://iceberg.apache.org/community/#community-guidelines)

#### ASF

*   [Apache Software Foundation](https://www.apache.org/)
*   [Thanks](https://www.apache.org/foundation/thanks.html)
*   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
*   [Security](https://www.apache.org/security/)
*   [License](https://www.apache.org/licenses/)

[![Image 3: apache software foundation logo](https://iceberg.apache.org/assets/images/asf-estd-1999-logo.png)](https://iceberg.apache.org/)

[](https://iceberg.apache.org/community/ "iceberg.apache.org")[](https://github.com/apache/iceberg "github.com")[](https://www.youtube.com/@ApacheIceberg "www.youtube.com")[](https://join.slack.com/t/apache-iceberg/shared_invite/zt-3kclosz6r-3heAW3d~_PHefmN2A_~cAg "join.slack.com")

Apache Iceberg, Iceberg, Apache, the Apache feather logo, and the Apache Iceberg project logo are either registered trademarks or trademarks of The Apache Software Foundation. Copyright © 2025 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/).
