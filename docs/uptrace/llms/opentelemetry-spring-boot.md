# Source: https://uptrace.dev/raw/guides/opentelemetry-spring-boot.md

# OpenTelemetry for Spring Boot: Guide with Examples

> Master OpenTelemetry Spring Boot integration with step-by-step setup, manual instrumentation examples, troubleshooting, and production-ready configurations. Learn spring opentelemetry best practices.

Monitoring distributed Spring Boot applications requires robust [observability tools](/tools/top-observability-tools). This guide shows you how to implement [OpenTelemetry](/opentelemetry) for Spring Boot integration, covering automatic instrumentation, manual instrumentation examples, and production deployment strategies.

## Choose Your Instrumentation Option

Spring Boot offers two main options for OpenTelemetry integration:

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Java Agent
    </th>
    
    <th>
      Spring Boot Starter
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Setup Complexity
      </strong>
    </td>
    
    <td>
      Minimal (JAR + env vars)
    </td>
    
    <td>
      Moderate (dependencies + config)
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Code Changes
      </strong>
    </td>
    
    <td>
      None required
    </td>
    
    <td>
      Minimal (configuration)
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Auto-Instrumentation
      </strong>
    </td>
    
    <td>
      150+ libraries
    </td>
    
    <td>
      Common Spring libraries
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Startup Overhead
      </strong>
    </td>
    
    <td>
      100-300ms
    </td>
    
    <td>
      50-100ms
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Memory Footprint
      </strong>
    </td>
    
    <td>
      +50-100MB
    </td>
    
    <td>
      +20-40MB
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Native Image Support
      </strong>
    </td>
    
    <td>
      Not supported
    </td>
    
    <td>
      Fully supported
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Configuration
      </strong>
    </td>
    
    <td>
      Env vars / system props
    </td>
    
    <td>
      Spring application.yml
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Best For
      </strong>
    </td>
    
    <td>
      Quick POC, existing apps
    </td>
    
    <td>
      Spring Boot 3, Native Image, Fine-grained control
    </td>
  </tr>
</tbody>
</table>

**Recommendation:**

- **Use Java Agent** for quickest setup with zero code changes and maximum auto-instrumentation coverage
- **Use Spring Boot Starter** for GraalVM Native Image, Spring-native configuration, or fine-grained control

For detailed Java Agent setup, see [OpenTelemetry Java Agent for Spring Boot](/blog/opentelemetry-java-agent-spring-boot). For other Java instrumentation options, see the [OpenTelemetry Java guide](/get/opentelemetry-java).

## Components of Spring OpenTelemetry

Spring OpenTelemetry provides comprehensive observability through three pillars:

- **Distributed Traces**: Complete request flows across microservices with [context propagation](/opentelemetry/context-propagation)
- **Application Metrics**: Performance indicators, latency histograms, and business KPIs
- **Structured Logs**: Contextual events with automatic trace correlation

### OpenTelemetry vs Micrometer in Spring

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      OpenTelemetry
    </th>
    
    <th>
      Micrometer
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Scope
      </strong>
    </td>
    
    <td>
      Traces, Metrics, Logs
    </td>
    
    <td>
      Primarily Metrics
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Distributed Tracing
      </strong>
    </td>
    
    <td>
      Full W3C standard support
    </td>
    
    <td>
      Limited capabilities
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Backend Support
      </strong>
    </td>
    
    <td>
      Any OTLP-compatible system
    </td>
    
    <td>
      Vendor-specific
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Spring Integration
      </strong>
    </td>
    
    <td>
      Auto + Manual instrumentation
    </td>
    
    <td>
      Native Spring Boot
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Semantic Conventions
      </strong>
    </td>
    
    <td>
      Standardized attributes
    </td>
    
    <td>
      Custom naming
    </td>
  </tr>
</tbody>
</table>

For a detailed comparison, see [OpenTelemetry vs Micrometer](/comparisons/opentelemetry-vs-micrometer).

