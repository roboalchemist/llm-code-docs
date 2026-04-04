# Source: https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0

Title: Migrate from ASP.NET Core in .NET 5 to .NET 6

URL Source: https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0

Markdown Content:
This article explains how to update an existing ASP.NET Core in .NET 5 project to .NET 6. For instructions on how to migrate from ASP.NET Core 3.1 to .NET 6, see [Migrate from ASP.NET Core 3.1 to .NET 6](https://learn.microsoft.com/en-us/aspnet/core/migration/31-to-60?view=aspnetcore-10.0).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.
*   [.NET 6 SDK](https://dotnet.microsoft.com/download/dotnet/6.0)

If you rely upon a [`global.json`](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json) file to target a specific .NET SDK version, update the `version` property to the .NET 6 SDK version that's installed. For example:

```
{
  "sdk": {
-    "version": "5.0.100"
+    "version": "6.0.100"
  }
}
```

Update the project file's [Target Framework Moniker (TFM)](https://learn.microsoft.com/en-us/dotnet/standard/frameworks) to `net6.0`:

```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
-    <TargetFramework>net5.0</TargetFramework>
+    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>

</Project>
```

In the project file, update each [`Microsoft.AspNetCore.*`](https://www.nuget.org/packages?q=Microsoft.AspNetCore.*) and [`Microsoft.Extensions.*`](https://www.nuget.org/packages?q=Microsoft.Extensions.*) package reference's `Version` attribute to 6.0.0 or later. For example:

```
<ItemGroup>
-    <PackageReference Include="Microsoft.AspNetCore.JsonPatch" Version="5.0.3" />
-    <PackageReference Include="Microsoft.Extensions.Caching.Abstractions" Version="5.0.0" />
+    <PackageReference Include="Microsoft.AspNetCore.JsonPatch" Version="6.0.0" />
+    <PackageReference Include="Microsoft.Extensions.Caching.Abstractions" Version="6.0.0" />
</ItemGroup>
```

The new .NET 6 minimal hosting model for ASP.NET Core apps requires only one file and a few lines of code. **Apps migrating to .NET 6 don't need to use the new minimal hosting model.** For more information, see [Apps migrating to .NET 6 don't need to use the new minimal hosting model](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#am6) in the following section.

The following code from the ASP.NET Core empty template creates an app using the new minimal hosting model:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
```

The minimal hosting model:

*   Significantly reduces the number of files and lines of code required to create an app. Only one file is needed with four lines of code.
*   Unifies `Startup.cs` and `Program.cs` into a single `Program.cs` file.
*   Uses [top-level statements](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements) to minimize the code required for an app.
*   Uses [global `using` directives](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-10#global-using-directives) to eliminate or minimize the number of [`using` statement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-statement) lines required.

The following code displays the `Startup.cs` and `Program.cs` files from an .NET 5 Web App template (Razor Pages) with unused `using` statements removed:

```
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
// Unused usings removed.

namespace WebAppRPv5
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddRazorPages();
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapRazorPages();
            });
        }
    }
}
```

```
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;
// Unused usings removed.

namespace WebAppRPv5
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                });
    }
}
```

In ASP.NET Core in .NET 6, the preceding code is replaced by the following:

```
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

The preceding ASP.NET Core in .NET 6 sample shows how:

