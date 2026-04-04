# Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0

Title: Tutorial: Get started with Razor Pages in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0

Markdown Content:
By [Rick Anderson](https://twitter.com/RickAndMSFT)

This tutorial is the first in a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0). For a video introduction, see [Entity Framework Core for Beginners](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oXCPdC3fTFA3Z79-eVH3K-s).

If you're new to ASP.NET Core development and are unsure of which ASP.NET Core web UI solution will best fit your needs, see [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0).

At the end of this tutorial, you have a Razor Pages web app that manages a database of movies.

![Image 1: Home or Index page.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/media/home10.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [The latest version of Visual Studio](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

[![Image 2: VS26 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0)](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0#lightbox)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **Create a new project**.

*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Razor Pages)**>**Next**.

*   In the **Configure your new project** dialog, enter `RazorPagesMovie` for **Project name**. Name the project **RazorPagesMovie**, including matching the capitalization, so the namespaces match when you copy and paste example code.

*   Select **Next**.

*   In the **Additional information** dialog:

    *   Select **.NET 10.0**.
    *   Verify: **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 3: Additional information dialog.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/media/net10-additional-info.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 4: Solution Explorer showing the RazorPagesMovie project structure.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/media/solution-explorer-project.png?view=aspnetcore-10.0)

For alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

Select **RazorPagesMovie** in **Solution Explorer**, and then press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project isn't yet configured to use SSL:

![Image 5: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcertvs22.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 6: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

*   Runs the app, which launches the [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).
*   Launches the default browser at `https://localhost:<port>`, which displays the app's UI. `<port>` is the random port that is assigned when the app was created.

Close the browser window.

The following sections contain an overview of the main project folders and files that you work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code by using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. `_Layout.cshtml` sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the following code:

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

app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();
app.MapRazorPages()
   .WithStaticAssets();

app.Run();
```

The following lines of code in this file create a `WebApplicationBuilder` with preconfigured defaults, add Razor Pages support to the [Dependency Injection (DI) container](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0), and build the app:

```
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();
```

The developer exception page is enabled by default and provides helpful information on exceptions. Don't run production apps in development mode because the developer exception page can leak sensitive information.

The following code sets the exception endpoint to `/Error` and enables [HTTP Strict Transport Security Protocol (HSTS)](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) when the app is _**not**_ running in development mode:

```
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
```

For example, the preceding code runs when the app is in production or test mode. For more information, see [Use multiple environments in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0).

The following code enables various [Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0):

*   `app.UseHttpsRedirection();` : Redirects HTTP requests to HTTPS.
*   `app.UseRouting();` : Adds route matching to the middleware pipeline. For more information, see [Routing in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0).
*   `app.UseAuthorization();` : Authorizes a user to access secure resources. This app doesn't use authorization, so you can remove this line.
*   `app.MapRazorPages();`: Configures endpoint routing for Razor Pages.
*   `app.MapStaticAssets()` : Optimizes the delivery of static assets in an app, such as HTML, CSS, images, and JavaScript. For more information, see [What's new in ASP.NET Core in .NET 9](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-9.0?view=aspnetcore-10.0#optimizing-static-web-asset-delivery).
*   `.WithStaticAssets();` : Ensures Razor Pages participate in the optimization system for static assets.
*   `app.Run();` : Runs the app.

If you run into a problem you can't resolve, compare your code to the completed project. [View or download completed project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie10) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

This is the first tutorial of a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0). For a video introduction, see [Entity Framework Core for Beginners](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oXCPdC3fTFA3Z79-eVH3K-s).

If you're new to ASP.NET Core development and are unsure of which ASP.NET Core web UI solution will best fit your needs, see [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0).

At the end of this tutorial, you'll have a Razor Pages web app that manages a database of movies.

![Image 7: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/9/home9.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 8: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **New project**.

*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Razor Pages)**>**Next**.

*   In the **Configure your new project** dialog, enter `RazorPagesMovie` for **Project name**. It's important to name the project **RazorPagesMovie**, including matching the capitalization, so the namespaces will match when you copy and paste example code.

*   Select **Next**.

*   In the **Additional information** dialog:

    *   Select **.NET 9.0**.
    *   Verify: **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 9: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/9/net9-additional-info.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 10: Solution Explorer](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/9/solution-explorer-project.png?view=aspnetcore-10.0)

For alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

Select **RazorPagesMovie** in **Solution Explorer**, and then press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 11: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcertvs22.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 12: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

*   Runs the app, which launches the [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).
*   Launches the default browser at `https://localhost:<port>`, which displays the apps UI. `<port>` is the random port that is assigned when the app was created.

Close the browser window.

The following sections contain an overview of the main project folders and files that you'll work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. `_Layout.cshtml` sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the following code:

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

app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();
app.MapRazorPages();

app.Run();
```

The following lines of code in this file create a `WebApplicationBuilder` with preconfigured defaults, add Razor Pages support to the [Dependency Injection (DI) container](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0), and builds the app:

```
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();
```

The developer exception page is enabled by default and provides helpful information on exceptions. Production apps should not be run in development mode because the developer exception page can leak sensitive information.

The following code sets the exception endpoint to `/Error` and enables [HTTP Strict Transport Security Protocol (HSTS)](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) when the app is _**not**_ running in development mode:

```
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
```

For example, the preceding code runs when the app is in production or test mode. For more information, see [Use multiple environments in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0).

The following code enables various [Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0):

*   `app.UseHttpsRedirection();` : Redirects HTTP requests to HTTPS.
*   `app.UseRouting();` : Adds route matching to the middleware pipeline. For more information, see [Routing in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0).
*   `app.UseAuthorization();` : Authorizes a user to access secure resources. This app doesn't use authorization, therefore this line could be removed.
*   `app.MapRazorPages();`: Configures endpoint routing for Razor Pages.
*   `app.MapStaticAssets();` : Optimize the delivery of static assets in an app, such as HTML, CSS, images, and JavaScript. For more information, see [What's new in ASP.NET Core in .NET 9](https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-9.0?view=aspnetcore-10.0#optimizing-static-web-asset-delivery).
*   `app.Run();` : Runs the app.

If you run into a problem you can't resolve, compare your code to the completed project. [View or download completed project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie90) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

This is the first tutorial of a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0). For a video introduction, see [Entity Framework Core for Beginners](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oXCPdC3fTFA3Z79-eVH3K-s).

If you're new to ASP.NET Core development and are unsure of which ASP.NET Core web UI solution will best fit your needs, see [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0).

At the end of this tutorial, you'll have a Razor Pages web app that manages a database of movies.

![Image 13: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/8/home8.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 14: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **New project**.

*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Razor Pages)**>**Next**.

*   In the **Configure your new project** dialog, enter `RazorPagesMovie` for **Project name**. It's important to name the project **RazorPagesMovie**, including matching the capitalization, so the namespaces will match when you copy and paste example code.

*   Select **Next**.

*   In the **Additional information** dialog:

    *   Select **.NET 8.0 (Long Term Support)**.
    *   Verify: **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 15: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/8/net8-additional-info.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 16: Solution Explorer](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/8/solution-explorer-project.png?view=aspnetcore-10.0)

For alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

Select **RazorPagesMovie** in **Solution Explorer**, and then press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 17: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcertvs22.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 18: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

*   Runs the app, which launches the [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).
*   Launches the default browser at `https://localhost:<port>`, which displays the apps UI. `<port>` is the random port that is assigned when the app was created.

Close the browser window.

The following sections contain an overview of the main project folders and files that you'll work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. `_Layout.cshtml` sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the following code:

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

The following lines of code in this file create a `WebApplicationBuilder` with preconfigured defaults, add Razor Pages support to the [Dependency Injection (DI) container](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0), and builds the app:

```
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();
```

The developer exception page is enabled by default and provides helpful information on exceptions. Production apps should not be run in development mode because the developer exception page can leak sensitive information.

The following code sets the exception endpoint to `/Error` and enables [HTTP Strict Transport Security Protocol (HSTS)](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) when the app is _**not**_ running in development mode:

```
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
```

For example, the preceding code runs when the app is in production or test mode. For more information, see [Use multiple environments in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0).

The following code enables various [Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0):

*   `app.UseHttpsRedirection();` : Redirects HTTP requests to HTTPS.
*   `app.UseStaticFiles();` : Enables static files, such as HTML, CSS, images, and JavaScript to be served. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).
*   `app.UseRouting();` : Adds route matching to the middleware pipeline. For more information, see [Routing in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0)
*   `app.MapRazorPages();`: Configures endpoint routing for Razor Pages.
*   `app.UseAuthorization();` : Authorizes a user to access secure resources. This app doesn't use authorization, therefore this line could be removed.
*   `app.Run();` : Runs the app.

If you run into a problem you can't resolve, compare your code to the completed project. [View or download completed project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie80) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

This is the first tutorial of a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0). For a video introduction, see [Entity Framework Core for Beginners](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oXCPdC3fTFA3Z79-eVH3K-s).

