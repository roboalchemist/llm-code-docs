# Source: https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0

Title: Code samples migrated to the new minimal hosting model in 6.0

URL Source: https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0

Markdown Content:
This article provides samples of code migrated to ASP.NET Core in .NET 6. ASP.NET Core in .NET 6 uses a new minimal hosting model. For more information, see [New hosting model](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#nhm).

The following code adds the Static File Middleware to a .NET 5 app:

```
public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.UseStaticFiles();
    }
}
```

The following code adds the Static File Middleware to an ASP.NET Core in .NET 6 app:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseStaticFiles();

app.Run();
```

[WebApplication.CreateBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.createbuilder) initializes a new instance of the [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) class with preconfigured defaults. For more information, see [ASP.NET Core Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-6.0)

The following code adds an endpoint to an .NET 5 app:

```
public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.UseRouting();
        app.UseEndpoints(endpoints =>
        {
            endpoints.MapGet("/", () => "Hello World");
        });
    }
}
```

In .NET 6, routes can be added directly to the [WebApplication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication) without an explicit call to [UseEndpoints](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.useendpoints) or [UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting). The following code adds an endpoint to an ASP.NET Core in .NET 6 app:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
```

**Note:** Routes added directly to the [WebApplication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication) execute at the _**end**_ of the pipeline.

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .UseContentRoot(Directory.GetCurrentDirectory())
        .UseEnvironment(Environments.Staging)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>()
                      .UseSetting(WebHostDefaults.ApplicationKey,
                                  typeof(Program).Assembly.FullName);
        });
```

```
var builder = WebApplication.CreateBuilder(new WebApplicationOptions
{
    Args = args,
    ApplicationName = typeof(Program).Assembly.FullName,
    ContentRootPath = Directory.GetCurrentDirectory(),
    EnvironmentName = Environments.Staging,
    WebRootPath = "customwwwroot"
});

Console.WriteLine($"Application Name: {builder.Environment.ApplicationName}");
Console.WriteLine($"Environment Name: {builder.Environment.EnvironmentName}");
Console.WriteLine($"ContentRoot Path: {builder.Environment.ContentRootPath}");
Console.WriteLine($"WebRootPath: {builder.Environment.WebRootPath}");

var app = builder.Build();
```

For more information, see [ASP.NET Core fundamentals overview](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0)

The following table shows the environment variable and command-line argument used to change the content root, app name, and environment:

| feature | Environment variable | Command-line argument |
| --- | --- | --- |
| Application name | ASPNETCORE_APPLICATIONNAME | --applicationName |
| Environment name | ASPNETCORE_ENVIRONMENT | --environment |
| Content root | ASPNETCORE_CONTENTROOT | --contentRoot |

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureAppConfiguration(config =>
        {
            config.AddIniFile("appsettings.ini");
        })
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

```
var builder = WebApplication.CreateBuilder(args);

builder.Configuration.AddIniFile("appsettings.ini");

var app = builder.Build();
```

For detailed information, see [File configuration providers](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-6.0#file-configuration-provider) in [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-6.0).

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureLogging(logging =>
        {
            logging.AddJsonConsole();
        })
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

```
var builder = WebApplication.CreateBuilder(args);

// Configure JSON logging to the console.
builder.Logging.AddJsonConsole();

var app = builder.Build();
```

For more information, see [Logging in .NET and ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/?view=aspnetcore-6.0#).

```
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        // Add the memory cache services
        services.AddMemoryCache();

        // Add a custom scoped service
        services.AddScoped<ITodoRepository, TodoRepository>();
    }
}
```

```
var builder = WebApplication.CreateBuilder(args);

// Add the memory cache services.
builder.Services.AddMemoryCache();

// Add a custom scoped service.
builder.Services.AddScoped<ITodoRepository, TodoRepository>();
var app = builder.Build();
```

For more information, see [Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-6.0#).

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureHostOptions(o => o.ShutdownTimeout = TimeSpan.FromSeconds(30));
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

```
var builder = WebApplication.CreateBuilder(args);

// Wait 30 seconds for graceful shutdown.
builder.Host.ConfigureHostOptions(o => o.ShutdownTimeout = TimeSpan.FromSeconds(30));

var app = builder.Build();
```

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            // Change the HTTP server implementation to be HTTP.sys based.
            webBuilder.UseHttpSys()
                      .UseStartup<Startup>();
        });
```

```
var builder = WebApplication.CreateBuilder(args);

// Change the HTTP server implementation to be HTTP.sys based.
// Windows only.
builder.WebHost.UseHttpSys();

var app = builder.Build();
```

By default, the web root is relative to the content root in the `wwwroot` folder. Web root is where the Static File Middleware looks for static files. Web root can be changed by setting the [WebRootPath](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationoptions.webrootpath#microsoft-aspnetcore-builder-webapplicationoptions-webrootpath) property on [WebApplicationOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationoptions):

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            // Look for static files in webroot.
            webBuilder.UseWebRoot("webroot")
                      .UseStartup<Startup>();
        });
```

```
var builder = WebApplication.CreateBuilder(new WebApplicationOptions
{
    Args = args,
    // Look for static files in webroot
    WebRootPath = "webroot"
});

