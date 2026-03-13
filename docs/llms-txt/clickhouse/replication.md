# Source: https://clickhouse.ferndocs.com/reference/engines/table-engines/mergetree-family/replication.md

# Source: https://clickhouse.ferndocs.com/open-source/architecture/replication.md

---
slug: /architecture/replication
sidebar_label: Replication
sidebar_position: 10
title: Replicating data
description: >-
  Page describing an example architecture with five servers configured. Two are
  used to host copies of the data and the rest are used to coordinate the
  replication of data
doc_type: guide
keywords:
  - replication
  - high availability
  - cluster setup
  - data redundancy
  - fault tolerance
---


> In this example, you'll learn how to set up a simple ClickHouse cluster which
replicates the data. There are five servers configured. Two are used to host 
copies of the data. The other three servers are used to coordinate the replication
of data. 

The architecture of the cluster you will be setting up is shown below:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f92282aa39a9504a4f8b930fa36755c29204cec3272d31bd3ef7885e9b625369/images/deployment-guides/replication-sharding-examples/replication.png" alt="Architecture diagram for 1 shard and 2 replicas with ReplicatedMergeTree"/>

<Note>
Although it is possible to run ClickHouse Server and ClickHouse Keeper combined on the same server,
we strongly recommend using *dedicated* hosts for ClickHouse keeper in production environments,
which is the approach we will demonstrate in this example.

Keeper servers can be smaller, and 4GB RAM is generally enough for each Keeper server
until your ClickHouse Servers grow large.
</Note>

## Prerequisites [#pre-requisites]

- You've set up a [local ClickHouse server](/install) before
- You are familiar with basic configuration concepts of ClickHouse such as [configuration files](/operations/configuration-files)
- You have docker installed on your machine

<Steps level="h2">

## Set up directory structure and test environment [#set-up]