If you're new to ASP.NET Core development and are unsure of which ASP.NET Core web UI solution will best fit your needs, see [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0).

At the end of this tutorial, you'll have a Razor Pages web app that manages a database of movies.

![Image 19: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/home6.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.

![Image 20: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio and select **Create a new project**.

*   In the **Create a new project** dialog, select **ASP.NET Core Web App**>**Next**.

*   In the **Configure your new project** dialog, enter `RazorPagesMovie` for **Project name**. It's important to name the project **RazorPagesMovie**, including matching the capitalization, so the namespaces will match when you copy and paste example code.

*   Select **Next**.

*   In the **Additional information** dialog:

    *   Select **.NET 7.0 (Standard Term Support)**.
    *   Verify: **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 21: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/7/additional_info.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 22: Solution Explorer](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/se.png?view=aspnetcore-10.0)

For alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

Select **RazorPagesMovie** in **Solution Explorer**, and then press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 23: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcertvs22.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 24: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

*   Runs the app, which launches the [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).
*   Launches the default browser at `https://localhost:<port>`, which displays the apps UI. `<port>` is the random port that is assigned when the app was created.

Close the browser window.

The following sections contain an overview of the main project folders and files that you'll work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. `_Layout.cshtml` sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the following code:

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

The following lines of code in this file create a `WebApplicationBuilder` with preconfigured defaults, add Razor Pages support to the [Dependency Injection (DI) container](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0), and builds the app:

```
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();
```

The developer exception page is enabled by default and provides helpful information on exceptions. Production apps should not be run in development mode because the developer exception page can leak sensitive information.

The following code sets the exception endpoint to `/Error` and enables [HTTP Strict Transport Security Protocol (HSTS)](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) when the app is _**not**_ running in development mode:

```
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
```

For example, the preceding code runs when the app is in production or test mode. For more information, see [Use multiple environments in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0).

The following code enables various [Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0):

*   `app.UseHttpsRedirection();` : Redirects HTTP requests to HTTPS.
*   `app.UseStaticFiles();` : Enables static files, such as HTML, CSS, images, and JavaScript to be served. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).
*   `app.UseRouting();` : Adds route matching to the middleware pipeline. For more information, see [Routing in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0)
*   `app.MapRazorPages();`: Configures endpoint routing for Razor Pages.
*   `app.UseAuthorization();` : Authorizes a user to access secure resources. This app doesn't use authorization, therefore this line could be removed.
*   `app.Run();` : Runs the app.

