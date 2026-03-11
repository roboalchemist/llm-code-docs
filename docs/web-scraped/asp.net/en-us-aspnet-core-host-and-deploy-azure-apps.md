# Source: https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0

Title: Deploy ASP.NET Core apps to Azure App Service

URL Source: https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0

Markdown Content:
[Azure App Service](https://azure.microsoft.com/services/app-service/) is a [Microsoft cloud computing platform service](https://azure.microsoft.com/) for hosting web apps, including ASP.NET Core.

For guidance on creating a reliable, secure, performant, testable, and scalable ASP.NET Core app, see [Enterprise web app patterns](https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/enterprise-app-patterns/overview). A complete production-quality sample web app that implements the patterns is available.

[App Service Documentation](https://learn.microsoft.com/en-us/azure/app-service/) is the home for Azure Apps documentation, tutorials, samples, how-to guides, and other resources. Two notable tutorials that pertain to hosting ASP.NET Core apps are:

[Create an ASP.NET Core web app in Azure](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-get-started-dotnet)

 Use Visual Studio to create and deploy an ASP.NET Core web app to Azure App Service on Windows.

[Create an ASP.NET Core app in App Service on Linux](https://learn.microsoft.com/en-us/azure/app-service/containers/quickstart-dotnetcore)

 Use the command line to create and deploy an ASP.NET Core web app to Azure App Service on Linux.

Subscribe to the [App Service Announcements](https://github.com/Azure/app-service-announcements/) repository and monitor the issues. The App Service team regularly posts announcements and scenarios arriving in App Service.

The following articles are available in ASP.NET Core documentation:

[Publish an ASP.NET Core app to Azure with Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-azure-webapp-using-vs?view=aspnetcore-10.0)

 Learn how to publish an ASP.NET Core app to Azure App Service using Visual Studio.

[Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started-yaml)

 Set up a CI build for an ASP.NET Core app, then create a continuous deployment release to Azure App Service.

[Azure Web App sandbox](https://github.com/projectkudu/kudu/wiki/Azure-Web-App-sandbox)

 Discover Azure App Service runtime execution limitations enforced by the Azure Apps platform.

[Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)

 Understand and troubleshoot warnings and errors with ASP.NET Core projects.

The platform architecture (x86/x64) of an App Services app is set in the app's settings in the Azure portal for apps that are hosted on an A-series compute (Basic) or higher hosting tier. Confirm that the app's publish settings (for example, in the Visual Studio [publish profile (.pubxml)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-10.0)) match the setting in the app's service configuration in the Azure portal.

ASP.NET Core apps can be published [framework-dependent](https://learn.microsoft.com/en-us/dotnet/core/deploying/) because the runtimes for 64-bit (x64) and 32-bit (x86) apps are present on Azure App Service. The [.NET Core SDK](https://learn.microsoft.com/en-us/dotnet/core/sdk) available on App Service is 32-bit, but you can deploy 64-bit apps built locally using the [Kudu](https://github.com/projectkudu/kudu/wiki) console or the publish process in Visual Studio. For more information, see the [Publish and deploy the app](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#publish-and-deploy-the-app) section.

For apps with native dependencies, runtimes for 32-bit (x86) apps are present on Azure App Service. The [.NET Core SDK](https://learn.microsoft.com/en-us/dotnet/core/sdk) available on App Service is 32-bit.

For more information on .NET Core framework components and distribution methods, such as information on the .NET Core runtime and the .NET Core SDK, see [About .NET Core: Composition](https://learn.microsoft.com/en-us/dotnet/core/about#composition).

Include the following NuGet packages to provide automatic logging features for apps deployed to Azure App Service:

*   [Microsoft.AspNetCore.AzureAppServices.HostingStartup](https://www.nuget.org/packages/Microsoft.AspNetCore.AzureAppServices.HostingStartup/) uses [IHostingStartup](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/platform-specific-configuration?view=aspnetcore-10.0) to provide ASP.NET Core logging integration with Azure App Service. The added logging features are provided by the `Microsoft.AspNetCore.AzureAppServicesIntegration` package.
*   [Microsoft.AspNetCore.AzureAppServicesIntegration](https://www.nuget.org/packages/Microsoft.AspNetCore.AzureAppServicesIntegration/) executes [AddAzureWebAppDiagnostics](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.azureappservicesloggerfactoryextensions.addazurewebappdiagnostics) to add Azure App Service diagnostics logging providers in the `Microsoft.Extensions.Logging.AzureAppServices` package.
*   [Microsoft.Extensions.Logging.AzureAppServices](https://www.nuget.org/packages/Microsoft.Extensions.Logging.AzureAppServices/) provides logger implementations to support Azure App Service diagnostics logs and log streaming features.

The preceding packages must be explicitly referenced in the app's project file.

App settings in the Azure portal permit you to set environment variables for the app. For more information, see the following resources:

*   [Configure an App Service app (Azure documentation)](https://learn.microsoft.com/en-us/azure/app-service/configure-common)
*   [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0#environment-variables-configuration-provider)

The [IIS Integration Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#enable-the-iisintegration-components), which configures Forwarded Headers Middleware when hosting [out-of-process](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#out-of-process-hosting-model), and the ASP.NET Core Module are configured to forward the scheme (HTTP/HTTPS) and the remote IP address where the request originated. Additional configuration might be required for apps hosted behind additional proxy servers and load balancers. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

ASP.NET Core apps deployed to App Service automatically receive an App Service extension, **ASP.NET Core Logging Integration**. The extension enables logging integration for ASP.NET Core apps on Azure App Service.

ASP.NET Core apps deployed to App Service automatically receive an App Service extension, **ASP.NET Core Logging Extensions**. The extension enables logging integration for ASP.NET Core apps on Azure App Service.

For monitoring, logging, and troubleshooting information, see the following articles:

[Monitor apps in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/web-sites-monitor)

 Learn how to review quotas and metrics for apps and App Service plans.

[Enable diagnostics logging for apps in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/web-sites-enable-diagnostic-log)

 Discover how to enable and access diagnostic logging for HTTP status codes, failed requests, and web server activity.

[Handle errors in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-10.0)

 Understand common approaches to handling errors in ASP.NET Core apps.

[Troubleshoot ASP.NET Core on Azure App Service and IIS](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot-azure-iis?view=aspnetcore-10.0)

 Learn how to diagnose issues with Azure App Service deployments with ASP.NET Core apps.

[Common error troubleshooting for Azure App Service and IIS with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-iis-errors-reference?view=aspnetcore-10.0)

 See the common deployment configuration errors for apps hosted by Azure App Service/IIS with troubleshooting advice.

[ASP.NET Core Data Protection keys](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/implementation/key-management?view=aspnetcore-10.0#data-protection-implementation-key-management) are persisted to the _%HOME%\ASP.NET\DataProtection-Keys_ folder. This folder is backed by network storage and is synchronized across all machines hosting the app. Keys aren't protected at rest. This folder supplies the key ring to all instances of an app in a single deployment slot. Separate deployment slots, such as Staging and Production, don't share a key ring.

When swapping between deployment slots, any system using data protection won't be able to decrypt stored data using the key ring inside the previous slot. ASP.NET Cookie Middleware uses data protection to protect its cookies. This leads to users being signed out of an app that uses the standard ASP.NET Cookie Middleware. For a slot-independent key ring solution, use an external key ring provider, such as:

*   Azure Blob Storage
*   Azure Key Vault
*   SQL store
*   Redis cache

For more information, see [Key storage providers in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/implementation/key-storage-providers?view=aspnetcore-10.0). [](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0)

To deploy an app that uses a preview release of .NET Core, see the following resources. These approaches are also used when the runtime is available but the SDK hasn't been installed on Azure App Service.

*   [Specify the .NET Core SDK Version using Azure Pipelines](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#specify-the-net-core-sdk-version-using-azure-pipelines)
*   [Deploy a self-contained preview app](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#deploy-a-self-contained-preview-app)
*   [Use Docker with Web Apps for containers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#use-docker-with-web-apps-for-containers)
*   [Install the preview site extension](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#install-the-preview-site-extension)

See [Select the .NET Core version to use](https://learn.microsoft.com/en-us/dotnet/core/versions/selection) for information on selecting the version of the .NET SDK for self-contained deployments.

Use [Azure App Service CI/CD scenarios](https://learn.microsoft.com/en-us/azure/app-service/deploy-continuous-deployment) to set up a continuous integration build with Azure DevOps. After the Azure DevOps build is created, optionally configure the build to use a specific SDK version.

When using the App Service deployment center to create an Azure DevOps build, the default build pipeline includes steps for `Restore`, `Build`, `Test`, and `Publish`. To specify the SDK version, select the **Add (+)** button in the Agent job list to add a new step. Search for **.NET Core SDK** in the search bar.

![Image 1: Add the .NET Core SDK step](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/index/add-sdk-step.png?view=aspnetcore-10.0)

Move the step into the first position in the build so that the steps following it use the specified version of the .NET Core SDK. Specify the version of the .NET Core SDK. In this example, the SDK is set to `3.0.100`.

![Image 2: Completed SDK step](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/index/sdk-step-first-place.png?view=aspnetcore-10.0)

To publish a [self-contained deployment (SCD)](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd), configure SCD in the `Publish` step and provide the [Runtime Identifier (RID)](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog).

![Image 3: Self-contained publish](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/index/self-contained.png?view=aspnetcore-10.0)

A [self-contained deployment (SCD)](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd) that targets a preview runtime carries the preview runtime in the deployment.

When deploying a self-contained app:

*   The site in Azure App Service doesn't require the [preview site extension](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#install-the-preview-site-extension).
*   The app must be published following a different approach than when publishing for a [framework-dependent deployment (FDD)](https://learn.microsoft.com/en-us/dotnet/core/deploying#framework-dependent-deployments-fdd).

Follow the guidance in the [Deploy the app self-contained](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#deploy-the-app-self-contained) section.

The Docker Hub at `https://hub.docker.com/_/microsoft-dotnet` contains the latest preview Docker images. The images can be used as a base image. Use the image and deploy to Web Apps for Containers normally.

If a problem occurs using the preview site extension, open an [dotnet/AspNetCore issue](https://github.com/dotnet/AspNetCore/issues).

1.   From the Azure portal, navigate to the App Service.
2.   Select the web app.
3.   Type "ex" in the search box to filter for "Extensions" or scroll down the list of management tools.
4.   Select **Extensions**.
5.   Select **Add**.
6.   Select the **ASP.NET Core {X.Y} ({x64|x86}) Runtime** extension from the list, where `{X.Y}` is the ASP.NET Core preview version and `{x64|x86}` specifies the platform.
7.   Select **OK** to accept the legal terms.
8.   Select **OK** to install the extension.

When the operation completes, the latest .NET Core preview is installed. Verify the installation:

1.   Select **Advanced Tools**.

2.   Select **Go** in **Advanced Tools**.

3.   Select the **Debug console**>**PowerShell** menu item.

4.   At the PowerShell prompt, execute the following command. Substitute the ASP.NET Core runtime version for `{X.Y}` and the platform for `{PLATFORM}` in the command:

```
Test-Path D:\home\SiteExtensions\AspNetCoreRuntime.{X.Y}.{PLATFORM}\
```

The command returns `True` when the x64 preview runtime is installed.

Note

The platform architecture (x86/x64) of an App Services app is set in the app's settings in the Azure portal for apps that are hosted on an A-series compute (Basic) or higher hosting tier. Confirm that the app's publish settings (for example, in the Visual Studio [publish profile (.pubxml)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/visual-studio-publish-profiles?view=aspnetcore-10.0)) match the setting in the app's service configuration in the Azure portal.

If the app is run in in-process mode and the platform architecture is configured for 64-bit (x64), the ASP.NET Core Module uses the 64-bit preview runtime, if present. Install the **ASP.NET Core {X.Y} (x64) Runtime** extension using the Azure portal.

After installing the x64 preview runtime, run the following command in the Azure Kudu PowerShell command window to verify the installation. Substitute the ASP.NET Core runtime version for `{X.Y}` in the following command:

```
Test-Path D:\home\SiteExtensions\AspNetCoreRuntime.{X.Y}.x64\
```

The command returns `True` when the x64 preview runtime is installed.

**Use the preview site extension with an ARM template**

If an ARM template is used to create and deploy apps, the `Microsoft.Web/sites/siteextensions` resource type can be used to add the site extension to a web app. In the following example, the .NET 5 (x64) Runtime site extension (`AspNetCoreRuntime.5.0.x64`) is added to the app:

```
{
    ...
    "parameters": {
        "site_name": {
            "defaultValue": "{SITE NAME}",
            "type": "String"
        },
        ...
    },       
    ...
    "resources": [
        ...
        {
            "type": "Microsoft.Web/sites/siteextensions",
            "apiVersion": "2018-11-01",
            "name": "[concat(parameters('site_name'), '/AspNetCoreRuntime.5.0.x64')]",
            "location": "[resourceGroup().location]",
            "dependsOn": [
                "[resourceId('Microsoft.Web/sites', parameters('site_name'))]"
            ]
        }
    ]
}
```

For the placeholder `{SITE NAME}`, use the app's name in Azure App Service (for example, `contoso`).

For a 64-bit deployment:

*   Use a 64-bit .NET Core SDK to build a 64-bit app.
*   Set the **Platform** to **64 Bit** in the App Service's **Configuration**>**General settings**. The app must use a Basic or higher service plan to enable the choice of platform bitness.

Apps published as framework-dependent are cross-platform and don't include the .NET runtime in the deployment. Azure App Service includes the .NET runtime.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#tabpanel_1_net-cli)

1.   Right-click the project in **Solution Explorer** and select **Publish**. Alternatively, select **Build**>**Publish {Application Name}** from the Visual Studio toolbar.
2.   In the **Publish** dialog, select **Azure**>**Next**.
3.   Select the Azure service.
4.   Select **Advanced**. The **Publish** dialog opens.
5.   Select a Resource group and Hosting plan, or create new ones.
6.   Select **Finish**.
7.   In the **Publish** page: 
    *   For **Configuration**, select the pen icon **Edit Configuration**: 
        *   Confirm that the **Release** configuration is selected.
        *   In the **Deployment Mode** drop-down list, select **Framework-Dependent**.
        *   In the **Target Runtime** drop-down list, select the desired runtime. The default is `win-x86`.

    *   To remove additional files upon deployment, open **File Publish Options** and select the checkbox to remove additional files at the destination.
    *   Select **Save**.
    *   Select **Publish**.

Publishing an app as self-contained produces a platform-specific executable. The output publishing folder contains all components of the app, including the .NET libraries and target runtime. For more information, see [Publish self-contained]/dotnet/core/deploying/#publish-self-contained). Use Visual Studio or the .NET CLI for a [self-contained deployment (SCD)](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0#tabpanel_2_net-cli)

1.   Right-click the project in **Solution Explorer** and select **Publish**. Alternatively, select **Build**>**Publish {Application Name}** from the Visual Studio toolbar.
2.   In the **Publish** dialog, select **Azure**>**Next**.
3.   Select the Azure service.
4.   Select **Advanced**. The **Publish** dialog opens.
5.   Select a Resource group and Hosting plan, or create new ones.
6.   Select **Finish**.
7.   In the **Publish** page: 
    *   For **Configuration**, select the pen icon **Edit Configuration**: 
        *   Confirm that the **Release** configuration is selected.
        *   In the **Deployment Mode** drop-down list, select **Self-Contained**.
        *   In the **Target Runtime** drop-down list, select the desired runtime. The default is `win-x86`.

    *   To remove additional files upon deployment, open **File Publish Options** and select the checkbox to remove additional files at the destination.
    *   Select **Save**.
    *   Select **Publish**.

Secure protocol bindings allow specifying a certificate to use when responding to requests over HTTPS. Binding requires a valid private certificate (_.pfx_) issued for the specific hostname. For more information, see [Tutorial: Bind an existing custom SSL certificate to Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-ssl).

If you need to transform _web.config_ on publish (for example, set environment variables based on the configuration, profile, or environment), see [Transform web.config](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/transform-webconfig?view=aspnetcore-10.0).

*   [App Service overview](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-overview)
*   [Azure App Service diagnostics overview](https://learn.microsoft.com/en-us/azure/app-service/app-service-diagnostics)
*   [Host ASP.NET Core in a web farm](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/web-farm?view=aspnetcore-10.0)
*   [Tutorial: Connect to SQL Database from .NET App Service without secrets using a managed identity](https://learn.microsoft.com/en-us/azure/app-service/tutorial-connect-msi-sql-database?tabs=efcore%2Cdotnetcore)

Azure App Service on Windows Server uses [Internet Information Services (IIS)](https://www.iis.net/). [Kestrel and YARP](https://devblogs.microsoft.com/dotnet/bringing-kestrel-and-yarp-to-azure-app-services/) on the front end provides the load balancer. The following topics pertain to the underlying IIS technology:

*   [Host ASP.NET Core on Windows with IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0)
*   [ASP.NET Core Module (ANCM) for IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0)
*   [IIS modules with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/modules?view=aspnetcore-10.0)
*   [Windows Server - IT administrator content for current and previous releases](https://learn.microsoft.com/en-us/windows-server/windows-server-versions)
