# Serilog Documentation

**Project:** https://github.com/serilog/serilog  
**Official Site:** https://serilog.net/  
**License:** Apache 2.0

## Overview

Serilog is a simple, powerful, and fully-featured library for structured logging in .NET applications. Unlike traditional logging libraries, Serilog is built from the ground up with powerful structured event data in mind.

### Key Features

- **Structured Events** - Log data as properties, not just formatted strings
- **Message Templates** - Simple DSL extending .NET format strings
- **Flexible Output** - Write to files, console, Seq, and 40+ other sinks
- **Enrichment** - Automatically add context to log events
- **Multiple Levels** - Verbose, Debug, Information, Warning, Error, Fatal
- **Configuration** - Via code, appsettings.json, or Seq
- **Performance** - Optimized for high-throughput scenarios
- **Open Source** - Apache 2.0 licensed, active community

---

## Getting Started

### Installation

Install Serilog from NuGet:

```bash
dotnet add package Serilog
```

For a specific sink (e.g., file output):

```bash
dotnet add package Serilog.Sinks.File
dotnet add package Serilog.Sinks.Console
```

### Basic Setup

Serilog uses a fluent configuration API:

```csharp
using Serilog;

Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Debug()
    .WriteTo.Console()
    .WriteTo.File("logs/myapp-.txt", rollingInterval: RollingInterval.Day)
    .CreateLogger();

Log.Information("Application started");
```

### Static Logger Usage

After configuration, use the static `Log` class:

```csharp
Log.Information("Hello {Name}", "World");
Log.Warning("This is a warning");
Log.Error(exception, "An error occurred");
```

### Logger Injection (Dependency Injection)

For ASP.NET Core applications:

```bash
dotnet add package Serilog.AspNetCore
```

In Program.cs:

```csharp
using Serilog;

var builder = WebApplication.CreateBuilder(args);

builder.Host.UseSerilog();

var app = builder.Build();
app.Run();
```

---

## Configuration Basics

### Fluent Configuration API

The configuration API uses a builder pattern:

```csharp
var log = new LoggerConfiguration()
    .MinimumLevel.Debug()
    .WriteTo.Console()
    .WriteTo.File("logs/app-.txt", rollingInterval: RollingInterval.Day)
    .Enrich.WithProperty("Version", "1.0")
    .CreateLogger();
```

### Appsettings.json Configuration

Serilog can be configured via `appsettings.json`:

```json
{
  "Serilog": {
    "MinimumLevel": "Information",
    "WriteTo": [
      { "Name": "Console" },
      {
        "Name": "File",
        "Args": {
          "path": "logs/app-.txt",
          "rollingInterval": "Day"
        }
      }
    ],
    "Enrich": ["FromLogContext", "WithMachineName"],
    "Properties": {
      "Application": "MyApp"
    }
  }
}
```

### Configuration Levels

- `Verbose` - Very detailed trace-level information
- `Debug` - Debug-level information useful during development
- `Information` - General informational messages
- `Warning` - Potentially harmful situations
- `Error` - Error conditions and exceptions
- `Fatal` - Critical errors that may cause application shutdown

### Minimum Level Overrides

Override minimum level per sink:

```csharp
new LoggerConfiguration()
    .MinimumLevel.Warning()
    .WriteTo.Console(
        restrictedToMinimumLevel: LogEventLevel.Information)
    .CreateLogger();
```

---

## Writing Log Events

### Message Templates

Serilog uses message templates similar to .NET format strings:

```csharp
Log.Information("User {UserId} logged in from {IPAddress}", 
    userId, ipAddress);
```

The template parameters become properties on the log event, enabling structured searching and analysis.

### Destructuring with @ Symbol

Use `@` to destructure complex objects:

```csharp
var person = new { Name = "Alice", Age = 30 };
Log.Information("Person: {@Person}", person);

// Logs: { "Person": { "Name": "Alice", "Age": 30 } }
```

### Format Strings

Apply .NET format strings to parameters:

```csharp
var elapsed = 1234.5;
Log.Information("Operation completed in {Elapsed:F2}ms", elapsed);

// Logs: Elapsed = 1234.50
```

### Exception Logging

Log exceptions with full context:

```csharp
try
{
    // ... code ...
}
catch (Exception ex)
{
    Log.Error(ex, "An error occurred while processing {Item}", itemId);
}
```

### Log Levels in Context

```csharp
Log.Verbose("Detailed trace information");
Log.Debug("Debug-level information");
Log.Information("General information");
Log.Warning("Warning message");
Log.Error("Error message");
Log.Fatal("Critical error");
```

---

## Structured Data

### Property Capture

Serilog automatically captures named parameters as properties:

```csharp
Log.Information("Order {OrderId} created by {UserId} for {Amount:C}", 
    orderId, userId, amount);

// Structured properties:
// OrderId: 12345
// UserId: "user123"
// Amount: 99.99
```

### Property Types

Captured properties preserve their types:

```csharp
Log.Information("Page loaded in {Elapsed}ms", 1234);      // int
Log.Information("Temperature {Temp:F1}C", 23.5);          // double
Log.Information("Active {IsActive}", true);               // bool
Log.Information("Items {@Items}", new[] { 1, 2, 3 });    // array
```

### JSON Output

With JSON sink, properties are properly structured:

```json
{
  "Timestamp": "2024-01-15T10:30:00.000Z",
  "Level": "Information",
  "MessageTemplate": "Order {OrderId} created",
  "Properties": {
    "OrderId": 12345
  }
}
```

