# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/components-reference.md

# Source: https://docs.pentaho.com/install/components-reference.md

# Source: https://docs.pentaho.com/install/9.3-install/components-reference.md

# Source: https://docs.pentaho.com/install/10.2-install/components-reference.md

# Source: https://docs.pentaho.com/pdia-try-pdia/components-reference.md

# Components reference

Pentaho aims to accommodate diverse computing environments. This list provides details about the environment components and versions we support. Where applicable, versions are listed as certified or supported:

* **Certified**

  The version has been tested and validated for compatibility with Pentaho.
* **Supported**

  Support is available for listed non-certified versions.

If you have questions about your particular computing environment, contact [Pentaho Support](https://support.pentaho.com/).

### Server operating system

The Pentaho Server is hardware-independent and runs on server-class computers.

Your server-class computer must comply with the specifications for minimum hardware and required operating systems:

| Hardware                                                                                                                                                                                                                                         | Certified Operating System - 64 bit                                                                            | Supported Operating System - 64 bit                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| <p><strong>Processor</strong></p><p>Intel EM64T or AMD64 Dual-Core or later</p><p></p><p><strong>RAM</strong></p><p>8 GB with 4 GB dedicated to Pentaho servers</p><p></p><p><strong>Disk Space</strong></p><p>20 GB free after installation</p> | <ul><li>Microsoft Windows 2025 Server</li><li>Red Hat Enterprise 9\*</li><li>Ubuntu Server 22.04 LTS</li></ul> | <p></p><ul><li>Microsoft Windows 2022 Server</li><li>Red Hat Enterprise 8\*</li></ul> |

\*Pentaho Data Integration and Analytics is supported on any Linux distribution binary-compatible with RHEL 9 and Ubuntu Server 22, including in virtualized and cloud environments. If you have any questions, contact [Pentaho Support](https://support.pentaho.com/).

{% hint style="info" %}
**Note:** Mac servers are not supported as an operating system.
{% endhint %}

### Container deployment

Supported technology for deploying Pentaho in containers.

<table><thead><tr><th width="164.99993896484375">Technology</th><th>Certified</th></tr></thead><tbody><tr><td>Docker</td><td>27.5.1</td></tr></tbody></table>

{% hint style="info" %}
**Note:** Kubernetes environments that use this Docker version are also supported.
{% endhint %}

You can also deploy pre-configured Docker images of specific Pentaho products in your AWS environments. See [Docker container deployment of Pentaho Server](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-server) and [Docker container deployment of Carte, Pan, and Kitchen](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/pentaho-installation-overview-cp/docker-container-deployment-of-carte-pan-and-kitchen) for details.

### Workstation operating system

These Pentaho design tools are hardware-independent and run on client-class computers that comply with these specifications for minimum hardware and required operation systems.

* Pentaho Aggregation Designer
* Pentaho Data Integration
* Pentaho Metadata Editor
* Pentaho Report Designer
* Pentaho Schema Workbench

| Hardware - 64 bit                                                                                                                                                                                                                                                                                                                                                                                                                       | Certified Operating System - 64 bit                                                            | Supported Operating System - 64 bit |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------- |
| <p><strong>Processors</strong></p><ul><li>Apple Macintosh Dual-Core</li><li>Apple Mac M1, M2, and M3 chipset</li><li>Intel EM64T or AMD64 Dual-Core or later</li></ul><p></p><p><strong>RAM</strong></p><p>2 GB RAM for most of the design tools, PDI requires 2 GB dedicated</p><p></p><p><strong>Disk Space</strong></p><p>2 GB free after installation</p><p></p><p><strong>Minimum Screen Size</strong></p><p>1280 x 960 pixels</p> | <ul><li>Ubuntu Desktop 22.04</li><li>Microsoft Windows 11</li><li>macOS 15 (Sequioa)</li></ul> | <ul><li>macOS 14 (Sonoma)</li></ul> |

{% hint style="info" %}
**Note:** Ubuntu Linux requires \`libwebkitgtk-1.0\`. See **Install Pentaho Data Integration and Analytics** for more information.
{% endhint %}

#### Embedded software <a href="#embedded-software" id="embedded-software"></a>

When embedding Pentaho software into other applications, the computing environment should comply with these specifications for minimum hardware and required operation systems.

* Embedded Pentaho Reporting
* Embedded Pentaho Analysis
* Embedded Pentaho Data Integration

{% hint style="info" %}
**Note:** Pentaho Data Integration and Analytics is officially certified to run on the Red Hat Enterprise and Ubuntu Linux distributions. It is compatible with any binary-compatible Linux distribution that meets the necessary software and hardware requirements, including in virtualized and cloud environments. If you have any questions, contact [Pentaho Support](https://support.pentaho.com/). The following specifications comply with minimum hardware and required operating systems for embedding Pentaho reporting, analysis, and data integration:
{% endhint %}

| Hardware—64 bit                                                                                                                                                                                                                                             | Certified Operating System—64 bit                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| <ul><li><strong>Processors</strong></li></ul><p>Intel EM64T or AMD64 Dual-Core</p><ul><li><strong>RAM</strong></li></ul><p>8 GB with 4 GB dedicated to Pentaho servers</p><ul><li><strong>Disk Space</strong></li></ul><p>20 GB free after installation</p> | <ul><li>Microsoft Windows 2022 Server</li><li>Red Hat Enterprise 9</li><li>Ubuntu Server 22.04 LTS</li></ul> |

### Application servers

The server to which you deploy Pentaho software must run the following application server:

* Tomcat 10.1.48 (Certified)

### Solution database repositories

Pentaho software stores processing artifacts in these database repositories:

<table><thead><tr><th width="165.99993896484375">Repository</th><th width="131">Certified</th><th width="280.00006103515625">Supported</th></tr></thead><tbody><tr><td>PostgreSQL</td><td>16</td><td>15</td></tr><tr><td>MySQL</td><td>8.4</td><td></td></tr><tr><td>Oracle</td><td>23c &#x26; 23ai</td><td></td></tr><tr><td>MS SQL Server</td><td>2022</td><td>2019 (including patched versions)</td></tr><tr><td>Maria DB</td><td>11.4</td><td></td></tr></tbody></table>

\* The default installed solution database.

#### Apache Hadoop vendors <a href="#apache-hadoop-vendors" id="apache-hadoop-vendors"></a>

Pentaho software has certified or supported data sources from these Hadoop Vendors.

| Vendor                                     | Driver Version |
| ------------------------------------------ | -------------- |
| Amazon EMR                                 | 7.7.0          |
| Cloudera Data Platform (CDP) Private Cloud | 7.1.x, 7.3.1   |

#### Data Sources: Pentaho Tools

This table summarizes which data sources are compatible with the main Pentaho tools.

<table><thead><tr><th width="372">Pentaho Software</th><th>Data Source</th></tr></thead><tbody><tr><td>Pentaho Reporting</td><td><ul><li>JDBC 3/4<sup>1</sup></li><li>ODBC</li><li>OLAP4J</li><li>XML</li><li>Pentaho Analysis</li><li>Pentaho Data Integration</li><li>Pentaho Metadata</li><li>Scriptable</li><li>Snowflake</li></ul></td></tr><tr><td>Pentaho Server, Action Sequences</td><td><ul><li>Relational (JDBC)</li><li>Hibernate</li><li>Javascript</li><li>Metadata (MQL)</li><li>Mondrian (MDX)</li><li>XML (XQuery)</li><li>Security User/Role List Provider</li><li>Snowflake</li><li>Data Integration Steps (PDI)</li><li>Other Action Sequences</li><li>Web Services</li><li>XMLA</li></ul></td></tr><tr><td>Pentaho Data Integration</td><td><ul><li>JDBC 3/4<sup>1</sup></li><li>OLAP4J</li><li>Salesforce</li><li>Snowflake</li><li>XML</li><li>CSV</li><li>Microsoft Excel</li></ul></td></tr></tbody></table>

<sup>1</sup> Use a JDBC 3.x or 4.x compliant driver that is compatible with SQL-92 standards when communicating with relational data sources. For a list of drivers to use with relational JDBC databases, see the [JDBC drivers reference](https://docs.pentaho.com/pdia-try-pdia/jdbc-drivers-reference).

### Big Data Sources: General

Pentaho software supports the following Big Data sources. Check this list if you are evaluating Pentaho or checking for general compatibility with a specific vendor.

| Data Source                                              | Certified | Supported |
| -------------------------------------------------------- | --------- | --------- |
| Amazon EMR (via Hive)                                    | 7.7.0     |           |
| Cassandra (Datastax)                                     | 6.8       |           |
| Cloudera Data Platform (CDP) on premises (private cloud) | 7.1.9     |           |
| Google BigQuery (Simba)                                  | 1.6.2     | 1.2.25    |
| MongoDB                                                  | 7.0       |           |
| Vertica<sup>\*</sup>                                     | 24        |           |

<sup>\*</sup> Deprecated beginning in version 11.0.

### Big Data Sources: Details

This table shows the Big Data sources that are compatible with specific Pentaho tools.

<table data-full-width="false"><thead><tr><th width="126">Data Source</th><th width="115">Versions</th><th width="107.00006103515625">Analyzer</th><th width="108">PIR/PDD</th><th width="116.0001220703125">Pentaho Reporting</th><th width="85">DSW</th><th width="156">PDIServer/Client</th><th width="95.00006103515625">PRD</th><th width="69.99993896484375">PSW</th><th>PME</th></tr></thead><tbody><tr><td>Amazon EMR</td><td>7.7.0<sup>1</sup> (Certified)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Cassandra (Datastax)</td><td>6.8 (Certified)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Cloudera Data Platform (CDP) Private Cloud</td><td>7.1.9 (for job execution)</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Cloudera Data Platform (CDP) Private Cloud</td><td><a href="#support-statement-for-analyzer-on-impala">via Impala</a> (as data source)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Cloudera Data Platform (CDP) Private Cloud</td><td>via Hive3<sup>2</sup> (as data source)</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td><a href="#google-bigquery">Google BigQuery</a></td><td>1.5.4.1008<sup>3</sup></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MongoDB</td><td>7</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Vertica<sup>4</sup></td><td>11</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></tbody></table>

<sup>1</sup> EMR clusters (version 7.x and later) built with JDK 17 exclude the `commons-lang-2.6.jar` library from their standard Hadoop library directories (`$HADOOP_HOME/lib`). To use the EMR driver for EMR 7.x, obtain the `commons-lang-2.6.jar` file from a trusted source, such as the official Maven repository ([Maven Repository: commons-lang » commons-lang » 2.6](https://mvnrepository.com/artifact/commons-lang/commons-lang/2.6)). Then manually copy the downloaded JAR file to the `$HADOOP_HOME/lib` or `$HADOOP_MAPRED_HOME/lib` directory on each node within the EMR cluster to ensure that all worker nodes have access to the library.

<sup>2</sup> Hive3 as a data source for CDP also supports Hive LLAP, and Hive3 on Tez.

<sup>3</sup> The Simba driver required for Google BigQuery is the JDBC 4.2-compatible version, which you can download from <https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery42_1.2.2.1004.zip>.

<sup>4</sup> Deprecated beginning in version 11.0.

{% hint style="info" %}
**Note:** A generic Apache Hadoop driver is included in the Pentaho distribution for version 11.0. Other supported drivers can be downloaded from the [Support Portal](https://support.pentaho.com/hc/en-us).
{% endhint %}

### SQL Dialect-Specific

Pentaho software generates dialect-specific SQL when communicating with these data sources. Certified indicates the SQL dialect has been tested for compatibility with Pentaho.

| Pentaho Software         | Data Source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pentaho Analyzer         | <p>Certified</p><ul><li>Amazon Redshift</li><li>Azure SQL</li><li>Impala</li><li>MySQL</li><li>Microsoft SQL Server</li><li>Oracle</li><li>PostgreSQL</li><li>Snowflake</li></ul><p>Supported</p><ul><li>Access</li><li>Firebird</li><li>Hsqldb</li><li>IBM DB2</li><li>IBM MQ 9.2</li><li>Informix</li><li>Ingres<sup>1</sup></li><li>Interbase<sup>1</sup></li><li>Neoview<sup>1</sup></li><li>SqlStream</li><li>Sybase<sup>1</sup></li><li>Vectorwise<sup>1</sup></li><li>Vertica<sup>1</sup></li><li>Other SQL-89 compliant<sup>2</sup></li></ul>                                                                                                                                                                         |
| Pentaho Metadata         | <p>Certified</p><ul><li>Azure SQL</li><li>Hive 2</li><li>Impala</li><li>MySQL</li><li>PostgreSQL</li></ul><p>Supported</p><ul><li>Amazon Redshift</li><li>ASSQL</li><li>Firebird</li><li>H2</li><li>Hypersonic</li><li>IBM DB2</li><li>IBM MQ 9.2</li><li>Ingres<sup>1</sup></li><li>Interbase<sup>1</sup></li><li>MS Access</li><li>MS SQL Server (JTDS Driver)</li><li>MS SQL Server (Microsoft Driver)</li><li>Snowflake</li><li>Sybase<sup>1</sup></li><li>Vertica<sup>1</sup></li><li>Other SQL-92 compliant<sup>2</sup></li></ul>                                                                                                                                                                                       |
| Pentaho Data Integration | <p>Certified</p><ul><li>Amazon Redshift</li><li>Azure SQL</li><li>Hive<sup>1</sup></li><li>Hive 2</li><li>Impala</li><li>MS SQL Server (JTDS Driver)</li><li>MS SQL Server (Microsoft Driver)</li><li>MySQL</li><li>Oracle</li><li>PostgreSQL</li><li>Snowflake</li><li>Vertica<sup>1</sup></li></ul><p>Supported</p><ul><li>AS/400</li><li>InfiniDB<sup>1</sup></li><li>Exasol 4</li><li>Firebird SQL</li><li>H2</li><li>Hypersonic</li><li>IBM DB2</li><li>IBM MQ 9.2</li><li>Informix</li><li>Ingres<sup>1</sup></li><li>Ingres VectorWise<sup>1</sup></li><li>MaxDB (SAP DB)</li><li>Neoview<sup>1</sup></li><li>Oracle RDB</li><li>SQLite</li><li>UniVerse database</li><li>Other SQL-92 compliant<sup>2</sup></li></ul> |

<sup>1</sup> Deprecated beginning in version 11.0.

<sup>2</sup> If your data source is not in this list and is compatible with SQL-92, Pentaho software uses a generic SQL dialect.

### Security

Pentaho software integrates with these third-party security authentication systems:

* CAS 7 (Certified)
* Integrated Windows Authentication with Internet Information Services 10 (Certified)
* Spring 6.2.12 (Certified)

### Java virtual machine

Pentaho software requirements for Java Runtime Environment (JRE).

| Pentaho Software     | Certified                                                  | Supported                                                  |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| All Pentaho software | <ul><li>Oracle Java 21</li><li>Oracle OpenJDK 21</li></ul> | <ul><li>Oracle Java 17</li><li>Oracle OpenJDK 17</li></ul> |

{% hint style="info" %}
**Note:** The PDI client requires at least Java 11.x to run on Windows 11.
{% endhint %}

### Web browsers

Pentaho supports major versions of web browsers that are publicly available six weeks before the finalization of a Pentaho release.

| Certified Browsers                                                                                                                          | Supported Browsers                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p></p><ul><li>Apple Safari 26.1 (On macOS only)</li><li>Google Chrome 142</li><li>Microsoft Edge 142</li><li>Mozilla Firefox 144</li></ul> | <p></p><ul><li>Apple Safari 26.1 and later (On macOS only)</li><li>Google Chrome 142 and later</li><li>Microsoft Edge 142 and later</li><li>Mozilla Firefox 144 and later</li></ul> |

### Support Statement for Analyzer on Impala

These are the minimum requirements for Analyzer to work with Impala:

* Pentaho 7.1 or later
* Impala 1.3.x or later
* Recommend using Parquet compressed file format for tables in Impala
* Make sure that the JDBC driver is dropped into the Pentaho Server and Schema Workbench directories. See the **Install Pentaho Data Integration and Analytics** document for details.
* Turn off connection pooling in Pentaho Server.
* In Mondrian schemas, divide dimension tables with high cardinality into several levels

**Note:** As with any data source, the performance of Pentaho Analyzer on Impala will be dependent upon the data shape, Impala’s configuration, and the types of queries. See the best practice, "Pentaho Analyzer with Impala as a Data Source" located at: [https://support.pentaho.com/hc/en-us/articles/208652846](https://support.pentaho.com/hc/en-us/articles/360002913871-Big-Data-and-Pentaho) or download the [PDF](https://support.pentaho.com/hc/en-us/article_attachments/360012191711/Pentaho_Analyzer_and_Impala_Data_Source_Settings_and_Recommendations.pdf).

There are some compiled Mondrian automated test suite results for Analyzer on Impala with OEM Simba, as well as the community Apache Hive driver:

* [Analyzer on Impala with OEM Simba](http://wiki.pentaho.com/display/analysis/PA_CR_PA-3.7.0.0-752_impalad-1.3.0_simba-2.5.2)
* [Analyzer on Impala with community Apache Hive driver](http://wiki.pentaho.com/display/analysis/PA_CR_PA-3.7.0.0-752_impalad-1.3.0)

### Google BigQuery

You can use Google BigQuery as a data source with the Pentaho User Console or with the PDI client.

Before you begin, you must have a Google account and must create service account credentials in the form of a key file in JSON format to connect to Google BigQuery. To create service account credentials, see the [Google Cloud Storage Authentication documentation](https://cloud.google.com/storage/docs/authentication).

Additionally, you must set permissions for your BigQuery and Google Cloud accounts. To configure your service account authentication, see the [Google Service Account documentation](https://www.simba.com/products/BigQuery/doc/v1/JDBC_InstallGuide/content/jdbc/bq/authenticating/serviceaccount.htm).

Perform the following steps to create a JDBC connection to a Google BigQuery data source from the User Console or PDI client.

1. Stop the Pentaho Server.
2. Download the ZIP file containing the Simba version 1.5.4.1008 JDBC 4.2 driver for Google BigQuery from <https://storage.googleapis.com/simba-bq-release/jdbc/SimbaJDBCDriverforGoogleBigQuery42_1.2.2.1004.zip>.
3. Navigate to the `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib` directory for the User Console or the `design-tools/data-integration/lib` directory for the PDI client and delete any files associated with previous versions of Google BigQuery.

   Visually verify each file to ensure the older version is deleted.
4. Extract the following files to the `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib` folder for the User Console or the `design-tools/data-integration/lib` directory for the PDI client.
   * `animal-sniffer-annotations-1.14.jar`
   * `api-common-1.7.0.jar`
   * `avro-1.9.0.jar`
   * `checker-compat-qual-2.5.2.jar`
   * `error_prone_annotations-2.1.3.jar`
   * `gax-1.42.0.jar`
   * `gax-grpc-1.42.0.jar`
   * `google-api-client-1.28.0.jar`
   * `google-api-services-bigquery-v2-rev426-1.25.0.jar`
   * `google-auth-library-credentials-0.15.0.jar`
   * `google-auth-library-oauth2-http-0.13.0.jar`
   * `GoogleBigQueryJDBC42.jar`
   * `google-cloud-bigquerystorage-0.85.0-alpha.jar`
   * `google-cloud-core-1.67.0.jar`
   * `google-cloud-core-grpc-1.67.0.jar`
   * `google-http-client-1.29.0.jar`
   * `google-http-client-apache-2.0.0.jar`
   * `google-http-client-jackson2-1.28.0.jar`
   * `google-oauth-client-1.28.0.jar`
   * `grpc-alts-1.18.0.jar`
   * `grpc-auth-1.18.0.jar`
   * `grpc-context-1.18.0.jar`
   * `grpc-core-1.18.0.jar`
   * `grpc-google-cloud-bigquerystorage-v1beta1-0.50.0.jar`
   * `grpc-grpclb-1.18.0.jar`
   * `grpc-netty-shaded-1.18.0.jar`
   * `grpc-protobuf-1.18.0.jar`
   * `grpc-protobuf-lite-1.18.0.jar`
   * `grpc-stub-1.18.0.jar`
   * `gson-2.7.jar`
   * `j2objc-annotations-1.1.jar`
   * `javax.annotation-api-1.3.2.jar`
   * `jsr305-3.0.2.jar`
   * `opencensus-api-0.18.0.jar`
   * `opencensus-contrib-grpc-metrics-0.18.0.jar`
   * `opencensus-contrib-http-util-0.18.0.jar`
   * `protobuf-java-3.7.0.jar`
   * `protobuf-java-util-3.7.0.jar`
   * `proto-google-cloud-bigquerystorage-v1beta1-0.50.0.jar`
   * `proto-google-common-protos-1.15.0.jar`
   * `proto-google-iam-v1-0.12.0.jar`
   * `threetenbp-1.3.3.jar`**Note:** The Google BigQuery connection name does not display in the User Console Database Connection dialog box until you copy these files.
5. Restart the Pentaho Server.
6. Log on to the User Console or the PDI client, then open the Database Connection dialog box.

   See the **Install Pentaho Data Integration and Analytics** document for more information on the Database Connection dialog box.
7. In the Database Connection dialog box, select **General**, then select **Google BigQuery** as the **Database Type**.
8. In the **Settings** area, enter the information for your Google BigQuery account.
   * The **Host Name** is the URL to Google's BigQuery web services API. For example, <https://www.googleapis.com/bigquery/v2>
   * The **Project ID** in the PDI client and the **Database name** in the User Console are identical.
   * The **Port Number** is `443`.
9. Click **Options**, then add the following parameters and values.

   | Parameter                 | Value                                                                                                                  |
   | ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
   | **OAuthType**             | `0` (Zero)                                                                                                             |
   | **OAuthServiceAcctEmail** | Specify your service account email address.                                                                            |
   | **OAuthPvtKeyPath**       | Specify the path to your private key credential file.                                                                  |
   | **Timeout**               | Specify the amount of time, in seconds, before the server closes the connection. The recommended value is 120 seconds. |
10. Click **Test** to verify that you can connect to your data.