<alert type="info">

**Quick Start**: For fastest setup without code changes, see the [Java zero-code instrumentation guide](/get/opentelemetry-java/zero-code).

</alert>

## Step-by-Step Spring Implementation

### Option 1: Java Agent (Recommended)

**Best for**: Quick setup with zero code changes

The OpenTelemetry Java Agent provides automatic instrumentation for 150+ libraries including Spring MVC, WebFlux, JDBC, JPA, Kafka, and HTTP clients.

**Step 1: Download the agent**

```bash
curl -L -O https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar
```

**Step 2: Configure environment**

```bash
export OTEL_SERVICE_NAME=spring-app
export OTEL_SERVICE_VERSION=1.0.0
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.uptrace.dev:4317
export OTEL_EXPORTER_OTLP_HEADERS=uptrace-dsn=<your_uptrace_dsn>
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip
```

**Step 3: Run with instrumentation**

```bash
java -javaagent:opentelemetry-javaagent.jar -jar your-spring-app.jar
```

For detailed configuration options and advanced usage, see [OpenTelemetry Java Agent for Spring Boot](/blog/opentelemetry-java-agent-spring-boot).

### Option 2: Spring Boot Starter

**Best for**: GraalVM Native Image, Spring-native configuration, and fine-grained control

The Spring Boot Starter integrates with Spring's auto-configuration system and supports Native Image compilation.

**Dependencies:**

Use the OpenTelemetry BOM (Bill of Materials) for consistent version management:

<code-group>

```xml [Maven]
<dependencyManagement>
    <dependencies>
        <!-- Import OTel BOM BEFORE spring-boot-dependencies -->
        <dependency>
            <groupId>io.opentelemetry.instrumentation</groupId>
            <artifactId>opentelemetry-instrumentation-bom</artifactId>
            <version>2.11.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>io.opentelemetry.instrumentation</groupId>
        <artifactId>opentelemetry-spring-boot-starter</artifactId>
    </dependency>
</dependencies>
```

```gradle [Gradle]
dependencies {
    implementation platform('io.opentelemetry.instrumentation:opentelemetry-instrumentation-bom:2.11.0')
    implementation 'io.opentelemetry.instrumentation:opentelemetry-spring-boot-starter'
}
```

</code-group>

**Configuration (application.yml):**

```yaml
spring:
  application:
    name: spring-app

otel:
  exporter:
    otlp:
      protocol: grpc
      endpoint: https://api.uptrace.dev:4317
      headers:
        uptrace-dsn: <your_uptrace_dsn>
      compression: gzip
  resource:
    attributes:
      service.version: 1.0.0
      deployment.environment: production
```

**Configuration (application.properties):**

```properties
spring.application.name=spring-app
otel.exporter.otlp.protocol=grpc
otel.exporter.otlp.endpoint=https://api.uptrace.dev:4317
otel.exporter.otlp.headers.uptrace-dsn=<your_uptrace_dsn>
otel.exporter.otlp.compression=gzip
otel.resource.attributes.service.version=1.0.0
otel.resource.attributes.deployment.environment=production
```

### Out-of-the-Box Instrumentation

The Spring Boot Starter automatically instruments common Spring components:

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Configuration Property
    </th>
    
    <th>
      Default
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      JDBC
    </td>
    
    <td>
      <code>
        otel.instrumentation.jdbc.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Spring Web
    </td>
    
    <td>
      <code>
        otel.instrumentation.spring-web.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Spring WebMVC
    </td>
    
    <td>
      <code>
        otel.instrumentation.spring-webmvc.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Spring WebFlux
    </td>
    
    <td>
      <code>
        otel.instrumentation.spring-webflux.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      R2DBC (Reactive)
    </td>
    
    <td>
      <code>
        otel.instrumentation.r2dbc.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Kafka
    </td>
    
    <td>
      <code>
        otel.instrumentation.kafka.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      MongoDB
    </td>
    
    <td>
      <code>
        otel.instrumentation.mongo.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Logback Appender
    </td>
    
    <td>
      <code>
        otel.instrumentation.logback-appender.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Logback MDC
    </td>
    
    <td>
      <code>
        otel.instrumentation.logback-mdc.enabled
      </code>
    </td>
    
    <td>
      true
    </td>
  </tr>
  
  <tr>
    <td>
      Micrometer
    </td>
    
    <td>
      <code>
        otel.instrumentation.micrometer.enabled
      </code>
    </td>
    
    <td>
      false
    </td>
  </tr>
