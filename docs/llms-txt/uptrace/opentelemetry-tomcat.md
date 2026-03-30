# Source: https://uptrace.dev/raw/guides/opentelemetry-tomcat.md

# OpenTelemetry Tomcat: Instrumentation and Monitoring Guide

> Monitor Apache Tomcat with OpenTelemetry Java Agent. Step-by-step setup for automatic tracing, JVM metrics, servlet instrumentation, and production deployment.

OpenTelemetry provides automatic instrumentation for Apache Tomcat applications, enabling distributed tracing, JVM metrics collection, and servlet monitoring without code changes. Using the OpenTelemetry Java Agent, you can gain full observability into your Tomcat-hosted web applications, including request latencies, database queries, and downstream service calls.

## Quick Reference

<table>
<thead>
  <tr>
    <th>
      Component
    </th>
    
    <th>
      Details
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Instrumentation method
    </td>
    
    <td>
      OpenTelemetry Java Agent (automatic)
    </td>
  </tr>
  
  <tr>
    <td>
      Supported signals
    </td>
    
    <td>
      Traces, Metrics, Logs
    </td>
  </tr>
  
  <tr>
    <td>
      Code changes required
    </td>
    
    <td>
      None (agent-based)
    </td>
  </tr>
  
  <tr>
    <td>
      Configuration
    </td>
    
    <td>
      Environment variables in <code>
        setenv.sh
      </code>
      
       / <code>
        setenv.bat
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Libraries instrumented
    </td>
    
    <td>
      Servlets, JSP, JDBC, HTTP clients, JMS, and 150+ more
    </td>
  </tr>
</tbody>
</table>

## What is OpenTelemetry?

[OpenTelemetry](/opentelemetry) is an open-source observability framework that standardizes the collection of telemetry data from applications. It provides three pillars of observability:

- **Distributed Traces**: Track requests across services and components
- **Metrics**: Collect JVM, servlet, and application-level measurements
- **Logs**: Capture structured application logs with trace correlation

OpenTelemetry is vendor-neutral, meaning you can export data to any compatible [OpenTelemetry backend](/blog/opentelemetry-backend) such as Uptrace, Jaeger, or Grafana. Configuration is managed through [environment variables](/opentelemetry/env-vars).

## Prerequisites

- **Apache Tomcat 7.0+** (Tomcat 9 and 10 recommended)
- **Java 8+** (Java 11+ recommended for full metrics support)
- **Network access** to your OTLP-compatible backend

## OpenTelemetry Java Agent

The OpenTelemetry Java Agent automatically instruments Tomcat applications at the bytecode level, capturing traces for servlets, JDBC queries, HTTP clients, and 150+ libraries without code changes.

Download the latest agent JAR:

```shell
wget https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar
```

Place the JAR in a directory accessible by Tomcat, such as `/opt/opentelemetry/` or Tomcat's `lib` directory.

<alert type="info">

For detailed agent configuration options and troubleshooting, see the [Java zero-code instrumentation guide](/get/opentelemetry-java/zero-code).

</alert>

## Configuring Tomcat with OpenTelemetry

### Linux / macOS

Create a `setenv.sh` file in Tomcat's `bin` directory:

```shell
#!/bin/bash

# Attach the OpenTelemetry Java Agent
export CATALINA_OPTS="$CATALINA_OPTS -javaagent:/opt/opentelemetry/opentelemetry-javaagent.jar"

# Service identification
export OTEL_RESOURCE_ATTRIBUTES=service.name=tomcat-app,service.version=1.0.0

# Enable all signal types
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp

# OTLP exporter configuration
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
export OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>"

# Recommended metrics settings
export OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=DELTA
export OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=BASE2_EXPONENTIAL_BUCKET_HISTOGRAM
```

Make the script executable and restart Tomcat:

```shell
chmod +x bin/setenv.sh
./bin/shutdown.sh && ./bin/startup.sh
```

### Windows

