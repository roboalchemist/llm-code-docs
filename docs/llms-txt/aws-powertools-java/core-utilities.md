# Core Utilities

Logging provides an opinionated logger with output structured as JSON.

**Key features**

- Capture key fields from Lambda context, cold start and structures logging output as JSON
- Log Lambda event when instructed, disabled by default, can be enabled explicitly via annotation param
- Append additional keys to structured log at any point in time

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-logging</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-logging</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-logging</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-logging</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-logging:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-logging:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Initialization

Powertools for AWS Lambda (Java) extends the functionality of Log4J. Below is an example `log4j2.xml` file, with the `JsonTemplateLayout` using `LambdaJsonLayout.json` configured.

LambdaJsonLayout is now deprecated

Configuring utility using `<LambdaJsonLayout/>` plugin is deprecated now. While utility still supports the old configuration, we strongly recommend upgrading the `log4j2.xml` configuration to `JsonTemplateLayout` instead. [JsonTemplateLayout](https://logging.apache.org/log4j/2.x/manual/json-template-layout.html) is recommended way of doing structured logging.

Please follow [this guide](#upgrade-to-jsontemplatelayout-from-deprecated-lambdajsonlayout-configuration-in-log4j2xml) for upgrade steps.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:LambdaJsonLayout.json" />
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

You can also override log level by setting **`POWERTOOLS_LOG_LEVEL`** env var. Here is an example using AWS Serverless Application Model (SAM)

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11
        Environment:
            Variables:
                POWERTOOLS_LOG_LEVEL: DEBUG
                POWERTOOLS_SERVICE_NAME: example

```

You can also explicitly set a service name via **`POWERTOOLS_SERVICE_NAME`** env var. This sets **service** key that will be present across all log statements.

## Standard structured keys

Your logs will always include the following keys to your structured logging:

| Key | Type | Example | Description | | --- | --- | --- | --- | | **timestamp** | String | "2020-05-24 18:17:33,774" | Timestamp of actual log statement | | **level** | String | "INFO" | Logging level | | **coldStart** | Boolean | true | ColdStart value. | | **service** | String | "payment" | Service name defined. "service_undefined" will be used if unknown | | **samplingRate** | int | 0.1 | Debug logging sampling rate in percentage e.g. 10% in this case | | **message** | String | "Collecting payment" | Log statement value. Unserializable JSON values will be casted to string | | **functionName** | String | "example-powertools-HelloWorldFunction-1P1Z6B39FLU73" | | | **functionVersion** | String | "12" | | | **functionMemorySize** | String | "128" | | | **functionArn** | String | "arn:aws:lambda:eu-west-1:012345678910:function:example-powertools-HelloWorldFunction-1P1Z6B39FLU73" | | | **xray_trace_id** | String | "1-5759e988-bd862e3fe1be46a994272793" | X-Ray Trace ID when Lambda function has enabled Tracing | | **function_request_id** | String | "899856cb-83d1-40d7-8611-9e78f15f32f4"" | AWS Request ID from lambda context |

## Capturing context Lambda info

When debugging in non-production environments, you can instruct Logger to log the incoming event with `@Logger(logEvent = true)` or via `POWERTOOLS_LOGGER_LOG_EVENT=true` environment variable.

Warning

Log event is disabled by default to prevent sensitive info being logged.

```
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import software.amazon.lambda.powertools.logging.LoggingUtils;
import software.amazon.lambda.powertools.logging.Logging;
...

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
     ...
    }
}

```

```
/**
 * Handler for requests to Lambda function.
 */
public class AppLogEvent implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(AppLogEvent.class);

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
     ...
    }
}

```

### Customising fields in logs

- Utility by default emits `timestamp` field in the logs in format `yyyy-MM-dd'T'HH:mm:ss.SSSZz` and in system default timezone. If you need to customize format and timezone, you can do so by configuring `log4j2.component.properties` and configuring properties as shown in example below:

```
log4j.layout.jsonTemplate.timestampFormatPattern=yyyy-MM-dd'T'HH:mm:ss.SSSZz
log4j.layout.jsonTemplate.timeZone=Europe/Oslo

