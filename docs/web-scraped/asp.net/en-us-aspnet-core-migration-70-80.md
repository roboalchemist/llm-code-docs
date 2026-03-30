# Source: https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0

Title: Migrate from ASP.NET Core in .NET 7 to .NET 8

URL Source: https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0

Markdown Content:
This article explains how to update an existing ASP.NET Core in .NET 7 project to .NET 8.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 1: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

If you rely on a [`global.json`](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json) file to target a specific .NET SDK version, update the `version` property to the .NET 8 SDK version that's installed. For example:

```
{
  "sdk": {
-    "version": "7.0.100"
+    "version": "8.0.100"
  }
}
```

Update the project file's [Target Framework Moniker (TFM)](https://learn.microsoft.com/en-us/dotnet/standard/frameworks) to `net8.0`:

```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
-    <TargetFramework>net7.0</TargetFramework>
+    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>

</Project>
```

In the project file, update each [`Microsoft.AspNetCore.*`](https://www.nuget.org/packages?q=Microsoft.AspNetCore.*), [`Microsoft.EntityFrameworkCore.*`](https://www.nuget.org/packages?q=Microsoft.EntityFrameworkCore.*), [`Microsoft.Extensions.*`](https://www.nuget.org/packages?q=Microsoft.Extensions.*), and [`System.Net.Http.Json`](https://www.nuget.org/packages/System.Net.Http.Json) package reference's `Version` attribute to 8.0.0 or later. For example:

```
<ItemGroup>
-   <PackageReference Include="Microsoft.AspNetCore.JsonPatch" Version="7.0.12" />
-   <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="7.0.12" />
-   <PackageReference Include="Microsoft.Extensions.Caching.Abstractions" Version="7.0.0" />
-   <PackageReference Include="System.Net.Http.Json" Version="7.0.1" />
+   <PackageReference Include="Microsoft.AspNetCore.JsonPatch" Version="8.0.0" />
+   <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="8.0.0" />
+   <PackageReference Include="Microsoft.Extensions.Caching.Abstractions" Version="8.0.0" />
+   <PackageReference Include="System.Net.Http.Json" Version="8.0.0" />
</ItemGroup>
```

The following migration scenarios are covered:

*   [Update a Blazor Server app](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-a-blazor-server-app)
*   [Adopt all Blazor Web App conventions](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#adopt-all-blazor-web-app-conventions)
*   [Convert a Blazor Server app into a Blazor Web App](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#convert-a-blazor-server-app-into-a-blazor-web-app)
*   [Update a Blazor WebAssembly app](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-a-blazor-webassembly-app)
*   [Convert a hosted Blazor WebAssembly app into a Blazor Web App](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#convert-a-hosted-blazor-webassembly-app-into-a-blazor-web-app)
*   [Update service and endpoint option configuration](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-service-and-endpoint-option-configuration)
*   [Drop Blazor Server with Yarp routing workaround](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#drop-blazor-server-with-yarp-routing-workaround)
*   [Migrate `CascadingValue` components in layout components](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#migrate-cascadingvalue-components-in-layout-components)
*   [Migrate the `BlazorEnableCompression` MSBuild property](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#migrate-the-blazorenablecompression-msbuild-property)
*   [Migrate the `<CascadingAuthenticationState>` component to cascading authentication state services](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#migrate-the-cascadingauthenticationstate-component-to-cascading-authentication-state-services)
*   [_New article_: HTTP caching issues during migration](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#new-article-on-http-caching-issues)
*   [_New article_: New article on class libraries with static server-side rendering (static SSR)](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#new-article-on-class-libraries-with-static-server-side-rendering-static-ssr)
*   [Discover components from additional assemblies](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#discover-components-from-additional-assemblies)
*   [Drop `[Parameter]` attribute when the parameter is supplied from a query string](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#drop-parameter-attribute-when-the-parameter-is-supplied-from-a-query-string)
*   [Blazor Server script fallback policy authorization](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#blazor-server-script-fallback-policy-authorization)

For guidance on adding Blazor support to an ASP.NET Core app, see [Integrate ASP.NET Core Razor components with MVC or Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/integration?view=aspnetcore-10.0#add-blazor-support-to-an-aspnet-core-app).

We recommend using Blazor Web Apps in .NET 8, but Blazor Server is supported. To continue using Blazor Server with .NET 8, follow the guidance in the first three sections of this article:

*   [Update the .NET SDK version in `global.json`](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-net-sdk-version-in-globaljson)
*   [Update the target framework](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-target-framework)
*   [Update package references](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-package-references)

New Blazor features introduced for Blazor Web Apps aren't available to a Blazor Server app updated to run under .NET 8. If you wish to adopt the new .NET 8 Blazor features, follow the guidance in either of the following sections:

*   [Adopt all Blazor Web App conventions](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#adopt-all-blazor-web-app-conventions)
*   [Convert a Blazor Server app into a Blazor Web App](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#convert-a-blazor-server-app-into-a-blazor-web-app)

To optionally adopt all of the new Blazor Web App conventions, we recommend the following process:

*   Create a new app from the Blazor Web App project template. For more information, see [Tooling for ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/tooling?view=aspnetcore-10.0).
*   Move the your app's components and code to the new Blazor Web App, making modifications to adopt new features.
*   Update the layout and styles of the Blazor Web App.

New .NET 8 features are covered in [What's new in ASP.NET Core in .NET 8](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-8.0?view=aspnetcore-10.0#blazor). When updating an app from .NET 6 or earlier, see the migration and release notes (_What's new_ articles) for intervening releases.

Blazor Server apps are supported in .NET 8 without any code changes. Use the following guidance to convert a Blazor Server app into an equivalent .NET 8 Blazor Web App, which makes all of the [new .NET 8 features](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-8.0?view=aspnetcore-10.0#blazor) available.

Important

This section focuses on the minimal changes required to convert a .NET 7 Blazor Server app into a .NET 8 Blazor Web App. To adopt all of the new Blazor Web App conventions, follow the guidance in the [Adopt all Blazor Web App conventions](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#adopt-all-blazor-web-app-conventions) section.

1.   Follow the guidance in the first three sections of this article:

    *   [Update the .NET SDK version in `global.json`](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-net-sdk-version-in-globaljson)
    *   [Update the target framework](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-target-framework)
    *   [Update package references](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-package-references)

2.   Move the contents of the `App` component (`App.razor`) to a new `Routes` component file (`Routes.razor`) added to the project's root folder. Leave the empty `App.razor` file in the app in the project's root folder.

3.   Add an entry to the `_Imports.razor` file to make shorthand render modes available to the app:

```
@using static Microsoft.AspNetCore.Components.Web.RenderMode
```
4.   Move the content in the `_Host` page (`Pages/_Host.cshtml`) to the empty `App.razor` file. Proceed to make the following changes to the `App` component.

Note

In the following example, the project's namespace is `BlazorServerApp`. Adjust the namespace to match your project. 
Remove the following lines from the top of the file:

```
- @page "/"
- @using Microsoft.AspNetCore.Components.Web
- @namespace BlazorServerApp.Pages
- @addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
```

Replace the preceding lines with a line that injects an [IHostEnvironment](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihostenvironment) instance:

```
@inject IHostEnvironment Env
```

Remove the tilde (`~`) from the `href` of the `<base>` tag and replace with the base path for your app:

```
- <base href="~/" />
+ <base href="/" />
```

Remove the Component Tag Helper for the [HeadOutlet](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.headoutlet) component and replace it with the [HeadOutlet](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.headoutlet) component.

Remove the following line:

```
- <component type="typeof(HeadOutlet)" render-mode="ServerPrerendered" />
```

Replace the preceding line with the following:

```
<HeadOutlet @rendermode="InteractiveServer" />
```

Remove the Component Tag Helper for the `App` component and replace it with the `Routes` component.

Remove the following line:

```
- <component type="typeof(App)" render-mode="ServerPrerendered" />
```

Replace the preceding line with the following:

```
<Routes @rendermode="InteractiveServer" />
```
Note

The preceding configuration assumes that the app's components adopt interactive server rendering. For more information, including how to adopt static server-side rendering (SSR), see [ASP.NET Core Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0). 
Remove the Environment Tag Helpers for error UI and replace them with the following Razor markup.

Remove the following lines:

```
- <environment include="Staging,Production">
-     An error has occurred. This application may no longer respond until reloaded.
- </environment>
- <environment include="Development">
-     An unhandled exception has occurred. See browser dev tools for details.
- </environment>
```

Replace the preceding lines with the following:

```
@if (Env.IsDevelopment())
{
    <text>
        An unhandled exception has occurred. See browser dev tools for details.
    </text>
}
else
{
    <text>
        An error has occurred. This app may no longer respond until reloaded.
    </text>
}
```

Change the Blazor script from `blazor.server.js` to `blazor.web.js`:

```
- <script src="_framework/blazor.server.js"></script>
+ <script src="_framework/blazor.web.js"></script>
```
5.   Delete the `Pages/_Host.cshtml` file.

6.   Update `Program.cs`:

Note

In the following example, the project's namespace is `BlazorServerApp`. Adjust the namespace to match your project. 
Add a `using` statement to the top of the file for the project's namespace:

```
using BlazorServerApp;
```

Replace [AddServerSideBlazor](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.componentservicecollectionextensions.addserversideblazor) with [AddRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.razorcomponentsservicecollectionextensions.addrazorcomponents) and a chained call to [AddInteractiveServerComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.serverrazorcomponentsbuilderextensions.addinteractiveservercomponents).

Remove the following line:

```
- builder.Services.AddServerSideBlazor();
```

Replace the preceding line with Razor component and interactive server component services. Calling [AddRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.razorcomponentsservicecollectionextensions.addrazorcomponents) adds antiforgery services ([AddAntiforgery](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.antiforgeryservicecollectionextensions.addantiforgery)) by default.

```
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();
```

Remove the following line:

```
- app.MapBlazorHub();
```

Replace the preceding line with a call to [MapRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorcomponentsendpointroutebuilderextensions.maprazorcomponents), supplying the `App` component as the root component type, and add a chained call to [AddInteractiveServerRenderMode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.serverrazorcomponentsendpointconventionbuilderextensions.addinteractiveserverrendermode):

```
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();
```

Remove the following line:

```
- app.MapFallbackToPage("/_Host");
```

Remove Routing Middleware:

```
- app.UseRouting();
```

Add [Antiforgery Middleware](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0#antiforgery-support) to the request processing pipeline after the line that adds HTTPS Redirection Middleware (`app.UseHttpsRedirection`):

```
app.UseAntiforgery();
```

The preceding call to `app.UseAntiforgery` must be placed after calls, if present, to `app.UseAuthentication` and `app.UseAuthorization`. There's no need to explicitly add antiforgery services (`builder.Services.AddAntiforgery`), as they're added automatically by [AddRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.razorcomponentsservicecollectionextensions.addrazorcomponents), which was covered earlier.

7.   If the Blazor Server app was configured to disable prerendering, you can continue to disable prerendering for the updated app. In the `App` component, change the value assigned to the `@rendermode` Razor directive attributes for the [HeadOutlet](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.headoutlet) and `Routes` components.

Change the value of the `@rendermode` directive attribute for both the [HeadOutlet](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.headoutlet) and `Routes` components to disable prerendering:

```
- @rendermode="InteractiveServer"
+ @rendermode="new InteractiveServerRenderMode(prerender: false)"
```

For more information, see [ASP.NET Core Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#prerendering).

Follow the guidance in the first three sections of this article:

*   [Update the .NET SDK version in `global.json`](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-net-sdk-version-in-globaljson)
*   [Update the target framework](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-target-framework)
*   [Update package references](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-package-references)

For apps that adopt [lazy assembly loading](https://learn.microsoft.com/en-us/aspnet/core/blazor/webassembly-lazy-load-assemblies?view=aspnetcore-10.0), change the file extension from `.dll` to `.wasm` in the app's implementation to reflect Blazor WebAssembly's adoption of [Webcil assembly packaging](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-8.0?view=aspnetcore-10.0#web-friendly-webcil-packaging).

Prior to the release of .NET 8, guidance in [Deployment layout for ASP.NET Core hosted Blazor WebAssembly apps](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/webassembly/deployment-layout?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0) addresses environments that block clients from downloading and executing DLLs with a multipart bundling approach. In .NET 8 or later, Blazor uses the Webcil file format to address this problem. Multipart bundling using the experimental NuGet package described by the _WebAssembly deployment layout_ article isn't supported for Blazor apps in .NET 8 or later. If you desire to continue using the multipart bundle package in .NET 8 or later apps, you can use the guidance in the article to create your own multipart bundling NuGet package, but it won't be supported by Microsoft.

Blazor WebAssembly apps are supported in .NET 8 without any code changes. Use the following guidance to convert an ASP.NET Core hosted Blazor WebAssembly app into an equivalent .NET 8 Blazor Web App, which makes all of the [new .NET 8 features](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-8.0?view=aspnetcore-10.0#blazor) available.

Important

This section focuses on the minimal changes required to convert a .NET 7 ASP.NET Core hosted Blazor WebAssembly app into a .NET 8 Blazor Web App. To adopt all of the new Blazor Web App conventions, follow the guidance in the [Adopt all Blazor Web App conventions](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#adopt-all-blazor-web-app-conventions) section.

1.   Follow the guidance in the first three sections of this article:

    *   [Update the .NET SDK version in `global.json`](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-net-sdk-version-in-globaljson)
    *   [Update the target framework](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-the-target-framework)
    *   [Update package references](https://learn.microsoft.com/en-us/aspnet/core/migration/70-80?view=aspnetcore-10.0#update-package-references)

Important

Using the preceding guidance, update the `.Client`, `.Server`, and `.Shared` projects of the solution.

2.   In the `.Client` project file (`.csproj`), add the following MSBuild properties:

```
<NoDefaultLaunchSettingsFile>true</NoDefaultLaunchSettingsFile>
<StaticWebAssetProjectMode>Default</StaticWebAssetProjectMode>
```

Also in the `.Client` project file, remove the [`Microsoft.AspNetCore.Components.WebAssembly.DevServer`](https://www.nuget.org/packages/Microsoft.AspNetCore.Components.WebAssembly.DevServer) package reference:

```
- <PackageReference Include="Microsoft.AspNetCore.Components.WebAssembly.DevServer"... />
```
3.   Move the file content from the `.Client/wwwroot/index.html` file to a new `App` component file (`App.razor`) created at the root of the `.Server` project. After you move the file's contents, delete the `index.html` file.

Rename `App.razor` in the `.Client` project to `Routes.razor`.

In `Routes.razor`, update the value of the `AppAssembly` attribute to `typeof(Program).Assembly`.

4.   In the `.Client` project, add an entry to the `_Imports.razor` file to make shorthand render modes available to the app:

```
@using static Microsoft.AspNetCore.Components.Web.RenderMode
```

Make a copy of the `.Client` project's `_Imports.razor` file and add it to the `.Server` project.

5.   Make the following changes to the `App.razor` file:

Replace the website's default website title (`<title>...</title>`) with a [HeadOutlet](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.headoutlet) component. Note the website title for use later and remove the title tags and title:

```
- <title>...</title>
```

Where you removed the title, place a [HeadOutlet](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.headoutlet) component assigning the Interactive WebAssembly render mode (prerendering disabled):

```
<HeadOutlet @rendermode="new InteractiveWebAssemblyRenderMode(prerender: false)" />
```

Change the [CSS style bundle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation?view=aspnetcore-10.0#css-isolation-bundling):

```
- <link href="{CLIENT PROJECT ASSEMBLY NAME}.styles.css" rel="stylesheet">
+ <link href="{SERVER PROJECT ASSEMBLY NAME}.styles.css" rel="stylesheet">
```

Placeholders in the preceding code:

    *   `{CLIENT PROJECT ASSEMBLY NAME}`: Client project assembly name. Example: `BlazorSample.Client`
    *   `{SERVER PROJECT ASSEMBLY NAME}`: Server project assembly name. Example: `BlazorSample.Server`

Locate following `<div>...</div>` HTML markup:

```
- <div id="app">
-     ...
- </div>
```

Replace the preceding `<div>...</div>` HTML markup with the `Routes` component using the Interactive WebAssembly render mode (prerendering disabled):

```
<Routes @rendermode="new InteractiveWebAssemblyRenderMode(prerender: false)" />
```

Update the `blazor.webassembly.js` script to `blazor.web.js`:

```
- <script src="_framework/blazor.webassembly.js"></script>
+ <script src="_framework/blazor.web.js"></script>
```
6.   Open the `.Client` project's layout file (`.Client/Shared/MainLayout.razor`) and add a [PageTitle](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.pagetitle) component with the website's default title (`{TITLE}` placeholder):

```
<PageTitle>{TITLE}</PageTitle>
```
7.   Remove the following lines from `.Client/Program.cs`:

```
- builder.RootComponents.Add<App>("#app");
- builder.RootComponents.Add<HeadOutlet>("head::after");
```
8.   Update `.Server/Program.cs`:

Add Razor component and interactive WebAssembly component services to the project. Call [AddRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.razorcomponentsservicecollectionextensions.addrazorcomponents) with a chained call to [AddInteractiveWebAssemblyComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.webassemblyrazorcomponentsbuilderextensions.addinteractivewebassemblycomponents). Calling [AddRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.razorcomponentsservicecollectionextensions.addrazorcomponents) adds antiforgery services ([AddAntiforgery](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.antiforgeryservicecollectionextensions.addantiforgery)) by default.

```
builder.Services.AddRazorComponents()
    .AddInteractiveWebAssemblyComponents();
```

Add [Antiforgery Middleware](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0#antiforgery-support) to the request processing pipeline.

Place the following line after the call to `app.UseHttpsRedirection`. The call to `app.UseAntiforgery` must be placed after calls, if present, to `app.UseAuthentication` and `app.UseAuthorization`. There's no need to explicitly add antiforgery services (`builder.Services.AddAntiforgery`), as they're added automatically by [AddRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.razorcomponentsservicecollectionextensions.addrazorcomponents), which was covered earlier.

```
app.UseAntiforgery();
```

Remove the following line:

```
- app.UseBlazorFrameworkFiles();
```

Remove the following line:

```
- app.MapFallbackToFile("index.html");
```

Replace the preceding line with a call to [MapRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorcomponentsendpointroutebuilderextensions.maprazorcomponents), supplying the `App` component as the root component type, and add chained calls to [AddInteractiveWebAssemblyRenderMode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webassemblyrazorcomponentsendpointconventionbuilderextensions.addinteractivewebassemblyrendermode) and [AddAdditionalAssemblies](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorcomponentsendpointconventionbuilderextensions.addadditionalassemblies):

```
app.MapRazorComponents<App>()
    .AddInteractiveWebAssemblyRenderMode()
    .AddAdditionalAssemblies(typeof({CLIENT APP NAMESPACE}._Imports).Assembly);
```

In the preceding example, the `{CLIENT APP NAMESPACE}` placeholder is the namespace of the `.Client` project (for example, `HostedBlazorApp.Client`).

9.   Run the solution from the `.Server` project:

For Visual Studio, confirm that the `.Server` project is selected in **Solution Explorer** when running the app.

If using the .NET CLI, run the project from the `.Server` project's folder.

With the release of Blazor Web Apps in .NET 8, Blazor service and endpoint option configuration is updated with the introduction of new API for interactive component services and component endpoint configuration.

Updated configuration guidance appears in the following locations:

*   [Setting and reading the app's environment](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/environments?view=aspnetcore-10.0): Contains updated guidance, especially in the section titled _Read the environment client-side in a Blazor Web App_.
*   [Server-side circuit handler options](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/signalr?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#server-side-circuit-handler-options): Covers new Blazor-SignalR circuit and hub options configuration.
*   [Render Razor components from JavaScript](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/js-spa-frameworks?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#render-razor-components-from-javascript): Covers dynamic component registration with [RegisterForJavaScript](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.web.jscomponentconfigurationextensions.registerforjavascript).
*   [Blazor custom elements: Blazor Web App registration](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/js-spa-frameworks?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#blazor-web-app-registration): Covers root component custom element registration with `RegisterCustomElement`.
*   [Prefix for Blazor WebAssembly assets](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/static-files?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#prefix-for-blazor-webassembly-assets): Covers control of the path string that indicates the prefix for Blazor WebAssembly assets.
*   [Temporary redirection URL validity duration](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#temporary-redirection-url-validity-duration): Covers control of the lifetime of data protection validity for temporary redirection URLs emitted by Blazor server-side rendering.
*   [Detailed errors](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/handle-errors?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#detailed-errors-for-razor-component-server-side-rendering): Covers enabling detailed errors for Razor component server-side rendering.
*   [Prerendering configuration](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#prerendering): Prerendering is enabled by default for Blazor Web Apps. Follow this link for guidance on how to disable prerendering if you have special circumstances that require an app to disable prerendering.
*   [Form binding options](https://learn.microsoft.com/en-us/aspnet/core/blazor/forms/binding?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#additional-binding-options): Covers form binding options configuration.

If you previously followed the guidance in [Enable ASP.NET Core Blazor Server support with Yarp in incremental migration](https://learn.microsoft.com/en-us/aspnet/core/migration/fx-to-core/inc/blazor?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-7.0) for migrating a Blazor Server app with Yarp to .NET 6 or .NET 7, you can reverse the workaround steps that you took when following the article's guidance. Routing and deep linking for Blazor Server with Yarp work correctly in .NET 8.

Cascading parameters don't pass data across render mode boundaries, and layouts are statically rendered in otherwise interactive apps. Therefore, apps that seek to use cascading parameters in interactively rendered components won't be able to cascade the values from a layout.

The two approaches for migration are:

*   (_Recommended_) Pass the state as a root-level cascading value. For more information, see the guidance on [root-level cascading values](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/cascading-values-and-parameters?view=aspnetcore-10.0#root-level-cascading-values) and [root-level cascading values with notifications](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/cascading-values-and-parameters?view=aspnetcore-10.0#root-level-cascading-values-with-notifications).
*   Wrap the router in the `Routes` component with the [`CascadingValue`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.cascadingvalue-1) component and make the `Routes` component interactively rendered. For an example, see [`CascadingValue` component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/cascading-values-and-parameters?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#cascadingvalue-component).

For more information, see [Cascading values/parameters and render mode boundaries](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/cascading-values-and-parameters?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#cascading-valuesparameters-and-render-mode-boundaries).

For Blazor WebAssembly apps that disable compression and target .NET 7 or earlier but are built with the .NET 8 SDK, the `BlazorEnableCompression` MSBuild property has changed to `CompressionEnabled`:

```
<PropertyGroup>
-   <BlazorEnableCompression>false</BlazorEnableCompression>
+   <CompressionEnabled>false</CompressionEnabled>
</PropertyGroup>
```

When using the .NET CLI publish command, use the new property:

```
dotnet publish -p:CompressionEnabled=false
```

For more information, see the following resources:

*   [Static Web Assets Compression Flag Breaking Change (dotnet/announcements #283)](https://github.com/dotnet/announcements/issues/283)
*   [Host and deploy ASP.NET Core Blazor WebAssembly](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/webassembly/?view=aspnetcore-10.0&preserve-view=true&view=aspnetcore-8.0#compression)

In .NET 7 or earlier, the [CascadingAuthenticationState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.authorization.cascadingauthenticationstate) component is wrapped around some part of the UI tree, for example around the Blazor router, to provide cascading authentication state:

```
<CascadingAuthenticationState>
    <Router ...>
        ...
    </Router>
</CascadingAuthenticationState>
```

In .NET 8, don't use the [CascadingAuthenticationState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.components.authorization.cascadingauthenticationstate) component:

```
- <CascadingAuthenticationState>
      <Router ...>
          ...
      </Router>
- </CascadingAuthenticationState>
```

Instead, add cascading authentication state services to the service collection by calling [AddCascadingAuthenticationState](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.cascadingauthenticationstateservicecollectionextensions.addcascadingauthenticationstate) in the `Program` file:

```
builder.Services.AddCascadingAuthenticationState();
```

For more information, see the following resources:

*   _ASP.NET Core Blazor authentication and authorization_ article 
    *   [`AuthenticationStateProvider` service](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0#authenticationstateprovider-service)
    *   [Expose the authentication state as a cascading parameter](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0#expose-the-authentication-state-as-a-cascading-parameter)
    *   [Customize unauthorized content with the Router component](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0#customize-unauthorized-content-with-the-router-component)

*   [ASP.NET Core Blazor authentication and authorization](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-10.0#implement-a-custom-authenticationstateprovider)

We've added a new article that discusses some of the common HTTP caching issues that can occur when upgrading Blazor apps across major versions and how to address HTTP caching issues.

For more information, see [Avoid HTTP caching issues when upgrading ASP.NET Core Blazor apps](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/webassembly/http-caching-issues?view=aspnetcore-10.0).

We've added a new article that discusses component library authorship in Razor class libraries (RCLs) with static server-side rendering (static SSR).

For more information, see [ASP.NET Core Razor class libraries (RCLs) with static server-side rendering (static SSR)](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/class-libraries-and-static-server-side-rendering?view=aspnetcore-10.0).

When migrating from a Blazor Server app to a Blazor Web App, access the guidance in [ASP.NET Core Blazor routing](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/routing?view=aspnetcore-10.0#route-to-components-from-multiple-assemblies) if the app uses routable components from additional assemblies, such as component class libraries.

The `[Parameter]` attribute is no longer required when supplying a parameter from the query string:

```
- [Parameter]
  [SupplyParameterFromQuery]
```

In .NET 7, the Blazor Server script (`blazor.server.js`) is [served by Static File Middleware](https://github.com/dotnet/aspnetcore/blob/v7.0.16/src/Components/Server/src/DependencyInjection/ConfigureStaticFilesOptions.cs). Placing the call for Static File Middleware ([UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles)) in the request processing pipeline before the call to Authorization Middleware ([UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization)) is sufficient in .NET 7 apps to serve the Blazor script to anonymous users.

In .NET 8, the Blazor Server script is served [by its own endpoint](https://github.com/search?q=repo%3Adotnet%2Faspnetcore%20GetBlazorEndpoint&type=code), using endpoint routing. This change is introduced by [Fixed bug - Passing options to UseStaticFiles breaks Blazor Server (`dotnet/aspnetcore` #45897)](https://github.com/dotnet/aspnetcore/pull/45897).

Consider a multi-tenant scenario where:

*   Both the default and fallback policies are set identically.
*   The tenant is resolved using the first segment in the request path (for example, `tld.com/tenant-name/...`).
*   The requests to tenant endpoints are authenticated by an additional authentication scheme, which adds an additional identity to the request principal.
*   The fallback authorization policy has requirements that check claims via the additional identity.

Requests for the Blazor script file (`blazor.server.js`) are served at `/_framework/blazor.server.js`, which is hardcoded in the framework. Requests for the file aren't authenticated by the additional authentication scheme for tenants _**but are still challenged by the fallback policy**_, which results in returning an unauthorized result.

This problem is under evaluation for a new framework feature in [MapRazorComponents broken with FallbackPolicy RequireAuthenticatedUser (`dotnet/aspnetcore` 51836)](https://github.com/dotnet/aspnetcore/issues/51836), which is currently scheduled for .NET 9's release in November, 2024. Until then, you can work around this problem using any of the following three approaches:

*   Don't use a fallback policy. Apply the `[Authorize]` attribute in the `_Imports.razor` file to apply it to all of the components of the app. For non-blazor endpoints, explicitly use `[Authorize]` or `RequireAuthorization`.

*   Add `[AllowAnonymous]` to the `/_framework/blazor.server.js` endpoint in the `Program` file:

```
app.MapBlazorHub().Add(endpointBuilder =>
{
    if (endpointBuilder is 
        RouteEndpointBuilder
        { 
            RoutePattern: { RawText: "/_framework/blazor.server.js" }
        })
    {
        endpointBuilder.Metadata.Add(new AllowAnonymousAttribute());
    }
});
```
*   Register a custom `AuthorizationHandler` that [checks the `HttpContext`](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/policies?view=aspnetcore-10.0#access-mvc-request-context-in-handlers) to allow the `/_framework/blazor.server.js` file through.

For apps using Docker, update the _Dockerfile_`FROM` statements and scripts. Use a base image that includes the .NET 8 runtime. Consider the following `docker pull` command difference between ASP.NET Core in .NET 7 and .NET 8:

```
- docker pull mcr.microsoft.com/dotnet/aspnet:7.0
+ docker pull mcr.microsoft.com/dotnet/aspnet:8.0
```

The default ASP.NET Core port configured in .NET container images has been updated from port 80 to 8080.

The new `ASPNETCORE_HTTP_PORTS` environment variable was added as a simpler alternative to `ASPNETCORE_URLS`.

For more information, see:

*   [Default ASP.NET Core port changed from 80 to 8080](https://learn.microsoft.com/en-us/dotnet/core/compatibility/containers/8.0/aspnet-port).
*   [Specify ports only with `ASPNETCORE_HTTP_PORTS`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints#specify-ports-only)

Use the articles in [Breaking changes in .NET](https://learn.microsoft.com/en-us/dotnet/core/compatibility/breaking-changes) to find breaking changes that might apply when upgrading an app to a newer version of .NET.
