# Source: https://docs.confluent.io/platform/current/get-started/platform-quickstart.md

<a id="quickstart"></a>

# Quick Start for Confluent Platform

Confluent Platform is a data-streaming platform that completes Kafka with advanced capabilities designed to help accelerate
application development and connectivity for enterprise use cases.

This quick start will help you get up and running locally with Confluent Platform and its main components
using either Docker containers or ZIP/TAR archives. For production installation methods, see [Install Confluent Platform On-Premises](../installation/overview.md#installation).
In this quick start, you create Apache KafkaÂ® topics, use Kafka Connect to generate mock data to those topics,
and use Confluent Control Center to view your data.

<a id="qs-prereq"></a>

## Prerequisites

Prerequisites vary based on your installation method. Choose your preferred method below.

### Docker

To run this quick start using Docker, you need Git, Docker, and Docker Compose installed on a computer
with a supported [Operating System](../installation/versions-interoperability.md#operating-systems). Make sure Docker is running.

### **Detailed prerequisites**

- A connection to the internet.
- [Operating System](../installation/versions-interoperability.md#operating-systems) currently supported by Confluent Platform.

  #### NOTE
  You can run the Confluent Platform Quick Start on Windows if you are running Docker Desktop for Windows on WSL 2.
  For more information, see [How to Run Confluent on Windows in Minutes](https://www.confluent.io/blog/set-up-and-run-kafka-on-windows-and-wsl-2/).
- Docker version 1.11 or later is [installed and running](https://docs.docker.com/engine/installation/).
- **On Mac:** Docker memory is allocated minimally at 6 GB (Mac).
  When using Docker Desktop for Mac, the default Docker memory
  allocation is 2 GB. Change the default allocation to 6 GB in the
  Docker Desktop app by navigating to **Preferences** > **Resources** > **Advanced**.

### ZIP/TAR

To run this quick start using ZIP/TAR archives, you need the following:

- A connection to the internet.
- [Operating System](../installation/versions-interoperability.md#operating-systems) currently supported by Confluent Platform.
- Java 21 or Java 17 installed.

#### NOTE
The `confluent local` commands are intended for single-node development environments
and are not suitable for production. For production deployments, see [Install and Upgrade Confluent Platform](../installation/index.md#installation-overview).

<a id="cp-quickstart-step-1"></a>

## Step 1: Download and start Confluent Platform

Choose your preferred installation method using the tabs below.

### Docker

In this step, you start by cloning a GitHub repository. This repository contains a Docker compose file and some required configuration files.
The `docker-compose.yml` file sets ports and Docker environment variables such as the replication factor and listener properties
for Confluent Platform and its components. To learn more about the settings in this file, see [Docker Image Configuration Reference for Confluent Platform](../installation/docker/config-reference.md#config-reference).

1. Clone the [Confluent Platform all-in-one example repository](https://github.com/confluentinc/cp-all-in-one/tree/latest/cp-all-in-one),
   for example:
   ```bash
   git clone https://github.com/confluentinc/cp-all-in-one.git
   ```
2. Change to the cloned repositoryâs root directory:
   ```bash
   cd cp-all-in-one
   ```
3. The default branch may not be the latest. Check out the branch for the version you want to run, for example, 8.2.0-post:
   ```bash
   git checkout 8.2.0-post
   ```
4. The `docker-compose.yml` file is located in a nested directory. Navigate into the following directory:
   ```bash
   cd cp-all-in-one
   ```
5. Start the Confluent Platform stack with the `-d` option to run in detached mode:
   ```bash
   docker compose up -d
   ```

   #### NOTE
   If you are using Docker Compose V1, you need to use a
   dash in the `docker compose` commands. For example:
   ```bash
   docker-compose up -d
   ```

   To learn more, see [Migrate to Compose V2](https://docs.docker.com/compose/releases/migrate/).

   Each Confluent Platform component starts in a separate container. Your output should
   resemble the following.  Your output may vary slightly from these
   examples depending on your operating system.
   ```bash
   â Network cp-all-in-one_default  Created       0.0s
   â Container prometheus           Started       0.7s
   â Container broker               Started       0.7s
   â Container flink-jobmanager     Started       0.7s
   â Container flink-sql-client     Started       0.7s
   â Container flink-taskmanager    Started       0.7s
   â Container alertmanager         Started       0.7s
   â Container schema-registry      Started       0.7s
   â Container connect              Started       0.7s
   â Container rest-proxy           Started       0.7s
   â Container ksqldb-server        Started       0.7s
   â Container control-center       Started       0.8s
   ```
6. Verify that the services are up and running:
   ```bash
   docker compose ps
   ```

   Your output should resemble:
   ```none
   NAME                IMAGE                                                       COMMAND                  SERVICE             CREATED         STATUS         PORTS
   alertmanager        confluentinc/cp-enterprise-alertmanager:2.2.1               "alertmanager-start"     alertmanager        3 minutes ago   Up 3 minutes   0.0.0.0:9093->9093/tcp, [::]:9093->9093/tcp
   broker              confluentinc/cp-server:8.2.0                                "/etc/confluent/dockâ¦"   broker              3 minutes ago   Up 3 minutes   0.0.0.0:9092->9092/tcp, [::]:9092->9092/tcp, 0.0.0.0:9101->9101/tcp, [::]:9101->9101/tcp
   connect             cnfldemos/cp-server-connect-datagen:0.6.4-7.6.0             "/etc/confluent/dockâ¦"   connect             3 minutes ago   Up 3 minutes   0.0.0.0:8083->8083/tcp, [::]:8083->8083/tcp
   control-center      confluentinc/cp-enterprise-control-center-next-gen:2.2.1    "/etc/confluent/dockâ¦"   control-center      3 minutes ago   Up 3 minutes   0.0.0.0:9021->9021/tcp, [::]:9021->9021/tcp
   flink-jobmanager    cnfldemos/flink-kafka:1.19.1-scala_2.12-java17              "/docker-entrypoint.â¦"   flink-jobmanager    3 minutes ago   Up 3 minutes   0.0.0.0:9081->9081/tcp, [::]:9081->9081/tcp
   flink-sql-client    cnfldemos/flink-sql-client-kafka:1.19.1-scala_2.12-java17   "/docker-entrypoint.â¦"   flink-sql-client    3 minutes ago   Up 3 minutes   6123/tcp, 8081/tcp
   flink-taskmanager   cnfldemos/flink-kafka:1.19.1-scala_2.12-java17              "/docker-entrypoint.â¦"   flink-taskmanager   3 minutes ago   Up 3 minutes   6123/tcp, 8081/tcp
   ksqldb-server       confluentinc/cp-ksqldb-server:8.2.0                         "/etc/confluent/dockâ¦"   ksqldb-server       3 minutes ago   Up 3 minutes   0.0.0.0:8088->8088/tcp, [::]:8088->8088/tcp
   prometheus          confluentinc/cp-enterprise-prometheus:2.2.1                 "prometheus-start"       prometheus          3 minutes ago   Up 3 minutes   0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp
   rest-proxy          confluentinc/cp-kafka-rest:8.2.0                            "/etc/confluent/dockâ¦"   rest-proxy          3 minutes ago   Up 3 minutes   0.0.0.0:8082->8082/tcp, [::]:8082->8082/tcp
   schema-registry     confluentinc/cp-schema-registry:8.2.0                       "/etc/confluent/dockâ¦"   schema-registry     3 minutes ago   Up 3 minutes   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp
   ```

   After a few minutes, if the state of any component isnât **Up**, run the
   `docker compose up -d` command again, or try `docker compose restart <image-name>`,
   for example:
   ```bash
   docker compose restart control-center
   ```

### ZIP/TAR

In the next few steps, you download and extract Confluent Platform, then use the Confluent CLI to start Confluent Platform services
locally in KRaft mode. This method starts the core Confluent Platform components including a KRaft controller,
broker, Schema Registry, REST Proxy, Connect, and ksqlDB. You download and start Control Center separately.

#### IMPORTANT
The Confluent CLI [confluent local](https://docs.confluent.io/confluent-cli/current/command-reference/local/index.html) commands are intended for a single-node development environment and
are not suitable for a production environment. The data that are produced are transient and are intended to be
temporary. For production-ready workflows, see [Install and Upgrade Confluent Platform](../installation/index.md#installation-overview).

1. Download the Confluent Platform TAR archive and extract it:
   ```bash
   curl -O https://packages.confluent.io/archive/8.2/confluent-8.2.0.tar.gz
   ```

   ```bash
   tar -xvf confluent-8.2.0.tar.gz
   ```

   ```bash
   cd confluent-8.2.0
   ```

   ```bash
   export CONFLUENT_HOME=`pwd`
   ```
2. Add the Confluent Platform `bin` directory to your PATH:
   ```bash
   export PATH=$PATH:$CONFLUENT_HOME/bin
   ```
3. Install the Connect Datagen source connector using the Confluent Marketplace client.
   This connector generates mock data for demonstration purposes and is not suitable
   for production. For more connectors, see [Confluent Hub](https://www.confluent.io/hub).
   ```bash
   confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:latest
   ```
4. Start all Confluent Platform services:
   ```bash
   confluent local services start
   ```

   Every service starts in order, printing a message with its status:
   ```bash
   Starting KRaft Controller
   KRaft Controller is [UP]
   Starting Kafka
   Kafka is [UP]
   Starting Schema Registry
   Schema Registry is [UP]
   Starting Kafka REST
   Kafka REST is [UP]
   Starting Connect
   Connect is [UP]
   Starting ksqlDB Server
   ksqlDB Server is [UP]
   ```
5. Verify that the services are running:
   ```bash
   confluent local services status
   ```

   Now, install and configure Control Center to work with your local Confluent Platform installation.
   As of Confluent Platform 8.0, Confluent Control Center is installed and runs separately from Confluent Platform. Follow these steps to
   install and configure Control Center to work with your local Confluent Platform installation.
   Installing Control Center requires three additional terminal windows for Prometheus,
   Alert Manager, and Control Center.
6. Start a new terminal window, then download and extract Control Center.
   ```bash
   curl -O https://packages.confluent.io/confluent-control-center-next-gen/archive/confluent-control-center-next-gen-2.3.1.tar.gz
   ```

   ```bash
   tar -xvf confluent-control-center-next-gen-2.3.1.tar.gz
   ```

   ```bash
   cd confluent-control-center-next-gen-2.3.1
   ```
7. Set the `CONTROL_CENTER_HOME` environment variable:
   ```bash
   export CONTROL_CENTER_HOME=`pwd`
   ```
8. Configure Prometheus to connect to Alert Manager on a non-default port.

   By default, Alert Manager and the KRaft controller (started in step 3) both use port
   9093. To avoid a conflict, you must configure Alert Manager to use port 9098.

   Edit `etc/confluent-control-center/prometheus-generated.yml`,
   locate the `alertmanagers` section, and change the target port from 9093 to 9098.
   ```yaml
   alerting:
     alertmanagers:
     - static_configs:
       - targets:
         - localhost:9098
   ```
9. In the same terminal window or a new one, start Prometheus. If Prometheus starts successfully, you will not see any output.
   - On Linux or Windows:
     ```bash
     bin/prometheus-start
     ```
   - On macOS:
     ```bash
     bash bin/prometheus-start
     ```
10. In a new terminal window, navigate to the Control Center directory and start Alert Manager. If Alert Manager starts successfully, you will not see any output.
    1. Navigate to the directory and set the home variable:
       ```bash
       cd confluent-control-center-next-gen-2.3.1
       ```

       ```bash
       export CONTROL_CENTER_HOME=`pwd`
       ```
    2. Start Alert Manager using the `ALERTMANAGER_PORT` environment variable to avoid the port conflict:
       - On Linux or Windows:

       ```bash
       export ALERTMANAGER_PORT=9098
       bin/alertmanager-start
       ```

       - On macOS:

       ```bash
       export ALERTMANAGER_PORT=9098
       bash bin/alertmanager-start
       ```
11. In another new terminal window, start Control Center:
    1. Navigate to the Control Center directory:
       ```bash
       cd confluent-control-center-next-gen-2.3.1
       ```
    2. Set the home variable:
       ```bash
       export CONTROL_CENTER_HOME=`pwd`
       ```
    3. Configure Control Center to connect to Alert Manager on the new port. Edit
       `$CONTROL_CENTER_HOME/etc/confluent-control-center/control-center-dev.properties`
       and uncomment or add the following line:
       ```properties
       confluent.controlcenter.alertmanager.url=http://localhost:9098
       ```
    4. Run the start script with your updated properties file:
       ```bash
       ./bin/control-center-start $CONTROL_CENTER_HOME/etc/confluent-control-center/control-center-dev.properties
       ```
12. Open Control Center in your browser at [http://localhost:9021](http://localhost:9021).
    It may take a few minutes for Control Center to start and load.

For more details on Control Center installation, see [Control Center Installation](/control-center/current/installation/overview.html#archive).

<a id="cp-quickstart-step-2"></a>

## Step 2: Create Kafka topics for storing your data

In Confluent Platform, real-time streaming events are stored in a [topic](../_glossary.md#term-topic), which is
an append-only log, and the fundamental unit of organization for Kafka.
To learn more about Kafka basics, see [Kafka Introduction](/kafka/introduction.html).

In this step, you create two topics by using [Control Center for Confluent Platform](https://docs.confluent.io/control-center/current/overview.html). Control Center
provides the features for building and monitoring production data pipelines
and [event streaming](../_glossary.md#term-event-streaming) applications.

The topics are named `pageviews` and `users`. In later steps, you create
connectors that produce data to these topics.

### Create the pageviews topic

Confluent Control Center enables creating topics in the UI with a few clicks.

1. Navigate to Control Center at [http://localhost:9021](http://localhost:9021).
   It takes a few minutes for Control Center to start and load. If needed, refresh
   your browser until it loads.
2. Click the **controlcenter.cluster** tile.
   ![The Cluster tile in Confluent Control Center](images/c3-landing-page.png)
3. In the navigation menu, click **Topics** to open the topics list. Click
   **+ Add topic** to start creating the `pageviews` topic.
   ![The Topics page in Confluent Control Center](images/c3-create-topic.png)
4. In the **Topic name** field, enter `pageviews` and click
   **Create with defaults**. Topic names *are* case-sensitive.
   ![Creating a Kafka topic in Confluent Control Center](images/c3-create-topic-name.png)

### Create the users topic

Repeat the previous steps to create the `users` topic.

1. In the navigation menu, click **Topics** to open the topics list. Click
   **+ Add topic** to start creating the `users` topic.
2. In the **Topic name** field, enter `users` and click
   **Create with defaults**.
3. You can optionally inspect a topic. On the **users** page, click **Configuration** to see details about the
   `users` topic.
   ![The Topic Configuration page in Confluent Control Center](images/c3-topic-config.png)

<a id="cp-quickstart-step-3"></a>

## Step 3: Generate mock data

In Confluent Platform, you get [events](../_glossary.md#term-event) from an external source by using [Kafka Connect](../connect/index.md#connect-concepts).
Connectors enable you to stream large volumes of data to and from your [Kafka cluster](../_glossary.md#term-Kafka-cluster). Confluent
publishes many connectors for integrating with external systems, like MongoDB
and Elasticsearch. For more information, see the [Kafka Connect Overview](../connect/index.md#kafka-connect) page.

In this step, you run the
[Datagen Source Connector](https://www.confluent.io/hub/confluentinc/kafka-connect-datagen)
to generate mock data. The mock data is stored in the `pageviews` and
`users` topics that you created previously. To learn more about installing connectors,
see [Install Self-Managed Connectors for Confluent Platform](../connect/install.md#connect-install-connectors).

1. In the navigation menu, click **Connect**.
2. Click the `connect-default` cluster in the **Connect clusters** list.
3. Click **Add connector** to start creating a connector for pageviews data.
4. Select the `DatagenConnector` tile.
5. In the **Name** field, enter `datagen-pageviews` as the name of the connector.
6. Enter the following configuration values in the following sections:

   **Common** section:
   - **Key converter class:** `org.apache.kafka.connect.storage.StringConverter`

   **General** section:
   - **kafka.topic:** Choose `pageviews` from the dropdown menu
   - **max.interval:** `100`
   - **quickstart:** `pageviews`
7. Click **Next** to review the connector configuration. When youâre satisfied
   with the settings, click **Launch**.
   ![Reviewing connector configuration in Confluent Control Center](images/connect-review-pageviews.png)

Run a second instance of the
[Datagen Source connector](https://www.confluent.io/hub/confluentinc/kafka-connect-datagen)
connector to produce mock data to the `users` topic.

1. In the navigation menu, click **Connect**.
2. In the **Connect clusters** list, click `connect-default`.
3. Click **Add connector**.
4. Select the `DatagenConnector` tile.
5. In the **Name** field, enter `datagen-users` as the name of the connector.
6. Enter the following configuration values:

   **Common** section:
   - **Key converter class:** `org.apache.kafka.connect.storage.StringConverter`

   **General** section:
   - **kafka.topic:** Choose `users` from the dropdown menu
   - **max.interval:** `1000`
   - **quickstart:** `users`
7. Click **Next** to review the connector configuration. When youâre satisfied
   with the settings, click **Launch**.
8. In the navigation menu, click **Topics** and in the list, click **users**.
9. Click **Messages** to confirm that the `datagen-users` connector is
   producing data to the `users` topic.
   ![Incoming messages displayed in the Topics page in Confluent Control Center](images/c3-topics-messages-users.gif)

### Inspect the schema of a topic

By default, the Datagen Source Connector produces data in Avro format, which
defines the schemas of `pageviews` and `users` messages.

Schema Registry ensures that messages sent to your cluster have the correct schema.
For more information, see [Schema Registry Documentation](/platform/current/schema-registry/index.html).

1. In the navigation menu, click **Topics**, and in the topic list, click
   **pageviews**.
2. Click **Schema** to inspect the Avro schema that applies to `pageviews`
   message values.

   Your output should resemble:
   ![image](images/qs-schema-ex.png)

<a id="cp-quickstart-step-4"></a>

<a id="cp-quickstart-step-6"></a>

## Step 4: Uninstall and clean up

When youâre done working with Confluent Platform, clean up using the method that matches your installation.

### Docker

Stop and remove the Docker containers and images.

1. Run the following command to stop the Docker containers for Confluent:
   ```bash
   docker compose stop
   ```
2. After stopping the Docker containers, run the following commands to
   prune the Docker system. Running these commands deletes containers,
   networks, volumes, and images, freeing up disk space:
   ```bash
   docker system prune -a --volumes --filter "label=io.confluent.docker"
   ```

   For more information, refer to the official [Docker](https://docs.docker.com/) documentation.

### ZIP/TAR

Stop all services and clean up the temporary data.

1. If you installed Control Center, stop it first by pressing `Ctrl+C` in the terminal
   windows running Control Center, Alert Manager, and Prometheus.
2. In the terminal window running Confluent services, stop all Confluent Platform services and delete the temporary data:
   ```bash
   confluent local services stop
   ```

   Your output should resemble:
   ```bash
   Stopping ksqlDB Server
   ksqlDB Server is [DOWN]
   Stopping Connect
   Connect is [DOWN]
   Stopping Kafka REST
   Kafka REST is [DOWN]
   Stopping Schema Registry
   Schema Registry is [DOWN]
   Stopping Kafka
   Kafka is [DOWN]
   Stopping KRaft Controller
   KRaft Controller is [DOWN]
   ```
3. To stop all services and delete all temporary data created during this quick start:
   ```bash
   confluent local destroy
   ```

   This removes all data stored in the temporary directory used by `confluent local`.

## Related content

- To download an automated version of this quick start, see [the Quick Start on GitHub](https://github.com/confluentinc/examples/tree/latest/cp-quickstart/README.md)
- To configure and run a multi-broker cluster without Docker, see [Tutorial: Set Up a Multi-Broker Kafka Cluster](tutorial-multi-broker.md#basics-multi-broker-setup)
- For alternative installation methods, you can use a [TAR or ZIP archive](../installation/installing_cp/zip-tar.md#prod-kafka-cli-install),
  or package managers like `systemd`, [Confluent for Kubernetes](https://docs.confluent.io/operator/current/overview.html),
  and [Ansible](https://docs.confluent.io/ansible/current/overview.html)
- To learn how to develop with Confluent Platform, see [Confluent Developer](https://developer.confluent.io/learn-kafka)
- To get started with Confluent Platform for Apache Flink in Confluent Control Center, see [Use Confluent Control Center with Confluent Manager for Apache Flink](/control-center/current/cmf.html)
- For training and certification guidance, including resources and access to hands-on
  training and certification exams, see [Confluent Education](https://www.confluent.io/training)
- To try out basic Kafka, Kafka Streams, and ksqlDB tutorials with step-by-step instructions, see [Kafka Tutorials](https://developer.confluent.io/tutorials/)
- To learn how to build stream processing applications in Java or Scala, see [Kafka Streams documentation](../streams/overview.md#kafka-streams)
- To learn how to read and write data to and from Kafka using programming
  languages such as Go, Python, .NET, C/C++, see [Kafka Clients documentation](../clients/overview.md#kafka-clients)