```

- Utility also provides sample template for [Elastic Common Schema(ECS)](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) layout. The field emitted in logs will follow specs from [ECS](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) together with field captured by utility as mentioned [above](#standard-structured-keys).

  Use `LambdaEcsLayout.json` as `eventTemplateUri` when configuring `JsonTemplateLayout`.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:LambdaEcsLayout.json" />
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

## Setting a Correlation ID

You can set a Correlation ID using `correlationIdPath` attribute by passing a [JSON Pointer expression](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-json-pointer-03).

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(correlationIdPath = "/headers/my_request_id_header")
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        log.info("Collecting payment")
        ...
    }
}

```

```
{
  "headers": {
    "my_request_id_header": "correlation_id_value"
  }
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72",
    "correlation_id": "correlation_id_value"
}

```

We provide [built-in JSON Pointer expression](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-json-pointer-03) for known event sources, where either a request ID or X-Ray Trace ID are present.

```
import software.amazon.lambda.powertools.logging.CorrelationIdPathConstants;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(correlationIdPath = CorrelationIdPathConstants.API_GATEWAY_REST)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        log.info("Collecting payment")
        ...
    }
}

```

```
{
  "requestContext": {
    "requestId": "correlation_id_value"
  }
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72",
    "correlation_id": "correlation_id_value"
}

```

## Appending additional keys

Custom keys are persisted across warm invocations

```
Always set additional keys as part of your handler to ensure they have the latest value, or explicitly clear them with [`clearState=true`](#clearing-all-state).

```

You can append your own keys to your existing logs via `appendKey`.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        LoggingUtils.appendKey("test", "willBeLogged");
        ...

        ...
         Map<String, String> customKeys = new HashMap<>();
         customKeys.put("test", "value");
         customKeys.put("test1", "value1");

         LoggingUtils.appendKeys(customKeys);
        ...
    }
}

```

### Removing additional keys

You can remove any additional key from entry using `LoggingUtils.removeKeys()`.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        LoggingUtils.appendKey("test", "willBeLogged");
        ...
        Map<String, String> customKeys = new HashMap<>();
        customKeys.put("test1", "value");
        customKeys.put("test2", "value1");

        LoggingUtils.appendKeys(customKeys);
        ...
        LoggingUtils.removeKey("test");
        LoggingUtils.removeKeys("test1", "test2");
        ...
    }
}

```

### Clearing all state

Logger is commonly initialized in the global scope. Due to [Lambda Execution Context reuse](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html), this means that custom keys can be persisted across invocations. If you want all custom keys to be deleted, you can use `clearState=true` attribute on `@Logging` annotation.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(clearState = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        if(input.getHeaders().get("someSpecialHeader")) {
            LoggingUtils.appendKey("specialKey", "value");
        }

        log.info("Collecting payment");
        ...
    }
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72",
    "specialKey": "value"
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72"
}

```

## Override default object mapper

You can optionally choose to override default object mapper which is used to serialize lambda function events. You might want to supply custom object mapper in order to control how serialisation is done, for example, when you want to log only specific fields from received event due to security.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    static {
        ObjectMapper objectMapper = new ObjectMapper();
        LoggingUtils.defaultObjectMapper(objectMapper);
    }

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
    }
}

```

## Sampling debug logs

You can dynamically set a percentage of your logs to **DEBUG** level via env var `POWERTOOLS_LOGGER_SAMPLE_RATE` or via `samplingRate` attribute on annotation.

Info

Configuration on environment variable is given precedence over sampling rate configuration on annotation, provided it's in valid value range.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(samplingRate = 0.5)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
     ...
    }
}

```

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11
        Environment:
            Variables:
                POWERTOOLS_LOGGER_SAMPLE_RATE: 0.5

```

## AWS Lambda Advanced Logging Controls (ALC)

When is it useful?

When you want to set a logging policy to drop informational or verbose logs for one or all AWS Lambda functions, regardless of runtime and logger used.

With [AWS Lambda Advanced Logging Controls (ALC)](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-advanced), you can enforce a minimum log level that Lambda will accept from your application code.

When enabled, you should keep `Logger` and ALC log level in sync to avoid data loss.

Here's a sequence diagram to demonstrate how ALC will drop both `INFO` and `DEBUG` logs emitted from `Logger`, when ALC log level is stricter than `Logger`.

