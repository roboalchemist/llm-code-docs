# Source: https://docs.snowflake.com/en/connectors/kafkahp/setup-kafka.md

# Snowflake High Performance connector for Kafka: Install and configure

This topic describes the steps to install and configure the Snowflake High Performance connector for Kafka.

## Installing the Kafka connector

The Kafka connector is provided as a JAR (Java executable) file.

Snowflake provides two versions of the connector:

* A version for the [Confluent Kafka installation](https://www.confluent.io/hub/snowflakeinc/snowflake-kafka-connector/).
* A version for the open source software (OSS) Apache Kafka <https://mvnrepository.com/artifact/com.snowflake/snowflake-kafka-connector/> ecosystem.

The instructions in this topic specify which steps apply only to either version of the connector.

## Installation prerequisites

* The Kafka connector supports the following package versions:

  | Package | Snowflake Kafka Connector Version | Package Support (Tested by Snowflake) |
  | --- | --- | --- |
  | Apache Kafka | 2.0.0 (or later) | Apache Kafka 2.8.2, 3.7.2 |
  | Confluent | 2.0.0 (or later) | Confluent 6.2.15, 7.8.2 |

* The Kafka connector is built for use with Kafka Connect API 3.9.0. Later versions of the Kafka Connect API are untested.
  Versions prior to 3.9.0 are compatible with the connector.
  For more information, see [Kafka Compatibility](https://kafka.apache.org/protocol.html#protocol_compatibility).
* When you have both the Kafka connector and the JDBC driver jar files in your environment,
  ensure your JDBC version matches the `snowflake-jdbc` version specified in the `pom.xml` file of your intended Kafka connector version.
  You can go to your preferred Kafka connector release version, for example, [v4.0.0-rc4](https://github.com/snowflakedb/snowflake-kafka-connector/releases/tag/v4.0.0-rc4). Then browse `pom.xml` file to find out the version of `snowflake-jdbc`.
* If you are using Avro format for ingesting data:

  > * Use the Avro parser, version 1.8.2 (or higher), available from <https://mvnrepository.com/artifact/org.apache.avro>.
  > * If you use the schema registry feature with Avro, use version 5.0.0 (or higher) of the Kafka Connect Avro Converter available at <https://mvnrepository.com/artifact/io.confluent>.
  >
  >   Note that the schema registry feature is not available in the OSS Apache Kafka package.
* Configure Kafka with the desired data retention time and/or storage limit.
* Install and configure the Kafka Connect cluster.

  Each Kafka Connect cluster node should include enough RAM for the Kafka connector. The minimum recommended amount is 5 MB per Kafka partition. This is in addition to the RAM required for any other work that Kafka Connect is doing.
* We recommend using the same versions on Kafka Broker and Kafka Connect Runtime.
* We strongly recommend running your Kafka Connect instance in the same cloud
  provider [region](../../user-guide/intro-regions.md) as your Snowflake account. This is not strictly required, but typically improves throughput.

For a list of the operating systems supported by Snowflake clients, see [Operating system support](../../release-notes/requirements.md).

## Installing the connector

This section provides instructions for installing and configuring the Kafka connector for Confluent.
The following table describes the supported versions and information about pre-release and release candidates.

| Release Series | Status | Notes |
| --- | --- | --- |
| 4.x.x | Public Preview | Early access. **Supporting** Snowpipe Streaming High Performance Architecture <https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview> Currently the migration from 3.x and 2.x versions has to be done manually. It can not be used as a drop in replacement for earlier versions. It has a different feature set than version 3.x, 2.x, 1.x |
| 3.x.x | Officially supported | **Not supporting** Snowpipe Streaming High Performance Architecture <https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview>. |
| 2.x.x | Officially supported | Upgrade recommended. **Not supporting** Snowpipe Streaming High Performance Architecture <https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview>. |
| 1.x.x | Not supported | Do not use this release series. |

### Installing the connector for Confluent

#### Download the Kafka connector files

Download the Kafka connector JAR file from either of the following locations:

Confluent Hub:
:   <https://www.confluent.io/hub/>

    The package includes all dependencies required to use either an encrypted or unencrypted private key for key pair authentication.
    For more information, see Using key pair authentication and key rotation later in this topic.

Maven Central Repository:
:   <https://mvnrepository.com/artifact/com.snowflake>

    When using this version you need to download the [Bouncy Castle](https://www.bouncycastle.org/) cryptography libraries (a JAR files):

    > * <https://mvnrepository.com/artifact/org.bouncycastle/bc-fips/2.1.0>
    > * <https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-fips/2.1.8>

    Download these files to the same local folder as the Kafka connector JAR file.

    The source code for the connector is available at <https://github.com/snowflakedb/snowflake-kafka-connector>.

#### Install the Kafka connector

Install the Kafka connector using the instructions provided for installing other connectors:

> <https://docs.confluent.io/current/connect/userguide.html>

### Installing the connector for open source Apache Kafka

This section provides instructions for installing and configuring the Kafka connector for open source Apache Kafka.

#### Install Apache Kafka

1. Download the Kafka package from the [Kafka official website](https://kafka.apache.org/downloads).
2. In a terminal window, change to the directory where you downloaded the package file.
3. Execute the following command to decompress the `kafka_<scala_version>-<kafka_version>.tgz` file:

   ```bash
   tar xzvf kafka_<scala_version>-<kafka_version>.tgz
   ```

#### Install the JDK

Install and configure the Java Development Kit (JDK) version 11 or higher.
Snowflake tests with the Standard Edition (SE) of the JDK. The Enterprise Edition (EE) is expected to be compatible but has not been tested.

If you have previously installed the JDK, you can skip this section.

1. Download the JDK from the [Oracle JDK website](https://www.oracle.com/technetwork/java/javase/downloads/index.html).
2. Install or decompress the JDK.
3. Following the instructions for your operating system, set the environment variable JAVA_HOME to point to the directory containing the JDK.

#### Download the Kafka connector JAR files

1. Download the Kafka connector JAR file from the Maven Central Repository:

   <https://mvnrepository.com/artifact/com.snowflake>
2. Download the [Bouncy Castle](https://www.bouncycastle.org/) cryptography library jar files:

   * <https://mvnrepository.com/artifact/org.bouncycastle/bc-fips/2.1.0>
   * <https://mvnrepository.com/artifact/org.bouncycastle/bcpkix-fips/2.1.8>
3. If your Kafka data is streamed in [Apache Avro](https://avro.apache.org/) format, download the Avro JAR file (1.11.4):

   * <https://mvnrepository.com/artifact/org.apache.avro/avro>

The source code for the connector is available at <https://github.com/snowflakedb/snowflake-kafka-connector>.

#### Install the Kafka connector

Copy the JAR files you downloaded in Installing the connector for open source Apache Kafka to the `<kafka_dir>/libs` folder.

## Configuring the Kafka connector

When deployed in standalone mode, the connector is configured by creating a file that
specifies parameters such as the Snowflake login credentials, topic name(s), Snowflake table name(s), and others.
When deployed in distributed mode the connector is configured by calling REST API endpoint of the kafka connect cluster.

> **Important:**
>
> The Kafka Connect framework broadcasts the configuration settings for the Kafka connector from the master node to worker nodes.
> Configuration settings include sensitive information, specifically, the Snowflake username and private key.
> Make sure to secure the communication channel between Kafka Connect nodes.
> For more information, see the documentation for your Apache Kafka software.

Each configuration specifies the topics and corresponding tables for one database and one schema in that database.
Note that a connector can ingest messages from
any number of topics, but the corresponding tables must all be stored in a single database and schema.

This section provides instructions for both the distributed and standalone modes.

For descriptions of the configuration fields, see Connector configuration properties.

> **Important:**
>
> Because the configuration file typically contains security related information,
> such as the private key, set read/write privileges appropriately on the file to limit access.
>
> In addition, consider storing the configuration file in a secure external
> location or a key management service. For more information, see Externalizing Secrets (in this topic).

### Distributed mode

Create the Kafka configuration file, e.g. `<path>/<config_file>.json`.
Populate the file with all connector configuration information.
The file must be in JSON format.

**Sample configuration file**

```json
{
  "name":"XYZCompanySensorData",
  "config":{
      "connector.class": "com.snowflake.kafka.connector.SnowflakeStreamingSinkConnector",
      "tasks.max": "1",
      "snowflake.topic2table.map": "topic1:table_1,topic2:table_2",
      "snowflake.url.name": "myorganization-myaccount.snowflakecomputing.com:443",
      "snowflake.warehouse.name": "WH",
      "snowflake.private.key": "-----BEGIN PRIVATE KEY-----\n .... \n-----END PRIVATE KEY-----\n",
      "snowflake.schema.name": "MY_SCHEMA",
      "snowflake.database.name": "MY_DATABASE",
      "snowflake.role.name": "MY_ROLE",
      "snowflake.user.name": "MY_USER",
      "value.converter": "org.apache.kafka.connect.json.JsonConverter",
      "key.converter": "org.apache.kafka.connect.storage.StringConverter",
      "errors.log.enable": "true",
      "topics": "topic1,topic2",
      "value.converter.schemas.enable": "false",
      "errors.tolerance": "none"
      }
}
```

### Standalone mode

Create a configuration file, for example `<kafka_dir>/config/SF_connect.properties`.
Populate the file with all connector
configuration information.

**Sample configuration file**

```properties
connector.class=com.snowflake.kafka.connector.SnowflakeStreamingSinkConnector
tasks.max=1
snowflake.topic2table.map=topic1:table_1,topic2:table_2
snowflake.url.name=myorganization-myaccount.snowflakecomputing.com:443
snowflake.warehouse.name=WH
snowflake.private.key=-----BEGIN PRIVATE KEY-----\n .... \n-----END PRIVATE KEY-----\n
snowflake.schema.name=MY_SCHEMA
snowflake.database.name=MY_DATABASE
snowflake.role.name=MY_ROLE
snowflake.user.name=MY_USER
value.converter=org.apache.kafka.connect.json.JsonConverter
key.converter=org.apache.kafka.connect.storage.StringConverter
errors.log.enable=true
topics=topic1,topic2
name=XYZCompanySensorData
value.converter.schemas.enable=false
errors.tolerance=none
```

## Cache considerations for testing and prototyping

The connector caches table and pipe lookup checks to improve performance during partition rebalances.
However, during testing and prototyping, this caching behavior can cause the connector
to not immediately detect manually created tables or pipes.

**Issue:** When you manually create a table or pipe while the connector is running,
the connector may continue to use cached existence check results (which may indicate the object doesn’t exist) for up to 5 minutes by default. This can lead to unexpected errors or behavior during testing.

**Recommendation for testing:** To avoid cache-related issues during testing and prototyping,
configure both cache expiration parameters to their minimum value of `1` millisecond or disable the caching:

```properties
snowflake.cache.table.exists.expire.ms=1
snowflake.cache.pipe.exists.expire.ms=1
```

This configuration ensures that the connector performs fresh existence checks on every partition rebalance, allowing you to see the effects of manually created tables and pipes immediately.

> **Important:**
>
> These minimal cache settings are recommended **only for testing and prototyping**. In production environments, use the default cache expiration values (5 minutes or greater) to minimize metadata queries to Snowflake and improve rebalance performance, especially when handling many partitions.

## Connector configuration properties

### Required properties

`name`
:   Application name. This must be unique across all Kafka connectors used by the customer. This name must be a valid Snowflake unquoted identifier. For information about valid identifiers, see [Identifier requirements](../../sql-reference/identifiers-syntax.md).

`connector.class`
:   `com.snowflake.kafka.connector.SnowflakeStreamingSinkConnector`

`topics`
:   Comma-separated list of topics. By default, Snowflake assumes that the table name is the same as the topic name. If the table name is not the same as the topic name, then use the optional `topic2table.map` parameter (below) to specify the mapping from topic name to table name. This table name must be a valid Snowflake unquoted identifier. For information about valid table names, see [Identifier requirements](../../sql-reference/identifiers-syntax.md).

    > **Note:**
    >
    > Either `topics` or `topics.regex` is required; not both.

`topics.regex`
:   This is a regular expression (“regex”) that specifies the topics that contain the messages to load into Snowflake tables. The connector loads data from any topic name that matches the regex. The regex must follow the rules for Java regular expressions (i.e. be compatible with java.util.regex.Pattern). The configuration file should contain either `topics` or `topics.regex`, not both.

`snowflake.url.name`
:   The URL for accessing your Snowflake account. This URL must include your [account identifier](../../user-guide/admin-account-identifier.md). Note that the protocol (`https://`) and port number are optional.

`snowflake.user.name`
:   User login name for the Snowflake account.

`snowflake.role.name`
:   The name of the role that the connector will use to insert data into the table.

`snowflake.private.key`
:   The private key to authenticate the user. Include only the key, not the header or footer. If the key is split across multiple lines, remove the line breaks. You can provide an unencrypted key, or you can provide an encrypted key and provide the `snowflake.private.key.passphrase` parameter to enable Snowflake to decrypt the key. Use this parameter if and only if the `snowflake.private.key` parameter value is encrypted. This decrypts private keys that were encrypted according to the instructions in [Key-pair authentication and key-pair rotation](../../user-guide/key-pair-auth.md).

    > **Note:**
    >
    > Also see `snowflake.private.key.passphrase` in Optional properties.

`snowflake.database.name`
:   The name of the database that contains the table to insert rows into.

`snowflake.schema.name`
:   The name of the schema that contains the table to insert rows into.

`header.converter`
:   Required only if the records are formatted in Avro and include a header. The value is `"org.apache.kafka.connect.storage.StringConverter"`.

`key.converter`
:   This is the Kafka record’s key converter (e.g. `"org.apache.kafka.connect.storage.StringConverter"`). This is not used by the Kafka connector, but is required by the Kafka Connect Platform.

    See [Kafka connector limitations](../../user-guide/kafka-connector-overview.md) for current limitations.

`value.converter`
:   The connector supports standard Kafka community converters. Choose the appropriate converter based on your data format:

    * For JSON records: `"org.apache.kafka.connect.json.JsonConverter"`
    * For Avro records with Schema Registry: `"io.confluent.connect.avro.AvroConverter"`

    See [Kafka connector limitations](../../user-guide/kafka-connector-overview.md) for current limitations.

### Optional properties

`snowflake.private.key.passphrase`
:   If the value of this parameter is not empty, the connector uses this phrase to try to decrypt the private key.

`tasks.max`
:   Number of tasks, usually the same as the number of CPU cores across the worker nodes in the Kafka Connect cluster. To achieve best performance, Snowflake recommends setting the number of tasks equal to the total number of Kafka partitions, but not exceeding the number of CPU cores. High number of tasks may result in an increased memory consumption and frequent rebalances.

`snowflake.topic2table.map`
:   This optional parameter lets a user specify which topics should be mapped to which tables. Each topic and its table name should be separated by a colon (see example below). This table name must be a valid Snowflake unquoted identifier. For information about valid table names, see [Identifier requirements](../../sql-reference/identifiers-syntax.md). The topic configuration allows use of regular expressions to define topics, just as the use of `topics.regex` does. The regular expressions cannot be ambiguous — any matched topic must match only a single target table.

    Example:

    ```none
    topics="topic1,topic2,topic5,topic6"
    snowflake.topic2table.map="topic1:low_range,topic2:low_range,topic5:high_range,topic6:high_range"
    ```

    could be written as:

    ```none
    topics.regex="topic[0-9]"
    snowflake.topic2table.map="topic[0-4]:low_range,topic[5-9]:high_range"
    ```

`value.converter.schema.registry.url`
:   If the format is Avro and you are using a Schema Registry Service, this should be the URL of the Schema Registry Service. Otherwise this field should be empty.

`value.converter.break.on.schema.registry.error`
:   If loading Avro data from the Schema Registry Service, this property determines if the Kafka connector should stop consuming records if it encounters an error while fetching the schema id. The default value is `false`. Set the value to `true` to enable this behavior.

`jvm.proxy.host`
:   To enable the Snowflake Kafka Connector to access Snowflake through a proxy server, set this parameter to specify the host of that proxy server.

`jvm.proxy.port`
:   To enable the Snowflake Kafka Connector to access Snowflake through a proxy server, set this parameter to specify the port of that proxy server.

`snowflake.streaming.max.client.lag`
:   Specifies how often the connector flushes the data to Snowflake, in seconds.

    Values:
    :   * Minimum: `1` second
        * Maximum: `600` seconds

    Default:
    :   `1` second

`jvm.proxy.username`
:   Username that authenticates with the proxy server.

`jvm.proxy.password`
:   Password for the username that authenticates with the proxy server.

`snowflake.jdbc.map`
:   Example: `"snowflake.jdbc.map": "networkTimeout:20,tracing:WARNING"`

    Additional JDBC properties (see [JDBC Driver connection parameter reference](../../developer-guide/jdbc/jdbc-parameters.md)) are not validated. These additional properties
    are not validated, and must not override nor be used instead of required properties such as: `jvm.proxy.xxx`,
    `snowflake.user.name`, `snowflake.private.key`, `snowflake.schema.name` etc.

    Specifying either of the following combinations:
    :   * `tracing` property along with `JDBC_TRACE` env variable
        * `database` property along with `snowflake.database.name`

    Will result in an ambiguous behavior and the behavior will be determined by the JDBC Driver.

`value.converter.basic.auth.credentials.source`
:   If you are using the Avro data format and require secure access to the Kafka schema registry, set this parameter to the string “USER_INFO”, and set the `value.converter.basic.auth.user.info` parameter described below. Otherwise, omit this parameter.

`value.converter.basic.auth.user.info`
:   If you are using the Avro data format and require secure access to the Kafka schema registry, set this parameter to the string “<user_ID>:<password>”, and set the value.converter.basic.auth.credentials.source parameter described above. Otherwise, omit this parameter.

`snowflake.metadata.createtime`
:   If value is set to FALSE, the `CreateTime` property value is omitted from the metadata in the RECORD_METADATA column. The default value is TRUE.

`snowflake.metadata.topic`
:   If value is set to FALSE, the `topic` property value is omitted from the metadata in the RECORD_METADATA column. The default value is TRUE.

`snowflake.metadata.offset.and.partition`
:   If value is set to FALSE, the `Offset` and `Partition` property values are omitted from the metadata in the RECORD_METADATA column. The default value is TRUE.

`snowflake.metadata.all`
:   If value is set to FALSE, the metadata in the RECORD_METADATA column is completely empty. The default value is TRUE.

`transforms`
:   Specify to skip tombstone records encountered by the Kafka connector and not load them into the target table. A tombstone record is
    defined as a record where the entire value field is null.

    Set the property value to `"tombstoneHandlerExample"`.

    > **Note:**
    >
    > Use this property with the Kafka community converters (i.e. `value.converter` property value) only (e.g.
    > `org.apache.kafka.connect.json.JsonConverter` or `org.apache.kafka.connect.json.AvroConverter`). To manage tombstone record
    > handling with the Snowflake converters, use the `behavior.on.null.values` property instead.

`transforms.tombstoneHandlerExample.type`
:   Required when setting the `transforms` property.

    Set the property value to `"io.confluent.connect.transforms.TombstoneHandler"`

`behavior.on.null.values`
:   Specify how the Kafka connector should handle tombstone records. A tombstone record is defined as a record where the entire value field
    is null. For [Snowpipe](../../user-guide/data-load-snowpipe-intro.md), this property is supported by the Kafka connector version 1.5.5 and later. For [Snowpipe Streaming](../../user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview.md), this property is supported by the Kafka connector version 2.1.0 and later.

    This property supports the following values:

    `DEFAULT`
    :   When the Kafka connector encounters a tombstone record, it inserts an empty JSON string in the content column.

    `IGNORE`
    :   The Kafka connector skips tombstone records and does not insert rows for these records.

    The default value is `DEFAULT`.

    > **Note:**
    >
    > Tombstone records ingestion varies by the ingestion methods:
    >
    > * For Snowpipe, the Kafka connector uses Snowflake converters only. To manage tombstone record handling with the Kafka community converters, use the `transform` and `transforms.tombstoneHandlerExample.type` properties instead.
    > * For Snowpipe Streaming, the Kafka connector uses community converters only.
    >
    > Records sent to Kafka brokers must not be NULL because these records will be dropped by the Kafka connector resulting in missing offsets. The missing offsets will break the Kafka connector in specific use cases. It is recommended that you use tombstone records instead of NULL records.

### Using key pair authentication and key rotation

The Kafka connector relies on key pair authentication instead of username and password authentication.
This authentication method requires a 2048-bit (minimum) RSA key pair.
Generate the public-private key pair using OpenSSL.
The public key is assigned to the Snowflake user defined in the configuration file.

After completing the key pair authentication tasks on this page and the tasks for [key pair rotation](../../user-guide/key-pair-auth.md),
evaluate the recommendation for Externalizing secrets, later in this topic.

To configure the public/private key pair:

1. From the command line in a terminal window, generate a private key.

   You can generate either an encrypted version or unencrypted version of the private key.

   > **Note:**
   >
   > The Kafka connector supports encryption algorithms that are validated to meet the Federal Information Processing Standard (140-2) (i.e. FIPS 140-2) requirements. For more information, see [FIPS 140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final).

   To generate an unencrypted version, use the following command:

   > ```bash
   > openssl genrsa -out rsa_key.pem 2048
   > ```

   To generate an encrypted version, use the following command:

   > ```bash
   > openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 <algorithm> -inform PEM -out rsa_key.p8
   > ```
   >
   > Where `<algorithm>` is a FIPS 140-2 compliant encryption algorithm.
   >
   > For example, to specify AES 256 as the encryption algorithm:
   >
   > ```bash
   > openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 aes256 -inform PEM -out rsa_key.p8
   > ```
   >
   > If you generate an encrypted version of the private key, record the passphrase.
   > Later, you will specify the passphrase in the `snowflake.private.key.passphrase` property in the Kafka configuration file.

   **Sample PEM private key**

   ```bash
   -----BEGIN ENCRYPTED PRIVATE KEY-----
   MIIE6TAbBgkqhkiG9w0BBQMwDgQILYPyCppzOwECAggABIIEyLiGSpeeGSe3xHP1
   wHLjfCYycUPennlX2bd8yX8xOxGSGfvB+99+PmSlex0FmY9ov1J8H1H9Y3lMWXbL
   ...
   -----END ENCRYPTED PRIVATE KEY-----
   ```

2. From the command line, generate the public key by referencing the private key:

   Assuming the private key is encrypted and contained in the file named `rsa_key.p8`, use the following command:

   ```bash
   openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
   ```

   **Sample PEM public key**

   ```bash
   -----BEGIN PUBLIC KEY-----
   MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy+Fw2qv4Roud3l6tjPH4
   zxybHjmZ5rhtCz9jppCV8UTWvEXxa88IGRIHbJ/PwKW/mR8LXdfI7l/9vCMXX4mk
   ...
   -----END PUBLIC KEY-----
   ```

3. Copy the public and private key files to a local directory for storage.
   Note the path to the files.
   The private key is stored using the PKCS#8 (Public Key Cryptography Standards) format
   and is encrypted using the passphrase you specified in the previous step; however,
   the file should still be protected from unauthorized access using the file permission mechanism provided by your
   operating system. It is the users responsibility to secure the file when it is not in use.
4. Log into Snowflake. Assign the public key to the Snowflake user using [ALTER USER](../../sql-reference/sql/alter-user.md).

   For example:

   > ```sqlexample
   > ALTER USER jsmith SET RSA_PUBLIC_KEY='MIIBIjANBgkqh...';
   > ```

   > **Note:**
   > * Only security administrators (i.e. users with the SECURITYADMIN role) or higher can alter a user.
   > * Exclude the public key header and footer in the SQL statement.

   Verify the user’s public key fingerprint using [DESCRIBE USER](../../sql-reference/sql/desc-user.md):

   ```sqlexample
   DESC USER jsmith;
   +-------------------------------+-----------------------------------------------------+---------+-------------------------------------------------------------------------------+
   | property                      | value                                               | default | description                                                                   |
   |-------------------------------+-----------------------------------------------------+---------+-------------------------------------------------------------------------------|
   | NAME                          | JSMITH                                              | null    | Name                                                                          |
   ...
   ...
   | RSA_PUBLIC_KEY_FP             | SHA256:nvnONUsfiuycCLMXIEWG4eTp4FjhVUZQUQbNpbSHXiA= | null    | Fingerprint of user's RSA public key.                                         |
   | RSA_PUBLIC_KEY_2_FP           | null                                                | null    | Fingerprint of user's second RSA public key.                                  |
   +-------------------------------+-----------------------------------------------------+---------+-------------------------------------------------------------------------------+
   ```

   > **Note:**
   >
   > The `RSA_PUBLIC_KEY_2_FP` property is described in [Configuring key-pair rotation](../../user-guide/key-pair-auth.md).
5. Copy and paste the entire private key into the `snowflake.private.key` field in the configuration file. Save the file.

#### Externalizing secrets

Snowflake strongly recommends externalizing secrets such as the private key and storing
them in an encrypted form or in a key management service such as AWS Key Management Service (KMS),
Microsoft Azure Key Vault, or HashiCorp Vault.
This can be accomplished by using a `ConfigProvider` implementation on your Kafka Connect cluster.

For more information, see the Confluent description of this [service](https://docs.confluent.io/current/connect/security.html#externalizing-secrets).

## Starting the connector

Start Kafka using the instructions provided in the third-party Confluent or Apache Kafka documentation.
You can start the Kafka connector in either distributed mode or standalone mode. Instructions for each are shown below:

### Distributed mode

In a terminal window, execute the following command:

```bash
curl -X POST -H "Content-Type: application/json" --data @<path>/<config_file>.json http://localhost:8083/connectors
```

### Standalone mode

In a terminal window, execute the following command:

```bash
<kafka_dir>/bin/connect-standalone.sh <kafka_dir>/<path>/connect-standalone.properties <kafka_dir>/config/SF_connect.properties
```

> **Note:**
>
> A default installation of Apache Kafka or Confluent Kafka should already include the file `connect-standalone.properties`.)

## Next steps

[test the connector](test-connector.md).