</tbody>
</table>

### Service Name Configuration

The service name is determined in this order of precedence:

1. `otel.service.name` property or `OTEL_SERVICE_NAME` env var
2. `service.name` in `otel.resource.attributes`
3. `spring.application.name` property
4. `build-info.properties` (generated by Spring Boot Maven/Gradle plugin)
5. Default: `unknown_service:java`

To automatically use your project name, add the build-info goal:

<code-group>

```xml [Maven]
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <executions>
        <execution>
            <goals>
                <goal>build-info</goal>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

```gradle [Gradle]
springBoot {
    buildInfo()
}
```

</code-group>

### SDK Configuration Options

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        otel.exporter.otlp.endpoint
      </code>
    </td>
    
    <td>
      OTLP endpoint URL
    </td>
    
    <td>
      <code>
        http://localhost:4318
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.exporter.otlp.protocol
      </code>
    </td>
    
    <td>
      Protocol (<code>
        grpc
      </code>
      
       or <code>
        http/protobuf
      </code>
      
      )
    </td>
    
    <td>
      <code>
        http/protobuf
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.exporter.otlp.headers.*
      </code>
    </td>
    
    <td>
      Custom headers for authentication
    </td>
    
    <td>
      -
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.exporter.otlp.compression
      </code>
    </td>
    
    <td>
      Compression (<code>
        gzip
      </code>
      
       or <code>
        none
      </code>
      
      )
    </td>
    
    <td>
      <code>
        none
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.traces.exporter
      </code>
    </td>
    
    <td>
      Traces exporter (<code>
        otlp
      </code>
      
      , <code>
        logging
      </code>
      
      , <code>
        none
      </code>
      
      )
    </td>
    
    <td>
      <code>
        otlp
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.metrics.exporter
      </code>
    </td>
    
    <td>
      Metrics exporter
    </td>
    
    <td>
      <code>
        otlp
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.logs.exporter
      </code>
    </td>
    
    <td>
      Logs exporter
    </td>
    
    <td>
      <code>
        otlp
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.propagators
      </code>
    </td>
    
    <td>
      Context propagators
    </td>
    
    <td>
      <code>
        tracecontext,baggage
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        otel.sdk.disabled
      </code>
    </td>
    
    <td>
      Disable OpenTelemetry (for testing)
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
</tbody>
</table>

### GraalVM Native Image Support

The Spring Boot Starter fully supports GraalVM Native Image compilation, making it the preferred choice for native applications:

<code-group>

```xml [Maven]
<build>
    <plugins>
        <plugin>
            <groupId>org.graalvm.buildtools</groupId>
            <artifactId>native-maven-plugin</artifactId>
        </plugin>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

```gradle [Gradle]
plugins {
    id 'org.graalvm.buildtools.native' version '0.10.4'
    id 'org.springframework.boot' version '3.4.1'
}
```

</code-group>

Build and run the native image:

```bash
# Maven
./mvnw -Pnative native:compile
./target/your-app

# Gradle
./gradlew nativeCompile
./build/native/nativeCompile/your-app
```

Native images start in milliseconds and have significantly lower memory footprint compared to JVM-based deployments.

## Spring WebFlux (Reactive) Support

Both the Java Agent and Spring Boot Starter provide full support for Spring WebFlux reactive applications.

