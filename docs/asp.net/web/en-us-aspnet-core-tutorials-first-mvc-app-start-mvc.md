# Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0

Title: Get started with ASP.NET Core MVC

URL Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0

Markdown Content:
This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages, validates, and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [The latest version of Visual Studio](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

[![Image 1: VS26 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0)](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev-2026.png?view=aspnetcore-10.0#lightbox)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Model-View-Controller)**>**Next**.
*   In the **Configure your new project** dialog: 
    *   Enter `MvcMovie` for **Project name**. It's important to name the project _MvcMovie_. Capitalization needs to match each `namespace` when code is copied.
    *   The **Location** for the project can be set to anywhere.

*   Select **Next**.
*   In the **Additional information** dialog: 
    *   Select **.NET 10.0 (Standard Term Support)**.
    *   Verify that **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 2: Additional info dialog.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/media/net10-additional-info.png?view=aspnetcore-10.0)

For more information, including alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

Visual Studio uses the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

*   Press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 3: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 4: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio runs the app and opens the default browser.

The address bar shows `localhost:<port#>` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by pressing Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu:

![Image 5: Start Debug and Start Without Debugging menus.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/media/debug-menu.png?view=aspnetcore-10.0)

You can debug the app by selecting the **https** button in the toolbar:

![Image 6: MvcMovie debug button.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/media/debug-button.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 7: Home or Index page.](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/media/mvc-movie-home-page.png?view=aspnetcore-10.0)

*   Close the browser window. Visual Studio will stop the application.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next tutorial in this series, you learn about MVC and start writing some code.

This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages, validates, and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 8: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Model-View-Controller)**>**Next**.
*   In the **Configure your new project** dialog: 
    *   Enter `MvcMovie` for **Project name**. It's important to name the project _MvcMovie_. Capitalization needs to match each `namespace` when code is copied.
    *   The **Location** for the project can be set to anywhere.

*   Select **Next**.
*   In the **Additional information** dialog: 
    *   Select **.NET 9.0 (Standard Term Support)**.
    *   Verify that **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 9: Additional info dialog](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/9/additional-info-vs22-17.11.0.png?view=aspnetcore-10.0)

For more information, including alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

Visual Studio uses the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

*   Press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 10: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 11: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio runs the app and opens the default browser.

The address bar shows `localhost:<port#>` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by pressing Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu:

![Image 12: Start Debug and Start Without Debugging menus](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/9/debug-and-without-debug-menus-vs22-17.11.0.png?view=aspnetcore-10.0)

You can debug the app by selecting the **https** button in the toolbar:

![Image 13: MvcMovie debug button](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/9/debug-button-vs22-17.11.0.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 14: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/9/home90-vs.png?view=aspnetcore-10.0)

*   Close the browser window. Visual Studio will stop the application.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next tutorial in this series, you learn about MVC and start writing some code.

This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) with the **ASP.NET and web development** workload.

![Image 15: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Model-View-Controller)**>**Next**.
*   In the **Configure your new project** dialog: 
    *   Enter `MvcMovie` for **Project name**. It's important to name the project _MvcMovie_. Capitalization needs to match each `namespace` when code is copied.
    *   The **Location** for the project can be set to anywhere.

*   Select **Next**.
*   In the **Additional information** dialog: 
    *   Select **.NET 8.0 (Long Term Support)**.
    *   Verify that **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 16: Additional info dialog](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/8/additional-info-vs22-17.9.0.png?view=aspnetcore-10.0)

For more information, including alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

Visual Studio uses the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)

*   Press Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 17: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 18: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio runs the app and opens the default browser.

The address bar shows `localhost:<port#>` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by pressing Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu:

![Image 19: Start Debug and Start Without Debugging menus](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/8/debug-and-without-debug-menus-vs22-17.8.0.png?view=aspnetcore-10.0)

You can debug the app by selecting the **https** button in the toolbar:

![Image 20: MvcMovie debug button](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/8/debug-button-vs22-17.8.0.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 21: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/home80-vs.png?view=aspnetcore-10.0)