```
sequenceDiagram
    participant Lambda service
    participant Lambda function
    participant Application Logger

    Note over Lambda service: AWS_LAMBDA_LOG_LEVEL="WARN"
    Note over Application Logger: POWERTOOLS_LOG_LEVEL="DEBUG"

    Lambda service->>Lambda function: Invoke (event)
    Lambda function->>Lambda function: Calls handler
    Lambda function->>Application Logger: logger.error("Something happened")
    Lambda function-->>Application Logger: logger.debug("Something happened")
    Lambda function-->>Application Logger: logger.info("Something happened")
    Lambda service--xLambda service: DROP INFO and DEBUG logs
    Lambda service->>CloudWatch Logs: Ingest error logs
```

### Priority of log level settings in Powertools for AWS Lambda

We prioritise log level settings in this order:

1. `AWS_LAMBDA_LOG_LEVEL` environment variable
1. `POWERTOOLS_LOG_LEVEL` environment variable

If you set `Logger` level lower than ALC, we will emit a warning informing you that your messages will be discarded by Lambda.

> **NOTE**
>
> With ALC enabled, we are unable to increase the minimum log level below the `AWS_LAMBDA_LOG_LEVEL` environment variable value, see [AWS Lambda service documentation](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-log-level) for more details.

### Timestamp format