<Tip title="Example files">
The following steps will walk you through setting up the cluster from
scratch. If you prefer to skip these steps and jump straight to running the
cluster, you can obtain the example
files from the examples repository ['docker-compose-recipes' directory](https://github.com/ClickHouse/examples/tree/main/docker-compose-recipes/recipes).
</Tip>

In this tutorial, you will use [Docker compose](https://docs.docker.com/compose/) to
set up the ClickHouse cluster. This setup could be modified to work
for separate local machines, virtual machines or cloud instances as well.

Run the following commands to set up the directory structure for this example:

```bash
mkdir cluster_1S_2R
cd cluster_1S_2R

# Create clickhouse-keeper directories
for i in {01..03}; do
  mkdir -p fs/volumes/clickhouse-keeper-${i}/etc/clickhouse-keeper
done

# Create clickhouse-server directories
for i in {01..02}; do
  mkdir -p fs/volumes/clickhouse-${i}/etc/clickhouse-server
done
```

Add the following `docker-compose.yml` file to the `cluster_1S_2R` directory:

```yaml title="docker-compose.yml"
version: '3.8'
services:
  clickhouse-01:
    image: "clickhouse/clickhouse-server:latest"
    user: "101:101"
    container_name: clickhouse-01
    hostname: clickhouse-01
    volumes:
      - ${PWD}/fs/volumes/clickhouse-01/etc/clickhouse-server/config.d/config.xml:/etc/clickhouse-server/config.d/config.xml
      - ${PWD}/fs/volumes/clickhouse-01/etc/clickhouse-server/users.d/users.xml:/etc/clickhouse-server/users.d/users.xml
    ports:
      - "127.0.0.1:8123:8123"
      - "127.0.0.1:9000:9000"
    depends_on:
      - clickhouse-keeper-01
      - clickhouse-keeper-02
      - clickhouse-keeper-03
  clickhouse-02:
    image: "clickhouse/clickhouse-server:latest"
    user: "101:101"
    container_name: clickhouse-02
    hostname: clickhouse-02
    volumes:
      - ${PWD}/fs/volumes/clickhouse-02/etc/clickhouse-server/config.d/config.xml:/etc/clickhouse-server/config.d/config.xml
      - ${PWD}/fs/volumes/clickhouse-02/etc/clickhouse-server/users.d/users.xml:/etc/clickhouse-server/users.d/users.xml
    ports:
      - "127.0.0.1:8124:8123"
      - "127.0.0.1:9001:9000"
    depends_on:
      - clickhouse-keeper-01
      - clickhouse-keeper-02
      - clickhouse-keeper-03
  clickhouse-keeper-01:
    image: "clickhouse/clickhouse-keeper:latest-alpine"
    user: "101:101"
    container_name: clickhouse-keeper-01
    hostname: clickhouse-keeper-01
    volumes:
     - ${PWD}/fs/volumes/clickhouse-keeper-01/etc/clickhouse-keeper/keeper_config.xml:/etc/clickhouse-keeper/keeper_config.xml
    ports:
        - "127.0.0.1:9181:9181"
  clickhouse-keeper-02:
    image: "clickhouse/clickhouse-keeper:latest-alpine"
    user: "101:101"
    container_name: clickhouse-keeper-02
    hostname: clickhouse-keeper-02
    volumes:
     - ${PWD}/fs/volumes/clickhouse-keeper-02/etc/clickhouse-keeper/keeper_config.xml:/etc/clickhouse-keeper/keeper_config.xml
    ports:
        - "127.0.0.1:9182:9181"
  clickhouse-keeper-03:
    image: "clickhouse/clickhouse-keeper:latest-alpine"
    user: "101:101"
    container_name: clickhouse-keeper-03
    hostname: clickhouse-keeper-03
    volumes:
     - ${PWD}/fs/volumes/clickhouse-keeper-03/etc/clickhouse-keeper/keeper_config.xml:/etc/clickhouse-keeper/keeper_config.xml
    ports:
        - "127.0.0.1:9183:9181"
```

Create the following sub-directories and files:

```bash
for i in {01..02}; do
  mkdir -p fs/volumes/clickhouse-${i}/etc/clickhouse-server/config.d
  mkdir -p fs/volumes/clickhouse-${i}/etc/clickhouse-server/users.d
  touch fs/volumes/clickhouse-${i}/etc/clickhouse-server/config.d/config.xml
  touch fs/volumes/clickhouse-${i}/etc/clickhouse-server/users.d/users.xml
done
```

- The `config.d` directory contains ClickHouse server configuration file `config.xml`,
  in which custom configuration for each ClickHouse node is defined. This
  configuration gets combined with the default `config.xml` ClickHouse configuration
  file that comes with every ClickHouse installation.
- The `users.d` directory contains user configuration file `users.xml`, in which
  custom configuration for users is defined. This configuration gets combined with
  the default ClickHouse `users.xml` configuration file that comes with every
  ClickHouse installation.

<Tip title="Custom configuration directories">
It is a best practice to make use of the `config.d` and `users.d` directories when
writing your own configuration, rather than directly modifying the default configuration
in `/etc/clickhouse-server/config.xml` and `etc/clickhouse-server/users.xml`.

The line

```xml
<clickhouse replace="true">
```

Ensures that the configuration sections defined in the `config.d` and `users.d`
directories override the default configuration sections defined in the default
`config.xml` and `users.xml` files.
</Tip>

## Configure ClickHouse nodes [#configure-clickhouse-servers]

### Server setup [#server-setup]

Now modify each empty configuration file `config.xml` located at
`fs/volumes/clickhouse-{}/etc/clickhouse-server/config.d`. The lines which are
highlighted below need to be changed to be specific to each node:

```xml
<clickhouse replace="true">
    <logger>
        <level>debug</level>
        <log>/var/log/clickhouse-server/clickhouse-server.log</log>
        <errorlog>/var/log/clickhouse-server/clickhouse-server.err.log</errorlog>
        <size>1000M</size>
        <count>3</count>
    </logger>
    <!--highlight-next-line-->
    <display_name>cluster_1S_2R node 1</display_name>
    <listen_host>0.0.0.0</listen_host>
    <http_port>8123</http_port>
    <tcp_port>9000</tcp_port>
    <user_directories>
        <users_xml>
            <path>users.xml</path>
        </users_xml>
        <local_directory>
            <path>/var/lib/clickhouse/access/</path>
        </local_directory>
    </user_directories>
    <distributed_ddl>
        <path>/clickhouse/task_queue/ddl</path>
    </distributed_ddl>
    <remote_servers>
        <cluster_1S_2R>
            <shard>
                <internal_replication>true</internal_replication>
                <replica>
                    <host>clickhouse-01</host>
                    <port>9000</port>
                </replica>
                <replica>
                    <host>clickhouse-02</host>
                    <port>9000</port>
                </replica>
            </shard>
        </cluster_1S_2R>
    </remote_servers>
    <zookeeper>
        <node>
            <host>clickhouse-keeper-01</host>
            <port>9181</port>
        </node>
        <node>
            <host>clickhouse-keeper-02</host>
            <port>9181</port>
        </node>
        <node>
            <host>clickhouse-keeper-03</host>
            <port>9181</port>
        </node>
    </zookeeper>
    <!--highlight-start-->
    <macros>
        <shard>01</shard>
        <replica>01</replica>
        <cluster>cluster_1S_2R</cluster>
    </macros>
    <!--highlight-end-->
</clickhouse>
```

| Directory                                                 | File                                                                                                                                                                              |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fs/volumes/clickhouse-01/etc/clickhouse-server/config.d` | [`config.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-01/etc/clickhouse-server/config.d/config.xml)  |
| `fs/volumes/clickhouse-02/etc/clickhouse-server/config.d` | [`config.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-02/etc/clickhouse-server/config.d/config.xml)  |

Each section of the above configuration file is explained in more detail below.

#### Networking and logging [#networking]

External communication to the network interface is enabled by activating the listen
host setting. This ensures that the ClickHouse server host is reachable by other
hosts:

```xml
<listen_host>0.0.0.0</listen_host>
```

The port for the HTTP API is set to `8123`:

```xml
<http_port>8123</http_port>
```

The TCP port for interaction by ClickHouse's native protocol between clickhouse-client
and other native ClickHouse tools, and clickhouse-server and other clickhouse-servers
is set to `9000`:

```xml
<tcp_port>9000</tcp_port>
```


Logging is defined in the `<logger>` block. This example configuration gives 
you a debug log that will roll over at 1000M three times:

```xml
<logger>
    <level>debug</level>
    <log>/var/log/clickhouse-server/clickhouse-server.log</log>
    <errorlog>/var/log/clickhouse-server/clickhouse-server.err.log</errorlog>
    <size>1000M</size>
    <count>3</count>
</logger>
```

For more information on logging configuration, see the comments included in the
default ClickHouse [configuration file](https://github.com/ClickHouse/ClickHouse/blob/master/programs/server/config.xml).

#### Cluster configuration [#cluster-configuration]

Configuration for the cluster is set up in the `<remote_servers>` block.
Here the cluster name `cluster_1S_2R` is defined.

The `<cluster_1S_2R></cluster_1S_2R>` block defines the layout of the cluster,
using the `<shard></shard>` and `<replica></replica>` settings, and acts as a 
template for distributed DDL queries, which are queries that execute across the 
cluster using the `ON CLUSTER` clause. By default, distributed DDL queries
are allowed, but can also be turned off with setting `allow_distributed_ddl_queries`.

`internal_replication` is set to true so that data is written to just one of the replicas.

```xml
<remote_servers>
    <!-- cluster name (should not contain dots) -->
    <cluster_1S_2R>
        <!-- <allow_distributed_ddl_queries>false</allow_distributed_ddl_queries> -->
        <shard>
            <!-- Optional. Whether to write data to just one of the replicas. Default: false (write data to all replicas). -->
            <internal_replication>true</internal_replication>
            <replica>
                <host>clickhouse-01</host>
                <port>9000</port>
            </replica>
            <replica>
                <host>clickhouse-02</host>
                <port>9000</port>
            </replica>
        </shard>
    </cluster_1S_2R>
</remote_servers>
```

For each server, the following parameters are specified:

| Parameter     | Description                                                                                                                                                                                                                                                                                                                                          | Default Value |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| `host`        | The address of the remote server. You can use either the domain or the IPv4 or IPv6 address. If you specify the domain, the server makes a DNS request when it starts, and the result is stored as long as the server is running. If the DNS request fails, the server does not start. If you change the DNS record, you need to restart the server. | -            |
| `port`        | The TCP port for messenger activity (`tcp_port` in the config, usually set to 9000). Not to be confused with `http_port`.                                                                                                                                                                                                                            | -            |


#### Keeper configuration [#keeper-config-explanation]

The `<ZooKeeper>` section tells ClickHouse where ClickHouse Keeper (or ZooKeeper) is running.
As we are using a ClickHouse Keeper cluster, each `<node>` of the cluster needs to be specified,
along with its hostname and port number using the `<host>` and `<port>` tags respectively.

Set up of ClickHouse Keeper is explained in the next step of the tutorial.

```xml
<zookeeper>
    <node>
        <host>clickhouse-keeper-01</host>
        <port>9181</port>
    </node>
    <node>
        <host>clickhouse-keeper-02</host>
        <port>9181</port>
    </node>
    <node>
        <host>clickhouse-keeper-03</host>
        <port>9181</port>
    </node>
</zookeeper>
```

<Note>
Although it is possible to run ClickHouse Keeper on the same server as ClickHouse Server, 
in production environments we strongly recommend that ClickHouse Keeper runs on dedicated hosts.
</Note>

#### Macros configuration [#macros-config-explanation]

Additionally, the `<macros>` section is used to define parameter substitutions for
replicated tables. These are listed in `system.macros` and allow using substitutions
like `{shard}` and `{replica}` in queries.

```xml
<macros>
    <shard>01</shard>
    <replica>01</replica>
    <cluster>cluster_1S_2R</cluster>
</macros>
```

<Note>
These will be defined uniquely depending on the layout of the cluster.
</Note>

### User configuration [#user-config]

Now modify each empty configuration file `users.xml` located at
`fs/volumes/clickhouse-{}/etc/clickhouse-server/users.d` with the following:

```xml title="/users.d/users.xml"
<?xml version="1.0"?>
<clickhouse replace="true">
    <profiles>
        <default>
            <max_memory_usage>10000000000</max_memory_usage>
            <use_uncompressed_cache>0</use_uncompressed_cache>
            <load_balancing>in_order</load_balancing>
            <log_queries>1</log_queries>
        </default>
    </profiles>
    <users>
        <default>
            <access_management>1</access_management>
            <profile>default</profile>
            <networks>
                <ip>::/0</ip>
            </networks>
            <quota>default</quota>
            <access_management>1</access_management>
            <named_collection_control>1</named_collection_control>
            <show_named_collections>1</show_named_collections>
            <show_named_collections_secrets>1</show_named_collections_secrets>
        </default>
    </users>
    <quotas>
        <default>
            <interval>
                <duration>3600</duration>
                <queries>0</queries>
                <errors>0</errors>
                <result_rows>0</result_rows>
                <read_rows>0</read_rows>
                <execution_time>0</execution_time>
            </interval>
        </default>
    </quotas>
</clickhouse>
```

| Directory                                                 | File                                                                                                                                                                             |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fs/volumes/clickhouse-01/etc/clickhouse-server/users.d`  | [`users.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-01/etc/clickhouse-server/users.d/users.xml)    |
| `fs/volumes/clickhouse-02/etc/clickhouse-server/users.d`  | [`users.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-02/etc/clickhouse-server/users.d/users.xml)    |

In this example, the default user is configured without a password for simplicity.
In practice, this is discouraged.

<Note>
In this example, each `users.xml` file is identical for all nodes in the cluster.
</Note>

## Configure ClickHouse Keeper [#configure-clickhouse-keeper-nodes]

### Keeper setup [#configuration-explanation]

In order for replication to work, a ClickHouse keeper cluster needs to be set up and
configured. ClickHouse Keeper provides the coordination system for data replication,
acting as a stand in replacement for Zookeeper, which could also be used.
ClickHouse Keeper is, however, recommended, as it provides better guarantees and
reliability and uses fewer resources than ZooKeeper. For high availability and to
keep quorum, it is recommended to run at least three ClickHouse Keeper nodes.

<Note>
ClickHouse Keeper can run on any node of the cluster alongside ClickHouse, although
it is recommended to have it run on a dedicated node which allows scaling and
managing the ClickHouse Keeper cluster independently of the database cluster.
</Note>

Create the `keeper_config.xml` files for each ClickHouse Keeper node
using the following command from the root of the example folder:

```bash
for i in {01..03}; do
  touch fs/volumes/clickhouse-keeper-${i}/etc/clickhouse-keeper/keeper_config.xml
done
```

Modify the empty configuration files which were created in each
node directory `fs/volumes/clickhouse-keeper-{}/etc/clickhouse-keeper`. The
highlighted lines below need to be changed to be specific to each node:

```xml title="/clickhouse-keeper/keeper_config.xml"
<clickhouse replace="true">
    <logger>
        <level>information</level>
        <log>/var/log/clickhouse-keeper/clickhouse-keeper.log</log>
        <errorlog>/var/log/clickhouse-keeper/clickhouse-keeper.err.log</errorlog>
        <size>1000M</size>
        <count>3</count>
    </logger>
    <listen_host>0.0.0.0</listen_host>
    <keeper_server>
        <tcp_port>9181</tcp_port>
        <!--highlight-next-line-->
        <server_id>1</server_id>
        <log_storage_path>/var/lib/clickhouse/coordination/log</log_storage_path>
        <snapshot_storage_path>/var/lib/clickhouse/coordination/snapshots</snapshot_storage_path>
        <coordination_settings>
            <operation_timeout_ms>10000</operation_timeout_ms>
            <session_timeout_ms>30000</session_timeout_ms>
            <raft_logs_level>information</raft_logs_level>
        </coordination_settings>
        <raft_configuration>
            <server>
                <id>1</id>
                <hostname>clickhouse-keeper-01</hostname>
                <port>9234</port>
            </server>
            <server>
                <id>2</id>
                <hostname>clickhouse-keeper-02</hostname>
                <port>9234</port>
            </server>
            <server>
                <id>3</id>
                <hostname>clickhouse-keeper-03</hostname>
                <port>9234</port>
            </server>
        </raft_configuration>
    </keeper_server>
</clickhouse>
```


| Directory                                                        | File                                                                                                                                                                                         |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fs/volumes/clickhouse-keeper-01/etc/clickhouse-keeper` | [`keeper_config.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-keeper-01/etc/clickhouse-keeper/keeper_config.xml) |
| `fs/volumes/clickhouse-keeper-02/etc/clickhouse-keeper` | [`keeper_config.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-keeper-02/etc/clickhouse-keeper/keeper_config.xml) |
| `fs/volumes/clickhouse-keeper-03/etc/clickhouse-keeper` | [`keeper_config.xml`](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/cluster_1S_2R/fs/volumes/clickhouse-keeper-03/etc/clickhouse-keeper/keeper_config.xml) |

Each configuration file will contain the following unique configuration (shown below).
The `server_id` used should be unique for that particular ClickHouse Keeper node
in the cluster and match the server `<id>` defined in the `<raft_configuration>` section.
`tcp_port` is the port used by _clients_ of ClickHouse Keeper.

```xml
<tcp_port>9181</tcp_port>
<server_id>{id}</server_id>
```

The following section is used to configure the servers that participate in the
quorum for the [raft consensus algorithm](https://en.wikipedia.org/wiki/Raft_(algorithm)):

```xml
<raft_configuration>
    <server>
        <id>1</id>
        <hostname>clickhouse-keeper-01</hostname>
        <!-- TCP port used for communication between ClickHouse Keeper nodes -->
        <!--highlight-next-line-->
        <port>9234</port>
    </server>
    <server>
        <id>2</id>
        <hostname>clickhouse-keeper-02</hostname>
        <port>9234</port>
    </server>
    <server>
        <id>3</id>
        <hostname>clickhouse-keeper-03</hostname>
        <port>9234</port>
    </server>
</raft_configuration>
```

<Tip title="ClickHouse Cloud simplifies management">
[ClickHouse Cloud](/cloud/overview)
removes the operational burden associated with managing shards and replicas. The
platform automatically handles high availability, replication, and scaling decisions.
Compute and storage are separate and scale based on demand without requiring manual
configuration or ongoing maintenance.

[Read more](/manage/scaling)
</Tip>


## Test the setup [#test-the-setup]

Make sure that docker is running on your machine.
Start the cluster using the `docker-compose up` command from the root of the `cluster_1S_2R` directory:

```bash
docker-compose up -d
```

You should see docker begin to pull the ClickHouse and Keeper images,
and then start the containers:

```bash
[+] Running 6/6
 ✔ Network cluster_1s_2r_default   Created
 ✔ Container clickhouse-keeper-03  Started
 ✔ Container clickhouse-keeper-02  Started
 ✔ Container clickhouse-keeper-01  Started
 ✔ Container clickhouse-01         Started
 ✔ Container clickhouse-02         Started
```

To verify that the cluster is running, connect to either `clickhouse-01` or `clickhouse-02` and run the
following query. The command to connect to the first node is shown:

```bash
# Connect to any node
docker exec -it clickhouse-01 clickhouse-client
```

If successful, you will see the ClickHouse client prompt:

```response
cluster_1S_2R node 1 :)
```

Run the following query to check what cluster topologies are defined for which
hosts:

```sql title="Query"
SELECT 
    cluster,
    shard_num,
    replica_num,
    host_name,
    port
FROM system.clusters;
```

```response title="Response"
   ┌─cluster───────┬─shard_num─┬─replica_num─┬─host_name─────┬─port─┐
1. │ cluster_1S_2R │         1 │           1 │ clickhouse-01 │ 9000 │
2. │ cluster_1S_2R │         1 │           2 │ clickhouse-02 │ 9000 │
3. │ default       │         1 │           1 │ localhost     │ 9000 │
   └───────────────┴───────────┴─────────────┴───────────────┴──────┘
```

Run the following query to check the status of the ClickHouse Keeper cluster:

```sql title="Query"
SELECT *
FROM system.zookeeper
WHERE path IN ('/', '/clickhouse')
```

```response title="Response"
   ┌─name───────┬─value─┬─path────────┐
1. │ sessions   │       │ /clickhouse │
2. │ task_queue │       │ /clickhouse │
3. │ keeper     │       │ /           │
4. │ clickhouse │       │ /           │
   └────────────┴───────┴─────────────┘
```

The `mntr` command is also commonly used to verify that ClickHouse Keeper is
running and to get state information about the relationship of the three Keeper nodes.
In the configuration used in this example, there are three nodes working together.
The nodes will elect a leader, and the remaining nodes will be followers.

The `mntr` command gives information related to performance, and whether a particular
node is a follower or a leader.

<Tip>
You may need to install `netcat` in order to send the `mntr` command to Keeper.
Please see the [nmap.org](https://nmap.org/ncat/) page for download information.
</Tip>

Run the command below from a shell on `clickhouse-keeper-01`, `clickhouse-keeper-02`, and
`clickhouse-keeper-03` to check the status of each Keeper node. The command
for `clickhouse-keeper-01` is shown below:

```bash
docker exec -it clickhouse-keeper-01  /bin/sh -c 'echo mntr | nc 127.0.0.1 9181'
```

The response below shows an example response from a follower node:

```response title="Response"
zk_version      v23.3.1.2823-testing-46e85357ce2da2a99f56ee83a079e892d7ec3726
zk_avg_latency  0
zk_max_latency  0
zk_min_latency  0
zk_packets_received     0
zk_packets_sent 0
zk_num_alive_connections        0
zk_outstanding_requests 0
zk_server_state follower
zk_znode_count  6
zk_watch_count  0
zk_ephemerals_count     0
zk_approximate_data_size        1271
zk_key_arena_size       4096
zk_latest_snapshot_size 0
zk_open_file_descriptor_count   46
zk_max_file_descriptor_count    18446744073709551615
```

The response below shows an example response from a leader node:

```response title="Response"
zk_version      v23.3.1.2823-testing-46e85357ce2da2a99f56ee83a079e892d7ec3726
zk_avg_latency  0
zk_max_latency  0
zk_min_latency  0
zk_packets_received     0
zk_packets_sent 0
zk_num_alive_connections        0
zk_outstanding_requests 0
# highlight-next-line
zk_server_state leader
zk_znode_count  6
zk_watch_count  0
zk_ephemerals_count     0
zk_approximate_data_size        1271
zk_key_arena_size       4096
zk_latest_snapshot_size 0
zk_open_file_descriptor_count   48
zk_max_file_descriptor_count    18446744073709551615
# highlight-start
zk_followers    2
zk_synced_followers     2
# highlight-end
```


With this, you have successfully set up a ClickHouse cluster with a single shard and two replicas.
In the next step, you will create a table in the cluster.

## Create a database [#creating-a-database]

Now that you have verified the cluster is correctly setup and is running, you
will be recreating the same table as the one used in the [UK property prices](/getting-started/example-datasets/uk-price-paid)
example dataset tutorial. It consists of around 30 million rows of prices paid
for real-estate property in England and Wales since 1995.

Connect to the client of each host by running each of the following commands from separate terminal
tabs or windows:

```bash
docker exec -it clickhouse-01 clickhouse-client
docker exec -it clickhouse-02 clickhouse-client
```

You can run the query below from clickhouse-client of each host to confirm that 
there are no databases created yet, apart from the default ones:

```sql title="Query"
SHOW DATABASES;
```

```response title="Response"
   ┌─name───────────────┐
1. │ INFORMATION_SCHEMA │
2. │ default            │
3. │ information_schema │
4. │ system             │
   └────────────────────┘
```

From the `clickhouse-01` client run the following **distributed** DDL query using the
`ON CLUSTER` clause to create a new database called `uk`:

```sql
CREATE DATABASE IF NOT EXISTS uk 
-- highlight-next-line
ON CLUSTER cluster_1S_2R;
```

You can again run the same query as before from the client of each host
to confirm that the database has been created across the cluster despite running
the query only `clickhouse-01`:

```sql
SHOW DATABASES;
```

```response
   ┌─name───────────────┐
1. │ INFORMATION_SCHEMA │
2. │ default            │
3. │ information_schema │
4. │ system             │
#highlight-next-line
5. │ uk                 │
   └────────────────────┘
```

## Create a table on the cluster [#creating-a-table]

Now that the database has been created, create a table on the cluster.
Run the following query from any of the host clients:

```sql
CREATE TABLE IF NOT EXISTS uk.uk_price_paid_local
--highlight-next-line
ON CLUSTER cluster_1S_2R
(
    price UInt32,
    date Date,
    postcode1 LowCardinality(String),
    postcode2 LowCardinality(String),
    type Enum8('terraced' = 1, 'semi-detached' = 2, 'detached' = 3, 'flat' = 4, 'other' = 0),
    is_new UInt8,
    duration Enum8('freehold' = 1, 'leasehold' = 2, 'unknown' = 0),
    addr1 String,
    addr2 String,
    street LowCardinality(String),
    locality LowCardinality(String),
    town LowCardinality(String),
    district LowCardinality(String),
    county LowCardinality(String)
)
--highlight-next-line
ENGINE = ReplicatedMergeTree
ORDER BY (postcode1, postcode2, addr1, addr2);
```

Notice that it is identical to the query used in the original `CREATE` statement of the
[UK property prices](/getting-started/example-datasets/uk-price-paid) example dataset tutorial,
except for the `ON CLUSTER` clause and use of the `ReplicatedMergeTree` engine.

The `ON CLUSTER` clause is designed for distributed execution of DDL (Data Definition Language)
queries such as `CREATE`, `DROP`, `ALTER`, and `RENAME`, ensuring that these
schema changes are applied across all nodes in a cluster.

The [`ReplicatedMergeTree`](https://clickhouse.com/docs/engines/table-engines/mergetree-family/replication#converting-from-mergetree-to-replicatedmergetree)
engine works just as the ordinary `MergeTree` table engine, but it will also replicate the data.

You can run the query below from either `clickhouse-01` or `clickhouse-02` client 
to confirm that the table has been created across the cluster:

```sql title="Query"
SHOW TABLES IN uk;
```

```response title="Response"
   ┌─name────────────────┐
1. │ uk_price_paid.      │
   └─────────────────────┘
```

## Insert data [#inserting-data]

As the data set is large and takes a few minutes to completely ingest, we will
insert only a small subset to begin with.

Insert a smaller subset of the data using the query below from `clickhouse-01`:

```sql
INSERT INTO uk.uk_price_paid_local
SELECT
    toUInt32(price_string) AS price,
    parseDateTimeBestEffortUS(time) AS date,
    splitByChar(' ', postcode)[1] AS postcode1,
    splitByChar(' ', postcode)[2] AS postcode2,
    transform(a, ['T', 'S', 'D', 'F', 'O'], ['terraced', 'semi-detached', 'detached', 'flat', 'other']) AS type,
    b = 'Y' AS is_new,
    transform(c, ['F', 'L', 'U'], ['freehold', 'leasehold', 'unknown']) AS duration,
    addr1,
    addr2,
    street,
    locality,
    town,
    district,
    county
FROM url(
    'http://prod1.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv',
    'CSV',
    'uuid_string String,
    price_string String,
    time String,
    postcode String,
    a String,
    b String,
    c String,
    addr1 String,
    addr2 String,
    street String,
    locality String,
    town String,
    district String,
    county String,
    d String,
    e String'
) LIMIT 10000
SETTINGS max_http_get_redirects=10;
```

Notice that the data is completely replicated on each host:

```sql
-- clickhouse-01
SELECT count(*)
FROM uk.uk_price_paid_local

--   ┌─count()─┐
-- 1.│   10000 │
--   └─────────┘

-- clickhouse-02
SELECT count(*)
FROM uk.uk_price_paid_local

--   ┌─count()─┐
-- 1.│   10000 │
--   └─────────┘
```

To demonstrate what happens when one of the hosts fails, create a simple test database
and test table from either of the hosts:

```sql
CREATE DATABASE IF NOT EXISTS test ON CLUSTER cluster_1S_2R;
CREATE TABLE test.test_table ON CLUSTER cluster_1S_2R
(
    `id` UInt64,
    `name` String
)
ENGINE = ReplicatedMergeTree
ORDER BY id;
```

As with the `uk_price_paid` table, we can insert data from either host:

```sql
INSERT INTO test.test_table (id, name) VALUES (1, 'Clicky McClickface');
```

But what will happen if one of the hosts is down? To simulate this, stop 
`clickhouse-01` by running:

```bash
docker stop clickhouse-01
```

Check that the host is down by running:

```bash
docker-compose ps
```

```response title="Response"
NAME                   IMAGE                                        COMMAND            SERVICE                CREATED          STATUS          PORTS
clickhouse-02          clickhouse/clickhouse-server:latest          "/entrypoint.sh"   clickhouse-02          X minutes ago    Up X minutes    127.0.0.1:8124->8123/tcp, 127.0.0.1:9001->9000/tcp
clickhouse-keeper-01   clickhouse/clickhouse-keeper:latest-alpine   "/entrypoint.sh"   clickhouse-keeper-01   X minutes ago    Up X minutes    127.0.0.1:9181->9181/tcp
clickhouse-keeper-02   clickhouse/clickhouse-keeper:latest-alpine   "/entrypoint.sh"   clickhouse-keeper-02   X minutes ago    Up X minutes    127.0.0.1:9182->9181/tcp
clickhouse-keeper-03   clickhouse/clickhouse-keeper:latest-alpine   "/entrypoint.sh"   clickhouse-keeper-03   X minutes ago    Up X minutes    127.0.0.1:9183->9181/tcp
```

With `clickhouse-01` now down, insert another row of data into the test table
and query the table:

```sql
INSERT INTO test.test_table (id, name) VALUES (2, 'Alexey Milovidov');
SELECT * FROM test.test_table;
```

```response title="Response"
   ┌─id─┬─name───────────────┐
1. │  1 │ Clicky McClickface │
2. │  2 │ Alexey Milovidov   │
   └────┴────────────────────┘
```

Now restart `clickhouse-01` with the following command (you can run `docker-compose ps` again after to confirm):

```sql
docker start clickhouse-01
```

Query the test table again from `clickhouse-01` after running `docker exec -it clickhouse-01 clickhouse-client`:

```sql title="Query"
SELECT * FROM test.test_table
```

```response title="Response"
   ┌─id─┬─name───────────────┐
1. │  1 │ Clicky McClickface │
2. │  2 │ Alexey Milovidov   │
   └────┴────────────────────┘
```

If at this stage you would like to ingest the full UK property price dataset
to play around with, you can run the following queries to do so:

```sql
TRUNCATE TABLE uk.uk_price_paid_local ON CLUSTER cluster_1S_2R;
INSERT INTO uk.uk_price_paid_local
SELECT
    toUInt32(price_string) AS price,
    parseDateTimeBestEffortUS(time) AS date,
    splitByChar(' ', postcode)[1] AS postcode1,
    splitByChar(' ', postcode)[2] AS postcode2,
    transform(a, ['T', 'S', 'D', 'F', 'O'], ['terraced', 'semi-detached', 'detached', 'flat', 'other']) AS type,
    b = 'Y' AS is_new,
    transform(c, ['F', 'L', 'U'], ['freehold', 'leasehold', 'unknown']) AS duration,
    addr1,
    addr2,
    street,
    locality,
    town,
    district,
    county
FROM url(
    'http://prod1.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv',
    'CSV',
    'uuid_string String,
    price_string String,
    time String,
    postcode String,
    a String,
    b String,
    c String,
    addr1 String,
    addr2 String,
    street String,
    locality String,
    town String,
    district String,
    county String,
    d String,
    e String'
    ) SETTINGS max_http_get_redirects=10;
```

Query the table from `clickhouse-02` or `clickhouse-01`:

```sql title="Query"
SELECT count(*) FROM uk.uk_price_paid_local;
```

```response title="Response"
   ┌──count()─┐
1. │ 30212555 │ -- 30.21 million
   └──────────┘
```

</Steps>

## Conclusion [#conclusion]

The advantage of this cluster topology is that with two replicas, 
your data exists on two separate hosts. If one host fails, the other replica 
continues serving data without any loss. This eliminates single points of 
failure at the storage level.

When one host goes down, the remaining replica is still able to:
- Handle read queries without interruption
- Accept new writes (depending on your consistency settings)
- Maintain service availability for applications

When the failed host comes back online, it is able to:
- Automatically sync missing data from the healthy replica
- Resume normal operations without manual intervention
- Restore full redundancy quickly

In the next example, we'll look at how to set up a cluster with two shards but 
only one replica.