*   Close the browser window. Visual Studio will stop the application.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next tutorial in this series, you learn about MVC and start writing some code.

This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.

![Image 22: VS22 installer workloads](https://learn.microsoft.com/en-us/aspnet/core/tutorials/min-web-api/_static/asp-net-web-dev.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Model-View-Controller)**>**Next**.
*   In the **Configure your new project** dialog: 
    *   Enter `MvcMovie` for **Project name**. It's important to name the project _MvcMovie_. Capitalization needs to match each `namespace` when code is copied.
    *   The **Location** for the project can be set to anywhere.

*   Select **Next**.
*   In the **Additional information** dialog: 
    *   Select **.NET 7.0**.
    *   Verify that **Do not use top-level statements** is unchecked.

*   Select **Create**.

![Image 23: Additional info dialog](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/net7-additional-info.png?view=aspnetcore-10.0)

For more information, including alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

Visual Studio uses the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

Visual Studio runs the app and opens the default browser.

The address bar shows `localhost:<port#>` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by pressing Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu:

![Image 24: Debug menu](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/debug_menu50.png?view=aspnetcore-10.0)

You can debug the app by selecting the **https** button in the toolbar:

![Image 25: MvcMovie debug button](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/net7-debug-button.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 26: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/home50-vs.png?view=aspnetcore-10.0)

*   Close the browser window. Visual Studio will stop the application.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next tutorial in this series, you learn about MVC and start writing some code.

This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2022](https://visualstudio.microsoft.com/vs/#download) with the **ASP.NET and web development** workload.
*   [.NET 6 SDK](https://dotnet.microsoft.com/download/dotnet/6.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web App (Model-View-Controller)**>**Next**.
*   In the **Configure your new project** dialog, enter `MvcMovie` for **Project name**. It's important to name the project _MvcMovie_. Capitalization needs to match each `namespace` when code is copied.
*   Select **Next**.
*   In the **Additional information** dialog, select **.NET 6.0 (Long-term support)**.
*   Select **Create**.

![Image 27: Additional info dialog](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/net6-additional-info.png?view=aspnetcore-10.0)

For alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

Visual Studio uses the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Select Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 28: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 29: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio runs the app and opens the default browser.

The address bar shows `localhost:<port#>` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by selecting Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu:

![Image 30: Debug menu](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/debug_menu50.png?view=aspnetcore-10.0)

You can debug the app by selecting the **MvcMovie** button in the toolbar:

![Image 31: MvcMovie debug button](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/net6-debug-button.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 32: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/home50-vs.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next tutorial in this series, you learn about MVC and start writing some code.

This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.8 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET 5 SDK](https://dotnet.microsoft.com/download/dotnet/5.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   Start Visual Studio and select **Create a new project**.
*   In the **Create a new project** dialog, select **ASP.NET Core Web Application**>**Next**.
*   In the **Configure your new project** dialog, enter `MvcMovie` for **Project name**. It's important to name the project _MvcMovie_. Capitalization needs to match each `namespace` matches when code is copied.
*   Select **Create**.
*   In the **Create a new ASP.NET Core web application** dialog, select: 
    *   **.NET Core** and **ASP.NET Core 5.0** in the dropdowns.
    *   **ASP.NET Core Web App (Model-View-Controller)**.
    *   **Create**.

![Image 33: Create a new ASP.NET Core web application](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/mvcvs19v16.9.png?view=aspnetcore-10.0)

For alternative approaches to create the project, see [Create a new project in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/create-new-project).

Visual Studio used the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Select Ctrl+F5 to run the app without the debugger.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 34: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 35: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview).
    *   Runs the app.

The address bar shows `localhost:port#` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by selecting Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu item:

![Image 36: Debug menu](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/debug_menu50.png?view=aspnetcore-10.0)

You can debug the app by selecting the **IIS Express** button

![Image 37: IIS Express](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/iis_express50.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 38: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/home50-vs.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next part of this tutorial, you learn about MVC and start writing some code.

This tutorial teaches ASP.NET Core MVC web development with controllers and views. If you're new to ASP.NET Core web development, consider the [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0) version of this tutorial, which provides an easier starting point. See [Choose an ASP.NET Core UI](https://learn.microsoft.com/en-us/aspnet/core/tutorials/choose-web-ui?view=aspnetcore-10.0), which compares Razor Pages, MVC, and Blazor for UI development.

This is the first tutorial of a series that teaches ASP.NET Core MVC web development with controllers and views.

At the end of the series, you'll have an app that manages and displays movie data. You learn how to:

*   Create a web app.
*   Add and scaffold a model.
*   Work with a database.
*   Add search and validation.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mvc-app/start-mvc/sample) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample)).

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Visual Studio 2019 16.4 or later](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=learn.microsoft.com&utm_campaign=inline+link&utm_content=download+vs2019) with the **ASP.NET and web development** workload
*   [.NET Core 3.1 SDK](https://dotnet.microsoft.com/download/dotnet-core/3.1)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_2_visual-studio-mac)

*   From the Visual Studio, select **Create a new project**.

*   Select **ASP.NET Core Web Application**>**Next**.

![Image 39: Create a new ASP.NET Core Web Application project](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/np_2.1.png?view=aspnetcore-10.0)

*   Name the project **MvcMovie** and select **Create**. It's important to name the project **MvcMovie** so when you copy code, the namespace will match.

![Image 40: Configure your new project](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/config.png?view=aspnetcore-10.0)

*   Select **Web Application(Model-View-Controller)**. From the dropdown boxes, select **.NET Core** and **ASP.NET Core 3.1**, then select **Create**.

![Image 41: New project dialog, .NET Core in left pane, ASP.NET Core web](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/new_project30.png?view=aspnetcore-10.0)

Visual Studio used the default project template for the created MVC project. The created project:

*   Is a working app.
*   Is a basic starter project.

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_3_visual-studio-mac)

