# Source: https://docs.confluent.io/kafka/operations-tools/kafka-tools.md

<style>
  input.search-bar {
    box-sizing: border-box;
    margin-bottom: 30px;
    font-size: 22px;
    padding: 20px;
    padding-left: 60px;
    border: 0;
    border-radius: 4px;
    box-shadow: none;
    flex: 1;
    width: 100%;
    color: #3B454F;
    line-height: 27.5px;
    background: #F1FAFF 20px 24px no-repeat url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAGqSURBVHgBrZRBTsJQEIZnHi6AkNiVeYRNDZC4xBMIN9AT0BuIJxBPwBHEExhPQDmB7NFYFiRNcNEFCZu2z5n2EUnpKwSd5KXT8vN15vWfh5AJy7KtSuXMiWNlI8I5AC7osev7Hy4cEbh7I2XrUQgYKAXWvlR5SkU93/c8OAYoZfsZUTn6dkpQNxEg2nS5ISBfgzDE3mo1nxUCuTJqb0griGO4y7Yn5ZUtRDiil9wydLMJL4PAC3KJLK7XW4qXlE0HCoI0k1TXGpo0AiDq6nzq+5/jAh5QhU9JWwj3RiBi3NFiFw7EzlZY7IZcoFLCghOiXIZ8INsBkgrVQTDv9zY32YeAaatCYN/Uxm+EfZ1MTQqh94WXVa2WRiZho9HusLU4p27GRqCu7oE9qBQ69Xrzi2zR3Qq4avYpjeK7fkT+i1wTEHcrIFO/6onIFycv5Y9hHkOxTZbL+UypUo/+9kIrK+RR7MXx2XX6G9LBUZpIadvGCrPBrbI1slXwl0aMJmkn+5UagUVRBD0JWAQ9GWiCluAPsV5/B7XaxRudo3ys2TTGC/iP0EfggPMf4IXM0qeAeMAAAAAASUVORK5CYII=);
    background-clip: padding-box;
    }
 </style>

 <script>

 function filterList() {
   // Get input value and convert to lowercase
   var input = document.getElementById("search-bar").value.toLowerCase();

   // Get all the h3 headers (tool names) and their first sibling, which is the tool description.
   var sections = document.getElementsByTagName("section")
   //var headerEntries = document.getElementsByTagName("h3");

   var h3Entry;
   var h2Entry;

   // Loop through all the headers
  for (var i = 0; i < sections.length; i++) {
   var section = sections[i];
   var h3Entries = section.getElementsByTagName("h3");

   // There is only 1 h3 in each section that contains a config value.
   if (h3Entries.length == 1) {
         // Check if the term matches the search input, and if so display the section. Otherwise, hide it.
     var h3text = h3Entries[0].textContent.toLowerCase();
     if (h3text.indexOf(input) > -1)
       section.style.display ="";
     else
       section.style.display = "none";
   }
  }
}

  window.addEventListener('load', filterList);

</script>

<a id="kafka-cli-tools"></a>

# Kafka Command-Line Interface (CLI) Tools

Apache KafkaÂ® is an open-source distributed streaming system used for stream processing,
real-time data pipelines, and data integration at scale.

Kafka provides a suite of command-line interface (CLI) tools that can be accessed from the `/bin` directory
after downloading Kafka and extracting the files. These tools offer a range of capabilities, including starting
and stopping Kafka, managing topics, and handling partitions. To learn how to use each tool,
simply run it with no argument or use the `--help` argument for detailed instructions.

The following sections group the tools by function and provide basic usage information. In some cases, a tool is listed in more than one section.

## Search by tool name

Enter a string to search and filter tools by name.

<form>

  <input type="text" id="search-bar"
    class="search-bar"
    aria-label="Search"
    placeholder="Search for a tool..."
    onkeyup="filterList()"
    autocomplete="off"></input>
</form>

## Manage Kafka and configure metadata

This section contains tools to start Kafka running in KRaft mode and to manage brokers.

### kafka-server-start.sh

Use the `kafka-server-start` tool to start a Kafka server. You must pass the path to the properties file you want to use.
To start Kafka in KRaft mode, first generate a cluster ID and store it in the properties file.

### **Usage details**

```bash
USAGE: ./kafka-server-start.sh [-daemon] server.properties [--override property=value]*

Option               Description
------               -----------
--override <String>  Optional property that should override values set in
                     server.properties file
--version            Print version information and exit.
```

### kafka-server-stop.sh

Use the `kafka-server-stop` tool to stop the running Kafka server.
When you run this tool, you do not need to have any arguments, but starting with
Kafka 3.7 you can optionally specify either a `process-role` value of `broker` or `controller`
or a `node-id` value indicating the node you want to stop.

For example, to stop all brokers, you would use the following command:

```none
./bin/kafka-server-stop.sh --process-role=broker
```

To stop node `1234`, you would use the following command.

```none
./bin/kafka-server-stop.sh --node-id=1234
```

### **Usage details**

```bash
USAGE: ./kafka-server-stop.sh  {[--process-role=value] |  [--node-id=value]}
```

### kafka-storage.sh

Use the `kafka-storage` tool to generate a Cluster UUID and format storage with the generated UUID when running Kafka in KRaft mode.
You must explicitly create a cluster ID for a KRaft cluster, and format the storage specifying that ID.

For example, the following command generates a cluster ID and stores it in a variable named `KAFKA_CLUSTER_ID`.
The next command formats storage with that ID.

```none
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

bin/kafka-storage.sh format -t KAFKA_CLUSTER_ID -c config/kraft/server.properties
```

### **Usage details**

```bash
USAGE: kafka-storage.sh [-h] {info,format,version-mapping,feature-dependencies,random-uuid} ...

The Kafka storage tool.

positional arguments:
 {info,format,version-mapping,feature-dependencies,random-uuid}
   info                 Get information about the Kafka log directories on this node.
   format               Format the Kafka log directories on this node.
   version-mapping      Look up the corresponding features for a given metadata version. Using the command with no
                        ``--release-version`` argument will return the mapping for the latest stable metadata version.
   feature-dependencies Look up dependencies for a given feature version. If the feature is not known or the version
                        not yet defined, an error is thrown. Multiple features can be specified.
   random-uuid          Print a random UUID.

optional arguments:
 --config CONFIG, -c CONFIG         The Kafka configuration file to use.
 --cluster-id CLUSTER_ID, -t        CLUSTER_ID The cluster ID to use.
 --add-scram ADD_SCRAM, -S          ADD_SCRAM A SCRAM_CREDENTIAL to add to the __cluster_metadata log e.g.
                                    'SCRAM-SHA-256=[name=alice,password=alice-secret]'
                                    'SCRAM-SHA-512=[name=alice,iterations=8192,salt="N3E=",saltedpassword="YCE="]'
 --ignore-formatted, -g             When this option is passed, the format command will skip over already formatted
                                    directories rather than failing.
 --release-version                  The release version to use for the initial feature settings. The minimum is 3.3-IV3; the
 RELEASE_VERSION, -r                default is 4.0-IV3
 RELEASE_VERSION

 --feature FEATURE,                 The setting to use for a specific feature, in feature=level format. For example: ``kraft.version=1``.
 -f FEATURE

 --standalone, -s                   Used to initialize a controller as a single-node dynamic quorum.
 --no-initial-controllers, -N       Used to initialize a server without a dynamic quorum topology.

--initial-controllers               Used to initialize a server with a specific dynamic quorum topology. The argument is a
INITIAL_CONTROLLERS,                comma-separated list of id@hostname:port:directory. The same values must be used to
-I INITIAL_CONTROLLERS              format all nodes. For example:
                                    0@example.com:8082:JEXY6aqzQY-32P5TStzaFg,1@example.com:8083:MvDxzVmcRsaTz33bUuRU6A,
                                    2@example.com:8084:07R5amHmR32VDA6jHkGbTA
 -h, --help                         show this help message and exit
```

<a id="kafka-cluster-usage"></a>

### kafka-cluster.sh

Use the `kafka-cluster` tool to get the ID of a cluster or unregister a cluster. The following example shows how to retrieve the cluster
ID, which requires a `bootstrap-server` argument.

```none
bin/kafka-cluster.sh cluster-id --bootstrap-server localhost:9092
```

The output for this command might look like the following.

```none
Cluster ID: WZEKwK-b123oT3ZOSU0dgw
```

### **Usage details**

```bash
USAGE: kafka-cluster.sh [-h] {cluster-id,unregister,list-endpoints} ...

The Kafka cluster tool.

positional arguments:
{cluster-id,unregister,list-endpoints}
  cluster-id           Get information about the ID of a cluster.
  unregister           Unregister a broker.
  list-endpoints       List endpoints

optional arguments:
  -h, --help             show this help message and exit
```

### kafka-features.sh

Use the `kafka-features` tool  to manage feature flags to disable or enable functionality at runtime in Kafka.
Pass the `describe` argument to describe the current active feature flags, `upgrade` to upgrade one
or more feature flags, `downgrade` to downgrade one or more, and `disable` to disable
one or more feature flags, which is the same as downgrading the version to zero.

### **Usage details**

```bash
usage: kafka-features [-h] [--command-config COMMAND_CONFIG] (--bootstrap-server BOOTSTRAP_SERVER |
                      --bootstrap-controller BOOTSTRAP_CONTROLLER) {describe,upgrade,downgrade,disable,version-mapping,feature-dependencies} ...

This tool manages feature flags in Kafka.

positional arguments:
  {describe,upgrade,downgrade,disable,version-mapping,feature-dependencies}
    describe             Describes the current active feature flags.
    upgrade              Upgrade one or more feature flags.
    downgrade            Upgrade one or more feature flags.
    disable              Disable one or more feature flags. This is the same as downgrading the version to zero.
    version-mapping      Look up the corresponding features for a given metadata version. Using the command with no
                         --release-version argument will return the mapping for the latest stable metadata version
    feature-dependencies Look up dependencies for a given feature version. If the feature is not known or the version
                         not yet defined, an error is thrown. Multiple features can be specified.

optional arguments:
  -h, --help             show this help message and exit
  --bootstrap-server BOOTSTRAP_SERVER
                        A comma-separated list of host:port pairs to use for establishing the connection to the
                        Kafka cluster.
  --bootstrap-controller BOOTSTRAP_CONTROLLER
                        A comma-separated list of host:port pairs to use for establishing the connection to the
                        KRaft quorum.
  --command-config COMMAND_CONFIG
                        Property file containing configs to be passed to Admin Client.
```

### kafka-broker-api-versions.sh

The `kafka-broker-api-versions` tool retrieves and displays broker information.
For example, the following command outputs the version of Kafka that is running on the broker:

```bash
bin/kafka-broker-api-versions.sh --bootstrap-server host1:9092 --version
```

This command might have the following output:

```bash
3.3.1 (Commit:e23c59d00e687ff5)
```

### **Usage details**

```bash
This tool helps to retrieve broker version information.

Option                                 Description
------                                 -----------
--bootstrap-server <String: server(s)  REQUIRED: The server to connect to.
  to use for bootstrapping>
--command-config <String: command      A property file containing configs to
  config property file>                  be passed to Admin Client.
--help                                 Print usage information.
--version                              Display Kafka version.
```

### kafka-metadata-quorum.sh

Use the `kafka-metadata-quorum` tool to query the metadata quorum status. This tool is useful when you are debugging a cluster in KRaft mode.
Pass the `describe` command to describe the current state of the metadata quorum.

The following code example displays a summary of the metadata quorum:

```none
bin/kafka-metadata-quorum.sh --bootstrap-server  host1:9092 describe --status
```

The output for this command might look like the following.

```none
ClusterId:              fMCL8kv1SWm87L_Md-I2hg
LeaderId:               3002
LeaderEpoch:            2
HighWatermark:          10
MaxFollowerLag:         0
MaxFollowerLagTimeMs:   -1
CurrentVoters:          [3000,3001,3002]
CurrentObservers:       [0,1,2]
```

### **Usage details**

```bash
usage: kafka-metadata-quorum [-h] [--command-config COMMAND_CONFIG] (--bootstrap-server BOOTSTRAP_SERVER |
                            --bootstrap-controller BOOTSTRAP_CONTROLLER) {describe,add-controller,remove-controller} ...

This tool describes kraft metadata quorum status.

positional arguments:
  {describe,add-controller,remove-controller}
    describe             Describe the metadata quorum info
    add-controller       Add a controller to the KRaft controller cluster
    remove-controller    Remove a controller from the KRaft controller cluster

optional arguments:
  -h, --help             show this help message and exit
  --bootstrap-server BOOTSTRAP_SERVER
                        A comma-separated list of host:port pairs  to  use  for establishing the connection to the
                        Kafka cluster.
  --bootstrap-controller BOOTSTRAP_CONTROLLER
                        A comma-separated list of host:port pairs  to  use  for establishing the connection to the
                        Kafka controllers.
  --command-config COMMAND_CONFIG
                        Property file containing configs to be passed to Admin Client.
```

### kafka-metadata-shell.sh

The `kafka-metadata-shell` tool enables you to interactively examine the metadata stored in a KRaft cluster.

To open the metadata shell, provide the path to your clusterâs metadata log directory using the `--directory` flag:

```none
kafka-metadata-shell.sh --directory tmp/kraft-combined-logs/_cluster-metadata-0/
```

To ensure `kafka-metadata-shell.sh` functions correctly, the `--directory` flag must point to your Kafka clusterâs
metadata log directory. While examples often show `/tmp/kraft-combined-logs/_cluster-metadata-0/`, this path varies
based on your Kafka configuration.

If your metadata files are not in their default or expected location, you have two options:

* Specify the full, correct path to your metadata log directory.
* Copy the metadata log directory to a temporary location (for example, /tmp), and then specify that temporary path.

After the shell loads, you can explore the contents of the metadata log, and exit. The following
code shows an example of this.

```none
Loading...
 [ Kafka Metadata Shell ]
 >> ls
 image local
 >>ls image
 acls cells clientQuotas cluster clusterLinks configs  delegationToken encryptor features  producerIds provenance replicaExclusions scram tenants  topics
 >> ls image/topics/
 byID byLinkId byName byTenant
 >>ls image/topics/byName
 test perf_test_124 othersourcetopic
 >> cat /image/topics/byName/othersourcetopic/0/
 {
   "replicas": [1],
   "observers": null,
   "directories": ["U9TE_0zN-oReJ5XwsShc-w"],
   "isr": [1],
   "removingReplicas": null,
   "addingReplicas": null,
   "removingObservers": null,
   "addingObservers": null,
   "elr": null,
   "lastKnownElr": null,
   "leader": -1,
   "leaderRecoveryState": "RECOVERED",
   "leaderEpoch": 57,
   "partitionEpoch": 9,
   "linkedLeaderEpoch": 54,
   "linkState": "ACTIVE"
 }
 >> exit
```

