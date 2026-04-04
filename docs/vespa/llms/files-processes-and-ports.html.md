# Source: https://docs.vespa.ai/en/operations/self-managed/files-processes-and-ports.html.md

# Files, Processes, Ports, Environment

 

This is a reference of directories used in a Vespa installation, processes that run on the Vespa nodes and ports / environment variables used. Also see [log files](../../reference/operations/log-files.html).

## Directories

| Directory | Description |
| --- | --- |
| $VESPA\_HOME/bin/ | Command line utilities and scripts |
| $VESPA\_HOME/libexec/vespa/ | Command line utilities and scripts |
| $VESPA\_HOME/sbin/ | Server programs, daemons, etc |
| $VESPA\_HOME/lib64/ | Dynamically linked libraries, typically third-party libraries |
| $VESPA\_HOME/lib/jars/ | Java archives |
| $VESPA\_HOME/logs/vespa/ | Log files |
| $VESPA\_HOME/var/db/vespa/config\_server/serverdb/ | Config server database and user applications |
| $VESPA\_HOME/share/vespa/ | A directory with config definitions and XML schemas for application package validation |
| $VESPA\_HOME/conf/vespa | Various config files used by Vespa or libraries Vespa depend on |

## Processes and ports

The following is an overview of which ports and port ranges are used by the different services in a Vespa system. Note that for services capable of running multiple instances on the same node, all instances will run within the listed port range.

Processes are run as user `vespa`.