*   Select Ctrl+F5 to run the app without debugging.

Visual Studio displays the following dialog when a project is not yet configured to use SSL:

![Image 42: This project is configured to use SSL. To avoid SSL warnings in the browser you can choose to trust the self-signed certificate that IIS Express has generated. Would you like to trust the IIS Express SSL certificate?](https://learn.microsoft.com/en-us/aspnet/core/static/trustcert.png?view=aspnetcore-10.0)

Select **Yes** if you trust the IIS Express SSL certificate.

The following dialog is displayed:

![Image 43: Security warning dialog](https://learn.microsoft.com/en-us/aspnet/core/static/cert.png?view=aspnetcore-10.0)

Select **Yes** if you agree to trust the development certificate.

For information on trusting the Firefox browser, see [Firefox SEC_ERROR_INADEQUATE_KEY_USAGE certificate error](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff).

Visual Studio:

    *   Starts [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview).
    *   Runs the app.

The address bar shows `localhost:port#` and not something like `example.com`. The standard hostname for your local computer is `localhost`. When Visual Studio creates a web project, a random port is used for the web server.

Launching the app without debugging by selecting Ctrl+F5 allows you to:

*   Make code changes.
*   Save the file.
*   Quickly refresh the browser and see the code changes.

You can launch the app in debug or non-debug mode from the **Debug** menu item:

![Image 44: Debug menu](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/debug_menu.png?view=aspnetcore-10.0)

You can debug the app by selecting the **IIS Express** button

![Image 45: IIS Express](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/iis_express.png?view=aspnetcore-10.0)

The following image shows the app:

![Image 46: Home or Index page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc/_static/home2.2.png?view=aspnetcore-10.0)

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [Visual Studio Code](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-code)
*   [Visual Studio for Mac](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0#tabpanel_1_visual-studio-mac)

*   [Learn to debug C# code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger)
*   [Introduction to the Visual Studio IDE](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-ide)

In the next part of this tutorial, you learn about MVC and start writing some code.