### Enrichment

Add properties to all events:

```csharp
new LoggerConfiguration()
    .Enrich.WithProperty("Application", "MyApp")
    .Enrich.WithProperty("Version", "1.0")
    .Enrich.WithMachineName()
    .Enrich.WithThreadId()
    .CreateLogger();
```

---

## Provided Sinks

Serilog includes several built-in sinks and supports 40+ additional sinks via NuGet.

### Console Sink

Write to console output:

```csharp
new LoggerConfiguration()
    .WriteTo.Console()
    .CreateLogger();
```

### File Sink

Write to text files:

```bash
dotnet add package Serilog.Sinks.File
```

```csharp
new LoggerConfiguration()
    .WriteTo.File("logs/app-.txt", 
        rollingInterval: RollingInterval.Day,
        retainedFileCountLimit: 30)
    .CreateLogger();
```

### Seq Sink

Centralized structured logging:

```bash
dotnet add package Serilog.Sinks.Seq
```

```csharp
new LoggerConfiguration()
    .WriteTo.Seq("http://localhost:5341")
    .CreateLogger();
```

### Popular Community Sinks

- **Application Insights** - Serilog.Sinks.ApplicationInsights
- **Datadog** - Serilog.Sinks.Datadog.Logs
- **Elasticsearch** - Serilog.Sinks.Elasticsearch
- **Loggly** - Serilog.Sinks.Loggly
- **Splunk** - Serilog.Sinks.Splunk
- **Google Cloud Logging** - Serilog.Sinks.GoogleCloudLogging
- **Azure Storage** - Serilog.Sinks.AzureTableStorage
- **Syslog** - Serilog.Sinks.Syslog

---

## Enrichers

Enrichers add properties to every log event.

### Built-in Enrichers

```bash
dotnet add package Serilog.Enrichers.Environment
dotnet add package Serilog.Enrichers.Thread
```

```csharp
new LoggerConfiguration()
    .Enrich.WithMachineName()
    .Enrich.WithThreadId()
    .Enrich.WithEnvironmentUserName()
    .Enrich.WithProperty("Application", "MyApp")
    .CreateLogger();
```

### Custom Enrichers

Create custom enrichers:

```csharp
public class RequestIdEnricher : ILogEventEnricher
{
    public void Enrich(LogEvent logEvent, ILogEventPropertyFactory propertyFactory)
    {
        var requestId = HttpContext.Current?.Request.Headers["X-Request-Id"];
        if (!string.IsNullOrEmpty(requestId))
        {
            logEvent.AddPropertyIfAbsent(
                propertyFactory.CreateProperty("RequestId", requestId));
        }
    }
}

// Register enricher
new LoggerConfiguration()
    .Enrich.With<RequestIdEnricher>()
    .CreateLogger();
```

### Common Enrichers

- `WithMachineName()` - Add machine/computer name
- `WithThreadId()` - Add managed thread ID
- `WithEnvironmentUserName()` - Add current Windows user
- `WithProperty(name, value)` - Add custom property
- `FromLogContext()` - Properties from LogContext

---

## Debugging and Diagnostics

### Self-Logging

Serilog includes diagnostics for troubleshooting configuration:

```csharp
Serilog.Debugging.SelfLog.Enable(msg => 
    Debug.WriteLine("SERILOG: " + msg));

var log = new LoggerConfiguration()
    .MinimumLevel.Debug()
    .WriteTo.Console()
    .CreateLogger();
```

### Checking Configuration

Verify logger configuration:

```csharp
var logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .WriteTo.File("logs/app.txt")
    .CreateLogger();

// Log a test message
logger.Information("Configuration test");
logger.Debug("This should not appear (below minimum level)");
```

### Common Issues

#### Logger not writing

- Check minimum level configuration
- Verify sink is properly configured
- Check file permissions for file sink
- Review SelfLog output for errors

#### Missing properties

- Ensure parameters are named in message template
- Use `@` symbol for object destructuring
- Check that enrichers are registered

#### Performance concerns

- Adjust minimum level to reduce overhead
- Use asynchronous sinks for I/O-bound operations
- Consider batching sinks for high-volume scenarios

---

## Integration with ASP.NET Core

### Basic Integration

```bash
dotnet add package Serilog.AspNetCore
```

In Program.cs:

```csharp
using Serilog;

var builder = WebApplication.CreateBuilder(args);

builder.Host.UseSerilog((context, loggerConfig) =>
{
    loggerConfig
        .WriteTo.Console()
        .WriteTo.File("logs/app-.txt", rollingInterval: RollingInterval.Day);
});

builder.Services.AddControllers();

var app = builder.Build();

app.MapControllers();
app.Run();
```

### Request Logging Middleware

Automatically log HTTP requests:

```csharp
app.UseSerilogRequestLogging();
```

---

## Resources and Links

- **GitHub Repository**: https://github.com/serilog/serilog
- **Official Website**: https://serilog.net/
- **NuGet Package**: https://www.nuget.org/packages/Serilog/
- **Wiki Documentation**: https://github.com/serilog/serilog/wiki
- **Gitter Chat**: https://gitter.im/serilog/serilog
- **Stack Overflow**: Tag `serilog`

---

## Related Packages

- **Serilog.AspNetCore** - ASP.NET Core integration
- **Serilog.Sinks.Seq** - Structured logging backend
- **Serilog.Sinks.File** - File output
- **Serilog.Sinks.Console** - Console output
- **Serilog.Enrichers.Environment** - Environmental enrichment