### Reactive Controller Example

```java
@RestController
@RequestMapping("/api/orders")
public class ReactiveOrderController {

    private final OrderService orderService;

    @GetMapping("/{id}")
    public Mono<Order> getOrder(@PathVariable String id) {
        // Automatically instrumented - spans propagate through reactive chain
        return orderService.findById(id)
            .doOnSuccess(order -> log.info("Found order: {}", order.getId()));
    }

    @GetMapping("/stream")
    public Flux<Order> streamOrders() {
        // Streaming endpoint also instrumented
        return orderService.streamAllOrders();
    }
}
```

### WebClient Instrumentation

Outbound HTTP calls with WebClient are automatically traced:

```java
@Service
public class PaymentClient {

    private final WebClient webClient;

    public PaymentClient(WebClient.Builder builder) {
        this.webClient = builder
            .baseUrl("https://payment-service")
            .build();
    }

    public Mono<PaymentResult> processPayment(Payment payment) {
        // Trace context automatically propagated to downstream service
        return webClient.post()
            .uri("/api/payments")
            .bodyValue(payment)
            .retrieve()
            .bodyToMono(PaymentResult.class);
    }
}
```

## Annotation-Based Instrumentation

The Spring Boot Starter supports `@WithSpan` and `@SpanAttribute` annotations for declarative instrumentation without manual span management.

### Setup

Add the Spring AOP dependency:

<code-group>

```xml [Maven]
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
```

```gradle [Gradle]
implementation 'org.springframework.boot:spring-boot-starter-aop'
```

</code-group>

### @WithSpan Annotation

Automatically wrap methods in spans:

```java
import io.opentelemetry.instrumentation.annotations.WithSpan;
import io.opentelemetry.instrumentation.annotations.SpanAttribute;
import io.opentelemetry.api.trace.SpanKind;

@Service
public class OrderService {

    @WithSpan
    public Order processOrder(String orderId) {
        // Creates span named "OrderService.processOrder"
        return doProcess(orderId);
    }

    @WithSpan("custom-operation-name")
    public void customNamedOperation() {
        // Creates span with custom name
    }

    @WithSpan(kind = SpanKind.CLIENT)
    public ExternalResult callExternalService() {
        // Creates CLIENT span for external calls
    }

    @WithSpan
    public Order findOrder(
            @SpanAttribute("order.id") String orderId,
            @SpanAttribute("customer.id") String customerId) {
        // Captures method parameters as span attributes
        return repository.find(orderId);
    }
}
```

**Important limitations:**

- Annotations only work on Spring-proxied beans
- Internal method calls within the same class are not instrumented
- Disable with: `otel.instrumentation.annotations.enabled=false`

### Programmatic Configuration

For advanced customization, use `AutoConfigurationCustomizerProvider` beans:

```java
import io.opentelemetry.sdk.autoconfigure.spi.AutoConfigurationCustomizerProvider;
import io.opentelemetry.semconv.UrlAttributes;
import io.opentelemetry.contrib.sampler.RuleBasedRoutingSampler;
import io.opentelemetry.api.trace.SpanKind;

@Configuration
public class OtelConfiguration {

    @Bean
    public AutoConfigurationCustomizerProvider otelCustomizer() {
        return p -> p.addSamplerCustomizer((sampler, config) ->
            RuleBasedRoutingSampler.builder(SpanKind.SERVER, sampler)
                .drop(UrlAttributes.URL_PATH, "^/actuator")
                .drop(UrlAttributes.URL_PATH, "^/health")
                .build()
        );
    }
}
```

This example filters out health check endpoints from tracing.

## Logging Integration

OpenTelemetry provides automatic log correlation with traces. The Spring Boot Starter automatically configures Logback integration without requiring manual `logback.xml` changes.

### Automatic Configuration (Spring Boot Starter)

When using the Spring Boot Starter, logging instrumentation is enabled by default:

