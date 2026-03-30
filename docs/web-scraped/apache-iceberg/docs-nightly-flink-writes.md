# Source: https://iceberg.apache.org/docs/nightly/flink-writes/

Title: Flink Writes - Apache Iceberg™

URL Source: https://iceberg.apache.org/docs/nightly/flink-writes/

Markdown Content:
Flink Writes - Apache Iceberg™
===============
- [x] - [x] 

[Skip to content](https://iceberg.apache.org/docs/nightly/flink-writes/#flink-writes)

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
                    *   - [x]  Flink Writes  [Flink Writes](https://iceberg.apache.org/docs/nightly/flink-writes/) Table of contents  
                        *   [Writing with SQL](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-sql)
                            *   [INSERT INTO](https://iceberg.apache.org/docs/nightly/flink-writes/#insert-into)
                            *   [INSERT OVERWRITE](https://iceberg.apache.org/docs/nightly/flink-writes/#insert-overwrite)
                            *   [UPSERT](https://iceberg.apache.org/docs/nightly/flink-writes/#upsert)

                        *   [Writing with DataStream](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-datastream)
                            *   [Appending data](https://iceberg.apache.org/docs/nightly/flink-writes/#appending-data)
                            *   [Overwrite data](https://iceberg.apache.org/docs/nightly/flink-writes/#overwrite-data)
                            *   [Upsert data](https://iceberg.apache.org/docs/nightly/flink-writes/#upsert-data)
                            *   [Write with Avro GenericRecord](https://iceberg.apache.org/docs/nightly/flink-writes/#write-with-avro-genericrecord)
                            *   [Branch Writes](https://iceberg.apache.org/docs/nightly/flink-writes/#branch-writes)
                            *   [Metrics](https://iceberg.apache.org/docs/nightly/flink-writes/#metrics)

                        *   [Options](https://iceberg.apache.org/docs/nightly/flink-writes/#options)
                            *   [Write options](https://iceberg.apache.org/docs/nightly/flink-writes/#write-options)

                        *   [Distribution mode](https://iceberg.apache.org/docs/nightly/flink-writes/#distribution-mode)
                            *   [Hash distribution](https://iceberg.apache.org/docs/nightly/flink-writes/#hash-distribution)
                            *   [Range distribution (experimental)](https://iceberg.apache.org/docs/nightly/flink-writes/#range-distribution-experimental)
                                *   [Use cases](https://iceberg.apache.org/docs/nightly/flink-writes/#use-cases)
                                *   [Traffic statistics](https://iceberg.apache.org/docs/nightly/flink-writes/#traffic-statistics)
                                *   [Usage](https://iceberg.apache.org/docs/nightly/flink-writes/#usage)

                            *   [Overhead](https://iceberg.apache.org/docs/nightly/flink-writes/#overhead)

                        *   [Notes](https://iceberg.apache.org/docs/nightly/flink-writes/#notes)
                        *   [Sink V2 based implementation](https://iceberg.apache.org/docs/nightly/flink-writes/#sink-v2-based-implementation)
                            *   [Writing with SQL](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-sql_1)
                            *   [Writing with DataStream](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-datastream_1)

                        *   [Flink Dynamic Iceberg Sink](https://iceberg.apache.org/docs/nightly/flink-writes/#flink-dynamic-iceberg-sink)
                            *   [Configuration Example](https://iceberg.apache.org/docs/nightly/flink-writes/#configuration-example)
                            *   [Dynamic Routing Configuration](https://iceberg.apache.org/docs/nightly/flink-writes/#dynamic-routing-configuration)
                            *   [Schema Evolution](https://iceberg.apache.org/docs/nightly/flink-writes/#schema-evolution)
                                *   [Supported schema updates](https://iceberg.apache.org/docs/nightly/flink-writes/#supported-schema-updates)
                                    *   [Unsupported schema updates](https://iceberg.apache.org/docs/nightly/flink-writes/#unsupported-schema-updates)

                            *   [Caching](https://iceberg.apache.org/docs/nightly/flink-writes/#caching)
                            *   [Dynamic Sink Configuration](https://iceberg.apache.org/docs/nightly/flink-writes/#dynamic-sink-configuration)
                            *   [Notes](https://iceberg.apache.org/docs/nightly/flink-writes/#notes_1)

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
*   [Writing with SQL](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-sql)
    *   [INSERT INTO](https://iceberg.apache.org/docs/nightly/flink-writes/#insert-into)
    *   [INSERT OVERWRITE](https://iceberg.apache.org/docs/nightly/flink-writes/#insert-overwrite)
    *   [UPSERT](https://iceberg.apache.org/docs/nightly/flink-writes/#upsert)

*   [Writing with DataStream](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-datastream)
    *   [Appending data](https://iceberg.apache.org/docs/nightly/flink-writes/#appending-data)
    *   [Overwrite data](https://iceberg.apache.org/docs/nightly/flink-writes/#overwrite-data)
    *   [Upsert data](https://iceberg.apache.org/docs/nightly/flink-writes/#upsert-data)
    *   [Write with Avro GenericRecord](https://iceberg.apache.org/docs/nightly/flink-writes/#write-with-avro-genericrecord)
    *   [Branch Writes](https://iceberg.apache.org/docs/nightly/flink-writes/#branch-writes)
    *   [Metrics](https://iceberg.apache.org/docs/nightly/flink-writes/#metrics)

*   [Options](https://iceberg.apache.org/docs/nightly/flink-writes/#options)
    *   [Write options](https://iceberg.apache.org/docs/nightly/flink-writes/#write-options)

*   [Distribution mode](https://iceberg.apache.org/docs/nightly/flink-writes/#distribution-mode)
    *   [Hash distribution](https://iceberg.apache.org/docs/nightly/flink-writes/#hash-distribution)
    *   [Range distribution (experimental)](https://iceberg.apache.org/docs/nightly/flink-writes/#range-distribution-experimental)
        *   [Use cases](https://iceberg.apache.org/docs/nightly/flink-writes/#use-cases)
        *   [Traffic statistics](https://iceberg.apache.org/docs/nightly/flink-writes/#traffic-statistics)
        *   [Usage](https://iceberg.apache.org/docs/nightly/flink-writes/#usage)

    *   [Overhead](https://iceberg.apache.org/docs/nightly/flink-writes/#overhead)

*   [Notes](https://iceberg.apache.org/docs/nightly/flink-writes/#notes)
*   [Sink V2 based implementation](https://iceberg.apache.org/docs/nightly/flink-writes/#sink-v2-based-implementation)
    *   [Writing with SQL](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-sql_1)
    *   [Writing with DataStream](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-datastream_1)

*   [Flink Dynamic Iceberg Sink](https://iceberg.apache.org/docs/nightly/flink-writes/#flink-dynamic-iceberg-sink)
    *   [Configuration Example](https://iceberg.apache.org/docs/nightly/flink-writes/#configuration-example)
    *   [Dynamic Routing Configuration](https://iceberg.apache.org/docs/nightly/flink-writes/#dynamic-routing-configuration)
    *   [Schema Evolution](https://iceberg.apache.org/docs/nightly/flink-writes/#schema-evolution)
        *   [Supported schema updates](https://iceberg.apache.org/docs/nightly/flink-writes/#supported-schema-updates)
            *   [Unsupported schema updates](https://iceberg.apache.org/docs/nightly/flink-writes/#unsupported-schema-updates)

    *   [Caching](https://iceberg.apache.org/docs/nightly/flink-writes/#caching)
    *   [Dynamic Sink Configuration](https://iceberg.apache.org/docs/nightly/flink-writes/#dynamic-sink-configuration)
    *   [Notes](https://iceberg.apache.org/docs/nightly/flink-writes/#notes_1)

1.   [Home](https://iceberg.apache.org/)
2.   [Docs](https://iceberg.apache.org/docs/nightly/)
3.   [Java](https://iceberg.apache.org/docs/nightly/)
4.   [Nightly](https://iceberg.apache.org/docs/nightly/)
5.   [Integrations](https://iceberg.apache.org/docs/nightly/spark-getting-started/)
6.   [Apache Flink](https://iceberg.apache.org/docs/nightly/flink/)

Flink Writes[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#flink-writes "Permanent link")
=====================================================================================================

Iceberg support batch and streaming writes with [Apache Flink](https://flink.apache.org/)'s DataStream API and Table API.

The Flink Iceberg sink guarantees exactly-once semantics.

Writing with SQL[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-sql "Permanent link")
-------------------------------------------------------------------------------------------------------------

Iceberg support both `INSERT INTO` and `INSERT OVERWRITE`.

### `INSERT INTO`[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#insert-into "Permanent link")

To append new data to a table with a Flink streaming job, use `INSERT INTO`:

```
INSERT INTO `hive_catalog`.`default`.`sample` VALUES (1, 'a');
INSERT INTO `hive_catalog`.`default`.`sample` SELECT id, data from other_kafka_table;
```

### `INSERT OVERWRITE`[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#insert-overwrite "Permanent link")

To replace data in the table with the result of a query, use `INSERT OVERWRITE` in batch job (flink streaming job does not support `INSERT OVERWRITE`). Overwrites are atomic operations for Iceberg tables.

Partitions that have rows produced by the SELECT query will be replaced, for example:

```
INSERT OVERWRITE sample VALUES (1, 'a');
```

Iceberg also support overwriting given partitions by the `select` values:

```
INSERT OVERWRITE `hive_catalog`.`default`.`sample` PARTITION(data='a') SELECT 6;
```

For a partitioned iceberg table, when all the partition columns are set a value in `PARTITION` clause, it is inserting into a static partition, otherwise if partial partition columns (prefix part of all partition columns) are set a value in `PARTITION` clause, it is writing the query result into a dynamic partition. For an unpartitioned iceberg table, its data will be completely overwritten by `INSERT OVERWRITE`.

### `UPSERT`[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#upsert "Permanent link")

Iceberg supports `UPSERT` based on the primary key when writing data into v2 table format. There are two ways to enable upsert.

1.   Enable the `UPSERT` mode as table-level property `write.upsert.enabled`. Here is an example SQL statement to set the table property when creating a table. It would be applied for all write paths to this table (batch or streaming) unless overwritten by write options as described later.

```
CREATE TABLE `hive_catalog`.`default`.`sample` (
    `id` INT COMMENT 'unique id',
    `data` STRING NOT NULL,
    PRIMARY KEY(`id`) NOT ENFORCED
) with ('format-version'='2', 'write.upsert.enabled'='true');
``` 
2.   Enabling `UPSERT` mode using `upsert-enabled` in the [write options](https://iceberg.apache.org/docs/nightly/flink-writes/#write-options) provides more flexibility than a table level config. Note that you still need to use v2 table format and specify the [primary key](https://iceberg.apache.org/docs/nightly/flink-ddl/#primary-key) or [identifier fields](https://iceberg.apache.org/spec/#identifier-field-ids) when creating the table.

```
INSERT INTO tableName /*+ OPTIONS('upsert-enabled'='true') */
...
``` 

Info

OVERWRITE and UPSERT modes are mutually exclusive and cannot be enabled at the same time. When using UPSERT mode with a partitioned table, source columns of corresponding partition fields must be included in the equality fields. For example, if the partition field is `days(ts)`, then `ts` must be part of the equality fields.

Writing with DataStream[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-datastream "Permanent link")
---------------------------------------------------------------------------------------------------------------------------

Iceberg support writing to iceberg table from different DataStream input.

### Appending data[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#appending-data "Permanent link")

Flink supports writing `DataStream<RowData>` and `DataStream<Row>` to the sink iceberg table natively.

```
StreamExecutionEnvironment env = ...;

DataStream<RowData> input = ... ;
Configuration hadoopConf = new Configuration();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path", hadoopConf);

FlinkSink.forRowData(input)
    .tableLoader(tableLoader)
    .append();

env.execute("Test Iceberg DataStream");
```

### Overwrite data[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#overwrite-data "Permanent link")

Set the `overwrite` flag in FlinkSink builder to overwrite the data in existing iceberg tables:

```
StreamExecutionEnvironment env = ...;

DataStream<RowData> input = ... ;
Configuration hadoopConf = new Configuration();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path", hadoopConf);

FlinkSink.forRowData(input)
    .tableLoader(tableLoader)
    .overwrite(true)
    .append();

env.execute("Test Iceberg DataStream");
```

### Upsert data[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#upsert-data "Permanent link")

Set the `upsert` flag in FlinkSink builder to upsert the data in existing iceberg table. The table must use v2 table format and have a primary key.

```
StreamExecutionEnvironment env = ...;

DataStream<RowData> input = ... ;
Configuration hadoopConf = new Configuration();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path", hadoopConf);

FlinkSink.forRowData(input)
    .tableLoader(tableLoader)
    .upsert(true)
    .append();

env.execute("Test Iceberg DataStream");
```

Info

OVERWRITE and UPSERT modes are mutually exclusive and cannot be enabled at the same time. When using UPSERT mode with a partitioned table, source columns of corresponding partition fields must be included in the equality fields. For example, if the partition field is `days(ts)`, then `ts` must be part of the equality fields.

### Write with Avro GenericRecord[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#write-with-avro-genericrecord "Permanent link")

Flink Iceberg sink provides `AvroGenericRecordToRowDataMapper` that converts Avro `GenericRecord` to Flink `RowData`. You can use the mapper to write Avro GenericRecord DataStream to Iceberg.

Please make sure `flink-avro` jar is included in the classpath. Also `iceberg-flink-runtime` shaded bundle jar can't be used because the runtime jar shades the avro package. Please use non-shaded `iceberg-flink` jar instead.

```
DataStream<org.apache.avro.generic.GenericRecord> dataStream = ...;

Schema icebergSchema = table.schema();

// The Avro schema converted from Iceberg schema can't be used
// due to precision difference between how Iceberg schema (micro)
// and Flink AvroToRowDataConverters (milli) deal with time type.
// Instead, use the Avro schema defined directly.
// See AvroGenericRecordToRowDataMapper Javadoc for more details.
org.apache.avro.Schema avroSchema = AvroSchemaUtil.convert(icebergSchema, table.name());

GenericRecordAvroTypeInfo avroTypeInfo = new GenericRecordAvroTypeInfo(avroSchema);
RowType rowType = FlinkSchemaUtil.convert(icebergSchema);

FlinkSink.builderFor(
    dataStream,
    AvroGenericRecordToRowDataMapper.forAvroSchema(avroSchema),
    FlinkCompatibilityUtil.toTypeInfo(rowType))
  .table(table)
  .tableLoader(tableLoader)
  .append();
```

### Branch Writes[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#branch-writes "Permanent link")

Writing to branches in Iceberg tables is also supported via the `toBranch` API in `FlinkSink` For more information on branches please refer to [branches](https://iceberg.apache.org/docs/nightly/branching/).

```
FlinkSink.forRowData(input)
    .tableLoader(tableLoader)
    .toBranch("audit-branch")
    .append();
```

### Metrics[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#metrics "Permanent link")

The following Flink metrics are provided by the Flink Iceberg sink.

Parallel writer metrics are added under the sub group of `IcebergStreamWriter`. They should have the following key-value tags.

*   table: full table name (like iceberg.my_db.my_table)
*   subtask_index: writer subtask index starting from 0

| Metric name | Metric type | Description |
| --- | --- | --- |
| lastFlushDurationMs | Gauge | The duration (in milli) that writer subtasks take to flush and upload the files during checkpoint. |
| flushedDataFiles | Counter | Number of data files flushed and uploaded. |
| flushedDeleteFiles | Counter | Number of delete files flushed and uploaded. |
| flushedReferencedDataFiles | Counter | Number of data files referenced by the flushed delete files. |
| dataFilesSizeHistogram | Histogram | Histogram distribution of data file sizes (in bytes). |
| deleteFilesSizeHistogram | Histogram | Histogram distribution of delete file sizes (in bytes). |

Committer metrics are added under the sub group of `IcebergFilesCommitter`. They should have the following key-value tags.

*   table: full table name (like iceberg.my_db.my_table)

| Metric name | Metric type | Description |
| --- | --- | --- |
| lastCheckpointDurationMs | Gauge | The duration (in milli) that the committer operator checkpoints its state. |
| lastCommitDurationMs | Gauge | The duration (in milli) that the Iceberg table commit takes. |
| committedDataFilesCount | Counter | Number of data files committed. |
| committedDataFilesRecordCount | Counter | Number of records contained in the committed data files. |
| committedDataFilesByteCount | Counter | Number of bytes contained in the committed data files. |
| committedDeleteFilesCount | Counter | Number of delete files committed. |
| committedDeleteFilesRecordCount | Counter | Number of records contained in the committed delete files. |
| committedDeleteFilesByteCount | Counter | Number of bytes contained in the committed delete files. |
| elapsedSecondsSinceLastSuccessfulCommit | Gauge | Elapsed time (in seconds) since last successful Iceberg commit. |

`elapsedSecondsSinceLastSuccessfulCommit` is an ideal alerting metric to detect failed or missing Iceberg commits.

*   Iceberg commit happened after successful Flink checkpoint in the `notifyCheckpointComplete` callback. It could happen that Iceberg commits failed (for whatever reason), while Flink checkpoints succeeding.
*   It could also happen that `notifyCheckpointComplete` wasn't triggered (for whatever bug). As a result, there won't be any Iceberg commits attempted.

If the checkpoint interval (and expected Iceberg commit interval) is 5 minutes, set up alert with rule like `elapsedSecondsSinceLastSuccessfulCommit > 60 minutes` to detect failed or missing Iceberg commits in the past hour.

Options[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#options "Permanent link")
-------------------------------------------------------------------------------------------

### Write options[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#write-options "Permanent link")

Flink write options are passed when configuring the FlinkSink, like this:

```
FlinkSink.Builder builder = FlinkSink.forRow(dataStream, SimpleDataUtil.FLINK_SCHEMA)
    .table(table)
    .tableLoader(tableLoader)
    .set("write-format", "orc")
    .set(FlinkWriteOptions.OVERWRITE_MODE, "true");
```

For Flink SQL, write options can be passed in via SQL hints like this:

```
INSERT INTO tableName /*+ OPTIONS('upsert-enabled'='true') */
...
```

Check out all the options here: [write-options](https://iceberg.apache.org/docs/nightly/flink-configuration/#write-options)

Distribution mode[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#distribution-mode "Permanent link")
---------------------------------------------------------------------------------------------------------------

Flink streaming writer supports both `HASH` and `RANGE` distribution mode. You can enable it via `FlinkSink#Builder#distributionMode(DistributionMode)` or via [write-options](https://iceberg.apache.org/docs/nightly/flink-configuration/#write-options).

### Hash distribution[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#hash-distribution "Permanent link")

HASH distribution shuffles data by partition key (partitioned table) or equality fields (non-partitioned table). It simply leverages Flink's `DataStream#keyBy` to distribute the data.

HASH distribution has a few limitations.

*   It doesn't handle skewed data well. E.g. some partitions have a lot more data than others. 
*   It can result in unbalanced traffic distribution if cardinality of the partition key or equality fields is low as demonstrated by [PR 4228](https://github.com/apache/iceberg/pull/4228). 
*   Writer parallelism is limited to the cardinality of the hash key. If the cardinality is 10, only at most 10 writer tasks would get the traffic. Having higher writer parallelism (even if traffic volume requires) won't help. 

### Range distribution (experimental)[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#range-distribution-experimental "Permanent link")

RANGE distribution shuffles data by partition key or sort order via a custom range partitioner. Range distribution collects traffic statistics to guide the range partitioner to evenly distribute traffic to writer tasks.

Range distribution only shuffle the data via range partitioner. Rows are _not_ sorted within a data file, which Flink streaming writer doesn't support yet.

#### Use cases[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#use-cases "Permanent link")

RANGE distribution can be applied to an Iceberg table that either is partitioned or has SortOrder defined. For a partitioned table without SortOrder, partition columns are used as sort order. If SortOrder is explicitly defined for the table, it is used by the range partitioner.

Range distribution can handle skewed data. E.g.

*   Table is partitioned by event time. Typically, recent hours have more data, while the long-tail hours have less and less data. 
*   Table is partitioned by country code, where some countries (like US) have a lot more traffic and smaller countries have a lot less data 
*   Table is partitioned by event type, where some types have a lot more data than others. 

Range distribution can also cluster data on non-partition columns. E.g., table is partitioned hourly on ingestion time. Queries often include predicate on a non-partition column like `device_id` or `country_code`. Range partition would improve the query performance by clustering on the non-partition column when table `SortOrder` is defined with the non-partition column.

#### Traffic statistics[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#traffic-statistics "Permanent link")

Statistics are collected by every shuffle operator subtask and aggregated by the coordinator for every checkpoint cycle. Aggregated statistics are broadcast to all subtasks and applied to the range partitioner in the next checkpoint. So it may take up to two checkpoint cycles to detect traffic distribution change and apply the new statistics to range partitioner.

Range distribution can work with low cardinality (like `country_code`) or high cardinality (like `device_id`) scenarios.

*   For low cardinality scenario (like hundreds or thousands), HashMap is used to track traffic distribution for every key. If a new sort key value shows up, range partitioner would just round-robin it to the writer tasks before traffic distribution has been learned about the new key. 
*   For high cardinality scenario (like millions or billions), uniform random sampling (reservoir sampling) is used to compute range bounds that split the sort key space evenly. It keeps the memory footprint and network exchange low. Reservoir sampling work well if key distribution is relatively even. If a single hot key has unbalanced large share of the traffic, range split by uniform sampling probably won't work very well. 

#### Usage[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#usage "Permanent link")

Here is how to enable range distribution in Java. There are two optional advanced configs. Default should work well for most cases. See [write-options](https://iceberg.apache.org/docs/nightly/flink-configuration/#write-options) for details.

```
FlinkSink.forRowData(input)
    ...
    .distributionMode(DistributionMode.RANGE)
    .rangeDistributionStatisticsType(StatisticsType.Auto)
    .rangeDistributionSortKeyBaseWeight(0.0d)
    .append();
```

### Overhead[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#overhead "Permanent link")

Data shuffling (hash or range) has computational overhead of serialization/deserialization and network I/O. Expect some increase of CPU utilization.

Range distribution also collect and aggregate data distribution statistics. That would also incur some CPU overhead. Memory overhead is typically small if using default statistics type of `Auto`. Don't use `Map` statistics type if key cardinality is high. That could result in significant memory footprint and large network exchange for statistics aggregation.

Notes[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#notes "Permanent link")
---------------------------------------------------------------------------------------

Flink streaming write jobs rely on snapshot summary to keep the last committed checkpoint ID, and store uncommitted data as temporary files. Therefore, [expiring snapshots](https://iceberg.apache.org/docs/nightly/maintenance/#expire-snapshots) and [deleting orphan files](https://iceberg.apache.org/docs/nightly/maintenance/#delete-orphan-files) could possibly corrupt the state of the Flink job. To avoid that, make sure to keep the last snapshot created by the Flink job (which can be identified by the `flink.job-id` property in the summary), and only delete orphan files that are old enough.

Sink V2 based implementation[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#sink-v2-based-implementation "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

At the time when the current default, `FlinkSink` implementation was created, Flink Sink's interface had some limitations that were not acceptable for the Iceberg tables purpose. Due to these limitations, `FlinkSink` is based on a custom chain of `StreamOperator`s terminated by `DiscardingSink`.

In the 1.15 version of Flink [SinkV2 interface](https://cwiki.apache.org/confluence/display/FLINK/FLIP-191%3A+Extend+unified+Sink+interface+to+support+small+file+compaction) was introduced. This interface is used in the new `IcebergSink` implementation which is available in the `iceberg-flink` module. The new implementation is a base for further work on features such as [table maintenance](https://iceberg.apache.org/docs/nightly/maintenance/). The SinkV2 based implementation is currently an experimental feature so use it with caution.

### Writing with SQL[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-sql_1 "Permanent link")

To turn on SinkV2 based implementation in SQL, set this configuration option:

```
SET table.exec.iceberg.use-v2-sink = true;
```

### Writing with DataStream[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#writing-with-datastream_1 "Permanent link")

To use SinkV2 based implementation, replace `FlinkSink` with `IcebergSink` in the provided snippets.

Warning

There are some slight differences between these implementations:

*   The `RANGE` distribution mode is not yet available for the `IcebergSink`
*   When using `IcebergSink` use `uidSuffix` instead of the `uidPrefix`

Flink Dynamic Iceberg Sink[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#flink-dynamic-iceberg-sink "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------

The Flink Dynamic Iceberg Sink (Dynamic Sink) allows:

1.   **Writing to any number of tables**

 A single sink can dynamically route records to multiple Iceberg tables.

2.   **Dynamic table creation and updates**

 Tables are created and updated based on user-defined routing logic.

3.   **Dynamic schema and partition evolution**

 Table schemas and partition specs update during streaming execution.

All configurations are controlled through the `DynamicRecord` class, eliminating the need for Flink job restarts when requirements change.

```
DynamicIcebergSink.forInput(dataStream)
        .generator((inputRecord, out) -> out.collect(
                new DynamicRecord(
                        TableIdentifier.of("db", "table"),
                        "branch",
                        SCHEMA,
                        (RowData) inputRecord,
                        PartitionSpec.unpartitioned(),
                        DistributionMode.HASH,
                        2)))
        .catalogLoader(CatalogLoader.hive("hive", new Configuration(), Map.of()))
        .writeParallelism(10)
        .immediateTableUpdate(true)
        .append();
```

### Configuration Example[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#configuration-example "Permanent link")

```
DynamicIcebergSink.Builder<RowData> builder = DynamicIcebergSink.forInput(inputStream);

// Set common properties
builder
    .set("write.parquet.compression-codec", "gzip");

// Set Dynamic Sink specific options
builder
    .writeParallelism(4)
    .uidPrefix("dynamic-sink")
    .cacheMaxSize(500)
    .cacheRefreshMs(5000);

// Add generator and append sink
builder.generator(new CustomRecordGenerator());
builder.append();
```

### Dynamic Routing Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#dynamic-routing-configuration "Permanent link")

Dynamic table routing can be customized by implementing the `DynamicRecordGenerator` interface:

```
public class CustomRecordGenerator implements DynamicRecordGenerator<RowData> {
    @Override
    public DynamicRecord generate(RowData row) {
        DynamicRecord record = new DynamicRecord();
        // Set table name based on business logic
        TableIdentifier tableIdentifier = TableIdentifier.of(database, tableName);
        record.setTableIdentifier(tableIdentifier);
        record.setData(row);
        // Set the maximum number of parallel writers for a given table/branch/schema/spec
        record.writeParallelism(2);
        return record;
    }
}

// Set custom record generator when building the sink
DynamicIcebergSink.Builder<RowData> builder = DynamicIcebergSink.forInput(inputStream);
builder.generator(new CustomRecordGenerator());
// ... other config ...
builder.append();
```

 The user should provide a converter which converts the input record to a DynamicRecord. We need the following information (DynamicRecord) for every record:
| Property | Description |
| --- | --- |
| `TableIdentifier` | The target table to which the record will be written. |
| `Branch` | The target branch for writing the record (optional). |
| `Schema` | The schema of the record. |
| `Spec` | The expected partitioning specification for the record. |
| `RowData` | The actual row data to be written. |
| `DistributionMode` | The distribution mode for writing the record (currently supports NONE or HASH). |
| `Parallelism` | The maximum number of parallel writers for a given table/branch/schema/spec (WriteTarget). |
| `UpsertMode` | Overrides this table's write.upsert.enabled (optional). |
| `EqualityFields` | The equality fields for the table(optional). |

### Schema Evolution[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#schema-evolution "Permanent link")

The dynamic sink tries to match the schema provided in `DynamicRecord` with the existing table schemas. - If there is a direct match with one of the existing table schemas, that table schema will be used for writing to the table. - If there is no direct match, DynamicSink tries to adapt the provided schema such that it matches one of table schemas. For example, if there is an additional optional column in the table schema, a null value will be added to the RowData provided via DynamicRecord. - Otherwise, we evolve the table schema to match the input schema, within the constraints described below.

The dynamic sink maintains an LRU cache for both table metadata and incoming schemas, with eviction based on size and time constraints. When a DynamicRecord contains a schema that is incompatible with the current table schema, a schema update is triggered. This update can occur either immediately or via a centralized executor, depending on the `immediateTableUpdate` configuration. While centralized updates reduce load on the Catalog, they may introduce backpressure on the sink.

#### Supported schema updates[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#supported-schema-updates "Permanent link")

*   Adding new columns
*   Widening existing column types (e.g., Integer → Long, Float → Double)
*   Making required columns optional
*   Dropping columns (disabled by default)

Dropping columns is disabled by default to prevent issues with late or out-of-order data, as removed fields cannot be easily restored without data loss.

You can opt-in to allow dropping columns (see the configuration options below). Once a column has been dropped, it is technically still possible to write data to that column because Iceberg maintains all past table schemas. However, regular queries won't be able to reference the column. If the field was to re-appear as part of a new schema, an entirely new column would be added, which apart from the name, has nothing in common with the old column, i.e. queries for the new column will never return data of the old column.

##### Unsupported schema updates[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#unsupported-schema-updates "Permanent link")

*   Renaming columns

Renaming is unsupported because schema comparison is name-based, and renames would require additional metadata or hints to resolve.

### Caching[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#caching "Permanent link")

There are two distinct caches involved: the table metadata cache and the input schema cache.

*   The table metadata cache holds metadata such as schema definitions and partition specs to reduce repeated Catalog lookups. Its size is governed by the `cacheMaxSize` setting.
*   The input schema cache stores incoming schemas per table along with their compatibility resolution results. Its size is controlled by `inputSchemasPerTableCacheMaxSize`.

To improve cache hit rates and performance, reuse the same DynamicRecord.schema instance if the record schema is unchanged.

### Dynamic Sink Configuration[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#dynamic-sink-configuration "Permanent link")

The Dynamic Iceberg Flink Sink is configured using the Builder pattern. Here are the key configuration methods:

| Method | Description |
| --- | --- |
| `overwrite(boolean enabled)` | Enable overwrite mode |
| `writeParallelism(int parallelism)` | Set writer parallelism |
| `uidPrefix(String prefix)` | Set operator UID prefix |
| `snapshotProperties(Map<String, String> properties)` | Set snapshot metadata properties |
| `toBranch(String branch)` | Write to a specific branch |
| `cacheMaxSize(int maxSize)` | Set cache size for table metadata |
| `cacheRefreshMs(long refreshMs)` | Set cache refresh interval |
| `inputSchemasPerTableCacheMaxSize(int size)` | Set max input schemas to cache per table |
| `immediateTableUpdate(boolean enabled)` | Controls whether table metadata (schema/partition spec) updates immediately (default: false) |
| `set(String property, String value)` | Set any Iceberg write property (e.g., `"write.format"`, `"write.upsert.enabled"`).Check out all the options here: [write-options](https://iceberg.apache.org/docs/nightly/flink-configuration/#write-options) |
| `setAll(Map<String, String> properties)` | Set multiple properties at once |
| `tableCreator(TableCreator creator)` | When DynamicIcebergSink creates new Iceberg tables, allows overriding how tables are created - setting custom table properties and location based on the table name. |
| `dropUnusedColumns(boolean enabled)` | When enabled, drops all columns from the current table schema which are not contained in the input schema (see the caveats above on dropping columns). |

### Notes[🔗](https://iceberg.apache.org/docs/nightly/flink-writes/#notes_1 "Permanent link")

*   **Range distribution mode**: Currently, the dynamic sink does not support the `RANGE` distribution mode, if set, it will fall back to `HASH`.
*   **Property Precedence Note**: When conflicts occur between table properties and sink properties, the sink properties will override the table properties configuration.
*   **Table Format Version upgrade**: Dynamic sink does not support upgrading a table with dynamic records. The job should not be running while the V2 to V3 upgrade is in progress.

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