Create a `setenv.bat` file in Tomcat's `bin` directory:

```bat
set "CATALINA_OPTS=%CATALINA_OPTS% -javaagent:C:\opentelemetry\opentelemetry-javaagent.jar"

set OTEL_RESOURCE_ATTRIBUTES=service.name=tomcat-app,service.version=1.0.0
set OTEL_TRACES_EXPORTER=otlp
set OTEL_METRICS_EXPORTER=otlp
set OTEL_LOGS_EXPORTER=otlp
set OTEL_EXPORTER_OTLP_COMPRESSION=gzip
set OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
set OTEL_EXPORTER_OTLP_HEADERS=uptrace-dsn=<FIXME>
set OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=DELTA
set OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=BASE2_EXPONENTIAL_BUCKET_HISTOGRAM
```

### Docker

For containerized Tomcat deployments, pass the agent as a JVM argument in your Dockerfile:

```dockerfile
FROM tomcat:10-jdk17

# Download OpenTelemetry Java Agent
ADD https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar /opt/opentelemetry/opentelemetry-javaagent.jar

# Set environment variables
ENV CATALINA_OPTS="-javaagent:/opt/opentelemetry/opentelemetry-javaagent.jar"
ENV OTEL_RESOURCE_ATTRIBUTES="service.name=tomcat-app,service.version=1.0.0"
ENV OTEL_TRACES_EXPORTER="otlp"
ENV OTEL_METRICS_EXPORTER="otlp"
ENV OTEL_LOGS_EXPORTER="otlp"
ENV OTEL_EXPORTER_OTLP_COMPRESSION="gzip"

# Deploy your application
COPY target/myapp.war /usr/local/tomcat/webapps/
```

Build and run:

```shell
docker build -t tomcat-otel .
docker run -p 8080:8080 \
  -e OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317 \
  -e OTEL_EXPORTER_OTLP_HEADERS="uptrace-dsn=<FIXME>" \
  tomcat-otel
```

For a complete Docker Compose setup with the OpenTelemetry Collector, see the [Docker deployment guide](/guides/opentelemetry-docker).

## Verifying the Installation

After restarting Tomcat, verify the agent is attached by checking the Tomcat logs:

```shell
tail -f logs/catalina.out | grep -i opentelemetry
```

You should see output similar to:

```text
[otel.javaagent] opentelemetry-javaagent - version: 2.x.x
[otel.javaagent] Installed instrumentation: servlet-5.0 [io.opentelemetry.javaagent]
[otel.javaagent] Installed instrumentation: tomcat-10.0 [io.opentelemetry.javaagent]
```

You can also verify from a running process:

```shell
ps aux | grep javaagent
```

## What Gets Instrumented Automatically

The Java Agent instruments these Tomcat components without code changes:

<table>
<thead>
  <tr>
    <th>
      Component
    </th>
    
    <th>
      Captured Data
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      HTTP Servlets
    </td>
    
    <td>
      Request method, URL, status code, latency
    </td>
  </tr>
  
  <tr>
    <td>
      JSP Pages
    </td>
    
    <td>
      Rendering time, template name
    </td>
  </tr>
  
  <tr>
    <td>
      JDBC
    </td>
    
    <td>
      Database queries, connection pool metrics
    </td>
  </tr>
  
  <tr>
    <td>
      HTTP Clients
    </td>
    
    <td>
      Outgoing requests (HttpURLConnection, Apache HttpClient)
    </td>
  </tr>
  
  <tr>
    <td>
      JMS
    </td>
    
    <td>
      Message queue operations
    </td>
  </tr>
  
  <tr>
    <td>
      JMX Metrics
    </td>
    
    <td>
      JVM memory, GC, thread counts, CPU usage
    </td>
  </tr>
</tbody>
</table>

## Custom Instrumentation

For application-specific tracing beyond automatic instrumentation, add the OpenTelemetry API to your project.

Add the dependency to `pom.xml`:

