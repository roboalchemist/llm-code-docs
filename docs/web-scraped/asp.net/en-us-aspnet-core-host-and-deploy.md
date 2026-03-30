# Source: https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/?view=aspnetcore-10.0

Title: Host and deploy ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/?view=aspnetcore-10.0

Published Time: Thu, 22 Jan 2026 23:58:07 GMT

Markdown Content:
In general, to deploy an ASP.NET Core app to a hosting environment:

*   Deploy the published app to a folder on the hosting server.
*   Set up a process manager that starts the app when requests arrive and restarts the app after it crashes or the server reboots.
*   For configuration of a reverse proxy, set up a reverse proxy to forward requests to the app.

For Blazor host and deploy guidance, which adds to or supersedes the guidance in this node, see [Host and deploy ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/?view=aspnetcore-10.0).

The [dotnet publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command compiles app code and copies the files required to run the app into a _publish_ folder. When deploying from Visual Studio, the `dotnet publish` step occurs automatically before the files are copied to the deployment destination.

To run the published app locally, run `dotnet <ApplicationName>.dll` from the _publish_ folder.

`*.json` files are published by default. To publish other settings files, specify them in an [`<ItemGroup><Content Include= ... />`](https://learn.microsoft.com/en-us/visualstudio/msbuild/common-msbuild-project-items#content) element in the project file. The following example publishes XML files:

```
<ItemGroup>
  <Content Include="**\*.xml" Exclude="bin\**\*;obj\**\*"
    CopyToOutputDirectory="PreserveNewest" />
</ItemGroup>
```

The _publish_ folder contains one or more app assembly files, dependencies, and optionally the .NET runtime.

A .NET Core app can be published as _self-contained deployment_ or _framework-dependent deployment_. If the app is self-contained, the assembly files that contain the .NET runtime are included in the _publish_ folder. If the app is framework-dependent, the .NET runtime files aren't included because the app has a reference to a version of .NET that's installed on the server. The default deployment model is framework-dependent. For more information, see [.NET Core application deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/).

In addition to _.exe_ and _.dll_ files, the _publish_ folder for an ASP.NET Core app typically contains configuration files, static assets, and MVC views. For more information, see [ASP.NET Core directory structure](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/directory-structure?view=aspnetcore-10.0).

An ASP.NET Core app is a console app that must be started when a server boots and restarted if it crashes. To automate starts and restarts, a process manager is required. The most common process managers for ASP.NET Core are:

*   Linux 
    *   [Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0)

*   Windows 
    *   [IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0)
    *   [Windows Service](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/windows-service?view=aspnetcore-10.0)

If the app uses the [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server, [Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0), or [IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0) can be used as a reverse proxy server. A reverse proxy server receives HTTP requests from the Internet and forwards them to Kestrel.

Either configuration—with or without a reverse proxy server—is a supported hosting configuration. For more information, see [When to use Kestrel with a reverse proxy](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/when-to-use-a-reverse-proxy?view=aspnetcore-10.0).

Either configuration—with or without a reverse proxy server—is a supported hosting configuration. For more information, see [When to use Kestrel with a reverse proxy](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#when-to-use-kestrel-with-a-reverse-proxy).

Additional configuration might be required for apps hosted behind proxy servers and load balancers. Without additional configuration, an app might not have access to the scheme (HTTP/HTTPS) and the remote IP address where a request originated. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

Deployment often requires additional tasks besides copying the output from [dotnet publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) to a server. For example, extra files might be required or excluded from the _publish_ folder. Visual Studio uses [MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild) for web deployment, and MSBuild can be customized to do many other tasks during deployment. For more information, see [Visual Studio publish profiles (.pubxml) for ASP.NET Core app deployment](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-10.0) and the [Using MSBuild and Team Foundation Build](https://www.microsoftpressstore.com/store/inside-the-microsoft-build-engine-using-msbuild-and-9780735645240) book.

By using [the Publish Web feature](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-azure-webapp-using-vs?view=aspnetcore-10.0) apps can be deployed directly from Visual Studio to the Azure App Service. Azure DevOps Services supports [continuous deployment to Azure App Service](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp). For more information, see [DevOps for ASP.NET Core Developers](https://learn.microsoft.com/en-us/dotnet/architecture/devops-for-aspnet-developers).

See [Publish an ASP.NET Core app to Azure with Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-azure-webapp-using-vs?view=aspnetcore-10.0) for instructions on how to publish an app to Azure using Visual Studio. An additional example is provided by [Create an ASP.NET Core web app in Azure](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-get-started-dotnet).

See [Visual Studio publish profiles (.pubxml) for ASP.NET Core app deployment](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-10.0) for instructions on how to publish an app with a Visual Studio publish profile, including from a Windows command prompt using the [dotnet msbuild](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-msbuild) command.

For deployments to Internet Information Services (IIS) with configuration provided by the _web.config_ file, see the articles under [Host ASP.NET Core on Windows with IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0).

For information on configuration for hosting ASP.NET Core apps in a web farm environment (for example, deployment of multiple instances of your app for scalability), see [Host ASP.NET Core in a web farm](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/web-farm?view=aspnetcore-10.0).

For more information, see [Host ASP.NET Core in Docker containers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/docker/?view=aspnetcore-10.0).

Use Health Check Middleware to perform health checks on an app and its dependencies. For more information, see [Health checks in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-10.0).

*   [.NET application publishing overview](https://learn.microsoft.com/en-us/dotnet/core/deploying)
*   [Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)
*   [ASP.NET Hosting](https://dotnet.microsoft.com/apps/aspnet/hosting)

In general, to deploy an ASP.NET Core app to a hosting environment:

*   Deploy the published app to a folder on the hosting server.
*   Set up a process manager that starts the app when requests arrive and restarts the app after it crashes or the server reboots.
*   For configuration of a reverse proxy, set up a reverse proxy to forward requests to the app.

The [dotnet publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command compiles app code and copies the files required to run the app into a _publish_ folder. When deploying from Visual Studio, the `dotnet publish` step occurs automatically before the files are copied to the deployment destination.

The _publish_ folder contains one or more app assembly files, dependencies, and optionally the .NET runtime.

A .NET Core app can be published as _self-contained deployment_ or _framework-dependent deployment_. If the app is self-contained, the assembly files that contain the .NET runtime are included in the _publish_ folder. If the app is framework-dependent, the .NET runtime files aren't included because the app has a reference to a version of .NET that's installed on the server. The default deployment model is framework-dependent. For more information, see [.NET Core application deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/).

In addition to _.exe_ and _.dll_ files, the _publish_ folder for an ASP.NET Core app typically contains configuration files, static assets, and MVC views. For more information, see [ASP.NET Core directory structure](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/directory-structure?view=aspnetcore-10.0).

An ASP.NET Core app is a console app that must be started when a server boots and restarted if it crashes. To automate starts and restarts, a process manager is required. The most common process managers for ASP.NET Core are:

*   Linux 
    *   [Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0)

*   Windows 
    *   [IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0)
    *   [Windows Service](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/windows-service?view=aspnetcore-10.0)

If the app uses the [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server, [Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0), or [IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0) can be used as a reverse proxy server. A reverse proxy server receives HTTP requests from the Internet and forwards them to Kestrel.

Either configuration—with or without a reverse proxy server—is a supported hosting configuration. For more information, see [When to use Kestrel with a reverse proxy](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#when-to-use-kestrel-with-a-reverse-proxy).

Additional configuration might be required for apps hosted behind proxy servers and load balancers. Without additional configuration, an app might not have access to the scheme (HTTP/HTTPS) and the remote IP address where a request originated. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

Deployment often requires additional tasks besides copying the output from [dotnet publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) to a server. For example, extra files might be required or excluded from the _publish_ folder. Visual Studio uses MSBuild for web deployment, and MSBuild can be customized to do many other tasks during deployment. For more information, see [Visual Studio publish profiles (.pubxml) for ASP.NET Core app deployment](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-10.0) and the [Using MSBuild and Team Foundation Build](https://www.microsoftpressstore.com/store/inside-the-microsoft-build-engine-using-msbuild-and-9780735645240) book.

By using [the Publish Web feature](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-azure-webapp-using-vs?view=aspnetcore-10.0), apps can be deployed directly from Visual Studio to the Azure App Service. Azure DevOps Services supports [continuous deployment to Azure App Service](https://learn.microsoft.com/en-us/azure/devops/pipelines/targets/webapp). For more information, see [DevOps for ASP.NET Core Developers](https://learn.microsoft.com/en-us/dotnet/architecture/devops-for-aspnet-developers).

See [Publish an ASP.NET Core app to Azure with Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-azure-webapp-using-vs?view=aspnetcore-10.0) for instructions on how to publish an app to Azure using Visual Studio. An additional example is provided by [Create an ASP.NET Core web app in Azure](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-get-started-dotnet).

See [Visual Studio publish profiles (.pubxml) for ASP.NET Core app deployment](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-10.0) for instructions on how to publish an app with a Visual Studio publish profile, including from a Windows command prompt using the [dotnet msbuild](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-msbuild) command.

For deployments to Internet Information Services (IIS) with configuration provided by the _web.config_ file, see the articles under [Host ASP.NET Core on Windows with IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0).

For information on configuration for hosting ASP.NET Core apps in a web farm environment (for example, deployment of multiple instances of your app for scalability), see [Host ASP.NET Core in a web farm](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/web-farm?view=aspnetcore-10.0).

For more information, see [Host ASP.NET Core in Docker containers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/docker/?view=aspnetcore-10.0).

*   [.NET application publishing overview](https://learn.microsoft.com/en-us/dotnet/core/deploying)
*   [Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)
*   [ASP.NET Hosting](https://dotnet.microsoft.com/apps/aspnet/hosting)
