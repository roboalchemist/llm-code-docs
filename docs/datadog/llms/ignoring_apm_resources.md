# Source: https://docs.datadoghq.com/tracing/guide/ignoring_apm_resources.md

---
title: Ignoring Unwanted Resources in APM
description: >-
  Learn how to exclude unwanted resources like health checks from traces using
  sampling rules and filtering to reduce noise and manage costs.
breadcrumbs: Docs > APM > Tracing Guides > Ignoring Unwanted Resources in APM
---

# Ignoring Unwanted Resources in APM

A service can handle a variety of requests, some of which you might not want traced or included in trace metrics. An example of this is, possibly, health checks in a web application. This documentation covers two main options: sampling and filtering.

If you need assistance deciding which option is the most relevant for your use case, contact [Datadog support](https://docs.datadoghq.com/help/).

## Sampling{% #sampling %}

If you want the span included in the trace metrics but don't want it ingested, use sampling rules. For more information on sampling, see [Ingestion Controls](https://docs.datadoghq.com/tracing/trace_ingestion/ingestion_controls).

### Using sampling rules{% #using-sampling-rules %}

The recommended approach is to use sampling rules, which allow you to sample traces based on resource names, service names, tags, and operation names:

```shell
DD_TRACE_SAMPLING_RULES='[{"resource": "GET healthcheck", "sample_rate": 0.0}]'
```

Or to sample based on HTTP URL tags:

```shell
DD_TRACE_SAMPLING_RULES='[{"tags": {"http.url": "http://.*/healthcheck$"}, "sample_rate": 0.0}]'
```

{% alert level="info" %}
Sampling decisions are determined using the first span in a trace. If the span containing the tag you want to filter on is not a Trace root span (A span is a trace root span when it is the first span of a trace. The root span is the entry-point method of the traced request. Its start marks the beginning of the trace.), this rule is not applied.
{% /alert %}

## Filtering{% #filtering %}

If you don't want the span ingested and don't want to see it reflected in trace metrics, use filtering.

There are two ways to specify that such an endpoint should be untraced and excluded from trace metrics:

- Trace Agent configuration (in Datadog Agent), or
- Tracer configuration.

### Trace Agent configuration options{% #trace-agent-configuration-options %}

The Trace Agent component within the Datadog Agent has two methods to prevent certain traces from coming through: ignoring span tags or ignoring resources. If traces are dropped due to these settings, the trace metrics exclude these requests.

Configuring the Trace Agent to ignore certain spans or resources applies to all services that send traces to this particular Datadog Agent. If you have application-specific requirements, use the Tracer configuration method instead.

#### Ignoring based on span tags{% #ignoring-based-on-span-tags %}

Starting with Datadog Agent 6.27.0/7.27.0, the **filter tags** option drops traces with root spans that match specified span tags. This option applies to all services that send traces to this particular Datadog Agent. Traces that are dropped because of filter tags are not included in trace metrics.

If you can programmatically identify a set of traces that you know you don't want to send to Datadog, and no other option in this guide solves your requirement, you can consider adding a [custom span tag](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/otel_instrumentation/) so you can drop the traces. [Reach out to Support](https://docs.datadoghq.com/help/) to discuss your use case further so Datadog can continue to expand this functionality.

The filter tags option requires an exact string match. If your use case requires ignoring by regex, see Ignoring based on resources.

You can specify span tags to require or reject by using a list of keys and values separated by spaces in environment variables:

{% dl %}

{% dt %}
`DD_APM_FILTER_TAGS_REQUIRE`
{% /dt %}

{% dd %}
Collects only traces that have root spans with an exact match for the specified span tags and values. If it does not match this rule, the trace is dropped. For example, `DD_APM_FILTER_TAGS_REQUIRE="key1:value1 key2:value2"`. In Datadog Agent 7.49+, regular expressions can be provided with `DD_APM_FILTER_TAGS_REGEX_REQUIRE`.
{% /dd %}

{% dt %}
`DD_APM_FILTER_TAGS_REJECT`
{% /dt %}

{% dd %}
Rejects traces that have root spans with an exact match for the specified span tags and values. If it matches this rule, the trace is dropped. For example, `DD_APM_FILTER_TAGS_REJECT="key1:value1 key2:value2"`. In Datadog Agent 7.49+, regular expressions can be provided with `DD_APM_FILTER_TAGS_REGEX_REJECT`.
{% /dd %}

{% /dl %}

{% tab title="datadog.yaml" %}
Alternatively, you can set them in the Agent configuration with a comma-separated list:

In the `datadog.yaml` file:

```yaml
apm_config:
  filter_tags:
    require: ["db:sql", "db.instance:mysql"]
    reject: ["outcome:success", "key2:value2"]
```

For example, to ignore health checks where the `http.url` matches this endpoint:

In the `datadog.yaml` file:

```yaml
apm_config:
  filter_tags:
    reject: ["http.url:http://localhost:5050/healthcheck"]
```

{% /tab %}

{% tab title="Kubernetes" %}
##### Datadog Operator{% #datadog-operator %}

In the `datadog-agent.yaml` file:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  override:
    nodeAgent:
      containers:
        trace-agent:
          env:
            - name: DD_APM_FILTER_TAGS_REJECT
              value: tag_key1:tag_val2 tag_key2:tag_val2
```

After making your changes, apply the new configuration by using the following command:

```shell
kubectl apply -n $DD_NAMESPACE -f datadog-agent.yaml
```

##### Helm{% #helm %}

In the `datadog-values.yaml` file:

```yaml
agents:
  containers:
    traceAgent:
      env:
        - name: DD_APM_FILTER_TAGS_REJECT
          value: tag_key1:tag_val2 tag_key2:tag_val2
```

After making your changes, upgrade your Datadog Helm chart using the following command:

```shell
helm upgrade -f datadog-values.yaml <RELEASE NAME> datadog/datadog
```

{% /tab %}

Filtering traces this way removes these requests from [trace metrics](https://docs.datadoghq.com/tracing/guide/metrics_namespace/). For more information on how to reduce ingestion without affecting the trace metrics, see [Ingestion Controls](https://docs.datadoghq.com/tracing/trace_ingestion/ingestion_controls).

On the backend, Datadog creates and adds the following span tags to spans after ingestion. Note, these tags cannot be used to drop traces at the Datadog Agent level, as the agent only filters based on tags available before ingestion.

| Name                                    | Description                                                              |
| --------------------------------------- | ------------------------------------------------------------------------ |
| `http.path_group`                       | The full URL path from the `http.url` tag.                               |
| `http.url_details.host`                 | The host name portion of the `http.url` tag.                             |
| `http.url_details.path`                 | The full request target as passed in an HTTP request line or equivalent. |
| `http.url_details.scheme`               | The request scheme from the `http.url` tag.                              |
| `http.url_details.queryString`          | The query string portion from the `http.url` tag.                        |
| `http.url_details.port`                 | The HTTP port from the `http.url` tag.                                   |
| `http.useragent_details.os.family`      | The OS family reported by the User-Agent.                                |
| `http.useragent_details.browser.family` | The browser family reported by the User-Agent.                           |
| `http.useragent_details.device.family`  | The device family reported by the User-Agent.                            |

{% alert level="danger" %}
Starting from October 1st 2022, Datadog backend applies a remapping in order to apply [Span Tags Semantics ](https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention)across tracers on all ingested spans. If you want to drop spans based on tags at the Datadog Agent level, use tags in the **Remap from** column.
{% /alert %}

##### Network communications{% #network-communications %}

| **Name**                   | **Remap from**                                                            |
| -------------------------- | ------------------------------------------------------------------------- |
| `network.host.ip`          | `tcp.local.address` - Node.js                                             |
| `network.destination.ip`   | `out.host` - All languages                                                |
| `network.destination.port` | `grpc.port` - Python`tcp.remote.port` - Node.js`out.port` - All languages |

##### HTTP requests{% #http-requests %}

| **Name**                       | **Remap from**                                                                            |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| `http.route`                   | `aspnet_core.route` - .NET`aspnet.route` - .NET`laravel.route` - PHP`symfony.route` - PHP |
| `http.useragent`               | `user_agent` - Java, C++                                                                  |
| `http.url_details.queryString` | `http.query.string` - Python                                                              |

##### Database{% #database %}

| **Name**                         | **Remap from**                                                                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `db.system`                      | `db.type` - Java, Python, Node.js, Go`active_record.db.vendor` - Ruby`sequel.db.vendor` - Ruby                                                                                                          |
| `db.instance`                    | `mongodb.db` - Python`sql.db` - Python`db.name` - All languages                                                                                                                                         |
| `db.statement`                   | `cassandra.query` - Go`consul.command` - Python`memcached.query` - Python`mongodb.query` - Python, .NET, Go`redis.command` - Python`redis.raw_command` - Python`sql.query` - Python, PHP, Node.js, Java |
| `db.row_count`                   | `cassandra.row_count` - Python`db.rowcount` - Python, PHP`mongodb.rows` - Python`sql.rows` - Python                                                                                                     |
| `db.cassandra.cluster`           | `cassandra.cluster` - Python, Go                                                                                                                                                                        |
| `db.cassandra.consistency_level` | `cassandra.consistency_level` - Python, Go                                                                                                                                                              |
| `db.cassandra.table`             | `cassandra.keyspace` - Python, Go                                                                                                                                                                       |
| `db.redis.database_index`        | `db.redis.dbIndex` - Java`out.redis_db` - Python, Ruby                                                                                                                                                  |
| `db.mongodb.collection`          | `mongodb.collection` - Python, .NET, Ruby, PHP                                                                                                                                                          |
| `db.cosmosdb.container`          | `cosmosdb.container` - .NET                                                                                                                                                                             |

##### Message Queue{% #message-queue %}

| **Name**                               | **Remap from**                                                                                 |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `messaging.destination`                | `amqp.destination` - Node.js`amqp.queue` - .NET`msmq.queue.path` - .NET`aws.queue.name` - .NET |
| `messaging.url`                        | `aws.queue.url` - .NET, Java                                                                   |
| `messaging.message_id`                 | `server_id` - Go                                                                               |
| `messaging.message_payload_size`       | `message.size` - .NET, Java                                                                    |
| `messaging.operation`                  | `amqp.command` - .NET`msmq.command` - .NET                                                     |
| `messaging.rabbitmq.routing_key`       | `amqp.routing_key` - Java`amqp.routingKey` - Nodes.js                                          |
| `messaging.rabbitmq.delivery_mode`     | `messaging.rabbitmq.exchange` - .NET                                                           |
| `messaging.msmq.message.transactional` | `msmq.message.transactional` - .NET                                                            |
| `messaging.msmq.queue.transactional`   | `msmq.queue.transactional` - .NET                                                              |
| `messaging.kafka.consumer_group`       | `kafka.group` - Java                                                                           |
| `messaging.kafka.tombstone`            | `kafka.tombstone` - .NET`tombstone` - Java                                                     |
| `messaging.kafka.partition`            | `kafka.partition` - .NET`partition` - Node.js, Go, Java                                        |
| `messaging.kafka.offset`               | `kafka.offset` - .NET                                                                          |
| `messaging.msmq.message.transactional` | `msmq.message.transactional` - .NET                                                            |

##### Remote procedure calls{% #remote-procedure-calls %}

| **Name**                       | **Remap from**                                                                                  |
| ------------------------------ | ----------------------------------------------------------------------------------------------- |
| `rpc.service`                  | `grpc.method.service` - Python, .NET                                                            |
| `rpc.method`                   | `grpc.method.name` - Python, .NET, Go                                                           |
| `rpc.grpc.package`             | `grpc.method.package` - Python, .NET, Go                                                        |
| `rpc.grpc.status_code`         | `grpc.code` - Go`status.code` - Python, .NET, Node.js`grpc.status.code` - Python, .NET, Node.js |
| `rpc.grpc.kind`                | `grpc.method.kind` - Python, Node.js, Go, .NET                                                  |
| `rpc.grpc.path`                | `rpc.grpc.path` - Python, Node.js, Go, .NET                                                     |
| `rpc.grpc.request.metadata.*`  | `grpc.request.metadata.*` - Python, Node.js`rpc.grpc.request.metadata` - Go                     |
| `rpc.grpc.response.metadata.*` | `grpc.response.metadata.*` - Python, Node.js                                                    |

##### Errors{% #errors %}

| **Name**        | **Remap from**              |
| --------------- | --------------------------- |
| `error.message` | `error.msg` - All languages |

#### Ignoring based on resources{% #ignoring-based-on-resources %}

The **ignore resources** option allows resources to be excluded if the global root span of the trace matches certain criteria. See [Exclude resources from being collected](https://docs.datadoghq.com/tracing/configure_data_security/?tab=mongodb#exclude-resources-from-being-collected). This option applies to all services that send traces to this particular Datadog Agent. Traces that are dropped because of ignore resources are not included in trace metrics.

You can specify resources to ignore either in the Agent configuration file, `datadog.yaml`, or with the `DD_APM_IGNORE_RESOURCES` environment variable. See examples below.

Using `datadog.yaml`:

In the `datadog.yaml` file:

```yaml
apm_config:
## @param ignore_resources - list of strings - optional
## A list of regular expressions can be provided to exclude certain traces based on their resource name.
## All entries must be surrounded by double quotes and separated by commas.

  ignore_resources: ["(GET|POST) /healthcheck","API::NotesController#index"]
```

Using `DD_APM_IGNORE_RESOURCES`:

```shell
DD_APM_IGNORE_RESOURCES="(GET|POST) /healthcheck,API::NotesController#index"
```

**Notes**:

- When using the environment variable format (`DD_APM_IGNORE_RESOURCES`), values must be provided as a comma-separated list of strings.
- The regex syntax that the Trace Agent accepts is evaluated by Go's [regexp](https://golang.org/pkg/regexp/).
- Depending on your deployment strategy, you may have to adjust the regex by escaping special characters.
- If you use dedicated containers with Kubernetes, make sure that the environment variable for the ignore resource option is being applied to the **trace-agent** container.

##### Example{% #example %}

Consider a trace that contains calls to `/api/healthcheck` that you don't want traces from:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/ignoring_apm_resources/ignoreresources.1ed6b670e3525b7180131992d35d3186.png?auto=format"
   alt="Flame graph of a resource you want the tracer to ignore" /%}

Take note of the resource name of the global root span.

- Operation name: `rack.request`
- Resource name: `Api::HealthchecksController#index`
- Http.url: `/api/healthcheck`

To use the ignore resource option correctly, the regex rule written must match with the resource name, `Api::HealthchecksController#index`. A few regex options are possible, but to filter out traces from this resource exactly as is, a potential regex to use is `Api::HealthchecksController#index$`.

Depending on how you deploy, the syntax looks a little different:

{% tab title="datadog.yaml" %}
In the `datadog.yaml` file:

```yaml
apm_config:
  ignore_resources: Api::HealthchecksController#index$
```

For multiple values:

```yaml
apm_config:
  ignore_resources: ["value1","Api::HealthchecksController#index$"]
```

{% /tab %}

{% tab title="Docker compose" %}
In the Datadog Agent container's list of environment variables, add `DD_APM_IGNORE_RESOURCES` with a pattern like the example below. Docker Compose has its own [variable substitution](https://docs.docker.com/compose/compose-file/compose-file-v3/#variable-substitution) to consider when you use special characters like `$`.

```yaml
    environment:
      // other Datadog Agent environment variables
      - DD_APM_IGNORE_RESOURCES=Api::HealthchecksController#index$$
```

For multiple values:

```yaml
    environment:
      // other Datadog Agent environment variables
      - DD_APM_IGNORE_RESOURCES="value1","Api::HealthchecksController#index$$"
```

{% /tab %}

{% tab title="Docker run" %}
In your docker run command to spin up the Datadog Agent, add `DD_APM_IGNORE_RESOURCES`:

```shell
docker run -d --name datadog-agent \
              --cgroupns host \
              --pid host \
              -v /var/run/docker.sock:/var/run/docker.sock:ro \
              -v /proc/:/host/proc/:ro \
              -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
              -e DD_API_KEY=<> \
              -e DD_APM_IGNORE_RESOURCES="Api::HealthchecksController#index$" \
              -e DD_APM_ENABLED=true \
              -e DD_APM_NON_LOCAL_TRAFFIC=true \
              gcr.io/datadoghq/agent:latest
```

For multiple values:

```yaml
              -e DD_APM_IGNORE_RESOURCES=["value1","Api::HealthchecksController#index$"] \
```

{% /tab %}

{% tab title="Kubernetes daemonset" %}
In the dedicated trace-agent container, add the environment variable `DD_APM_IGNORE_RESOURCES`:

```yaml
    - name: trace-agent
        image: "gcr.io/datadoghq/agent:latest"
        imagePullPolicy: IfNotPresent
        command: ["trace-agent", "-config=/etc/datadog-agent/datadog.yaml"]
        resources: {}
        ports:
        - containerPort: 8126
          hostPort: 8126
          name: traceport
          protocol: TCP
        env:
        - name: DD_API_KEY
          valueFrom:
            secretKeyRef:
              name: "datadog-secret"
              key: api-key
        - name: DD_KUBERNETES_KUBELET_HOST
          valueFrom:
            fieldRef:
              fieldPath: status.hostIP
        - name: KUBERNETES
          value: "yes"
        - name: DOCKER_HOST
          value: unix:///host/var/run/docker.sock
        - name: DD_LOG_LEVEL
          value: "INFO"
        - name: DD_APM_ENABLED
          value: "true"
        - name: DD_APM_NON_LOCAL_TRAFFIC
          value: "true"
        - name: DD_APM_RECEIVER_PORT
          value: "8126"
        - name: DD_KUBELET_TLS_VERIFY
          value: "false"
        - name: DD_APM_IGNORE_RESOURCES
          value: "Api::HealthchecksController#index$"
```

For multiple values:

```yaml
        - name: DD_APM_IGNORE_RESOURCES
          value: '"value1","Api::HealthchecksController#index$"'
```

{% /tab %}

{% tab title="Kubernetes Helm" %}
In the `traceAgent` section of the `values.yaml` file, add `DD_APM_IGNORE_RESOURCES` in the `env` section, then [spin up helm as usual](https://docs.datadoghq.com/agent/kubernetes/?tab=helm#installation).

In the `values.yaml` file:

```yaml
    traceAgent:
      # agents.containers.traceAgent.env -- Additional environment variables for the trace-agent container
      env:
        - name: DD_APM_IGNORE_RESOURCES
          value: Api::HealthchecksController#index$
```

For multiple values:

```yaml
        - name: DD_APM_IGNORE_RESOURCES
          value: value1, Api::HealthchecksController#index$
```

Alternatively, you can set `agents.containers.traceAgent.env` in the `helm install` command:

```shell
helm install dd-agent -f values.yaml \
  --set datadog.apiKeyExistingSecret="datadog-secret" \
  --set agents.containers.traceAgent.env[0].name=DD_APM_IGNORE_RESOURCES, \
    agents.containers.traceAgent.env[0].value="Api::HealthchecksController#index$" \
  datadog/datadog
```

{% /tab %}

{% tab title="Amazon ECS Task Definition" %}
If you use Amazon ECS (such as on EC2), in your Datadog Agent container definition, add the environment variable `DD_APM_IGNORE_RESOURCES` with the values such that the JSON evaluates to something like this:

```json
    "environment": [
    // other environment variables for the Datadog Agent
        {
          "name": "DD_APM_IGNORE_RESOURCES",
          "value": "Api::HealthchecksController#index$"
        }
     ]
```

{% /tab %}

{% alert level="danger" %}
Filtering traces this way removes these requests from [trace metrics](https://docs.datadoghq.com/tracing/guide/metrics_namespace/). For information on how to reduce ingestion without affecting the trace metrics, see [ingestion controls](https://docs.datadoghq.com/tracing/trace_ingestion/ingestion_controls).
{% /alert %}

## Tracer configuration options{% #tracer-configuration-options %}

Some of the language-specific tracers have an option to modify spans before they are sent to the Datadog Agent. Use this option if you have application-specific requirements and are using a language listed below.

{% alert level="warning" %}
1. If the request is associated with a distributed trace, the resulting trace can have sampling inaccuracy if you drop portions of it due to these filtering rules.2. Filtering traces this way removes these requests from [trace metrics](https://docs.datadoghq.com/tracing/guide/metrics_namespace/). For information on how to reduce ingestion without affecting the trace metrics, see [ingestion controls](https://docs.datadoghq.com/tracing/trace_ingestion/ingestion_controls).
{% /alert %}

{% tab title="Ruby" %}
The Ruby tracer has a post-processing pipeline that removes traces that meet certain criteria. More information and examples can be found in [Post-processing traces](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/ruby/?tab=activespan#post-processing-traces).

For example, if the resource name is `Api::HealthchecksController#index`, use the `Datadog::Tracing::Pipeline::SpanFilter` class to remove traces that contain the resource name. This filter can also be used to match on other metadata available for the [span object](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby/#manual-instrumentation).

```
Datadog::Tracing.before_flush(
   Datadog::Tracing::Pipeline::SpanFilter.new { |span| span.resource =~ /Api::HealthchecksController#index/ }
)
```

{% /tab %}

{% tab title="Python" %}
The Python tracer provides an option to filter unwanted traces:

### Using custom filters{% #using-custom-filters %}

For advanced use cases, you can create custom filters:

```py
from ddtrace.trace import tracer
from ddtrace.trace import TraceFilter
import re

class CustomFilter(TraceFilter):
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)

    def process_trace(self, trace):
        for span in trace:
            if span.get_tag('http.url') and self.pattern.match(span.get_tag('http.url')):
                return None  # Drop the trace
        return trace  # Keep the trace

# Configure the tracer with your custom filter
tracer.configure(trace_processors=[CustomFilter(r'http://.*/healthcheck$')])
```

{% /tab %}

{% tab title="Node.js" %}
Configure a blocklist on the [Http](https://datadoghq.dev/dd-trace-js/interfaces/export_.plugins.connect.html#blocklist) plugin. Take note of what the blocklist matches on from the API docs. For example, incoming Http requests matches on URL paths, so if the trace's `http.url` span tag is `http://<domain>/healthcheck`, write a rule that matches the `healthcheck` URL:

```gdscript3
const tracer = require('dd-trace').init();
tracer.use('http', {
  // incoming http requests match on the path
  server: {
    blocklist: ['/healthcheck']
  },
  // outgoing http requests match on a full URL
  client: {
    blocklist: ['https://telemetry.example.org/api/v1/record']
  }
})

//import http
```

{% alert level="info" %}
The tracer configuration for the integration must come *before* that instrumented module is imported.
{% /alert %}

{% /tab %}

{% tab title="Java" %}
The Java tracer has an option for a custom `TraceInterceptor` to filter out certain spans. See [Extending Tracers](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java/#extending-tracers).

For example, if your resource name is `GET /healthcheck`, write a trace interceptor that drops traces containing this resource name. Adjust the logic to meet your use case.

```gdscript3
public class GreetingController {
   static {
       // In a class static block to avoid initializing multiple times.
       GlobalTracer.get().addTraceInterceptor(new TraceInterceptor() {
           @Override
           public Collection<? extends MutableSpan> onTraceComplete(Collection<? extends MutableSpan> trace) {
               for (MutableSpan span : trace) {
                   if ("GET /healthcheck".contentEquals(span.getResourceName())) {
                       return Collections.emptyList();
                   }
               }
               return trace;
           }
           @Override
           public int priority() {
               return 200;  // Some unique number
           }
       });
   }
}
```

{% /tab %}
