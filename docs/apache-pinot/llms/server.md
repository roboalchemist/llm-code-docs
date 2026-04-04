# Source: https://docs.pinot.apache.org/release-0.4.0/basics/components/server.md

# Source: https://docs.pinot.apache.org/release-0.9.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-0.9.0/basics/components/server.md

# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/components/server.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/components/server.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/components/server.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/components/server.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/components/cluster/server.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/components/cluster/server.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/concepts/components/cluster/server.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/concepts/components/cluster/server.md

# Source: https://docs.pinot.apache.org/release-1.4.0/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/concepts/components/cluster/server.md

# Source: https://docs.pinot.apache.org/configuration-reference/server.md

# Source: https://docs.pinot.apache.org/basics/concepts/components/cluster/server.md

# Server

Pinot servers provide the primary storage for [segments](https://docs.pinot.apache.org/basics/concepts/components/table/segment) and perform the computation required to execute queries. A production Pinot cluster contains many servers. In general, the more servers, the more data the cluster can retain in tables, the lower latency the cluster can deliver on queries, and the more concurrent queries the cluster can process.

Servers are typically segregated into real-time and offline workloads, with "real-time" servers hosting only real-time tables, and "offline" servers hosting only offline tables. This is a ubiquitous operational convention, not a difference or an explicit configuration in the server process itself. There are two types of servers:

## Offline

Offline servers are responsible for downloading segments from the segment store, to host and serve queries off. When a new segment is uploaded to the controller, the controller decides the servers (as many as replication) that will host the new segment and notifies them to download the segment from the segment store. On receiving this notification, the servers download the segment file and load the segment onto the server, to server queries off them.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M1c9YtcmhZ3sT3JGbVB%2F-M1cBoDyJPidtPVN1ZEA%2FOfflineServer%20\(4\).jpg?alt=media\&token=a69b79b0-01f4-45a3-bed2-4948474cf70a)

## Real-time

Real-time servers directly ingest from a real-time stream (such as Kafka or EventHubs). Periodically, they make segments of the in-memory ingested data, based on certain thresholds. This segment is then persisted onto the segment store.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M1c9YtcmhZ3sT3JGbVB%2F-M1cD4trRQ2yIC5LAmvJ%2FRealtimeServer%20\(1\).jpg?alt=media\&token=15f21383-4ad5-44db-a033-27aca5639e24)

Pinot servers are modeled as Helix participants, hosting Pinot tables (referred to as *resources* in Helix terminology). Segments of a table are modeled as Helix partitions (of a resource). Thus, a Pinot server hosts one or more Helix partitions of one or more helix resources (*i.e.* one or more segments of one or more tables).

## Starting a server

Make sure you've [set up Zookeeper](https://docs.pinot.apache.org/basics/concepts/components/cluster/..#setup-a-pinot-cluster). If you're using Docker, make sure to [pull the Pinot Docker image](https://docs.pinot.apache.org/basics/concepts/components/cluster/..#setup-a-pinot-cluster). To start a server:

```
Usage: StartServer
 -serverHost               <String>                      : Host name for controller. (required=false)
 -serverPort               <int>                         : Port number to start the server at. (required=false)
 -serverAdminPort          <int>                         : Port number to serve the server admin API at. (required=false)
 -dataDir                  <string>                      : Path to directory containing data. (required=false)
 -segmentDir               <string>                      : Path to directory containing segments. (required=false)
 -zkAddress                <http>                        : Http address of Zookeeper. (required=false)
 -clusterName              <String>                      : Pinot cluster name. (required=false)
 -configFileName           <Config File Name>            : Broker Starter Config file. (required=false)
 -help                                                   : Print this message. (required=false)
```

{% tabs %}
{% tab title="Docker Image" %}

```
docker run \
    --network=pinot-demo \
    --name pinot-server \
    -d ${PINOT_IMAGE} StartServer \
    -zkAddress pinot-zookeeper:2181
```

{% endtab %}

{% tab title="Launcher Scripts" %}

```
bin/pinot-admin.sh StartServer \
    -zkAddress localhost:2181
```

{% endtab %}
{% endtabs %}
