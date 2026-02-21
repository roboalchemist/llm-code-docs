# Source: https://airflow.apache.org/docs/

Title: Documentation

URL Source: https://airflow.apache.org/docs/

Markdown Content:
[Apache Airflow®](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
-----------------------------------------------------------------------------------

Apache Airflow Core, which includes webserver, scheduler, CLI and other components that are needed for minimal Airflow installation. [Read the documentation »](https://airflow.apache.org/docs/apache-airflow/stable/index.html)

[Apache Airflow CTL (airflowctl)](https://airflow.apache.org/docs/apache-airflow-ctl/stable/index.html)
-------------------------------------------------------------------------------------------------------

Apache Airflow CTL (airflowctl) is a command-line interface (CLI) for Apache Airflow that interacts exclusively with the Airflow REST API. It provides a secure, auditable, and consistent way to manage Airflow deployments — without direct access to the metadata database. [Read the documentation »](https://airflow.apache.org/docs/apache-airflow-ctl/stable/index.html)

[Task SDK](https://airflow.apache.org/docs/task-sdk/stable/index.html)
----------------------------------------------------------------------

The Task SDK provides python-native interfaces for defining DAGs, executing tasks in isolated subprocesses and interacting with Airflow resources (e.g., Connections, Variables, XComs, Metrics, Logs, and OpenLineage events) at runtime. The goal of task-sdk is to decouple DAG authoring from Airflow internals (Scheduler, API Server, etc.), providing a forward-compatible, stable interface for writing and maintaining DAGs across Airflow versions. [Read the documentation »](https://airflow.apache.org/docs/task-sdk/stable/index.html)

[Docker stack](https://airflow.apache.org/docs/docker-stack/index.html)
-----------------------------------------------------------------------

Airflow has an official Dockerfile and Docker image published in DockerHub as a convenience package for installation. You can extend and customize the image according to your requirements and use it in your own deployments. [Read the documentation »](https://airflow.apache.org/docs/docker-stack/index.html)

[Helm Chart](https://airflow.apache.org/docs/helm-chart/stable/index.html)
--------------------------------------------------------------------------

Airflow has an official Helm Chart that will help you set up your own Airflow on a cloud/on-prem Kubernetes environment and leverage its scalable nature to support a large group of users. Thanks to Kubernetes, we are not tied to a specific cloud provider. [Read the documentation »](https://airflow.apache.org/docs/helm-chart/stable/index.html)

[Python API Client](https://github.com/apache/airflow-client-python)
--------------------------------------------------------------------

Airflow releases official Python API client that can be used to easily interact with Airflow REST API from Python code. [See the client repository](https://github.com/apache/airflow-client-python)

[Providers packages](https://airflow.apache.org/docs/apache-airflow-providers/index.html)
-----------------------------------------------------------------------------------------

Providers packages include integrations with third party projects. They are versioned and released independently of the Apache Airflow core. [Read the documentation »](https://airflow.apache.org/docs/apache-airflow-providers/index.html)

### Active providers

*   [`Airbyte`](https://airflow.apache.org/docs/apache-airflow-providers-airbyte/stable/index.html)
*   [`Alibaba`](https://airflow.apache.org/docs/apache-airflow-providers-alibaba/stable/index.html)
*   [`Amazon`](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html)
*   [`Apache Beam`](https://airflow.apache.org/docs/apache-airflow-providers-apache-beam/stable/index.html)
*   [`Apache Cassandra`](https://airflow.apache.org/docs/apache-airflow-providers-apache-cassandra/stable/index.html)
*   [`Apache Drill`](https://airflow.apache.org/docs/apache-airflow-providers-apache-drill/stable/index.html)
*   [`Apache Druid`](https://airflow.apache.org/docs/apache-airflow-providers-apache-druid/stable/index.html)
*   [`Apache Flink`](https://airflow.apache.org/docs/apache-airflow-providers-apache-flink/stable/index.html)
*   [`Apache HDFS`](https://airflow.apache.org/docs/apache-airflow-providers-apache-hdfs/stable/index.html)
*   [`Apache Hive`](https://airflow.apache.org/docs/apache-airflow-providers-apache-hive/stable/index.html)
*   [`Apache Iceberg`](https://airflow.apache.org/docs/apache-airflow-providers-apache-iceberg/stable/index.html)
*   [`Apache Impala`](https://airflow.apache.org/docs/apache-airflow-providers-apache-impala/stable/index.html)
*   [`Apache Kafka`](https://airflow.apache.org/docs/apache-airflow-providers-apache-kafka/stable/index.html)
*   [`Apache Kylin`](https://airflow.apache.org/docs/apache-airflow-providers-apache-kylin/stable/index.html)
*   [`Apache Livy`](https://airflow.apache.org/docs/apache-airflow-providers-apache-livy/stable/index.html)
*   [`Apache Pig`](https://airflow.apache.org/docs/apache-airflow-providers-apache-pig/stable/index.html)
*   [`Apache Pinot`](https://airflow.apache.org/docs/apache-airflow-providers-apache-pinot/stable/index.html)
*   [`Apache Spark`](https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/stable/index.html)
*   [`Apache Tinkerpop`](https://airflow.apache.org/docs/apache-airflow-providers-apache-tinkerpop/stable/index.html)
*   [`Apprise`](https://airflow.apache.org/docs/apache-airflow-providers-apprise/stable/index.html)
*   [`ArangoDB`](https://airflow.apache.org/docs/apache-airflow-providers-arangodb/stable/index.html)
*   [`Asana`](https://airflow.apache.org/docs/apache-airflow-providers-asana/stable/index.html)
*   [`Atlassian Jira`](https://airflow.apache.org/docs/apache-airflow-providers-atlassian-jira/stable/index.html)
*   [`Celery`](https://airflow.apache.org/docs/apache-airflow-providers-celery/stable/index.html)
*   [`Cloudant`](https://airflow.apache.org/docs/apache-airflow-providers-cloudant/stable/index.html)
*   [`CNCF Kubernetes`](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/index.html)
*   [`Cohere`](https://airflow.apache.org/docs/apache-airflow-providers-cohere/stable/index.html)
*   [`Common Compat`](https://airflow.apache.org/docs/apache-airflow-providers-common-compat/stable/index.html)
*   [`Common IO`](https://airflow.apache.org/docs/apache-airflow-providers-common-io/stable/index.html)
*   [`Common Messaging`](https://airflow.apache.org/docs/apache-airflow-providers-common-messaging/stable/index.html)
*   [`Common SQL`](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/stable/index.html)
*   [`Databricks`](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html)
*   [`Datadog`](https://airflow.apache.org/docs/apache-airflow-providers-datadog/stable/index.html)
*   [`dbt Cloud`](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html)
*   [`Dingding`](https://airflow.apache.org/docs/apache-airflow-providers-dingding/stable/index.html)
*   [`Discord`](https://airflow.apache.org/docs/apache-airflow-providers-discord/stable/index.html)
*   [`Docker`](https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/index.html)
*   [`Edge3`](https://airflow.apache.org/docs/apache-airflow-providers-edge3/stable/index.html)
*   [`Elasticsearch`](https://airflow.apache.org/docs/apache-airflow-providers-elasticsearch/stable/index.html)
*   [`Exasol`](https://airflow.apache.org/docs/apache-airflow-providers-exasol/stable/index.html)
*   [`FAB (Flask-AppBuilder)`](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html)
*   [`Facebook`](https://airflow.apache.org/docs/apache-airflow-providers-facebook/stable/index.html)
*   [`File Transfer Protocol (FTP)`](https://airflow.apache.org/docs/apache-airflow-providers-ftp/stable/index.html)
*   [`Git`](https://airflow.apache.org/docs/apache-airflow-providers-git/stable/index.html)
*   [`GitHub`](https://airflow.apache.org/docs/apache-airflow-providers-github/stable/index.html)
*   [`Google`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/index.html)
*   [`gRPC`](https://airflow.apache.org/docs/apache-airflow-providers-grpc/stable/index.html)
*   [`Hashicorp`](https://airflow.apache.org/docs/apache-airflow-providers-hashicorp/stable/index.html)
*   [`Hypertext Transfer Protocol (HTTP)`](https://airflow.apache.org/docs/apache-airflow-providers-http/stable/index.html)
*   [`IBM Cloudant`](https://airflow.apache.org/docs/apache-airflow-providers-cloudant/stable/index.html)
*   [`Influx DB`](https://airflow.apache.org/docs/apache-airflow-providers-influxdb/stable/index.html)
*   [`Internet Message Access Protocol (IMAP)`](https://airflow.apache.org/docs/apache-airflow-providers-imap/stable/index.html)
*   [`Java Database Connectivity (JDBC)`](https://airflow.apache.org/docs/apache-airflow-providers-jdbc/stable/index.html)
*   [`Jenkins`](https://airflow.apache.org/docs/apache-airflow-providers-jenkins/stable/index.html)
*   [`Keycloak`](https://airflow.apache.org/docs/apache-airflow-providers-keycloak/stable/index.html)
*   [`Microsoft Azure`](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html)
*   [`Microsoft SQL Server (MSSQL)`](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-mssql/stable/index.html)
*   [`Microsoft PowerShell Remoting Protocol (PSRP)`](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-psrp/stable/index.html)
*   [`Microsoft Windows Remote Management (WinRM)`](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-winrm/stable/index.html)
*   [`MongoDB`](https://airflow.apache.org/docs/apache-airflow-providers-mongo/stable/index.html)
*   [`MySQL`](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/index.html)
*   [`Neo4j`](https://airflow.apache.org/docs/apache-airflow-providers-neo4j/stable/index.html)
*   [`ODBC`](https://airflow.apache.org/docs/apache-airflow-providers-odbc/stable/index.html)
*   [`OpenAI`](https://airflow.apache.org/docs/apache-airflow-providers-openai/stable/index.html)
*   [`OpenFaaS`](https://airflow.apache.org/docs/apache-airflow-providers-openfaas/stable/index.html)
*   [`OpenLineage`](https://airflow.apache.org/docs/apache-airflow-providers-openlineage/stable/index.html)
*   [`Open Search`](https://airflow.apache.org/docs/apache-airflow-providers-opensearch/stable/index.html)
*   [`Opsgenie`](https://airflow.apache.org/docs/apache-airflow-providers-opsgenie/stable/index.html)
*   [`Oracle`](https://airflow.apache.org/docs/apache-airflow-providers-oracle/stable/index.html)
*   [`Pagerduty`](https://airflow.apache.org/docs/apache-airflow-providers-pagerduty/stable/index.html)
*   [`Papermill`](https://airflow.apache.org/docs/apache-airflow-providers-papermill/stable/index.html)
*   [`PgVector`](https://airflow.apache.org/docs/apache-airflow-providers-pgvector/stable/index.html)
*   [`Pinecone`](https://airflow.apache.org/docs/apache-airflow-providers-pinecone/stable/index.html)
*   [`PostgreSQL`](https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/index.html)
*   [`Presto`](https://airflow.apache.org/docs/apache-airflow-providers-presto/stable/index.html)
*   [`Qdrant`](https://airflow.apache.org/docs/apache-airflow-providers-qdrant/stable/index.html)
*   [`Redis`](https://airflow.apache.org/docs/apache-airflow-providers-redis/stable/index.html)
*   [`Salesforce`](https://airflow.apache.org/docs/apache-airflow-providers-salesforce/stable/index.html)
*   [`Samba`](https://airflow.apache.org/docs/apache-airflow-providers-samba/stable/index.html)
*   [`Segment`](https://airflow.apache.org/docs/apache-airflow-providers-segment/stable/index.html)
*   [`Sendgrid`](https://airflow.apache.org/docs/apache-airflow-providers-sendgrid/stable/index.html)
*   [`SFTP`](https://airflow.apache.org/docs/apache-airflow-providers-sftp/stable/index.html)
*   [`Singularity`](https://airflow.apache.org/docs/apache-airflow-providers-singularity/stable/index.html)
*   [`Slack`](https://airflow.apache.org/docs/apache-airflow-providers-slack/stable/index.html)
*   [`SMTP`](https://airflow.apache.org/docs/apache-airflow-providers-smtp/stable/index.html)
*   [`Snowflake`](https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/index.html)
*   [`SQLite`](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/stable/index.html)
*   [`SSH`](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/index.html)
*   [`Standard`](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/index.html)
*   [`Tableau`](https://airflow.apache.org/docs/apache-airflow-providers-tableau/stable/index.html)
*   [`Telegram`](https://airflow.apache.org/docs/apache-airflow-providers-telegram/stable/index.html)
*   [`Teradata`](https://airflow.apache.org/docs/apache-airflow-providers-teradata/stable/index.html)
*   [`Trino`](https://airflow.apache.org/docs/apache-airflow-providers-trino/stable/index.html)
*   [`Vertica`](https://airflow.apache.org/docs/apache-airflow-providers-vertica/stable/index.html)
*   [`Weaviate`](https://airflow.apache.org/docs/apache-airflow-providers-weaviate/stable/index.html)
*   [`Yandex`](https://airflow.apache.org/docs/apache-airflow-providers-yandex/stable/index.html)
*   [`YDB`](https://airflow.apache.org/docs/apache-airflow-providers-ydb/stable/index.html)
*   [`Zendesk`](https://airflow.apache.org/docs/apache-airflow-providers-zendesk/stable/index.html)

### Suspended providers

These providers are currently suspended from releases and we are not actively testing their compatibility with latest Airflow releases. You can still use the released versions of these providers if you need to and in case the reason for suspension is resolved, the provider might be resumed by a PR of a community member who will resolve the suspension reason. It the provider is suspended for quite some time, the community might make a decision about removing it.

More about the suspension/resuming process can be found in the [Community provider’s lifecycle documentation](https://github.com/apache/airflow/blob/main/PROVIDERS.rst#community-providers-lifecycle) page.

*   No suspended providers at the moment

### Removed providers

These providers are no longer supported and have been removed from the codebase, you can however still use the released versions of these providers if you need to.

More about the removal process can be found in the [Community provider’s lifecycle documentation](https://github.com/apache/airflow/blob/main/PROVIDERS.rst#community-providers-lifecycle) page.

*   [`Apache Sqoop`](https://airflow.apache.org/docs/apache-airflow-providers-apache-sqoop/stable/index.html)
*   [`Dask Executor`](https://airflow.apache.org/docs/apache-airflow-providers-daskexecutor/stable/index.html)
*   [`Plexus`](https://airflow.apache.org/docs/apache-airflow-providers-plexus/stable/index.html)
*   [`Qubole`](https://airflow.apache.org/docs/apache-airflow-providers-qubole/stable/index.html)
*   [`Tabular`](https://airflow.apache.org/docs/apache-airflow-providers-tabular/stable/index.html)