var app = builder.Build();
```

The following .NET 5 and .NET 6 samples use [Autofac](https://docs.autofac.org/en/latest/integration/aspnetcore.html)

**Program class**

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .UseServiceProviderFactory(new AutofacServiceProviderFactory())
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

**Startup**

```
public class Startup
{
    public void ConfigureContainer(ContainerBuilder containerBuilder)
    {
    }
}
```

```
var builder = WebApplication.CreateBuilder(args);

builder.Host.UseServiceProviderFactory(new AutofacServiceProviderFactory());

// Register services directly with Autofac here. Don't
// call builder.Populate(), that happens in AutofacServiceProviderFactory.
builder.Host.ConfigureContainer<ContainerBuilder>(builder => builder.RegisterModule(new MyApplicationModule()));

var app = builder.Build();
```

`Startup.Configure` can inject any service added via the [IServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection).

```
public class Startup
{
    // This method gets called by the runtime. Use this method to add services
    // to the container.
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddSingleton<IService, Service>();
    }

    // Anything added to the service collection can be injected into Configure.
    public void Configure(IApplicationBuilder app,
                          IWebHostEnvironment env,
                          IHostApplicationLifetime lifetime,
                          IService service,
                          ILogger<Startup> logger)
    {
        lifetime.ApplicationStarted.Register(() =>
            logger.LogInformation(
                "The application {Name} started in the injected {Service}",
                env.ApplicationName, service));
    }
}
```

In ASP.NET Core in .NET 6:

*   There are a few common services available as top level properties on [WebApplication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication).
*   Additional services need to be manually resolved from the `IServiceProvider` via [WebApplication.Services](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.services#microsoft-aspnetcore-builder-webapplication-services).

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<IService, Service>();

var app = builder.Build();

IService service = app.Services.GetRequiredService<IService>();
ILogger logger = app.Logger;
IHostApplicationLifetime lifetime = app.Lifetime;
IWebHostEnvironment env = app.Environment;

lifetime.ApplicationStarted.Register(() =>
    logger.LogInformation(
        $"The application {env.ApplicationName} started" +
        $" with injected {service}"));
```

In the following samples, the test project uses `TestServer` and [WebApplicationFactory<TEntryPoint>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.testing.webapplicationfactory-1). These ship as separate packages that require explicit reference:

```
<ItemGroup>
  <PackageReference Include="Microsoft.AspNetCore.Mvc.Testing" Version="{Version}" />
</ItemGroup>
```

```
<ItemGroup>
  <PackageReference Include="Microsoft.AspNetCore.TestHost" Version="{Version}" />
</ItemGroup>
```

```
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddSingleton<IHelloService, HelloService>();
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env, IHelloService helloService)
    {
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }

        app.UseRouting();

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapGet("/", async context =>
            {
                await context.Response.WriteAsync(helloService.HelloMessage);
            });
        });
    }
}
```

```
[Fact]
public async Task HelloWorld()
{
    using var host = Host.CreateDefaultBuilder()
        .ConfigureWebHostDefaults(builder =>
        {
            // Use the test server and point to the application's startup
            builder.UseTestServer()
                    .UseStartup<WebApplication1.Startup>();
        })
        .ConfigureServices(services =>
        {
            // Replace the service
            services.AddSingleton<IHelloService, MockHelloService>();
        })
        .Build();

    await host.StartAsync();

    var client = host.GetTestClient();

    var response = await client.GetStringAsync("/");

    Assert.Equal("Test Hello", response);
}

class MockHelloService : IHelloService
{
    public string HelloMessage => "Test Hello";
}
```

```
[Fact]
public async Task HelloWorld()
{
    var application = new WebApplicationFactory<Program>()
        .WithWebHostBuilder(builder =>
        {
            builder.ConfigureServices(services =>
            {
                services.AddSingleton<IHelloService, MockHelloService>();
            });
        });

    var client = application.CreateClient();

    var response = await client.GetStringAsync("/");

    Assert.Equal("Test Hello", response);
}

class MockHelloService : IHelloService
{
    public string HelloMessage => "Test Hello";
}
```

```
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<IHelloService, HelloService>();

var app = builder.Build();

var helloService = app.Services.GetRequiredService<IHelloService>();

app.MapGet("/", async context =>
{
    await context.Response.WriteAsync(helloService.HelloMessage);
});

app.Run();
```

The project file can contain one of the following:

```
<ItemGroup>
    <InternalsVisibleTo Include="MyTestProject" />
</ItemGroup>
```

Or

```
[assembly: InternalsVisibleTo("MyTestProject")]
```

An alternative solution is to make the `Program` class public. `Program` can be made public with [Top-level statements](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements) by defining a `public partial Program` class in the project or in `Program.cs`:

```
var builder = WebApplication.CreateBuilder(args);

// ... Configure services, routes, etc.

app.Run();

public partial class Program { }
```

```
[Fact]
public async Task HelloWorld()
{
    var application = new WebApplicationFactory<Program>()
        .WithWebHostBuilder(builder =>
        {
            builder.ConfigureServices(services =>
            {
                services.AddSingleton<IHelloService, MockHelloService>();
            });
        });

    var client = application.CreateClient();

    var response = await client.GetStringAsync("/");

    Assert.Equal("Test Hello", response);
}

class MockHelloService : IHelloService
{
    public string HelloMessage => "Test Hello";
}
```

The .NET 5 version and .NET 6 version with the `WebApplicationFactory` are identical by design.