Many services are allocated ports dynamically. So even though the allocation is deterministic, i.e. the same system will get the same ports on subsequent startups, a particular service instance may get different ports when the overall system setup is changed through [services.xml](../../reference/applications/services/services.html). Use [vespa-model-inspect](../../reference/operations/self-managed/tools.html#vespa-model-inspect) to see port allocations.

- The number of ports used in a range depends on number of instances that are running 
- Not all ports within a range are used, but they are assigned each service to support future extensions 
- The range from 19100 is used for internal communication ports, i.e. ports that are not necessary to use from an external API 
- See [Configuring Http Servers and Filters](../../applications/http-servers-and-filters.html) for how to configure Container ports and [services.xml](../../reference/applications/services/services.html) for how to configure other ports 

| Process | Host | Port/range | ps | Function |
| --- | --- | --- | --- | --- |
| [Config server](configuration-server.html) | Config server nodes | 19070-19071 | java (...) -jar $VESPA\_HOME/lib/jars/standalone-container-jar-with-dependencies.jar | Vespa Configuration server |
| 2181-2183 | | Embedded Zookeeper cluster ports, see [zookeeper-server.def](https://github.com/vespa-engine/vespa/blob/master/configdefinitions/src/vespa/zookeeper-server.def) |
| [Config sentinel](config-sentinel.html) | All nodes | 19098 | $VESPA\_HOME/sbin/vespa-config-sentinel | Sentinel that starts and stops vespa services and makes sure they are running unless they are manually stopped |
| [Config proxy](config-proxy.html) | All nodes | 19090 | java (…) com.yahoo.vespa.config.proxy.ProxyServer | Communication liaison between Vespa processes and config server. Caches config in memory |
| [Slobrok](slobrok.html) | Admin nodes | 19099 for RPC port, HTTP port dynamically allocated in the 19100-19899 range | $VESPA\_HOME/sbin/vespa-slobrok | Service location object broker |
| [logd](../../reference/operations/log-files.html#logd) | All nodes | 19089 | $VESPA\_HOME/sbin/vespa-logd | Reads local log files and sends them to log server |
| [Log server](../../reference/operations/log-files.html#log-server) | Log server node | 19080 | java (...) -jar lib/jars/logserver-jar-with-dependencies.jar | Vespa Log server |
| [Metrics proxy](monitoring.html#metrics-proxy) | All nodes | 19092-19095 | java (...) -jar $VESPA\_HOME/lib/jars/container-disc-with-dependencies.jar | Provides a single access point for metrics from all services on a Vespa node |
| [Distributor](../../content/content-nodes.html#distributor) | Content cluster | dynamically allocated in the 19100-19899 range | $VESPA\_HOME/sbin/vespa-distributord-bin | Content layer distributor processes |
| [Cluster controller](../../content/content-nodes.html#cluster-controller) | Content cluster | 19050, plus ports dynamically allocated in the 19100-19899 range | java (...) -jar $VESPA\_HOME/lib/jars/container-disc-jar-with-dependencies.jar | Cluster controller processes, manages state for content nodes |
| [proton](../../content/proton.html) | Content cluster | dynamically allocated in the 19100-19899 range | $VESPA\_HOME/sbin/vespa-proton-bin | Searchnode process, receives queries from the container and returns results from the indexes. Also receives feed and indexes documents |
| [container](../../applications/containers.html) | Container cluster | 8080 | java (...) -jar $VESPA\_HOME/lib/jars/container-disc-with-dependencies.jar | Container running servers, handlers and processing components |

## System limits

The [startup scripts](admin-procedures.html#vespa-start-stop-restart) checks that system limits are set, failing startup if not. Refer to [vespa-configserver.service](https://github.com/vespa-engine/vespa/blob/master/vespabase/src/vespa-configserver.service.in) and [vespa.service](https://github.com/vespa-engine/vespa/blob/master/vespabase/src/vespa.service.in) for minimum values.

## Core dumps

Example settings:

```
$ mkdir -p /tmp/cores && chmod a+rwx /tmp/cores
$ echo "/tmp/cores/core.%e.%p.%h.%t" > /proc/sys/kernel/core_pattern
```

This will write files like _/tmp/cores/core.vespa-proton-bi.1721.localhost.1580387387_.

## Environment variables

Vespa configuration is set in [application packages](../../basics/applications.html). Some configuration is used to bootstrap nodes - this is set in environment variables. Environment variables are only read at startup.

_$VESPA\_HOME/conf/vespa/default-env.txt_ is read in Vespa start scripts - use this to modify variables ([example](multinode-systems.html#aws-ec2)). Each line has the format `action variablename value` where the items are:

| Item | Description |
| --- | --- |
| action | One of `fallback`, `override`, or `unset`. `fallback` sets the variable if it is unset (or empty). `override` set the value regardless. `unset` unsets the variable. |
| variablename | The name of the variable, e.g. `VESPA_CONFIGSERVERS` |
| value | The rest of the line is the variable's value. |

Refer to the [template](https://github.com/vespa-engine/vespa/blob/master/vespabase/conf/default-env.txt.in) for format.

| Environment variable | Description |
| --- | --- |
| VESPA\_CONFIGSERVERS | A comma-separated list of hosts to run configservers, use fully qualified hostnames. Should always be set to the same value on all hosts in a multi-host setup. If not set, `localhost` is assumed. Refer to [configuration server operations](configuration-server.html). |
| VESPA\_HOSTNAME | 

Vespa uses `hostname` for node identity. But sometimes this doesn't work properly, either because that name can't be used to find an IP address which works for connecting to services running on the node, or it's just that the name doesn't agree with what the config server thinks the node's host name is. In this case, override by setting the `VESPA_HOSTNAME`, to be used instead of running the `hostname` command.

Note that `VESPA_HOSTNAME` will be used _both_ when a node identifies itself to the config server _and_ when a service on that node registers a network connection point that other services can connect to.

An error message with "hostname detection failed" is emitted if the `VESPA_HOSTNAME` isn't set and the hostname isn't usable. If `VESPA_HOSTNAME` is set to something that cannot work, an error with "hostname validation failed" is emitted instead.

 |
| VESPA\_CONFIG\_SOURCES | Used by libraries like the [Document API](../../writing/document-api-guide.html) to set config server endpoints. Refer to [configuration server operations](configuration-server.html#configuration) for example use. |
| VESPA\_WEB\_SERVICE\_PORT | The port number where REST apis will run, default `8080`. This isn't strictly needed, as the port number can be set for each HTTP server in `services.xml`, but with a big application it can be easier to set the default port number just once. Also note that this needs to be set when starting the _configserver_, since the REST api implementation gets its port number from there. |
| VESPA\_TLS\_CONFIG\_FILE | Absolute path to [TLS configuration file](../../security/mtls). |
| VESPA\_CONFIGSERVER\_JVMARGS | JVM arguments for the config server - see [tuning](../../performance/container-tuning.html#config-server-and-config-proxy). |
| VESPA\_CONFIGPROXY\_JVMARGS | JVM arguments for the config proxy - see [tuning](../../performance/container-tuning.html#config-server-and-config-proxy). |
| VESPA\_LOG\_LEVEL | Tuning of log output from tools, see [controlling log levels](../../reference/operations/log-files.html#controlling-log-levels). |

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Directories](#directories)
- [Processes and ports](#processes-and-ports)
- [System limits](#vespa-system-limits)
- [Core dumps](#core-dumps)
- [Environment variables](#environment-variables)

