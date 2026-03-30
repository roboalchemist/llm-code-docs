# Source: https://docs.confluent.io/platform/current/installation/installing_cp/zip-tar.md

<a id="prod-kafka-cli-install"></a>

# Install Confluent Platform using ZIP and TAR Archives

This topic provides instructions for running Confluent Platform locally or running a production-ready Confluent Platform configuration in a multi-node environment.

With the production-ready installation method, you will connect to every node manually, download the archive, and run the Confluent Platform
installation commands.

## Prerequisites

- You must complete these steps for each node in your cluster.
- Before installing Confluent Platform, your environment must meet the prerequisites as described in
  [software and hardware requirements](../system-requirements.md#system-requirements).

## Software package and repository retention policy

To maintain security and performance, Confluent enforces a retention policy for unsupported package versions, including RPM, DEB, and ZIP/TAR archives.
Confluent removes packages and repository metadata for versions that reach end of life (EOL).

If your Confluent Ansible playbooks target an EOL version, deployments fail after Confluent removes the packages from the repositories.
Migrate to a supported release regularly to ensure continued access to installation files and security updates.

<a id="get-software"></a>

## Get the software

1. Go to the <a href="https://www.confluent.io/installation/" target="_blank">installation page</a>.
2. Select the **SELF-MANAGED** tab.
   You will be prompted to enter your name, company, email address, and country. When finished,
   click **Download Free**.
3. On the installation page, choose your package type (ZIP or TAR) and click **Download**, or
   download a package directly by using the `curl` command.

   Confluent Platform
   : - ZIP
       ```bash
       curl -O https://packages.confluent.io/archive/8.2/confluent-8.2.0.zip
       ```
     - TAR
       ```bash
       curl -O https://packages.confluent.io/archive/8.2/confluent-8.2.0.tar.gz
       ```

   Confluent Platform using only Confluent Community components
   : - ZIP
       ```bash
       curl -O https://packages.confluent.io/archive/8.2/confluent-community-8.2.0.zip
       ```
     - TAR
       ```bash
       curl -O https://packages.confluent.io/archive/8.2/confluent-community-8.2.0.tar.gz
       ```
4. Extract the contents of the archive. For ZIP files, run this command in a terminal.
   ```bash
   unzip confluent-8.2.0.zip
   ```

   For TAR files run this command:
   ```bash
   tar xzf confluent-8.2.0.tar.gz
   ```

   You should have these directories:
   <!-- tarball_contents -->

   | Folder    | Description                                          |
   |-----------|------------------------------------------------------|
   | /bin/     | Driver scripts for starting and stopping services    |
   | /etc/     | Configuration files                                  |
   | /lib/     | Systemd services                                     |
   | /libexec/ | Multi-platform CLI binaries                          |
   | /share/   | Jars and licenses                                    |
   | /src/     | Source files that require a platform-dependent build |

<a id="configure-confluent-home"></a>

## Configure CONFLUENT_HOME and PATH

To more easily use the Confluent CLI and all of the [command-line tools that are provided with Confluent Platform](../../tools/cli-reference.md#cp-all-cli), you can optionally configure the `CONFLUENT_HOME`
variable and add the Confluent Platform `\bin` folder to your `PATH`.
Then you can use the CLI tools without navigating to the `CONFLUENT_HOME` directory.

1. Set the environment variable for the Confluent Platform home directory. This is the directory where
   Confluent Platform is installed. For example:
   ```bash
   export CONFLUENT_HOME=~/confluent-8.2.0
   ```
2. Add the Confluent Platform `bin` directory to your `PATH`
   ```bash
   export PATH=$PATH:$CONFLUENT_HOME/bin
   ```
3. Test that you set the `CONFLUENT_HOME` variable correctly by running the `confluent` command:
   ```bash
   confluent --help
   ```

   Your output should show the available commands for managing Confluent Platform.

<a id="config-cp-for-production"></a>

## Configure Confluent Platform for production

Configure Confluent Platform with the individual component properties files. By default these are located in `CONFLUENT_HOME/etc/`.
You must minimally configure the following components.

<!-- kafka -->

### Kafka

For Kafka in KRaft mode, you must configure a node to be a broker or a controller.
In addition, you must create a unique cluster ID and format the log directories with that ID.

Typically in a production environment, you should have a minimum of three brokers and three controllers.

* Navigate to the KRaft configuration files located in the  `/etc/kafka/` directory. In this directory, you will find three sample property files for different node roles:
  - `broker.properties`: Use this file to configure a broker node.
  - `controller.properties`: Use this file to configure a controller node.
  - `server.properties`: Use this file to configure a node that runs in combined mode as both a broker and a controller. This mode is not supported for production environments.

  Choose the appropriate properties file for the nodeâs role in your KRaft cluster and then customize the settings in that file.
* Configure the `process.roles`, `node.id` and `controller.quorum.voters` for each node.
  - For `process.roles`, set whether the node will be a `broker` or a `controller`. `combined` mode, meaning `process.roles` is set to
    `broker,controller`, is currently not supported and should only be used for experimentation.
  - Set a system-wide unique ID for the `node.id` for each broker/controller.
  - `controller.quorum.voters` should be a comma-separated list of controllers in the format `nodeID@hostname:port`
    ```bash
    ############################# Server Basics #############################

    # The role of this server. Setting this puts us in KRaft mode
    process.roles=broker

    # The node id associated with this instance's roles
    node.id=2

    # The connect string for the controller quorum
    controller.quorum.voters=1@controller1:9093,3@controller3:9093,5@controller5:9093
    ```
* Configure how brokers and clients communicate with the broker using `listeners`, and where controllers listen with
  `controller.listener.names`.
  - `listeners`: Comma-separated list of URIs and listener names to listen on in the format `listener_name://host_name:port`
  - `controller.listener.names`: Comma-separated list of `listener_name` entries for listeners used by the controller.

  For more information, see [KRaft Configuration for Confluent Platform](../../kafka-metadata/config-kraft.md#configure-kraft).
* Configure security for your environment.
  - For general security guidance, see [KRaft Security in Confluent Platform](../../security/component/kraft-security.md#kraft-security).
  - For role-based access control (RBAC), see [Configure Metadata Service (MDS) in Confluent Platform](../../kafka/configure-mds/index.md#rbac-mds-config).
  - For configuring SASL/SCRAM for broker-to-broker communication, see [KRaft-based Confluent Platform clusters](../../security/authentication/sasl/scram/overview.md#sasl-scram-kraft-based-clusters).

#### Schema Registry

<!-- configuration Schema Registry -->

Navigate to the Schema Registry properties file (`/etc/schema-registry/schema-registry.properties`)
and specify the following properties:

```none
# Specify the address the socket server listens on, e.g. listeners = PLAINTEXT://your.host.name:9092
listeners=http://0.0.0.0:8081

# The advertised host name. This must be specified if you are running Schema Registry
# with multiple nodes.
host.name=192.168.50.1

# List of Kafka brokers to connect to, e.g. PLAINTEXT://hostname:9092,SSL://hostname2:9092
kafkastore.bootstrap.servers=PLAINTEXT://hostname:9092,SSL://hostname2:9092
```

This configuration is for a three node multi-node cluster. For more information, see [Deploy Schema Registry in Production on Confluent Platform](../../schema-registry/installation/deployment.md#schema-registry-prod).

<a id="start-cp-command-line"></a>

#### REST Proxy

If you are using a Confluent Enterprise license, navigate to the REST Proxy properties file (`/etc/kafka-rest/rest-proxy.properties`)
and specify the following property:

```bash
kafka.rest.resource.extension.class=io.confluent.kafkarest.security.KafkaRestSecurityResourceExtension
```

<a id="start-c3-zip"></a>

## Start Confluent Platform

To start Confluent Platform, make sure you have configured [CONFLUENT_HOME](#configure-confluent-home) and then use
the following Kafka CLI commands. In addition, you must format the log directories with a unique cluster ID before
you start Confluent Platform.

You should start your KRaft controllers first, then Kafka brokers, and then Schema Registry must be started before any other components.

1. Before you start Kafka, you must use the [kafka-storage](/kafka/operations-tools/kafka-tools.html#kafka-storage-sh) tool with the `random-uuid` command
   to generate a cluster ID for each new cluster. You only need one cluster ID, which you will use to format
   each node in the cluster.
   ```none
   bin/kafka-storage random-uuid
   ```

   This results in output like the following:
   ```none
   q1Sh-9_ISia_zwGINzRvyQ
   ```

   Then use the cluster ID to format storage for each node in the cluster with the `kafka-storage` tool that is provided with Confluent Platform,
   and the `format` command like the following example, specifying the properties file for a controller.
   ```none
   bin/kafka-storage format -t q1Sh-9_ISia_zwGINzRvyQ -c etc/kafka/controller.properties
   ```

   Previously, Kafka would format blank storage directories automatically and generate a new cluster ID automatically.
   One reason for the change is that auto-formatting can sometimes obscure an
   error condition. This is particularly important for the metadata log maintained by the controller and broker servers.
   If a majority of the controllers were able to start with an empty log directory, a leader might be able to be elected with
   missing committed data. To configure the log directory, either set `metadata.log.dir` or `log.dirs`. For more
   information, see [Inter-broker listeners](../../kafka-metadata/config-kraft.md#kraft-log-settings).
2. Start a Kafka controller. Run this command in its own terminal.
   ```bash
   kafka-server-start $CONFLUENT_HOME/etc/kafka/controller.properties
   ```
3. Start a Kafka broker.
   ```bash
   kafka-server-start $CONFLUENT_HOME/etc/kafka/broker.properties
   ```
4. Start Schema Registry. Run this command in its own terminal.
   ```bash
   schema-registry-start $CONFLUENT_HOME/etc/schema-registry/schema-registry.properties
   ```

   - Kafka Connect
     ```bash
     connect-distributed $CONFLUENT_HOME/etc/schema-registry/connect-avro-distributed.properties
     ```
   - Confluent REST Proxy
     ```bash
     kafka-rest-start $CONFLUENT_HOME/etc/kafka-rest/kafka-rest.properties
     ```
   - ksqlDB
     ```bash
     ksql-server-start $CONFLUENT_HOME/etc/ksqldb/ksql-server.properties
     ```

## Uninstall

1. Remove the Confluent directory. For example, if you have Confluent Platform 8.2.0 installed:
   ```bash
   rm -rf $CONFLUENT_HOME
   ```
2. Remove the Confluent Platform data files.
   ```bash
   rm -rf /var/lib/<confluent-platform-data-files>
   ```

## Related content

- [Install Control Center](/control-center/current/installation/overview.html)
- [Confluent Platform and Apache Kafka compatibility](../versions-interoperability.md#cp-ak-compatibility)
- [Quick Start for Confluent Platform](../../get-started/platform-quickstart.md#quickstart).
- [Use Confluent Platform systemd Service Unit Files](scripted-install.md#installing-systemd-unit)