When the Advanced Logging Controls feature is enabled, Powertools for AWS Lambda must comply with the timestamp format required by AWS Lambda, which is [RFC3339](https://www.rfc-editor.org/rfc/rfc3339). In this case the format will be `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.

## Upgrade to JsonTemplateLayout from deprecated LambdaJsonLayout configuration in log4j2.xml

Prior to version [1.10.0](https://github.com/aws-powertools/powertools-lambda-java/releases/tag/v1.10.0), only supported way of configuring `log4j2.xml` was via `<LambdaJsonLayout/>`. This plugin is deprecated now and will be removed in future version. Switching to `JsonTemplateLayout` is straight forward.

Below examples shows deprecated and new configuration of `log4j2.xml`.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <LambdaJsonLayout compact="true" eventEol="true"/>
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:LambdaJsonLayout.json" />
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

Metrics creates custom metrics asynchronously by logging metrics to standard output following Amazon CloudWatch Embedded Metric Format (EMF).

These metrics can be visualized through [Amazon CloudWatch Console](https://console.aws.amazon.com/cloudwatch/).

**Key features**

- Aggregate up to 100 metrics using a single CloudWatch EMF object (large JSON blob).
- Validate against common metric definitions mistakes (metric unit, values, max dimensions, max metrics, etc).
- Metrics are created asynchronously by the CloudWatch service, no custom stacks needed.
- Context manager to create a one off metric with a different dimension.

## Terminologies

If you're new to Amazon CloudWatch, there are two terminologies you must be aware of before using this utility:

- **Namespace**. It's the highest level container that will group multiple metrics from multiple services for a given application, for example `ServerlessEcommerce`.
- **Dimensions**. Metrics metadata in key-value format. They help you slice and dice metrics visualization, for example `ColdStart` metric by Payment `service`.

Metric terminology, visually explained

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-metrics</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-metrics</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-metrics</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-metrics</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-metrics:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-metrics:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Getting started

Metric has two global settings that will be used across all metrics emitted:

| Setting | Description | Environment variable | Constructor parameter | | --- | --- | --- | --- | | **Metric namespace** | Logical container where all metrics will be placed e.g. `ServerlessAirline` | `POWERTOOLS_METRICS_NAMESPACE` | `namespace` | | **Service** | Optionally, sets **service** metric dimension across all metrics e.g. `payment` | `POWERTOOLS_SERVICE_NAME` | `service` |

Use your application or main service as the metric namespace to easily group all metrics

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11
        Environment:
            Variables:
                POWERTOOLS_SERVICE_NAME: payment
                POWERTOOLS_METRICS_NAMESPACE: ServerlessAirline

```

```
import software.amazon.lambda.powertools.metrics.Metrics;

public class MetricsEnabledHandler implements RequestHandler<Object, Object> {

    MetricsLogger metricsLogger = MetricsUtils.metricsLogger();

    @Override
    @Metrics(namespace = "ExampleApplication", service = "booking")
    public Object handleRequest(Object input, Context context) {
        ...
    }
}

```

You can initialize Metrics anywhere in your code as many times as you need - It'll keep track of your aggregate metrics in memory.

## Creating metrics

You can create metrics using `putMetric`, and manually create dimensions for all your aggregate metrics using `putDimensions`.

```
import software.amazon.lambda.powertools.metrics.Metrics;
import software.amazon.cloudwatchlogs.emf.logger.MetricsLogger;

public class MetricsEnabledHandler implements RequestHandler<Object, Object> {

    MetricsLogger metricsLogger = MetricsUtils.metricsLogger();

    @Override
    @Metrics(namespace = "ExampleApplication", service = "booking")
    public Object handleRequest(Object input, Context context) {
        metricsLogger.putDimensions(DimensionSet.of("environment", "prod"));
        metricsLogger.putMetric("SuccessfulBooking", 1, Unit.COUNT);
        ...
    }
}

```

The `Unit` enum facilitate finding a supported metric unit by CloudWatch.

Metrics overflow

CloudWatch EMF supports a max of 100 metrics. Metrics utility will flush all metrics when adding the 100th metric while subsequent metrics will be aggregated into a new EMF object, for your convenience.

### Flushing metrics

The `@Metrics` annotation **validates**, **serializes**, and **flushes** all your metrics. During metrics validation, if no metrics are provided no exception will be raised. If metrics are provided, and any of the following criteria are not met, `ValidationException` exception will be raised.

Metric validation

- Maximum of 9 dimensions

If you want to ensure that at least one metric is emitted, you can pass `raiseOnEmptyMetrics = true` to the **@Metrics** annotation:

```
import software.amazon.lambda.powertools.metrics.Metrics;

public class MetricsRaiseOnEmpty implements RequestHandler<Object, Object> {

    @Override
    @Metrics(raiseOnEmptyMetrics = true)
    public Object handleRequest(Object input, Context context) {
    ...
    }
}

```

## Capturing cold start metric

You can capture cold start metrics automatically with `@Metrics` via the `captureColdStart` variable.

```
import software.amazon.lambda.powertools.metrics.Metrics;

public class MetricsColdStart implements RequestHandler<Object, Object> {

    @Override
    @Metrics(captureColdStart = true)
    public Object handleRequest(Object input, Context context) {
    ...
    }
}

```

If it's a cold start invocation, this feature will:

- Create a separate EMF blob solely containing a metric named `ColdStart`
- Add `FunctionName` and `Service` dimensions

This has the advantage of keeping cold start metric separate from your application metrics.

## Advanced

## Adding metadata

You can use `putMetadata` for advanced use cases, where you want to metadata as part of the serialized metrics object.

Info

**This will not be available during metrics visualization, use `dimensions` for this purpose.**

```
import software.amazon.lambda.powertools.metrics.Metrics;
import software.amazon.cloudwatchlogs.emf.logger.MetricsLogger;

public class App implements RequestHandler<Object, Object> {

    @Override
    @Metrics(namespace = "ServerlessAirline", service = "payment")
    public Object handleRequest(Object input, Context context) {
        metricsLogger().putMetric("CustomMetric1", 1, Unit.COUNT);
        metricsLogger().putMetadata("booking_id", "1234567890");
        ...
    }
}

```

This will be available in CloudWatch Logs to ease operations on high cardinal data.

## Overriding default dimension set

By default, all metrics emitted via module captures `Service` as one of the default dimension. This is either specified via `POWERTOOLS_SERVICE_NAME` environment variable or via `service` attribute on `Metrics` annotation. If you wish to override the default Dimension, it can be done via `MetricsUtils.defaultDimensions()`.

```
import software.amazon.lambda.powertools.metrics.Metrics;
import static software.amazon.lambda.powertools.metrics.MetricsUtils;

public class App implements RequestHandler<Object, Object> {

    MetricsLogger metricsLogger = MetricsUtils.metricsLogger();

    static {
        MetricsUtils.defaultDimensions(DimensionSet.of("CustomDimension", "booking"));
    }

    @Override
    @Metrics(namespace = "ExampleApplication", service = "booking")
    public Object handleRequest(Object input, Context context) {
        ...
        MetricsUtils.withSingleMetric("Metric2", 1, Unit.COUNT, log -> {});
    }
}

```

## Creating a metric with a different dimension

CloudWatch EMF uses the same dimensions across all your metrics. Use `withSingleMetric` if you have a metric that should have different dimensions.

Info

Generally, this would be an edge case since you [pay for unique metric](https://aws.amazon.com/cloudwatch/pricing/). Keep the following formula in mind: **unique metric = (metric_name + dimension_name + dimension_value)**

```
import static software.amazon.lambda.powertools.metrics.MetricsUtils.withSingleMetric;

public class App implements RequestHandler<Object, Object> {

    @Override
    public Object handleRequest(Object input, Context context) {
         withSingleMetric("CustomMetrics2", 1, Unit.COUNT, "Another", (metric) -> {
            metric.setDimensions(DimensionSet.of("AnotherService", "CustomService"));
        });
    }
}

```

## Creating metrics with different configurations

Use `withMetricsLogger` if you have one or more metrics that should have different configurations e.g. dimensions or namespace.

```
import static software.amazon.lambda.powertools.metrics.MetricsUtils.withMetricsLogger;

public class App implements RequestHandler<Object, Object> {

    @Override
    public Object handleRequest(Object input, Context context) {
         withMetricsLogger(logger -> {
            // override default dimensions
            logger.setDimensions(DimensionSet.of("AnotherService", "CustomService"));
            // add metrics
            logger.putMetric("CustomMetrics1", 1, Unit.COUNT);
            logger.putMetric("CustomMetrics2", 5, Unit.COUNT);
        });
    }
}

```

Powertools tracing is an opinionated thin wrapper for [AWS X-Ray Java SDK](https://github.com/aws/aws-xray-sdk-java/) a provides functionality to reduce the overhead of performing common tracing tasks.

**Key Features**

- Capture cold start as annotation, and responses as well as full exceptions as metadata
- Helper methods to improve the developer experience of creating new X-Ray subsegments.
- Better developer experience when developing with multiple threads.
- Auto patch supported modules by AWS X-Ray

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-tracing</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-tracing</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-tracing</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-tracing</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-tracing:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-tracing:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Initialization

Before your use this utility, your AWS Lambda function [must have permissions](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html#services-xray-permissions) to send traces to AWS X-Ray.

> Example using AWS Serverless Application Model (SAM)

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11

        Tracing: Active
        Environment:
            Variables:
                POWERTOOLS_SERVICE_NAME: example

```

The Powertools for AWS Lambda (Java) service name is used as the X-Ray namespace. This can be set using the environment variable `POWERTOOLS_SERVICE_NAME`

### Lambda handler

To enable Powertools for AWS Lambda (Java) tracing to your function add the `@Tracing` annotation to your `handleRequest` method or on any method will capture the method as a separate subsegment automatically. You can optionally choose to customize segment name that appears in traces.

```
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        businessLogic1();

        businessLogic2();
    }

    @Tracing
    public void businessLogic1(){

    }

    @Tracing
    public void businessLogic2(){

    }
}

```

```
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing(segmentName="yourCustomName")
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
    ...
    }

```

When using this `@Tracing` annotation, Utility performs these additional tasks to ease operations:

- Creates a `ColdStart` annotation to easily filter traces that have had an initialization overhead.
- Creates a `Service` annotation if service parameter or `POWERTOOLS_SERVICE_NAME` is set.
- Captures any response, or full exceptions generated by the handler, and include as tracing metadata.

By default, this annotation will automatically record method responses and exceptions. You can change the default behavior by setting the environment variables `POWERTOOLS_TRACER_CAPTURE_RESPONSE` and `POWERTOOLS_TRACER_CAPTURE_ERROR` as needed. Optionally, you can override behavior by different supported `captureMode` to record response, exception or both.

Returning sensitive information from your Lambda handler or functions, where `Tracing` is used?

You can disable annotation from capturing their responses and exception as tracing metadata with **`captureMode=DISABLED`** or globally by setting environment variables **`POWERTOOLS_TRACER_CAPTURE_RESPONSE`** and **`POWERTOOLS_TRACER_CAPTURE_ERROR`** to **`false`**

```
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing(captureMode=CaptureMode.DISABLED)
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
    ...
    }

```

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11

        Tracing: Active
        Environment:
            Variables:
                POWERTOOLS_TRACER_CAPTURE_RESPONSE: false
                POWERTOOLS_TRACER_CAPTURE_ERROR: false

```

### Annotations & Metadata

**Annotations** are key-values associated with traces and indexed by AWS X-Ray. You can use them to filter traces and to create [Trace Groups](https://aws.amazon.com/about-aws/whats-new/2018/11/aws-xray-adds-the-ability-to-group-traces/) to slice and dice your transactions.

**Metadata** are key-values also associated with traces but not indexed by AWS X-Ray. You can use them to add additional context for an operation using any native object.

You can add annotations using `putAnnotation()` method from TracingUtils

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        TracingUtils.putAnnotation("annotation", "value");
    }
}

```

You can add metadata using `putMetadata()` method from TracingUtils

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        TracingUtils.putMetadata("content", "value");
    }
}

```

## Override default object mapper

You can optionally choose to override default object mapper which is used to serialize method response and exceptions when enabled. You might want to supply custom object mapper in order to control how serialisation is done, for example, when you want to log only specific fields from received event due to security.

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;
import static software.amazon.lambda.powertools.tracing.CaptureMode.RESPONSE;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> { 
    static {
        ObjectMapper objectMapper = new ObjectMapper();
        SimpleModule simpleModule = new SimpleModule();
        objectMapper.registerModule(simpleModule);

        TracingUtils.defaultObjectMapper(objectMapper);
    }

    @Tracing(captureMode = RESPONSE)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
    }
}

```

## Utilities

Tracing modules comes with certain utility method when you don't want to use annotation for capturing a code block under a subsegment, or you are doing multithreaded programming. Refer examples below.

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
         TracingUtils.withSubsegment("loggingResponse", subsegment -> {
            // Some business logic
         });

         TracingUtils.withSubsegment("localNamespace", "loggingResponse", subsegment -> {
            // Some business logic
         });
    }
}