- **Logback Appender**: Exports logs via OTLP (`otel.instrumentation.logback-appender.enabled=true`)
- **MDC Injection**: Adds trace/span IDs to MDC (`otel.instrumentation.logback-mdc.enabled=true`)

Configure experimental features via application properties:

```properties
# Capture thread name and ID
otel.instrumentation.logback-appender.experimental-log-attributes=true

# Capture source code location (may add overhead)
otel.instrumentation.logback-appender.experimental.capture-code-attributes=true

# Capture all MDC attributes
otel.instrumentation.logback-appender.experimental.capture-mdc-attributes=*
```

### Custom Logback Configuration

For more control, configure manually in `logback-spring.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} trace_id=%X{trace_id} span_id=%X{span_id} - %msg%n</pattern>
    </encoder>
  </appender>

  <appender name="OpenTelemetry"
      class="io.opentelemetry.instrumentation.logback.appender.v1_0.OpenTelemetryAppender">
    <captureExperimentalAttributes>true</captureExperimentalAttributes>
    <captureCodeAttributes>true</captureCodeAttributes>
    <captureMdcAttributes>*</captureMdcAttributes>
  </appender>

  <root level="INFO">
    <appender-ref ref="console"/>
    <appender-ref ref="OpenTelemetry"/>
  </root>
</configuration>
```

For complete configuration options, see the [OpenTelemetry Logback guide](/guides/opentelemetry-logback).

### Log4j2 Configuration

For Log4j2, see the [OpenTelemetry Log4j guide](/guides/opentelemetry-log4j).

## Custom Instrumentation for Business Telemetry

For comprehensive manual instrumentation patterns with complete working examples, see [OpenTelemetry Java Manual Instrumentation](/blog/opentelemetry-java-manual-instrumentation).

### Custom Trace Implementation

This example shows how to create custom spans that capture business-specific context and operations:

```java
@Service
public class OrderProcessingService {

    private final Tracer tracer;

    public OrderProcessingService(OpenTelemetry openTelemetry) {
        this.tracer = openTelemetry.getTracer("com.example.orders", "1.0.0");
    }

    public OrderResult processOrder(OrderRequest request) {
        Span orderSpan = tracer.spanBuilder("process-order")
            .setAttribute("order.id", request.getOrderId())
            .setAttribute("customer.id", request.getCustomerId())
            .setAttribute("order.amount", request.getTotalAmount())
            .startSpan();

        try (Scope scope = orderSpan.makeCurrent()) {
            // Business logic with automatic context propagation
            validateOrder(request);
            orderSpan.addEvent("order.validated");

            PaymentResult payment = processPayment(request);
            orderSpan.setAttribute("payment.status", payment.getStatus());

            OrderResult result = finalizeOrder(request);
            orderSpan.setStatus(StatusCode.OK);

            return result;
        } catch (Exception e) {
            orderSpan.setStatus(StatusCode.ERROR, e.getMessage());
            orderSpan.recordException(e);
            throw e;
        } finally {
            orderSpan.end();
        }
    }
}
```

### Business Metrics Collection

Use this pattern to capture custom business metrics that provide insights into your application's performance and user behavior:

```java
@Component
public class BusinessMetricsCollector {

    private final LongCounter orderCounter;
    private final DoubleHistogram orderValueHistogram;

    public BusinessMetricsCollector(OpenTelemetry openTelemetry) {
        Meter meter = openTelemetry.getMeter("com.example.business", "1.0.0");

        orderCounter = meter.counterBuilder("orders.processed.total")
            .setDescription("Total orders processed")
            .build();

        orderValueHistogram = meter.histogramBuilder("order.value")
            .setDescription("Order value distribution")
            .setUnit("USD")
            .build();
    }

    public void recordOrder(String type, String status, double value) {
        orderCounter.add(1, Attributes.of(
            AttributeKey.stringKey("order.type"), type,
            AttributeKey.stringKey("order.status"), status
        ));

        orderValueHistogram.record(value, Attributes.of(
            AttributeKey.stringKey("order.type"), type
        ));
    }
}
```