```xml
<dependency>
    <groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-api</artifactId>
    <version>1.44.1</version>
</dependency>
```

Create custom spans in your servlets:

```java
import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import jakarta.servlet.http.*;

public class OrderServlet extends HttpServlet {
    private static final Tracer tracer =
        GlobalOpenTelemetry.getTracer("com.example.orders");

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
        Span span = tracer.spanBuilder("process-order").startSpan();
        try (var scope = span.makeCurrent()) {
            String orderId = req.getParameter("orderId");
            span.setAttribute("order.id", orderId);

            // Your business logic
            processOrder(orderId);

            span.setAttribute("order.status", "completed");
        } catch (Exception e) {
            span.recordException(e);
            span.setStatus(io.opentelemetry.api.trace.StatusCode.ERROR, e.getMessage());
            resp.setStatus(500);
        } finally {
            span.end();
        }
    }
}
```

For comprehensive Java instrumentation, see the [OpenTelemetry Java guide](/get/opentelemetry-java).

## Environment Variables Reference

Common environment variables for tuning the Java Agent with Tomcat:

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Example Value
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
      Service name
    </td>
    
    <td>
      <code>
        tomcat-app
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_ENDPOINT
      </code>
    </td>
    
    <td>
      OTLP collector endpoint
    </td>
    
    <td>
      <code>
        https://api.uptrace.dev:4317
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_EXPORTER_OTLP_HEADERS
      </code>
    </td>
    
    <td>
      Authentication headers
    </td>
    
    <td>
      <code>
        uptrace-dsn=<FIXME>
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER
      </code>
    </td>
    
    <td>
      Sampling strategy
    </td>
    
    <td>
      <code>
        parentbased_traceidratio
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_TRACES_SAMPLER_ARG
      </code>
    </td>
    
    <td>
      Sampling ratio (0.0 to 1.0)
    </td>
    
    <td>
      <code>
        0.1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST
      </code>
    </td>
    
    <td>
      Capture request headers
    </td>
    
    <td>
      <code>
        content-type,x-request-id
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        OTEL_JAVAAGENT_DEBUG
      </code>
    </td>
    
    <td>
      Enable debug logging
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
</tbody>
</table>

For the full list of environment variables, see the [OpenTelemetry environment variables reference](/opentelemetry/env-vars).

## Troubleshooting

**Agent not loading**: Verify the `-javaagent` path is correct and the JAR file is readable by the Tomcat process user. Check `catalina.out` for errors.

**No traces appearing**: Confirm `OTEL_EXPORTER_OTLP_ENDPOINT` is reachable from the Tomcat server. Test connectivity:

```shell
curl -v https://api.uptrace.dev:4317
```

**High memory usage**: Reduce the export batch size and queue:

```shell
export OTEL_BSP_MAX_QUEUE_SIZE=512
export OTEL_BSP_MAX_EXPORT_BATCH_SIZE=128
```

**Startup performance**: The agent adds 100-300ms to startup. For faster startup in development, disable unused instrumentations:

```shell
export OTEL_INSTRUMENTATION_COMMON_DEFAULT_ENABLED=false
export OTEL_INSTRUMENTATION_SERVLET_ENABLED=true
export OTEL_INSTRUMENTATION_JDBC_ENABLED=true
```

**Debug logging**: Enable agent debug output to diagnose issues:

```shell
export OTEL_JAVAAGENT_DEBUG=true
```

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's next?

Your Tomcat server is now instrumented with OpenTelemetry for comprehensive monitoring. Next steps:

- [Spring Boot instrumentation](/guides/opentelemetry-spring-boot) for Spring-based Tomcat applications
- [Quarkus instrumentation](/guides/opentelemetry-quarkus) for an alternative Java framework
- [Docker deployment](/guides/opentelemetry-docker) for containerized Tomcat applications
- [OpenTelemetry Java guide](/get/opentelemetry-java) for deeper instrumentation options