```

```
import static software.amazon.lambda.powertools.tracing.TracingUtils.withEntitySubsegment;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        // Extract existing trace data
        Entity traceEntity = AWSXRay.getTraceEntity();

        Thread anotherThread = new Thread(() -> withEntitySubsegment("inlineLog", traceEntity, subsegment -> {
            // Business logic in separate thread
        }));
    }
}

```

## Instrumenting SDK clients and HTTP calls

Powertools for Lambda (Java) cannot intercept SDK clients instantiation to add X-Ray instrumentation. You should make sure to instrument the SDK clients explicitly. Refer details on [how to instrument SDK client with Xray](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html#xray-sdk-java-awssdkclients) and [outgoing http calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html#xray-sdk-java-httpclients). For example:

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.handlers.TracingHandler;

public class LambdaHandler {
    private AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
        .withRegion(Regions.fromName(System.getenv("AWS_REGION")))
        .withRequestHandlers(new TracingHandler(AWSXRay.getGlobalRecorder()))
        .build();
    // ...
}

```

## Testing your code

When using `@Tracing` annotation, your Junit test cases needs to be configured to create parent Segment required by [AWS X-Ray SDK for Java](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html).

Below are two ways in which you can configure your tests.

#### Configure environment variable on project level (Recommended)

You can choose to configure environment variable on project level for your test cases run. This is recommended approach as it will avoid the need of configuring each test case specifically.