If you run into a problem you can't resolve, compare your code to the completed project. [View or download completed project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie70) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

This is the first tutorial of a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0). For a video introduction, see [Entity Framework Core for Beginners](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oXCPdC3fTFA3Z79-eVH3K-s).

If you're new to ASP.NET Core development and are unsure of which ASP.NET Core web UI solution will best fit your needs, see [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0).

At the end of the series, you'll have an app that manages a database of movies.

In this tutorial, you:

*   Create a Razor Pages web app.
*   Run the app.
*   Examine the project files.

At the end of this tutorial, you'll have a working Razor Pages web app that you'll enhance in later tutorials.

![Image 25: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/home6.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.
*   [.NET 6 SDK](https://dotnet.microsoft.com/download/dotnet/6.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

1.   Start Visual Studio 2022 and select **Create a new project**.

![Image 26: Create a new project from the start window](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/start-window-create-new-project.png?view=aspnetcore-10.0)

2.   In the **Create a new project** dialog, select **ASP.NET Core Web App**, and then select **Next**.

![Image 27: Create an ASP.NET Core Web App](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/np.png?view=aspnetcore-10.0)

3.   In the **Configure your new project** dialog, enter `RazorPagesMovie` for **Project name**. It's important to name the project _RazorPagesMovie_, including matching the capitalization, so the namespaces will match when you copy and paste example code.

![Image 28: Configure your new project](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/config.png?view=aspnetcore-10.0)

4.   Select **Next**.

5.   In the **Additional information** dialog, select **.NET 6.0 (Long-term support)** and then select **Create**.

![Image 29: Additional information](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/additional-info.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 30: Solution Explorer](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/6/se.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

Select **RazorPagesMovie** in **Solution Explorer**, and then press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 31: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcertvs22.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 32: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

*   Runs the app, which launches the [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).
*   Launches the default browser at `https://localhost:5001`, which displays the apps UI.

The following sections contain an overview of the main project folders and files that you'll work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. This file sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the following code:

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

The following lines of code in this file create a `WebApplicationBuilder` with preconfigured defaults, add Razor Pages support to the [Dependency Injection (DI) container](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0), and build the app:

```
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();
```

The developer exception page is enabled by default and provides helpful information on exceptions. Production apps should not be run in development mode because the developer exception page can leak sensitive information.

The following code sets the exception endpoint to `/Error` and enables [HTTP Strict Transport Security Protocol (HSTS)](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) when the app is _**not**_ running in development mode:

```
// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
```

For example, the preceding code runs when the app is in production or test mode. For more information, see [Use multiple environments in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0).

The following code enables various [Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0):

*   `app.UseHttpsRedirection();` : Redirects HTTP requests to HTTPS.
*   `app.UseStaticFiles();` : Enables static files, such as HTML, CSS, images, and JavaScript to be served. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).
*   `app.UseRouting();` : Adds route matching to the middleware pipeline. For more information, see [Routing in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0)
*   `app.MapRazorPages();`: Configures endpoint routing for Razor Pages.
*   `app.UseAuthorization();` : Authorizes a user to access secure resources. This app doesn't use authorization, therefore this line could be removed.
*   `app.Run();` : Runs the app.

If you run into a problem you can't resolve, compare your code to the completed project. [View or download completed project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie60) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

This is the first tutorial of a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0).

If you're new to ASP.NET Core development and are unsure of which ASP.NET Core web UI solution will best fit your needs, see [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0).

At the end of the series, you'll have an app that manages a database of movies.

In this tutorial, you:

*   Create a Razor Pages web app.
*   Run the app.
*   Examine the project files.

At the end of this tutorial, you'll have a working Razor Pages web app that you'll enhance in later tutorials.

![Image 33: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/5/home5.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.8 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET 5 SDK](https://dotnet.microsoft.com/download/dotnet/5.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

1.   Start Visual Studio and select **Create a new project**. For more information, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

![Image 34: Create a new project from the start window](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/5/start-window-create-new-project.png?view=aspnetcore-10.0)

2.   In the **Create a new project** dialog, select **ASP.NET Core Web Application**, and then select **Next**.

![Image 35: Create an ASP.NET Core Web Application](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/5/np.png?view=aspnetcore-10.0)

3.   In the **Configure your new project** dialog, enter `RazorPagesMovie` for **Project name**. It's important to name the project _RazorPagesMovie_, including matching the capitalization, so the namespaces will match when you copy and paste example code.

4.   Select **Create**.

![Image 36: Name the project](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/config.png?view=aspnetcore-10.0)

5.   In the **Create a new ASP.NET Core web application** dialog, select:

    1.   **.NET Core** and **ASP.NET Core 5.0** in the dropdowns.
    2.   **Web Application**.
    3.   **Create**.

![Image 37: Select ASP.NET Core Web App](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/5/npx.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 38: Solution Explorer](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/se2.2.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 39: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 40: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio starts [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) and runs the app. The address bar shows `localhost:port#` and not something like `example.com`. That's because `localhost` is the standard hostname for the local computer. Localhost only serves web requests from the local computer. When Visual Studio creates a web project, a random port is used for the web server.

Here's an overview of the main project folders and files that you'll work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. This file sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static assets, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the entry point for the app. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).

Contains code that configures app behavior. For more information, see [App startup in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).

If you run into a problem you can't resolve, compare your code to the completed project. [View or download completed project](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie50) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

This is the first tutorial of a series that teaches the basics of building an ASP.NET Core Razor Pages web app.

For a more advanced introduction aimed at developers who are familiar with controllers and views, see [Introduction to Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-10.0).

At the end of the series, you'll have an app that manages a database of movies.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/razor-pages/razor-pages-start/sample/RazorPagesMovie30) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

In this tutorial, you:

*   Create a Razor Pages web app.
*   Run the app.
*   Examine the project files.

At the end of this tutorial, you'll have a working Razor Pages web app that you'll build on in later tutorials.

![Image 41: The Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/home2.2.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.4 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET Core 3.1 SDK](https://dotnet.microsoft.com/download/dotnet-core/3.1)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   From the Visual Studio **File** menu, select **New**>**Project**.

*   Create a new ASP.NET Core Web Application and select **Next**. ![Image 42: Create the new project from the start window](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/np_2.1.png?view=aspnetcore-10.0)

*   Name the project **RazorPagesMovie**. It's important to name the project _RazorPagesMovie_ so the namespaces will match when you copy and paste code. ![Image 43: Name the project](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/config.png?view=aspnetcore-10.0)

*   Select **ASP.NET Core 3.1** in the dropdown, **Web Application**, and then select **Create**.

![Image 44: Select ASP.NET Core Web Application](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/3/npx.png?view=aspnetcore-10.0)

The following starter project is created:

![Image 45: Solution Explorer](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start/_static/se2.2.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   Press Ctrl+F5 to run without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 46: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 47: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio starts [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) and runs the app. The address bar shows `localhost:port#` and not something like `example.com`. That's because `localhost` is the standard hostname for the local computer. Localhost only serves web requests from the local computer. When Visual Studio creates a web project, a random port is used for the web server.

Here's an overview of the main project folders and files that you'll work with in later tutorials.

Contains Razor pages and supporting files. Each Razor page is a pair of files:

*   A `.cshtml` file that has HTML markup with C# code using Razor syntax.
*   A `.cshtml.cs` file that has C# code that handles page events.

Supporting files have names that begin with an underscore. For example, the `_Layout.cshtml` file configures UI elements common to all pages. This file sets up the navigation menu at the top of the page and the copyright notice at the bottom of the page. For more information, see [Layout in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/layout?view=aspnetcore-10.0).

Contains static files, like HTML files, JavaScript files, and CSS files. For more information, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

Contains configuration data, like connection strings. For more information, see [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0).

Contains the entry point for the program. For more information, see [.NET Generic Host in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0).

Contains code that configures app behavior. For more information, see [App startup in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0).