### Enhanced Controller Instrumentation

Here's how to enrich your REST controllers with additional telemetry context and business metrics:

```java
@RestController
@RequestMapping("/api/orders")
public class OrderController {

    private final OrderProcessingService orderService;
    private final BusinessMetricsCollector metricsCollector;

    @PostMapping
    public ResponseEntity<OrderResponse> createOrder(@RequestBody OrderRequest request) {
        // Current span enrichment
        Span currentSpan = Span.current();
        currentSpan.setAttribute("order.items.count", request.getItems().size());
        currentSpan.setAttribute("customer.region", request.getCustomerRegion());

        try {
            OrderResult result = orderService.processOrder(request);

            // Record business metrics
            metricsCollector.recordOrder(
                request.getOrderType(),
                result.getStatus(),
                request.getTotalAmount()
            );

            currentSpan.setStatus(StatusCode.OK);
            return ResponseEntity.ok(new OrderResponse(result.getOrderId()));

        } catch (OrderValidationException e) {
            currentSpan.setStatus(StatusCode.ERROR, "Validation failed");
            return ResponseEntity.badRequest()
                .body(new ErrorResponse("VALIDATION_ERROR", e.getMessage()));
        }
    }
}
```

## OpenTelemetry Collector Setup

The [OpenTelemetry Collector](/opentelemetry/collector) acts as a vendor-agnostic proxy between your Spring Boot applications and your observability backend, providing buffering, batching, and data transformation.

### Basic Configuration

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 1000
  memory_limiter:
    check_interval: 1s
    limit_mib: 1000
    spike_limit_mib: 200

exporters:
  otlp:
    endpoint: https://api.uptrace.dev:4317
    headers:
      uptrace-dsn: ${UPTRACE_DSN}
    compression: gzip

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlp]
    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlp]
```

### Kubernetes Deployment

Deploy your Spring Boot application with the collector in Kubernetes:

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-app
spec:
  template:
    spec:
      containers:
        - name: spring-app
          image: your-spring-app:latest
          env:
            - name: OTEL_SERVICE_NAME
              value: spring-app
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: http://otel-collector:4317
            - name: OTEL_EXPORTER_OTLP_PROTOCOL
              value: grpc
            - name: OTEL_TRACES_SAMPLER
              value: parentbased_traceidratio
            - name: OTEL_TRACES_SAMPLER_ARG
              value: "0.1"
```

### Docker Compose Deployment

```yaml
# docker-compose.yml
services:
  spring-app:
    image: your-spring-app:latest
    environment:
      - OTEL_SERVICE_NAME=spring-app
      - OTEL_EXPORTER_OTLP_PROTOCOL=grpc
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
      - OTEL_TRACES_SAMPLER=parentbased_traceidratio
      - OTEL_TRACES_SAMPLER_ARG=0.1
    depends_on:
      - otel-collector

  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    command: ["--config=/etc/otel-collector-config.yaml"]
    environment:
      - UPTRACE_DSN=${UPTRACE_DSN}
    volumes:
      - ./otel-collector-config.yaml:/etc/otel-collector-config.yaml
    ports:
      - "4317:4317"
      - "4318:4318"
```

## Troubleshooting

### No Telemetry Data

**Symptoms**: Application runs but no traces appear in backend

**Diagnosis:**

```bash
# Enable debug logging for Java Agent
export OTEL_JAVAAGENT_DEBUG=true

# For Spring Boot Starter, add to application.properties
logging.level.io.opentelemetry=DEBUG

# Check connectivity to collector
curl -v http://your-collector:4318/v1/traces
```

**Common causes and solutions:**

