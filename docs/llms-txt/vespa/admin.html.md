# Source: https://docs.vespa.ai/en/reference/applications/services/admin.html.md

# services.xml - 'admin'

 

Reference documentation for `<admin>` in [services.xml](services.html). Find a working example of this configuration in the sample application _multinode-HA_[services.xml](https://github.com/vespa-engine/sample-apps/blob/master/examples/operations/multinode-HA/services.xml).

```
admin [version][adminserver [hostalias]](#adminserver)[cluster-controllers](#cluster-controllers)[cluster-controller [hostalias, baseport, jvm-options, jvm-gc-options]](#cluster-controller)[configservers](#configservers)[configserver [hostalias, baseport]](#configserver)[logserver [jvm-options, jvm-gc-options]](#logserver)[slobroks](#slobroks)[slobrok [hostalias, baseport]](#slobrok)[monitoring [systemname]](#monitoring)[metrics](#metrics)[consumer [id]](#consumer)[metric-set [id]](#metric-set)[metric [id]](#metric)[cloudwatch [region, namespace]](#cloudwatch)[shared-credentials [file, profile]](#shared-credentials)[logging](#logging)
```

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| version | required | number | | 

2.0

 |

## adminserver

The configured node will be the default administration node in your Vespa system, which means that unless configured otherwise all administrative services - i.e. the log server, the configuration server, the slobrok, and so on - will run on this node. Use [configservers](#configservers), [logserver](#logserver),[slobroks](#slobroks) elements if you need to specify baseport or jvm options for any of these services.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| hostalias | required | string | | 

 |
| baseport | optional | number | | 

 |

## cluster-controllers

Container for one or more [cluster-controller](#cluster-controller) elements. When having one or more [content](content.html) clusters, configuring at least one cluster controller is required.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| standalone-zookeeper | optional | true/false | false | 

Will by default share the ZooKeeper instance with configserver. If configured to true a separate ZooKeeper instance will be configured and started on the set of nodes where you run cluster controller on. The set of cluster controllers nodes cannot overlap with the set of nodes where config server is running. If this setting is changed from false to true in a running system, all previous cluster state information will be lost as the underlying ZooKeeper changes. Cluster controllers will re-discover the state, but nodes that have been manually set as down will again be considered to be up.

 |

## cluster-controller

Specifies a host on which to run the [Cluster Controller](../../../content/content-nodes.html#cluster-controller) service. The Cluster Controller manages the state of the cluster in order to provide elasticity and failure detection.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| hostalias | required | string | | 

 |
| baseport | optional | number | | 

 |
| jvm-options | optional | string | | 

 |

## configservers

Container for one or more `configserver` elements.

## configserver

Specifies a host on which to run the [Configuration Server](/en/operations/self-managed/configuration-server.html) service. If contained directly below `<admin>` you may only have one, so if you need to configure multiple instances of this service, contain them within the [`<configservers>`](#configservers) element.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| hostalias | required | string | | 

 |
| baseport | optional | number | | 

 |

## logserver

Specifies a host on which to run the [Vespa Log Server](../../operations/log-files.html#log-server) service. If not specified, the logserver is placed on the [adminserver](#adminserver), like in the [example](https://github.com/vespa-engine/sample-apps/blob/master/examples/operations/multinode-HA/services.xml).

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| hostalias | required | string | | 

 |
| baseport | optional | number | | 

 |
| jvm-options | optional | string | | 

 |
| jvm-gc-options | optional | string | | 

 |

Example:

```
```
<logserver hostalias="node1" />
```
```

## slobroks

This is a container for one or more `slobrok` elements.

## slobrok

Specifies a host on which to run the [Service Location Broker (slobrok)](/en/operations/self-managed/slobrok.html) service.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| hostalias | required | string | | 

 |
| baseport | optional | number | | 

 |

## monitoring

Settings for how to pass metrics to a monitoring service - see [monitoring](/en/operations/self-managed/monitoring.html).

```
```
<monitoring systemname="name-in-metrics-system" />
```
```

| systemname | The name of the application in question in the monitoring system, default is "vespa" |

## logging

Used for tuning log levels of Java plug-ins. If you (temporarily) need to enable debug logging from some class or package, or if some third-party component is spamming your log with unnecessary INFO level messages, you can turn levels on or off. Example:

```
```
<logging>
    <class name="org.myorg.MyHelperClass" levels="+debug" />
    <class name="org.thirdparty.TooSpammyClass" levels="-info" />
    <package name="org.myorg.tricky.package" levels="all" />
    <package name="org.anotherorg" levels="all -info -debug -spam" />
</logging>
```
```

Note that tuning also affects sub-packages, so the above would also affect all packages with `org.anotherorg.` as prefix. And if there is a `org.myorg.tricky.package.foo.InternalClass` you will get even "spam" level logging from it!

The default for `levels` is `"all -debug -spam"` and as seen above you can add and remove specific levels.

## metrics

Used for configuring the forwarding of metrics to graphing applications - add `consumer` child elements. Also see [monitoring](/en/operations/self-managed/monitoring.html). Example:

```
```
<metrics>
    <consumer id="my-metric-namespace">
        <metric-set id="default" />
        <metric id="my-custom-metric" />
        <cloudwatch region="us-east-1" namespace="my-vespa">
            <shared-credentials file="/path/to/credentials-file" profile="default" />
        </cloudwatch>
    </consumer>
</metrics>
```
```

## consumer

Configure a metrics consumer. The metrics contained in this element will be exported to the consumer with the given id. `consumer` is a request parameter in [/metrics/v1/values](../../api/metrics-v1.html), [/metrics/v2/values](../../api/metrics-v2.html) and [/prometheus/v1/values](../../api/prometheus-v1.html).

Add `metric` and/or `metric-set` children.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | string | | 

The name of the consumer to export metrics to.

 |

## metric-set

Include a pre-defined set of metrics to the consumer.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | string | | 

The id of the metric set to include. Built-in metric sets are:

- `default`
- `Vespa`

 |

## metric

Configure a metric.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| id | required | string | | 

The name of the metric as defined in custom code or in [process metrics api](../../api/state-v1.html#state-v1-metrics)

 |

Note that metric id needs to include the metric specific suffix, e.g. _.average_.

In this example, there is one metric added to a custom consumer in addition to the default metric set. Use _&consumer=my-custom-consumer_ parameter for the prometheus endpoint. Also notice the .count suffix, see [process metrics api](../../api/state-v1.html#state-v1-metrics).

The per process metrics api endpoint _/state/v1/metrics_ also includes a description of each emitted metric. The _/state/v1/metrics_ endpoint also includes the metric aggregates (.count, .average, .rate, .max).

```
```
<metrics>
    <consumer id="my-custom-consumer">
        <metric-set id="default" />
        <metric id="vds.idealstate.garbage_collection.documents_removed.count" />
    </consumer>
</metrics>
```
```

## cloudwatch

Specifies that the metrics from this consumer should be forwarded to CloudWatch.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| region | required | string | | 

Your AWS region

 |
| namespace | required | string | | 

The metrics namespace in CloudWatch

 |

Example:

```
```
<cloudwatch region="us-east-1" namespace="my-vespa">
    <shared-credentials file="/path/to/credentials-file" profile="default" />
</cloudwatch>
```
```

## shared-credentials

Specifies that a profile from a shared-credentials file should be used for authentication to CloudWatch.

| Attribute | Required | Value | Default | Description |
| --- | --- | --- | --- | --- |
| file | required | string | | 

The path to the shared-credentials file

 |
| profile | optional | string | default | 

The profile in the shared-credentials file

 |

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [adminserver](#adminserver)
- [cluster-controllers](#cluster-controllers)
- [cluster-controller](#cluster-controller)
- [configservers](#configservers)
- [configserver](#configserver)
- [logserver](#logserver)
- [slobroks](#slobroks)
- [slobrok](#slobrok)
- [monitoring](#monitoring)
- [logging](#logging)
- [metrics](#metrics)
- [consumer](#consumer)
- [metric-set](#metric-set)
- [metric](#metric)
- [cloudwatch](#cloudwatch)
- [shared-credentials](#shared-credentials)

