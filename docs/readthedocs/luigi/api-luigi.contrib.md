# luigi.contrib

Package containing optional and-on functionality.

Modules

`azureblob`

`batch`

AWS Batch wrapper for Luigi

`beam_dataflow`

`bigquery`

`bigquery_avro`

Specialized tasks for handling Avro data in BigQuery from GCS.

`datadog_metric`

`docker_runner`

Docker container wrapper for Luigi.

`dropbox`

`esindex`

Support for Elasticsearch (1.0.0 or newer).

`external_daily_snapshot`

`external_program`

Template tasks for running external programs as luigi tasks.

`ftp`

This library is a wrapper of ftplib or pysftp.

`gcp`

Common code for GCP (google cloud services) integration

`gcs`

luigi bindings for Google Cloud Storage

`hadoop`

Run Hadoop Mapreduce jobs using Hadoop Streaming.

`hadoop_jar`

Provides functionality to run a Hadoop job using a Jar

`hdfs`

Provides access to HDFS using the `HdfsTarget`, a subclass of `Target`.

`hive`

`kubernetes`

Kubernetes Job wrapper for Luigi.

`lsf`

`lsf_runner`

`mongodb`

`mrrunner`

Since after Luigi 2.5.0, this is a private module to Luigi.

`mssqldb`

`mysqldb`

`opener`

OpenerTarget support, allows easier testing and configuration by abstracting out the LocalTarget, S3Target, and MockTarget types.

`pai`

MicroSoft OpenPAI Job wrapper for Luigi.

`pig`

Apache Pig support. Example configuration section in luigi.cfg::.

`postgres`

Implements a subclass of `Target` that writes data to Postgres.

`presto`

`prometheus_metric`

`pyspark_runner`

The pyspark program.

`rdbms`

A common module for postgres like databases, such as postgres or redshift

`redis_store`

`redshift`

`s3`

Implementation of Simple Storage Service support.

`salesforce`

`scalding`

`sge`

SGE batch system Tasks.

`sge_runner`

The SunGrid Engine runner

`simulate`

A module containing classes used to simulate certain behaviors

`spark`

`sparkey`

`sqla`

Support for SQLAlchemy.

`ssh`

Light-weight remote execution library and utilities.

`target`

`webhdfs`

Provides a `WebHdfsTarget` using the Python hdfs [https://pypi.python.org/pypi/hdfs/]