# Source: https://serilog.net/

Title: Serilog — simple .NET logging with fully-structured events

URL Source: https://serilog.net/

Published Time: Mon, 18 Nov 2019 22:16:10 GMT

Markdown Content:
Serilog — simple .NET logging with fully-structured events
===============

Flexible, structured events — log file convenience.
===================================================

Why Serilog?
------------

Like many other libraries for .NET, Serilog provides diagnostic logging to files, the console, and [elsewhere](https://github.com/serilog/serilog/wiki/Provided-Sinks). It is easy to set up, has a clean API, and is portable between recent .NET platforms.

_Unlike_ other logging libraries, Serilog is built with powerful _structured event data_ in mind.

### Text formatting with a twist

Serilog _message templates_ are a simple DSL extending .NET format strings. Parameters can be named, and their values are serialized as properties on the event for incredible searching and sorting flexibility:

var position = new { Latitude = 25, Longitude = 134 }; var elapsedMs = 34; log.Information("Processed {@Position} in {Elapsed:000} ms.", position, elapsedMs);

This example records two properties, `Position` and `Elapsed` along with the log event. The properties captured in the example, in JSON format, would appear like:

{"Position": {"Latitude": 25, "Longitude": 134}, "Elapsed": 34}

The `@` operator in front of `Position` tells Serilog to serialize the object passed in, rather than convert it using `ToString()`.

The `:000` segment following `Elapsed` is a standard .NET format string that affects how the property is rendered. The console sink included with Serilog will display the above message as:

09:14:22 [Information] Processed { Latitude: 25, Longitude: 134 } in 034 ms.

### Documentation

You'll find heaps of information and advice about using Serilog on the project site:

*   [Installation](https://github.com/serilog/serilog/wiki/Getting-Started)
*   [Configuration basics](https://github.com/serilog/serilog/wiki/Configuration-Basics)
*   [Writing log events](https://github.com/serilog/serilog/wiki/Writing-Log-Events)
*   [Structured data](https://github.com/serilog/serilog/wiki/Structured-Data)
*   [Provided sinks](https://github.com/serilog/serilog/wiki/Provided-Sinks)
*   [Debugging and diagnostics](https://github.com/serilog/serilog/wiki/Debugging-and-Diagnostics)

### Resources

*   [GitHub project](https://github.com/serilog/serilog)
*   [`serilog` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/serilog)
*   [Blog posts at nblumhardt.com](http://nblumhardt.com/)
*   [Packages on NuGet](https://nuget.org/packages?q=Tags%3A%22serilog%22)
*   [Serilog integration for ASP.NET Core 2+](https://github.com/serilog/serilog-aspnetcore)
*   [Gitter chat](https://gitter.im/serilog/serilog)

[Dive in deeper with this great Serilog course on ![Image 1: Pluralsight](https://serilog.net/img/pluralsight-light.png)](http://pluralsight.com/training/Courses/TableOfContents/modern-structured-logging-serilog-seq)

Serilog is open source software under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) license, copyright © and maintained by its [contributors](https://github.com/serilog/serilog/contributors).
