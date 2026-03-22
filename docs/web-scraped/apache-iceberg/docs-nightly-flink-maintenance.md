# Source: https://iceberg.apache.org/docs/nightly/flink-maintenance/

Title: Flink TableMaintenance - Apache Iceberg™

URL Source: https://iceberg.apache.org/docs/nightly/flink-maintenance/

Markdown Content:
Flink TableMaintenance - Apache Iceberg™
===============
- [x] - [x] 

[Skip to content](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-batchmode)

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
                    *   - [x]  Flink TableMaintenance  [Flink TableMaintenance](https://iceberg.apache.org/docs/nightly/flink-maintenance/) Table of contents  
                        *   [Flink Table Maintenance BatchMode](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-batchmode)
                            *   [Rewrite files action](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewrite-files-action)

                        *   [Flink Table Maintenance StreamingMode](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-streamingmode)
                            *   [Overview](https://iceberg.apache.org/docs/nightly/flink-maintenance/#overview)
                            *   [Supported Features (Flink)](https://iceberg.apache.org/docs/nightly/flink-maintenance/#supported-features-flink)
                                *   [ExpireSnapshots](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expiresnapshots)
                                *   [RewriteDataFiles](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewritedatafiles)
                                *   [DeleteOrphanFiles](https://iceberg.apache.org/docs/nightly/flink-maintenance/#deleteorphanfiles)

                            *   [Lock Management](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-management)
                                *   [Why Locks Are Needed](https://iceberg.apache.org/docs/nightly/flink-maintenance/#why-locks-are-needed)
                                *   [Supported Lock Types](https://iceberg.apache.org/docs/nightly/flink-maintenance/#supported-lock-types)
                                    *   [JDBC Lock Factory](https://iceberg.apache.org/docs/nightly/flink-maintenance/#jdbc-lock-factory)
                                    *   [ZooKeeper Lock Factory](https://iceberg.apache.org/docs/nightly/flink-maintenance/#zookeeper-lock-factory)

                                *   [Flink-maintained lock](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-maintained-lock)

                            *   [Quick Start](https://iceberg.apache.org/docs/nightly/flink-maintenance/#quick-start)
                            *   [Configuration Options](https://iceberg.apache.org/docs/nightly/flink-maintenance/#configuration-options)
                                *   [TableMaintenance Builder](https://iceberg.apache.org/docs/nightly/flink-maintenance/#tablemaintenance-builder)
                                *   [Maintenance Task Common Options](https://iceberg.apache.org/docs/nightly/flink-maintenance/#maintenance-task-common-options)
                                *   [ExpireSnapshots Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expiresnapshots-configuration)
                                *   [RewriteDataFiles Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewritedatafiles-configuration)
                                *   [DeleteOrphanFiles Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#deleteorphanfiles-configuration)

                            *   [Complete Example](https://iceberg.apache.org/docs/nightly/flink-maintenance/#complete-example)
                            *   [IcebergSink with Post-Commit Integration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#icebergsink-with-post-commit-integration)
                                *   [DataStream API](https://iceberg.apache.org/docs/nightly/flink-maintenance/#datastream-api)
                                    *   [Builder](https://iceberg.apache.org/docs/nightly/flink-maintenance/#builder)
                                    *   [Config](https://iceberg.apache.org/docs/nightly/flink-maintenance/#config)

                                *   [SQL Examples](https://iceberg.apache.org/docs/nightly/flink-maintenance/#sql-examples)

                            *   [IcebergSink Maintenance Configuration (SQL)](https://iceberg.apache.org/docs/nightly/flink-maintenance/#icebergsink-maintenance-configuration-sql)
                                *   [Enable Flags](https://iceberg.apache.org/docs/nightly/flink-maintenance/#enable-flags)
                                *   [Rewrite Data Files Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewrite-data-files-configuration)
                                *   [Expire Snapshots Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expire-snapshots-configuration)
                                *   [Delete Orphan Files Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#delete-orphan-files-configuration)

                            *   [Lock Configuration (SQL)](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-configuration-sql)
                            *   [Best Practices](https://iceberg.apache.org/docs/nightly/flink-maintenance/#best-practices)
                                *   [Resource Management](https://iceberg.apache.org/docs/nightly/flink-maintenance/#resource-management)
                                *   [Scheduling Strategy](https://iceberg.apache.org/docs/nightly/flink-maintenance/#scheduling-strategy)
                                *   [Performance Tuning](https://iceberg.apache.org/docs/nightly/flink-maintenance/#performance-tuning)

                            *   [Troubleshooting](https://iceberg.apache.org/docs/nightly/flink-maintenance/#troubleshooting)
                                *   [OutOfMemoryError during file deletion](https://iceberg.apache.org/docs/nightly/flink-maintenance/#outofmemoryerror-during-file-deletion)
                                *   [Lock conflicts](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-conflicts)
                                *   [Slow rewrite operations](https://iceberg.apache.org/docs/nightly/flink-maintenance/#slow-rewrite-operations)

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
                *   [Java Custom Catalog](https://iceberg.apache.org/docs/nightly/custom-catalog/)
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
*   [Flink Table Maintenance BatchMode](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-batchmode)
    *   [Rewrite files action](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewrite-files-action)

*   [Flink Table Maintenance StreamingMode](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-streamingmode)
    *   [Overview](https://iceberg.apache.org/docs/nightly/flink-maintenance/#overview)
    *   [Supported Features (Flink)](https://iceberg.apache.org/docs/nightly/flink-maintenance/#supported-features-flink)
        *   [ExpireSnapshots](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expiresnapshots)
        *   [RewriteDataFiles](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewritedatafiles)
        *   [DeleteOrphanFiles](https://iceberg.apache.org/docs/nightly/flink-maintenance/#deleteorphanfiles)

    *   [Lock Management](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-management)
        *   [Why Locks Are Needed](https://iceberg.apache.org/docs/nightly/flink-maintenance/#why-locks-are-needed)
        *   [Supported Lock Types](https://iceberg.apache.org/docs/nightly/flink-maintenance/#supported-lock-types)
            *   [JDBC Lock Factory](https://iceberg.apache.org/docs/nightly/flink-maintenance/#jdbc-lock-factory)
            *   [ZooKeeper Lock Factory](https://iceberg.apache.org/docs/nightly/flink-maintenance/#zookeeper-lock-factory)

        *   [Flink-maintained lock](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-maintained-lock)

    *   [Quick Start](https://iceberg.apache.org/docs/nightly/flink-maintenance/#quick-start)
    *   [Configuration Options](https://iceberg.apache.org/docs/nightly/flink-maintenance/#configuration-options)
        *   [TableMaintenance Builder](https://iceberg.apache.org/docs/nightly/flink-maintenance/#tablemaintenance-builder)
        *   [Maintenance Task Common Options](https://iceberg.apache.org/docs/nightly/flink-maintenance/#maintenance-task-common-options)
        *   [ExpireSnapshots Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expiresnapshots-configuration)
        *   [RewriteDataFiles Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewritedatafiles-configuration)
        *   [DeleteOrphanFiles Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#deleteorphanfiles-configuration)

    *   [Complete Example](https://iceberg.apache.org/docs/nightly/flink-maintenance/#complete-example)
    *   [IcebergSink with Post-Commit Integration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#icebergsink-with-post-commit-integration)
        *   [DataStream API](https://iceberg.apache.org/docs/nightly/flink-maintenance/#datastream-api)
            *   [Builder](https://iceberg.apache.org/docs/nightly/flink-maintenance/#builder)
            *   [Config](https://iceberg.apache.org/docs/nightly/flink-maintenance/#config)

        *   [SQL Examples](https://iceberg.apache.org/docs/nightly/flink-maintenance/#sql-examples)

    *   [IcebergSink Maintenance Configuration (SQL)](https://iceberg.apache.org/docs/nightly/flink-maintenance/#icebergsink-maintenance-configuration-sql)
        *   [Enable Flags](https://iceberg.apache.org/docs/nightly/flink-maintenance/#enable-flags)
        *   [Rewrite Data Files Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewrite-data-files-configuration)
        *   [Expire Snapshots Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expire-snapshots-configuration)
        *   [Delete Orphan Files Configuration](https://iceberg.apache.org/docs/nightly/flink-maintenance/#delete-orphan-files-configuration)

    *   [Lock Configuration (SQL)](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-configuration-sql)
    *   [Best Practices](https://iceberg.apache.org/docs/nightly/flink-maintenance/#best-practices)
        *   [Resource Management](https://iceberg.apache.org/docs/nightly/flink-maintenance/#resource-management)
        *   [Scheduling Strategy](https://iceberg.apache.org/docs/nightly/flink-maintenance/#scheduling-strategy)
        *   [Performance Tuning](https://iceberg.apache.org/docs/nightly/flink-maintenance/#performance-tuning)

    *   [Troubleshooting](https://iceberg.apache.org/docs/nightly/flink-maintenance/#troubleshooting)
        *   [OutOfMemoryError during file deletion](https://iceberg.apache.org/docs/nightly/flink-maintenance/#outofmemoryerror-during-file-deletion)
        *   [Lock conflicts](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-conflicts)
        *   [Slow rewrite operations](https://iceberg.apache.org/docs/nightly/flink-maintenance/#slow-rewrite-operations)

1.   [Home](https://iceberg.apache.org/)
2.   [Docs](https://iceberg.apache.org/docs/nightly/)
3.   [Java](https://iceberg.apache.org/docs/nightly/)
4.   [Nightly](https://iceberg.apache.org/docs/nightly/)
5.   [Integrations](https://iceberg.apache.org/docs/nightly/spark-getting-started/)
6.   [Apache Flink](https://iceberg.apache.org/docs/nightly/flink/)

Flink TableMaintenance
======================

Flink Table Maintenance BatchMode[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-batchmode "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------

### Rewrite files action[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewrite-files-action "Permanent link")

Iceberg provides API to rewrite small files into large files by submitting Flink batch jobs. The behavior of this Flink action is the same as Spark's [rewriteDataFiles](https://iceberg.apache.org/docs/nightly/maintenance/#compact-data-files).

```
import org.apache.iceberg.flink.actions.Actions;

TableLoader tableLoader = TableLoader.fromCatalog(
    CatalogLoader.hive("my_catalog", configuration, properties),
    TableIdentifier.of("database", "table")
);

Table table = tableLoader.loadTable();
RewriteDataFilesActionResult result = Actions.forTable(table)
        .rewriteDataFiles()
        .execute();
```

For more details of the rewrite files action, please refer to [RewriteDataFilesAction](https://iceberg.apache.org/javadoc/1.10.1/org/apache/iceberg/flink/actions/RewriteDataFilesAction.html)

Flink Table Maintenance StreamingMode[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-table-maintenance-streamingmode "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------

### Overview[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#overview "Permanent link")

In **Apache Iceberg** deployments within **Flink streaming environments**, implementing automated table maintenance operations—including `snapshot expiration`, `small file compaction`, and `orphan file cleanup`—is critical for optimal query performance and storage efficiency.

Traditionally, these maintenance operations were exclusively accessible through **Iceberg Spark Actions**, necessitating the deployment and management of dedicated Spark clusters. This dependency on **Spark infrastructure** solely for table optimization introduces significant **architectural complexity** and **operational overhead**.

The `TableMaintenance` API in **Apache Iceberg** empowers **Flink jobs** to execute maintenance tasks **natively**, either embedded within existing streaming pipelines or deployed as standalone Flink jobs. This eliminates dependencies on external systems, thereby **streamlining architecture**, **reducing operational costs**, and **enhancing automation capabilities**.

### Supported Features (Flink)[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#supported-features-flink "Permanent link")

#### ExpireSnapshots[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expiresnapshots "Permanent link")

Removes old snapshots and their files. Internally uses `cleanExpiredFiles(true)` when committing, so expired metadata/files are cleaned up automatically.

```
.add(ExpireSnapshots.builder()
    .maxSnapshotAge(Duration.ofDays(7))
    .retainLast(10)
    .deleteBatchSize(1000))
```

#### RewriteDataFiles[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewritedatafiles "Permanent link")

Compacts small files to optimize file sizes. Supports partial progress commits and limiting maximum rewritten bytes per run.

```
.add(RewriteDataFiles.builder()
    .targetFileSizeBytes(256 * 1024 * 1024)
    .minFileSizeBytes(32 * 1024 * 1024)
    .partialProgressEnabled(true)
    .partialProgressMaxCommits(5))
```

#### DeleteOrphanFiles[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#deleteorphanfiles "Permanent link")

Used to remove files which are not referenced in any metadata files of an Iceberg table and can thus be considered "orphaned".The table location is checked for such files.

```
.add(DeleteOrphanFiles.builder()
    .minAge(Duration.ofDays(3))
    .deleteBatchSize(1000))
```

### Lock Management[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-management "Permanent link")

The `TriggerLockFactory` is essential for coordinating maintenance tasks. It prevents concurrent maintenance operations on the same table, which could lead to conflicts or data corruption. This locking mechanism is necessary even for a single job, as multiple instances of the same task could otherwise conflict.

#### Why Locks Are Needed[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#why-locks-are-needed "Permanent link")

*   **Concurrent Access**: Multiple Flink jobs may attempt maintenance simultaneously
*   **Data Consistency**: Ensures only one maintenance operation runs per table at a time
*   **Resource Management**: Prevents resource conflicts and scheduling issues
*   **Avoid Duplicate Work**: Even when only a single compaction job is scheduled, multiple instances could attempt the same operation, leading to redundant work and wasted resources.

#### Supported Lock Types[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#supported-lock-types "Permanent link")

##### JDBC Lock Factory[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#jdbc-lock-factory "Permanent link")

Uses a database table to manage distributed locks:

```
Map<String, String> jdbcProps = new HashMap<>();
jdbcProps.put("jdbc.user", "flink");
jdbcProps.put("jdbc.password", "flinkpw");
jdbcProps.put("flink-maintenance.lock.jdbc.init-lock-tables", "true"); // Auto-create lock table if it doesn't exist

TriggerLockFactory lockFactory = new JdbcLockFactory(
    "jdbc:postgresql://localhost:5432/iceberg", // JDBC URL
    "catalog.db.table",                         // Lock ID (unique identifier)
    jdbcProps                                   // JDBC connection properties
);
```

##### ZooKeeper Lock Factory[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#zookeeper-lock-factory "Permanent link")

Uses Apache ZooKeeper for distributed locks:

```
TriggerLockFactory lockFactory = new ZkLockFactory(
    "localhost:2181",       // ZooKeeper connection string
    "catalog.db.table",     // Lock ID (unique identifier)
    60000,                  // sessionTimeoutMs
    15000,                  // connectionTimeoutMs
    3000,                   // baseSleepTimeMs
    3                       // maxRetries
);
```

#### Flink-maintained lock[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#flink-maintained-lock "Permanent link")

Maintain the lock within Flink itself. This does not require configuring external systems. The only prerequisite is that there are no parallel table maintenance jobs for a given table.

### Quick Start[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#quick-start "Permanent link")

The following example demonstrates the implementation of automated maintenance for an Iceberg table within a Flink environment.

```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

TableLoader tableLoader = TableLoader.fromCatalog(
    CatalogLoader.hive("my_catalog", configuration, properties),  
    TableIdentifier.of("database", "table")
);

Map<String, String> jdbcProps = new HashMap<>();
jdbcProps.put("jdbc.user", "flink");
jdbcProps.put("jdbc.password", "flinkpw");

// JdbcLockFactory Example
TriggerLockFactory lockFactory = new JdbcLockFactory(
    "jdbc:postgresql://localhost:5432/iceberg", // JDBC URL
    "catalog.db.table",                         // Lock ID (unique identifier)
    jdbcProps                                   // JDBC connection properties
);

// Option 1: With external lock factory (plan to deprecate this Option since 1.12)
TableMaintenance.forTable(env, tableLoader, lockFactory)
// Option 2: With Flink-managed lock (no external lock required)
TableMaintenance.forTable(env, tableLoader)
    .uidSuffix("my-maintenance-job")
    .rateLimit(Duration.ofMinutes(10))
    .lockCheckDelay(Duration.ofSeconds(10))
    .add(ExpireSnapshots.builder()
        .scheduleOnCommitCount(10)
        .maxSnapshotAge(Duration.ofMinutes(10))
        .retainLast(5)
        .deleteBatchSize(5)
        .parallelism(8))
    .add(RewriteDataFiles.builder()
        .scheduleOnDataFileCount(10)
        .targetFileSizeBytes(128 * 1024 * 1024)
        .partialProgressEnabled(true)
        .partialProgressMaxCommits(10))
    .append();

env.execute("Table Maintenance Job");
```

### Configuration Options[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#configuration-options "Permanent link")

#### TableMaintenance Builder[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#tablemaintenance-builder "Permanent link")

| Method | Description | Default |
| --- | --- | --- |
| `uidSuffix(String)` | Unique identifier suffix for the job | Random UUID |
| `rateLimit(Duration)` | Minimum interval between task executions | 60 seconds |
| `lockCheckDelay(Duration)` | Delay for checking lock availability | 30 seconds |
| `parallelism(int)` | Default parallelism for maintenance tasks | System default |
| `maxReadBack(int)` | Max snapshots to check during initialization | 100 |

#### Maintenance Task Common Options[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#maintenance-task-common-options "Permanent link")

| Method | Description | Default Value | Type |
| --- | --- | --- | --- |
| `scheduleOnCommitCount(int)` | Trigger after N commits | No automatic scheduling | int |
| `scheduleOnDataFileCount(int)` | Trigger after N data files | No automatic scheduling | int |
| `scheduleOnDataFileSize(long)` | Trigger after total data file size (bytes) | No automatic scheduling | long |
| `scheduleOnPosDeleteFileCount(int)` | Trigger after N positional delete files | No automatic scheduling | int |
| `scheduleOnPosDeleteRecordCount(long)` | Trigger after N positional delete records | No automatic scheduling | long |
| `scheduleOnEqDeleteFileCount(int)` | Trigger after N equality delete files | No automatic scheduling | int |
| `scheduleOnEqDeleteRecordCount(long)` | Trigger after N equality delete records | No automatic scheduling | long |
| `scheduleOnInterval(Duration)` | Trigger after time interval | No automatic scheduling | Duration |

#### ExpireSnapshots Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expiresnapshots-configuration "Permanent link")

| Method | Description | Default Value | Type |
| --- | --- | --- | --- |
| `maxSnapshotAge(Duration)` | Maximum age of snapshots to retain | 5 days | Duration |
| `retainLast(int)` | Minimum number of snapshots to retain | 1 | int |
| `deleteBatchSize(int)` | Number of files to delete in each batch | 1000 | int |
| `planningWorkerPoolSize(int)` | Number of worker threads for planning snapshot expiration | Shared worker pool | int |
| `cleanExpiredMetadata(boolean)` | Remove expired metadata files when expiring snapshots | true | boolean |

#### RewriteDataFiles Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewritedatafiles-configuration "Permanent link")

| Method | Description | Default Value | Type |
| --- | --- | --- | --- |
| `targetFileSizeBytes(long)` | Target size for rewritten files | Table property or 512MB | long |
| `minFileSizeBytes(long)` | Minimum size of files eligible for compaction | 75% of target file size | long |
| `maxFileSizeBytes(long)` | Maximum size of files eligible for compaction | 180% of target file size | long |
| `minInputFiles(int)` | Minimum number of files to trigger rewrite | 5 | int |
| `deleteFileThreshold(int)` | Minimum delete-file count per data file to force rewrite | Integer.MAX_VALUE | int |
| `rewriteAll(boolean)` | Rewrite all data files regardless of thresholds | false | boolean |
| `maxFileGroupSizeBytes(long)` | Maximum total size of a file group | 107374182400 (100GB) | long |
| `maxFilesToRewrite(int)` | If this option is not specified, all eligible files will be rewritten | null | int |
| `partialProgressEnabled(boolean)` | Enable partial progress commits | false | boolean |
| `partialProgressMaxCommits(int)` | Maximum commits allowed for partial progress when partialProgressEnabled is true | 10 | int |
| `maxRewriteBytes(long)` | Maximum bytes to rewrite per execution | Long.MAX_VALUE | long |
| `filter(Expression)` | Filter expression for selecting files to rewrite | Expressions.alwaysTrue() | Expression |
| `maxFileGroupInputFiles(long)` | Maximum allowed number of input files within a file group | Long.MAX_VALUE | long |

#### DeleteOrphanFiles Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#deleteorphanfiles-configuration "Permanent link")

| Method | Description | Default Value | Type |
| --- | --- | --- | --- |
| `location(string)` | The location to start the recursive listing of the candidate files for removal. | Table's location | String |
| `usePrefixListing(boolean)` | When true, use prefix-based file listing via the SupportsPrefixOperations interface. The Table FileIO implementation must support SupportsPrefixOperations when this flag is enabled.(Note: Setting it to False will use a recursive method to obtain file information. If the underlying storage is object storage, it will repeatedly call the API to get the path.) | True | boolean |
| `prefixMismatchMode(PrefixMismatchMode)` | Action behavior when location prefixes (schemes/authorities) mismatch: * ERROR - throw an exception. * IGNORE - no action. * DELETE - delete files. | ERROR | PrefixMismatchMode |
| `equalSchemes(Map<String, String>)` | Mapping of file system schemes to be considered equal. Key is a comma-separated list of schemes and value is a scheme | "s3n"=>"s3","s3a"=>"s3" | Map |
| `equalAuthorities(Map<String, String>)` | Mapping of file system authorities to be considered equal. Key is a comma-separated list of authorities and value is an authority. | Empty map | Map |
| `minAge(Duration)` | Remove orphan files created before this timestamp | 3 days ago | Duration |
| `planningWorkerPoolSize(int)` | Number of worker threads for planning snapshot expiration | Shared worker pool | int |

### Complete Example[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#complete-example "Permanent link")

```
public class TableMaintenanceJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.enableCheckpointing(60000); // Enable checkpointing

        // Configure table loader
        TableLoader tableLoader = TableLoader.fromCatalog(
            CatalogLoader.hive("my_catalog", configuration),
            TableIdentifier.of("database", "table")
        );

        // Set up JDBC lock factory
        Map<String, String> jdbcProps = new HashMap<>();
        jdbcProps.put("jdbc.user", "flink");
        jdbcProps.put("jdbc.password", "flinkpw");
        jdbcProps.put("flink-maintenance.lock.jdbc.init-lock-tables", "true");

        TriggerLockFactory lockFactory = new JdbcLockFactory(
            "jdbc:postgresql://localhost:5432/iceberg",
            "catalog.db.table",
            jdbcProps
        );

        // Set up maintenance with comprehensive configuration
        TableMaintenance.forTable(env, tableLoader, lockFactory)
            .uidSuffix("production-maintenance")
            .rateLimit(Duration.ofMinutes(15))
            .lockCheckDelay(Duration.ofSeconds(30))
            .parallelism(4)

            // Daily snapshot cleanup
            .add(ExpireSnapshots.builder()
                .maxSnapshotAge(Duration.ofDays(7))
                .retainLast(10))

            // Continuous file optimization
            .add(RewriteDataFiles.builder()
                .targetFileSizeBytes(256 * 1024 * 1024)
                .minFileSizeBytes(32 * 1024 * 1024)
                .scheduleOnDataFileCount(20)
                .partialProgressEnabled(true)
                .partialProgressMaxCommits(5)
                .maxRewriteBytes(2L * 1024 * 1024 * 1024)
                .parallelism(6))

            // Delete orphans files created more than five days ago
            .add(DeleteOrphanFiles.builder()
                        .minAge(Duration.ofDays(5)))  

            .append();

        env.execute("Iceberg Table Maintenance");
    }
}
```

### IcebergSink with Post-Commit Integration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#icebergsink-with-post-commit-integration "Permanent link")

Apache Iceberg Sink V2 for Flink allows automatic execution of maintenance tasks after data is committed to the table, using the addPostCommitTopology(...) method.

#### DataStream API[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#datastream-api "Permanent link")

##### Builder[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#builder "Permanent link")

```
IcebergSink.forRowData(dataStream)
    .table(table)
    .tableLoader(tableLoader)
    .rewriteDataFiles(Map.of(
        RewriteDataFilesConfig.MAX_BYTES, "1073741824"))
    .expireSnapshots(Map.of(
        ExpireSnapshotsConfig.RETAIN_LAST, "5",
        ExpireSnapshotsConfig.MAX_SNAPSHOT_AGE_SECONDS, "604800"))
    .deleteOrphanFiles(Map.of(
        DeleteOrphanFilesConfig.MIN_AGE_SECONDS, "259200"))
    .append();
```

##### Config[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#config "Permanent link")

All maintenance tasks are configured through string properties:

```
Map<String, String> flinkConf = new HashMap<>();

// Enable maintenance tasks
flinkConf.put("flink-maintenance.rewrite.enabled", "true");
flinkConf.put("flink-maintenance.expire-snapshots.enabled", "true");
flinkConf.put("flink-maintenance.delete-orphan-files.enabled", "true");

// Configure rewrite data files
flinkConf.put("flink-maintenance.rewrite.max-bytes", "1073741824");

// Configure expire snapshots
flinkConf.put("flink-maintenance.expire-snapshots.retain-last", "5");
flinkConf.put("flink-maintenance.expire-snapshots.max-snapshot-age-seconds", "604800");

// Configure delete orphan files
flinkConf.put("flink-maintenance.delete-orphan-files.min-age-seconds", "259200");

// Configure JDBC lock settings (deprecated, lock configuration is no longer required for a single Flink job)
flinkConf.put("flink-maintenance.lock.type", "jdbc");
flinkConf.put("flink-maintenance.lock.jdbc.uri", "jdbc:postgresql://localhost:5432/iceberg");
flinkConf.put("flink-maintenance.lock.lock-id", "catalog.db.table");

IcebergSink.forRowData(dataStream)
    .table(table)
    .tableLoader(tableLoader)
    .setAll(flinkConf)
    .append();
```

#### SQL Examples[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#sql-examples "Permanent link")

You can enable maintenance and configure locks using SQL before executing writes:

```
-- Enable Iceberg V2 Sink and maintenance tasks
SET 'table.exec.iceberg.use.v2.sink' = 'true';
SET 'flink-maintenance.rewrite.enabled' = 'true';
SET 'flink-maintenance.expire-snapshots.enabled' = 'true';
SET 'flink-maintenance.delete-orphan-files.enabled' = 'true';

-- Configure rewrite data files
SET 'flink-maintenance.rewrite.max-bytes' = '1073741824';

-- Configure expire snapshots
SET 'flink-maintenance.expire-snapshots.retain-last' = '5';

-- Configure delete orphan files
SET 'flink-maintenance.delete-orphan-files.min-age-seconds' = '259200';

-- Configure maintenance lock (JDBC)
SET 'flink-maintenance.lock.type' = 'jdbc';
SET 'flink-maintenance.lock.lock-id' = 'catalog.db.table';
SET 'flink-maintenance.lock.jdbc.uri' = 'jdbc:postgresql://localhost:5432/iceberg';
SET 'flink-maintenance.lock.jdbc.init-lock-tables' = 'true';

-- Now run writes; maintenance will be scheduled post-commit
INSERT INTO db.tbl SELECT ...;
```

Or specify options in table DDL:

```
CREATE TABLE db.tbl (
  ...
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = 'my_catalog',
  'catalog-database' = 'db',
  'catalog-table' = 'tbl',
  'flink-maintenance.rewrite.enabled' = 'true',
  'flink-maintenance.expire-snapshots.enabled' = 'true',
  'flink-maintenance.delete-orphan-files.enabled' = 'true',

  'flink-maintenance.rewrite.max-bytes' = '1073741824',
  'flink-maintenance.expire-snapshots.retain-last' = '5',
  'flink-maintenance.delete-orphan-files.min-age-seconds' = '259200',

  'flink-maintenance.lock.type' = 'jdbc',
  'flink-maintenance.lock.lock-id' = 'catalog.db.table',
  'flink-maintenance.lock.jdbc.uri' = 'jdbc:postgresql://localhost:5432/iceberg',
  'flink-maintenance.lock.jdbc.init-lock-tables' = 'true'
);
```

### IcebergSink Maintenance Configuration (SQL)[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#icebergsink-maintenance-configuration-sql "Permanent link")

These keys are used in SQL (SET or table WITH options) or via `IcebergSink.Builder.set()` / `setAll()`.

#### Enable Flags[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#enable-flags "Permanent link")

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.rewrite.enabled` | Enable compaction (rewrite data files) | `false` |
| `flink-maintenance.expire-snapshots.enabled` | Enable expire snapshots | `false` |
| `flink-maintenance.delete-orphan-files.enabled` | Enable delete orphan files | `false` |

#### Rewrite Data Files Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#rewrite-data-files-configuration "Permanent link")

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.rewrite.schedule.commit-count` | Trigger after N commits | `10` |
| `flink-maintenance.rewrite.schedule.data-file-count` | Trigger after N data files | `1000` |
| `flink-maintenance.rewrite.schedule.data-file-size` | Trigger after total data file size (bytes) | `107374182400` (100GB) |
| `flink-maintenance.rewrite.schedule.interval-second` | Trigger after time interval (seconds) | `600` |
| `flink-maintenance.rewrite.max-bytes` | Maximum bytes to rewrite per execution | `Long.MAX_VALUE` |
| `flink-maintenance.rewrite.partial-progress.enabled` | Enable partial progress commits | `false` |
| `flink-maintenance.rewrite.partial-progress.max-commits` | Maximum commits for partial progress | `10` |

#### Expire Snapshots Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#expire-snapshots-configuration "Permanent link")

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.expire-snapshots.schedule.commit-count` | Trigger after N commits | `10` |
| `flink-maintenance.expire-snapshots.schedule.interval-second` | Trigger after time interval (seconds) | `3600` (1 hour) |
| `flink-maintenance.expire-snapshots.max-snapshot-age-seconds` | Maximum age of snapshots to retain (seconds) | Not set |
| `flink-maintenance.expire-snapshots.retain-last` | Minimum number of snapshots to retain | Not set |
| `flink-maintenance.expire-snapshots.delete-batch-size` | Batch size for deleting expired files | `1000` |
| `flink-maintenance.expire-snapshots.clean-expired-metadata` | Remove expired metadata (partition specs, schemas) | `true` |
| `flink-maintenance.expire-snapshots.planning-worker-pool-size` | Worker pool size for planning | Shared pool |

#### Delete Orphan Files Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#delete-orphan-files-configuration "Permanent link")

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.delete-orphan-files.schedule.interval-second` | Trigger after time interval (seconds) | `3600` (1 hour) |
| `flink-maintenance.delete-orphan-files.min-age-seconds` | Minimum age of files to consider for deletion (seconds) | `259200` (3 days) |
| `flink-maintenance.delete-orphan-files.delete-batch-size` | Batch size for deleting orphan files | `1000` |
| `flink-maintenance.delete-orphan-files.location` | Location to start recursive listing | Table location |
| `flink-maintenance.delete-orphan-files.use-prefix-listing` | Use prefix listing for file discovery | `true` |
| `flink-maintenance.delete-orphan-files.planning-worker-pool-size` | Worker pool size for planning | Shared pool |
| `flink-maintenance.delete-orphan-files.equal-schemes` | Equivalent schemes (format: `s3n=s3,s3a=s3`) | `s3n=s3,s3a=s3` |
| `flink-maintenance.delete-orphan-files.equal-authorities` | Equivalent authorities (format: `auth1=auth2`) | Not set |
| `flink-maintenance.delete-orphan-files.prefix-mismatch-mode` | Behavior on prefix mismatch: `ERROR`, `IGNORE`, `DELETE` | `ERROR` |

### Lock Configuration (SQL)[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-configuration-sql "Permanent link")

These keys are used in SQL (SET or table WITH options) and are applicable when writing with maintenance enabled.

*   JDBC

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.lock.type` | Set to `jdbc` |  |
| `flink-maintenance.lock.lock-id` | Unique lock ID per table |  |
| `flink-maintenance.lock.jdbc.uri` | JDBC URI |  |
| `flink-maintenance.lock.jdbc.init-lock-tables` | Auto-create lock table | `false` |

*   ZooKeeper

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.lock.type` | Set to `zookeeper` |  |
| `flink-maintenance.lock.lock-id` | Unique lock ID per table |  |
| `flink-maintenance.lock.zookeeper.uri` | ZK connection URI |  |
| `flink-maintenance.lock.zookeeper.session-timeout-ms` | Session timeout (ms) | `60000` |
| `flink-maintenance.lock.zookeeper.connection-timeout-ms` | Connection timeout (ms) | `15000` |
| `flink-maintenance.lock.zookeeper.max-retries` | Max retries | `3` |
| `flink-maintenance.lock.zookeeper.base-sleep-ms` | Base sleep between retries (ms) | `3000` |
| `flink-maintenance.lock.zookeeper.max-sleep-ms` | Maximum sleep time (ms) between retries. Caps the exponential backoff delay. | `10000` |
| `flink-maintenance.lock.zookeeper.retry-policy` | Retry policy name for ZooKeeper client. Supported values include: ONE_TIME, N_TIME, BOUNDED_EXPONENTIAL_BACKOFF, UNTIL_ELAPSED, EXPONENTIAL_BACKOFF. | `EXPONENTIAL_BACKOFF` |

*   COORDINATOR LOCK

| Key | Description | Default |
| --- | --- | --- |
| `flink-maintenance.lock.type` | Set to `` or not set |  |

### Best Practices[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#best-practices "Permanent link")

#### Resource Management[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#resource-management "Permanent link")

*   Use dedicated slot sharing groups for maintenance tasks
*   Set appropriate parallelism based on cluster resources
*   Enable checkpointing for fault tolerance

#### Scheduling Strategy[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#scheduling-strategy "Permanent link")

*   Avoid too frequent executions with `rateLimit`
*   Use `scheduleOnCommitCount` for write-heavy tables
*   Use `scheduleOnDataFileCount` for fine-grained control

#### Performance Tuning[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#performance-tuning "Permanent link")

*   Adjust `deleteBatchSize` based on storage performance
*   Enable `partialProgressEnabled` for large rewrite operations
*   Set reasonable `maxRewriteBytes` limits
*   Setting an appropriate `maxFileGroupSizeBytes` can break down large FileGroups into smaller ones, thereby increasing the speed of parallel processing

### Troubleshooting[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#troubleshooting "Permanent link")

#### OutOfMemoryError during file deletion[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#outofmemoryerror-during-file-deletion "Permanent link")

**Scenario:** This can occur when the maintenance task attempts to delete a very large number of files in a single batch, especially in tables with long retention histories or after bulk deletions. **Cause:** Each file deletion involves metadata and object store operations, which together can consume significant memory. Large batches magnify this effect and may exhaust the JVM heap. **Recommendation:** Reduce the batch size to limit memory usage during deletion.

```
.deleteBatchSize(500) // Example: 500 files per batch
```

#### Lock conflicts[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#lock-conflicts "Permanent link")

**Scenario:** In multi-job or high-availability environments, two or more Flink jobs may attempt maintenance on the same table simultaneously. **Cause:** Concurrent jobs compete for the same distributed lock, causing retries and possible delays. **Recommendation:** Increase lock check delay and rate limit so that failed attempts back off and reduce contention.

```
.lockCheckDelay(Duration.ofMinutes(1)) // Wait longer before re-checking lock
.rateLimit(Duration.ofMinutes(10))     // Reduce frequency of task execution
```

#### Slow rewrite operations[🔗](https://iceberg.apache.org/docs/nightly/flink-maintenance/#slow-rewrite-operations "Permanent link")

**Scenario:** Large tables with many small files can require rewriting terabytes of data in a single run, which may overwhelm available resources. **Cause:** Without limits, rewrite tasks attempt to process all eligible files at once, leading to long execution times and possible job failures. **Recommendation:** Enable partial progress so that rewritten files can be committed in smaller batches, and cap the maximum data rewritten in each execution.

```
.partialProgressEnabled(true) // Commit progress incrementally
.partialProgressMaxCommits(3) // Allow up to 3 commits per run
.maxRewriteBytes(1L * 1024 * 1024 * 1024) // Limit to ~1GB per run
```

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
