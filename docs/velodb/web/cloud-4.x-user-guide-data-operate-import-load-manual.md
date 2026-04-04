# Source: https://docs.velodb.io/cloud/4.x/user-guide/data-operate/import/load-manual

Version: 4.x

On this page

# Loading Overview

Apache Doris offers various methods for importing and integrating data,
allowing you to import data from various sources into the database. These
methods can be categorized into four types:

  * **Real-Time Writing** : Data is written into Doris tables in real-time via HTTP or JDBC, suitable for scenarios requiring immediate analysis and querying.

    * For small amounts of data (once every 5 minutes), you can use [JDBC INSERT](/cloud/4.x/user-guide/data-operate/import/import-way/insert-into-manual).

    * For higher concurrency or frequency (more than 20 concurrent writes or multiple writes per minute), you can enable [Group Commit](/cloud/4.x/user-guide/data-operate/import/group-commit-manual) and use JDBC INSERT or Stream Load.

    * For high throughput, you can use [Stream Load](/cloud/4.x/user-guide/data-operate/import/import-way/stream-load-manual) via HTTP.

  * **Streaming Synchronization** : Real-time data streams (e.g., Flink, Kafka, transactional databases) are imported into Doris tables, ideal for real-time analysis and querying.

    * You can use Flink Doris Connector to write Flink’s real-time data streams into Doris.

    * You can use [Routine Load](/cloud/4.x/user-guide/data-operate/import/import-way/routine-load-manual) or Doris Kafka Connector for Kafka’s real-time data streams. Routine Load pulls data from Kafka to Doris and supports CSV and JSON formats, while Kafka Connector writes data to Doris, supporting Avro, JSON, CSV, and Protobuf formats.

    * You can use Flink CDC or Datax to write transactional database CDC data streams into Doris.

  * **Batch Import** : Data is batch-loaded from external storage systems (e.g., Object Storage, HDFS, local files, NAS) into Doris tables, suitable for non-real-time data import needs.

    * You can use [Broker Load](/cloud/4.x/user-guide/data-operate/import/import-way/broker-load-manual) to write files from Object Storage and HDFS into Doris.

    * You can use [INSERT INTO SELECT](/cloud/4.x/user-guide/data-operate/import/import-way/insert-into-manual) to synchronously load files from Object Storage, HDFS, and NAS into Doris, and you can perform the operation asynchronously using a [JOB](/cloud/4.x/user-guide/admin-manual/workload-management/job-scheduler).

    * You can use [Stream Load](/cloud/4.x/user-guide/data-operate/import/import-way/stream-load-manual) or Doris Streamloader to write local files into Doris.

  * **External Data Source Integration** : Query and partially import data from external sources (e.g., Hive, JDBC, Iceberg) into Doris tables.

    * You can create a [Catalog](/cloud/4.x/user-guide/lakehouse/lakehouse-overview) to read data from external sources and use [INSERT INTO SELECT](/cloud/4.x/user-guide/data-operate/import/import-way/insert-into-manual) to synchronize this data into Doris, with asynchronous execution via [JOB](/cloud/4.x/user-guide/admin-manual/workload-management/job-scheduler).

Each import method in Doris is an implicit transaction by default. For more
information on transactions, refer to [Transactions](/cloud/4.x/user-
guide/data-operate/transaction).

### Quick Overview of Import Methods​

Doris import process mainly involves various aspects such as data sources,
data formats, import methods, error handling, data transformation, and
transactions. You can quickly browse the scenarios suitable for each import
method and the supported file formats in the table below.

Import Method| Use Case| Supported File Formats| Import Mode| [Stream
Load](/cloud/4.x/user-guide/data-operate/import/import-way/stream-load-
manual)| Importing local files or push data in applications via HTTP.| csv,
json, parquet, orc| Synchronous| [Broker Load](/cloud/4.x/user-guide/data-
operate/import/import-way/broker-load-manual)| Importing from object storage,
HDFS, etc.| csv, json, parquet, orc| Asynchronous| [INSERT INTO
VALUES](/cloud/4.x/user-guide/data-operate/import/import-way/insert-into-
manual)| Writing data via JDBC.| SQL| Synchronous| [INSERT INTO
SELECT](/cloud/4.x/user-guide/data-operate/import/import-way/insert-into-
manual)| Importing from an external source like a table in a catalog or files
in Object Storage, HDFS.| SQL| Synchronous, Asynchronous via Job| [Routine
Load](/cloud/4.x/user-guide/data-operate/import/import-way/routine-load-
manual)| Real-time import from Kafka| csv, json| Asynchronous| [MySQL
Load](/cloud/4.x/user-guide/data-operate/import/import-way/mysql-load-manual)|
Importing from local files.| csv| Synchronous| [Group Commit](/cloud/4.x/user-
guide/data-operate/import/group-commit-manual)| Writing with high frequency.|
Depending on the import method used| -  
---|---|---|---  
  
On This Page

  * Quick Overview of Import Methods

