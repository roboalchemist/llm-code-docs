# Source: https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide

Title: Guide for running C# Azure Functions in an isolated worker process

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide

Published Time: Thu, 05 Mar 2026 06:20:58 GMT

Markdown Content:
This article introduces working with Azure Functions in .NET using the isolated worker model. This model lets your project target versions of .NET independently of other runtime components. For information about specific .NET versions supported, see [supported version](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#supported-versions).

Use the following links to get started right away building .NET isolated worker model functions.

| Getting started | Concepts | Samples |
| --- | --- | --- |
| * [Using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-vs-code?pivot=programming-language-csharp?tabs=isolated-process) * [Using command line tools](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-csharp) * [Using Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-your-first-function-visual-studio?tabs=isolated-process) | * [Hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) * [Monitoring](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring) | * [Reference samples](https://github.com/Azure/azure-functions-dotnet-worker/tree/main/samples) |

To learn about deploying an isolated worker model project to Azure, see [Deploy to Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#deploy-to-azure-functions).

You can run your .NET class library functions in two modes: either [in the same process](https://learn.microsoft.com/en-us/azure/azure-functions/functions-dotnet-class-library) as the Functions host runtime (_in-process_) or in an isolated worker process. When your .NET functions run in an isolated worker process, you can take advantage of the following benefits:

*   **Fewer conflicts:** Because your functions run in a separate process, assemblies used in your app don't conflict with different versions of the same assemblies used by the host process.
*   **Full control of the process**: You control the start-up of the app, which means that you can manage the configurations used and the middleware started.
*   **Standard dependency injection:** Because you have full control of the process, you can use current .NET behaviors for dependency injection and incorporating middleware into your function app.
*   **.NET version flexibility:** Running outside of the host process means that your functions can run on versions of .NET not natively supported by the Functions runtime, including the .NET Framework.

If you have an existing C# function app that runs in-process, you need to migrate your app to take advantage of these benefits. For more information, see [Migrate .NET apps from the in-process model to the isolated worker model](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-dotnet-to-isolated-model).

For a comprehensive comparison between the two modes, see [Differences between in-process and isolate worker process .NET Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-in-process-differences).

Versions of the Functions runtime support specific versions of .NET. To learn more about Functions versions, see [Azure Functions runtime versions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions). Version support also depends on whether your functions run in-process or isolated worker process.

The following table shows the highest level of .NET or .NET Framework that can be used with a specific version of Functions.

| Functions runtime version | [Isolated worker model](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide) | [In-process model](https://learn.microsoft.com/en-us/azure/azure-functions/functions-dotnet-class-library)4 |
| --- | --- | --- |
| Functions 4.x 1 | .NET 10 5 .NET 9.0 .NET 8.0 .NET Framework 4.8 2 | .NET 8.0 |
| Functions 1.x 3 | n/a | .NET Framework 4.8 |

1 .NET 6 was previously supported on both models but reached the [end of official support](https://dotnet.microsoft.com/platform/support/policy) on November 12, 2024. .NET 7 was previously supported on the isolated worker model but reached the [end of official support](https://dotnet.microsoft.com/platform/support/policy) on May 14, 2024.

2 The build process also requires the [.NET SDK](https://dotnet.microsoft.com/download).

3 Support ends for version 1.x of the Azure Functions runtime on September 14, 2026. For more information, see [this support announcement](https://aka.ms/azure-functions-retirements/hostv1). For continued full support, you should [migrate your apps to version 4.x](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-1-version-4).

4 Support ends for the in-process model on November 10, 2026. For more information, see [this support announcement](https://aka.ms/azure-functions-retirements/in-process-model). For continued full support, you should [migrate your apps to the isolated worker model](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-dotnet-to-isolated-model).

5 You can't run .NET 10 apps on Linux in the Consumption plan. To run on Linux, you should instead use the [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan). For step-by-step migration instructions, see [Migrate Consumption plan apps to the Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/migration/migrate-plan-consumption-to-flex?pivots=platform-linux).

For the latest news about Azure Functions releases, including the removal of specific older minor versions, monitor [Azure App Service announcements](https://github.com/Azure/app-service-announcements/issues).

A .NET project for Azure Functions that uses the isolated worker model is basically a .NET console app project that targets a supported .NET runtime. The following files are the basic files required in any .NET isolated project:

*   C# project file (.csproj) that defines the project and dependencies.
*   Program.cs file that's the entry point for the app.
*   Any code files [defining your functions](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#methods-recognized-as-functions).
*   [host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json) file that defines configuration shared by functions in your project.
*   [local.settings.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file) file that defines environment variables used by your project when run locally on your machine.

For complete examples, see the [.NET 8 sample project](https://github.com/Azure/azure-functions-dotnet-worker/tree/main/samples/FunctionApp) and the [.NET Framework 4.8 sample project](https://github.com/Azure/azure-functions-dotnet-worker/tree/main/samples/NetFxWorker).

A .NET project for Azure Functions that uses the isolated worker model uses a unique set of packages for both core functionality and binding extensions.

To run your .NET functions in an isolated worker process, you need the following packages:

*   [Microsoft.Azure.Functions.Worker](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker/)
*   [Microsoft.Azure.Functions.Worker.Sdk](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Sdk/)

The minimum versions of these packages depend on your target .NET version:

| .NET version | `Microsoft.Azure.Functions.Worker` | `Microsoft.Azure.Functions.Worker.Sdk` |
| --- | --- | --- |
| .NET 10 | 2.50.0 or later | 2.0.5 or later |
| .NET 9 | 2.0.0 or later | 2.0.0 or later |
| .NET 8 | 1.16.0 or later | 1.11.0 or later |
| .NET Framework | 1.16.0 or later | 1.11.0 or later |

The 2.x versions of the core packages change the supported frameworks and bring in support for new .NET APIs from these later versions. When updating to the 2.x versions, note the following changes:

*   Starting with version 2.0.0 of [Microsoft.Azure.Functions.Worker.Sdk](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Sdk/): 
    *   The SDK includes default configurations for [SDK container builds](https://learn.microsoft.com/en-us/dotnet/core/docker/publish-as-container).
    *   The SDK includes support for [`dotnet run`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run) when the [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local) is installed. On Windows, install the Core Tools through a mechanism other than NPM.

*   Starting with version 2.0.0 of [Microsoft.Azure.Functions.Worker](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker/): 
    *   This version adds support for `IHostApplicationBuilder`. Some examples in this guide include tabs to show alternatives using `IHostApplicationBuilder`. These examples require the 2.x versions.
    *   Service provider scope validation is included by default if run in a development environment. This behavior matches ASP.NET Core.
    *   The `EnableUserCodeException` option is enabled by default. The property is now marked as obsolete.
    *   The `IncludeEmptyEntriesInMessagePayload` option is enabled by default. With this option enabled, trigger payloads that represent collections always include empty entries. For example, if a message is sent without a body, an empty entry is still present in `string[]` for the trigger data. The inclusion of empty entries facilitates cross-referencing with metadata arrays which the function may also reference. You can disable this behavior by setting `IncludeEmptyEntriesInMessagePayload` to `false` in the `WorkerOptions` service configuration.
    *   The `ILoggerExtensions` class is renamed to `FunctionsLoggerExtensions`. The rename prevents an ambiguous call error when using `LogMetric()` on an `ILogger` instance.
    *   For apps that use `HttpResponseData`, the `WriteAsJsonAsync()` method no longer sets the status code to `200 OK`. In 1.x, this behavior overrode other error codes that you set.

*   The 2.x versions drop .NET 5 TFM support.

Because .NET isolated worker process functions use different binding types, they require a unique set of binding extension packages.

You find these extension packages under [Microsoft.Azure.Functions.Worker.Extensions](https://www.nuget.org/packages?q=Microsoft.Azure.Functions.Worker.Extensions).

When you use the isolated worker model, you have access to the start-up of your function app, which is usually in `Program.cs`. You're responsible for creating and starting your own host instance. As such, you also have direct access to the configuration pipeline for your app. With .NET Functions isolated worker process, you can much more easily add configurations, inject dependencies, and run your own middleware.

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_1_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_1_hostbuilder)

_To use `IHostApplicationBuilder`, your app must use version 2.x or later of the [core packages](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#core-packages)._

The following code shows an example of an [IHostApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostapplicationbuilder) pipeline:

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.Services
    .AddApplicationInsightsTelemetryWorkerService()
    .ConfigureFunctionsApplicationInsights();

builder.Logging.Services.Configure<LoggerFilterOptions>(options =>
    {
        // The Application Insights SDK adds a default logging filter that instructs ILogger to capture only Warning and more severe logs. Application Insights requires an explicit override.
        // Log levels can also be configured using appsettings.json. For more information, see https://learn.microsoft.com/azure/azure-monitor/app/worker-service#ilogger-logs
        LoggerFilterRule? defaultRule = options.Rules.FirstOrDefault(rule => rule.ProviderName
            == "Microsoft.Extensions.Logging.ApplicationInsights.ApplicationInsightsLoggerProvider");
        if (defaultRule is not null)
        {
            options.Rules.Remove(defaultRule);
        }
    });

var host = builder.Build();
```

Before calling `Build()` on the `IHostApplicationBuilder`, you should:

*   If you want to use [ASP.NET Core integration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration), call `builder.ConfigureFunctionsWebApplication()`.
*   If you're writing your application using F#, you might need to register some binding extensions. See the setup documentation for the [Blobs extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob#install-extension), the [Tables extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table#install-extension), and the [Cosmos DB extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2#install-extension) when you plan to use these extensions in an F# app.
*   Configure any services or app configuration your project requires. See [Configuration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#configuration) for details.
*   If you're planning to use Application Insights, you need to call `AddApplicationInsightsTelemetryWorkerService()` and `ConfigureFunctionsApplicationInsights()` against the builder's `Services` property. See [Application Insights](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#application-insights) for details.

If your project targets .NET Framework 4.8, you also need to add `FunctionsDebugger.Enable();` before creating the HostBuilder. It should be the first line of your `Main()` method. For more information, see [Debugging when targeting .NET Framework](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#debugging-when-targeting-net-framework).

The [IHostApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostapplicationbuilder) is used to build and return a fully initialized [`IHost`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihost) instance, which you run asynchronously to start your function app.

```
await host.RunAsync();
```

The type of builder you use determines how you configure the application.

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_2_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_2_hostbuilder)

Use the `FunctionsApplication.CreateBuilder()` method to add the settings required for the function app to run. The method includes the following functionality:

*   Default set of converters.
*   Set the default [JsonSerializerOptions](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions) to ignore casing on property names.
*   Integrate with Azure Functions logging.
*   Output binding middleware and features.
*   Function execution middleware.
*   Default gRPC support.
*   Apply other defaults from [Host.CreateDefaultBuilder()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.host.createdefaultbuilder).

You have access to the builder pipeline, so you can set any app-specific configurations during initialization. You can call extension methods on the builder's `Configuration` property to add any configuration sources required by your code. For more information about app configuration, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration).

These configurations only apply to the worker code you author. They don't directly influence the configuration of the Functions host or triggers and bindings. To make changes to the functions host or trigger and binding configuration, use the [host.json file](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json).

The isolated worker model uses standard .NET mechanisms for injecting services.

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_3_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_3_hostbuilder)

When you use an `IHostApplicationBuilder`, use its `Services` property to access the [IServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection). The following example injects a singleton service dependency:

```
builder.Services.AddSingleton<IHttpResponderService, DefaultHttpResponderService>();
```

This code requires `using Microsoft.Extensions.DependencyInjection;`. To learn more, see [Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-5.0&preserve-view=true).

Use dependency injection to interact with other Azure services. You can inject clients from the [Azure SDK for .NET](https://learn.microsoft.com/en-us/dotnet/azure/sdk/azure-sdk-for-dotnet) by using the [Microsoft.Extensions.Azure](https://www.nuget.org/packages/Microsoft.Extensions.Azure) package. After installing the package, [register the clients](https://learn.microsoft.com/en-us/dotnet/azure/sdk/dependency-injection#register-clients) by calling `AddAzureClients()` on the service collection in `Program.cs`. The following example configures a [named client](https://learn.microsoft.com/en-us/dotnet/azure/sdk/dependency-injection#configure-multiple-service-clients-with-different-names) for Azure Blobs:

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_4_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_4_hostbuilder)

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.Azure;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.Services
    .AddAzureClients(clientBuilder =>
        {
            clientBuilder.AddBlobServiceClient(builder.Configuration.GetSection("MyStorageConnection"))
                .WithName("copierOutputBlob");
        });

builder.Build().Run();
```

The following example shows how you can use this registration and [SDK types](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#sdk-types) to copy blob contents as a stream from one container to another by using an injected client:

```
using Microsoft.Extensions.Azure;
using Microsoft.Extensions.Logging;

namespace MyFunctionApp
{
    public class BlobCopier
    {
        private readonly ILogger<BlobCopier> _logger;
        private readonly BlobContainerClient _copyContainerClient;

        public BlobCopier(ILogger<BlobCopier> logger, IAzureClientFactory<BlobServiceClient> blobClientFactory)
        {
            _logger = logger;
            _copyContainerClient = blobClientFactory.CreateClient("copierOutputBlob").GetBlobContainerClient("samples-workitems-copy");
            _copyContainerClient.CreateIfNotExists();
        }

        [Function("BlobCopier")]
        public async Task Run([BlobTrigger("samples-workitems/{name}", Connection = "MyStorageConnection")] Stream myBlob, string name)
        {
            await _copyContainerClient.UploadBlobAsync(name, myBlob);
            _logger.LogInformation($"Blob {name} copied!");
        }

    }
}
```

The [`ILogger<T>`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1) in this example is also obtained through dependency injection, so it's registered automatically. To learn more about configuration options for logging, see [Logging](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#logging).

Tip

The example uses a literal string for the name of the client in both `Program.cs` and the function. Instead, consider using a shared constant string defined on the function class. For example, you could add `public const string CopyStorageClientName = nameof(_copyContainerClient);` and then reference `BlobCopier.CopyStorageClientName` in both locations. You could similarly define the configuration section name with the function rather than in `Program.cs`.

The isolated worker model also supports middleware registration, again by using a model similar to what exists in ASP.NET. This model gives you the ability to inject logic into the invocation pipeline, and before and after functions execute.

The [ConfigureFunctionsWorkerDefaults](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.workerhostbuilderextensions.configurefunctionsworkerdefaults?view=azure-dotnet&preserve-view=true#Microsoft_Extensions_Hosting_WorkerHostBuilderExtensions_ConfigureFunctionsWorkerDefaults_Microsoft_Extensions_Hosting_IHostBuilder_) extension method has an overload that lets you register your own middleware, as you see in the following example.

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_5_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_5_hostbuilder)

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

// Register our custom middlewares with the worker
builder
    .UseMiddleware<ExceptionHandlingMiddleware>()
    .UseMiddleware<MyCustomMiddleware>()
    .UseWhen<StampHttpHeaderMiddleware>((context) =>
    {
        // We want to use this middleware only for http trigger invocations.
        return context.FunctionDefinition.InputBindings.Values
                        .First(a => a.Type.EndsWith("Trigger")).Type == "httpTrigger";
    });

builder.Build().Run();
```

The `UseWhen` extension method registers a middleware that executes conditionally. You must pass a predicate that returns a boolean value to this method. The middleware participates in the invocation processing pipeline when the predicate returns `true`.

The following extension methods on [FunctionContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.functioncontext?view=azure-dotnet&preserve-view=true) make it easier to work with middleware in the isolated model.

| Method | Description |
| --- | --- |
| **`GetHttpRequestDataAsync`** | Gets the `HttpRequestData` instance when called by an HTTP trigger. This method returns an instance of `ValueTask<HttpRequestData?>`, which is useful when you want to read message data, such as request headers and cookies. |
| **`GetHttpResponseData`** | Gets the `HttpResponseData` instance when called by an HTTP trigger. |
| **`GetInvocationResult`** | Gets an instance of `InvocationResult`, which represents the result of the current function execution. Use the `Value` property to get or set the value as needed. |
| **`GetOutputBindings`** | Gets the output binding entries for the current function execution. Each entry in the result of this method is of type `OutputBindingData`. You can use the `Value` property to get or set the value as needed. |
| **`BindInputAsync`** | Binds an input binding item for the requested `BindingMetadata` instance. For example, use this method when you have a function with a `BlobInput` input binding that needs to be used by your middleware. |

This example shows a middleware implementation that reads the `HttpRequestData` instance and updates the `HttpResponseData` instance during function execution:

```
internal sealed class StampHttpHeaderMiddleware : IFunctionsWorkerMiddleware
{
    public async Task Invoke(FunctionContext context, FunctionExecutionDelegate next)
    {
        var requestData = await context.GetHttpRequestDataAsync();

        string correlationId;
        if (requestData!.Headers.TryGetValues("x-correlationId", out var values))
        {
            correlationId = values.First();
        }
        else
        {
            correlationId = Guid.NewGuid().ToString();
        }

        await next(context);

        context.GetHttpResponseData()?.Headers.Add("x-correlationId", correlationId);
    }
}
```

This middleware checks for the presence of a specific request header (`x-correlationId`). When the header is present, the middleware uses the header value to stamp a response header. Otherwise, it generates a new GUID value and uses that value for stamping the response header.

Tip

The pattern shown earlier of setting response headers after `await next(context)` might not work reliably in all scenarios. This issue is particularly true when using ASP.NET Core integration or in certain runtime configurations where the response stream might have already been sent. To ensure headers are set correctly, consider retrieving the response from `context.GetInvocationResult().Value` and setting headers before the response is returned from your function, rather than attempting to modify them in middleware after function execution completes.

For a more complete example of using custom middleware in your function app, see the [custom middleware reference sample](https://github.com/Azure/azure-functions-dotnet-worker/blob/main/samples/CustomMiddleware).

The isolated worker model uses `System.Text.Json` by default. You can customize the behavior of the serializer by configuring services as part of your `Program.cs` file. This section covers general-purpose serialization and doesn't influence [HTTP trigger JSON serialization with ASP.NET Core integration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#json-serialization-with-aspnet-core-integration), which you must configure separately.

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_6_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_6_hostbuilder)

```
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.ConfigureFunctionsWebApplication();

builder.Services.Configure<JsonSerializerOptions>(jsonSerializerOptions =>
    {
        jsonSerializerOptions.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;
        jsonSerializerOptions.DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull;
        jsonSerializerOptions.ReferenceHandler = ReferenceHandler.Preserve;

        // override the default value
        jsonSerializerOptions.PropertyNameCaseInsensitive = false;
    });

builder.Build().Run();
```

To use JSON.NET (`Newtonsoft.Json`) for serialization, install the [`Microsoft.Azure.Core.NewtonsoftJson`](https://www.nuget.org/packages/Microsoft.Azure.Core.NewtonsoftJson) package. Then, in your service registration, reassign the `Serializer` property on the `WorkerOptions` configuration. The following example shows this configuration by using `ConfigureFunctionsWebApplication`, but it also works for `ConfigureFunctionsWorkerDefaults`:

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_7_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_7_hostbuilder)

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.ConfigureFunctionsWebApplication();

builder.Services.Configure<WorkerOptions>(workerOptions =>
    {
        var settings = NewtonsoftJsonObjectSerializer.CreateJsonSerializerSettings();
        settings.ContractResolver = new CamelCasePropertyNamesContractResolver();
        settings.NullValueHandling = NullValueHandling.Ignore;

        workerOptions.Serializer = new NewtonsoftJsonObjectSerializer(settings);
    });

builder.Build().Run();
```

A function method is a public method of a public class with a `Function` attribute applied to the method and a trigger attribute applied to an input parameter, as shown in the following example:

```
[Function(nameof(QueueInputOutputFunction))]
[QueueOutput("output-queue")]
public string[] QueueInputOutputFunction([QueueTrigger("input-queue")] Album myQueueItem, FunctionContext context)
```

The trigger attribute specifies the trigger type and binds input data to a method parameter. The preceding example function is triggered by a queue message, and the queue message is passed to the method in the `myQueueItem` parameter.

The `Function` attribute marks the method as a function entry point. The name must be unique within a project, start with a letter, and only contain letters, numbers, `_`, and `-`, up to 127 characters in length. Project templates often create a method named `Run`, but the method name can be any valid C# method name. The method must be a public member of a public class. It should generally be an instance method so that services can be passed in via [dependency injection](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#dependency-injection).

Here are some of the parameters that you can include as part of a function method signature:

*   [Bindings](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#bindings), which are marked as such by decorating the parameters as attributes. The function must contain exactly one trigger parameter.
*   An [execution context object](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#execution-context), which provides information about the current invocation.
*   A [cancellation token](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#cancellation-tokens), used for graceful shutdown.

In the isolated worker model, the worker process passes a [FunctionContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.functioncontext?view=azure-dotnet&preserve-view=true) object to your function methods. This object lets you get an [`ILogger`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger) instance to write to the logs by calling the [GetLogger](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.functioncontextloggerextensions.getlogger) method and supplying a `categoryName` string. You can use this context to obtain an [`ILogger`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger) without having to use dependency injection. For more information, see [Logging](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#logging).

A function can accept a [cancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) parameter, which enables the operating system to notify your code when the function is about to be terminated. You can use this notification to make sure the function doesn't terminate unexpectedly in a way that leaves data in an inconsistent state.

.NET functions that run in an isolated worker process support cancellation tokens. The following example raises an exception when a cancellation request is received:

```
[Function(nameof(ThrowOnCancellation))]
public async Task ThrowOnCancellation(
    [EventHubTrigger("sample-workitem-1", Connection = "EventHubConnection")] string[] messages,
    FunctionContext context,
    CancellationToken cancellationToken)
{
    _logger.LogInformation("C# EventHub {functionName} trigger function processing a request.", nameof(ThrowOnCancellation));

    foreach (var message in messages)
    {
        cancellationToken.ThrowIfCancellationRequested();
        await Task.Delay(6000); // task delay to simulate message processing
        _logger.LogInformation("Message '{msg}' was processed.", message);
    }
}
```

The following example performs clean-up actions when a cancellation request is received:

```
[Function(nameof(HandleCancellationCleanup))]
public async Task HandleCancellationCleanup(
    [EventHubTrigger("sample-workitem-2", Connection = "EventHubConnection")] string[] messages,
    FunctionContext context,
    CancellationToken cancellationToken)
{
    _logger.LogInformation("C# EventHub {functionName} trigger function processing a request.", nameof(HandleCancellationCleanup));

    foreach (var message in messages)
    {
        if (cancellationToken.IsCancellationRequested)
        {
            _logger.LogInformation("A cancellation token was received, taking precautionary actions.");
            // Take precautions like noting how far along you are with processing the batch
            _logger.LogInformation("Precautionary activities complete.");
            break;
        }

        await Task.Delay(6000); // task delay to simulate message processing
        _logger.LogInformation("Message '{msg}' was processed.", message);
    }
}
```

The cancellation token is signaled when the function invocation is canceled. Several reasons could lead to a cancellation, and those reasons vary depending on the trigger type being used. Some common reasons are:

*   Client disconnect: The client that is invoking your function disconnects. This reason is most likely for HTTP trigger functions.
*   Function app restart: You or the platform restart (or stop) the function app around the same time an invocation is requested. A restart can occur due to worker instance movements, worker instance updates, or scaling.

*   Invocations in-flight during a restart event might be retried depending on how they were triggered. For more information, see the [retry documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages#retries).

*   The host sends the invocation through to the worker _even_ if the cancellation token is canceled _before_ the host is able to send the invocation request to the worker.

*   If you don't want pre-canceled invocations to be sent to the worker, add the `SendCanceledInvocationsToWorker` property to your `host.json` file to disable this behavior.

This example shows a `host.json` file that uses this property:

```
{
    "version": "2.0",
    "SendCanceledInvocationsToWorker": "false"
}
```
*   Setting `SendCanceledInvocationsToWorker` to `false` might lead to a `FunctionInvocationCanceled` exception with the following log:

> Cancellation has been requested. The invocation request with id '{invocationId}' is canceled and won't be sent to the worker.

This exception occurs when the cancellation token is canceled (as a result of one of the events described earlier) _before_ the host sends an incoming invocation request to the worker. This exception can be safely ignored and is expected when `SendCanceledInvocationsToWorker` is `false`.

The .NET isolated worker doesn't set a custom [`SynchronizationContext`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.synchronizationcontext). This means that `SynchronizationContext.Current` is `null` during function execution. After an `await`, continuations are scheduled on the thread pool, which is the standard .NET behavior.

Because there's no `SynchronizationContext` to suppress, using [`ConfigureAwait(false)`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.configureawait) in your function code has no practical effect. The isolated worker process runs as a standard .NET generic host (console app), so the same async/await behavior you'd expect in any ASP.NET Core or console application applies here. This is also true for .NET Framework (net48) isolated worker apps, since the worker process is always a console executable using `HostBuilder`.

Note

[Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview) orchestrators have their own threading constraints. The orchestrator replay thread must run continuations, so using `ConfigureAwait(false)` in orchestrator functions or orchestrator middleware can interfere with orchestration execution. For more information, see the [Durable Functions code constraints](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-code-constraints).

Define bindings by using attributes on methods, parameters, and return types. Bindings can provide data as strings, arrays, and serializable types, such as plain old class objects (POCOs). For some binding extensions, you can also [bind to service-specific types](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#sdk-types) defined in service SDKs.

For HTTP triggers, see the [HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#http-trigger) section.

For a complete set of reference samples that use triggers and bindings with isolated worker process functions, see the [binding extensions reference sample](https://github.com/Azure/azure-functions-dotnet-worker/blob/main/samples/Extensions).

A function can have zero or more input bindings that pass data to the function. Like triggers, you define input bindings by applying a binding attribute to an input parameter. When the function executes, the runtime tries to get data specified in the binding. The data being requested often depends on information provided by the trigger through binding parameters.

To write to an output binding, you must apply an output binding attribute to the function method. This attribute defines how to write to the bound service. The method's return value is written to the output binding. For example, the following example writes a string value to a message queue named `output-queue` by using an output binding:

```
[Function(nameof(QueueInputOutputFunction))]
[QueueOutput("output-queue")]
public string[] QueueInputOutputFunction([QueueTrigger("input-queue")] Album myQueueItem, FunctionContext context)
{
    // Use a string array to return more than one message.
    string[] messages = {
        $"Album name = {myQueueItem.Name}",
        $"Album songs = {myQueueItem.Songs}"};

    _logger.LogInformation("{msg1},{msg2}", messages[0], messages[1]);

    // Queue Output messages
    return messages;
}
```

The data written to an output binding is always the return value of the function. If you need to write to more than one output binding, you must create a custom return type. This return type must have the output binding attribute applied to one or more properties of the class. The following example is an HTTP-triggered function that uses [ASP.NET Core integration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) and writes to both the HTTP response and a queue output binding:

```
public class MultipleOutputBindings
{
    private readonly ILogger<MultipleOutputBindings> _logger;

    public MultipleOutputBindings(ILogger<MultipleOutputBindings> logger)
    {
        _logger = logger;
    }

    [Function("MultipleOutputBindings")]
    public MyOutputType Run([HttpTrigger(AuthorizationLevel.Function, "post")] HttpRequest req)
    {
        _logger.LogInformation("C# HTTP trigger function processed a request.");
        var myObject = new MyOutputType
        {
            Result = new OkObjectResult("C# HTTP trigger function processed a request."),
            MessageText = "some output"
        };
        return myObject;
    }

    public class MyOutputType
    {
        [HttpResult]
        public IActionResult Result { get; set; }

        [QueueOutput("myQueue")]
        public string MessageText { get; set; }
    }
}
```

When you use custom return types for multiple output bindings with ASP.NET Core integration, you must add the `[HttpResult]` attribute to the property that provides the result. The `HttpResult` attribute is available when using [SDK 1.17.3-preview2 or later](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Sdk/1.17.3-preview2) along with [version 3.2.0 or later of the HTTP extension](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.Http/3.2.0) and [version 1.3.0 or later of the ASP.NET Core extension](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore/1.3.0).

For some service-specific binding types, you can provide binding data by using types from service SDKs and frameworks. These types offer capabilities beyond what a serialized string or plain-old CLR object (POCO) can provide. To use the newer types, update your project to use newer versions of core dependencies.

| Dependency | Version requirement |
| --- | --- |
| [Microsoft.Azure.Functions.Worker](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker/) | 1.18.0 or later |
| [Microsoft.Azure.Functions.Worker.Sdk](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Sdk/) | 1.13.0 or later |

When testing SDK types locally on your machine, you also need to use [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local), version 4.0.5000 or later. You can check your current version by using the `func --version` command.

Each binding extension also has its own minimum version requirement, which is described in the extension reference articles. These binding extensions currently support SDK types:

| Extension | Types | Support level |
| --- | --- | --- |
| [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `BlobClient` `BlobContainerClient` `BlockBlobClient` `PageBlobClient` `AppendBlobClient` | Trigger: GA Input: GA |
| [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2?tabs=isolated-process,extensionv4&pivots=programming-language-csharp#binding-types) | `CosmosClient` `Database` `Container` | Input: GA |
| [Azure Event Grid](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid?tabs=isolated-process,extensionv3&pivots=programming-language-csharp#binding-types) | `CloudEvent` `EventGridEvent` | Trigger: GA |
| [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `EventData` `EventHubProducerClient` | Trigger: GA |
| [Azure Queue Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `QueueClient` `QueueMessage` | Trigger: GA |
| [Azure Service Bus](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus?tabs=isolated-process,extensionv5&pivots=programming-language-csharp#binding-types) | `ServiceBusClient` `ServiceBusReceiver` `ServiceBusSender` `ServiceBusMessage` | Trigger: GA |
| [Azure Table Storage](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table?tabs=isolated-process,table-api&pivots=programming-language-csharp#binding-types) | `TableClient` `TableEntity` | Input: GA |

Considerations for SDK types:

*   When using [binding expressions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns) that rely on trigger data, SDK types for the trigger itself cannot be used.
*   For output scenarios where you might use an SDK type, create and work with SDK clients directly instead of using an output binding.
*   The Azure Cosmos DB trigger uses the [Azure Cosmos DB change feed](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed) and exposes change feed items as JSON-serializable types. As a result, SDK types aren't supported for this trigger.

[HTTP triggers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger) allow a function to be invoked by an HTTP request. You can use two different approaches:

*   An [ASP.NET Core integration model](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) that uses concepts familiar to ASP.NET Core developers
*   A [built-in model](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#built-in-http-model), which doesn't require extra dependencies and uses custom types for HTTP requests and responses. This approach is maintained for backward compatibility with previous .NET isolated worker apps.

This section shows how to work with the underlying HTTP request and response objects by using types from ASP.NET Core, including [HttpRequest](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest), [HttpResponse](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpresponse), and [IActionResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.iactionresult). This model isn't available to [apps targeting .NET Framework](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#supported-versions), which should instead use the [built-in model](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#built-in-http-model).

Note

This model doesn't expose all features of ASP.NET Core. Specifically, it doesn't provide access to the ASP.NET Core middleware pipeline and routing capabilities. ASP.NET Core integration requires you to use updated packages.

To enable ASP.NET Core integration for HTTP:

1.   Add a reference in your project to the [Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore/) package, version 1.0.0 or later.

2.   Update your project to use these specific package versions:

    *   [Microsoft.Azure.Functions.Worker.Sdk](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Sdk/), version 1.11.0. or later
    *   [Microsoft.Azure.Functions.Worker](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker/), version 1.16.0 or later.

3.   In your `Program.cs` file, update the host builder configuration to call `ConfigureFunctionsWebApplication()`. This method replaces `ConfigureFunctionsWorkerDefaults()` if you would use that method otherwise. The following example shows a minimal setup without other customizations:

    *   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_8_hostbuilder)
    *   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_8_ihostapplicationbuilder)

```
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.ConfigureFunctionsWebApplication();    

builder.Build().Run();
```

4.   Update any existing HTTP-triggered functions to use the ASP.NET Core types. This example shows the standard `HttpRequest` and an `IActionResult` used for a simple "hello, world" function:

```
[Function("HttpFunction")]
public IActionResult Run(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get")] HttpRequest req)
{
    return new OkObjectResult($"Welcome to Azure Functions, {req.Query["name"]}!");
}
```

ASP.NET Core has its own serialization layer, and it isn't affected by [customizing general serialization configuration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#customizing-json-serialization). To customize the serialization behavior used for your HTTP triggers, you need to include an `.AddMvc()` call as part of service registration. The returned `IMvcBuilder` can be used to modify ASP.NET Core's JSON serialization settings.

You can continue to use `HttpRequestData` and `HttpResponseData` while using ASP.NET integration, though for most apps, it's better to instead use `HttpRequest` and `IActionResult`. Using `HttpRequestData`/`HttpResponseData` doesn't invoke the ASP.NET Core serialization layer and instead relies upon the [general worker serialization configuration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#customizing-json-serialization) for the app. However, when ASP.NET Core integration is enabled, you might still need to add configuration. The default behavior from ASP.NET Core is to disallow synchronous IO. To use a custom serializer that doesn't support asynchronous IO, such as `NewtonsoftJsonObjectSerializer`, you need to enable synchronous IO for your application by configuring the `KestrelServerOptions`.

The following example shows how to configure JSON.NET (`Newtonsoft.Json`) and the [Microsoft.AspNetCore.Mvc.NewtonsoftJson NuGet package](https://www.nuget.org/packages/Microsoft.AspNetCore.Mvc.NewtonsoftJson) for serialization using this approach:

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_9_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_9_hostbuilder)

```
using Microsoft.AspNetCore.Server.Kestrel.Core;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.ConfigureFunctionsWebApplication();

builder.Services
    .AddApplicationInsightsTelemetryWorkerService()
    .ConfigureFunctionsApplicationInsights();

builder.Services.AddMvc().AddNewtonsoftJson();

// Only needed if using HttpRequestData/HttpResponseData and a serializer that doesn't support asynchronous IO
// builder.Services.Configure<KestrelServerOptions>(options => options.AllowSynchronousIO = true);

builder.Build().Run();
```

In the built-in model, the system translates the incoming HTTP request message into an [HttpRequestData](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.http.httprequestdata?view=azure-dotnet&preserve-view=true) object that it passes to the function. This object provides data from the request, including `Headers`, `Cookies`, `Identities`, `URL`, and optionally a message `Body`. This object represents the HTTP request but isn't directly connected to the underlying HTTP listener or the received message.

Important

If you use `HttpRequestData`, the body of the HTTP request can't be a stream. For example, if the request has the `Transfer-Encoding: chunked` header and no `Content-Length` header, the `HttpRequestData` object's `Body` property will be a null stream. If you need to work with streaming HTTP requests, consider using the [ASP.NET Core integration model](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) instead.

Likewise, the function returns an [HttpResponseData](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.http.httpresponsedata?view=azure-dotnet&preserve-view=true) object, which provides data used to create the HTTP response, including message `StatusCode`, `Headers`, and optionally a message `Body`.

The following example demonstrates the use of `HttpRequestData` and `HttpResponseData`:

```
[Function(nameof(HttpFunction))]
public static HttpResponseData Run([HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequestData req,
    FunctionContext executionContext)
{
    var logger = executionContext.GetLogger(nameof(HttpFunction));
    logger.LogInformation("message logged");

    var response = req.CreateResponse(HttpStatusCode.OK);
    response.Headers.Add("Content-Type", "text/plain; charset=utf-8");
    response.WriteString("Welcome to .NET isolated worker !!");

    return response;
}
```

You can write to logs by using an [`ILogger<T>`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1) or [`ILogger`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger) instance. You can get the logger through [dependency injection](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#dependency-injection) of an [`ILogger<T>`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1) or of an [ILoggerFactory](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.iloggerfactory):

```
public class MyFunction {
    
    private readonly ILogger<MyFunction> _logger;
    
    public MyFunction(ILogger<MyFunction> logger) {
        _logger = logger;
    }
    
    [Function(nameof(MyFunction))]
    public void Run([BlobTrigger("samples-workitems/{name}", Connection = "")] string myBlob, string name)
    {
        _logger.LogInformation($"C# Blob trigger function Processed blob\n Name: {name} \n Data: {myBlob}");
    }

}
```

Note

When you inject an `ILogger<T>` in your class constructor, like the previous example, the log category is automatically set to the fully qualified name of that class, such as `MyFunctionApp.MyFunction`. These category names contain `.` (period) characters. When you host your function app on Linux, you can't use environment variables to override log levels for categories that contain periods. To work around this limitation, you can instead [configure log levels in your code](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#managing-log-levels) or in an `appsettings.json` file.

You can also get the logger from a [FunctionContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.functioncontext?view=azure-dotnet&preserve-view=true) object passed to your function. Call the [GetLogger<T>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.functioncontextloggerextensions.getlogger#microsoft-azure-functions-worker-functioncontextloggerextensions-getlogger-1) or [GetLogger](https://learn.microsoft.com/en-us/dotnet/api/microsoft.azure.functions.worker.functioncontextloggerextensions.getlogger) method, passing a string value that is the name for the category in which the logs are written. The category is usually the name of the specific function from which the logs are written. For more information about categories, see the [monitoring article](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring#log-levels-and-categories).

Use the methods of [`ILogger<T>`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger-1) and [`ILogger`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger) to write various log levels, such as `LogWarning` or `LogError`. For more information about log levels, see the [monitoring article](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring#log-levels-and-categories). You can customize the log levels for components added to your code by registering filters:

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_10_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_10_hostbuilder)

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

var builder = FunctionsApplication.CreateBuilder(args);

builder.ConfigureFunctionsWebApplication();

// Registers IHttpClientFactory.
// By default this sends a lot of Information-level logs.
builder.Services.AddHttpClient();

// Disable IHttpClientFactory Informational logs.
// Note -- you can also remove the handler that does the logging: https://github.com/aspnet/HttpClientFactory/issues/196#issuecomment-432755765 
builder.Logging.AddFilter("System.Net.Http.HttpClient", LogLevel.Warning);
    
builder.Build().Run();
```

As part of configuring your app in `Program.cs`, you can also define the behavior for how errors are surfaced to your logs. The default behavior depends on the type of builder you're using.

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_11_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_11_hostbuilder)

When you use an `IHostApplicationBuilder`, exceptions thrown by your code flow through the system without changes. You don't need any other configuration.

You can configure your isolated process application to send logs directly to [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview?tabs=net). This configuration replaces the default behavior of [relaying logs through the host](https://learn.microsoft.com/en-us/azure/azure-functions/configure-monitoring#custom-application-logs). Unless you're using [Aspire](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspire), configure direct Application Insights integration because it gives you control over how those logs are emitted.

Application Insights integration isn't enabled by default in all setup experiences. Some templates create Functions projects with the necessary packages and startup code commented out. If you want to use Application Insights integration, uncomment these lines in `Program.cs` and the project's `.csproj` file. The instructions in the rest of this section also describe how to enable the integration.

If your project is part of an [Aspire orchestration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspire), it uses OpenTelemetry for monitoring instead. Don't enable direct Application Insights integration within Aspire projects. Instead, configure the Azure Monitor OpenTelemetry exporter as part of the [service defaults project](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/service-defaults#opentelemetry-configuration). If your Functions project uses Application Insights integration in an Aspire context, the application errors on startup.

To write logs directly to Application Insights from your code, add references to these packages in your project:

*   [Microsoft.Azure.Functions.Worker.ApplicationInsights](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.ApplicationInsights/), version 1.0.0 or later.
*   [Microsoft.ApplicationInsights.WorkerService](https://www.nuget.org/packages/Microsoft.ApplicationInsights.WorkerService).

Run the following commands to add these references to your project:

```
dotnet add package Microsoft.ApplicationInsights.WorkerService
dotnet add package Microsoft.Azure.Functions.Worker.ApplicationInsights
```

After installing the packages, call `AddApplicationInsightsTelemetryWorkerService()` and `ConfigureFunctionsApplicationInsights()` during service configuration in your `Program.cs` file, as shown in the following example:

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_12_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_12_hostbuilder)

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
    
var builder = FunctionsApplication.CreateBuilder(args);

builder.Services
    .AddApplicationInsightsTelemetryWorkerService()
    .ConfigureFunctionsApplicationInsights();

builder.Build().Run();
```

The call to `ConfigureFunctionsApplicationInsights()` adds an `ITelemetryModule` that listens to a Functions-defined `ActivitySource`. This module creates the dependency telemetry required to support distributed tracing. For more information about `AddApplicationInsightsTelemetryWorkerService()` and how to use it, see [Application Insights for Worker Service applications](https://learn.microsoft.com/en-us/azure/azure-monitor/app/worker-service).

Important

The Functions host and the isolated process worker have separate configuration for log levels. Any [Application Insights configuration in host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json#applicationinsights) doesn't affect logging from the worker, and similarly, configuration in your worker code doesn't impact logging from the host. Apply changes in both places if your scenario requires customization at both layers.

The rest of your application continues to work with `ILogger` and `ILogger<T>`. However, by default, the Application Insights SDK adds a logging filter that instructs the logger to capture only warnings and more severe logs. You can configure log levels in the isolated worker process in one of these ways:

| Configuration method | Benefits |
| --- | --- |
| In your code | Promotes a clearer separation between host-side and worker-side configurations. |
| Using `appsettings.json` | Useful when you want to set different log levels for different categories without having to modify your code. |

*   [Code-based](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_13_code_ihostapplicationbuilder)
*   [Configuration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_13_config_ihostapplicationbuilder)

To disable the default behavior and capture all log levels, remove the filter rule as part of service configuration:

```
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

var builder = FunctionsApplication.CreateBuilder(args);

builder.Services
    .AddApplicationInsightsTelemetryWorkerService()
    .ConfigureFunctionsApplicationInsights();

builder.Logging.Services.Configure<LoggerFilterOptions>(options =>
    {
        LoggerFilterRule? defaultRule = options.Rules.FirstOrDefault(rule => rule.ProviderName
            == "Microsoft.Extensions.Logging.ApplicationInsights.ApplicationInsightsLoggerProvider");
        if (defaultRule is not null)
        {
            options.Rules.Remove(defaultRule);
        }
    });

builder.Build().Run();
```

For more information about configuring logging, see [Logging in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging) and [Application Insights for Worker Service applications](https://learn.microsoft.com/en-us/azure/azure-monitor/app/worker-service#ilogger-logs).

This section outlines options you can enable that improve performance around [cold start](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling#cold-start).

In general, your app should use the latest versions of its core dependencies. At a minimum, update your project as follows:

1.   Upgrade [Microsoft.Azure.Functions.Worker](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker/) to version 1.19.0 or later.
2.   Upgrade [Microsoft.Azure.Functions.Worker.Sdk](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Sdk/) to version 1.16.4 or later.
3.   Add a framework reference to `Microsoft.AspNetCore.App`, unless your app targets .NET Framework.

The following snippet shows this configuration in the context of a project file:

```
<ItemGroup>
    <FrameworkReference Include="Microsoft.AspNetCore.App" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker" Version="1.21.0" />
    <PackageReference Include="Microsoft.Azure.Functions.Worker.Sdk" Version="1.16.4" />
  </ItemGroup>
```

Placeholders are a platform capability that improves cold start for apps targeting .NET 6 or later. To use this optimization, you must explicitly enable placeholders by following these steps:

1.   Update your project configuration to use the latest dependency versions, as detailed in the previous section.

2.   Set the [`WEBSITE_USE_PLACEHOLDER_DOTNETISOLATED`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_use_placeholder_dotnetisolated) application setting to `1`. Use this [az functionapp config appsettings set](https://learn.microsoft.com/en-us/cli/azure/functionapp/config/appsettings#az-functionapp-config-appsettings-set) command:

```
az functionapp config appsettings set -g <groupName> -n <appName> --settings 'WEBSITE_USE_PLACEHOLDER_DOTNETISOLATED=1'
```

In this example, replace `<groupName>` with the name of the resource group, and replace `<appName>` with the name of your function app.

3.   Make sure that the [`netFrameworkVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#netframeworkversion) property of the function app matches your project's target framework, which must be .NET 6 or later. Use this [az functionapp config set](https://learn.microsoft.com/en-us/cli/azure/functionapp/config#az-functionapp-config-set) command:

```
az functionapp config set -g <groupName> -n <appName> --net-framework-version <framework>
```

In this example, also replace `<framework>` with the appropriate version string, such as `v8.0`, according to your target .NET version.

4.   Make sure that your function app is configured to use a 64-bit process. Use this [az functionapp config set](https://learn.microsoft.com/en-us/cli/azure/functionapp/config#az-functionapp-config-set) command:

```
az functionapp config set -g <groupName> -n <appName> --use-32bit-worker-process false
```

The function executor is a component of the platform that causes invocations to run. An optimized version of this component is enabled by default starting with version 1.16.2 of the SDK. No other configuration is required.

You can compile your function app as [ReadyToRun binaries](https://learn.microsoft.com/en-us/dotnet/core/deploying/ready-to-run). ReadyToRun is a form of ahead-of-time compilation that can improve startup performance to help reduce the effect of cold starts when running in a [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan). ReadyToRun is available in .NET 6 and later versions and requires [version 4.0 or later](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions) of the Azure Functions runtime.

ReadyToRun requires you to build the project against the runtime architecture of the hosting app. When these architectures aren't aligned, your app encounters an error at startup. Select your runtime identifier from this table:

| Operating System | App is 32-bit 1 | Runtime identifier |
| --- | --- | --- |
| Windows | True | `win-x86` |
| Windows | False | `win-x64` |
| Linux | True | N/A (not supported) |
| Linux | False | `linux-x64` |

1 Only 64-bit apps are eligible for some other performance optimizations.

To check if your Windows app is 32-bit or 64-bit, run the following CLI command, substituting `<group_name>` with the name of your resource group and `<app_name>` with the name of your application. An output of "true" indicates that the app is 32-bit, and "false" indicates 64-bit.

```
az functionapp config show -g <group_name> -n <app_name> --query "use32BitWorkerProcess"
```

You can change your application to 64-bit with the following command, using the same substitutions:

```
az functionapp config set -g <group_name> -n <app_name> --use-32bit-worker-process false`
```

To compile your project as ReadyToRun, update your project file by adding the `<PublishReadyToRun>` and `<RuntimeIdentifier>` elements. The following example shows a configuration for publishing to a Windows 64-bit function app.

```
<PropertyGroup>
  <TargetFramework>net8.0</TargetFramework>
  <AzureFunctionsVersion>v4</AzureFunctionsVersion>
  <RuntimeIdentifier>win-x64</RuntimeIdentifier>
  <PublishReadyToRun>true</PublishReadyToRun>
</PropertyGroup>
```

If you don't want to set the `<RuntimeIdentifier>` as part of the project file, you can also configure this setting as part of the publishing gesture itself. For example, with a Windows 64-bit function app, the .NET CLI command is:

```
dotnet publish --runtime win-x64
```

In Visual Studio, set the **Target Runtime** option in the publish profile to the correct runtime identifier. When set to the default value of **Portable**, ReadyToRun isn't used.

When you deploy your function code project to Azure, it must run in either a function app or in a Linux container. You must create the function app and other required Azure resources before you deploy your code.

You can also deploy your function app in a Linux container. For more information, see [Working with containers and Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-custom-container).

You can create your function app and other required resources in Azure by using one of these methods:

*   [Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs#publish-to-azure): Visual Studio can create resources for you during the code publishing process.
*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code#publish-to-azure): Visual Studio Code can connect to your subscription, create the resources needed by your app, and then publish your code.
*   [Azure CLI](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-csharp#create-supporting-azure-resources-for-your-function): Use the Azure CLI to create the required resources in Azure.
*   [Azure PowerShell](https://learn.microsoft.com/en-us/azure/azure-functions/create-resources-azure-powershell#create-a-serverless-function-app-for-c): Use Azure PowerShell to create the required resources in Azure.
*   [Deployment templates](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code): Use ARM templates and Bicep files to automate the deployment of the required resources to Azure. Make sure your template includes any [required settings](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#deployment-requirements).
*   [Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal): Create the required resources in the [Azure portal](https://portal.azure.com/).

After creating your function app and other required resources in Azure, deploy the code project to Azure by using one of these methods:

*   [Visual Studio](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs#publish-to-azure): Simple manual deployment during development.
*   [Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=isolated-process&pivots=programming-language-csharp#republish-project-files): Simple manual deployment during development.
*   [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linuxisolated-process&pivots=programming-language-csharp#project-file-deployment): Deploy project file from the command line.
*   [Continuous deployment](https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment): Useful for ongoing maintenance, frequently to a [staging slot](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots).
*   [Deployment templates](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code#zip-deployment-package): You can use ARM templates or Bicep files to automate package deployments.

For more information, see [Deployment technologies in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies).

Many of the deployment methods use a zip archive. If you create the zip archive yourself, it must follow the structure outlined in this section. If it doesn't, your app might experience errors at startup.

The deployment payload should match the output of a `dotnet publish` command, though without the enclosing parent folder. The zip archive should be made from the following files:

*   `.azurefunctions/`
*   `extensions.json`
*   `functions.metadata`
*   `host.json`
*   `worker.config.json`
*   Your project executable (a console app)
*   Other supporting files and directories peer to that executable

The build process generates these files, and you shouldn't edit them directly.

Tip

You can use the `func pack` command in Core Tools to correctly generate a zip archive for deployment. Support for `func pack` is currently in preview.

When preparing a zip archive for deployment, compress only the contents of the output directory, not the enclosing directory itself. When the archive is extracted into the current working directory, the files listed earlier need to be immediately visible.

To run .NET functions in the isolated worker model in Azure, you need to meet a few requirements. The requirements depend on the operating system:

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_14_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_14_linux)

*   Set [FUNCTIONS_WORKER_RUNTIME](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_runtime) to `dotnet-isolated`.
*   Set [`linuxFxVersion`](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#linuxfxversion) to the [correct base image](https://learn.microsoft.com/en-us/azure/azure-functions/update-language-versions?tabs=azure-cli,linux&pivots=programming-language-csharp#update-the-stack-configuration), like `DOTNET-ISOLATED|8.0`.

When you create your function app in Azure using the methods in the previous section, these required settings are added for you. When you create these resources [by using ARM templates or Bicep files for automation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-infrastructure-as-code), you must make sure to set them in the template.

[Aspire](https://learn.microsoft.com/en-us/dotnet/aspire/get-started/aspire-overview) is an opinionated stack that simplifies development of distributed applications in the cloud. You can enlist isolated worker model projects in Aspire 13 orchestrations. See [Azure Functions with Aspire](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-aspire-integration) for more information.

When running locally using Visual Studio or Visual Studio Code, you're able to debug your .NET isolated worker project as normal. However, there are two debugging scenarios that don't work as expected.

Because your isolated worker process app runs outside the Functions runtime, you need to attach the remote debugger to a separate process. To learn more about debugging using Visual Studio, see [Remote Debugging](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs?tabs=isolated-process#remote-debugging).

If your isolated project targets .NET Framework 4.8, you need to take manual steps to enable debugging. These steps aren't required if using another target framework.

Your app should start with a call to `FunctionsDebugger.Enable();` as its first operation. This occurs in the `Main()` method before initializing a HostBuilder. Your `Program.cs` file should look similar to this:

*   [IHostApplicationBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_15_ihostapplicationbuilder)
*   [IHostBuilder](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_15_hostbuilder)

```
using System;
using System.Diagnostics;
using Microsoft.Extensions.Hosting;
using Microsoft.Azure.Functions.Worker;
using NetFxWorker;

namespace MyDotnetFrameworkProject
{
    internal class Program
    {
        static void Main(string[] args)
        {
            FunctionsDebugger.Enable();

            var host = FunctionsApplication
                .CreateBuilder(args)
                .Build();

            host.Run();
        }
    }
}
```

Next, you need to manually attach to the process using a .NET Framework debugger. Visual Studio doesn't do this automatically for isolated worker process .NET Framework apps yet, and the "Start Debugging" operation should be avoided.

In your project directory (or its build output directory), run:

```
func host start --dotnet-isolated-debug
```

This starts your worker, and the process stops with the following message:

```
Azure Functions .NET Worker (PID: <process id>) initialized in debug mode. Waiting for debugger to attach...
```

Where `<process id>` is the ID for your worker process. You can now use Visual Studio to manually attach to the process. For instructions on this operation, see [How to attach to a running process](https://learn.microsoft.com/en-us/visualstudio/debugger/attach-to-running-processes-with-the-visual-studio-debugger#BKMK_Attach_to_a_running_process).

After the debugger is attached, the process execution resumes, and you'll be able to debug.

Before a generally available release, a .NET version might be released in a _Preview_ or _Go-live_ state. See the [.NET Official Support Policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-core) for details on these states.

While it might be possible to target a given release from a local Functions project, function apps hosted in Azure might not have that release available. Azure Functions can only be used with Preview or Go-live releases noted in this section.

Azure Functions doesn't currently work with any "Preview" or "Go-live" .NET releases. See [Supported versions](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#supported-versions) for a list of generally available releases that you can use.

To use Azure Functions with a preview version of .NET, you need to update your project by:

1.   Installing the relevant .NET SDK version in your development
2.   Changing the `TargetFramework` setting in your `.csproj` file

When you deploy to your function app in Azure, you also need to ensure that the framework is made available to the app. During the preview period, some tools and experiences may not surface the new preview version as an option. If you don't see the preview version included in the Azure portal, for example, you can use the REST API, Bicep files, or the Azure CLI to configure the version manually.

*   [Windows](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_16_windows)
*   [Linux](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#tabpanel_16_linux)

For apps hosted on Linux, use the following Azure CLI command. Replace `<groupName>` with the name of the resource group, and replace `<appName>` with the name of your function app. Replace `<version>` with the appropriate version string, such as `8.0`.

```
az functionapp config set -g <groupName> -n <appName> --linux-fx-version "dotnet-isolated|<version>"
```

Keep these considerations in mind when using Functions with preview versions of .NET:

*   When you author your functions in Visual Studio, you must use [Visual Studio Insiders](https://visualstudio.microsoft.com/insiders/), which supports building Azure Functions projects with .NET preview SDKs.

*   Make sure you have the latest Functions tools and templates. To update your tools:

    1.   Navigate to **Tools**>**Options**, choose **Azure Functions** under **Projects and Solutions**>**More Settings**.
    2.   Select **Check for updates** and install updates as prompted.

*   During a preview period, your development environment might have a more recent version of the .NET preview than the hosted service. This can cause your function app to fail when deployed. To address this, you can specify the version of the SDK to use in [`global.json`](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json).

    1.   Run the `dotnet --list-sdks` command and note the preview version you're currently using during local development.
    2.   Run the `dotnet new globaljson --sdk-version <SDK_VERSION> --force` command, where `<SDK_VERSION>` is the version you're using locally. For example, `dotnet new globaljson --sdk-version dotnet-sdk-10.0.100-preview.5.25277.114 --force` causes the system to use the .NET 10 Preview 5 SDK when building your project.

Note

Because of the just-in-time loading of preview frameworks, function apps running on Windows can experience increased cold start times when compared against earlier GA versions.
