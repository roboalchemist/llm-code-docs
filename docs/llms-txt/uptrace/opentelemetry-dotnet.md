# Source: https://uptrace.dev/raw/get/opentelemetry-dotnet.md

# OpenTelemetry .NET distro for Uptrace

> Step-by-step guide to install and configure OpenTelemetry .NET SDKs, export telemetry to Uptrace, and verify that traces, metrics, and logs arrive via OTLP.

![undefined](/devicon/dot-net-original.svg)This guide shows you how to configure the OpenTelemetry .NET SDK to export spans, logs, and metrics to Uptrace using the OTLP/HTTP protocol.

## Choose Your Setup Path

### Option A: Quick Start with uptrace-dotnet (Recommended)

Best for: Getting started quickly, automatic configuration

[uptrace-dotnet](https://github.com/uptrace/uptrace-dotnet) is a lightweight wrapper around [opentelemetry-dotnet](https://github.com/open-telemetry/opentelemetry-dotnet) that pre-configures the OpenTelemetry SDK to export data to Uptrace. It doesn't add new functionality but simplifies the setup process for your convenience.

```shell
dotnet add package Uptrace.OpenTelemetry --prerelease
```

â [Continue below](#quick-start)

### Option B: Direct OTLP Configuration

Best for: Existing OpenTelemetry users, custom exporters, fine-grained control

â [Direct OTLP Setup](/get/opentelemetry-dotnet/otlp)

## Quick Start Guide

Follow these steps to get your first trace running in 5 minutes:

### Step 1: Create an Uptrace Project

[Create](/get) an Uptrace project to obtain a [DSN](/get#dsn) (Data Source Name), for example, `https://<secret>@api.uptrace.dev?grpc=4317`.

### Step 2: Install uptrace-dotnet

```shell
dotnet add package Uptrace.OpenTelemetry --prerelease
```

### Step 3: Basic Configuration

Configure the Uptrace client using a [DSN](/get#dsn) (Data Source Name) from your project settings page. Replace `<FIXME>` with your actual Uptrace DSN and `myservice` with a name that identifies your application.

```cs
using System;
using System.Diagnostics;

using OpenTelemetry;
using OpenTelemetry.Trace;
using OpenTelemetry.Resources;

using Uptrace.OpenTelemetry;

var serviceName = "myservice";
var serviceVersion = "1.0.0";

using var tracerProvider = Sdk.CreateTracerProviderBuilder()
    .AddSource(serviceName) // For custom spans
    .SetResourceBuilder(
        ResourceBuilder
            .CreateDefault()
            .AddEnvironmentVariableDetector()
            .AddTelemetrySdk()
            .AddService(serviceName: serviceName, serviceVersion: serviceVersion)
    )
    .AddAspNetCoreInstrumentation() // Automatic HTTP server spans
    .AddHttpClientInstrumentation() // Automatic HTTP client spans
    // Copy your project DSN here or use UPTRACE_DSN env var
    //.AddUptrace("<FIXME>")
    .AddUptrace()
    .Build();
```

For the instrumentation to work, install these additional packages:

```shell
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Http
```

### Step 4: Run the Complete Example

Clone the [basic](https://github.com/uptrace/uptrace-dotnet/tree/master/example/basic) example to get a ready-to-run application:

```shell
git clone https://github.com/uptrace/uptrace-dotnet.git
cd uptrace-dotnet/example/basic
```

### Step 5: Run Your Application

Execute your application, replacing `<FIXME>` with your Uptrace DSN:

```shell
UPTRACE_DSN="<FIXME>" dotnet run
```

You should see output similar to:

```text
https://app.uptrace.dev/traces/<trace_id>
```

### Step 6: View Your Trace

Click the generated link to view your trace in the Uptrace dashboard:

![Basic trace](/get/basic-trace.png)

## Configuration Options

Use these settings when configuring resources and the Uptrace exporter:

<table>
<thead>
  <tr>
    <th>
      Setting
    </th>
    
    <th>
      Where to configure
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
        UPTRACE_DSN
      </code>
    </td>
    
    <td>
      <code>
        AddUptrace("<DSN>")
      </code>
      
       or environment variable
    </td>
    
    <td>
      A data source that specifies Uptrace project credentials.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service.name
      </code>
    </td>
    
    <td>
      <code>
        AddService(serviceName: ...)
      </code>
      
       or <code>
        OTEL_SERVICE_NAME
      </code>
    </td>
    
    <td>
      The service name shown in Uptrace.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service.version
      </code>
    </td>
    
    <td>
      <code>
        AddService(..., serviceVersion: ...)
      </code>
    </td>
    
    <td>
      The service version for deployments.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        deployment.environment
      </code>
    </td>
    
    <td>
      <code>
        AddAttributes(...)
      </code>
      
       or <code>
        OTEL_RESOURCE_ATTRIBUTES
      </code>
    </td>
    
    <td>
      The environment (production, staging).
    </td>
  </tr>
  
  <tr>
    <td>
      Resource attributes
    </td>
    
    <td>
      <code>
        AddAttributes(...)
      </code>
      
       or <code>
        OTEL_RESOURCE_ATTRIBUTES
      </code>
    </td>
    
    <td>
      Additional metadata like <code>
        service.namespace
      </code>
      
       or <code>
        team.name
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      Resource detectors
    </td>
    
    <td>
      <code>
        AddEnvironmentVariableDetector()
      </code>
    </td>
    
    <td>
      Reads resource attributes from environment variables.
    </td>
  </tr>
</tbody>
</table>

## ASP.NET Core Configuration

For ASP.NET Core applications, use the modern `AddOpenTelemetry()` extension method which provides a cleaner configuration experience:

```cs
using OpenTelemetry.Exporter;
using OpenTelemetry.Logs;
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

var serviceName = "myservice";
var serviceVersion = "1.0.0";

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenTelemetry()
    .ConfigureResource(resource => resource
        .AddService(serviceName: serviceName, serviceVersion: serviceVersion)
        .AddAttributes(new Dictionary<string, object>
        {
            ["deployment.environment"] = builder.Environment.EnvironmentName
        }))
    .WithTracing(tracing => tracing
        .AddSource(serviceName)
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("https://api.uptrace.dev/v1/traces");
            options.Headers = $"uptrace-dsn={Environment.GetEnvironmentVariable("UPTRACE_DSN")}";
            options.Protocol = OtlpExportProtocol.HttpProtobuf;
        }))
    .WithMetrics(metrics => metrics
        .AddMeter(serviceName)
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("https://api.uptrace.dev/v1/metrics");
            options.Headers = $"uptrace-dsn={Environment.GetEnvironmentVariable("UPTRACE_DSN")}";
            options.Protocol = OtlpExportProtocol.HttpProtobuf;
        }));

builder.Logging.AddOpenTelemetry(logging =>
{
    logging.SetResourceBuilder(ResourceBuilder.CreateDefault()
        .AddService(serviceName: serviceName, serviceVersion: serviceVersion)
        .AddAttributes(new Dictionary<string, object>
        {
            ["deployment.environment"] = builder.Environment.EnvironmentName
        }));
    logging.IncludeFormattedMessage = true;
    logging.IncludeScopes = true;
    logging.AddOtlpExporter(options =>
    {
        options.Endpoint = new Uri("https://api.uptrace.dev/v1/logs");
        options.Headers = $"uptrace-dsn={Environment.GetEnvironmentVariable("UPTRACE_DSN")}";
        options.Protocol = OtlpExportProtocol.HttpProtobuf;
    });
});

builder.Services.AddControllers();

var app = builder.Build();
app.MapControllers();
app.Run();
```

### Required NuGet Packages

Install the following packages for ASP.NET Core:

```shell
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Http
```

## Error Monitoring

To monitor errors with exception details, use the `RecordException` method on an `Activity`:

```cs
using System;
using System.Diagnostics;

var activitySource = new ActivitySource("app_or_package_name");

using var activity = activitySource.StartActivity("operation-name");

try
{
    // Your code that might throw
    throw new InvalidOperationException("Something went wrong");
}
catch (Exception ex)
{
    activity?.RecordException(ex);
    activity?.SetStatus(ActivityStatusCode.Error, ex.Message);
    throw;
}
```

This records the exception as a span event with the following attributes:

- `exception.type`
- `exception.message`
- `exception.stacktrace`

### ASP.NET Core Automatic Exception Recording

For ASP.NET Core applications, you can enable automatic exception recording using the instrumentation options:

```cs
using OpenTelemetry;
using OpenTelemetry.Trace;

var tracerProvider = Sdk.CreateTracerProviderBuilder()
    .AddAspNetCoreInstrumentation(options =>
    {
        options.RecordException = true;
    })
    .AddOtlpExporter()
    .Build();
```

When `RecordException` is enabled, unhandled exceptions in your ASP.NET Core application are automatically recorded as span events with full exception details.

See [OpenTelemetry .NET Tracing API](/get/opentelemetry-dotnet/tracing) for more details.

## Resource Configuration

Resources provide metadata about the entity producing telemetry. You can configure resources using environment variables or in code.

### Using Environment Variables

Use the `OTEL_RESOURCE_ATTRIBUTES` environment variable to inject resource attributes:

```shell
export OTEL_SERVICE_NAME="myservice"
export OTEL_RESOURCE_ATTRIBUTES="service.version=1.0.0,deployment.environment=production,team.name=backend"
```

The .NET SDK automatically detects these environment variables when you use `AddEnvironmentVariableDetector()`:

```cs
var resourceBuilder = ResourceBuilder
    .CreateDefault()
    .AddEnvironmentVariableDetector()
    .AddTelemetrySdk();
```

### Using Code

Add custom resource attributes programmatically:

```cs
using OpenTelemetry.Resources;

var resourceBuilder = ResourceBuilder
    .CreateDefault()
    .AddService(serviceName: "myservice", serviceVersion: "1.0.0")
    .AddAttributes(new Dictionary<string, object>
    {
        ["deployment.environment"] = "production",
        ["team.name"] = "backend",
        ["service.namespace"] = "my-namespace"
    });
```

Common resource attributes include:

<table>
<thead>
  <tr>
    <th>
      Attribute
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
        service.name
      </code>
    </td>
    
    <td>
      The name of the service
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service.version
      </code>
    </td>
    
    <td>
      The version of the service
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service.namespace
      </code>
    </td>
    
    <td>
      A namespace for the service
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        service.instance.id
      </code>
    </td>
    
    <td>
      Unique identifier for the service instance
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        deployment.environment
      </code>
    </td>
    
    <td>
      The deployment environment (production, staging)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        host.name
      </code>
    </td>
    
    <td>
      The hostname
    </td>
  </tr>
</tbody>
</table>

## Troubleshooting

If you encounter issues with OpenTelemetry .NET, try these troubleshooting guides:

- [OpenTelemetry .NET Core Documentation](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/src/OpenTelemetry/README.md#troubleshooting)
- [OpenTelemetry .NET Instrumentation Troubleshooting](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/blob/main/docs/troubleshooting.md)

### Common Issues

**No data appearing in Uptrace:**

- Verify your DSN is correctly configured
- Check that your application is generating spans/metrics
- Ensure network connectivity to Uptrace endpoints

**Performance issues:**

- Adjust sampling rates if collecting too much data
- Review instrumentation configuration for unnecessary overhead

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
      <a href="/get/opentelemetry-dotnet/zero-code">
        Zero-code instrumentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Instrument my code with spans
    </td>
    
    <td>
      <a href="/get/opentelemetry-dotnet/tracing">
        OpenTelemetry .NET Tracing API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Collect application metrics
    </td>
    
    <td>
      <a href="/get/opentelemetry-dotnet/metrics">
        OpenTelemetry .NET Metrics API
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Send logs to Uptrace
    </td>
    
    <td>
      <a href="/get/opentelemetry-dotnet/logs">
        OpenTelemetry .NET Logs
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Enable distributed tracing
    </td>
    
    <td>
      <a href="/get/opentelemetry-dotnet/propagation">
        OpenTelemetry .NET Context Propagation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Reduce costs in production
    </td>
    
    <td>
      <a href="/get/opentelemetry-dotnet/sampling">
        OpenTelemetry .NET Sampling
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Auto-detect cloud environment
    </td>
    
    <td>
      <a href="/get/opentelemetry-dotnet/resources">
        OpenTelemetry .NET Resource detectors
      </a>
    </td>
  </tr>
</tbody>
</table>

### Framework Guides

- [OpenTelemetry ASP.NET Core configuration](#aspnetcore)
