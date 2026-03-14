# Source: https://ocelot.readthedocs.io/en/latest/features/tracing.html

Title: Tracing — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/tracing.html

Markdown Content:
This chapter explains how to perform distributed tracing using Ocelot.

[![Image 1: opentracing-csharp Logo](https://avatars.githubusercontent.com/u/15482765)](https://avatars.githubusercontent.com/u/15482765) OpenTracing[¶](https://ocelot.readthedocs.io/en/latest/features/tracing.html#opentracing-csharp-logo-opentracing "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Namespace: `Ocelot.Tracing.OpenTracing`

Ocelot provides tracing functionality through the excellent project from [opentracing-csharp](https://github.com/opentracing/opentracing-csharp) repository. The code for Ocelot integration can be found in this [Ocelot project](https://github.com/ThreeMammals/Ocelot/tree/main/src/Ocelot.Tracing.OpenTracing).

The example below uses the [C# Client for Jaeger](https://github.com/jaegertracing/jaeger-client-csharp) to provide the tracer used in Ocelot. To add [OpenTracing](https://opentracing.io/) services, you must call the `AddOpenTracing()` extension method on the `OcelotBuilder` returned by `AddOcelot()`[[1]](https://ocelot.readthedocs.io/en/latest/features/tracing.html#f1), as shown below:

builder.Services
 .AddSingleton(serviceProvider =>
 {
 var loggerFactory = serviceProvider.GetService<ILoggerFactory>();
 var config = new Jaeger.Configuration(builder.Environment.ApplicationName, loggerFactory);
 var tracer = config.GetTracer();
 GlobalTracer.Register(tracer);
 return tracer;
 })
 .AddOcelot(builder.Configuration)
 .AddOpenTracing();

Then, in your [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/OpenTracing/ocelot.json), add the following to the route you want to trace:

"HttpHandlerOptions": {
 "UseTracing": true
}

Ocelot will now send tracing information to [Jaeger](https://www.jaegertracing.io/) whenever this route is called.

Butterfly[¶](https://ocelot.readthedocs.io/en/latest/features/tracing.html#butterfly "Link to this heading")
------------------------------------------------------------------------------------------------------------

> Namespace: `Ocelot.Tracing.Butterfly`

Ocelot provides tracing functionality through the excellent [Butterfly](https://github.com/liuhaoyang/butterfly) project. The code for the Ocelot integration can be found in this [Ocelot project](https://github.com/ThreeMammals/Ocelot/tree/main/src/Ocelot.Tracing.Butterfly). To use the tracing functionality, please refer to the [Butterfly](https://github.com/liuhaoyang/butterfly) documentation.

In Ocelot, you need to add the NuGet package if you wish to trace a route:

Install-Package Ocelot.Tracing.Butterfly

In your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs), to add [Butterfly](https://github.com/liuhaoyang/butterfly) services, you must call the `AddButterfly()` extension method on the `OcelotBuilder` returned by `AddOcelot()`, as shown below:

using Ocelot.Tracing.Butterfly;

builder.Services
 .AddOcelot(builder.Configuration)
 .AddButterfly(options => {
 // This is the URL that the Butterfly collector server is running on...
 options.CollectorUrl = "http://localhost:9618";
 options.Service = "Ocelot";
 });

Then, in your [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json), add the following to the route you want to trace:

"HttpHandlerOptions": {
 "UseTracing": true
}

Ocelot will now send tracing information to [Butterfly](https://github.com/liuhaoyang/butterfly) whenever this route is called.

> **Note**: The [Butterfly](https://github.com/liuhaoyang/butterfly) project has not been supported for more than seven years, as of 2025. The latest release of the [Butterfly.Client](https://www.nuget.org/packages/Butterfly.Client) package (version [0.0.8](https://www.nuget.org/packages/Butterfly.Client/0.0.8)) was made on February 22, 2018. The Ocelot team is planning to discontinue the [Ocelot.Tracing.Butterfly](https://www.nuget.org/packages/Ocelot.Tracing.Butterfly) package, which is scheduled to happen after the release of Ocelot version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0).

* * *
