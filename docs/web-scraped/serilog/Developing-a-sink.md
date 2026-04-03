The following example uses the `dotnet` command to create a project.

## Create the project

```
mkdir SimpleSink
cd SimpleSink
dotnet new console
```

### Add Dependencies

* Add the Serilog Package from NuGet

```
dotnet add package serilog
```
## Building a Simple Sink

Include the following `using` statements.  These are used by the sink class and also the configuring Serilog.

```csharp
using Serilog;
using Serilog.Core;
using Serilog.Events;
using Serilog.Configuration;

```

### Create the Sink

A sink is simply a class that implements the `ILogEventSink` interface.  The following example renders every message regardless of log level to the console.

```csharp
public class MySink : ILogEventSink
{
    private readonly IFormatProvider _formatProvider;

    public MySink(IFormatProvider formatProvider)
    {
        _formatProvider = formatProvider;
    }

    public void Emit(LogEvent logEvent)
    {
        var message = logEvent.RenderMessage(_formatProvider);
        Console.WriteLine(DateTimeOffset.Now.ToString() + " "  + message);
    }
}
```

### Extensions for configuration

A pattern often used when configuring a sink, is to provide an extension method class for the `LoggerSinkConfiguration`.  The following code illustrates this approach by exposing a `MySink` option when configuring Serilog.

```csharp
public static class MySinkExtensions
{
    public static LoggerConfiguration MySink(
              this LoggerSinkConfiguration loggerConfiguration,
              IFormatProvider formatProvider = null)
    {
        return loggerConfiguration.Sink(new MySink(formatProvider));
    }
}
```

These extension methods also drive JSON configuration. When configuring from e.g. `appsettings.json`, some deployment models require adding the assembly containing the extension method class to the `Using` directive:

```json
{
  "Serilog": {
    "MinimumLevel": "Information",
    "Using": [ "Example.SimpleSink" ],
    "WriteTo":
      [
        { "Name": "MySink" }
      ]
  }
}
```

### Using the sink

As seen in [Configuration Basics](https://github.com/serilog/serilog/wiki/Configuration-Basics) the new sink can be configured as follows.

```csharp
var log = new LoggerConfiguration()
    .MinimumLevel.Information()
    .WriteTo.MySink()
    .CreateLogger();
```

### Releasing resources

If the sink implements `IDisposable`, Serilog will call its `Dispose()` method when either `Log.CloseAndFlush()` is called (when using the static `Log` class), or the `Logger` writing to the sink is disposed directly.

### Handling errors and exceptions

If a sink cannot accept/successfully process an event, it can (and should) throw an exception from `Emit()` to notify Serilog of this. Serilog will suppress the exception and write a standard diagnostic message to `SelfLog`, unless the sink is configured explicitly for auditing.

Sinks can additionally write diagnostic messages to `SelfLog`, however this should be done sparingly to avoid adverse performance impact.

### Threading

Sinks must be completely thread-safe once constructed, and accept calls to `Emit()` on any thread. Serilog will invoke `Emit()` concurrently.

## Full Sample

Below is the full example code as a console app.

```csharp
using System;
using Serilog;
using Serilog.Core;
using Serilog.Events;
using Serilog.Configuration;

namespace SimpleSink
{
    class Program
    {
        static void Main(string[] args)
        {
            var log = new LoggerConfiguration()
                .MinimumLevel.Information()
                .WriteTo.MySink()
                .CreateLogger();
            
            var position = new { Latitude = 25, Longitude = 134 };
            var elapsedMs = 34;

            log.Information("Processed {@Position} in {Elapsed:000} ms.", position, elapsedMs);

        }
    }

    public class MySink : ILogEventSink
    {
        private readonly IFormatProvider _formatProvider;

        public MySink(IFormatProvider formatProvider)
        {
            _formatProvider = formatProvider;
        }

        public void Emit(LogEvent logEvent)
        {
            var message = logEvent.RenderMessage(_formatProvider);
            Console.WriteLine(DateTimeOffset.Now.ToString() + " "  + message);
        }
    }

    public static class MySinkExtensions
    {
        public static LoggerConfiguration MySink(
                  this LoggerSinkConfiguration loggerConfiguration,
                  IFormatProvider formatProvider = null)
        {
            return loggerConfiguration.Sink(new MySink(formatProvider));
        }
    }
}
```

*Example Output*

```
17/01/2017 3:10:26 PM +10:00 Processed { Latitude: 25, Longitude: 134 } in 034 ms.
```