# Source: https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html

Title: Getting Started — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html

Markdown Content:
Ocelot is designed to work with [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-9.0) and is currently on [.NET 8](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle)[LTS](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#release-types) and [.NET 9](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#lifecycle)[STS](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core#release-types) frameworks.

Install[¶](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#install "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Install Ocelot and it’s dependencies using [NuGet](https://www.nuget.org/). You will need to create a [ASP.NET Core minimal API project](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api) with “ASP.NET Core Empty” template but without `app.Map*` methods, and bring the package into it. Then follow the startup below and [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) sections to get up and running.

Install-Package Ocelot

All versions can be found in the [NuGet Gallery | Ocelot](https://www.nuget.org/packages/Ocelot/).

Configuration[¶](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

The following is a very basic [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json). It won’t do anything but should get Ocelot starting.

{
 "Aggregates": [], // optional
 "Routes": [], // required section
 "DynamicRoutes": [], // optional section
 "GlobalConfiguration": { // required
 "BaseUrl": "https://api.mybusiness.com"
 }
}

If you want some example that actually does something use the following:

{
 "Routes": [
 {
 "UpstreamHttpMethod": [ "Get" ],
 "UpstreamPathTemplate": "/ocelot/posts/{id}",
 "DownstreamPathTemplate": "/todos/{id}",
 "DownstreamScheme": "https",
 "DownstreamHostAndPorts": [
 { "Host": "jsonplaceholder.typicode.com", "Port": 443 }
 ]
 }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://api.mybusiness.com"
 }
}

The most important thing to note here is `BaseUrl` property. Ocelot needs to know the URL it is running under in order to do Header [Find and Replace 2](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#ht-find-and-replace) and for certain [Administration](https://ocelot.readthedocs.io/en/latest/features/administration.html) configurations. When setting this URL it should be the external URL that clients will see Ocelot running on e.g. If you are running containers Ocelot might run on the URL `http://123.12.1.2:6543` but has something like [nginx](https://nginx.org/) in front of it responding on `https://api.mybusiness.com`. In this case the Ocelot `BaseUrl` should be `https://api.mybusiness.com`.

If you are using containers and require Ocelot to respond to clients on `http://123.12.1.2:6543` then you can do this, however if you are deploying multiple Ocelot’s you will probably want to pass this on the command line in some kind of script. Hopefully whatever scheduler you are using can pass the IP.

Program[¶](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#program "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Then in your [Program.cs](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs) (with [top-level statements](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements)) you will want to have the following.

 using Ocelot.DependencyInjection;
 using Ocelot.Middleware;

 var builder = WebApplication.CreateBuilder(args);

 // Ocelot Basic setup
 builder.Configuration
 .SetBasePath(builder.Environment.ContentRootPath)
 .AddOcelot(); // single ocelot.json file in read-only mode builder.Services
 .AddOcelot(builder.Configuration);
 // Add your features
 if (builder.Environment.IsDevelopment())
 {
 builder.Logging.AddConsole();
 }

 // Add middlewares aka app.Use*()
 var app = builder.Build();
 await app.UseOcelot(); await app.RunAsync();

The main things to note are

*   `builder.Configuration.AddOcelot()` adds single [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) configuration file in read-only mode.

*   `builder.Services.AddOcelot(builder.Configuration)` adds Ocelot required and default services [[1]](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#f1)

*   `app.UseOcelot()` sets up all the Ocelot middlewares. Note, we have to await the threading result before calling `app.RunAsync()`

*   Do not add endpoint mappings (minimal API methods) such as `app.MapGet()` because the Ocelot pipeline is not compatible with them!

Samples[¶](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#samples "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

For beginners, we have prepared basic [samples](https://github.com/ThreeMammals/Ocelot/tree/main/samples) to help Ocelot newbies clone, compile, and get it running.

*   [Basic](https://github.com/ThreeMammals/Ocelot/tree/main/samples/Basic) sample: It has a single configuration file, [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json).

*   [Basic Configuration](https://github.com/ThreeMammals/Ocelot/tree/main/samples/Configuration) sample: It has multiple configuration files (`ocelot.*.json`) to be merged into `ocelot.json` and written back to disk.

After running in Visual Studio [[2]](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#f2), you may use `API.http` files to send testing requests to the `localhost` Ocelot application instance.

* * *