For more information, see the [Kafka Wiki](https://cwiki.apache.org/confluence/display/KAFKA/KIP-631%3A+The+Quorum-based+Kafka+Controller#KIP631:TheQuorumbasedKafkaController-kafka-metadata-shell.sh).

### **Usage details**

```bash
usage: metadata-shell-tool [-h] [--snapshot SNAPSHOT] [command [command ...]]

The Apache Kafka metadata tool

positional arguments:
  command                The command to run.

optional arguments:
  -h, --help             show this help message and exit
  --snapshot SNAPSHOT,
   -s SNAPSHOT           The snapshot file to read.
```

<a id="kafka-configs-tool"></a>

### kafka-configs.sh

Use the `kafka-configs` tool to change and describe topic, client, user, broker, IP configuration setting or
KRaft controller.
To describe or view a KRaft controller, use the `--bootstrap-controller` option, and do not specify a `bootstrap-server`.

To change a property, specify the `entity-type` to the desired entity (topic, broker, user, etc), and use the
`alter` option. The following example shows how you might add the `delete.retention` configuration property for a topic with `kafka-configs`.

```none
/bin/kafka-configs.sh --bootstrap-server host1:9092 --entity-type topics --entity-default --alter --add-config delete.retention.ms=172800000
```

When you use the `--add-config` flag to add multiple values, use square brackets around the comma-separated list
like the following example:

```none
/bin/kafka-configs.sh --bootstrap-server host1:9092 --alter --add-config max.connections.per.ip.overrides=[host1:50,host2:9] --entity-type brokers --entity-default
```

The following example shows how you might check the cluster ID, by specifying the `--bootstrap-controller` option.

```none
/bin/kafka-cluster.sh cluster-id --bootstrap-controller localhost:9092
```

See [Kafka Topic Operations](topic-operations.md#topic-operations) for more examples of how to work with topics.

### **Usage details**

```bash
This tool helps to manipulate and describe entity config for a topic, client, user, broker, ip or client-metrics

Option                                 Description
------                                 -----------
--add-config <String>                  Key Value pairs of configs to add.
                                       Square brackets can be used to group
                                       values which contain commas: 'k1=v1,
                                       k2=[v1,v2,v2],k3=v3'. The following
                                       is a list of valid configurations:
                                       For entity-type 'topics':
                                       cleanup.policy
                                       compression.gzip.level
                                       compression.lz4.level
                                       compression.type
                                       compression.zstd.level
                                       delete.retention.ms
                                       file.delete.delay.ms
                                       flush.messages
                                       flush.ms
                                       follower.replication.throttled.
                                       replicas
                                       index.interval.bytes
                                       leader.replication.throttled.replicas
                                       local.retention.bytes
                                       local.retention.ms
                                       max.compaction.lag.ms
                                       max.message.bytes
                                       message.timestamp.after.max.ms
                                       message.timestamp.before.max.ms
                                       message.timestamp.type
                                       min.cleanable.dirty.ratio
                                       min.compaction.lag.ms
                                       min.insync.replicas
                                       preallocate
                                       remote.log.copy.disable
                                       remote.log.delete.on.disable
                                       remote.storage.enable
                                       retention.bytes
                                       retention.ms
                                       segment.bytes
                                       segment.index.bytes
                                       segment.jitter.ms
                                       segment.ms
                                       unclean.leader.election.enable
                                       For entity-type 'brokers':
                                       background.threads
                                       compression.gzip.level
                                       compression.lz4.level
                                       compression.type
                                       compression.zstd.level
                                       follower.replication.throttled.rate
                                       leader.replication.throttled.rate
                                       listener.security.protocol.map
                                       listeners
                                       log.cleaner.backoff.ms
                                       log.cleaner.dedupe.buffer.size
                                       log.cleaner.delete.retention.ms
                                       log.cleaner.io.buffer.load.factor
                                       log.cleaner.io.buffer.size
                                       log.cleaner.io.max.bytes.per.second
                                       log.cleaner.max.compaction.lag.ms
                                       log.cleaner.min.cleanable.ratio
                                       log.cleaner.min.compaction.lag.ms
                                       log.cleaner.threads
                                       log.cleanup.policy
                                       log.flush.interval.messages
                                       log.flush.interval.ms
                                       log.index.interval.bytes
                                       log.index.size.max.bytes
                                       log.local.retention.bytes
                                       log.local.retention.ms
                                       log.message.timestamp.after.max.ms
                                       log.message.timestamp.before.max.ms
                                       log.message.timestamp.type
                                       log.preallocate
                                       log.retention.bytes
                                       log.retention.ms
                                       log.roll.jitter.ms
                                       log.roll.ms
                                       log.segment.bytes
                                       log.segment.delete.delay.ms
                                       max.connection.creation.rate
                                       max.connections
                                       max.connections.per.ip
                                       max.connections.per.ip.overrides
                                       message.max.bytes
                                       metric.reporters
                                       min.insync.replicas
                                       num.io.threads
                                       num.network.threads
                                       num.recovery.threads.per.data.dir
                                       num.replica.fetchers
                                       principal.builder.class
                                       producer.id.expiration.ms
                                       remote.fetch.max.wait.ms
                                       remote.list.offsets.request.timeout.ms
                                       remote.log.index.file.cache.total.
                                       size.bytes
                                       remote.log.manager.copier.thread.pool.
                                       size
                                       remote.log.manager.copy.max.bytes.per.
                                       second
                                       remote.log.manager.expiration.thread.
                                       pool.size
                                       remote.log.manager.fetch.max.bytes.
                                       per.second
                                       remote.log.reader.threads
                                       replica.alter.log.dirs.io.max.bytes.
                                       per.second
                                       sasl.enabled.mechanisms
                                       sasl.jaas.config
                                       sasl.kerberos.kinit.cmd
                                       sasl.kerberos.min.time.before.relogin
                                       sasl.kerberos.principal.to.local.rules
                                       sasl.kerberos.service.name
                                       sasl.kerberos.ticket.renew.jitter
                                       sasl.kerberos.ticket.renew.window.
                                       factor
                                       sasl.login.refresh.buffer.seconds
                                       sasl.login.refresh.min.period.seconds
                                       sasl.login.refresh.window.factor
                                       sasl.login.refresh.window.jitter
                                       sasl.mechanism.inter.broker.protocol
                                       ssl.cipher.suites
                                       ssl.client.auth
                                       ssl.enabled.protocols
                                       ssl.endpoint.identification.algorithm
                                       ssl.engine.factory.class
                                       ssl.key.password
                                       ssl.keymanager.algorithm
                                       ssl.keystore.certificate.chain
                                       ssl.keystore.key
                                       ssl.keystore.location
                                       ssl.keystore.password
                                       ssl.keystore.type
                                       ssl.protocol
                                       ssl.provider
                                       ssl.secure.random.implementation
                                       ssl.trustmanager.algorithm
                                       ssl.truststore.certificates
                                       ssl.truststore.location
                                       ssl.truststore.password
                                       ssl.truststore.type
                                       transaction.partition.verification.
                                       enable
                                       unclean.leader.election.enable
                                       For entity-type 'users':
                                       SCRAM-SHA-256
                                       SCRAM-SHA-512
                                       consumer_byte_rate
                                       controller_mutation_rate
                                       producer_byte_rate
                                       request_percentage
                                       For entity-type 'clients':
                                       consumer_byte_rate
                                       controller_mutation_rate
                                       producer_byte_rate
                                       request_percentage
                                       For entity-type 'ips':
                                       connection_creation_rate
                                       For entity-type 'client-metrics':
                                       interval.ms
                                       match
                                       metrics
                                       For entity-type 'groups':
                                       consumer.heartbeat.interval.ms
                                       consumer.session.timeout.ms
                                       share.auto.offset.reset
                                       share.heartbeat.interval.ms
                                       share.record.lock.duration.ms
                                       share.session.timeout.ms
                                       Entity types 'users' and 'clients' may
                                       be specified together to update
                                       config for clients of a specific
                                       user.
--add-config-file <String>             Path to a properties file with configs
                                       to add. See add-config for a list of
                                       valid configurations.
--all                                  List all configs for the given topic,
                                       broker, or broker-logger entity
                                       (includes static configuration when
                                       the entity type is brokers)
--alter                                Alter the configuration for the entity.
--bootstrap-controller <String:        The Kafka controllers to connect to.
controller to connect to>
--bootstrap-server <String: server to  The Kafka servers to connect to.
connect to>
--broker <String>                      The broker's ID.
--broker-defaults                      The config defaults for all brokers.
--broker-logger <String>               The broker's ID for its logger config.
--client <String>                      The client's ID.
--client-defaults                      The config defaults for all clients.
--client-metrics <String>              The client metrics config resource
                                       name.
--command-config <String: command      Property file containing configs to be
config property file>                  passed to Admin Client. This is used
                                       only with --bootstrap-server option
                                       for describing and altering broker
                                       configs.
--delete-config <String>               config keys to remove 'k1,k2'
--describe                             List configs for the given entity.
--entity-default                       Default entity name for
                                       clients/users/brokers/ips (applies
                                       to corresponding entity type in
                                       command line)
--entity-name <String>                 Name of entity (topic name/client
                                       id/user principal name/broker
                                       id/ip/client metrics)
--entity-type <String>                 Type of entity
                                       (topics/clients/users/brokers/broker-
                                       loggers/ips/client-metrics)
--force                                Suppress console prompts
--group <String>                       The group ID.
--help                                 Print usage information.
--ip <String>                          The IP address.
--ip-defaults                          The config defaults for all IPs.
--topic <String>                       The topic's name.
--user <String>                        The user's principal name.
--user-defaults                        The config defaults for all users.
--version                              Display Kafka version.
```

## Manage topics, partitions, and replication

<a id="kafka-topics-usage"></a>

### kafka-topics.sh

Use the `kafka-topics` tool to create or delete a topic. You can also use the tool to retrieve a list of topics associated with a Kafka cluster.
For more information, see [Kafka Topic Operations](topic-operations.md#topic-operations).

To change a topic, see [kafka-configs.sh](#kafka-configs-usage), or [how to modify a topic](topic-operations.md#modify-topic).

Example:

```bash
bin/kafka-topics.sh --bootstrap-server host1:9092 --topic test-topic --partitions 3
```

### **Usage details**

```bash
This tool helps to create, delete, describe, or change a topic.
Option                                   Description
------                                   -----------
--alter                                  Alter the number of partitions and
                                          replica assignment. (To alter topic
                                          configurations, the kafka-configs
                                          tool can be used.)
--at-min-isr-partitions                  if set when describing topics, only
                                          show partitions whose isr count is
                                          equal to the configured minimum.
--bootstrap-server <String: server to    REQUIRED: The Kafka server to connect
  connect to>                              to.
--command-config <String: command        Property file containing configs to be
  config property file>                    passed to the Admin Client.
--config <String: name=value>            A topic configuration override for the
                                          topic being created or altered. The
                                          following is a list of valid
                                          configurations:
                                                cleanup.policy
                                                compression.gzip.level
                                                      compression.lz4.level
                                                compression.type
                                                compression.zstd.level
                                                delete.retention.ms
                                                file.delete.delay.ms
                                                flush.messages
                                                flush.ms
                                                follower.replication.throttled.
                                          replicas
                                                index.interval.bytes
                                                leader.replication.throttled.replicas
                                                local.retention.bytes
                                                local.retention.ms
                                                max.compaction.lag.ms
                                                max.message.bytes
                                                message.timestamp.after.max.ms
                                                message.timestamp.before.max.ms
                                                message.timestamp.type
                                                min.cleanable.dirty.ratio
                                                min.compaction.lag.ms
                                                min.insync.replicas
                                                preallocate
                                                remote.log.copy.disable
                                                      remote.log.delete.on.disable
                                                remote.storage.enable
                                                retention.bytes
                                                retention.ms
                                                segment.bytes
                                                segment.index.bytes
                                                segment.jitter.ms
                                                segment.ms
                                                unclean.leader.election.enable
                                        See the Kafka documentation for full
                                          details on the topic configs. It is
                                          supported only in combination with --
                                          create. (To alter topic
                                          configurations, the kafka-configs
                                          tool can be used.)
--create                                 Create a new topic.
--delete                                 Delete a topic
--delete-config <String: name>           This option is no longer supported and
                                         has been deprecated since 4.0.
--describe                               List details for the given topics.
--exclude-internal                       Exclude internal topics when running
                                          list or describe command. The
                                          internal topics will be listed by
                                          default.
--help                                   Print usage information.
--if-exists                              if set when altering or deleting or
                                          describing topics, the action will
                                          only execute if the topic exists.
--if-not-exists                          If set when creating topics, the
                                          action will only execute if the
                                          topic does not already exist.
--list                                   List all available topics.
--partition-size-limit-per-response      The maximum partition size to be
  <Integer: maximum number of            included in one
  partitions per response>               DescribeTopicPartitions response.
--partitions <Integer: # of partitions>  The number of partitions for the topic
                                          being created or altered (WARNING:
                                          If partitions are increased for a
                                          topic that has a key, the partition
                                          logic or ordering of the messages
                                          will be affected). If not supplied
                                          for create, defaults to the cluster
                                          default.
--replica-assignment <String:            A list of manual partition-to-broker
  broker_id_for_part1_replica1 :           assignments for the topic being
  broker_id_for_part1_replica2 ,           created or altered.
  broker_id_for_part2_replica1 :
  broker_id_for_part2_replica2 , ...>
--replication-factor <Integer:           The replication factor for each
  replication factor>                      partition in the topic being
                                          created. If not supplied, defaults
                                          to the cluster default.
--topic <String: topic>                  The topic to create, alter, describe
                                          or delete. It also accepts a regular
                                          expression, except for --create
                                          option. Put topic name in double
                                          quotes and use the '\' prefix to
                                          escape regular expression symbols; e.
                                          g. "test\.topic".
--topic-id <String: topic-id>            The topic-id to describe. This is used
                                          only with --bootstrap-server option
                                          for describing topics.
--topics-with-overrides                  If set when describing topics, only
                                          show topics that have overridden
                                          configs.
--unavailable-partitions                 If set when describing topics, only
                                          show partitions whose leader is not
                                          available.
--under-min-isr-partitions               If set when describing topics, only
                                          show partitions whose isr count is
                                          less than the configured minimum.
--under-replicated-partitions            If set when describing topics, only
                                          show under replicated partitions
--version                                Display Kafka version.
```

<a id="kafka-configs-usage"></a>

### kafka-configs.sh

Use the `kafka-configs` tool to change and describe topic, client, user, broker, IP configuration setting or
KRaft controller.
To describe or view a KRaft controller, use the `--bootstrap-controller` option, and do not specify a `bootstrap-server`.

To change a property, specify the `entity-type` to the desired entity (topic, broker, user, etc), and use the
`alter` option. The following example shows how you might add the `delete.retention` configuration property for a topic with `kafka-configs`.

```none
/bin/kafka-configs.sh --bootstrap-server host1:9092 --entity-type topics --entity-default --alter --add-config delete.retention.ms=172800000
```

When you use the `--add-config` flag to add multiple values, use square brackets around the comma-separated list
like the following example:

```none
/bin/kafka-configs.sh --bootstrap-server host1:9092 --alter --add-config max.connections.per.ip.overrides=[host1:50,host2:9] --entity-type brokers --entity-default
```

The following example shows how you might check the cluster ID, by specifying the `--bootstrap-controller` option.

```none
/bin/kafka-cluster.sh cluster-id --bootstrap-controller localhost:9092
```

See [Kafka Topic Operations](topic-operations.md#topic-operations) for more examples of how to work with topics.

### **Usage details**

```bash
This tool helps to manipulate and describe entity config for a topic, client, user, broker, ip or client-metrics

Option                                 Description
------                                 -----------
--add-config <String>                  Key Value pairs of configs to add.
                                       Square brackets can be used to group
                                       values which contain commas: 'k1=v1,
                                       k2=[v1,v2,v2],k3=v3'. The following
                                       is a list of valid configurations:
                                       For entity-type 'topics':
                                       cleanup.policy
                                       compression.gzip.level
                                       compression.lz4.level
                                       compression.type
                                       compression.zstd.level
                                       delete.retention.ms
                                       file.delete.delay.ms
                                       flush.messages
                                       flush.ms
                                       follower.replication.throttled.
                                       replicas
                                       index.interval.bytes
                                       leader.replication.throttled.replicas
                                       local.retention.bytes
                                       local.retention.ms
                                       max.compaction.lag.ms
                                       max.message.bytes
                                       message.timestamp.after.max.ms
                                       message.timestamp.before.max.ms
                                       message.timestamp.type
                                       min.cleanable.dirty.ratio
                                       min.compaction.lag.ms
                                       min.insync.replicas
                                       preallocate
                                       remote.log.copy.disable
                                       remote.log.delete.on.disable
                                       remote.storage.enable
                                       retention.bytes
                                       retention.ms
                                       segment.bytes
                                       segment.index.bytes
                                       segment.jitter.ms
                                       segment.ms
                                       unclean.leader.election.enable
                                       For entity-type 'brokers':
                                       background.threads
                                       compression.gzip.level
                                       compression.lz4.level
                                       compression.type
                                       compression.zstd.level
                                       follower.replication.throttled.rate
                                       leader.replication.throttled.rate
                                       listener.security.protocol.map
                                       listeners
                                       log.cleaner.backoff.ms
                                       log.cleaner.dedupe.buffer.size
                                       log.cleaner.delete.retention.ms
                                       log.cleaner.io.buffer.load.factor
                                       log.cleaner.io.buffer.size
                                       log.cleaner.io.max.bytes.per.second
                                       log.cleaner.max.compaction.lag.ms
                                       log.cleaner.min.cleanable.ratio
                                       log.cleaner.min.compaction.lag.ms
                                       log.cleaner.threads
                                       log.cleanup.policy
                                       log.flush.interval.messages
                                       log.flush.interval.ms
                                       log.index.interval.bytes
                                       log.index.size.max.bytes
                                       log.local.retention.bytes
                                       log.local.retention.ms
                                       log.message.timestamp.after.max.ms
                                       log.message.timestamp.before.max.ms
                                       log.message.timestamp.type
                                       log.preallocate
                                       log.retention.bytes
                                       log.retention.ms
                                       log.roll.jitter.ms
                                       log.roll.ms
                                       log.segment.bytes
                                       log.segment.delete.delay.ms
                                       max.connection.creation.rate
                                       max.connections
                                       max.connections.per.ip
                                       max.connections.per.ip.overrides
                                       message.max.bytes
                                       metric.reporters
                                       min.insync.replicas
                                       num.io.threads
                                       num.network.threads
                                       num.recovery.threads.per.data.dir
                                       num.replica.fetchers
                                       principal.builder.class
                                       producer.id.expiration.ms
                                       remote.fetch.max.wait.ms
                                       remote.list.offsets.request.timeout.ms
                                       remote.log.index.file.cache.total.
                                       size.bytes
                                       remote.log.manager.copier.thread.pool.
                                       size
                                       remote.log.manager.copy.max.bytes.per.
                                       second
                                       remote.log.manager.expiration.thread.
                                       pool.size
                                       remote.log.manager.fetch.max.bytes.
                                       per.second
                                       remote.log.reader.threads
                                       replica.alter.log.dirs.io.max.bytes.
                                       per.second
                                       sasl.enabled.mechanisms
                                       sasl.jaas.config
                                       sasl.kerberos.kinit.cmd
                                       sasl.kerberos.min.time.before.relogin
                                       sasl.kerberos.principal.to.local.rules
                                       sasl.kerberos.service.name
                                       sasl.kerberos.ticket.renew.jitter
                                       sasl.kerberos.ticket.renew.window.
                                       factor
                                       sasl.login.refresh.buffer.seconds
                                       sasl.login.refresh.min.period.seconds
                                       sasl.login.refresh.window.factor
                                       sasl.login.refresh.window.jitter
                                       sasl.mechanism.inter.broker.protocol
                                       ssl.cipher.suites
                                       ssl.client.auth
                                       ssl.enabled.protocols
                                       ssl.endpoint.identification.algorithm
                                       ssl.engine.factory.class
                                       ssl.key.password
                                       ssl.keymanager.algorithm
                                       ssl.keystore.certificate.chain
                                       ssl.keystore.key
                                       ssl.keystore.location
                                       ssl.keystore.password
                                       ssl.keystore.type
                                       ssl.protocol
                                       ssl.provider
                                       ssl.secure.random.implementation
                                       ssl.trustmanager.algorithm
                                       ssl.truststore.certificates
                                       ssl.truststore.location
                                       ssl.truststore.password
                                       ssl.truststore.type
                                       transaction.partition.verification.
                                       enable
                                       unclean.leader.election.enable
                                       For entity-type 'users':
                                       SCRAM-SHA-256
                                       SCRAM-SHA-512
                                       consumer_byte_rate
                                       controller_mutation_rate
                                       producer_byte_rate
                                       request_percentage
                                       For entity-type 'clients':
                                       consumer_byte_rate
                                       controller_mutation_rate
                                       producer_byte_rate
                                       request_percentage
                                       For entity-type 'ips':
                                       connection_creation_rate
                                       For entity-type 'client-metrics':
                                       interval.ms
                                       match
                                       metrics
                                       For entity-type 'groups':
                                       consumer.heartbeat.interval.ms
                                       consumer.session.timeout.ms
                                       share.auto.offset.reset
                                       share.heartbeat.interval.ms
                                       share.record.lock.duration.ms
                                       share.session.timeout.ms
                                       Entity types 'users' and 'clients' may
                                       be specified together to update
                                       config for clients of a specific
                                       user.
--add-config-file <String>             Path to a properties file with configs
                                       to add. See add-config for a list of
                                       valid configurations.
--all                                  List all configs for the given topic,
                                       broker, or broker-logger entity
                                       (includes static configuration when
                                       the entity type is brokers)
--alter                                Alter the configuration for the entity.
--bootstrap-controller <String:        The Kafka controllers to connect to.
controller to connect to>
--bootstrap-server <String: server to  The Kafka servers to connect to.
connect to>
--broker <String>                      The broker's ID.
--broker-defaults                      The config defaults for all brokers.
--broker-logger <String>               The broker's ID for its logger config.
--client <String>                      The client's ID.
--client-defaults                      The config defaults for all clients.
--client-metrics <String>              The client metrics config resource
                                       name.
--command-config <String: command      Property file containing configs to be
config property file>                  passed to Admin Client. This is used
                                       only with --bootstrap-server option
                                       for describing and altering broker
                                       configs.
--delete-config <String>               config keys to remove 'k1,k2'
--describe                             List configs for the given entity.
--entity-default                       Default entity name for
                                       clients/users/brokers/ips (applies
                                       to corresponding entity type in
                                       command line)
--entity-name <String>                 Name of entity (topic name/client
                                       id/user principal name/broker
                                       id/ip/client metrics)
--entity-type <String>                 Type of entity
                                       (topics/clients/users/brokers/broker-
                                       loggers/ips/client-metrics)
--force                                Suppress console prompts
--group <String>                       The group ID.
--help                                 Print usage information.
--ip <String>                          The IP address.
--ip-defaults                          The config defaults for all IPs.
--topic <String>                       The topic's name.
--user <String>                        The user's principal name.
--user-defaults                        The config defaults for all users.
--version                              Display Kafka version.
```

### kafka-get-offsets.sh

Use the `kafka-get-offsets` tool to retrieve topic-partition offsets.

### **Usage details**

```bash
An interactive shell for getting topic-partition offsets.

Option                                   Description
------                                   -----------
--bootstrap-server <String: HOST1:       REQUIRED. The server(s) to connect to
  PORT1,...,HOST3:PORT3>                 in the form HOST1:PORT1,HOST2:PORT2.
--broker-list <String: HOST1:PORT1,...,  DEPRECATED, use --bootstrap-server
  HOST3:PORT3>                             instead; ignored if --bootstrap-
                                          server is specified. The server(s)
                                          to connect to in the form HOST1:
                                          PORT1,HOST2:PORT2.
--command-config <String: config file>   Property file containing configs to be
                                          passed to Admin Client.
--exclude-internal-topics                By default, internal topics are
                                          included. If specified, internal
                                          topics are excluded.
--help                                   Print usage information.
--partitions <String: partition ids>     Comma separated list of partition ids
                                          to get the offsets for. If not
                                          present, all partitions of the
                                          authorized topics are queried.
                                          Cannot be used if --topic-partitions
                                          is present.
--time <String: <timestamp> / -1 or      timestamp of the offsets before that.
  latest / -2 or earliest / -3 or max-     [Note: No offset is returned, if the
  timestamp>                               timestamp greater than recently
                                          committed record timestamp is
                                          given.] (default: latest)
--topic <String: topic>                  The topic to get the offsets for. It
                                          also accepts a regular expression.
                                          If not present, all authorized
                                          topics are queried. Cannot be used
                                          if --topic-partitions is present.
--topic-partitions <String: topic1:1,    Comma separated list of topic-
  topic2:0-3,topic3,topic4:5-,topic5:-3    partition patterns to get the
  >                                        offsets for, with the format of:
                                          ([^:,]*)(?::(?:([0-9]*)|(?:([0-9]*)
                                          -([0-9]*))))?. The first group is
                                          an optional regex for the topic
                                          name, if omitted, it matches any
                                          topic name. The section after ':'
                                          describes a partition pattern,
                                          which can be: a number, a range in
                                          the format of NUMBER-NUMBER (lower
                                          inclusive, upper exclusive), an
                                          inclusive lower bound in the format
                                          of NUMBER-, an exclusive upper
                                          bound in the format of -NUMBER or
                                          may be omitted to accept all
                                          partitions.
--version                                Display Kafka version.
```

### kafka-leader-election.sh

Use the `kafka-leader-election` tool to attempt to elect a new leader for a set of topic partitions.

Run this tool manually to restore leadership if the `auto.leader.rebalance.enable` property is set to `false`.

### **Usage details**

```bash
This tool attempts to elect a new leader for a set of topic partitions. The type of elections supported are preferred replicas and unclean replicas.
Option                                  Description
------                                  -----------
--admin.config <String: config file>    Configuration properties files to pass
                                          to the admin client
--all-topic-partitions                  Perform election on all of the
                                          eligible topic partitions based on
                                          the type of election (see the --
                                          election-type flag). Not allowed if
                                          --topic or --path-to-json-file is
                                          specified.
--bootstrap-server <String: host:port>  A hostname and port for the broker to
                                          connect to, in the form host:port.
                                          Multiple comma separated URLs can be
                                          given. REQUIRED.
--election-type <[PREFERRED,UNCLEAN]:   Type of election to attempt. Possible
  election type>                          values are "preferred" for preferred
                                          leader election or "unclean" for
                                          unclean leader election. If
                                          preferred election is selection, the
                                          election is only performed if the
                                          current leader is not the preferred
                                          leader for the topic partition. If
                                          unclean election is selected, the
                                          election is only performed if there
                                          are no leader for the topic
                                          partition. REQUIRED.
--help                                  Print usage information.
--partition <Integer: partition id>     Partition id for which to perform an
                                          election. REQUIRED if --topic is
                                          specified.
--path-to-json-file <String: Path to    The JSON file with the list  of
  JSON file>                              partition for which leader elections
                                          should be performed. This is an
                                          example format.
                                        {"partitions":
                                                [{"topic": "foo", "partition": 1},
                                                {"topic": "foobar", "partition": 2}]
                                        }
                                        Not allowed if --all-topic-partitions
                                          or --topic flags are specified.
--topic <String: topic name>            Name of topic for which to perform an
                                          election. Not allowed if --path-to-
                                          json-file or --all-topic-partitions
                                          is specified.
--version                               Display Kafka version.
```

### kafka-transactions.sh

Use the `kafka-transactions` tool to list and describe transactions. Use to detect and abort hanging transactions.
For more information, see [Detect and Abort Hanging Transactions](https://cwiki.apache.org/confluence/display/KAFKA/KIP-664%3A+Provide+tooling+to+detect+and+abort+hanging+transactions#KIP664:Providetoolingtodetectandaborthangingtransactions-CommandLineTool)

### **Usage details**

```bash
usage: kafka-transactions.sh [-h] [-v] [--command-config FILE] --bootstrap-server host:port COMMAND ...

This tool is used to analyze the transactional state  of  producers  in  the  cluster. It can be used to detect and
recover from hanging transactions.

optional arguments:
  -h, --help             show this help message and exit
  -v, --version          show the version of this Kafka distribution and exit
  --command-config FILE  property file containing configs to be passed to admin client
  --bootstrap-server host:port
                        hostname and port for the broker to connect  to, in the form `host:port`
                       (multiple comma-separated entries can be given)

commands:
    list                 list transactions
    describe             describe the state of an active transactional-id
    describe-producers   describe the states of active producers for a topic partition
    abort                abort a hanging transaction (requires administrative privileges)
    find-hanging         find hanging transactions
```

### kafka-reassign-partitions.sh

Use the `kafka-reassign-partitions` to move topic partitions between replicas
You pass a JSON-formatted file to specify the new replicas. To learn more,
see [Changing the replication factor](/platform/current/kafka/post-deployment.html#changing-the-replication-factor)
in the Confluent documentation.

### **Usage details**

```bash
This tool helps to move topic partitions between replicas.

Option                                  Description
------                                  -----------
--additional                            Execute this reassignment in addition
                                          to any other ongoing ones. This
                                          option can also be used to change
                                          the throttle of an ongoing
                                          reassignment.

--bootstrap-controller                   The controller to use for reassignment.
[String: bootstrap controller            By default, the tool will get the quorum controller. This
to connect to]                           option supports the actions --cancel and --list.

--bootstrap-server <String: Server(s)   REQUIRED: the server(s) to use for
  to use for bootstrapping>               bootstrapping.
--broker-list <String: brokerlist>      The list of brokers to which the
                                          partitions need to be reassigned in
                                          the form "0,1,2". This is required
                                          if --topics-to-move-json-file is
                                          used to generate reassignment
                                          configuration
--cancel                                Cancel an active reassignment.
--command-config <String: Admin client  Property file containing configs to be
  property file>                          passed to Admin Client.
--disable-rack-aware                    Disable rack aware replica assignment
--execute                               Kick off the reassignment as specified
                                          by the --reassignment-json-file
                                          option.
--generate                              Generate a candidate partition
                                          reassignment configuration. Note
                                          that this only generates a candidate
                                          assignment, it does not execute it.
--help                                  Print usage information.
--list                                  List all active partition
                                          reassignments.
--preserve-throttles                    Do not modify broker or topic
                                          throttles.
--reassignment-json-file <String:       The JSON file with the partition
  manual assignment json file path>       reassignment configurationThe format
                                          to use is -
                                        {"partitions":
                                                [{"topic": "foo",
                                                  "partition": 1,
                                                  "replicas": [1,2,3,4],
                                                  "observers":[3,4],
                                                  "log_dirs": ["dir1","dir2","dir3","
                                          dir4"] }],
                                        "version":1
                                        }
                                        Note that "log_dirs" is optional. When
                                          it is specified, its length must
                                          equal the length of the replicas
                                          list. The value in this list can be
                                          either "any" or the absolution path
                                          of the log directory on the broker.
                                          If absolute log directory path is
                                          specified, the replica will be moved
                                          to the specified log directory on
                                          the broker.
                                        Note that  "observers" is optional.
                                          When it is specified it must be a
                                          suffix of the replicas list.
--replica-alter-log-dirs-throttle       The movement of replicas between log
  <Long: replicaAlterLogDirsThrottle>     directories on the same broker will
                                          be throttled to this value
                                          (bytes/sec). This option can be
                                          included with --execute when a
                                          reassignment is started, and it can
                                          be altered by resubmitting the
                                          current reassignment along with the
                                          --additional flag. The throttle rate
                                          should be at least 1 KB/s. (default:
                                          -1)
--throttle <Long: throttle>             The movement of partitions between
                                          brokers will be throttled to this
                                          value (bytes/sec). This option can
                                          be included with --execute when a
                                          reassignment is started, and it can
                                          be altered by resubmitting the
                                          current reassignment along with the
                                          --additional flag. The throttle rate
                                          should be at least 1 KB/s. (default:
                                          -1)
--timeout <Long: timeout>               The maximum time in ms to wait for log
                                          directory replica assignment to
                                          begin. (default: 10000)
--topics-to-move-json-file <String:     Generate a reassignment configuration
  topics to reassign json file path>      to move the partitions of the
                                          specified topics to the list of
                                          brokers specified by the --broker-
                                          list option. The format to use is -
                                        {"topics":
                                                [{"topic": "foo"},{"topic": "foo1"}],
                                        "version":1
                                        }
--verify                                Verify if the reassignment completed
                                          as specified by the --reassignment-
                                          json-file option. If there is a
                                          throttle engaged for the replicas
                                          specified, and the rebalance has
                                          completed, the throttle will be
                                          removed
--version                               Display Kafka version.
```

### kafka-delete-records.sh

Use the `kafka-delete-records` tool to delete partition records. Use this if a topic receives bad data.
Pass a JSON-formatted file that specifies the topic, partition, and offset for data deletion. Data will be deleted up to the offset specified.
Example:

```bash
bin/kafka-delete-records.sh --bootstrap-server host1:9092 --offset-json-file deleteme.json
```

### **Usage details**

```bash
This tool helps to delete records of the given partitions down to the specified offset.

Option                                 Description
------                                 -----------
--bootstrap-server <String: server(s)  REQUIRED: The server to connect to.
  to use for bootstrapping>
--command-config <String: command      A property file containing configs to
  config property file path>             be passed to Admin Client.
--help                                 Print usage information.
--offset-json-file <String: Offset     REQUIRED: The JSON file with offset
  json file path>                        per partition. The format to use is:
                                      {"partitions":
                                        [{"topic": "foo", "partition": 1,
                                        "offset": 1}],
                                        "version":1
                                      }
--version                              Display Kafka version.
```

### kafka-log-dirs.sh

Use the `kafka-log-dirs` tool to get a list of replicas per log directory on a broker.

### **Usage details**

```bash
This tool helps to query log directory usage on the specified brokers.

------                                  -----------
--bootstrap-server <String: The server  REQUIRED: the server(s) to use for
  (s) to use for bootstrapping>           bootstrapping
--broker-list <String: Broker list>     The list of brokers to be queried in
                                          the form "0,1,2". All brokers in the
                                          cluster will be queried if no broker
                                          list is specified
--command-config <String: Admin client  Property file containing configs to be
  property file>                          passed to Admin Client.
--describe                              Describe the specified log directories
                                          on the specified brokers.
--help                                  Print usage information.
--topic-list <String: Topic list>       The list of topics to be queried in
                                          the form "topic1,topic2,topic3". All
                                          topics will be queried if no topic
                                          list is specified (default: )
--version                               Display Kafka version.
```

### kafka-replica-verification.sh

Use the `kafka-replica-verification` tool to verify that all replicas of a topic contain the same data.
Requires a `broker-list` parameter that contains a comma-separated list of `<hostname:port>` entries specifying the server/port to connect to.

### **Usage details**

```bash
Validate that all replicas for a set of topics have the same data.

Option                                  Description
------                                  -----------
--broker-list <String: hostname:        REQUIRED: The list of hostname and
  port,...,hostname:port>                 port of the server to connect to.
--fetch-size <Integer: bytes>           The fetch size of each request.
                                          (default: 1048576)
--help                                  Print usage information.
--max-wait-ms <Integer: ms>             The max amount of time each fetch
                                          request waits. (default: 1000)
--report-interval-ms <Long: ms>         The reporting interval. (default:
                                          30000)
--time <Long: timestamp/-1(latest)/-2   Timestamp for getting the initial
  (earliest)>                             offsets. (default: -1)
--topic-white-list <String: Java regex  DEPRECATED use --topics-include
  (String)>                               instead; ignored if --topics-include
                                          specified. List of topics to verify
                                          replica consistency. Defaults to '.
                                          *' (all topics) (default: .*)
--topics-include <String: Java regex    List of topics to verify replica
  (String)>                               consistency. Defaults to '.*' (all
                                          topics) (default: .*)
--version                               Print version information and exit.
```

### kafka-mirror-maker.sh

DEPRECATED: For an alternative, see [connect-mirror-maker.sh](#mirror-maker-2). Enables the creation of a replica of an existing Kafka cluster.
Example: `bin/connect-mirror-maker.sh connect-mirror-maker.properties --clusters secondary`.
Learn more [Kafka mirroring](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27846330)

### **Usage details**

```bash
This tool helps to continuously copy data between two Kafka clusters.
Option                                   Description
------                                   -----------
--abort.on.send.failure <String: Stop    Configure the mirror maker to exit on
  the entire mirror maker when a send      a failed send. (default: true)
  failure occurs>
--consumer.config <String: config file>  Embedded consumer config for consuming
                                          from the source cluster.
--consumer.rebalance.listener <String:   The consumer rebalance listener to use
  A custom rebalance listener of type      for mirror maker consumer.
  ConsumerRebalanceListener>
--help                                   Print usage information.
--include <String: Java regex (String)>  List of included topics to mirror.
--message.handler <String: A custom      Message handler which will process
  message handler of type                  every record in-between consumer and
  MirrorMakerMessageHandler>               producer.
--message.handler.args <String:          Arguments used by custom message
  Arguments passed to message handler      handler for mirror maker.
  constructor.>
--new.consumer                           DEPRECATED Use new consumer in mirror
                                          maker (this is the default so this
                                          option will be removed in a future
                                          version).
--num.streams <Integer: Number of        Number of consumption streams.
  threads>                                 (default: 1)
--offset.commit.interval.ms <Integer:    Offset commit interval in ms.
  offset commit interval in                (default: 60000)
  millisecond>
--producer.config <String: config file>  Embedded producer config.
--rebalance.listener.args <String:       Arguments used by custom rebalance
  Arguments passed to custom rebalance     listener for mirror maker consumer.
  listener constructor as a string.>
--version                                Display Kafka version.
--whitelist <String: Java regex          DEPRECATED, use --include instead;
  (String)>                                ignored if --include specified. List
                                          of included topics to mirror.
```

<a id="mirror-maker-2"></a>

### connect-mirror-maker.sh

Use the `connect-mirror-maker` tool to replicate topics from one cluster to another using the Connect framework.
You must pass an an `mm2.properties` MM2 configuration file. For more information, see
[KIP-382: MirrorMaker 2.0](https://cwiki.apache.org/confluence/display/KAFKA/KIP-382%3A+MirrorMaker+2.0)
or [Getting up to speed with MirrorMaker 2](https://www.confluent.io/resources/kafka-summit-2020/getting-up-to-speed-with-mirrormaker-2/).

### **Usage details**

```bash
usage: connect-mirror-maker [-h] [--clusters CLUSTER [CLUSTER ...]] mm2.properties

MirrorMaker 2.0 driver

positional arguments:
  mm2.properties         MM2 configuration file.

optional arguments:
  -h, --help             show this help message and exit
  --clusters CLUSTER [CLUSTER ...]
                        Target cluster to use for this node.
```

<a id="client-producer-consumer-tools"></a>

## Client, producer, and consumer tools

### kafka-client-metrics.sh

Use the `kafka-client-metrics` tool to manipulate and describe client metrics configurations for clusters
where client metrics are enabled. This tool
provides a simpler alternative to using `kafka-configs.sh` to configure client metrics.

For example, to list all of the client metric configuration resource, use the following command:

```none
kafka-client-metrics.sh --bootstrap-server HOST1:PORT1 --describe
```

To describe a specific configuration:

```none
kafka-client-metrics.sh --bootstrap-server HOST1:PORT1 --describe --name MYMETRICS
```

You can use this tool to create a client metric configuration resource and generate a unique name.
In this example, `--generate-name` is used to create a type-4 UUID to use as
the client metrics configuration resource name:

```none
kafka-client-metrics.sh --bootstrap-server HOST1:PORT1  --alter --generate-name \
--metrics org.apache.kafka.producer.node.request.latency.,org.apache.kafka.consumer.node.request.latency. \
--interval 60000
```

### **Usage details**

```bash
Option                                 Description
------                                 -----------
--alter                                Alter the configuration for the client
                                        metrics resource.
--bootstrap-server <String: server to  REQUIRED: The Kafka server to connect
  connect to>                            to.
--command-config <String: command      Property file containing configs to be
  config property file>                  passed to Admin Client.
--delete                               Delete the configuration for the
                                        client metrics resource.
--describe                             List configurations for the client
                                        metrics resource.
--generate-name                        Generate a UUID to use as the name.
--help                                 Print usage information.
--interval <Integer: push interval>    The metrics push interval in
                                        milliseconds.
--list                                 List the client metrics resources.
--match <String: k1=v1,k2=v2>          Matching selector 'k1=v1,k2=v2'. The
                                        following is a list of valid
                                        selector names:
                                        client_id
                                        client_instance_id
                                        client_software_name
                                        client_software_version
                                        client_source_address
                                        client_source_port
--metrics <String: m1,m2>              Telemetry metric name prefixes 'm1,m2'.
--name <String: name>                  Name of client metrics configuration
                                        resource.
--version                              Display Kafka version.
```

### kafka-verifiable-consumer.sh

The `kafka-verifiable-consumer` tool consumes messages from a topic and emits consumer events as JSON objects to STDOUT. For example, group rebalances, received messages, and offsets committed.
Intended for internal testing.

### **Usage details**

```bash
usage: verifiable-consumer [-h] --topic TOPIC --group-id GROUP_ID
                          [--group-instance-id GROUP_INSTANCE_ID]
                          [--max-messages MAX-MESSAGES] [--session-timeout TIMEOUT_MS]
                          [--verbose] [--enable-autocommit] [--send-offset-for-times-data]
                          [--reset-policy RESETPOLICY]
                          [--assignment-strategy ASSIGNMENTSTRATEGY]
                          [--consumer.config CONFIG_FILE]
                          (--bootstrap-server HOST1:PORT1[,HOST2:PORT2[...]] |
                          --broker-list HOST1:PORT1[,HOST2:PORT2[...]])

This tool consumes messages  from  a  specific  topic  and  emits  consumer  events (e.g. group
rebalances, received messages, and offsets committed) as JSON objects to STDOUT.

optional arguments:
  -h, --help             show this help message and exit
  --topic TOPIC          Consumes messages from this topic.
  --group-protocol GROUP_PROTOCOL
                        Group protocol (must be one of CLASSIC, CONSUMER) (default: classic)
  --group-remote-assignor GROUP_REMOTE_ASSIGNOR
                        Group remote assignor; only used if the group protocol is CONSUMER
  --group-id GROUP_ID    The groupId shared among members of the consumer group
  --group-instance-id GROUP_INSTANCE_ID
                        A unique identifier of the consumer instance
  --max-messages MAX-MESSAGES
                        Consume this many messages.  If  -1  (the  default), the consumer will
                        consume until the process is killed externally (default: -1)
  --session-timeout TIMEOUT_MS
                        Set the consumer's session timeout (default: 30000)
  --verbose              Enable to log individual consumed records (default: false)
  --enable-autocommit    Enable offset auto-commit on consumer (default: false)
  --reset-policy RESETPOLICY
                        Set reset policy  (must  be  either  'earliest',  'latest',  or 'none'
                        (default: earliest)
  --assignment-strategy ASSIGNMENTSTRATEGY
                        Set  assignment   strategy   (e.g.  org.apache.kafka.clients.consumer.
                        RoundRobinAssignor)    (default:    org.apache.kafka.clients.consumer.
                        RangeAssignor)
  --consumer.config CONFIG_FILE
                        Consumer config properties file  (config  options  shared with command
                        line parameters will be overridden).

Connection Group:
  Group of arguments for connection to brokers

  --bootstrap-server HOST1:PORT1[,HOST2:PORT2[...]]
                        REQUIRED unless --broker-list(deprecated) is  specified. The server(s)
                        to connect to.  Comma-separated  list  of  Kafka  brokers  in the form
                        HOST1:PORT1,HOST2:PORT2,...
  --broker-list HOST1:PORT1[,HOST2:PORT2[...]]
                        DEPRECATED, use --bootstrap-server  instead;  ignored  if --bootstrap-
                        server is specified.  Comma-separated  list  of  Kafka  brokers in the
                        form HOST1:PORT1,HOST2:PORT2,...
```

### kafka-configs.sh

Use the `kafka-configs` tool to change and describe topic, client, user, broker, IP configuration setting or
KRaft controller.
To describe or view a KRaft controller, use the `--bootstrap-controller` option, and do not specify a `bootstrap-server`.

To change a property, specify the `entity-type` to the desired entity (topic, broker, user, etc), and use the
`alter` option. The following example shows how you might add the `delete.retention` configuration property for a topic with `kafka-configs`.

```none
/bin/kafka-configs.sh --bootstrap-server host1:9092 --entity-type topics --entity-default --alter --add-config delete.retention.ms=172800000
```

When you use the `--add-config` flag to add multiple values, use square brackets around the comma-separated list
like the following example:

```none
/bin/kafka-configs.sh --bootstrap-server host1:9092 --alter --add-config max.connections.per.ip.overrides=[host1:50,host2:9] --entity-type brokers --entity-default
```

The following example shows how you might check the cluster ID, by specifying the `--bootstrap-controller` option.

```none
/bin/kafka-cluster.sh cluster-id --bootstrap-controller localhost:9092
```

See [Kafka Topic Operations](topic-operations.md#topic-operations) for more examples of how to work with topics.

### **Usage details**

```bash
This tool helps to manipulate and describe entity config for a topic, client, user, broker, ip or client-metrics

Option                                 Description
------                                 -----------
--add-config <String>                  Key Value pairs of configs to add.
                                       Square brackets can be used to group
                                       values which contain commas: 'k1=v1,
                                       k2=[v1,v2,v2],k3=v3'. The following
                                       is a list of valid configurations:
                                       For entity-type 'topics':
                                       cleanup.policy
                                       compression.gzip.level
                                       compression.lz4.level
                                       compression.type
                                       compression.zstd.level
                                       delete.retention.ms
                                       file.delete.delay.ms
                                       flush.messages
                                       flush.ms
                                       follower.replication.throttled.
                                       replicas
                                       index.interval.bytes
                                       leader.replication.throttled.replicas
                                       local.retention.bytes
                                       local.retention.ms
                                       max.compaction.lag.ms
                                       max.message.bytes
                                       message.timestamp.after.max.ms
                                       message.timestamp.before.max.ms
                                       message.timestamp.type
                                       min.cleanable.dirty.ratio
                                       min.compaction.lag.ms
                                       min.insync.replicas
                                       preallocate
                                       remote.log.copy.disable
                                       remote.log.delete.on.disable
                                       remote.storage.enable
                                       retention.bytes
                                       retention.ms
                                       segment.bytes
                                       segment.index.bytes
                                       segment.jitter.ms
                                       segment.ms
                                       unclean.leader.election.enable
                                       For entity-type 'brokers':
                                       background.threads
                                       compression.gzip.level
                                       compression.lz4.level
                                       compression.type
                                       compression.zstd.level
                                       follower.replication.throttled.rate
                                       leader.replication.throttled.rate
                                       listener.security.protocol.map
                                       listeners
                                       log.cleaner.backoff.ms
                                       log.cleaner.dedupe.buffer.size
                                       log.cleaner.delete.retention.ms
                                       log.cleaner.io.buffer.load.factor
                                       log.cleaner.io.buffer.size
                                       log.cleaner.io.max.bytes.per.second
                                       log.cleaner.max.compaction.lag.ms
                                       log.cleaner.min.cleanable.ratio
                                       log.cleaner.min.compaction.lag.ms
                                       log.cleaner.threads
                                       log.cleanup.policy
                                       log.flush.interval.messages
                                       log.flush.interval.ms
                                       log.index.interval.bytes
                                       log.index.size.max.bytes
                                       log.local.retention.bytes
                                       log.local.retention.ms
                                       log.message.timestamp.after.max.ms
                                       log.message.timestamp.before.max.ms
                                       log.message.timestamp.type
                                       log.preallocate
                                       log.retention.bytes
                                       log.retention.ms
                                       log.roll.jitter.ms
                                       log.roll.ms
                                       log.segment.bytes
                                       log.segment.delete.delay.ms
                                       max.connection.creation.rate
                                       max.connections
                                       max.connections.per.ip
                                       max.connections.per.ip.overrides
                                       message.max.bytes
                                       metric.reporters
                                       min.insync.replicas
                                       num.io.threads
                                       num.network.threads
                                       num.recovery.threads.per.data.dir
                                       num.replica.fetchers
                                       principal.builder.class
                                       producer.id.expiration.ms
                                       remote.fetch.max.wait.ms
                                       remote.list.offsets.request.timeout.ms
                                       remote.log.index.file.cache.total.
                                       size.bytes
                                       remote.log.manager.copier.thread.pool.
                                       size
                                       remote.log.manager.copy.max.bytes.per.
                                       second
                                       remote.log.manager.expiration.thread.
                                       pool.size
                                       remote.log.manager.fetch.max.bytes.
                                       per.second
                                       remote.log.reader.threads
                                       replica.alter.log.dirs.io.max.bytes.
                                       per.second
                                       sasl.enabled.mechanisms
                                       sasl.jaas.config
                                       sasl.kerberos.kinit.cmd
                                       sasl.kerberos.min.time.before.relogin
                                       sasl.kerberos.principal.to.local.rules
                                       sasl.kerberos.service.name
                                       sasl.kerberos.ticket.renew.jitter
                                       sasl.kerberos.ticket.renew.window.
                                       factor
                                       sasl.login.refresh.buffer.seconds
                                       sasl.login.refresh.min.period.seconds
                                       sasl.login.refresh.window.factor
                                       sasl.login.refresh.window.jitter
                                       sasl.mechanism.inter.broker.protocol
                                       ssl.cipher.suites
                                       ssl.client.auth
                                       ssl.enabled.protocols
                                       ssl.endpoint.identification.algorithm
                                       ssl.engine.factory.class
                                       ssl.key.password
                                       ssl.keymanager.algorithm
                                       ssl.keystore.certificate.chain
                                       ssl.keystore.key
                                       ssl.keystore.location
                                       ssl.keystore.password
                                       ssl.keystore.type
                                       ssl.protocol
                                       ssl.provider
                                       ssl.secure.random.implementation
                                       ssl.trustmanager.algorithm
                                       ssl.truststore.certificates
                                       ssl.truststore.location
                                       ssl.truststore.password
                                       ssl.truststore.type
                                       transaction.partition.verification.
                                       enable
                                       unclean.leader.election.enable
                                       For entity-type 'users':
                                       SCRAM-SHA-256
                                       SCRAM-SHA-512
                                       consumer_byte_rate
                                       controller_mutation_rate
                                       producer_byte_rate
                                       request_percentage
                                       For entity-type 'clients':
                                       consumer_byte_rate
                                       controller_mutation_rate
                                       producer_byte_rate
                                       request_percentage
                                       For entity-type 'ips':
                                       connection_creation_rate
                                       For entity-type 'client-metrics':
                                       interval.ms
                                       match
                                       metrics
                                       For entity-type 'groups':
                                       consumer.heartbeat.interval.ms
                                       consumer.session.timeout.ms
                                       share.auto.offset.reset
                                       share.heartbeat.interval.ms
                                       share.record.lock.duration.ms
                                       share.session.timeout.ms
                                       Entity types 'users' and 'clients' may
                                       be specified together to update
                                       config for clients of a specific
                                       user.
--add-config-file <String>             Path to a properties file with configs
                                       to add. See add-config for a list of
                                       valid configurations.
--all                                  List all configs for the given topic,
                                       broker, or broker-logger entity
                                       (includes static configuration when
                                       the entity type is brokers)
--alter                                Alter the configuration for the entity.
--bootstrap-controller <String:        The Kafka controllers to connect to.
controller to connect to>
--bootstrap-server <String: server to  The Kafka servers to connect to.
connect to>
--broker <String>                      The broker's ID.
--broker-defaults                      The config defaults for all brokers.
--broker-logger <String>               The broker's ID for its logger config.
--client <String>                      The client's ID.
--client-defaults                      The config defaults for all clients.
--client-metrics <String>              The client metrics config resource
                                       name.
--command-config <String: command      Property file containing configs to be
config property file>                  passed to Admin Client. This is used
                                       only with --bootstrap-server option
                                       for describing and altering broker
                                       configs.
--delete-config <String>               config keys to remove 'k1,k2'
--describe                             List configs for the given entity.
--entity-default                       Default entity name for
                                       clients/users/brokers/ips (applies
                                       to corresponding entity type in
                                       command line)
--entity-name <String>                 Name of entity (topic name/client
                                       id/user principal name/broker
                                       id/ip/client metrics)
--entity-type <String>                 Type of entity
                                       (topics/clients/users/brokers/broker-
                                       loggers/ips/client-metrics)
--force                                Suppress console prompts
--group <String>                       The group ID.
--help                                 Print usage information.
--ip <String>                          The IP address.
--ip-defaults                          The config defaults for all IPs.
--topic <String>                       The topic's name.
--user <String>                        The user's principal name.
--user-defaults                        The config defaults for all users.
--version                              Display Kafka version.
```

### kafka-verifiable-producer.sh

The `kafka-verifiable-producer` tool produces increasing integers to the specified topic and prints JSON metadata to STDOUT on each `send` request.
This tool shows which messages have been acked and which have not. This tool is intended for internal testing.

### **Usage details**

```bash
usage: verifiable-producer [-h] --topic TOPIC [--max-messages MAX-MESSAGES]
                     [--throughput THROUGHPUT] [--acks ACKS]
                     [--producer.config CONFIG_FILE] [--message-create-time CREATETIME]
                     [--value-prefix VALUE-PREFIX] [--repeating-keys REPEATING-KEYS]
                     (--bootstrap-server HOST1:PORT1[,HOST2:PORT2[...]] |
                     --broker-list HOST1:PORT1[,HOST2:PORT2[...]])

This tool produces increasing integers  to  the  specified  topic  and  prints JSON metadata to
stdout on each "send" request, making  externally  visible  which  messages have been acked and
which have not.

optional arguments:
  -h, --help             show this help message and exit
  --topic TOPIC          Produce messages to this topic.
  --max-messages MAX-MESSAGES
                        Produce this many messages. If -1,  produce messages until the process
                        is killed externally. (default: -1)
  --throughput THROUGHPUT
                        If set >= 0,  throttle  maximum  message throughput to *approximately*
                        THROUGHPUT messages/sec. (default: -1)
  --acks ACKS            Acks required on each produced  message.  See  Kafka  docs on acks for
                        details. (default: -1)
  --producer.config CONFIG_FILE
                        Producer config properties file.
  --message-create-time CREATETIME
                        Send messages with creation time  starting  at the arguments value, in
                        milliseconds since epoch (default: -1)
  --value-prefix VALUE-PREFIX
                        If specified, each produced value  will  have  this  prefix with a dot
                        separator
  --repeating-keys REPEATING-KEYS
                        If specified, each produced  record  will  have  a  key  starting at 0
                        increment by 1 up to  the  number  specified (exclusive), then the key
                        is set to 0 again

Connection Group:
  Group of arguments for connection to brokers

  --bootstrap-server HOST1:PORT1[,HOST2:PORT2[...]]
                        REQUIRED: The server(s) to connect  to.  Comma-separated list of Kafka
                        brokers in the form HOST1:PORT1,HOST2:PORT2,...
  --broker-list HOST1:PORT1[,HOST2:PORT2[...]]
                        DEPRECATED, use --bootstrap-server  instead;  ignored  if --bootstrap-
                        server is specified.  Comma-separated  list  of  Kafka  brokers in the
                        form HOST1:PORT1,HOST2:PORT2,...
```

### kafka-verifiable-share-consumer.sh

This tool creates a share group and consumes messages from a specific topic. It outputs share consumer events, such as share consumer startup, received messages, and offsets acknowledged, as JSON objects to `STDOUT`.

### **Usage details**

```bash
usage: verifiable-share-consumer [-h] --topic TOPIC --group-id GROUP_ID
                                 [--max-messages MAX-MESSAGES] [--verbose]
                                 [--acknowledgement-mode ACKNOWLEDGEMENTMODE]
                                 [--offset-reset-strategy OFFSETRESETSTRATEGY]
                                 [--command-config CONFIG_FILE]
                                 --bootstrap-server HOST1:PORT1[,HOST2:PORT2[...]]

Optional arguments:

  -h, --help                          Shows this help message and exits.

  --topic TOPIC                       Consumes messages from this topic.

  --group-id GROUP_ID                 The group ID shared among members of
                                      the share group.

  --max-messages MAX-MESSAGES         Consumes this many messages. If set to -1, which is
                                      default, the share consumers consume
                                      until the process is killed externally.
                                      (Default: -1)

  --verbose                           Enables logging of individual consumed
                                      records. (Default: false)

  --acknowledgement-mode              Acknowledgement mode for the share
    ACKNOWLEDGEMENTMODE               consumers. The mode can be auto,
                                      sync, or async. (Default: auto)

  --offset-reset-strategy             Sets the share group reset strategy.
    OFFSETRESETSTRATEGY               Must be earliest or latest.
                                      (Default: latest)

  --command-config CONFIG_FILE        Specifies a configuration properties file.
                                      Configuration options shared with
                                      command line parameters are overridden by this file.

Connection Group:
  Group of arguments for connection to brokers

  --bootstrap-server                  The servers to connect to. A comma-
    HOST1:PORT1[,HOST2:PORT2[...]]    separated list of Kafka brokers in the
                                      form HOST1:PORT1,HOST2:PORT2,...
```

<a id="console-consumer-usage"></a>

### kafka-console-consumer.sh

Use the `kafka-console-consumer` tool to consume records from a topic.
Requires `bootstrap-server` parameter that contains a comma-separated list of `<hostname:port>` entries specifying the server/port to connect to.

<a id="confluenttip-0"></a>

Example:

```bash
bin/kafka-console-consumer.sh --bootstrap-server HOST1:PORT1,HOST2:PORT2 --consumer.config config.properties --topic testTopic --property "print.key=true"
```

### **Usage details**

```bash
This tool helps to read data from Kafka topics and outputs it to standard output.

Option                                   Description
------                                   -----------
--bootstrap-server <String: server to    REQUIRED: The servers to connect to.
  connect to>
--consumer-property <String:             A mechanism to pass user-defined
  consumer_prop>                           properties in the form key=value to
                                          the consumer.
--consumer.config <String: config file>  Consumer config properties file. Note
                                          that [consumer-property] takes
                                          precedence over this config.
--enable-systest-events                  Log lifecycle events of the consumer
                                          in addition to logging consumed
                                          messages. (This is specific for
                                          system tests.)
--formatter <String: class>              The name of a class to use for
                                          formatting kafka messages for
                                          display. (default: kafka.tools.
                                          DefaultMessageFormatter)
--formatter-config <String: config       Config properties file to initialize
file>                                    the message formatter. Note that
                                         [property] takes precedence over
                                         this config.
--from-beginning                         If the consumer does not already have
                                          an established offset to consume
                                          from, start with the earliest
                                          message present in the log rather
                                          than the latest message.
--group <String: consumer group id>      The consumer group id of the consumer.
--help                                   Print usage information.
--include <String: Java regex (String)>  Regular expression specifying list of
                                          topics to include for consumption.
--isolation-level <String>               Set to read_committed in order to
                                          filter out transactional messages
                                          which are not committed. Set to
                                          read_uncommitted to read all
                                          messages. (default: read_uncommitted)
--key-deserializer <String:
  deserializer for key>
--max-messages <Integer: num_messages>   The maximum number of messages to
                                          consume before exiting. If not set,
                                          consumption is continual.
--offset <String: consume offset>        The offset to consume from (a non-
                                          negative number), or 'earliest'
                                          which means from beginning, or
                                          'latest' which means from end
                                          (default: latest)
--partition <Integer: partition>         The partition to consume from.
                                          Consumption starts from the end of
                                          the partition unless '--offset' is
                                          specified.
--property <String: prop>                The properties to initialize the
                                          message formatter. Default
                                          properties include:
                                          print.timestamp=true|false
                                          print.key=true|false
                                          print.offset=true|false
                                          print.partition=true|false
                                          print.headers=true|false
                                          print.value=true|false
                                          key.separator=<key.separator>
                                          line.separator=<line.separator>
                                          headers.separator=<line.separator>
                                          null.literal=<null.literal>
                                          key.deserializer=<key.deserializer>
                                          value.deserializer=<value.
                                          deserializer>
                                          header.deserializer=<header.
                                          deserializer>
                                        Users can also pass in customized
                                          properties for their formatter; more
                                          specifically, users can pass in
                                          properties keyed with 'key.
                                          deserializer.', 'value.
                                          deserializer.' and 'headers.
                                          deserializer.' prefixes to configure
                                          their deserializers.
--skip-message-on-error                  If there is an error when processing a
                                          message, skip it instead of halt.
--timeout-ms <Integer: timeout_ms>       If specified, exit if no message is
                                          available for consumption for the
                                          specified interval.
--topic <String: topic>                  The topic to consume on.
--value-deserializer <String:
  deserializer for values>
--version                                Display Kafka version.
```

<a id="console-producer-usage"></a>

### kafka-console-producer.sh

Use the `kafka-console-producer` tool to produce records to a topic.
Requires a `bootstrap-server` parameter that contains a comma-separated list of <hostname:port> entries specifying the server/port to connect to.
Example:

```bash
kafka-console-producer.sh --bootstrap-server HOST1:PORT1,HOST2:PORT2 --producer.config config.properties --topic testTopic --property "parse.key=true" --property "key.separator=:"
```

<a id="confluenttip-1"></a>

### **Usage details**

```bash
This tool helps to read data from standard input and publish it to Kafka.
Option                                   Description
------                                   -----------
--batch-size <Integer: size>             Number of messages to send in a single
                                          batch if they are not being sent
                                          synchronously. please note that this
                                          option will be replaced if max-
                                          partition-memory-bytes is also set
                                          (default: 16384)
--bootstrap-server <String: server to    REQUIRED unless --broker-list
  connect to>                              (deprecated) is specified. The server
                                          (s) to connect to. The broker list
                                          string in the form HOST1:PORT1,HOST2:
                                          PORT2.
--broker-list <String: broker-list>      DEPRECATED, use --bootstrap-server
                                          instead; ignored if --bootstrap-
                                          server is specified.  The broker
                                          list string in the form HOST1:PORT1,
                                          HOST2:PORT2.
--compression-codec [String:             The compression codec: either 'none',
  compression-codec]                       'gzip', 'snappy', 'lz4', or 'zstd'.
                                          If specified without value, then it
                                          defaults to 'gzip'
--help                                   Print usage information.
--line-reader <String: reader_class>     The class name of the class to use for
                                          reading lines from standard in. By
                                          default each line is read as a
                                          separate message. (default: kafka.
                                          tools.
                                          ConsoleProducer$LineMessageReader)
--max-block-ms <Long: max block on       The max time that the producer will
  send>                                    block for during a send request.
                                          (default: 60000)
--max-memory-bytes <Long: total memory   The total memory used by the producer
  in bytes>                                to buffer records waiting to be sent
                                          to the server. This is the option to
                                          control `buffer.memory` in producer
                                          configs. (default: 33554432)
--max-partition-memory-bytes <Integer:   The buffer size allocated for a
  memory in bytes per partition>           partition. When records are received
                                          which are smaller than this size the
                                          producer will attempt to
                                          optimistically group them together
                                          until this size is reached. This is
                                          the option to control `batch.size`
                                          in producer configs. (default: 16384)
--message-send-max-retries <Integer>     Brokers can fail receiving the message
                                          for multiple reasons, and being
                                          unavailable transiently is just one
                                          of them. This property specifies the
                                          number of retries before the
                                          producer give up and drop this
                                          message. This is the option to
                                          control `retries` in producer
                                          configs. (default: 3)
--metadata-expiry-ms <Long: metadata     The period of time in milliseconds
  expiration interval>                     after which we force a refresh of
                                          metadata even if we haven't seen any
                                          leadership changes. This is the
                                          option to control `metadata.max.age.
                                          ms` in producer configs. (default:
                                          300000)
--producer-property <String:             A mechanism to pass user-defined
  producer_prop>                           properties in the form key=value to
                                          the producer.
--producer.config <String: config file>  Producer config properties file. Note
                                          that [producer-property] takes
                                          precedence over this config.
--property <String: prop>                A mechanism to pass user-defined
                                          properties in the form key=value to
                                          the message reader. This allows
                                          custom configuration for a user-
                                          defined message reader.
                                        Default properties include:
                                          parse.key=false
                                          parse.headers=false
                                          ignore.error=false
                                          key.separator=\t
                                          headers.delimiter=\t
                                          headers.separator=,
                                          headers.key.separator=:
                                          null.marker=   When set, any fields
                                          (key, value and headers) equal to
                                          this will be replaced by null
                                        Default parsing pattern when:
                                          parse.headers=true and parse.key=true:
                                          "h1:v1,h2:v2...\tkey\tvalue"
                                          parse.key=true:
                                          "key\tvalue"
                                          parse.headers=true:
                                          "h1:v1,h2:v2...\tvalue"
--reader-config <String: config file>     Config properties file for the message
                                          reader. Note that [property] takes
                                          precedence over this config.
--request-required-acks <String:         The required `acks` of the producer
  request required acks>                   requests (default: -1)
--request-timeout-ms <Integer: request   The ack timeout of the producer
  timeout ms>                              requests. Value must be non-negative
                                          and non-zero. (default: 1500)
--retry-backoff-ms <Long>                Before each retry, the producer
                                          refreshes the metadata of relevant
                                          topics. Since leader election takes
                                          a bit of time, this property
                                          specifies the amount of time that
                                          the producer waits before refreshing
                                          the metadata. This is the option to
                                          control `retry.backoff.ms` in
                                          producer configs. (default: 100)
--socket-buffer-size <Integer: size>     The size of the tcp RECV size. This is
                                          the option to control `send.buffer.
                                          bytes` in producer configs.
                                          (default: 102400)
--sync                                   If set message send requests to the
                                          brokers are synchronously, one at a
                                          time as they arrive.
--timeout <Long: timeout_ms>             If set and the producer is running in
                                          asynchronous mode, this gives the
                                          maximum amount of time a message
                                          will queue awaiting sufficient batch
                                          size. The value is given in ms. This
                                          is the option to control `linger.ms`
                                          in producer configs. (default: 1000)
--topic <String: topic>                  REQUIRED: The topic id to produce
                                          messages to.
--version                                Display Kafka version.
```

### kafka-console-share-consumer.sh

Use the `kafka-console-share-consumer` tool to consume messages from a Kafka topic using a share group. It allows multiple consumer
instances to jointly consume messages from a topic in a queue-like fashion, where each message is processed by only one consumer within the
share group. This differs from traditional Kafka consumer groups, which assign exclusive partitions to consumers.

Example:

```bash
kafka-console-share-consumer.sh --bootstrap-server localhost:9092 --topic my-share-topic --group my-shared-group
```

### **Usage details**

```bash
This tool helps to read data from Kafka topics using share groups and outputs it to standard output.

Option                                   Description
------                                   -----------
--bootstrap-server <String: server to    REQUIRED: The servers to connect to.
  connect to>
--consumer-config <String: config file>  Consumer config properties file. Note
                                          that [consumer-property] takes
                                          precedence over this config.
--consumer-property <String:             A mechanism to pass user-defined
  consumer_prop>                           properties in the form key=value to
                                          the consumer.
--enable-systest-events                  Log lifecycle events of the share
                                          consumer in addition to logging
                                          consumed messages. This is specific
                                          to system tests.
--formatter <String: class>              The name of a class to use for
                                          formatting Kafka messages for
                                          display. (default: org.apache.kafka.
                                          tools.consumer.
                                          DefaultMessageFormatter)
--formatter-config <String: config       Config properties file to initialize
  file>                                    the message formatter. Note that
                                          [property] takes precedence over
                                          this config.
--group <String: share group id>         The share group id of the consumer.
--help                                   Print usage information.
--key-deserializer <String:              The name of the class to use for
  deserializer for key>                    deserializing keys.
--max-messages <Integer: num_messages>   The maximum number of messages to
                                          consume before exiting. If not set,
                                          consumption is continual.
--property <String: prop>                The properties to initialize the
                                          message formatter. Default
                                          properties include:
                                          print.timestamp=true|false
                                          print.key=true|false
                                          print.offset=true|false
                                          print.delivery=true|false
                                          print.epoch=true|false
                                          print.partition=true|false
                                          print.headers=true|false
                                          print.value=true|false
                                          key.separator=<key.separator>
                                          line.separator=<line.separator>
                                          headers.separator=<line.separator>
                                          null.literal=<null.literal>
                                          key.deserializer=<key.deserializer>
                                          value.deserializer=<value.
                                          deserializer>
                                          header.deserializer=<header.
                                          deserializer>
                                         You can also pass in customized
                                          properties for their formatter; more
                                          specifically, you can pass in
                                          properties keyed with 'key.
                                          deserializer.', 'value.
                                          deserializer.' and 'headers.
                                          deserializer.' prefixes to configure
                                          their deserializers.
--reject                                 If specified, messages are rejected as
                                          they are consumed.
--reject-message-on-error                If there is an error when processing a
                                          message, reject it instead of
                                          halting.
--release                                If specified, messages are released as
                                          they are consumed.
--timeout-ms <Integer: timeout_ms>       If specified, exit if no message is
                                          available for consumption for the
                                          specified interval.
--topic <String: topic>                  The topic to consume from.
--value-deserializer <String:            The name of the class to use for
  deserializer for values>                 deserializing values.
--version                                Display Kafka version.
```

### kafka-producer-perf-test.sh

The `kafka-producer-perf-test` tool enables you to produce a large quantity of data to test producer performance for the Kafka cluster.

Example:

```bash
bin/kafka-producer-perf-test.sh --topic topic-a --num-records 200000 --record-size 1000 --throughput 10000000 --producer-props bootstrap.servers=host1:9092
```

### **Usage details**

```bash
usage: producer-perf-test [-h] --topic TOPIC --num-records NUM-RECORDS
                            [--payload-delimiter PAYLOAD-DELIMITER] --throughput THROUGHPUT
                            [--producer-props PROP-NAME=PROP-VALUE [PROP-NAME=PROP-VALUE ...]]
                            [--producer.config CONFIG-FILE] [--print-metrics]
                            [--transactional-id TRANSACTIONAL-ID]
                            [--transaction-duration-ms TRANSACTION-DURATION]
                            (--record-size RECORD-SIZE | --payload-file PAYLOAD-FILE) | --payload-monotonic)

This tool is used to verify the producer performance. To enable transactions, you can specify a transaction id or set a transaction
duration using --transaction-duration-ms. There are three ways to specify the transaction id:
set transaction.id=<id> via --producer-props, set transaction.id=<id> in the config file via --producer.config, or use --transaction-id <id>.

optional arguments:
  -h, --help             show this help message and exit
  --topic TOPIC          produce messages to this topic
  --num-records NUM-RECORDS
                        number of messages to produce
  --payload-delimiter PAYLOAD-DELIMITER
                        provides  delimiter  to  be  used  when  --payload-file  is  provided.
                        Defaults to new line. Note that  this  parameter will be ignored if --
                        payload-file is not provided. (default: \n)
  --throughput THROUGHPUT
                        throttle maximum  message  throughput  to  *approximately*  THROUGHPUT
                        messages/sec. Set this to -1 to disable throttling.
  --producer-props PROP-NAME=PROP-VALUE [PROP-NAME=PROP-VALUE ...]
                        kafka  producer  related  configuration   properties  like  bootstrap.
                        servers, client.id  etc.  These  configs  take  precedence  over  those
                        passed via --producer.config.
  --producer.config CONFIG-FILE
                        producer config properties file.
  --print-metrics        print out metrics at the end of the test. (default: false)
  --transactional-id TRANSACTIONAL-ID
                        The transactionalId to use if  transaction-duration-ms  is > 0. Useful
                        when testing the  performance  of  concurrent  transactions. (default:
                        performance-producer-default-transactional-id)
  --transaction-duration-ms TRANSACTION-DURATION
                        The max age of each transaction. The commitTransaction will be called
                        after this time has elapsed. The value should be greater than 0. If the
                        transactional id is specified via --producer-props, --producer.config,
                        or --transactional-id but --transaction-duration-ms is not specified,
                        the default value will be 3000.

  either --record-size or --payload-file must be specified but not both.

  --record-size RECORD-SIZE
                        message size in bytes. Note that  you  must  provide exactly one of --
                        record-size or --payload-file.
  --payload-file PAYLOAD-FILE
                        file to read the  message  payloads  from.  This  works only for UTF-8
                        encoded text files.  Payloads  will  be  read  from  this  file  and a
                        payload will be randomly  selected  when  sending  messages. Note that
                        you must provide exactly one of --record-size or --payload-file.
    --payload-monotonic
                        payload is monotonically increasing integer. Note that you must provide exactly one
                        of --record-size or --payload-file or --payload-monotonic. (default: false)
```

<a id="kafka-consumer-group-usage"></a>

### kafka-groups.sh

This tool helps to list groups of all types.

### **Usage details**

```bash
Option                                   Description
------                                   -----------
--bootstrap-server <String:            The Kafka server to connect
  server to REQUIRED:
  connect to>
--command-config <String: command      Property file containing configs to be
  config property file>                passed to the admin client.
--consumer                             Filter the groups to show all kinds of
                                       consumer groups, including classic
                                       and simple consumer groups. This
                                       matches group type 'consumer', and
                                       group type 'classic' where the
                                       protocol type is 'consumer' or empty.
--group-type <String: type>            Filter the groups based on group type.
                                       Valid types are: 'classic',
                                       'consumer' and 'share'.
--help                                 Print usage information.
--list                                 List the groups.
--protocol <String: protocol>          Filter the groups based on protocol
                                       type.
--share                                Filter the groups to show share groups.
--version                              Display Kafka version.
```

### kafka-consumer-groups.sh

Use the `kafka-consumer-groups` tool to get a list of the active groups in the cluster.

For example, to show the position of all consumers in a group named `user-group`, you might use the following command.

```none
bin/kafka-consumer-groups.sh \
         --bootstrap-server localhost:9092 \
         --describe --group user-group
```

This would result in output like the following (`CONSUMER-ID` entries truncated for readability).

```none
TOPIC          PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG CONSUMER-ID       HOST         CLIENT-ID
user           0          2               4               2   consumer-1-...    /127.0.0.1   consumer-1
user           1          2               3               1   consumer-1-...    /127.0.0.1   consumer-1
user           2          2               3               1   consumer-2-...    /127.0.0.1   consumer-2
```

For more examples, see [View Consumer Group Info in Kafka](manage-consumer-groups.md#manage-consumer-groups).

### **Usage details**

```bash
Option                                  Description
------                                  -----------
--all-groups                            Apply to all consumer groups.
--all-topics                            Consider all topics assigned to a
                                          group in the `reset-offsets` process.
--bootstrap-server
<String: server to   REQUIRED:          The servers to connect to. Required for all options except for --validate-regex.
  connect to>
--by-duration <String: duration>        Reset offsets to offset by duration
                                          from current timestamp. Format:
                                          'PnDTnHnMnS'
--command-config <String: command       Property file containing configs to be
  config property file>                   passed to Admin Client and Consumer.
--delete                                Pass in groups to delete topic
                                          partition offsets and ownership
                                          information over the entire consumer
                                          group. For instance --group g1 --
                                          group g2
--delete-offsets                        Delete offsets of consumer group.
                                          Supports one consumer group at the
                                          time, and multiple topics.
--describe                              Describe consumer group and list
                                          offset lag (number of messages not
                                          yet processed) related to given
                                          group.
--dry-run                               Only show results without executing
                                          changes on Consumer Groups.
                                          Supported operations: reset-offsets.
--execute                               Execute operation. Supported
                                          operations: reset-offsets.
--export                                Export operation execution to a CSV
                                          file. Supported operations: reset-
                                          offsets.
--from-file <String: path to CSV file>  Reset offsets to values defined in CSV
                                          file.
--group <String: consumer group>        The consumer group we wish to act on.
--help                                  Print usage information.
--list                                  List all consumer groups.
--members                               Describe members of the group. This
                                          option may be used with '--describe'
                                          and '--bootstrap-server' options
                                          only.
                                        Example: --bootstrap-server localhost:
                                          9092 --describe --group group1 --
                                          members
--offsets                               Describe the group and list all topic
                                          partitions in the group along with
                                          their offset lag. This is the
                                          default sub-action of and may be
                                          used with '--describe' and '--
                                          bootstrap-server' options only.
                                        Example: --bootstrap-server localhost:
                                          9092 --describe --group group1 --
                                          offsets
--reset-offsets                         Reset offsets of consumer group.
                                          Supports one consumer group at the
                                          time, and instances should be
                                          inactive
                                        Has 2 execution options: --dry-run
                                          (the default) to plan which offsets
                                          to reset, and --execute to update
                                          the offsets. Additionally, the --
                                          export option is used to export the
                                          results to a CSV format.
                                        You must choose one of the following
                                          reset specifications: --to-datetime,
                                          --by-period, --to-earliest, --to-
                                          latest, --shift-by, --from-file, --
                                          to-current.
                                        To define the scope use --all-topics
                                          or --topic. One scope must be
                                          specified unless you use '--from-
                                          file'.
--shift-by <Long: number-of-offsets>    Reset offsets shifting current offset
                                          by 'n', where 'n' can be positive or
                                          negative.
--state [String]                        When specified with '--describe',
                                          includes the state of the group.
                                        Example: --bootstrap-server localhost:
                                          9092 --describe --group group1 --
                                          state
                                        When specified with '--list', it
                                          displays the state of all groups. It
                                          can also be used to list groups with
                                          specific states.
                                        Example: --bootstrap-server localhost:
                                          9092 --list --state stable,empty
                                        This option may be used with '--
                                          describe', '--list' and '--bootstrap-
                                          server' options only.
--timeout <Long: timeout (ms)>          The timeout that can be set for some
                                          use cases. For example, it can be
                                          used when describing the group to
                                          specify the maximum amount of time
                                          in milliseconds to wait before the
                                          group stabilizes (when the group is
                                          just created, or is going through
                                          some changes). (default: 5000)
--to-current                            Reset offsets to current offset.
--to-datetime <String: datetime>        Reset offsets to offset from datetime.
                                          Format: 'YYYY-MM-DDTHH:mm:SS.sss'
--to-earliest                           Reset offsets to earliest offset.
--to-latest                             Reset offsets to latest offset.
--to-offset <Long: offset>              Reset offsets to a specific offset.
--topic <String: topic>                 The topic whose consumer group
                                          information should be deleted or
                                          topic whose should be included in
                                          the reset offset process. In `reset-
                                          offsets` case, partitions can be
                                          specified using this format: `topic1:
                                          0,1,2`, where 0,1,2 are the
                                          partition to be included in the
                                          process. Reset-offsets also supports
                                          multiple topic inputs.
--type [String]                         When specified with '--list', it
                                          displays the types of all the
                                          groups. It can also be used to list
                                          groups with specific types.
                                        Example: --bootstrap-server localhost:
                                          9092 --list --type classic, consumer
                                        This option may be used with the '--list'
                                        option only.
--validate-regex <String: regex>        Validate that the syntax of the
                                          provided regular expression is valid
                                          according to the RE2 format.
--verbose                               Provide additional information, if
                                          any, when describing the group. This
                                          option may be used with '--
                                          offsets'/'--members'/'--state' and
                                          '--bootstrap-server' options only.
                                        Example: --bootstrap-server localhost:
                                          9092 --describe --group group1 --
                                          members --verbose
--version                               Display Kafka version.
```

### kafka-consumer-perf-test.sh

This tool tests the consumer performance for the Kafka cluster.

### **Usage details**

```bash
Option                                   Description
------                                   -----------
--bootstrap-server <String: server to    REQUIRED unless --broker-list
  connect to>                              (deprecated) is specified. The server
                                          (s) to connect to.
--broker-list <String: broker-list>      DEPRECATED, use --bootstrap-server
                                          instead; ignored if --bootstrap-
                                          server is specified.  The broker
                                          list string in the form HOST1:PORT1,
                                          HOST2:PORT2.
--consumer.config <String: config file>  Consumer config properties file.
--date-format <String: date format>      The date format to use for formatting
                                          the time field. See java.text.
                                          SimpleDateFormat for options.
                                          (default: yyyy-MM-dd HH:mm:ss:SSS)
--fetch-size <Integer: size>             The amount of data to fetch in a
                                          single request. (default: 1048576)
--from-latest                            If the consumer does not already have
                                          an established offset to consume
                                          from, start with the latest message
                                          present in the log rather than the
                                          earliest message.
--group <String: gid>                    The group id to consume on. (default:
                                          perf-consumer-50334)
--help                                   Print usage information.
--hide-header                            If set, skips printing the header for
                                          the stats
--messages <Long: count>                 REQUIRED: The number of messages to
                                          send or consume
--num-fetch-threads <Integer: count>     DEPRECATED AND IGNORED: Number of
                                          fetcher threads. (default: 1)
--print-metrics                          Print out the metrics.
--reporting-interval <Integer:           Interval in milliseconds at which to
  interval_ms>                             print progress info. (default: 5000)
--show-detailed-stats                    If set, stats are reported for each
                                          reporting interval as configured by
                                          reporting-interval
--socket-buffer-size <Integer: size>     The size of the tcp RECV size.
                                          (default: 2097152)
--threads <Integer: count>               DEPRECATED AND IGNORED: Number of
                                          processing threads. (default: 10)
--timeout [Long: milliseconds]           The maximum allowed time in
                                          milliseconds between returned
                                          records. (default: 10000)
--topic <String: topic>                  REQUIRED: The topic to consume from.
--version                                Display Kafka version.
```

### kafka-share-consumer-perf-test.sh

Use this tool to verify share consumer performance.

### **Usage details**

```bash
Option                                   Description
------                                   -----------

--bootstrap-server                       (REQUIRED) The servers to connect to.
 <String: server to connect to>

--consumer.config <String: config file>  Share consumer configuration properties file.

--date-format <String: date format>      The date format to use for formatting
                                         the time field. See :java:`java.text.
                                         SimpleDateFormat` for options.
                                         (Default: yyyy-MM-dd HH:mm:ss:SSS)

--fetch-size <Integer: size>             The amount of data to fetch in a
                                         single request. (Default: 1048576)

--group <String: gid>                    The group ID to consume on. (Default:
                                         perf-share-consumer)

--help                                   Prints usage information.

--hide-header                            If set, skips printing the header for
                                         the stats.

--messages <Long: count>                 (REQUIRED) The number of messages to
                                         send or consume.

--print-metrics                          Prints the metrics.

--reporting-interval <Long:              Interval in milliseconds at which to
  interval_ms>                           print progress information. (Default: 5000)

--show-consumer-stats                    If set, reports stats for each share
                                         consumer depending on the number of
                                         threads.

--show-detailed-stats                    If set, reports stats for each
                                         reporting interval as configured by
                                         reporting-interval.

--socket-buffer-size <Integer: size>     The size of the TCP RECV size.
                                         (Default: 2097152)

--threads <Integer: count>               The number of share consumers to use
                                         for sharing the load. (Default: 1)

--timeout [Long: milliseconds]           The maximum allowed time in
                                         milliseconds between returned records.
                                         (Default: 10000)

--topic <String: topic>                  (REQUIRED) The topic to consume from.

--version                                Displays Kafka version.
```

### kafka-share-groups.sh

This tool helps to list, describe, reset and delete share groups.

### **Usage details**

```bash
Option                                   Description
------                                   -----------
--all-topics                           Consider all topics assigned to a
                                       share group in the 'reset-offsets'
                                       process.
--bootstrap-server <String:            The servers to connect to.
  server to REQUIRED:
  connect to>
--command-config <String: command      Property file containing configs to be
  config property file>                passed to the admin client.
--delete                               Delete share group.
--delete-offsets                       Delete offsets of share group.
                                       Supports one share group at the
                                       time, and multiple topics.
--describe                             Describe share group, members and
                                       offset information.
--dry-run                              Only show results without executing
                                       changes on share groups. Supported
                                       operations: reset-offsets.
--execute                              Execute operation. Supported
                                       operations: reset-offsets.
--group <String: share group>          The share group we wish to act on.
--help                                 Print usage information.
--list                                 List all share groups.
--members                              Describe members of the group. This
                                       option may be used with the '--
                                       describe' option only.
--offsets                              Describe the group and list all topic
                                       partitions in the group along with
                                       their offset information. This is
                                       the default sub-action and may be
                                       used with the '--describe' option
                                       only.
--reset-offsets                        Reset offsets of share group. Supports
                                       one share group at the time, and
                                       instances must be inactive.
                                       Has 2 execution options: --dry-run
                                       (the default) to plan which offsets
                                       to reset, and --execute to reset the
                                       offsets.
                                       You must choose one of the following
                                       reset specifications: --to-datetime,
                                       --to-earliest, --to-latest.
                                       To define the scope use --all-topics
                                       or --topic.
--state [String]                       When specified with '--describe',
                                       includes the state of the group.
                                       When specified with '--list', it
                                       displays the state of all groups. It
                                       can also be used to list groups with
                                       specific states. Valid values are
                                       Empty, Stable and Dead.
--timeout <Long: timeout (ms)>         The timeout that can be set for some
                                       use cases. For example, it can be
                                       used when describing the group to
                                       specify the maximum amount of time
                                       in milliseconds to wait before the
                                       group stabilizes. (default: 5000)
--to-datetime <String: datetime>       Reset offsets to offset from datetime.
                                       Format: 'YYYY-MM-DDTHH:mm:SS.sss'
--to-earliest                          Reset offsets to earliest offset.
--to-latest                            Reset offsets to latest offset.
--topic <String: topic>                The topic whose share group
                                       information should be deleted or
                                       topic whose should be included in
                                       the reset offset process. When
                                       resetting offsets, partitions can be
                                       specified using this format: 'topic1:
                                       0,1,2', where 0,1,2 are the
                                       partitions to be included.
--version                              Display Kafka version.
```

## Manage Kafka Connect

### connect-distributed.sh

Use the `connect-distributed` tool to run Connect workers in Distributed mode, meaning on multiple, distributed, machines.
Distributed mode handles automatic balancing of work, allows you to scale up
(or down) dynamically, and offers fault tolerance both in the active tasks and for configuration and offset commit data.

### **Usage details**

```bash
USAGE: ./connect-distributed.sh [-daemon] connect-distributed.properties
```

### connect-standalone.sh

Use the `connect-standalone` tool to run Kafka Connect in standalone mode meaning all work is performed in a single process. This is good for
getting started but lacks fault tolerance.
For more information, see [Kafka Connect](/platform/current/current/connect/index.html).

### **Usage details**

```bash
USAGE: ./connect-standalone.sh [-daemon] connect-standalone.properties
```

### connect-mirror-maker.sh

Use the `connect-mirror-maker` tool to replicate topics from one cluster to another using the Connect framework.
You must pass an an `mm2.properties` MM2 configuration file. For more information, see
[KIP-382: MirrorMaker 2.0](https://cwiki.apache.org/confluence/display/KAFKA/KIP-382%3A+MirrorMaker+2.0)
or [Getting up to speed with MirrorMaker 2](https://www.confluent.io/resources/kafka-summit-2020/getting-up-to-speed-with-mirrormaker-2/).

### **Usage details**

```bash
usage: connect-mirror-maker [-h] [--clusters CLUSTER [CLUSTER ...]] mm2.properties

MirrorMaker 2.0 driver

positional arguments:
  mm2.properties         MM2 configuration file.

optional arguments:
  -h, --help             show this help message and exit
  --clusters CLUSTER [CLUSTER ...]
                        Target cluster to use for this node.
```

## Manage Kafka Streams

### kafka-streams-application-reset.sh

For Kafka Streams applications, the `kafka-streams-application-reset` tool resets the application and forces it to reprocess its data from the beginning. Useful for debugging and testing.

For example, the following command would reset the `my-streams-app` application:

```none
kafka-streams-application-reset.sh --application-id my-streams-app \
                                   --input-topics my-input-topic \
                                   --intermediate-topics rekeyed-topic
```

For more information, see [Kafka Streams Application Reset Tool](/platform/current/streams/developer-guide/app-reset-tool.html#step-2-reset-the-local-environments-of-your-application-instances) 
in the Confluent documentation.

### **Usage details**

```bash
This tool helps to quickly reset an application in order to reprocess its data from scratch.

* This tool resets offsets of input topics to the earliest available offset (by default), or to a specific
  defined position.
* This tool deletes the internal topics that were created by Kafka Streams (topics starting with "<application.id>-").
  The tool finds these internal topics automatically. If the topics flagged automatically for deletion by
  the dry-run are unsuitable, you can specify a subset with the "--internal-topics" option.
* This tool will not delete output topics (if you want to delete them, you need to do it yourself with the bin/kafka-topics.sh command).
* This tool will not clean up the local state on the stream application instances (the persisted stores
  used to cache aggregation results). You need to call KafkaStreams#cleanUp() in your application
  or manually delete them from the directory specified by "state.dir"
  configuration (${java.io.tmpdir}/kafka-streams/<application.id> by default).
* When long session timeout has been configured, active members could take longer to get expired on the
  broker thus blocking the reset job to complete. Use the "--force" option could remove those
  left-over members immediately. Make sure to stop all stream applications when this option
  is specified to avoid unexpected disruptions.

*** Important! You will get wrong output if you don't clean up the local stores after running the reset tool!

*** Warning! This tool makes irreversible changes to your application. It is strongly recommended that you run this first with "--dry-run" to preview your changes before making them.


Option (* = required)                 Description
---------------------                 -----------
* --application-id <String: id>       The Kafka Streams application ID
                                        (application.id).
--bootstrap-servers <String: urls>    Comma-separated list of broker urls with
                                        format: HOST1:PORT1,HOST2:PORT2
                                        (default: localhost:9092)
--by-duration <String>                Reset offsets to offset by duration from
                                        current timestamp. Format: 'PnDTnHnMnS'
--config-file <String: file name>     Property file containing configs to be
                                        passed to admin clients and embedded
                                        consumer.
--dry-run                             Display the actions that would be
                                        performed without executing the reset
                                        commands.
--force                               Force the removal of members of the
                                        consumer group (intended to remove
                                        stopped members if a long session
                                        timeout was used). Make sure to shut
                                        down all stream applications when this
                                        option is specified to avoid unexpected
                                        rebalances.
--from-file <String>                  Reset offsets to values defined in CSV
                                        file.
--help                                Print usage information.
--input-topics <String: list>         Comma-separated list of user input
                                        topics. For these topics, the tool by
                                        default will reset the offset to the
                                        earliest available offset. Reset to
                                        other offset position by appending
                                        other reset offset option, ex: --input-
                                        topics foo --shift-by 5
--intermediate-topics <String: list>  Comma-separated list of intermediate user
                                        topics (topics that are input and
                                        output topics, e.g., used in the
                                        deprecated through() method). For these
                                        topics, the tool will skip to the end.
--internal-topics <String: list>      Comma-separated list of internal topics
                                        to delete. Must be a subset of the
                                        internal topics marked for deletion by
                                        the default behaviour (do a dry-run
                                        without this option to view these
                                        topics).
--shift-by <Long: number-of-offsets>  Reset offsets shifting current offset by
                                        'n', where 'n' can be positive or
                                        negative
--to-datetime <String>                Reset offsets to offset from datetime.
                                        Format: 'YYYY-MM-DDTHH:mm:SS.sss'
--to-earliest                         Reset offsets to earliest offset.
--to-latest                           Reset offsets to latest offset.
--to-offset <Long>                    Reset offsets to a specific offset.
--version                             Print version information and exit.
```

### kafka-streams-groups.sh

Use this tool to list or describe streams groups.

### **Usage details**

```bash
Option                                 Description
------                                 -----------

--all-groups                           Applies to all streams groups.

--all-input-topics                     Considers all input topics assigned to
                                       a group in the reset-offsets and
                                       delete-offsets process. Only input
                                       topics are supported.

--bootstrap-server                     (REQUIRED) The servers to connect to.
 <String: server to connect to>

--command-config <String: command      Property file that contains
  config property file>                configurations to pass to the admin
                                       client.

--delete                               Deletes topic partition offsets and
                                       ownership information for the entire
                                       streams group. For example, --group
                                       g1 --group g2.

--delete-offsets                       Deletes offsets of a streams group.
                                       Supports one streams group at a time
                                       and multiple topics.

--describe                             Describes the streams group and lists
                                       offset lag related to the specified
                                       group.

--group <String: streams group>        The streams group to act on.

--help                                 Prints usage information.

--input-topic <String: topic>          The topic whose streams group
                                       information to delete, or the topic to
                                       include in the reset offset process.

                                       For reset-offsets, you can specify
                                       partitions using this format: topic1:
                                       0,1,2, where 0,1,2 are the partitions
                                       to include in the process.

                                       Reset-offsets also supports multiple topic
                                       inputs. All types of topics are
                                       supported.

--list                                 Lists all streams groups.

--members                              Describes members of the group. Use
                                       this option with the --describe
                                       option only.

--offsets                              Describes the group and lists all
                                       topic partitions in the group along
                                       with their offset information. This is
                                       the default sub-action. Use with the
                                       --describe option only.

--state [String]                       When specified with --list, displays
                                       the state of all groups. Can also be
                                       used to list groups with specific
                                       states. The valid values are Empty, NotReady,
                                       Stable, Assigning, Reconciling, and
                                       Dead.

--timeout <Long: timeout (ms)>         The timeout for some use cases. For
                                       example, when describing the group,
                                       specifies the maximum amount of time
                                       in milliseconds to wait before the
                                       group stabilizes. (Default: 5000)

--verbose                              Use with --describe --state to show
                                       group epoch and target assignment
                                       epoch.

                                       Use with --describe --members to
                                       show each member the member's epoch,
                                       target assignment epoch, current
                                       assignment, target assignment, and
                                       whether the member is still using the
                                       classic rebalance protocol.

                                       Use with --describe --offsets and
                                       --describe to show leader epochs for
                                       each partition.

--version                              Displays Kafka version.
```

## Manage security

### kafka-acls

Use the `kafka-acls` tool to add, remove and list ACLs. For example, if you wanted to
add two principal users, Jose and Jane to have read and write permissions on
the `user` topic from specific IP addresses, you could use a command like the following:

```none
bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:Jose --allow-principal User:Jane --allow-host 198.51.100.0 --allow-host 198.51.100.1 --operation Read --operation Write --topic user
```

### **Usage details**

```bash
This tool helps to manage acls on kafka.
Option                                   Description
------                                   -----------
--add                                    Indicates you are trying to add ACLs.
--allow-host <String: allow-host>        Host from which principals listed in --
                                          allow-principal will have access. If
                                          you have specified --allow-principal
                                          then the default for this option
                                          will be set to '*' which allows
                                          access from all hosts.
--allow-principal <String: allow-        principal is in principalType:name
  principal>                               format. Note that principalType must
                                          be supported by the Authorizer being
                                          used. For example, User:'*' is the
                                          wild card indicating all users.
--bootstrap-controller <String:          A list of host/port pairs to use for
  controller to connect to>              establishing the connection to the
                                         Kafka  cluster. This list should be
                                         in the form host1:port1,host2:
                                         port2,... This config is required
                                         for acl management using admin
                                         client API.
--bootstrap-server <String: server to    A list of host/port pairs to use for
  connect to>                              establishing the connection to the
                                          Kafka cluster. This list should be
                                          in the form host1:port1,host2:
                                          port2,... This config is required
                                          for acl management using admin
                                          client API.
--cluster                                Add/Remove cluster ACLs.
--command-config [String: command-       A property file containing configs to
  config]                                  be passed to Admin Client.
--consumer                               Convenience option to add/remove ACLs
                                          for consumer role. This will
                                          generate ACLs that allows READ,
                                          DESCRIBE on topic and READ on group.
--delegation-token <String: delegation-  Delegation token to which ACLs should
  token>                                   be added or removed. A value of '*'
                                          indicates ACL should apply to all
                                          tokens.
--deny-host <String: deny-host>          Host from which principals listed in --
                                          deny-principal will be denied
                                          access. If you have specified --deny-
                                          principal then the default for this
                                          option will be set to '*' which
                                          denies access from all hosts.
--deny-principal <String: deny-          principal is in principalType:name
  principal>                               format. By default anyone not added
                                          through --allow-principal is denied
                                          access. You only need to use this
                                          option as negation to already
                                          allowed set. Note that principalType
                                          must be supported by the Authorizer
                                          being used. For example if you
                                          wanted to allow access to all users
                                          in the system but not test-user you
                                          can define an ACL that allows access
                                          to User:'*' and specify --deny-
                                          principal=User:test@EXAMPLE.COM. AND
                                          PLEASE REMEMBER DENY RULES TAKES
                                          PRECEDENCE OVER ALLOW RULES.
--force                                  Assume Yes to all queries and do not
                                          prompt.
--group <String: group>                  Consumer Group to which the ACLs
                                          should be added or removed. A value
                                          of '*' indicates the ACLs should
                                          apply to all groups.
--help                                   Print usage information.
--idempotent                             Enable idempotence for the producer.
                                          This should be used in combination
                                          with the --producer option. Note
                                          that idempotence is enabled
                                          automatically if the producer is
                                          authorized to a particular
                                          transactional-id.
--list                                   List ACLs for the specified resource,
                                          use --topic <topic> or --group
                                          <group> or --cluster to specify a
                                          resource.
--operation <String>                     Operation that is being allowed or
                                          denied. Valid operation names are:
                                                Describe
                                                DescribeConfigs
                                                Alter
                                                IdempotentWrite
                                                Read
                                                Delete
                                                Create
                                                ClusterAction
                                                All
                                                CreateTokens
                                                DescribeTokens
                                                Write
                                                AlterConfigs
                                          (default: All)
--principal [String: principal]          List ACLs for the specified principal.
                                          principal is in principalType:name
                                          format. Note that principalType must
                                          be supported by the Authorizer being
                                          used. Multiple --principal option
                                          can be passed.
--producer                               Convenience option to add/remove ACLs
                                          for producer role. This will
                                          generate ACLs that allows WRITE,
                                          DESCRIBE and CREATE on topic.
--remove                                 Indicates you are trying to remove
                                          ACLs.
--resource-pattern-type                  The type of the resource pattern or
  <ANY|MATCH|LITERAL|PREFIXED>             pattern filter. When adding acls,
                                          this should be a specific pattern
                                          type, e.g. 'literal' or 'prefixed'.
                                          When listing or removing acls, a
                                          specific pattern type can be used to
                                          list or remove acls from specific
                                          resource patterns, or use the filter
                                          values of 'any' or 'match', where
                                          'any' will match any pattern type,
                                          but will match the resource name
                                          exactly, where as 'match' will
                                          perform pattern matching to list or
                                          remove all acls that affect the
                                          supplied resource(s). WARNING:
                                          'match', when used in combination
                                          with the '--remove' switch, should
                                          be used with care. (default: LITERAL)
--topic <String: topic>                  topic to which ACLs should be added or
                                          removed. A value of '*' indicates
                                          ACL should apply to all topics.
--transactional-id <String:              The transactionalId to which ACLs
  transactional-id>                        should be added or removed. A value
                                          of '*' indicates the ACLs should
                                          apply to all transactionalIds.
--user-principal <String: user-          Specifies a user principal as a
  principal>                               resource in relation with the
                                          operation. For instance one could
                                          grant CreateTokens or DescribeTokens
                                          permission on a given user principal.
--version                                Display Kafka version.
```

### kafka-delegation-tokens.sh

Use the `kafka-delegation-tokens` tool to create, renew, expire and describe delegation tokens. Delegation tokens
are shared secrets between Kafka brokers and clients, and are a lightweight authentication mechanism meant to complement
existing SASL/SSL methods.
For more information, see [Authentication using Delegation Tokens](/platform/current/kafka/authentication_sasl/authentication_sasl_delegation.html#token-authentication) in the
Confluent Documentation.

### **Usage details**

```bash
This tool helps to create, renew, expire, or describe delegation tokens.
Option                         Description
------                         -----------
--bootstrap-server <String>    REQUIRED: server(s) to use for bootstrapping.
--command-config <String>      REQUIRED: A property file containing configs to
                                be passed to Admin Client. Token management
                                operations are allowed in secure mode only.
                                This config file is used to pass security
                                related configs.
--create                       Create a new delegation token. Use --renewer-
                                principal option to pass renewers principals.
--describe                     Describe delegation tokens for the given
                                principals. Use --owner-principal to pass
                                owner/renewer principals. If --owner-principal
                                option is not supplied, all the user owned
                                tokens and tokens where user have Describe
                                permission will be returned.
--expire                       Expire delegation token. Use --expiry-time-
                                period option to expire the token.
--expiry-time-period [Long]    Expiry time period in milliseconds. If the value
                                is -1, then the token will get invalidated
                                immediately.
--help                         Print usage information.
--hmac [String]                HMAC of the delegation token
--max-life-time-period [Long]  Max life period for the token in milliseconds.
                                If the value is -1, then token max life time
                                will default to a server side config value
                                (delegation.token.max.lifetime.ms).
--owner-principal [String]     owner is a kafka principal. It is should be in
                                principalType:name format.
--renew                        Renew delegation token. Use --renew-time-period
                                option to set renew time period.
--renew-time-period [Long]     Renew time period in milliseconds. If the value
                                is -1, then the renew time period will default
                                to a server side config value (delegation.
                                token.expiry.time.ms).
--renewer-principal [String]   renewer is a kafka principal. It is should be in
                                principalType:name format.
--version                      Display Kafka version.
```

## Test and troubleshoot

This section contains tools you can use for testing and troubleshooting your applications.

### kafka-e2e-latency.sh

The `kafka-e2e-latency` tool is a performance testing tool used to measure end-to-end latency in Kafka.
It works by sending messages to a Kafka topic and then consuming those messages from a Kafka consumer.
The tool calculates the time difference between when a message was produced and when it was consumed,
giving you an idea of the end-to-end latency for your Kafka cluster. This tool is useful for testing the
performance of your Kafka cluster and identifying any bottlenecks or issues that may be affecting latency.

To run the tool, you provide details such as the message size, number of messages and `acks` setting for the producer.
For more about end-to-end latency, see [Configure Kafka to Minimize Latency](https://www.confluent.io/blog/configure-kafka-to-minimize-latency/).

Following are the required arguments
: * `broker_list`: The location of the bootstrap broker for both the producer and the consumer
  * `topic`: The topic name used by both the producer and the consumer to send/receive messages
  * `num_messages`: The number of messages to send
  * `producer_acks`: The producer setting for [acks](/platform/current/installation/configuration/producer-configs.html#acks).
  * `message_size_bytes`: size of each message in bytes

For example:

```bash
kafka-e2e-latency.sh localhost:9092 test 10000 1 20
```

### **Usage details**

```bash
USAGE: java org.apache.kafka.tools.EndToEndLatency broker_list topic num_messages producer_acks message_size_bytes [optional] properties_file
```

### kafka-dump-log.sh

The `kafka-dump-log` tool can be used in KRaft mode to parse a metadata log file and output its contents to the console.
Requires a comma-separated list of log files. The tool will scan the provided files and decode the metadata records.

The following example shows using the `cluster-metadata-decoder` argument to decode
the metadata records in a log segment.

```none
bin/kafka-dump-log.sh --cluster-metadata-decoder --files tmp/kraft-combined-logs/_cluster_metadata-0/00000000000000023946.log
```

### **Usage details**

```none
This tool helps to parse a log file and dump its contents to the console, useful for debugging a seemingly corrupt log segment.

Option                               Description
------                               -----------
--cluster-metadata-decoder           if set, log data will be parsed as cluster
                                      metadata records.
--deep-iteration                     if set, uses deep instead of shallow
                                      iteration. Automatically set if print-
                                      data-log is enabled.
--files <String: file1, file2, ...>  REQUIRED: The comma separated list of data
                                      and index log files to be dumped.
--help                               Print usage information.
--index-sanity-check                 if set, just checks the index sanity
                                      without printing its content. This is
                                      the same check that is executed on
                                      broker startup to determine if an index
                                      needs rebuilding or not.
--key-decoder-class [String]         if set, used to deserialize the keys. This
                                      class should implement kafka.serializer.
                                      Decoder trait. Custom jar should be
                                      available in kafka/libs directory.
                                      (default: kafka.serializer.StringDecoder)
--max-bytes <Integer: size>          Limit the amount of total batches read in
                                      bytes avoiding reading the whole .log
                                      file(s). (default: 2147483647)
--max-message-size <Integer: size>   Size of largest message. (default: 5242880)
--offsets-decoder                    if set, log data will be parsed as offset
                                      data from the __consumer_offsets topic.
--print-data-log                     if set, printing the messages content when
                                      dumping data logs. Automatically set if
                                      any decoder option is specified.
--remote-log-metadata-decoder        If set, log data will be parsed as
                                     TopicBasedRemoteLogMetadataManager
                                     (RLMM) metadata records. Instead, the
                                     value-decoder-class option can be used
                                     if a custom RLMM implementation is
                                     configured.
--share-group-state-decoder          If set, log data will be parsed as share
                                     group state data from the
                                     __share_group_state topic.
--skip-record-metadata               whether to skip printing metadata for each
                                      record.
--transaction-log-decoder            if set, log data will be parsed as
                                      transaction metadata from the
                                      __transaction_state topic.
--value-decoder-class [String]       if set, used to deserialize the messages.
                                      This class should implement kafka.
                                      serializer.Decoder trait. Custom jar
                                      should be available in kafka/libs
                                      directory. (default: kafka.serializer.
                                      StringDecoder)
--verify-index-only                  if set, just verify the index log without
                                      printing its content.
--version                            Display Kafka version.
```

### kafka-jmx.sh

The `kafka-jmx` tool enables you to read JMX metrics from a given endpoint.
This tool only works reliably if the JmxServer is fully initialized prior to invoking the tool.

### **Usage details**

```none
      Dump JMX values to standard output.
Option                                   Description
------                                   -----------
--attributes <String: name>              The list of attributes to include in
                                          the query. This is a comma-separated
                                          list. If no attributes are specified
                                          all objects will be queried.
--date-format <String: format>           The date format to use for formatting
                                          the time field. See java.text.
                                          SimpleDateFormat for options.
--help                                   Print usage information.
--jmx-auth-prop <String: jmx-auth-prop>  A mechanism to pass property in the
                                          form 'username=password' when
                                          enabling remote JMX with password
                                          authentication.
--jmx-ssl-enable <Boolean: ssl-enable>   Flag to enable remote JMX with SSL.
                                          (default: false)
--jmx-url <String: service-url>          The url to connect to poll JMX data.
                                          See Oracle javadoc for JMXServiceURL
                                          for details. (default: service:jmx:
                                          rmi:///jndi/rmi://:9999/jmxrmi)
--object-name <String: name>             A JMX object name to use as a query.
                                          This can contain wild cards, and
                                          this option can be given multiple
                                          times to specify more than one
                                          query. If no objects are specified
                                          all objects will be queried.
--one-time [Boolean: one-time]           Flag to indicate run once only.
                                          (default: false)
--report-format <String: report-format>  output format name: either 'original',
                                          'properties', 'csv', 'tsv'
                                          (default: original)
--reporting-interval <Integer: ms>       Interval in MS with which to poll jmx
                                          stats; default value is 2 seconds.
                                          Value of -1 equivalent to setting
                                          one-time to true (default: 2000)
--version                                Display Kafka version.
--wait                                   Wait for requested JMX objects to
                                          become available before starting
                                          output. Only supported when the list
                                          of objects is non-empty and contains
                                          no object name patterns.
```

### trogdor.sh

Trogdor is a test framework for Kafka. Trogdor can run benchmarks and other workloads. Trogdor can also inject faults in order to stress test the system.
For more information, see [Trogdor](https://cwiki.apache.org/confluence/display/KAFKA/Fault+Injection#FaultInjection-Trogdor) and [TROGDOR](https://github.com/apache/kafka/blob/trunk/TROGDOR.md).

### **Usage details**

```none
The Trogdor fault injector.

Usage:
  ./trogdor.sh [action] [options]

Actions:
  agent: Run the trogdor agent.
  coordinator: Run the trogdor coordinator.
  client: Run the client which communicates with the trogdor coordinator.
  agent-client: Run the client which communicates with the trogdor agent.
  help: This help message.
```

### kafka-run-class.sh

This `kafka-run-class` tool is a thin wrapper around the Kafka Java class.
It is called by other tools, and should not be run or modified directly.

### **Usage details**

```none
USAGE: ./kafka-run-class.sh [-daemon] [-name servicename] [-loggc] classname [opts]
```

### Related content

- [Kafka Producer Design](../design/producer-design.md#producer-design)
- [Kafka Consumer Design: Consumers, Consumer Groups, and Offsets](../design/consumer-design.md#consumer-design)
- [Kafka Message Delivery Guarantees](../design/delivery-semantics.md#delivery-semantics)
- [Kafka Log Compaction](../design/log_compaction.md#log-compaction)
- [Kafka Replication and Committed Messages](../design/replication.md#replication)
- [Kafka Quotas](../design/quotas.md#quotas)

#### NOTE
This website includes content developed at the [Apache Software Foundation](https://www.apache.org/)
under the terms of the [Apache License v2](https://www.apache.org/licenses/LICENSE-2.0.html).