*   [ConfigureServices](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.startupbase.configureservices) is replaced with [`WebApplication.Services`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.services#microsoft-aspnetcore-builder-webapplication-services).
*   `builder.Build()` returns a configured [WebApplication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication) to the variable `app`. [Configure](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.startupbase.configure) is replaced with configuration calls to same services using `app`.

Detailed examples of migrating ASP.NET Core in .NET 5 `Startup` code to .NET 6 using the minimal hosting model are provided later in this document.

There are a few changes to the other files generated for the Web App template:

*   `Index.cshtml` and `Privacy.cshtml` have the unused `using` statements removed.
*   `RequestId` in `Error.cshtml` is declared as a [nullable reference type (NRT)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-reference-types):

```
- public string RequestId { get; set; }
+ public string? RequestId { get; set; }
```

*   Log level defaults have changed in `appsettings.json` and `appsettings.Development.json`:

```
- "Microsoft": "Warning",
- "Microsoft.Hosting.Lifetime": "Information"
+ "Microsoft.AspNetCore": "Warning"
```

In the preceding ASP.NET Core template code, `"Microsoft": "Warning"` has been changed to `"Microsoft.AspNetCore": "Warning"`. This change results in logging all informational messages from the `Microsoft` namespace _**except**_`Microsoft.AspNetCore`. For example, `Microsoft.EntityFrameworkCore` is now logged at the informational level.

For more details on the new hosting model, see the [Frequently asked questions](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#faq) section. For more information on the adoption of NRTs and .NET compiler null-state analysis, see the [Nullable reference types (NRTs) and .NET compiler null-state static analysis](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#nullable-reference-types-nrts-and-net-compiler-null-state-static-analysis) section.

Using [`Startup`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-5.0) and the [Generic Host](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0) used by the ASP.NET Core 3.1 and 5.0 templates is fully supported.

ASP.NET Core 3.1 and 5.0 apps can use their `Startup` code with the new minimal hosting model. Using `Startup` with the minimal hosting model has the following advantages:

*   No hidden reflection is used to call the `Startup` class.
*   Asynchronous code can be written because the developer controls the call to `Startup`.
*   Code can be written that interleaves `ConfigureServices` and `Configure`.

One minor limitation in using `Startup` code with the new minimal hosting model is that to inject a dependency into `Configure`, the service in `Program.cs` must be manually resolved.

Consider the following code generated by the ASP.NET Core 3.1 or 5.0 Razor Pages template:

```
public class Program
{
    public static void Main(string[] args)
    {
        CreateHostBuilder(args).Build().Run();
    }

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
            });
}
```

```
public class Startup
{
    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddRazorPages();
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }
        else
        {
            app.UseExceptionHandler("/Error");
            app.UseHsts();
        }

        app.UseHttpsRedirection();
        app.UseStaticFiles();
        app.UseRouting();

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapRazorPages();
        });
    }
}
```

The preceding code migrated to the new minimal hosting model:

```
using Microsoft.AspNetCore.Builder;

var builder = WebApplication.CreateBuilder(args);

var startup = new Startup(builder.Configuration);

startup.ConfigureServices(builder.Services);

var app = builder.Build();

startup.Configure(app, app.Environment);

app.Run();
```

```
public class Startup
{
    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddRazorPages();
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (!env.IsDevelopment())
        {
            app.UseExceptionHandler("/Error");
            app.UseHsts();
        }

        app.UseHttpsRedirection();
        app.UseStaticFiles();
        app.UseRouting();

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapRazorPages();
        });
    }
}
```

In the preceding code, the `if (env.IsDevelopment())` block is removed because in [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0), the developer exception page middleware is enabled by default. For more information, see [Differences between the ASP.NET Core in .NET 5 and .NET 6 hosting models](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#diff) in the next section.

When using a custom dependency injection (DI) container, add the following highlighted code:

```
using Autofac;
using Autofac.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

var startup = new Startup(builder.Configuration);

startup.ConfigureServices(builder.Services);

// Using a custom DI container.
builder.Host.UseServiceProviderFactory(new AutofacServiceProviderFactory());
builder.Host.ConfigureContainer<ContainerBuilder>(startup.ConfigureContainer);

var app = builder.Build();

startup.Configure(app, app.Environment);

app.Run();
```

```
using Autofac;
public class Startup
{
    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddRazorPages();
    }

    //  Using a custom DI container
    public void ConfigureContainer(ContainerBuilder builder)
    {
        // Configure custom container.
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (!env.IsDevelopment())
        {
            app.UseExceptionHandler("/Error");
            app.UseHsts();
        }

        app.UseHttpsRedirection();
        app.UseStaticFiles();
        app.UseRouting();

        app.UseEndpoints(endpoints =>
        {
            endpoints.MapRazorPages();
        });
    }
}
```

When using the minimal hosting model, the endpoint routing middleware wraps the entire middleware pipeline, therefore there's no need to have explicit calls to `UseRouting` or `UseEndpoints` to register routes. `UseRouting` can still be used to specify where route matching happens, but `UseRouting` doesn't need to be explicitly called if routes should be matched at the beginning of the middleware pipeline.

In the following code, the calls to `UseRouting` and `UseEndpoints` are removed from `Startup`. `MapRazorPages` is called in `Program.cs`:

```
public class Startup
{
    public Startup(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public IConfiguration Configuration { get; }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddRazorPages();
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        if (!env.IsDevelopment())
        {
            app.UseExceptionHandler("/Error");
            app.UseHsts();
        }

        app.UseHttpsRedirection();
        app.UseStaticFiles();
        //app.UseRouting();

        //app.UseEndpoints(endpoints =>
        //{
        //    endpoints.MapRazorPages();
        //});
    }
}
```

```
using Microsoft.AspNetCore.Builder;

var builder = WebApplication.CreateBuilder(args);

var startup = new Startup(builder.Configuration);

startup.ConfigureServices(builder.Services);

var app = builder.Build();

startup.Configure(app, app.Environment);

app.MapRazorPages();

app.Run();
```

When using `Startup` with the new minimal hosting model, keep in mind the following difference:

*   `Program.cs` controls the instantiation and lifetime of the `Startup` class.
*   Any additional services injected into the `Configure` method need to be manually resolved by the `Program` class.

*   In [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0), the developer exception page middleware is enabled by default.
*   The app name defaults to the entry point assembly's name: `Assembly.GetEntryAssembly().GetName().FullName`. When using the [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) in a library, explicitly change the app name to the library's assembly to allow MVC's [application part discovery](https://learn.microsoft.com/en-us/aspnet/core/mvc/advanced/app-parts?view=aspnetcore-10.0) to work. See [Change the content root, app name, and environment](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0#ccr) in this document for detailed instructions.
*   The endpoint routing middleware wraps the entire middleware pipeline, therefore there's no need to have explicit calls to `UseRouting` or `UseEndpoints` to register routes. `UseRouting` can still be used to specify where route matching happens, but `UseRouting` doesn't need to be explicitly called if routes should be matched at the beginning of the middleware pipeline.
*   The [pipeline](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0) is created before any [IStartupFilter](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.istartupfilter) runs, therefore exceptions caused while building the pipeline aren't visible to the `IStartupFilter` call chain.
*   Some tools, such as EF migrations, use [`Program.CreateHostBuilder`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0) to access the app's `IServiceProvider` to execute custom logic in the context of the app. These tools have been updated to use a new technique to execute custom logic in the context of the app. [Entity Framework Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/) is an example of a tool that uses `Program.CreateHostBuilder` in this way. We're working to make sure tools are updated to use the new model.
*   Unlike the `Startup` class, the minimal host doesn't automatically configure a DI scope when instantiating the service provider. For contexts where a scope is required, it is necessary to invoke [IServiceScope](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicescope) with [IServiceScopeFactory.CreateScope](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicescopefactory.createscope) to instantiate a new scope. For more information, see [how to resolve a service at app startup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0#resolve-a-service-at-app-start-up).
*   It's _**not**_ possible to [change any host settings such as app name, environment, or the content root](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0#ccr) after the creation of the [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder). For detailed instructions on changing host settings, see [Customize `IHostBuilder` or `IWebHostBuilder`](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0#cii). The following highlighted APIs throw an exception:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

// WebHost

try
{
    builder.WebHost.UseContentRoot(Directory.GetCurrentDirectory());
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

try
{
    builder.WebHost.UseEnvironment(Environments.Staging);
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

try
{
    builder.WebHost.UseSetting(WebHostDefaults.ApplicationKey, "ApplicationName2");
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

try
{
    builder.WebHost.UseSetting(WebHostDefaults.ContentRootKey, Directory.GetCurrentDirectory());
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

try
{
    builder.WebHost.UseSetting(WebHostDefaults.EnvironmentKey, Environments.Staging);
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

// Host
try
{
    builder.Host.UseEnvironment(Environments.Staging);
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

try
{
    // TODO: This does not throw
    builder.Host.UseContentRoot(Directory.GetCurrentDirectory());
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

*   The `Startup` class can't be used from [`WebApplicationBuilder.Host`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder.host#microsoft-aspnetcore-builder-webapplicationbuilder-host) or [`WebApplicationBuilder.WebHost`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder.webhost#microsoft-aspnetcore-builder-webapplicationbuilder-webhost). The following highlighted code throws an exception:

```
var builder = WebApplication.CreateBuilder(args);

try
{
    builder.Host.ConfigureWebHostDefaults(webHostBuilder =>
    {
        webHostBuilder.UseStartup<Startup>();
    });
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
    throw;    
}

builder.Services.AddRazorPages();

var app = builder.Build();
```

```
var builder = WebApplication.CreateBuilder(args);

try
{
    builder.WebHost.UseStartup<Startup>();
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
    throw;    
}

builder.Services.AddRazorPages();

var app = builder.Build();
```
*   The [IHostBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostbuilder) implementation on [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) (`WebApplicationBuilder.Host`), doesn't defer execution of the [ConfigureServices](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.istartup.configureservices), [ConfigureAppConfiguration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostbuilder.configureappconfiguration), or [ConfigureHostConfiguration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostbuilder.configurehostconfiguration) methods. Not deferring execution allows code using [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) to observe changes made to the `IServiceCollection` and `IConfiguration`. The following example only adds `Service1` as an `IService`:

```
using Microsoft.Extensions.DependencyInjection.Extensions;

var builder = WebApplication.CreateBuilder(args);

builder.Host.ConfigureServices(services =>
{
    services.TryAddSingleton<IService, Service1>();
});

builder.Services.TryAddSingleton<IService, Service2>();

var app = builder.Build();

// Displays Service1 only.
Console.WriteLine(app.Services.GetRequiredService<IService>());

app.Run();

class Service1 : IService
{
}

class Service2 : IService
{
}

interface IService
{
}
```

In the preceding code, the `builder.Host.ConfigureServices` callback gets called inline rather than being deferred until `builder.Build` is called. This means that `Service1` gets added to the `IServiceCollection` before `Service2` and results in `Service1` being resolved for `IService`.

The existing .NET ecosystem built extensibility around [IServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection), [IHostBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostbuilder), and [IWebHostBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.iwebhostbuilder). These properties are available on [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) as `Services`, `Host`, and `WebHost`.

`WebApplication` implements both [Microsoft.AspNetCore.Builder.IApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.iapplicationbuilder) and [Microsoft.AspNetCore.Routing.IEndpointRouteBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.routing.iendpointroutebuilder).

We expect library authors to continue targeting `IHostBuilder`, `IWebHostBuilder`, `IApplicationBuilder`, and `IEndpointRouteBuilder` when building ASP.NET Core specific components. This ensures that your middleware, route handler, or other extensibility points continue to work across different hosting models.

*   **Is the new minimal hosting model less capable?**

No. The new hosting model is functionally equivalent for 98% of scenarios supported by `IHostBuilder` and the `IWebHostBuilder`. There are some advanced scenarios that require specific workarounds on `IHostBuilder`, but we expect those to be extremely rare.

*   **Is the generic hosting model deprecated?**

No. The generic hosting model is an alternative model that is supported indefinitely. The generic host underpins the new hosting model and is still the primary way to host worker-based applications.

*   **Do I have to migrate to the new hosting model?**

No. The new hosting model is the preferred way to host new apps using .NET 6 or later, but you aren't forced to change the project layout in existing apps. This means apps can upgrade from .NET 5 to .NET 6 by changing the target framework in the project file from `net5.0` to `net6.0`. For more information, see the [Update the target framework](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60?view=aspnetcore-10.0#tf) section in this article. However, we recommend apps migrate to the new hosting model to take advantage of new features only available to the new hosting model.

*   **Do I have to use top-level statements?**

No. The new project templates all use [top-level statements](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements), but the new hosting APIs can be used in any .NET 6 app to host a webserver or web app.

*   **Where do I put state that was stored as fields in my `Program` or `Startup` class?**

We strongly recommend using [dependency injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0) (DI) to flow state in ASP.NET Core apps.

There are two approaches to storing state outside of DI:

    *   Store the state in another class. Storing in a class assumes a static state that can be accessed from anywhere in the app.

    *   Use the `Program` class generated by top level statements to store state. Using `Program` to store state is the semantic approach:

```
var builder = WebApplication.CreateBuilder(args);

ConfigurationValue = builder.Configuration["SomeKey"] ?? "Hello";

var app = builder.Build();

app.MapGet("/", () => ConfigurationValue);

app.Run();

partial class Program
{
    public static string? ConfigurationValue { get; private set; }
}
```

*   **What if I was using a custom dependency injection container?**

Custom DI containers are supported. For an example, see [Custom dependency injection (DI) container](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0#cdi).

*   **Do `WebApplicationFactory` and `TestServer` still work?**

Yes. `WebApplicationFactory<TEntryPoint>` is the way to test the new hosting model. For an example, see [Test with `WebApplicationFactory` or `TestServer`](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0#twa).

After following the guidance earlier in this article to update an app to .NET 6, adopt specific features by following the links in [What's new in ASP.NET Core in .NET 6](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-6.0?view=aspnetcore-10.0#blazor).

To adopt all of the [new 6.0 features for Blazor apps](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-6.0?view=aspnetcore-10.0#blazor), we recommend the following process:

*   Create a new 6.0 Blazor project from one of the Blazor project templates. For more information, see [Tooling for ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/tooling?view=aspnetcore-10.0).
*   Move the app's components and code to the 6.0 app making modifications to adopt the new .NET 6 features.

See [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/44600)

See **Migrating React applications from Spa Extensions** in [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/44600)

For apps using Docker, update your _Dockerfile_`FROM` statements and scripts. Use a base image that includes the ASP.NET Core in .NET 6 runtime. Consider the following `docker pull` command difference between ASP.NET Core in .NET 5 and .NET 6:

```
- docker pull mcr.microsoft.com/dotnet/aspnet:5.0
+ docker pull mcr.microsoft.com/dotnet/aspnet:6.0
```

See GitHub issue [Breaking Change: Default console logger format set to JSON](https://github.com/dotnet/dotnet-docker/issues/3274).

The Razor compiler now leverages the new [source generators feature](https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/) to generate compiled C# files from the Razor views and pages in a project. In previous versions:

*   The compilation relied on the `RazorGenerate` and `RazorCompile` targets to produce the generated code. These targets are no longer valid. In .NET 6, both code generation and compilation are supported by a single call to the compiler. `RazorComponentGenerateDependsOn` is still supported to specify dependencies that are required before the build runs.
*   A separate Razor assembly, `AppName.Views.dll`, was generated that contained the compiled view types in an application. This behavior has been deprecated and a single assembly `AppName.dll` is produced that contains both the app types and the generated views.
*   The app types in `AppName.Views.dll` were public. In .NET 6, the app types are in `AppName.dll` but are `internal sealed`. Apps doing type discover on `AppName.Views.dll` won't be able to do type discover on `AppName.dll`. The following shows the API change:

```
- public class Views_Home_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<dynamic>
+ internal sealed class Views_Home_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<dynamic>
```

Make the following changes:

*   The following properties are no longer applicable with the single-step compilation model. 
    *   `RazorTargetAssemblyAttribute`
    *   `RazorTargetName`
    *   `EnableDefaultRazorTargetAssemblyInfoAttributes`
    *   `UseRazorBuildServer`
    *   `GenerateRazorTargetAssemblyInfo`
    *   `GenerateMvcApplicationPartsAssemblyAttributes`

For more information, see [Razor compiler no longer produces a Views assembly](https://github.com/aspnet/Announcements/issues/459).

Project templates now use [Duende Identity Server](https://docs.duendesoftware.com/).

Add a `DbSet<Key>` property named `Keys` to every `IdentityDbContext` to satisfy a new requirement from the updated version of `IPersistedGrantDbContext`. The keys are required as part of the contract with Duende Identity Server's stores.

```
public DbSet<Key> Keys { get; set; }
```

Note

Existing migrations must be recreated for Duende Identity Server.

[Code samples migrated to the new minimal hosting model in 6.0](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0)

Use the articles in [Breaking changes in .NET](https://learn.microsoft.com/en-us/dotnet/core/compatibility/breaking-changes) to find breaking changes that might apply when upgrading an app to a newer version of .NET.

For more information, see [Announcements GitHub repository (`aspnet/Announcements`, `6.0.0` label)](https://github.com/aspnet/Announcements/issues?q=is%3Aissue+label%3A6.0.0+is%3Aopen): Includes breaking and non-breaking information.

ASP.NET Core project templates use nullable reference types (NRTs), and the .NET compiler performs null-state static analysis. These features were released with C# 8 and are enabled by default for apps generated using ASP.NET Core in .NET 6 (C# 10) or later.

The .NET compiler's null-state static analysis warnings can either serve as a guide for updating a documentation example or sample app locally or be ignored. Null-state static analysis can be disabled by [setting `Nullable` to `disable`](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-reference-types#setting-the-nullable-context) in the app's project file, which we only recommend for documentation examples and sample apps if the compiler warnings are distracting while learning about .NET. **_We don't recommend disabling null-state checking in production projects._**

For more information on NRTs, the MSBuild `Nullable` property, and updating apps (including `#pragma` guidance), see the following resources in the C# documentation:

*   [Nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references)
*   [Nullable reference types (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-reference-types)
*   [Learn techniques to resolve nullable warnings](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-warnings)
*   [Update a codebase with nullable reference types to improve null diagnostic warnings](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-migration-strategies)
*   [Attributes for null-state static analysis](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/attributes/nullable-analysis)
*   [! (null-forgiving) operator (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-forgiving)

If the [ASP.NET Core Module (ANCM)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0) wasn't a selected component when Visual Studio was installed or if a prior version of the ANCM was installed on the system, download the latest [.NET Core Hosting Bundle Installer (direct download)](https://dotnet.microsoft.com/permalink/dotnetcore-current-windows-runtime-bundle-installer) and run the installer. For more information, see [Hosting Bundle](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/hosting-bundle?view=aspnetcore-10.0).

In .NET 6, [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) normalizes the content root path to end with a [DirectorySeparatorChar](https://learn.microsoft.com/en-us/dotnet/api/system.io.path.directoryseparatorchar#system-io-path-directoryseparatorchar). Most apps migrating from [HostBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostbuilder) or [WebHostBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.webhostbuilder) won't have the same app name because they aren't normalized. For more information, see [SetApplicationName](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/configuration/overview?view=aspnetcore-10.0#set-the-application-name-setapplicationname)

*   [Code samples migrated to the new minimal hosting model in 6.0](https://learn.microsoft.com/en-us/aspnet/core/migration/50-to-60-samples?view=aspnetcore-10.0)
