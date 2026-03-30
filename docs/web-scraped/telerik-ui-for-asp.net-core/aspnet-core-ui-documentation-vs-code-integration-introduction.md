# Source: https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction

Title: ASP.NET Core Overview - Telerik UI for ASP.NET Core

URL Source: https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction

Markdown Content:
New to Telerik UI for ASP.NET Core?[Start a free 30-day trial](https://www.telerik.com/try/aspnet-core-ui)

[Telerik UI for ASP.NET Core Visual Studio Code Integration Overview](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#telerik-ui-for-aspnet-core-visual-studio-code-integration-overview)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 10, 2025

The **Telerik UI for ASP.NET Core Productivity Tools** is an extension for [Visual Studio Code](https://code.visualstudio.com/) that enhances the application development experience with Telerik UI for ASP.NET Core.

As its primary advantage, the VS Code extension facilitates the creation of projects through a wizard directly in Visual Studio Code.

[Get Telerik UI for ASP.NET Core Productivity Tools](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#get-telerik-ui-for-aspnet-core-productivity-tools)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can get the extension:

* from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TelerikInc.aspnetcoretemplatewizard)

* by opening the **Extensions** tab in Visual Studio Code, then searching for **Telerik UI for ASP.NET Core Productivity Tools** and clicking **Install**

[Create a Telerik Project](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#create-a-telerik-project)
------------------------------------------------------------------------------------------------------------------------------------------

To create a Telerik-enabled ASP.NET Core project:

1. Press `Ctrl`+`Shift`+`P` in Windows/Linux or `Cmd`+`Shift`+`P` on Mac to open the VSCode extension launcher.

2. Type/Select `Telerik UI for ASP.NET Core Template Wizard: Launch` and press `Enter` to launch the extension.

3. Enter a project name and select the location.

4. Choose whether to start from a [**Blank Project** or use one of the available Telerik project templates](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#project-templates) as a base:

![Image 1: UI for ASP.NET Core choose Telerik template, project name and location](https://www.telerik.com/aspnet-core-ui/documentation/assets/0c0fee0c09c50abaaa224276eb17daba/project-name-and-location.png)

[Install or Update License Key](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#install-or-update-license-key)
----------------------------------------------------------------------------------------------------------------------------------------------------

If necessary, the Telerik Visual Studio Code extension will notify you about a missing or outdated [license key](https://www.telerik.com/aspnet-core-ui/documentation/installation/activating-your-license/setting-up-your-license), and will install or update it.

[Configure the Project](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#configure-the-project)
------------------------------------------------------------------------------------------------------------------------------------

With the template wizard, you can configure the following project options:

* Project template
* License type
* Target framework
* Tag or HTML Helpers
* Localization
* Visual theme

### [Project Templates](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#project-templates)

The following project templates are available:

| Project | Description |
| --- | --- |
| **Blank Project** | The Blank template has the package references and the client-side resources loaded in the `_Layout.cshtml` file. It also features the expected [JSON serialization configuration](https://docs.telerik.com/aspnet-core/installation/json-serialization) in the `Program.cs` file. The default editor templates are included in the `~Views\Shared\EditorTemplates` folder. |
| **Standard** | The Standard template features: *Everything from the **Blank Project**.**** ***** A Responsive Panel and Menu in `_Layout.cshtml`.* A PanelBar in `Index.cshtml`. *A TabStrip in `Contact.cshtml`.* An HTML styled with [Cards](https://docs.telerik.com/aspnet-core/knowledge-base/cards) in `About.cshtml`.**** |
| **The Content Security Policy (CSP)** | Content Security Policy (CSP) template features: *A Menu in `_Layout.cshtml`.* A Detail Grid with a TabStrip in `Index.cshtml`. *A Child Grid in `_Child_Grid.cshtml`.* A [DeferredToScriptFiles](https://docs.telerik.com/aspnet-core/html-helpers/helper-basics/deferred-initialization#deferring-components-globally) setting in `Program.cs`. * A `KendoDeferredScripts` Middleware in `Program.cs`. |
| **Grid and Menu** | The Grid and Menu template features: *Everything from the **Blank Project**.* Buttons and Grid in `Index.cshtml`. * A Responsive Panel and Menu in `_Layout.cshtml`. |
| **Grid Razor Pages** | The Grid Razor Pages template includes everything from the **Blank Project**. It features an editable Grid in the `Index.cshtml` that uses handlers for the CRUD data operations. The `AntiForgeryToken` is set up, as well. |
| **Dashboard** | The Dashboard template features: *Everything from the **Blank Project** except the editor templates folder.* A TileLayout with Charts and Grids in the `Index.cshtml`, as well as shared DataSource and dynamically populated templates. |
| **Admin** | The Admin is a Razor Pages template configured with [TagHelpers](https://docs.telerik.com/aspnet-core/tag-helpers/overview). It features: *Everything from the **Blank Project**.* Authentication functionallity (Registration, Login, and Logout) in `Areas/Login/Pages`. *A navigation that is created by using the [Drawer](https://docs.telerik.com/aspnet-core/tag-helpers/navigation/drawer/overview) and [AppBar](https://docs.telerik.com/aspnet-core/tag-helpers/navigation/appbar/overview) components.* A [TileLayout](https://docs.telerik.com/aspnet-core/tag-helpers/layout/tilelayout/overview) with [Cards](https://docs.telerik.com/aspnet-core/styles-and-layout/cards), [Arc Gauge](https://docs.telerik.com/aspnet-core/tag-helpers/gauges/arcgauge/overview), [Chart](https://docs.telerik.com/aspnet-core/tag-helpers/charts/overview) and [Grid](https://docs.telerik.com/aspnet-core/tag-helpers/data-management/grid/overview) in `Index.cshtml`. *A [TileLayout](https://docs.telerik.com/aspnet-core/tag-helpers/layout/tilelayout/overview) with a variety of [Charts](https://docs.telerik.com/aspnet-core/tag-helpers/charts/overview) and [Gauges](https://docs.telerik.com/aspnet-core/tag-helpers/gauges/radialgauge/overview) in `Performance.cshtml`.* A [TileLayout](https://docs.telerik.com/aspnet-core/tag-helpers/layout/tilelayout/overview) with [Bubble Chart](https://docs.telerik.com/aspnet-core/tag-helpers/charts/overview) and [ListView](https://docs.telerik.com/aspnet-core/html-helpers/data-management/listview/overview) with editable [Cards](https://docs.telerik.com/aspnet-core/styles-and-layout/cards) in `Products.cshtml` as well as [Pager](https://docs.telerik.com/aspnet-core/tag-helpers/data-management/pager/overview) and search panel. * A [TileLayout](https://docs.telerik.com/aspnet-core/tag-helpers/layout/tilelayout/overview) with [Form](https://docs.telerik.com/aspnet-core/tag-helpers/layout/form/overview) and [Calendar](https://docs.telerik.com/aspnet-core/tag-helpers/scheduling/calendar/overview) in `Settings.cshtml`. |

### [License Type](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#license-type)

Select the type of your Telerik license (trial or commercial).

![Image 2: UI for ASP.NET Core choose Telerik license](https://www.telerik.com/aspnet-core-ui/documentation/assets/dbaf081c019c30c3fa0e01b1a59a0875/license-type.png)

### [Target Framework](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#target-framework)

Choose the desired target framework version.

![Image 3: UI for ASP.NET Core choose target framework](https://www.telerik.com/aspnet-core-ui/documentation/assets/096162187115ffaf1ffe2d49dc5abf9d/target-framewok.png)

### [Helper Selection](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#helper-selection)

You can choose if you want the template project to use [HtmlHelpers or TagHelpers](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/helper-basics/overview) version of the components.

![Image 4: UI for ASP.NET Core HTML/Tag helper options](https://www.telerik.com/aspnet-core-ui/documentation/assets/e61c7fc6d230aa4cd9d453043a731c48/helper-type.png)

### [Localization](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#localization)

If you enable the localization option, the language specific files will be copied to `~/wwwroot/lib/kendo-ui/js/messages/` folder. For more information, refer to the [localization documentation](https://www.telerik.com/aspnet-core-ui/documentation/globalization/localization).

![Image 5: UI for ASP.NET Core enable project localization](https://www.telerik.com/aspnet-core-ui/documentation/assets/6cbdc80c3ef32e0731e923b7739d1204/enable-localization.png)

### [Themes](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#themes)

You can add styling to your application by selecting one of the [Kendo UI Sass-Based themes](https://www.telerik.com/aspnet-core-ui/documentation/styles-and-layout/sass-themes/overview) (Default, Bootstrap, Material, Fluent, or Classic) and pick from a variety of [swatches](https://www.telerik.com/aspnet-core-ui/documentation/styles-and-layout/sass-themes/overview#swatch) that come with each theme. When you make your choice, the wizard will add to the `_Layout.cshtml` only these files that are required by the selected theme.

![Image 6: UI for ASP.NET Core Theme options](https://www.telerik.com/aspnet-core-ui/documentation/assets/42c7154d002986ddf272e1bb0dbda56c/themes.png)

[Run the Project](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#run-the-project)
------------------------------------------------------------------------------------------------------------------------

After configuring the settings of the project, click **Create Project** to start creating the new UI for ASP.NET Core application.

To run the project:

1. Open the terminal and navigate to the project folder.
2. Execute `dotnet run` and open the link in the console output in your browser.

Alternatively, open the solution file with Visual Studio and build the application. Once the NuGet packages get restored and the build passes, you will have your Telerik UI for ASP.NET Core project up and running.

[See Also](https://www.telerik.com/aspnet-core-ui/documentation/vs-code-integration/introduction#see-also)
----------------------------------------------------------------------------------------------------------

* [Troubleshooting the Telerik UI for ASP.NET Core Productivity Tools Extension](https://www.telerik.com/aspnet-core-ui/documentation/knowledge-base/vs-code-extension-issues)
