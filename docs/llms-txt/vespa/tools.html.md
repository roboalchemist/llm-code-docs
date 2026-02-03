# Source: https://docs.vespa.ai/en/reference/operations/tools.html.md

# Source: https://docs.vespa.ai/en/reference/operations/self-managed/tools.html.md

# Vespa Command-line Tools

 

This is the reference for the Vespa command-line tools.

 **Note:** The tools listed on this page are primarily used for operating and debugging a _self-hosted_ Vespa instance. For most use-cases, we recommend the [Vespa CLI](../../../clients/vespa-cli.html), which should work against most Vespa applications regardless of how they are deployed.

You can run these tools in [Vespa Docker image](https://hub.docker.com/r/vespaengine/vespa/tags):

```
docker run --entrypoint bash vespaengine/vespa ./opt/vespa/bin/[tool] [args]
```

## vespa-configproxy-cmd

_vespa-configproxy-cmd_ is a status and control tool for the[config proxy](../../../operations/self-managed/config-proxy.html). The config proxy runs on all nodes as a proxy for one or more[config servers](../../../operations/self-managed/configuration-server.html). It connects to the config proxy on localhost by default.

Run it without arguments to dump a list of active configIds - format specification:

`<config definition name>,<config id>,<config generation>,<MD5 checksum>,<xxHash checksum>`

Synopsis: `vespa-configproxy-cmd [args]`

Example:

```
$ vespa-configproxy-cmd -m sources
```

Find a more comprehensive example in [inspecting config](../../../operations/self-managed/config-proxy.html#inspecting-config).

| Option | Description |
| --- | --- |
| -m | method, available methods are: 

| cache | Output the config proxy cache content (overview) |
| gc | |
| dumpcache | |
| statistics | |
| heap | |
| getConfig | Get config (see [vespa-get-config](#vespa-get-config)) |
| getmode | Outputs the current mode of the config proxy |
| setmode | Use _default_ or _memorycache_ - [example](../../../operations/self-managed/config-proxy.html) |
| invalidatecache | Clears the current cache in the config proxy |
| cachefull | Output the config proxy cache content (including config payload) |
| sources | Output the config proxy's upstream config sources |
| updatesources | Updates the config proxy's upstream config sources to the supplied ones |

 |
| -p | port number, optional |
| -s | hostname, optional |
| -h | help text and usage |

## vespa-configserver-remove-state

_vespa-configserver-remove-state_ removes the config server state on the host.

Synopsis: `vespa-configserver-remove-state [-force]`

| Option | Description |
| --- | --- |
| -force | Do not ask for confirmation before removal |

## vespa-config-status

_vespa-config-status_ can run on any machine in a Vespa cluster and outputs a list of all running services which is running with an outdated application package. It can be invoked without any arguments or with optional arguments.

Synopsis: `vespa-config-status [-v] [-c host] [-c host:port] [-f host0,...,hostN]`

Example:

```
$ vespa-config-status
```

| Option | Description |
| --- | --- |
| -v | Verbose - show all services, even if they are up-to-date |
| -c arg | Get the Vespa cluster configuration from the config server specified by host and port. Use _host_ or _host:port_ for config server |
| -f | Filter to only query config status for the given comma-separated set of hosts |

## vespa-deploy

_vespa-deploy_ is a standalone tool to deploy an application package. Prefer the [Vespa CLI](../../../clients/vespa-cli.html#deployment) instead. Under the hood, deployment uses the [deploy REST API](/en/reference/api/deploy-v2.html), which you can also use directly. Refer to the [deploy reference](../../applications/application-packages.html#deploy) for details.

Synopsis: `vespa-deploy [-h] [-v] [-n] [-f] [-t timeout] [-c hostname] [-p port] prepare|activate|upload|fetch|help [args]`

Example:

```
$ vespa-deploy prepare [application-path|zip-file] && vespa-deploy activate
```

```
$ vespa-deploy prepare app.zip && vespa-deploy activate
```

| Command | Description |
| --- | --- |
| prepare | _vespa-deploy prepare_ combines the [upload](../../api/deploy-v2.html#create-session) and [prepare](../../api/deploy-v2.html#prepare-session) steps. |
| activate | _vespa-deploy activate_ invokes the [activate](../../api/deploy-v2.html#activate-session) step. |
| upload | _vespa-deploy upload_ uploads an application package |
| fetch | _vespa-deploy fetch_ fetches an application package. Useful to get the active configuration for an instance. |
| help | Same as **-h** |

| Option | Description |
| --- | --- |
| -h | Show help text |
| -v | Verbose |
| -n | Dry-run deployment |
| -f | Force - ignore validation errors |
| -t | Timeout |
| -c | Config server hostname |
| -p | Config server port |

## vespa-destination

_vespa-destination_ is a simple receiver for messagebus messages. It outputs messages received on stdout. Also see [vespa-visit-target](#vespa-visit-target).

Synopsis: `vespa-destination [options]`

Example:

```
$ vespa-destination --name msg_sink
```

| Option | Description |
| --- | --- |
| --instant | Reply in message thread |
| --name arg | Slobrok name to register |
| --maxqueuetime arg | Adjust the in-queue size to have a maximum queue wait period of this many ms (default -1 = unlimited) |
| --silent #nummsg | Do not dump anything, but progress every #nummsg |
| --sleeptime arg | The number of milliseconds to sleep per message, to simulate processing time |
| --threads arg | The number of threads to process the incoming data |
| --verbose | Dump the contents of certain messages to stdout |

## vespa-fbench-filter-file

```
usage: vespa-fbench-filter-file [-a] [-h] [-m maxLineSize]

Read concatenated logs from stdin and write
extracted query urls to stdout.

 -a : all parameters to the original query urls are preserved.
            If the -a switch is not given, only 'query' and 'type'
            parameters are kept in the extracted query urls.
 -h : print this usage information.
 -m <num> : max line size for input/output lines.
            Can not be less than the default [10240]
```

## vespa-fbench-geturl

```
usage: vespa-fbench-geturl <host> <port> <url>
```

## vespa-fbench-split-file

```
usage: vespa-fbench-split-file [-p pattern] [-m maxLineSize] <numparts> [<file>]

Reads from <file> (stdin if <file> is not given) and
randomly distributes each line between <numpart> output
files. The names of the output files are generated by
combining the <pattern> with sequential numbers using
the sprintf function.

 -p pattern : output name pattern ['query%03d.txt']
 -m <num> : max line size for input/output lines.
              Can not be less than the default [10240]
 <numparts> : number of output files to generate.
```

## vespa-feeder

_vespa-feeder_ is a feeding client that parses[JSON](../../schemas/document-json-format.html) input as Vespa document operations and sends to a Vespa application. It parses the content of the input sequentially and feeds each operation in order. However, since many operations will be pending at any time, and because the processing time of an operation varies, there is no guarantee as to which order operations will reach the content nodes. As this can be important when it comes to operations that apply to the same document id, there is logic in place to not send an operation for a document id to which there is already a pending operation.

_vespa-feeder_ prints a report at the end of the feed. To print this report once a minute, use _--verbose_:

```
Messages sent to vespa (route default) :
----------------------------------------
PutDocument: ok: 999997 msgs/sec: 411.38 failed: 0ignored: 0latency(min, max, avg): 2, 4360, 99
```

_ignored_ reports the number of documents that could not be routed to any [content clusters](../../applications/services/content.html) because they did not match any of the[configured document types](../../applications/services/content.html#documents) or selections - examples are:

- A document type is removed from the application and the feed file contains documents of this type 
- One or more selection expressions restrict the documents the cluster accepts, and the feed file contains documents that are excluded. An example is feeding [expired documents](../../../schemas/documents.html#document-expiry) - a selection for documents that are less than 30 days old and the feed file contains documents that are 30+ days old 

Synopsis: `vespa-feeder [--abortondataerror true|false] [--abortonsenderror true|false] [--file arg] [--maxpending arg] [--maxpendingsize arg] [--maxfeedrate arg] [mode standard|benchmark] [--noretry] [--retrydelay arg] [--route arg] [--timeout arg] [--trace arg] [--validate] [--dumpDocuments filename] [--numthreads arg] [create-if-non-existent] [-v,--verbose] filename`

Example:

```
$ vespa-feeder file.json
```

| Option | Description |
| --- | --- |
| --abortondataerror arg | Abort if the input has errors (true|false) - default true. Set to _false_ in case the input has errors (e.g., invalid characters). _vespa-feeder_ notifies on parsing errors at the end of the feed, but it will not abort |
| --abortonsenderror arg | Abort if an error occurred while sending operations to Vespa (true|false) - default true |
| --file arg | Input files to read. These can also be passed as arguments without the option prefix. If none is given, this tool parses identifiers from stdin |
| --maxpending arg | Maximum number of pending operations. This disables dynamic throttling, use with care |
| --maxpendingsize arg | Maximum size (in bytes) of pending operations |
| --maxfeedrate arg | Limits the feed rate to the given number (operations/second) |
| --mode | The mode to run vespa-feeder in (standard|benchmark) - default standard |
| --noretry | Disables retries of recoverable failures |
| --retrydelay arg | The time (in seconds) to wait between retries of a failed operation. Default 1 |
| --route arg | The [route](../../../writing/document-routing.html) to send the data to. Default the _default_ route |
| --timeout arg | Time (in seconds) allowed for sending operations. Default 180 |
| --trace arg | Trace level of network traffic. Default 0 |
| --validate | Run validation tool on input files - do not feed |
| --dumpDocuments \<filename\> | File where documents in the put are serialized |
| --numthreads arg | How many threads to use for sending. Default 1 |
| --create-if-non-existent | Enable setting of create-if-non-existent to true on all document updates in the given feed |
| -v, --verbose | Enable verbose output of progress |

## vespa-get

_vespa-get_ retrieves documents from a Vespa content cluster, and prints to _stdout_._vespa-get_ retrieves documents identified by the document ids passed as command line arguments. If no document ids are passed through the command line interface, ids will be read from _stdin_ - separated by line breaks.

Synopsis: `vespa-get <options> [documentid...]`

| Option | Description |
| --- | --- |
| -a,--trace _tracelevel_ | Trace level to use (default 0) |
| -c,--configid _configid_ | Use the specified config id for messagebus configuration |
| -f,--fieldset _fieldset_ | Retrieve the specified fields only (see [Document field sets](../../../schemas/documents.html#fieldsets)). Default: `[document]` |
| -h,--help | Show this syntax page |
| -i,--printids | Show only identifiers of retrieved documents |
| -j,--jsonoutput | JSON output (default) |
| -l,--loadtype _loadtype_ | Load type (default "") |
| -n,--noretry | Do not retry operation on transient errors, as is default |
| -r,--route _route_ | Send request to the given messagebus route |
| -s,--showdocsize | Show binary size of document |
| --shorttensors | Output using [tensor short form](../../schemas/document-json-format.html#tensor) |
| -t,--timeout _timeout_ | Set timeout for the request in seconds (default 0) |
| -u,--cluster _cluster_ | Send request to the given content cluster |

## vespa-get-cluster-state

Get cluster state - refer to [content nodes](../../../content/content-nodes.html).

Synopsis: `vespa-get-cluster-state [options]`

| Option | Description |
| --- | --- |
| -h, --help | Show help |
| -v | More verbose output |
| -s | Less verbose output |
| --show-hidden | Also show hidden undocumented debug options |
| -c, --cluster | The cluster name of the cluster to query. If unspecified, and vespa is installed on the current node, information will be attempted auto-extracted |
| -f, --force | Force execution |
| --config-server | Host name of the config server to query |
| --config-server-port | Port to connect to the config server on |
| --config-request-timeout | Timeout of config request |

## vespa-get-config

_vespa-get-config_ is a command-line tool to get configuration from a [config server](../../../operations/self-managed/configuration-server.html)or [config proxy](../../../operations/self-managed/config-proxy.html). By default, it connects to the config proxy on localhost, fetches config from its cache and prints the config payload on stdout. Configuration is addressed using name and [configId](../../../applications/configapi-dev.html#config-id). If configId is omitted, the global and default data for that name is returned. The default port number is 19090, the config proxy's port - use 19070 to access a config server. Also check [ports](../../../operations/self-managed/files-processes-and-ports.html).

Synopsis: `vespa-get-config -n defName -i configId <option> [args]`

Example:

```
$ vespa-get-config -n container.statistics -i search/cluster.search
```

Find a more comprehensive example in [inspecting config](../../../operations/self-managed/config-proxy.html#inspecting-config).

| Option | Description |
| --- | --- |
| -n | config definition name, including namespace (on the form \<namespace\>.\<name\>) |
| -i | config id, optional |
| -a | config def schema file, optional (if you want to use another schema than the one known for the config server) |
| -m | defMd5, optional |
| -c | configMd5, optional |
| -t | server timeout, in seconds, default value 3, optional |
| -w | timeout, default value 10, optional |
| -s | server hostname, default localhost, optional |
| -p | port, default 19090, optional |
| -d | debug mode, optional |
| -h | help text and usage |

## vespa-get-node-state

Get the state of one or more storage services from the fleet controller - refer to [content nodes](../../../content/content-nodes.html):

| State | Description |
| --- | --- |
| Unit state | The state of the node seen from the cluster controller. |
| User state | The state the administrator wants the node to be in, default "up". Can be set by using [vespa-set-node-state](#vespa-set-node-state) or by the cluster controller |
| Generated state | The state of a given node in the current cluster state. This is the state all the other nodes know about. This state is a product of the other two states and cluster controller logic to keep the cluster stable. |

Synopsis: `vespa-get-node-state [options]`

| Option | Description |
| --- | --- |
| -h, --help | Show help |
| -v | More verbose output |
| -s | Less verbose output |
| --show-hidden | Also show hidden undocumented debug options |
| -c, --cluster | The cluster name of the cluster to query. If unspecified, and vespa is installed on the current node, information will be attempted auto-extracted |
| -f, --force | Force execution |
| -t, --type | Node type - can either be 'storage' or 'distributor'. If not specified, the operation will use state for both types |
| -i, --index | Node index. If not specified, all nodes found running on this host will be used |
| --config-server | Host name of the config server to query |
| --config-server-port | Port to connect to the config server on |
| --config-request-timeout | Timeout of config request |

## vespa-index-inspect

Use _vespa-index-inspect_ to inspect indexed data on a content node. To troubleshoot [query rewriting](../../../linguistics/query-rewriting.html)and [linguistic transformations](../../../linguistics/linguistics.html)use this [guide](../../../querying/text-matching.html#index-and-attribute) instead.

It shows posting list information (per token or all/range), or dumps the indexed tokens:

```
vespa-index-inspect showpostings [--indexdir indexDir] --field field word

vespa-index-inspect showpostings [--indexdir indexDir] [--field field] --transpose \
  [--docidlimit docIdLimit] [--mindocid mindocid]

vespa-index-inspect dumpwords [--indexdir indexDir] --field field \
  [--minnumdocs minnumdocs] [--verbose] [--wordnum]
```

Synopsis:`vespa-index-inspect showpostings|dumpwords [--indexdir path] [--field fieldname] [--transpose] [--minnumdocs count] [--docidlimit docIdLimit] [--mindocid mindocid] [--verbose] [--wordnum] [word]`

Example (make sure to flush the index before using):

```
$[vespa-proton-cmd](#vespa-proton-cmd)--local triggerFlush && \
  vespa-index-inspect dumpwords \
  --indexdir /opt/vespa/var/db/vespa/search/cluster.music/n0/documents/music/0.ready/index/index.flush.1 \
  --field artist
bad	2
so	1
```

| Option | Description |
| --- | --- |
| --indexdir _path_ | Index location |
| --field _fieldname_ | Field to analyze |
| --transpose | Dump all tokens |
| --minnumdocs _count_ | Minimum number of documents to analyze |
| --docidlimit _docid_ | Dump up to this doc id |
| --mindocid _docid_ | Start from this docid |
| --wordnum | Also dump token numbers |
| --verbose | Verbose output |

## vespa-attribute-inspect

Use _vespa-attribute-inspect_ to inspect the content of an attribute field on a content node. To troubleshoot [query rewriting](../../../linguistics/query-rewriting.html)and [linguistic transformations](../../../linguistics/linguistics.html)use this [guide](../../../querying/text-matching.html#index-and-attribute) instead.

Synopsis: `vespa-attribute-inspect [-p attribute] [-a] [-s attribute] <attribute>`

Example (make sure to flush the attribute before using):

```
$[vespa-proton-cmd](#vespa-proton-cmd)--local triggerFlush && \
  vespa-attribute-inspect -p /opt/vespa/var/db/vespa/search/cluster.music/n0/documents/music/0.ready/attribute/year/snapshot-10/year && \
  cat /opt/vespa/var/db/vespa/search/cluster.music/n0/documents/music/0.ready/attribute/year/snapshot-10/year.out
```

| Option | Description |
| --- | --- |
| -p | print content to \<attribute\>.out |
| -s | save attribute to \<attribute\>.save.dat |

## vespa-jvm-dumper

Dump JVM heap, thread stacks, and other debugging information from a Java-based Vespa service.

Invoke binary without arguments to print help and list the services running on this node.

```
$ vespa-jvm-dumper
```

Produce JVM debugging information by invoking the binary with the config ID of the target service and the output directory.

```
$ vespa-jvm-dumper default/container.1 /opt/vespa/tmp/jvm-dump
```

## vespa-logctl

Print or modify log levels for a VESPA service, stored in_$VESPA\_HOME/var/db/vespa/logcontrol/service.logcontrol_. Refer to [controlling log levels](../log-files.html#controlling-log-levels) for details._component-specification_ specifies which subcomponents of the service should be controlled. If empty, all components are controlled:

- `x.` : Matches only component x
- `x` : Matches component x and all its subcomponents

Synopsis (show log levels): `vespa-logctl [OPTION] <service>[:component-specification]`

Synopsis (set log levels): `vespa-logctl [OPTION] <service>[:component-specification] <level-mods>`

_level-mods_ are defined as : \<level\>=\<on|off\>[,\<level\>=\<on|off\>]...

_level_ is one of:`all`, `fatal`, `error`, `warning`,`info`, `event`, `config`, `debug`, `spam`

Example: For service `container`, set `com.yahoo.search.searchchain`and all subcomponents of `com.yahoo.search.searchchain` to enable all except spam and debug:

```
$ vespa-logctl container:com.yahoo.search.searchchain all=on,spam=off,debug=off
```

| Option | Description |
| --- | --- |
| -c | Create the control file if it does not exist (implies -n) |
| -a | Update all .logcontrol files |
| -r | Reset to default levels |
| -n | Create the component entry if it does not exist |
| -f _file_ | Use \<file\> as the log control file |
| -d _dir_ | Look in \<dir\> for log control files |

## vespa-logfmt

`vespa-logfmt` reads Vespa log files, selects messages, and writes a formatted version of these messages to standard output. If no file argument is given, vespa-logfmt will read the last Vespa log file `$VESPA_HOME/logs/vespa/vespa.log`(this also works with the `-f` option). Otherwise, reads only the files given as arguments. To read standard input, supply a single dash ’-’ as a file argument. Refer to the [logs reference](../log-files.html).

Synopsis: `
vespa-logfmt [-l levellist] [-s fieldlist] [-p pid] [-S service] [-H host]
[-c regex] [-m regex] [-f] [-N] [-t] [-ts] [file …]`

Examples:

Display only messages with log level "event", printing a human-readable time (without any fractional seconds), the service generating the event and the event message:

```
$ vespa-logfmt -l event -s fmttime,service,message
...
[2017-09-05 06:16:16] config-sentinel stopped/1 name="sbin/vespa-config-sentinel -c hosts/vespa-container (pid 1558)" pid=1558 exitcode=1
[2017-09-05 06:16:16] config-sentinel starting/1 name="sbin/vespa-config-sentinel -c hosts/vespa-container (pid 1564)"
[2017-09-05 06:16:16] config-sentinel started/1 name="config-sentinel"
[2017-09-05 06:17:00] configserver count/1 name=configserver.failedRequests value=0
[2017-09-05 06:17:00] configserver count/1 name=procTime value=0
[2017-09-05 06:17:00] configserver count/1 name=configserver.requests value=0
```

Display messages with log levels that are _not_ any of_info, debug,_ or _event,_ printing the time in seconds and microseconds, the log level, the component name, and the message text:

```
$ vespa-logfmt -l all-info,-debug -s level -s time,usecs,component,message -t -l -event
...
1504592294.738000 WARNING : configproxy.com No config found for name=sentinel,namespace=cloud.config,configId=hosts/vespa-container within timeout, will retry
1504592296.388000 WARNING : configproxy.com Request callback failed: APPLICATION_NOT_LOADED. Connection spec: tcp/localhost:19070, error message: Failed request (No application exists) from Connection { Socket[addr=/127.0.0.1,port=37806,localport=19070] }
1504592307.949461 WARNING : config-sentinel Connection to tcp/localhost:19090 failed or timed out
1504592307.949587 WARNING : config-sentinel FRT Connection tcp/localhost:19090 suspended until 2017-09-05 06:19:07 GMT
```

| Option | Description |
| --- | --- |
| -l _levellist_ (--level=_levellist_) | Filter messages by log level. By default, only messages of level _fatal, error, warning_, and _info_ will be included, while messages of level _config, event, debug_, and _spam_ will be ignored. This option allows you to replace or modify the list of log levels to be included. _levellist_ is a comma-separated list of level names. 
- The name _all_ may be used to add all known levels
- You may use + or - in front of terms to add or remove from the current (or default) list of levels instead of replacing it
- Adding term

 |
| -s _fieldlist_ | Select which fields of log messages to show. The output field order is fixed. When using this option, only the named fields will be printed. The default fields are as [**-s fmttime,msecs,level,service,component,message**]. The fieldlist is a comma-separated list of field names. The name _all_ may be used to add all possible fields. Prepending a minus sign will turn off the display of the named field. Starting the list with a plus sign will add and remove fields from the current (or default) list of fields instead of replacing it. Using this option several times works as if the given _fieldlist_ arguments had been concatenated into one comma-separated list. Fields: 

| time | Print the time in seconds since the epoch. Ignored if _fmttime_ is shown |
| fmttime | Print the time in human-readable [YYYY-MM-DD HH:mm:ss] format. Note that the time is printed in the local timezone. To get GMT output, use `env TZ=GMT vespa-logfmt` |
| msecs | Add milliseconds after the seconds in _time_ and _fmttime_ output. Ignored if _usecs_ is in effect |
| usecs | Add microseconds after the seconds in _time_ and _fmttime_ output |
| host | Print the hostname field |
| level | Print the level field (upper-cased) |
| pid | Print the pid field |
| service | Print the service field |
| component | Print the component field |
| message | Print the message text field. You probably always want to add this |

 |
| -p _pid_ | Select messages where the pid field matches the _pid_ string |
| -S _service_ | Select messages where the service field matches the _service_ string |
| -H _host_ | Select messages where the hostname field matches the _host_ string |
| -c _regex_ | Select messages where the component field matches the _regex_, using _perlre_ regular expression matching |
| -m _regex_ | Select messages where the message text field matches the _regex_, using _perlre_ regular expression matching |
| -f | Invoke tail -F to follow the input file |
| -N | De-quote quoted newlines in the message text field to an actual newline plus tab |
| -t | Format the component field (if shown) as a fixed-width string, truncating if necessary |
| -ts | Format the service field (if shown) as a fixed-width string, truncating if necessary |
| -i, --internal | Only include log entries emitted by the Vespa platform, i.e., exclude log entries from custom components |

## vespa-model-inspect

_vespa-model-inspect_ is a tool for inspecting the topology and services of a Vespa system. Hosts, services, clusters, ports, URLs, and config ids can be inspected. It can run on any machine in a Vespa cluster that is running a Vespa configuration server.

Synopsis: `vespa-model-inspect [-c host | host:port] [-t tag] [-h] [-u] [-v] command`

| Command | Description |
| --- | --- |
| hosts | Show hostnames of all hosts in the Vespa system |
| services | Show a list of all service types in the Vespa system |
| clusters | Show a list of all named clusters in the Vespa system |
| configids | Show a list of all config ids in the Vespa system |
| filter:ports | List ports matching filter options |
| host _hostname_ | Show host details: What services are running, and what ports have they allocated |
| service _servicetype_ | Show service details: What instances of the service are running, on what hosts, and what ports have they allocated |
| cluster _clustername_ | Show all services in the cluster, with details on hostname and allocated ports |
| configid _configid_ | Show all services using this configid |
| get-index-of _servicetype_ _host_ | Show all indexes for instances of the service type on the given host |

| Option | Description |
| --- | --- |
| -c _host_ | _host:port_ | Specify host and port (or just host) to use for getting the config that this tool displays. Default is to use the configserver. You might want to use localhost:19090 if you are on a host with a running Vespa system without a config server |
| -h | Show usage |
| -t _tag_ | to filter on a port tag |
| -u | Show URLs for services |
| -v | Verbose mode |

Examples:

```
$ vespa-model-inspect hosts
mynode.mydomain.com

$ vespa-model-inspect services
config-sentinel
configproxy
configserver
container
container-clustercontroller
distributor
docprocservice
filedistributorservice
logd
logserver
searchnode
slobrok
storagenode

$ vespa-model-inspect -u service distributor
distributor @ myhost.mydomain.com : content
myapp/distributor/4
    tcp/myhost1.mydomain.com:19112 (MESSAGING)
    tcp/myhost1.mydomain.com:19113 (STATUS RPC)
    http://myhost1.mydomain.com:19114/ (STATE STATUS HTTP)
distributor @ myhost2.mydomain.com : content
myapp/distributor/5
    tcp/myhost2.mydomain.com:19112 (MESSAGING)
    tcp/myhost2.mydomain.com:19113 (STATUS RPC)
    http://myhost2.mydomain.com:19114/ (STATE STATUS HTTP)
distributor @ myhost3.mydomain.com : content
```

## vespa-print-default

Internal script used by other scripts to find hostname, config server addresses/ports, version, and more. Not intended for end-user usage.

## vespa-proton-cmd

Use _vespa-proton-cmd_ to send commands to [proton](../../../content/proton.html).

Synopsis: `vespa-proton-cmd HOSTSPEC COMMAND [ARGS]`

The _hostspec_ argument is one of `port|spec|--local|--id=name`. Use [vespa-model-inspect](#vespa-model-inspect) to locate the search node ADMIN RPC port:

```
$ vespa-model-inspect service searchnode
searchnode @ /mynode.myhost.com : search
music/search/cluster.music/0
    tcp/mynode.myhost.com:19108 (STATUS ADMIN RTC RPC)
    tcp/mynode.myhost.com:19109 (FS4)
    tcp/mynode.myhost.com:19110 (TEST HACK SRMP)
    tcp/mynode.myhost.com:19111 (ENGINES-PROVIDER RPC)
    tcp/mynode.myhost.com:19112 (STATE HEALTH JSON HTTP)
```

Example:

```
$ vespa-proton-cmd 19108 triggerFlush
  OK: flush trigger enabled
```

Unless the **-h** or **--help** option is used, one of these commands must be present:

| Command | Description |
| --- | --- |
| getProtonStatus | Get the current proton state and its components. |
| getState | Get the current proton state. |
| triggerFlush | Trigger [flush](../../../content/proton.html#proton-maintenance-jobs) as soon as possible for all document types. |
| prepareRestart | Estimates the cost of [transaction log](../../../content/proton.html#transaction-log) replay, and flushes data structures if that will speed up a subsequent start. If this is not called before stopping proton, there is no estimation and no flush. |

## vespa-remove-index

_vespa-remove-index_ is a command-line tool to remove index data on a Vespa search node, by wiping out selected files and subdirectories found in _$VESPA\_HOME/var/db/vespa/_. This process is irreversible, and the indexes deleted can not be recovered.

Stop _services_ before running it - example:

```
$ vespa-stop-services && vespa-remove-index -force && vespa-start-services
```

Synopsis:`vespa-remove-index [-force] [-cluster name]`

Example:

```
$ vespa-remove-index
[info] For cluster music distribution key 0 you have:
[info] 156 kilobytes of data in var/db/vespa/search/cluster.music/n0
Really to remove this vespa index? Type "yes" if you are sure ==> yes
[info] removing data: rm -rf var/db/vespa/search/cluster.music/n0
[info] removed.
```

| Option | Description |
| --- | --- |
| -force | Do not require verification from the user before really removing index data |
| -cluster _name_ | Only remove data for the given cluster name |

## vespa-route

_vespa-route_ is a tool to inspect Vespa routing configurations. If file is set, it will be parsed as a feed and the output will look similar to when using [/document/v1/](../../api/document-v1.html)with trace enabled.

Synopsis: `vespa-route [options] [file]`

Example:

```
$ vespa-route
There are 5 route(s):
    1. default
    2. music
    3. music-direct
    4. music-index
    5. storage/cluster.music

There are 2 hop(s):
    1. docproc/cluster.music.indexing/chain.indexing
    2. indexing
```

| Option | Description |
| --- | --- |
| --documentmanagerconfigid \<id\> | Sets the config id that supplies document configuration |
| --dump | Prints the complete content of the routing table |
| --help | Prints this help |
| --hop \<name\> | Prints detailed information about hop \<name\> |
| --hops | Prints a list of all available hops |
| --identity \<id\> | Sets the identity of message bus |
| --listenport \<num\> | Sets the port message bus will listen to |
| --oosserverpattern \<id\> | Sets the out-of-service server pattern for message bus |
| --protocol \<name\> | Sets the name of the protocol whose routing to inspect |
| --route \<name\> | Prints detailed information about route \<name\> |
| --routes | Prints a list of all available routes |
| --routingconfigid \<id\> | Sets the config id that supplies the routing tables |
| --services | Prints a list of all available services |
| --slobrokconfigid \<id\> | Sets the config id that supplies the slobrok server list |
| --trace \<num\> | Sets the trace level to use when visualizing the route |
| --verify | All hops and routes are verified when routing |

## vespa-sentinel-cmd

Use _vespa-sentinel-cmd_ to list, start and stop services - refer to [config sentinel](../../../operations/self-managed/config-sentinel.html) for examples. It can also check for connectivity between nodes.

 **Important:** See [start / stop / restart](../../../operations/self-managed/admin-procedures.html#vespa-start-stop-restart)for how to stop all services on a node, optimizing for restart time - use this for tasks like software upgrade.

Synopsis: `vespa-sentinel-cmd [-h] list|start <service>|restart <service>|stop <service>|connectivity`

| Option | Description |
| --- | --- |
| -h | Help text |

| Command | Description |
| --- | --- |
| list | Lists the services running on this node and their status: 

| service name | |
| state | 
- RUNNING: Service is running
- FINISHED: Service has been stopped
- FAILED: Service has crashed and failed to restart
- TERMINATING: Service is stopping

 |
| mode | 
- MANUAL: Service has to be started and stopped manually
- AUTO: Service will restart automatically if it stops

 |
| pid | Pid of the process (main thread) |
| exitstatus | Exit code the last time the service stopped. |
| id | [Config ID](../../../applications/configapi-dev.html#config-id) of the service |

 |
| restart [name] | Restarts the service with the given name. The name is the first string in the service list given by `list` |
| stop [name] | Stops the service with the given name |
| start [name] | Starts the service with the given name |
| connectivity | Use to troubleshoot startup issues/network configuration/ACLs/iptables:
```
$ vespa-sentinel-cmd connectivity
vespa-sentinel-cmd 'connectivity' OK.
node0.vespanet -> ok
node1.vespanet -> ok
node2.vespanet -> ok
```
 |

## vespa-set-node-state

Set the [user state](../../api/cluster-v2.html#state-user) of a node. This will set the generated state to the user state if the user state is "better" than the generated state that would have been created if the user state were up. For instance, a node that is in `up` state can be forced into `down` state, while a node that is currently `down` can not be forced into `retired` state, but can be forced into maintenance state.

Synopsis: `vespa-set-node-state [options] up|down|maintenance|retired [description]`

Example:

```
$ vespa-set-node-state -i 0 maintenance "Set to maintenance for software upgrade"
```

| Option | Description |
| --- | --- |
| -h, --help | Show help |
| -v | More verbose output |
| -s | Less verbose output |
| --show-hidden | Also show hidden undocumented debug options |
| -n, --no-wait | Do not wait for node state changes to be visible in the cluster before returning |
| -c, --cluster | The cluster name of the cluster to query. If unspecified, and vespa is installed on the current node, information will be attempted auto-extracted |
| -f, --force | Force execution |
| -t, --type | Node type - can either be 'storage' or 'distributor'. If not specified, the operation will use state for both types |
| -i, --index | Node index. If not specified, all nodes found running on this host will be used |
| --config-server | Host name of the config server to query |
| --config-server-port | Port to connect to the config server on |
| --config-request-timeout | Timeout of config request |

## vespa-significance

Generates a [significance model file](../../../ranking/significance#significance-model-file) for global significance.

Synopsis: `vespa-significance <command> [options]`

Commands:

- `generate` – build a significance model from Vespa documents (JSONL) or Vespa Significance TSV (VSTSV) files.
- `export` – dump term statistics from an index to a VSTSV file.
- `merge` – merge multiple VSTSV files, optionally filtering low-frequency terms.

### vespa-significance generate

The command uses the same tokenizer as the default query processor, see [linguistics in Vespa](../../../linguistics/linguistics.html) for details. Custom tokenizers require a matching extractor. Tokens are lower-cased without stemming to align with query processing.

Synopsis: `vespa-significance generate [options] --in <FILE>`

Example:

```
$ vespa-significance generate --in vespa-dump.jsonl --out en_model.json --field text --language en
```

This example generates a significance model called `en_mode.json` from a collection of Vespa Documents (the jsonl file). This is available in Vespa as of version 8.426.8.

When running in Docker, mount the data directory to persist input and output files, e.g.:

```
$ podman run -it --entrypoint bash -v $PWD/data:/data -w /data vespaengine/vespa:latest /opt/vespa/bin/vespa-significance generate --in docs.jsonl --out model.zst --field text --language en
```

To dump documents for JSONL input, use [vespa-visit](#vespa-visit) with the `--field-set` option:

```
$ vespa visit --field-set mydocument:text_field > ./data/docs.jsonl
```

Inspect the resulting model file with `zstdcat` and `jq`:

```
$ zstdcat ./data/model.zst | jq
```

Example generating model from VSTSV:

```
$ vespa-significance generate --format vstsv --in dumped_term_df.vstsv --out un_model.json
```

In this example the input is generated with `vespa-significance export`. This is available in Vespa as of version 8.597.8. When language is not specified, the default is set to unknown when using VSTSV format.

| Option | Description |
| --- | --- |
| -h, --help | Show help for the subcommand. |
| -i, --in \<FILE\> | Input file. Default format is JSON Lines where each line is a [Vespa document in JSON](../../schemas/document-json-format.html). Use `--format vstsv` to read VSTSV files. |
| --format \<FORMAT\> | Input format. Format can be `jsonl` or `vstsv`. Defaults to `jsonl`. |
| -o, --out \<model.json[.zst]\> | Output [significance model](../../../ranking/significance#significance-model-file). |
| -f, --field \<field\> | JSONL: the name of the text field to analyse. VSTSV: No effect. |
| -l, --language \<tag[,tag...]\> | Comma-separated ISO language tags. The first tag controls tokenization; additional tags are stored in the model. Required for JSONL, optional for VSTSV (defaults to `un`). See supported tags in [linguistics in Vespa](../../../linguistics/linguistics-opennlp.html#default-languages). |
| -zst, --zst-compression \<ENABLED\> | Enable Zstandard compression of the output. Enabled can be `true` or `false`. Default `false`. When `true`, the output file must end with `.zst`. |

### vespa-significance export

Synopsis: `vespa-significance export [options] --field <FIELD>`

Example:

```
$ vespa-significance export --schema product --field title --out text.vstsv
```

Locates an index on the content node and exports term document frequencies from that index using `vespa-index-inspect`. The output VSTSV file can be passed to `generate --format vstsv` or merged with other exports. This is available in Vespa as of version 8.597.8.

This command must be executed on a content node.

| Option | Description |
| --- | --- |
| -h, --help | Show help for the subcommand. |
| --index-dir \<path/to/index\> | Explicit path to the index directory. If omitted, the tool locates the directory using cluster, schema, and node information. |
| --out \<FILE.vstsv[.zst]\> | Output VSTSV file. Defaults to `export_FIELD.vstsv`. Compression adds `.zst` automatically. |
| --field \<FIELD\> | Text field to export. Must correspond to a field directory within the selected index. This is the same as a field in the schema. |
| --cluster \<NAME\> | Specifies the content cluster name for locating the index directory. If multiple clusters exist per node, use --cluster to choose one. |
| --schema \<NAME\> | Specifies the schema (document type) name used when locating the index directory. |
| --node-index \<NUMBER\> | Specifies the content node index for locating the index directory. If there are multiple indexes on a node, use --node-index to choose one. |
| -zst, --zst-compression | Write the VSTSV output compressed with Zstandard. |

### vespa-significance merge

Synopsis: `vespa-significance merge [options] <input.vstsv[.zst]> [<input2.vstsv[.zst]> ...]`

Example:

```
$ vespa-significance merge --out merged_title.vstsv export_title_node1.vstsv export_title_node2.vstsv
```

Merges multiple VSTSV files and preserves the total document count in the header. Use this to combine exports before generating a model. This is available in Vespa as of version 8.597.8.

| Option | Description |
| --- | --- |
| -h, --help | Show help for the subcommand. |
| --out \<FILE.vstsv[.zst]\> | Output VSTSV file. Defaults to `merged.vstsv`. Compression adds `.zst`. |
| --min-keep \<NUMBER\> | Filter out terms with document frequency strictly lower than `NUMBER`. |
| -zst, --zst-compression | Write the merged VSTSV output compressed with Zstandard. |

## vespa-start-configserver

Start a config server on a node, [details](../../../operations/self-managed/admin-procedures.html#vespa-start-stop-restart). See [vespa-start-services](#vespa-start-services) for node setup steps, before startup.

Synopsis: `vespa-start-configserver`

## vespa-start-services

Start all services on a node, [details](../../../operations/self-managed/admin-procedures.html#vespa-start-stop-restart).

As part of starting Vespa, the startup script calls [rhel-prestart.sh](https://github.com/vespa-engine/vespa/blob/master/vespabase/src/rhel-prestart.sh) to set up directories and system limits - this requires privileges to do so - run this command with sudo, see [example](../../../operations/self-managed/multinode-systems.html#config-server-cluster-setup). Refer to [vespa-start-services.sh](https://github.com/vespa-engine/vespa/blob/master/vespabase/src/vespa-start-services.sh) and [environment variables](../../../operations/self-managed/files-processes-and-ports.html#environment-variables).

Synopsis: `vespa-start-services`

When debugging a failed start, use [vespa-logfmt](#vespa-logfmt) to inspect the log. It is also useful to read up on the [start sequence](../../../operations/self-managed/configuration-server.html#start-sequence) and make sure the config server is running - Vespa will not start with a running config server.

Vespa has a _Safe Cluster Startup_ mode to only start vespa services after X% of nodes are running - see [cluster startup](../../../operations/self-managed/config-sentinel.html#cluster-startup).

## vespa-stat

_vespa-stat_ is a tool to fetch statistics about a specific user, group, bucket, gid or document.

vespa-stat works in two stages. The first stage is to figure out the actual buckets we want to look at. In the second stage, it can dump the located buckets. For each command line option, only the relevant documents will be dumped (the document for `--document/--gid`, or the user/group's documents for `--user/--group`). This stage can be turned on by adding `--dump`, but is default on for the case of `--document/--gid`.

Synopsis: `vespa-stat [options]`

Example:

```
$ vespa-stat --document id:my_namespace:my_search::12345678-4fb7-3797-ae9a-d4d7a4e6e085
Bucket maps to the following actual files:
	BucketInfo(BucketId(0x4000000000004800): [distributor:17] [node(idx=17,crc=0xe5ce35c7,docs=57/57,bytes=478040/478040,trusted=true,active=true,ready=true), node(idx=15,crc=0xe5ce35c7,docs=57/57,bytes=478040/478040,trusted=true,active=true,ready=true)])

Details for BucketId(0x4000000000004800):
	Bucket information from node 15:
Persistence bucket BucketId(0x4000000000004800), partition 0
  Timestamp: 1452598747000000, Doc(id:my_namespace:my_search::12345678-4fb7-3797-ae9a-d4d7a4e6e085), gid(0x0048e840a48002b12abbb0a0), size: 101

	Bucket information from node 17:
Persistence bucket BucketId(0x4000000000004800), partition 0
  Timestamp: 1452598747000000, Doc(id:my_namespace:my_search::12345678-4fb7-3797-ae9a-d4d7a4e6e085), gid(0x0048e840a48002b12abbb0a0), size: 101
```

| Option | Description |
| --- | --- |
| -b, --bucket \<bucketid\> | Dump list of buckets that are contained in the given bucket, or that contain it |
| -d, --dump | Dump list of documents for all buckets matching the selection command. |
| -g, --group \<groupid\> | Dump list of buckets that can contain the given group |
| -h, --help | Help text |
| -l, --gid \<globalid\> | Dump information about one specific document, as given by the GID (implies --dump) |
| -o, --document \<docid\> | Dump information about one specific document (implies --dump) |
| -r, --route \<route\> | Route to send the messages to, usually the name of the storage cluster |
| -s, --bucketspace \<space\> | [Bucket space](../../../content/buckets.html#bucket-space) (_default_ or _global_). If not specified, _default_ is used |
| -u, --user \<userid\> | Dump list of buckets that can contain the given user |

## vespa-status-filedistribution

Use _vespa-status-filedistribution_ to get status from file distribution. Should be run on a config server, it connects to config server on localhost to get status.

Synopsis: `vespa-status-filedistribution [--application <applicationNameArg>]
  [--debug] [--environment <environmentArg>] [(-h | --help)]
  [--instance <instanceNameArg>] [--region <regionArg>]
  [--tenant <tenantNameArg>] [--timeout <timeoutArg>]`

| Option | Description |
| --- | --- |
| --application \<applicationName\> | Application name |
| --debug | Print debug log |
| --environment \<environment\> | Environment name |
| -h, --help | Display help information |
| --instance \<instanceName\> | Instance name |
| --region \<regionName\> | Region name |
| --tenant \<tenantName\> | Tenant name |
| --timeout \<timeout\> | timeout (in seconds) |

## vespa-stop-configserver

Stop a config server on a node, [details](../../../operations/self-managed/admin-procedures.html#vespa-start-stop-restart).

Synopsis: `vespa-stop-configserver`

## vespa-stop-services

Stop all services on a node, [details](../../../operations/self-managed/admin-procedures.html#vespa-start-stop-restart). Running _vespa-stop-services_ on a content node will call [prepareRestart](#vespa-proton-cmd) to optimize restart time.

Synopsis: `vespa-stop-services`

## vespa-summary-benchmark

Tool for testing and benchmarking RPC docsum interface. Refer to[VespaSummaryBenchmark.java](https://github.com/vespa-engine/vespa/blob/master/vespaclient-java/src/main/java/com/yahoo/vespasummarybenchmark/VespaSummaryBenchmark.java)

## vespa-visit

Used to run a [visit](../../../writing/visiting.html) operation, with more options than [vespa visit](../../../clients/vespa-cli.html). It uses the [Vespa Message Bus](../../../writing/document-routing.html) and must be run inside a Vespa application - it does not use the Vespa HTTP APIs.

 **Note:** This tool is easily confused with `vespa visit`in the [vespa CLI](../../../clients/vespa-cli.html). The latter is the common tool for visiting, `vespa-visit` is built for debugging and complex use cases.

By default, vespa-visit gets visited documents and emits them to stdout. However, the tool may specify a [vespa-visit-target](#vespa-visit-target) and be used as a tool to run reprocessing or migration. It supports keeping a progress file on disk, such that you can restart it if it should fail in the middle for some reason.

To migrate a set of documents from one cluster to another, use _visiting_ - as the data is transferred directly, using a compact serialization format, from the source nodes to the targets, this is performance optimal (data is not piped through the visit client). Implement backup this way, or dump to file.

Search node recovery: Feed the documents directly to a search cluster. Example, selecting documents of type _music_:

```
$ vespa-visit --selection music --datahandler indexing
```

This feeds from the source into the search cluster in the same application. Note that simultaneous feed can make updates go lost.

Include [remove-entries](../../../operations/self-managed/admin-procedures.html#data-retention-vs-size) in the visit operation using _--visitremove_ - this dumps the tombstones of documents recently removed.

The [content policy](../../../writing/document-routing.html#content) can be configured to use a set of configuration servers from another cluster to configure itself. This is specified with the _config_ parameter. As an example, the following route routes to the content cluster _mycluster_ with a configuration server on _myconfigserver.mydomain.com:12345_:

```
[Content:config=tcp/myconfigserver.mydomain.com:12345;cluster=mycluster]
```

The following examples illustrate how to copy all data from a source cluster to another cluster using vespa-visit:

```
# Copies all data in the local cluster, routing it to the remote_mycluster_$ vespa-visit --datahandler '[Content:config=tcp/myconfigserver.mydomain.com:12345;cluster=mycluster]'

# Limit to 'music' documents only
$ vespa-visit --datahandler '[Content:config=tcp/myconfigserver.mydomain.com:19070;cluster=mycluster]' \
  --selection music

# Limit to all documents for user '1234'
$ vespa-visit --datahandler '[Content:config=tcp/myconfigserver.mydomain.com:12345;cluster=mycluster]' \
  --selection id.user=1234
```

Visitor processor types:

| Processor Type | Description |
| --- | --- |
| Dump visitor | The most commonly used visitor processor type is the dump visitor. All it does is to send the read documents on to some external target specified by the visitor. Using the command line tool _vespa-visit_, the default is to just send the documents back to the client, and have them printed to stdout. The dump visitor is used to implement reprocessing. Typically, using a messagebus route, which will send the documents through the document processing cluster and then back to the content cluster. Migration of documents from one cluster to another is also implemented using a dump visitor. |
| Streaming search visitor | The [streaming search](../../../performance/streaming-search.html) visitor runs in the Vespa container, making it transparent whether search results were created from streaming or indexed search - see [indexing mode](../../applications/services/content.html#document). |

Requests sent from the visitor processor are sent to a visitor target - types:

| Target Type | Description |
| --- | --- |
| Message bus routes | You can specify a [message bus route](../../../writing/document-routing.html) name directly, and this route will be used to send the results. This is typically used when doing reprocessing or migration. Message bus routes are set up in the application package. In addition, some routes may have been auto-generated in simple setups, for instance, a route called _default_ is generated if your setup is simple enough for the config model to likely guess where you want to send your data. |
| Slobrok address | 

You can also specify a slobrok address for data to be sent to. A slobrok address is a slash-separated path where you can use an asterisk to mean any element within this path. For instance, if you have a docproc cluster called _mydpcluster_, it will have registered its nodes with slobrok names like _docproc/cluster.mydpcluster/docproc/0/feed\_processor_, where the 0 here indicates the first node in the cluster. You can thus specify to send visit data to this docproc cluster by stating a slobrok address of _docproc/cluster.mydpcluster/docproc/\*/feed\_processor_. Note that this will not send all the data to one or all the nodes. The data sent from the visitor will be distributed among the matching nodes, but each message will just be sent to one node.

Slobrok names can be used when using [vespa-visit-target](#vespa-visit-target) to retrieve the data from some location. If you start vespa-visit-target on two nodes, listening to slobrok names _mynode/0/visit-destination_ and _mynode/1/visit-destination_, you can send the results to these nodes by specifying _mynode/\*/visit-destination_ as the data handler.

[vespa-destination](#vespa-destination) is similar to vespa-visit-target in that it can receive messages from messagebus and print the contents to stdout. It can be useful in situations where you want to debug a route or a docproc, by using the vespadestination as the endpoint of your route.

 |
| TCP socket | TCP sockets can also be specified directly. This requires that the endpoint speaks FNET RPC. This is typically done, either by using the _vespa-visit-target_ tool, or by using a visitor destination programmatically by using a utility class in the document API. A socket address looks like the following: tcp/_hostname_:_port_/_servicename_. For instance, an address generated by _vespa-visit-target_ might look like: _tcp/myhost.mydomain.com:12345/visit-destination_ |

Also see [vespa-destination](#vespa-destination).

Synopsis: `vespa-visit [options]`

| Option | Description |
| --- | --- |
| --abortonclusterdown | Abort if cluster is down |
| -b, --maxbuckets \<num\> | Maximum buckets per visitor |
| --bucketspace \<space\> | [Bucket space](../../../content/buckets.html#bucket-space) to visit (_default_ or _global_). If not specified, _default_ is used |
| -c, --cluster \<cluster\> | Visit the given cluster |
| -d, --datahandler \<target\> | Send results to the given target - see [vespa-visit-target](#vespa-visit-target) |
| -f, --from \<timestamp\> | Only visit from the given timestamp (microseconds) |
| -h, --help | Show help text |
| -i, --printids | Display only document identifiers |
| --jsonoutput | Output a JSON array of document objects. This is the default output format. |
| --jsonl | Output documents as JSONL (JSON Lines format). Each individual document is output as a single line, with a newline separating each document. Lines are not comma-separated, and there is no top-level array wrapping the document objects. |
| -l, --fieldset \<fieldset\> | Retrieve the specified fields only (see [Document field sets](../../../schemas/documents.html#fieldsets)). Default: `[document]` |
| --libraryparam \<key\> \<val\> | Send parameter to the visitor library |
| -m, --maxpending \<num\> | Maximum pending messages to data handlers per storage visitor |
| --maxpendingsuperbuckets \<num\> | Maximum pending visitor messages from the vespa-visit client. If set, dynamic throttling of visitors is disabled |
| --maxtotalhits \<num\> | Abort visiting when received this many total documents. This is only an approximate number, all pending work will be completed, and those documents will also be returned |
| -o, --timeout \<milliseconds\> | Time out visitor after given time |
| -p, --progress \<file\> | Use the given file to track progress. `-p progress-file` saves progress, allowing the visitor to resume at next startup. Always remove the progress file to run the visiting operation from the start. |
| --processtime \<num\> | Sleep for this number of milliseconds before processing the message. (Debug option for pretending to be a slow client) |
| -r, --visitremoves | Return tombstone entries of documents that have been removed. Tombstones will be output as `remove` objects, which only contain a document ID. When using `--visitremoves`, regular (non-tombstone) documents will also be returned. |
| -s, --selection \<selection\> | 

[Selection](../../writing/document-selector-language.html) string for which documents to visit. E.g., `-s 'id.hash().abs() % 100 == 0'` dumps 1% of the corpus - see [selection](../../../writing/visiting.html#selection). Note that this expression is evaluated for _every_ document in the cluster, so running 100 visits comparing against all values in [0, 99) end up reading all documents 100 times. Prefer using `--slices` and `--sliceid` instead if available.

 |
| --shorttensors | Output using [tensor short form](../../schemas/document-json-format.html#tensor) |
| --skipbucketsonfatalerrors | Skip visiting super buckets with fatal error codes |
| --sliceid \<arg\> | The slice number of the visit represented by this visitor. This number must be non-negative and less than the number of slices specified for the visit. |
| --slices \<arg\> | 

Split the document corpus into this number of independent slices. This lets multiple, concurrent series of visitors advance the same logical visit independently, by specifying a different `sliceid` for each.

E.g. `--slices 100 --sliceid 0` dumps 1% of the corpus by efficiently iterating over only 1/100th of the data space. For a given number of `--slices`, it's possible to visit the entire corpus (possibly in parallel) with non-overlapping output by visiting with all `--sliceid` values from (and including) 0 up to (and excluding) `--slices`.

 |
| -t, --to \<timestamp\> | Only visit up to the given timestamp (microseconds) |
| --tracelevel \<level\> | Tracelevel ([0-9]), for debugging |
| -u, --buckettimeout \<milliseconds\> | Fail visitor if visiting a single bucket takes longer than this (default same as timeout) |
| -v, --verbose | Show progress and info on STDERR |
| --visitinconsistentbuckets | 

Don't wait for inconsistent buckets to become consistent. See [read-consistency](../../../content/consistency#read-consistency) for details.

 |
| --visitlibrary \<string\> | Use the given visitor library |

## vespa-visit-target

[vespa-visit-target](#vespa-visit-target) is a tool to set up an endpoint for [visiting](../../../writing/visiting.html) data. It binds to a socket or a slobrok address, which is specified as a target in the visit client. Also see [vespa-destination](#vespa-destination).

Synopsis: `vespa-visit-target [options]`

| Option | Description |
| --- | --- |
| -c, --visithandler \<classname\> | Use the given class as a visit handler (defaults to StdOutVisitorHandler) |
| -h, --help | Show help page |
| -i, --printids | Display document IDs only |
| -o, --visitoptions \<args\> | Option arguments to pass through to the visitor handler instance |
| -p, --processtime \<msecs\> | Sleep msecs milliseconds before processing the message. (Debug option for pretending to be a slow client) |
| -s, --bindtoslobrok \<address\> | Bind to slobrok address. One, and only one, of the binding options must be set |
| -t, --bindtosocket \<port\> | Bind to TCP port. One, and only one, of the binding options must be set |
| -v, --verbose | Indent output, show progress and info on STDERR |

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [vespa-configproxy-cmd](#vespa-configproxy-cmd)
- [vespa-configserver-remove-state](#vespa-configserver-remove-state)
- [vespa-config-status](#vespa-config-status)
- [vespa-deploy](#vespa-deploy)
- [vespa-destination](#vespa-destination)
- [vespa-fbench-filter-file](#vespa-fbench-filter-file)
- [vespa-fbench-geturl](#vespa-fbench-geturl)
- [vespa-fbench-split-file](#vespa-fbench-split-file)
- [vespa-feeder](#vespa-feeder)
- [vespa-get](#vespa-get)
- [vespa-get-cluster-state](#vespa-get-cluster-state)
- [vespa-get-config](#vespa-get-config)
- [vespa-get-node-state](#vespa-get-node-state)
- [vespa-index-inspect](#vespa-index-inspect)
- [vespa-attribute-inspect](#vespa-attribute-inspect)
- [vespa-jvm-dumper](#vespa-jvm-dumper)
- [vespa-logctl](#vespa-logctl)
- [vespa-logfmt](#vespa-logfmt)
- [vespa-model-inspect](#vespa-model-inspect)
- [vespa-print-default](#vespa-print-default)
- [vespa-proton-cmd](#vespa-proton-cmd)
- [vespa-remove-index](#vespa-remove-index)
- [vespa-route](#vespa-route)
- [vespa-sentinel-cmd](#vespa-sentinel-cmd)
- [vespa-set-node-state](#vespa-set-node-state)
- [vespa-significance](#vespa-significance)
- [vespa-significance generate](#vespa-significance-generate)
- [vespa-significance export](#vespa-significance-export)
- [vespa-significance merge](#vespa-significance-merge)
- [vespa-start-configserver](#vespa-start-configserver)
- [vespa-start-services](#vespa-start-services)
- [vespa-stat](#vespa-stat)
- [vespa-status-filedistribution](#vespa-status-filedistribution)
- [vespa-stop-configserver](#vespa-stop-configserver)
- [vespa-stop-services](#vespa-stop-services)
- [vespa-summary-benchmark](#vespa-summary-benchmark)
- [vespa-visit](#vespa-visit)
- [vespa-visit-target](#vespa-visit-target)

