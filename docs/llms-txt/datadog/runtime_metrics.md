# Source: https://docs.datadoghq.com/tracing/metrics/runtime_metrics.md

---
title: Runtime Metrics
description: >-
  Gain additional insights into an application's performance with the runtime
  metrics associated with your traces.
breadcrumbs: Docs > APM > APM Metrics > Runtime Metrics
---

# Runtime Metrics

## Overview{% #overview %}

Runtime metrics monitor your application's memory usage, garbage collection, and parallelization. Datadog tracing libraries automatically collect these metrics for supported environments and send them to the Datadog Agent.

These metrics help you identify bottlenecks, troubleshoot performance issues, and optimize resource utilization. By viewing runtime metrics alongside traces and logs, you gain comprehensive visibility into your application's health and performance.

## Compatibility{% #compatibility %}

Runtime metrics are available for several programming languages and runtimes, with varying levels of support and configuration options.

{% tab title="Java" %}

- **Enabled By Default**: Yes
- **Library Version**: 0.29.0+
- **Runtimes**: Java 8+

{% alert level="danger" %}
JMX metrics collection is not supported in AWS Lambda environments.
{% /alert %}

{% /tab %}

{% tab title="Python" %}

- **Enabled By Default**: No
- **Library Version**: 0.30.0+
- **Support Level**: Preview
- **Runtimes**: All supported Python versions

{% /tab %}

{% tab title="Ruby" %}

- **Enabled By Default**: No
- **Library Version**: 0.44.0+
- **Runtimes**: All supported Ruby versions