1. **Wrong endpoint URL**: Ensure the endpoint matches your collector configuration
2. **Protocol mismatch**: Default changed to `http/protobuf` in recent versions
3. **Missing headers**: Check authentication headers are set correctly

```yaml
otel:
  exporter:
    otlp:
      endpoint: http://collector:4318
      protocol: http/protobuf
```

### Broken Trace Propagation

**Symptoms**: Disconnected spans across services, missing parent-child relationships

**Diagnosis:**

```java
@GetMapping("/debug/trace")
public Map<String, String> debugTrace(HttpServletRequest request) {
    Map<String, String> headers = new HashMap<>();
    headers.put("traceparent", request.getHeader("traceparent"));
    headers.put("current-trace-id", Span.current().getSpanContext().getTraceId());
    headers.put("current-span-id", Span.current().getSpanContext().getSpanId());
    return headers;
}
```

**Common causes:**

1. **Missing propagator configuration**: Ensure W3C Trace Context is enabled
2. **HTTP client not instrumented**: Check RestTemplate/WebClient are auto-instrumented
3. **Async operations**: Context may not propagate across thread boundaries

**Solution for custom propagation:**

```java
@Bean
public TextMapPropagator textMapPropagator() {
    return TextMapPropagator.composite(
        W3CTraceContextPropagator.getInstance(),
        W3CBaggagePropagator.getInstance()
    );
}
```

### High Memory Usage

**Symptoms**: Increasing heap usage, frequent GC, OutOfMemoryError

**Solutions:**

```bash
# Reduce batch queue size
export OTEL_BSP_MAX_QUEUE_SIZE=1024
export OTEL_BSP_MAX_EXPORT_BATCH_SIZE=256
export OTEL_BSP_SCHEDULE_DELAY=2000

# Implement sampling to reduce trace volume
export OTEL_TRACES_SAMPLER=parentbased_traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.1

# Disable unused instrumentations
export OTEL_INSTRUMENTATION_SPRING_SCHEDULING_ENABLED=false
```

### Slow Application Startup

**Symptoms**: Application takes longer to start with Java Agent

**Solutions:**

1. **Use Spring Boot Starter** instead of Java Agent for faster startup
2. **Disable unused instrumentations**:

```bash
export OTEL_INSTRUMENTATION_COMMON_DEFAULT_ENABLED=false
export OTEL_INSTRUMENTATION_SPRING_WEBMVC_ENABLED=true
export OTEL_INSTRUMENTATION_JDBC_ENABLED=true
```

1. **For Native Image**, use Spring Boot Starter (Java Agent not supported)

### Connection Timeouts

**Symptoms**: "Failed to export spans" errors in logs

**Solutions:**

```bash
# Increase timeout
export OTEL_EXPORTER_OTLP_TIMEOUT=30000

# Enable compression
export OTEL_EXPORTER_OTLP_COMPRESSION=gzip

# Use async exporter
export OTEL_BSP_SCHEDULE_DELAY=5000
```

## Performance and Resource Impact

### Performance Impact Analysis

<table>
<thead>
  <tr>
    <th>
      Component
    </th>
    
    <th>
      Overhead
    </th>
    
    <th>
      Mitigation
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        CPU Usage
      </strong>
    </td>
    
    <td>
      3-8%
    </td>
    
    <td>
      Optimize sampling rates
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Memory
      </strong>
    </td>
    
    <td>
      10-15%
    </td>
    
    <td>
      Configure buffer limits
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Network
      </strong>
    </td>
    
    <td>
      5-10KB/request
    </td>
    
    <td>
      Enable compression
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Latency
      </strong>
    </td>
    
    <td>
      1-5ms/request
    </td>
    
    <td>
      Use async exporters
    </td>
  </tr>
</tbody>
</table>

### Production Optimization

These environment variables help optimize OpenTelemetry performance for high-traffic production environments:

