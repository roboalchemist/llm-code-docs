# Source: https://uptrace.dev/raw/get/opentelemetry-java.md

# OpenTelemetry Java for Uptrace

> Step-by-step guide to install and configure OpenTelemetry Java SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/java-original.svg)This document explains how to configure the OpenTelemetry Java Agent to export spans (traces), logs, and metrics to Uptrace using OTLP/gRPC.

## OpenTelemetry Java Agent

The OpenTelemetry Java Agent provides automatic instrumentation and [tracing](/get/opentelemetry-java/tracing) capabilities for Java applications without requiring any code changes. It works by attaching to a Java application at runtime and intercepting method calls to collect telemetry data.

The agent supports a huge number of [libraries and frameworks](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#libraries--frameworks) and most popular [application servers](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#application-servers).

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Download Java Agent

Download the latest pre-compiled Java agent JAR:

```shell
wget https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar
```

### Step 3: Configure Environment Variables

Configure the agent to export data to Uptrace using environment variables. Replace `<FIXME>` with your actual Uptrace DSN, and `myservice` with a name that identifies your application:

```shell
export OTEL_RESOURCE_ATTRIBUTES=service.name=myservice,service.version=1.0.0
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>"
export OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=DELTA
export OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=BASE2_EXPONENTIAL_BUCKET_HISTOGRAM
```

### Step 4: Run Your Application

Enable the agent by providing the `-javaagent` flag when starting your application:

```shell
java -javaagent:path/to/opentelemetry-javaagent.jar \
     -jar myapp.jar
```

### Step 5: View Your Trace

Navigate to the Uptrace UI to view your traces:

![Basic trace](/get/basic-trace.png)

## Configuration Options

You can find the full list of available options in the [official documentation](https://opentelemetry.io/docs/instrumentation/java/automatic/agent-config/).

<table>
<thead>
  <tr>
    <th>
      Environment Variable
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        OTEL_SERVICE_NAME
      </code>
    </td>
    
    <td>
      The logical name of the service. For example, <code>
        myservice
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_RESOURCE_ATTRIBUTES
      </code>
    </td>
    
    <td>
      Key-value pairs to be used as resource attributes. For example, <code>
        service.version=1.0.0
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_ENDPOINT
      </code>
    </td>
    
    <td>
      OTLP exporter endpoint. For Uptrace, use <code>
        https://api.uptrace.dev:4317
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_HEADERS
      </code>
    </td>
    
    <td>
      Headers to send with OTLP requests. For example, <code>
        uptrace-dsn=<your-dsn>
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER
      </code>
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/sampling">
        Sampler
      </a>
      
       to use. For example, <code>
        parentbased_traceidratio
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER_ARG
      </code>
    </td>
    
    <td>
      Sampler argument. For example, <code>
        0.1
      </code>
      
       to sample 10% of traces.
    </td>
  </tr>
</tbody>
</table>

### Configuration Methods

The agent can be configured using environment variables, system properties, or a configuration file.

<code-group>

```shell [Environment variables]
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>"
export OTEL_RESOURCE_ATTRIBUTES=service.name=myservice,service.version=1.0.0
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
export OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=DELTA
export OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=BASE2_EXPONENTIAL_BUCKET_HISTOGRAM
```

```shell [System properties]
java -javaagent:path/to/opentelemetry-javaagent.jar \
     -jar myapp.jar \
     -Dotel.exporter.otlp.endpoint=https://api.uptrace.dev:4317 \
     -Dotel.exporter.otlp.headers=uptrace-dsn=<FIXME> \
     -Dotel.resource.attributes=service.name=myservice,service.version=1.0.0 \
     -Dotel.traces.exporter=otlp \
     -Dotel.metrics.exporter=otlp \
     -Dotel.logs.exporter=otlp \
     -Dotel.exporter.otlp.compression=gzip \
     -Dotel.exporter.otlp.metrics.temporality.preference=DELTA \
     -Dotel.exporter.otlp.metrics.default.histogram.aggregation=BASE2_EXPONENTIAL_BUCKET_HISTOGRAM
```

```properties [Configuration file]
# Save as uptrace.properties
otel.exporter.otlp.protocol=grpc
otel.exporter.otlp.endpoint=https://api.uptrace.dev:4317
otel.exporter.otlp.headers=uptrace-dsn=<FIXME>
otel.resource.attributes=service.name=myservice,service.version=1.0.0
otel.traces.exporter=otlp
otel.metrics.exporter=otlp
otel.logs.exporter=otlp
otel.exporter.otlp.compression=gzip
otel.exporter.otlp.metrics.temporality.preference=DELTA
otel.exporter.otlp.metrics.default.histogram.aggregation=BASE2_EXPONENTIAL_BUCKET_HISTOGRAM
```

</code-group>

When using a configuration file, pass it to the agent using the `otel.javaagent.configuration-file` system property:

```shell
java -javaagent:path/to/opentelemetry-javaagent.jar \
     -Dotel.javaagent.configuration-file=path/to/uptrace.properties \
     -jar myapp.jar
```

## Disabling the Java Agent

To disable the agent entirely, pass `-Dotel.javaagent.enabled=false` or use the `OTEL_JAVAAGENT_ENABLED=false` environment variable.

You can also disable specific instrumentations by passing `-Dotel.instrumentation.[name].enabled=false` or using the `OTEL_INSTRUMENTATION_[NAME]_ENABLED=false` environment variable. See the [documentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md#libraries--frameworks) for the list of instrumentation names.

## Troubleshooting

### Common Issues

**Agent not starting:**

- Verify the path to the `opentelemetry-javaagent.jar` file is correct
- Check that Java has read permissions for the JAR file
- Ensure you're using a supported Java version

**No data in Uptrace:**

- Verify your DSN is correctly configured in `OTEL_EXPORTER_OTLP_HEADERS`
- Check that the endpoint URL is correct: `https://api.uptrace.dev:4317`
- Ensure your application is generating [spans](/get/opentelemetry-java/tracing) (check application logs for errors)

**Performance issues:**

- Adjust sampling rate to reduce overhead: `OTEL_TRACES_SAMPLER_ARG=0.1` (10% sampling)
- Disable unused instrumentations to reduce memory usage

## What's Next?

Instrument more operations to get a detailed picture of your application. Prioritize network calls, database queries, errors, and logs.

### By Use Case

<table>
<thead>
  <tr>
    <th>
      I want to...
    </th>
    
    <th>
      Read this
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Instrument without code changes
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/zero-code">
        Zero-code instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/tracing">
        Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/metrics">
        Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/logs">
        Logs integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/propagation">
        Context propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/resources">
        Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry Spring Boot](/guides/opentelemetry-spring-boot)
- [OpenTelemetry Quarkus](/guides/opentelemetry-quarkus)
- [OpenTelemetry Tomcat](/guides/opentelemetry-tomcat)

### Logging Libraries

- [OpenTelemetry Log4j2](/guides/opentelemetry-log4j)
- [OpenTelemetry Logback](/guides/opentelemetry-logback)