{% alert level="info" %}
You must add the [dogstatsd-ruby](https://rubygems.org/gems/dogstatsd-ruby) gem to your application.
{% /alert %}

{% /tab %}

{% tab title="Go" %}

- **Enabled By Default**: No
- **Library Version**: 1.18.0+
- **Runtimes**: All supported Go versions

{% /tab %}

{% tab title="Node.js" %}

- **Enabled By Default**: No
- **Library Version**: 3.0.0+
- **Runtimes**: All supported Node.js versions

{% /tab %}

{% tab title=".NET" %}

- **Enabled By Default**: No
- **Library Version**: 1.23.0+
- **Runtimes**: .NET Framework 4.6.1+ and .NET Core 3.1+ (including .NET 5 and newer).

#### Permissions for Internet Information Services (IIS){% #permissions-for-internet-information-services-iis %}

On .NET Framework, metrics are collected using performance counters. Users in non-interactive logon sessions (that includes IIS application pool accounts and some service accounts) must be added to the **Performance Monitoring Users** group to access counter data.

IIS application pools use special accounts that do not appear in the list of users. To add them to the Performance Monitoring Users group, look for `IIS APPPOOL\<name of the pool>`. For instance, the user for the DefaultAppPool would be `IIS APPPOOL\DefaultAppPool`.

This can be done either from the "Computer Management" UI, or from an administrator command prompt:

```shell
net localgroup "Performance Monitor Users" "IIS APPPOOL\DefaultAppPool" /add
```

{% /tab %}

{% tab title="PHP" %}

{% alert level="danger" %}
Runtime metrics for PHP is not supported.
{% /alert %}

{% /tab %}

{% tab title="C++" %}

{% alert level="danger" %}
Runtime metrics for C++ is not supported.
{% /alert %}

{% /tab %}

## Setup instructions{% #setup-instructions %}

To set up runtime metrics, you need to configure both the Datadog Agent and your application.

### 1. Configure the Datadog Agent

Enable [DogStatsD for the Agent](https://docs.datadoghq.com/developers/dogstatsd/#setup). By default, the Datadog Agent is configured to ingest metrics with UDP over port `8125`.

{% collapsible-section %}
#### Container-specific configuration

When running the Agent in containerized environments, additional configuration is required:

1. Set `dogstatsd_non_local_traffic: true` in your main [`datadog.yaml` configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#main-configuration-file), or set the [environment variable](https://docs.datadoghq.com/agent/docker/#dogstatsd-custom-metrics) `DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true`. **Note**: DogStatsD nonâlocal traffic is enabled by default, so you only need to set this if you've overridden it.
1. Follow these container-specific setup instructions:

- [Docker](https://docs.datadoghq.com/containers/docker/?tab=standard#dogstatsd-custom-metrics)
- [Kubernetes](https://docs.datadoghq.com/containers/kubernetes/configuration/?tab=datadogoperator#configure-dogstatsd)
- [Amazon ECS](https://docs.datadoghq.com/containers/amazon_ecs/#dogstatsd)
- [ECS Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/#metric-collection)

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.ddog-gov.com, ap1.datadoghq.com, ap2.datadoghq.com


Set `DD_SITE` in the Datadog Agent to  to ensure the Agent sends data to the correct Datadog location.

{% /callout %}

{% /collapsible-section %}

### 2. Configure your application

Configure runtime metrics in your application using environment variables. Some languages also support configuring runtime metrics directly in code.

#### Environment variables{% #environment-variables %}

Use the following environment variables to configure runtime metrics in your application:

{% dl %}

{% dt %}
`DD_RUNTIME_METRICS_ENABLED`
{% /dt %}

{% dd %}
**Default**: `true` for Java, `false` for all other languages**Description**: Enables the collection of runtime metrics. Metrics are sent to the Datadog agent, as configured for the instrumented application.
{% /dd %}

{% dt %}
`DD_RUNTIME_METRICS_RUNTIME_ID_ENABLED`
{% /dt %}

{% dd %}
**Default**: `true` for Java, `false` for Node.js, Ruby, and Python. Does not exist for .NET and Go; the `runtime_id` is always reported.**Description**: Enables enhanced runtime metrics, providing a `runtime_id` tag along with every metric. The `runtime_id` represents the application's process identifier and allows you to directly correlate runtime metrics with individual running applications.
{% /dd %}

{% dt %}
`DD_AGENT_HOST`
{% /dt %}

{% dd %}
**Default**: `localhost`**Description**: Sets the host address for the tracing library's metric submission. Can be a hostname or an IP address.
{% /dd %}

{% dt %}
`DD_DOGSTATSD_PORT`
{% /dt %}

{% dd %}
**Default**: `8125`**Description**: Sets the port for the tracing library's metric submission.
{% /dd %}

{% /dl %}

#### Code-based configuration{% #code-based-configuration %}

In addition to environment variables, some languages support configuring runtime metrics directly in code.

{% tab title="Java" %}
You can only enable runtime metrics with environment variables.

However, you can extend the metrics collected by adding custom JMX metrics. For more information, see [JMX Integration](https://docs.datadoghq.com/integrations/java/) documentation.
{% /tab %}

{% tab title="Python" %}
You can enable runtime metrics with environment variables or in code:

```python
from ddtrace.runtime import RuntimeMetrics
RuntimeMetrics.enable()
```

{% alert level="danger" %}
This only applies if you are not using `ddtrace-run`
{% /alert %}

{% /tab %}

{% tab title="Ruby" %}
You can enable runtime metrics with environment variables or in code:

```ruby
# config/initializers/datadog.rb
require 'datadog/statsd'
require 'datadog' # Use 'ddtrace' if you're using v1.x

Datadog.configure do |c|
  c.runtime_metrics.enabled = true

  # Optionally, you can configure the DogStatsD instance used for sending runtime metrics.
  # DogStatsD is automatically configured with default settings if `dogstatsd-ruby` is available.
  # You can configure with host and port of Datadog agent; defaults to 'localhost:8125'.
  c.runtime_metrics.statsd = Datadog::Statsd.new
end
```

{% /tab %}

{% tab title="Go" %}
You can enable runtime metrics with environment variables or in code:

```go
// Basic configuration
tracer.Start(tracer.WithRuntimeMetrics())

// With custom DogStatsD address
tracer.Start(
  tracer.WithRuntimeMetrics(),
  tracer.WithDogstatsdAddr("custom-host:8125")
)
```

The `WithDogstatsdAddr` option allows you to specify a custom address for the DogStatsD server. Use the [`WithDogstatsdAddr`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace/tracer#WithDogstatsdAddr) (or [`WithDogstatsdAddress` v1](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer#WithDogstatsdAddress)) option if your address differs from the default `localhost:8125`. (Available for 1.18.0+)
{% /tab %}

{% tab title="Node.js" %}
You can enable runtime metrics with environment variables or in code:

```js
const tracer = require('dd-trace').init({
  // Other tracer options...
  runtimeMetrics: true
})
```

{% /tab %}

{% tab title=".NET" %}
You can only enable runtime metrics with environment variables.
{% /tab %}

## Dashboards{% #dashboards %}

After setup is complete, you can view runtime metrics in:

- The instrumented service's details page
- The flame graph **Metrics** tab
- Default runtime dashboards

{% image
   source="https://datadog-docs.imgix.net/images/tracing/runtime_metrics/jvm_runtime_trace.f0c8b3752897a246aac6cff7b3d3dd4a.png?auto=format"
   alt="JVM Runtime Trace" /%}

## Troubleshooting{% #troubleshooting %}

- To associate runtime metrics within flame graphs, ensure the `env` tag (case-sensitive) is set and matching across your environment.
- For runtime metrics to appear on the service page when using Fargate, ensure that `DD_DOGSTATSD_TAGS` is set on your Agent task, and that the configured `env` tag matches the `env` of the instrumented service.

## Data collected{% #data-collected %}

Each supported language collects a set of runtime metrics that provide insights into memory usage, garbage collection, CPU utilization, and other performance indicators.

{% tab title="Java" %}

|  |
|  |
| **jvm.heap\_memory**(gauge)                 | The total Java heap memory used.*Shown as byte*                                                                                              |
| **jvm.heap\_memory\_committed**(gauge)      | The total Java heap memory committed to be used.*Shown as byte*                                                                              |
| **jvm.heap\_memory\_init**(gauge)           | The initial Java heap memory allocated.*Shown as byte*                                                                                       |
| **jvm.heap\_memory\_max**(gauge)            | The maximum Java heap memory available.*Shown as byte*                                                                                       |
| **jvm.loaded\_classes**(gauge)              | Number of classes currently loaded.                                                                                                          |
| **jvm.non\_heap\_memory**(gauge)            | The total Java non-heap memory used. Non-heap memory is calculated as follows: `Metaspace + CompressedClassSpace + CodeCache`*Shown as byte* |
| **jvm.non\_heap\_memory\_committed**(gauge) | The total Java non-heap memory committed to be used.*Shown as byte*                                                                          |
| **jvm.non\_heap\_memory\_init**(gauge)      | The initial Java non-heap memory allocated.*Shown as byte*                                                                                   |
| **jvm.non\_heap\_memory\_max**(gauge)       | The maximum Java non-heap memory available.*Shown as byte*                                                                                   |
| **jvm.thread\_count**(count)                | The number of live threads.*Shown as thread*                                                                                                 |
| **jvm.gc.cms.count**(count)                 | The total number of garbage collections that have occurred.                                                                                  |
| **jvm.gc.major\_collection\_count**(gauge)  | The rate of major garbage collections. Set `new_gc_metrics: true` to receive this metric.                                                    |
| **jvm.gc.minor\_collection\_count**(gauge)  | The rate of minor garbage collections. Set `new_gc_metrics: true` to receive this metric.                                                    |
| **jvm.gc.parnew.time**(gauge)               | The approximate accumulated garbage collection time elapsed.*Shown as millisecond*                                                           |
| **jvm.gc.major\_collection\_time**(gauge)   | The fraction of time spent in major garbage collection. Set `new_gc_metrics: true` to receive this metric.*Shown as permille*                |
| **jvm.gc.minor\_collection\_time**(gauge)   | The fraction of time spent in minor garbage collection. Set `new_gc_metrics: true` to receive this metric.*Shown as permille*                |

**Note**: Set `new_gc_metrics: true` in your [jmx.d/conf.yaml](https://github.com/DataDog/datadog-agent/blob/master/cmd/agent/dist/conf.d/jmx.d/conf.yaml.example) to replace the following metrics:

```text
jvm.gc.cms.count   => jvm.gc.minor_collection_count
                      jvm.gc.major_collection_count
jvm.gc.parnew.time => jvm.gc.minor_collection_time
                      jvm.gc.major_collection_time
```

{% /tab %}

{% tab title="Python" %}

|  |
|  |
| **runtime.python.cpu.time.sys**(gauge)                | Number of seconds executing in the kernel*Shown as second*      |
| **runtime.python.cpu.time.user**(gauge)               | Number of seconds executing outside the kernel*Shown as second* |
| **runtime.python.cpu.percent**(gauge)                 | CPU utilization percentage*Shown as percent*                    |
| **runtime.python.cpu.ctx\_switch.voluntary**(gauge)   | Number of voluntary context switches*Shown as invocation*       |
| **runtime.python.cpu.ctx\_switch.involuntary**(gauge) | Number of involuntary context switches*Shown as invocation*     |
| **runtime.python.gc.count.gen0**(gauge)               | Number of generation 0 objects*Shown as resource*               |
| **runtime.python.gc.count.gen1**(gauge)               | Number of generation 1 objects*Shown as resource*               |
| **runtime.python.gc.count.gen2**(gauge)               | Number of generation 2 objects*Shown as resource*               |
| **runtime.python.mem.rss**(gauge)                     | Resident set memory*Shown as byte*                              |
| **runtime.python.thread\_count**(gauge)               | Number of threads*Shown as thread*                              |

{% /tab %}

{% tab title="Ruby" %}

|  |
|  |
| **runtime.ruby.class\_count**(gauge)                                   | Total number of classes loaded*Shown as resource*                                                                            |
| **runtime.ruby.gc.remembered\_wb\_unprotected\_objects**(gauge)        | Number of write-barrier unprotected objects in the remembered set*Shown as resource*                                         |
| **runtime.ruby.gc.remembered\_wb\_unprotected\_objects\_limit**(gauge) | Limit on write-barrier unprotected objects allowed in the remembered set*Shown as resource*                                  |
| **runtime.ruby.gc.oldmalloc\_increase\_bytes**(gauge)                  | Total bytes allocated to old objects*Shown as byte*                                                                          |
| **runtime.ruby.gc.oldmalloc\_increase\_bytes\_limit**(gauge)           | Bytes limit that will trigger garbage collection of old objects*Shown as byte*                                               |
| **runtime.ruby.gc.malloc\_increase\_bytes**(gauge)                     | Total bytes allocated to objects*Shown as byte*                                                                              |
| **runtime.ruby.gc.malloc\_increase\_bytes\_limit**(gauge)              | Bytes limit that will trigger garbage collection of objects*Shown as byte*                                                   |
| **runtime.ruby.gc.total\_allocated\_objects**(gauge)                   | Total number of allocated objects over the lifetime of this process*Shown as resource*                                       |
| **runtime.ruby.gc.total\_freed\_objects**(gauge)                       | Total number of freed objects over the lifetime of this process*Shown as resource*                                           |
| **runtime.ruby.gc.total\_allocated\_pages**(gauge)                     | Total number of allocated pages over the lifetime of this process*Shown as page*                                             |
| **runtime.ruby.gc.total\_freed\_pages**(gauge)                         | Total number of freed pages over the lifetime of this process*Shown as page*                                                 |
| **runtime.ruby.gc.heap\_live\_slots**(gauge)                           | Number of live objects slots*Shown as resource*                                                                              |
| **runtime.ruby.gc.heap\_final\_slots**(gauge)                          | Number of object slots with finalizers attached to them*Shown as resource*                                                   |
| **runtime.ruby.gc.heap\_marked\_slots**(gauge)                         | Count of old objects which survived more than 3 GC cycles and number of write-barrier unprotected objects*Shown as resource* |
| **runtime.ruby.gc.heap\_available\_slots**(gauge)                      | Total number of slots in heap pages*Shown as resource*                                                                       |
| **runtime.ruby.gc.heap\_free\_slots**(gauge)                           | Number of free slots in heap pages*Shown as resource*                                                                        |
| **runtime.ruby.thread\_count**(gauge)                                  | Total number of threads*Shown as thread*                                                                                     |
| **runtime.ruby.gc.old\_objects**(gauge)                                | Total number of old objects*Shown as resource*                                                                               |
| **runtime.ruby.gc.old\_objects\_limit**(gauge)                         | Limit on number of old objects*Shown as resource*                                                                            |
| **runtime.ruby.global\_constant\_state**(gauge)                        | Global constant cache generation*Shown as event*                                                                             |
| **runtime.ruby.global\_method\_state**(gauge)                          | Global method cache generation*Shown as event*                                                                               |
| **runtime.ruby.constant\_cache\_invalidations**(gauge)                 | Constant cache invalidations*Shown as resource*                                                                              |
| **runtime.ruby.constant\_cache\_misses**(gauge)                        | Constant cache misses*Shown as resource*                                                                                     |

{% /tab %}

{% tab title="Go" %}

|  |
|  |
| **runtime.go.num\_cpu**(gauge)                       | CPUs detected by the runtime.*Shown as resource*                                                                                |
| **runtime.go.num\_goroutine**(gauge)                 | goroutines spawned.*Shown as invocation*                                                                                        |
| **runtime.go.num\_cgo\_call**(gauge)                 | CGO calls made.*Shown as invocation*                                                                                            |
| **runtime.go.mem\_stats.alloc**(gauge)               | Alloc is bytes of allocated heap objects.*Shown as byte*                                                                        |
| **runtime.go.mem\_stats.total\_alloc**(gauge)        | TotalAlloc is cumulative bytes allocated for heap objects.*Shown as byte*                                                       |
| **runtime.go.mem\_stats.sys**(gauge)                 | Sys is the total bytes of memory obtained from the OS.*Shown as byte*                                                           |
| **runtime.go.mem\_stats.lookups**(gauge)             | Lookups is the number of pointer lookups performed by the*Shown as unit*                                                        |
| **runtime.go.mem\_stats.mallocs**(gauge)             | Mallocs is the cumulative count of heap objects allocated.*Shown as unit*                                                       |
| **runtime.go.mem\_stats.frees**(gauge)               | Frees is the cumulative count of heap objects freed.*Shown as unit*                                                             |
| **runtime.go.mem\_stats.heap\_alloc**(gauge)         | HeapAlloc is bytes of allocated heap objects.*Shown as byte*                                                                    |
| **runtime.go.mem\_stats.heap\_sys**(gauge)           | HeapSys is bytes of heap memory obtained from the OS.*Shown as byte*                                                            |
| **runtime.go.mem\_stats.heap\_idle**(gauge)          | HeapIdle is bytes in idle (unused) spans.*Shown as byte*                                                                        |
| **runtime.go.mem\_stats.heap\_inuse**(gauge)         | HeapInuse is bytes in in-use spans.*Shown as byte*                                                                              |
| **runtime.go.mem\_stats.heap\_released**(gauge)      | HeapReleased is bytes of physical memory returned to the OS.*Shown as byte*                                                     |
| **runtime.go.mem\_stats.heap\_objects**(gauge)       | HeapObjects is the number of allocated heap objects.*Shown as unit*                                                             |
| **runtime.go.mem\_stats.stack\_inuse**(gauge)        | StackInuse is bytes in stack spans.*Shown as byte*                                                                              |
| **runtime.go.mem\_stats.stack\_sys**(gauge)          | StackSys is bytes of stack memory obtained from the OS.*Shown as byte*                                                          |
| **runtime.go.mem\_stats.m\_span\_inuse**(gauge)      | MSpanInuse is bytes of allocated mspan structures.*Shown as byte*                                                               |
| **runtime.go.mem\_stats.m\_span\_sys**(gauge)        | MSpanSys is bytes of memory obtained from the OS for mspan structures.*Shown as byte*                                           |
| **runtime.go.mem\_stats.m\_cache\_inuse**(gauge)     | MCacheInuse is bytes of allocated mcache structures.*Shown as byte*                                                             |
| **runtime.go.mem\_stats.m\_cache\_sys**(gauge)       | MCacheSys is bytes of memory obtained from the OS for*Shown as byte*                                                            |
| **runtime.go.mem\_stats.buck\_hash\_sys**(gauge)     | BuckHashSys is bytes of memory in profiling bucket hash tables.*Shown as byte*                                                  |
| **runtime.go.mem\_stats.gc\_sys**(gauge)             | GCSys is bytes of memory in garbage collection metadata.*Shown as byte*                                                         |
| **runtime.go.mem\_stats.other\_sys**(gauge)          | OtherSys is bytes of memory in miscellaneous off-heap*Shown as byte*                                                            |
| **runtime.go.mem\_stats.next\_gc**(gauge)            | NextGC is the target heap size of the next GC cycle.*Shown as byte*                                                             |
| **runtime.go.mem\_stats.last\_gc**(gauge)            | LastGC is the time the last garbage collection finished, as nanoseconds since 1970 (the UNIX epoch).*Shown as nanosecond*       |
| **runtime.go.mem\_stats.pause\_total\_ns**(gauge)    | PauseTotalNs is the cumulative nanoseconds in GC*Shown as nanosecond*                                                           |
| **runtime.go.mem\_stats.num\_gc**(gauge)             | NumGC is the number of completed GC cycles.*Shown as unit*                                                                      |
| **runtime.go.mem\_stats.num\_forced\_gc**(gauge)     | NumForcedGC is the number of GC cycles that were forced by the application calling the GC function.*Shown as unit*              |
| **runtime.go.mem\_stats.gc\_cpu\_fraction**(gauge)   | GCCPUFraction is the fraction of this program's available CPU time used by the GC since the program started.*Shown as fraction* |
| **runtime.go.gc\_stats.pause\_quantiles.min**(gauge) | Distribution of GC pause times: minimum values*Shown as nanosecond*                                                             |
| **runtime.go.gc\_stats.pause\_quantiles.25p**(gauge) | Distribution of GC pause times: 25th percentile*Shown as nanosecond*                                                            |
| **runtime.go.gc\_stats.pause\_quantiles.75p**(gauge) | Distribution of GC pause times: 50th percentile*Shown as nanosecond*                                                            |
| **runtime.go.gc\_stats.pause\_quantiles.95p**(gauge) | Distribution of GC pause times: 75th percentile*Shown as nanosecond*                                                            |
| **runtime.go.gc\_stats.pause\_quantiles.max**(gauge) | Distribution of GC pause times: maximum values*Shown as nanosecond*                                                             |

{% /tab %}

{% tab title="Node.js" %}

|  |
|  |
| **runtime.node.cpu.user**(gauge)                           | CPU usage in user code*Shown as percent*                                 |
| **runtime.node.cpu.system**(gauge)                         | CPU usage in system code*Shown as percent*                               |
| **runtime.node.cpu.total**(gauge)                          | Total CPU usage*Shown as percent*                                        |
| **runtime.node.mem.rss**(gauge)                            | Resident set size*Shown as byte*                                         |
| **runtime.node.mem.heap\_total**(gauge)                    | Total heap memory*Shown as byte*                                         |
| **runtime.node.mem.heap\_used**(gauge)                     | Heap memory usage*Shown as byte*                                         |
| **runtime.node.mem.external**(gauge)                       | External memory*Shown as byte*                                           |
| **runtime.node.heap.total\_heap\_size**(gauge)             | Total heap size*Shown as byte*                                           |
| **runtime.node.heap.total\_heap\_size\_executable**(gauge) | Total executable heap size*Shown as byte*                                |
| **runtime.node.heap.total\_physical\_size**(gauge)         | Total physical heap size*Shown as byte*                                  |
| **runtime.node.heap.used\_heap\_size**(gauge)              | Used heap size*Shown as byte*                                            |
| **runtime.node.heap.heap\_size\_limit**(gauge)             | Heap size limit*Shown as byte*                                           |
| **runtime.node.heap.malloced\_memory**(gauge)              | Malloced memory*Shown as byte*                                           |
| **runtime.node.heap.peak\_malloced\_memory**(gauge)        | Peak allocated memory*Shown as byte*                                     |
| **runtime.node.heap.size.by.space**(gauge)                 | Heap space size*Shown as byte*                                           |
| **runtime.node.heap.used\_size.by.space**(gauge)           | Heap space used size*Shown as byte*                                      |
| **runtime.node.heap.available\_size.by.space**(gauge)      | Heap space available size*Shown as byte*                                 |
| **runtime.node.heap.physical\_size.by.space**(gauge)       | Heap space physical size*Shown as byte*                                  |
| **runtime.node.process.uptime**(gauge)                     | Process uptime*Shown as second*                                          |
| **runtime.node.event\_loop.delay.max**(gauge)              | Maximum event loop delay*Shown as nanosecond*                            |
| **runtime.node.event\_loop.delay.min**(gauge)              | Minimum event loop delay*Shown as nanosecond*                            |
| **runtime.node.event\_loop.delay.avg**(gauge)              | Average event loop delay*Shown as nanosecond*                            |
| **runtime.node.event\_loop.delay.sum**(rate)               | Total event loop delay*Shown as nanosecond*                              |
| **runtime.node.event\_loop.delay.median**(gauge)           | Median event loop delay*Shown as nanosecond*                             |
| **runtime.node.event\_loop.delay.95percentile**(gauge)     | 95th percentile event loop delay*Shown as nanosecond*                    |
| **runtime.node.event\_loop.delay.count**(rate)             | Event loop iteration count where a delay is detected*Shown as execution* |
| **runtime.node.gc.pause.max**(gauge)                       | Maximum garbage collection pause*Shown as nanosecond*                    |
| **runtime.node.gc.pause.min**(gauge)                       | Minimum garbage collection pause*Shown as nanosecond*                    |
| **runtime.node.gc.pause.avg**(gauge)                       | Average garbage collection pause*Shown as nanosecond*                    |
| **runtime.node.gc.pause.sum**(rate)                        | Total garbage collection pause*Shown as nanosecond*                      |
| **runtime.node.gc.pause.median**(gauge)                    | Median garbage collection pause*Shown as nanosecond*                     |
| **runtime.node.gc.pause.95percentile**(gauge)              | 95th percentile garbage collection pause*Shown as nanosecond*            |
| **runtime.node.gc.pause.count**(rate)                      | Number of garbage collections*Shown as garbage collection*               |
| **runtime.node.gc.pause.by.type.max**(gauge)               | Maximum garbage collection pause by type*Shown as nanosecond*            |
| **runtime.node.gc.pause.by.type.min**(gauge)               | Minimum garbage collection pause by type*Shown as nanosecond*            |
| **runtime.node.gc.pause.by.type.avg**(gauge)               | Average garbage collection pause by type*Shown as nanosecond*            |
| **runtime.node.gc.pause.by.type.sum**(rate)                | Total garbage collection pause by type*Shown as nanosecond*              |
| **runtime.node.gc.pause.by.type.median**(gauge)            | Median garbage collection pause by type*Shown as nanosecond*             |
| **runtime.node.gc.pause.by.type.95percentile**(gauge)      | 95th percentile garbage collection pause by type*Shown as nanosecond*    |
| **runtime.node.gc.pause.by.type.count**(rate)              | Number of garbage collections by type*Shown as garbage collection*       |

{% /tab %}

{% tab title=".NET" %}

|  |
|  |
| **runtime.dotnet.cpu.system**(gauge)                           | The number of milliseconds executing in the kernel*Shown as millisecond*                                                                                   |
| **runtime.dotnet.cpu.user**(gauge)                             | The number of milliseconds executing outside the kernel*Shown as millisecond*                                                                              |
| **runtime.dotnet.cpu.percent**(gauge)                          | The percentage of total CPU used by the application*Shown as percent*                                                                                      |
| **runtime.dotnet.mem.committed**(gauge)                        | Memory usage*Shown as byte*                                                                                                                                |
| **runtime.dotnet.threads.count**(gauge)                        | The number of threads*Shown as thread*                                                                                                                     |
| **runtime.dotnet.threads.workers\_count**(gauge)               | The number of workers in the threadpool (.NET Core 3.1+ only)*Shown as thread*                                                                             |
| **runtime.dotnet.threads.contention\_time**(gauge)             | The cumulated time spent by threads waiting on a lock (.NET Core 3.1+ only)*Shown as millisecond*                                                          |
| **runtime.dotnet.threads.contention\_count**(count)            | The number of times a thread stopped to wait on a lock                                                                                                     |
| **runtime.dotnet.exceptions.count**(count)                     | The number of first-chance exceptions*Shown as exception*                                                                                                  |
| **runtime.dotnet.gc.size.gen0**(gauge)                         | The size of the gen 0 heap*Shown as byte*                                                                                                                  |
| **runtime.dotnet.gc.size.gen1**(gauge)                         | The size of the gen 1 heap*Shown as byte*                                                                                                                  |
| **runtime.dotnet.gc.size.gen2**(gauge)                         | The size of the gen 2 heap*Shown as byte*                                                                                                                  |
| **runtime.dotnet.gc.size.loh**(gauge)                          | The size of the large object heap*Shown as byte*                                                                                                           |
| **runtime.dotnet.gc.memory\_load**(gauge)                      | The percentage of the total memory used by the process. The GC changes its behavior when this value gets above 85. (.NET Core 3.1+ only)*Shown as percent* |
| **runtime.dotnet.gc.pause\_time**(gauge)                       | The amount of time the GC paused the application threads (.NET Core 3.1+ only)*Shown as millisecond*                                                       |
| **runtime.dotnet.gc.count.gen0**(count)                        | The number of gen 0 garbage collections*Shown as garbage collection*                                                                                       |
| **runtime.dotnet.gc.count.gen1**(count)                        | The number of gen 1 garbage collections*Shown as garbage collection*                                                                                       |
| **runtime.dotnet.gc.count.gen2**(count)                        | The number of gen 2 garbage collections*Shown as garbage collection*                                                                                       |
| **runtime.dotnet.aspnetcore.requests.total**(gauge)            | The total number of HTTP requests received by the server (.NET Core 3.1+ only)*Shown as request*                                                           |
| **runtime.dotnet.aspnetcore.requests.failed**(gauge)           | The number of failed HTTP requests received by the server (.NET Core 3.1+ only)*Shown as request*                                                          |
| **runtime.dotnet.aspnetcore.requests.current**(gauge)          | The total number of HTTP requests that have started but not yet stopped (.NET Core 3.1+ only)*Shown as request*                                            |
| **runtime.dotnet.aspnetcore.requests.queue\_length**(gauge)    | The current length of the server HTTP request queue (.NET 5+ only)*Shown as request*                                                                       |
| **runtime.dotnet.aspnetcore.connections.total**(gauge)         | The total number of HTTP connections established to the server (.NET 5+ only)*Shown as connection*                                                         |
| **runtime.dotnet.aspnetcore.connections.current**(gauge)       | The current number of active HTTP connections to the server (.NET 5+ only)*Shown as connection*                                                            |
| **runtime.dotnet.aspnetcore.connections.queue\_length**(gauge) | The current length of the HTTP server connection queue (.NET 5+ only)*Shown as connection*                                                                 |

{% /tab %}

## Further reading{% #further-reading %}

- [Correlate your logs and traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces)
- [Manually instrument your application to create traces.](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/glossary/)
