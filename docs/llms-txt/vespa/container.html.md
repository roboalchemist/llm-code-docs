# Source: https://docs.vespa.ai/en/reference/operations/metrics/container.html.md

# Source: https://docs.vespa.ai/en/reference/applications/services/container.html.md

# Source: https://docs.vespa.ai/en/operations/self-managed/container.html.md

# Source: https://docs.vespa.ai/en/reference/operations/metrics/container.html.md

# Source: https://docs.vespa.ai/en/reference/applications/services/container.html.md

# Source: https://docs.vespa.ai/en/operations/self-managed/container.html.md

# Source: https://docs.vespa.ai/en/reference/operations/metrics/container.html.md

# Source: https://docs.vespa.ai/en/reference/applications/services/container.html.md

# Source: https://docs.vespa.ai/en/operations/self-managed/container.html.md

# Container

 

This is the Container service operational guide.

 ![Vespa Overview](/assets/img/vespa-overview.svg)

Note that "container" is an overloaded concept in Vespa - in this guide it refers to service instance nodes in blue.

Refer to [container metrics](../metrics.html#container-metrics).

## Endpoints

Container service(s) hosts the query and feed endpoints - examples:

- [album-recommendation](https://github.com/vespa-engine/sample-apps/blob/master/album-recommendation/app/services.xml) configures \_both\_ query and feed in the same container cluster (i.e. service):
```
```
<container id="default" version="1.0">
    <document-api />
    <search />
    <nodes>
        <node hostalias="node1" />
    </nodes>
</container>
```
```
- [multinode-HA](https://github.com/vespa-engine/sample-apps/blob/master/examples/operations/multinode-HA/services.xml) configures query and feed in separate container clusters (i.e. services):
```
```
<container id="feed" version="1.0">
    <document-api />
    <document-processing />
    <nodes>
        <node hostalias="node4" />
        <node hostalias="node5" />
    </nodes>
</container>

<container id="query" version="1.0">
    <search />
    <nodes>
        <node hostalias="node6" />
        <node hostalias="node7" />
    </nodes>
</container>
```
```

Observe that `<document-api>` and `<search>` are located in separate clusters in the second example, and endpoints are therefore different.

 **Important:** The first thing to validate when troubleshooting query errors is to make sure that the endpoint is correct, i.e. that query requests hit the correct nodes. A query will be written to the [access log](../access-logging.html)on one of the nodes in the container cluster

## Inspecting Vespa Java Services using JConsole

Determine the state of each running Java Vespa service using JConsole. JConsole is distributed along with the Java developer kit. Start JConsole:

```
$ jconsole <host>:<port>
```

where the host and port determine which service to attach to. For security purposes the JConsole tool can not directly attach to Vespa services from external machines.

### Connecting to a Vespa instance

To attach a JConsole to a Vespa service running on another host, create a tunnel from the JConsole host to the Vespa service host. This can for example be done by setting up two SSH tunnels as follows:

```
$ ssh -N -L<port1>:localhost:<port1> <service-host> &
$ ssh -N -L<port2>:localhost:<port2> <service-host> &
```

where port1 and port2 are determined by the type of service (see below). A JConsole can then be attached to the service as follows:

```
$ jconsole localhost:<port1>
```

Port numbers:

| Service | Port 1 | Port 2 |
| --- | --- | --- |
| QRS | 19015 | 19016 |
| Docproc | 19123 | 19124 |

Updated port information can be found by running:

```
$[vespa-model-inspect](../../reference/operations/self-managed/tools.html#vespa-model-inspect)service <servicename>
```

where the resulting RMIREGISTRY and JMX lines determine port1 and port2, respectively.

### Examining thread states

The state of each container is available in JConsole by pressing the Threads tab and selecting the thread of interest in the threads list. Threads of interest includes _search_, _connector_, _closer_, _transport_ and _acceptor_ (the latter four are used for backend communications).

 Copyright © 2025 - [Cookie Preferences](#)

