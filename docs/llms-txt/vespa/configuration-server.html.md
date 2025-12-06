# Source: https://docs.vespa.ai/en/operations/self-managed/configuration-server.html.md

# Configuration Servers

 

Vespa Configuration Servers host the endpoint where application packages are deployed - and serves generated configuration to all services - see the [overview](../../learn/overview.html) and [application packages](../../basics/applications.html) for details. I.e., one cannot configure Vespa without config servers, and services cannot run without it.

It is useful to understand the [Vespa start sequence](config-sentinel.html). Refer to the sample applications [multinode](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode) and [multinode-HA](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode-HA) for practical examples of multi-configserver configuration.

Vespa configuration is set up using one or more configuration servers (config servers). A config server uses [Apache ZooKeeper](https://zookeeper.apache.org/) as a distributed data storage for the configuration system. In addition, each node runs a config proxy to cache configuration data - find an overview at [services start](config-sentinel.html).

## Status and config generation

Check the health of a running config server using (replace localhost with hostname):

```
$ curl http://localhost:19071/state/v1/health
```

Note that the config server is a service is itself, and runs with file-based configuration. The application packages deployed will not change the config server - the config server serves this configuration to all other Vespa nodes. This will hence always be config generation 0:

```
$ curl http://localhost:19071/state/v1/config
```

Details in [start-configserver](https://github.com/vespa-engine/vespa/blob/master/configserver/src/main/sh/start-configserver).

## Redundancy

The config servers are defined in [VESPA\_CONFIGSERVERS](files-processes-and-ports.html#environment-variables), [services.xml](../../reference/applications/services/services.html) and [hosts.xml](/en/reference/applications/hosts.html):

```
$ VESPA_CONFIGSERVERS=myserver0.mydomain.com,myserver1.mydomain.com,myserver2.mydomain.com
```

```
```
<services>
    <admin version="2.0">
        <configservers>
            <configserver hostalias="admin0" />
            <configserver hostalias="admin1" />
            <configserver hostalias="admin2" />
        </configservers>
    </admin>
</services>
```
```

```
```
<hosts>
    <host name="myserver0.mydomain.com">
        <alias>admin0</alias>
    </host>
    <host name="myserver1.mydomain.com">
        <alias>admin1</alias>
    </host>
    <host name="myserver2.mydomain.com">
        <alias>admin2</alias>
    </host>
</hosts>
```
```

[VESPA\_CONFIGSERVERS](files-processes-and-ports.html#environment-variables) must be set on all nodes. This is a comma- or whitespace-separated list with the hostname of all config servers, like _myhost1.mydomain.com,myhost2.mydomain.com,myhost3.mydomain.com_.

When there are multiple config servers, the [config proxy](config-proxy.html) will pick a config server randomly (to achieve load balancing between config servers). The config proxy is fault-tolerant and will switch to another config server (if there is more than one) if the one it is using becomes unavailable or there is an error in the configuration it receives.

For the system to tolerate _n_ failures, [ZooKeeper](#zookeeper) by design requires using _(2\*n)+1_ nodes. Consequently, only an odd numbers of nodes is useful, so you need minimum 3 nodes to have a fault-tolerant config system.

Even when using just one config server, the application will work if the server goes down (but deploying application changes will not work). Since the _config proxy_ runs on every node and caches configs, it will continue to serve config to the services on that node. However, restarting a node when config servers are unavailable means that services on the node will be unable to start since the cache will be destroyed when restarting the config proxy.

Refer to the [admin model reference](../../reference/applications/services/admin.html#configservers) for more details on _services.xml_.

## Start sequence

To bootstrap a Vespa application instance, the high-level steps are:

- Start config servers
- Deploy config
- Start Vespa nodes

[multinode-HA](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode-HA) is a great guide on how to start a multinode Vespa application instance - try this first. Detailed steps for config server startup:

1. Set [VESPA\_CONFIGSERVERS](files-processes-and-ports.html#environment-variables) on all nodes, using fully qualified hostnames and the same value on all nodes, including the config servers. 
2. Start the config server on the nodes configured in _services/hosts.xml_. Make sure the startup is successful by inspecting [/state/v1/health](../../reference/api/state-v1.html#state-v1-health), default on port 19071:
```
$ curl http://localhost:19071/state/v1/health
```

```
```
{
    "time" : 1651147368066,
    "status" : {
        "code" : "up"
    },
    "metrics" : {
        "snapshot" : {
            "from" : 1.651147308063E9,
            "to" : 1.651147367996E9
        }
    }
}
```
```
 If there is no response on the health API, two things can have happened: 
  - The config server process did not start - inspect logs using `vespa-logfmt`, or check _$VESPA\_HOME/logs/vespa/vespa.log_, normally _/opt/vespa/logs/vespa/vespa.log_.
  - The config server process started, and is waiting for [Zookeeper quorum](#zookeeper):

```
$ vespa-logfmt -S configserver
```

```
configserver Container.com.yahoo.vespa.zookeeper.ZooKeeperRunner Starting ZooKeeper server with /opt/vespa/var/zookeeper/conf/zookeeper.cfg. Trying to establish ZooKeeper quorum (members: [node0.vespanet, node1.vespanet, node2.vespanet], attempt 1)configserver Container.com.yahoo.container.handler.threadpool.ContainerThreadpoolImpl	Threadpool 'default-pool': min=12, max=600, queue=0
configserver Container.com.yahoo.vespa.config.server.tenant.TenantRepository	Adding tenant 'default', created 2022-04-28T13:02:24.182Z. Bootstrapping in PT0.175576S
configserver Container.com.yahoo.vespa.config.server.rpc.RpcServer	Rpc server will listen on port 19070
configserver Container.com.yahoo.container.jdisc.state.StateMonitor	Changing health status code from 'initializing' to 'up'
configserver Container.com.yahoo.jdisc.http.server.jetty.Janitor	Creating janitor executor with 2 threads
configserver Container.com.yahoo.jdisc.http.server.jetty.JettyHttpServer	Threadpool size: min=22, max=22
configserver Container.org.eclipse.jetty.server.Server	jetty-9.4.46.v20220331; built: 2022-03-31T16:38:08.030Z; git: bc17a0369a11ecf40bb92c839b9ef0a8ac50ea18; jvm 11.0.14.1+1-
configserver Container.org.eclipse.jetty.server.handler.ContextHandler	Started o.e.j.s.ServletContextHandler@341c0dfc{19071,/,null,AVAILABLE}
configserver Container.org.eclipse.jetty.server.AbstractConnector	Started configserver@3cd6d147{HTTP/1.1, (http/1.1, h2c)}{0.0.0.0:19071}
configserver Container.org.eclipse.jetty.server.Server	Started @21955ms
configserver Container.com.yahoo.container.jdisc.ConfiguredApplication	Switching to the latest deployed set of configurations and components.Application config generation: 0
```
 It will hang until quorum is reached, and the second highlighted log line is emitted. Root causes for missing quorum can be: 
  - No connectivity between the config servers. Zookeeper logs the members like `(members: [node0.vespanet, node1.vespanet, node2.vespanet], attempt 1)`. Verify that the nodes running config server can reach each other on port 2181. 
  - No connectivity can be wrong network config. [multinode-HA](https://github.com/vespa-engine/sample-apps/tree/master/examples/operations/multinode-HA) uses a docker network, make sure there are no underscores in the hostnames. 

3. Once all config servers return `up` on _state/v1/health_, an application package can be deployed. This means, if deploy fails, it is always a good idea to verify the config server health first - if config servers are up, and deploy fails, it is most likely an issue with the application package - if so, refer to [application packages](../../basics/applications.html). 
4. A successful deployment logs the following, for the _prepare_ and _activate_ steps:
```
Container.com.yahoo.vespa.config.server.ApplicationRepository	Session 2 prepared successfully.
Container.com.yahoo.vespa.config.server.deploy.Deployment	Session 2 activated successfully using no host provisioner. Config generation 2. File references: [file '9cfc8dc57f415c72']
Container.com.yahoo.vespa.config.server.session.SessionRepository	Session activated: 2
```
5. Start the Vespa nodes. Technically, they can be started at any time. When troubleshooting, it is easier to make sure the config servers are started successfully, and deployment was successful - before starting any other nodes. Refer to the [Vespa start sequence](config-sentinel.html) and [Vespa start / stop / restart](admin-procedures.html#vespa-start-stop-restart). 

Make sure to look for logs on all config servers when debugging.

## Scaling up

Add a config server node for increased fault tolerance or when replacing a node. Read up on [ZooKeeper configuration](#zookeeper-configuration) before continuing. Although it is _possible_ to add more than one config server at a time, doing it one by one is recommended, to keep the ZooKeeper quorum intact.

Due to the ZooKeeper majority vote, use one or three config servers.

1. Install _vespa_ on new config server node. 
2. Append the config server node's hostname to VESPA\_CONFIGSERVERS on all nodes, then (re)start all config servers in sequence to update the ZooKeeper config. By appending, the current config server nodes keep their current ZooKeeper index. Restart the existing config server(s) first. Config server will log which servers are configured when starting up to vespa log. 
3. Update _services.xml_ and _hosts.xml_ with the new set of config servers, then _vespa prepare_ and _vespa activate_. 
4. Restart other nodes one by one to start using the new config servers. This will let the vespa nodes use the updated set of config servers. 

The config servers will automatically redistribute the application data to new nodes.

## Scaling down

This is the inverse of scaling up, and the procedure is the same. Remove config servers from the end of _VESPA\_CONFIGSERVERS_, and here one can remove two nodes in one go, if going from three to one.

## Replacing nodes

- Make sure to replace only one node at a time.
- If you have only one config server you need to first scale up with a new node, then scale down by removing the old node.
- If you have 3 or more you can replace one of the old nodes in VESPA\_CONFIGSERVERS with the new one instead of adding one, otherwise same procedure as in [Scaling up](#scaling-up). Repeat for each node you want to replace.

## Tools

Tools to access config:

- [vespa-get-config](../../reference/operations/self-managed/tools.html#vespa-get-config)
- [vespa-configproxy-cmd](../../reference/operations/self-managed/tools.html#vespa-configproxy-cmd)
- [Config API](../../reference/api/config-v2.html)

## ZooKeeper

[ZooKeeper](https://zookeeper.apache.org/) handles data consistency across multiple config servers. The config server Java application runs a ZooKeeper server, embedded with an RPC frontend that the other nodes use. ZooKeeper stores data internally in _nodes_ that can have _sub-nodes_, similar to a file system.

At [vespa prepare](../../reference/clients/vespa-cli/vespa_prepare), the application's files, along with global configurations, are stored in ZooKeeper. The application data is stored under _/config/v2/tenants/default/sessions/[sessionid]/userapp_. At [vespa activate](../../reference/clients/vespa-cli/vespa_activate), the newest application is activated _live_ by writing the session id into _/config/v2/tenants/default/applications/default:default:default_. It is at that point the other nodes get configured.

Use _vespa-zkcli_ to inspect state, replace with actual session id:

```
$ vespa-zkcli ls /config/v2/tenants/default/sessions/sessionid/userapp
$ vespa-zkcli get /config/v2/tenants/default/sessions/sessionid/userapp/services.xml
```

The ZooKeeper server logs to _$VESPA\_HOME/logs/vespa/zookeeper.configserver.0.log (files are rotated with sequence number)_

### ZooKeeper configuration

The members of the ZooKeeper cluster is generated based on the contents of [VESPA\_CONFIGSERVERS](files-processes-and-ports.html#environment-variables). _$VESPA\_HOME/var/zookeeper/conf/zookeeper.cfg_ is written when (re)starting the config server. Hence, config server(s) must all be restarted when `VESPA_CONFIGSERVERS` changes.

The order of the nodes is used to create indexes in _zookeeper.cfg_, do not change node order.

### ZooKeeper recovery

If the config server(s) should experience data corruption, for instance a hardware failure, use the following recovery procedure. One example of such a scenario is if _$VESPA\_HOME/logs/vespa/zookeeper.configserver.0.log_ says _java.io.IOException: Negative seek offset at java.io.RandomAccessFile.seek(Native Method)_, which indicates ZooKeeper has not been able to recover after a full disk. There is no need to restart Vespa on other nodes during the procedure:

1. [vespa-stop-configserver](../../reference/operations/self-managed/tools.html#vespa-stop-configserver)
2. [vespa-configserver-remove-state](../../reference/operations/self-managed/tools.html#vespa-configserver-remove-state)
3. [vespa-start-configserver](../../reference/operations/self-managed/tools.html#vespa-start-configserver)
4. [vespa](../../clients/vespa-cli.html#deployment) prepare \<application path\>
5. [vespa](../../clients/vespa-cli.html#deployment) activate

This procedure completely cleans out ZooKeeper's internal data snapshots and deploys from scratch.

Note that by default the [cluster controller](../../content/content-nodes.html#cluster-controller) that maintains the state of the content cluster will use the shared same ZooKeeper instance, so the content cluster state is also reset when removing state. Manually set state will be lost (e.g. a node with user state _down_). It is possible to run cluster-controllers in standalone zookeeper mode - see [standalone-zookeeper](../../reference/applications/services/admin.html#cluster-controllers).

### ZooKeeper barrier timeout

If the config servers are heavily loaded, or the applications being deployed are big, the internals of the server may time out when synchronizing with the other servers during deploy. To work around, increase the timeout by setting: [VESPA\_CONFIGSERVER\_ZOOKEEPER\_BARRIER\_TIMEOUT](files-processes-and-ports.html#environment-variables) to 600 (seconds) or higher, and restart the config servers.

## Configuration

To access config from a node not running the config system (e.g. doing feeding via the Document API), use the environment variable [VESPA\_CONFIG\_SOURCES](files-processes-and-ports.html#environment-variables):

```
$ export VESPA_CONFIG_SOURCES="myadmin0.mydomain.com:19071,myadmin1.mydomain.com:19071"
```

Alternatively, for Java programs, use the system property _configsources_ and set it programmatically or on the command line with the _-D_ option to Java. The syntax for the value is the same as for _VESPA\_CONFIG\_SOURCES_.

### System requirements

The minimum heap size for the JVM it runs under is 128 Mb and max heap size is 2 GB (which can be changed with a [setting](../../performance/container-tuning.html#config-server-and-config-proxy)). It writes a transaction log that is regularly purged of old items, so little disk space is required. Note that running on a server that has a lot of disk I/O will adversely affect performance and is not recommended.

### Ports

The config server RPC port can be changed by setting [VESPA\_CONFIGSERVER\_RPC\_PORT](files-processes-and-ports.html#environment-variables) on all nodes in the system.

Changing HTTP port requires changing the port in _$VESPA\_HOME/conf/configserver-app/services.xml_:

```
```
<http>
    <server port="19079" id="configserver" />
</http>
```
```

When deploying, use the _-p_ option, if port is changed from the default.

## Troubleshooting

| Problem | Description |
| --- | --- |
| Health checks | 

Verify that a config server is up and running using [/state/v1/health](../../reference/api/state-v1.html#state-v1-health), see [start sequence](#start-sequence). Status code is `up` if the server is up and has finished bootstrapping.

Alternatively, use [http://localhost:19071/status.html](http://localhost:19071/status.html) which will return response code 200 if server is up and has finished bootstrapping.

Metrics are found at [/state/v1/metrics](../../reference/api/state-v1.html#state-v1-metrics). Use [vespa-model-inspect](../../reference/operations/self-managed/tools.html#vespa-model-inspect) to find host and port number, port is 19071 by default.

 |
| Consistency | 

When having more than one config server, consistency between the servers is crucial. [http://localhost:19071/status](http://localhost:19071/status) can be used to check that settings for config servers are the same for all servers.

[vespa-config-status](../../reference/operations/self-managed/tools.html#vespa-config-status) can be used to check config on nodes.

[http://localhost:19071/application/v2/tenant/default/application/default](http://localhost:19071/application/v2/tenant/default/application/default) displays active config generation and should be the same on all servers, and the same as in response from running [vespa deploy](../../clients/vespa-cli.html#deployment)

 |
| Bad Node | 

If running with more than one config server and one of these goes down or has hardware failure, the cluster will still work and serve config as usual (clients will switch to use one of the good servers). It is not necessary to remove a bad server from the configuration.

Deploying applications will take longer, as [vespa deploy](../../clients/vespa-cli.html#deployment) will not be able to complete a deployment on all servers when one of them is down. If this is troublesome, lower the [barrier timeout](#zookeeper-barrier-timeout) - (default value is 120 seconds).

Note also that if you have not configured [cluster controllers](../../reference/applications/services/admin.html#cluster-controller) explicitly, these will run on the config server nodes and the operation of these might be affected. This is another reason for not trying to manually remove a bad node from the config server setup.

 |
| Stuck filedistribution | 

The config system distributes binary files (such as jar bundle files) using [file-distribution](../../applications/deployment.html#file-distribution) - use [vespa-status-filedistribution](../../reference/operations/self-managed/tools.html#vespa-status-filedistribution) to see detailed status if it gets stuck.

 |
| Memory | 

Insufficient memory on the host / in the container running the config server will cause startup or deploy / configuration problems - see [Docker containers](docker-containers.html).

 |
| ZooKeeper | 

The following can be caused by a full disk on the config server, or clocks out of sync:

```
at com.yahoo.vespa.zookeeper.ZooKeeperRunner.startServer(ZooKeeperRunner.java:92)
Caused by: java.io.IOException: The accepted epoch, 10 is less than the current epoch, 48
```

Users have reported that "Copying the currentEpoch to acceptedEpoch fixed the problem".

 |

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Status and config generation](#status-and-config-generation)
- [Redundancy](#redundancy)
- [Start sequence](#start-sequence)
- [Scaling up](#scaling-up)
- [Scaling down](#scaling-down)
- [Replacing nodes](#replacing-nodes)
- [Tools](#tools)
- [ZooKeeper](#zookeeper)
- [ZooKeeper configuration](#zookeeper-configuration)
- [ZooKeeper recovery](#zookeeper-recovery)
- [ZooKeeper barrier timeout](#zookeeper-barrier-timeout)
- [Configuration](#configuration)
- [System requirements](#system-requirements)
- [Ports](#ports)
- [Troubleshooting](#troubleshooting)