Below are examples configuring your maven/gradle projects. You can choose to configure it differently as well as long as you are making sure that environment variable `LAMBDA_TASK_ROOT` is set. This variable is used internally via AWS X-Ray SDK to configure itself properly for lambda runtime.

```
<build>
    ...
  <plugins>
    <!--  Configures environment variable to avoid initialization of AWS X-Ray segments for each tests-->
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <configuration>
              <environmentVariables>
                  <LAMBDA_TASK_ROOT>handler</LAMBDA_TASK_ROOT>
              </environmentVariables>
          </configuration>
      </plugin>
  </plugins>
</build>

```

```
// Configures environment variable to avoid initialization of AWS X-Ray segments for each tests
test {
    environment "LAMBDA_TASK_ROOT", "handler"
}

```

#### Configure test cases (Not Recommended)

You can choose to configure each of your test case instead as well if you choose not to configure environment variable on project level. Below is an example configuration needed for each test case.

```
import com.amazonaws.xray.AWSXRay;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class AppTest {

    @Before
    public void setup() {
        if(null == System.getenv("LAMBDA_TASK_ROOT")) {
            AWSXRay.beginSegment("test");
        }
    }

    @After
    public void tearDown() {
        // Needed when using sam build --use-container
        if (AWSXRay.getCurrentSubsegmentOptional().isPresent()) {
            AWSXRay.endSubsegment();
        }

        if(null == System.getenv("LAMBDA_TASK_ROOT")) {
          AWSXRay.endSegment();
        }
    }

    @Test
    public void successfulResponse() {
        // test logic
    }

```