```bash
# JVM optimization
export JAVA_OPTS="-XX:+UseG1GC -Xms2g -Xmx4g"

# OpenTelemetry performance tuning
export OTEL_BSP_SCHEDULE_DELAY=5000
export OTEL_BSP_MAX_EXPORT_BATCH_SIZE=512
export OTEL_TRACES_SAMPLER_ARG=0.1

# Disable unnecessary instrumentation
export OTEL_INSTRUMENTATION_LOGBACK_APPENDER_ENABLED=false
```

## Best Practices

### Environment-Specific Configurations

**Development:**

```yaml
otel:
  traces:
    sampler: parentbased_always_on  # Full sampling
  exporter:
    otlp:
      protocol: grpc
      endpoint: http://localhost:4317
```

**Production:**

```yaml
otel:
  traces:
    sampler: parentbased_traceidratio
    sampler.arg: 0.1  # Controlled sampling
  exporter:
    otlp:
      protocol: grpc
      endpoint: https://prod-collector:4317
      compression: gzip
```

### Monitoring Strategy

1. **Start Simple**: Begin with Java Agent for immediate results
2. **Add Context**: Implement custom instrumentation for business insights
3. **Optimize Gradually**: Fine-tune sampling and performance settings
4. **Monitor Impact**: Track OpenTelemetry's resource usage
5. **Scale Appropriately**: Adjust configuration based on traffic patterns

## What is Uptrace?

Uptrace is an [OpenTelemetry APM](/opentelemetry/apm) that supports distributed tracing, metrics, and logs. You can use it to monitor applications and troubleshoot issues.

![Uptrace Overview](/home/screenshots/apm.png)

Uptrace comes with an intuitive query builder, rich dashboards, alerting rules with notifications, and integrations for most languages and frameworks.

Uptrace can process billions of spans and metrics on a single server and allows you to monitor your applications at 10x lower cost.

In just a few minutes, you can try Uptrace by visiting the [cloud demo](https://play.uptrace.dev/) (no login required) or running it locally with [Docker](/get/hosted/docker). The source code is available on [GitHub](https://github.com/uptrace/uptrace).

## What's Next?

OpenTelemetry Spring Boot integration provides comprehensive observability for your Java applications. Here are recommended next steps:

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
      Use zero-code instrumentation
    </td>
    
    <td>
      <a href="/blog/opentelemetry-java-agent-spring-boot">
        Java Agent for Spring Boot
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Add custom spans and metrics
    </td>
    
    <td>
      <a href="/blog/opentelemetry-java-manual-instrumentation">
        Manual Instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Configure log correlation
    </td>
    
    <td>
      <a href="/guides/opentelemetry-logback">
        Logback integration
      </a>
      
       or <a href="/guides/opentelemetry-log4j">
        Log4j integration
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Monitor Tomcat containers
    </td>
    
    <td>
      <a href="/guides/opentelemetry-tomcat">
        Tomcat instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Compare with Micrometer
    </td>
    
    <td>
      <a href="/comparisons/opentelemetry-vs-micrometer">
        OpenTelemetry vs Micrometer
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Understand sampling
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/sampling">
        Sampling strategies
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Configure context propagation
    </td>
    
    <td>
      <a href="/get/opentelemetry-java/propagation">
        Context propagation
      </a>
    </td>
  </tr>
</tbody>
</table>

### Related Guides

- [OpenTelemetry Java guide](/get/opentelemetry-java) - Core Java SDK documentation
- [OpenTelemetry Quarkus](/guides/opentelemetry-quarkus) - Quarkus instrumentation with native image support
- [Spring Boot Microservices Monitoring](/blog/spring-boot-microservices-monitoring) - Monitoring patterns for microservices
- [OpenTelemetry Collector](/opentelemetry/collector) - Collector configuration and deployment

### External Resources

- [OpenTelemetry Java Instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation)
- [Spring Boot Starter Documentation](https://opentelemetry.io/docs/zero-code/java/spring-boot-starter/)
- [Supported Libraries List](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md)
