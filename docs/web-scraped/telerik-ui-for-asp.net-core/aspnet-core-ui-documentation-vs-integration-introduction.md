# Source: https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction

Title: ASP.NET Core Overview - Telerik UI for ASP.NET Core

URL Source: https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction

Markdown Content:
[Telerik UI for ASP.NET Core Visual Studio Integration Overview](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#telerik-ui-for-aspnet-core-visual-studio-integration-overview)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 10, 2025

To integrate with Visual Studio, Telerik provides the Progress® Telerik® UI for ASP.NET Core Visual Studio (VS) Extensions. They enhance the experience in developing web applications with Telerik UI for ASP.NET Core.

The VS Extensions come with handy templates that ease the creation of new projects. They also help you add Telerik UI for ASP.NET Core to an existing project or upgrade the UI for ASP.NET Core version. The Telerik UI for ASP.NET Core VS extensions support VS 2022, 2019 and 2017, and are distributed through the [Telerik UI for ASP.NET Core installer](https://www.telerik.com/aspnet-core-ui/documentation/installation/installation-options/msi-install) and the [Visual Studio Marketplace](https://marketplace.visualstudio.com/).

![Image 1: ninja-icon](https://www.telerik.com/aspnet-core-ui/documentation/static/35a2c49c0e7b061f81d272dd33a23e0d/avatar-ninja.svg)New to Telerik UI for ASP.NET Core?[Telerik UI for ASP.NET Core](https://www.telerik.com/aspnet-core-ui) is a professional grade UI library with 110+ components for building modern and feature-rich applications. To try it out sign up for a free 30-day trial.[Start Free Trial](https://www.telerik.com/try/aspnet-core-ui)

The VS extensions provide wizards that allow you to automate the following procedures:

* [Project Creation wizard](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/new-project-wizard)—allows you to use pre-configured project templates that include the required package references and client-side resources. These templates enable the quick deployment of popular components like Grid and Menu or even entire Dashboard applications. With the Project Creation wizard you can:

  * Select between project templates for both helper flavors—HTML Helpers and Tag Helpers.

  * Select the ASP.NET Core version and target framework.

  * Select the Telerik UI for ASP.NET Core version that you want to use.

* [Project Conversion](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/convert-project-wizard)—automatically configures any existing ASP.NET Core application to use the Telerik UI components, and turns it into a complete Telerik application. The wizard lets you select between using CDN or local files for the client-side resources.

* [Project Configuration](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/configure-project-wizard)—allows you to change the visual theme and to configure the right-to-left support, localization, and CDN use in existing projects that are already configured to use the Telerik UI components.

* [Update notifications](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/latest-version-retrieval)—the VS Extensions notify you when a new version of Telerik UI for ASP.NET Core is available and allow you to upgrade your applications.

* The Project Creation and Conversion wizards let you select a visual theme so that only the necessary CSS files are included.

[Installing the Extensions](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-the-extensions)
---------------------------------------------------------------------------------------------------------------------------------------

There are three ways to install the VS Extensions:

* By using the [automated MSI installer](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-with-the-msi)
* By installing from the [Visual Studio Marketplace](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-from-visual-studio-marketplace)
* By installing [directly from Visual Studio](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-in-visual-studio)

### [Installing with the MSI](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-with-the-msi)

To install the Telerik UI for ASP.NET Core Visual Studio Extensions, run the [Telerik UI for ASP.NET Core installer](https://www.telerik.com/aspnet-core-ui/documentation/installation/installation-options/msi-install) and verify that the Visual Studio Extensions are selected for installation.

### [Installing from Visual Studio Marketplace](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-from-visual-studio-marketplace)

Go to the Visual Studio Marketplace and select the desired version:

* For [Visual Studio 2017 and 2019](https://marketplace.visualstudio.com/items?itemName=TelerikInc.TelerikASPNETCoreVSExtensions)
* For [Visual Studio 2022](https://marketplace.visualstudio.com/items?itemName=TelerikInc.ProgressTelerikASPNETCoreVSExtensions)

When the download is complete, navigate to the download folder and click on the downloaded `TelerikUI.ASP.NET.Core.VSPackage.vsix` file to install the extensions.

### [Installing in Visual Studio](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#installing-in-visual-studio)

1. Launch Visual Studio.
2. Select **Extensions** from the top menu. (In Visual Studio 2017, this menu is called **Tools**.)
3. Click **Manage Extensions** from the drop-down menu. (In Visual Studio 2017, this menu is called **Extensions and Updates**.)
4. Click **Online** to the left and select **Visual Studio Marketplace**.
5. In the **Search** text box, enter `Telerik ASP.NET Core VSExtensions`
6. Select the extension and click **Download**.
7. Visual Studio will apply the changes automatically once you close all Microsoft Visual Studio windows.

[Using the Telerik VS Extensions in VS 2019 and later](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#using-the-telerik-vs-extensions-in-vs-2019-and-later)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* To access the VS extensions from the VS Toolbar, go to **Extensions > Telerik > Telerik UI for ASP.NET Core**. Choose one of the two options - **Create New Project** or **Convert to Telerik Application**.

![Image 2: UI for ASP.NET Core Visual Studio 2019 Extensions menu](https://www.telerik.com/aspnet-core-ui/documentation/assets/891f929864bdd48399830cd6b7bf306f/create-project-core.png)

* To access the template projects, go to **File**>**New**>**Project** and search for `Telerik`.

![Image 3: UI for ASP.NET Core New project Template](https://www.telerik.com/aspnet-core-ui/documentation/assets/4a579631ebfd2ef1b88e1d2432521191/new-project-template-core.png)

[Using the Telerik VS Extensions in VS 2017](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#using-the-telerik-vs-extensions-in-vs-2017)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* To access the VS extensions from the VS, go to **Telerik > Telerik UI for ASP.NET Core**. Choose from one of the two options - **Create New Project** or **Convert to Telerik Application**.

![Image 4: UI for ASP.NET Core Visual Studio 2017 Extensions menu](https://www.telerik.com/aspnet-core-ui/documentation/assets/141218c2ebea3cede04ab70ea6d666fe/create-project-core-vs2017.png)

* To access the template projects, go to **File**>**New**>**Project** and click on **Installed**>**Telerik** or search for `Telerik` in the search textbox on the right.

![Image 5: UI for ASP.NET Core New project Template](https://www.telerik.com/aspnet-core-ui/documentation/assets/b83e240ffe970206c51b249596b98f11/new-project-template-core-vs2017.png)

You can find the Telerik UI for ASP.NET Core VS Extensions settings in the standard Visual Studio options dialog under the Telerik node.

![Image 6: UI for ASP.NET Core The Options dialog](https://www.telerik.com/aspnet-core-ui/documentation/assets/3f383349a4ec21e211da1d00ea69ffc9/asp_core_settings.png)

[See Also](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/introduction#see-also)
-----------------------------------------------------------------------------------------------------

* [Creating New Projects with Visual Studio](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/new-project-wizard)
* [Converting Existing Projects with Visual Studio](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/convert-project-wizard)
* [Downloading the Latest Telerik UI for ASP.NET Core Version](https://www.telerik.com/aspnet-core-ui/documentation/vs-integration/latest-version-retrieval)
