# Source: https://docs.syncfusion.com/extension/wpf-extension/add-references.md

# Source: https://docs.syncfusion.com/extension/windowsforms-extension/add-references.md

# Source: https://docs.syncfusion.com/extension/docxeditor-sdk-extension/visual-studio/add-references.md

# Source: https://docs.syncfusion.com/extension/spreadsheeteditor-sdk-extension/visual-studio/add-references.md

# Source: https://docs.syncfusion.com/extension/pdfviewer-sdk-extension/visual-studio/add-references.md

# Source: https://docs.syncfusion.com/windowsforms/visual-studio-integration/add-references.md

# Source: https://docs.syncfusion.com/wpf/visual-studio-integration/add-references.md

# Add Reference for WPF

Syncfusion Reference Manager is the Visual Studio add-in for the WPF platform. It adds the SyncfusionÂ® assembly reference to the project, either from the GAC location, from the Essential StudioÂ® installed location, or from NuGet packages. It can also migrate the projects that contain the old versions of the SyncfusionÂ® assembly reference to newer or specific versions of the SyncfusionÂ® assembly reference. It supports Microsoft Visual Studio 2015 or higher. This Visual Studio extension is included in the Essential StudioÂ® 2013 Volume 3 release.

N> This Reference Manager can be applied to a project for SyncfusionÂ® assembly versions 10.4.0.71 and later.

To add the SyncfusionÂ® assembly references in Visual Studio, follow the steps below:

> Check whether the **WPF Extensions - Syncfusion** are installed or not in Visual Studio Extension Manager by going to **Extensions -> Manage Extensions -> Installed** for Visual Studio 2019 or later and for Visual Studio 2017 or lower by going to **Tools -> Extensions and Updates -> Installed**. If this extension not installed, please install the extension by follow the steps from the [download and installation](download-and-installation) help topic.

1. Open a new or existing **WPF** application.

2. To open Syncfusion Reference Manager Wizard, follow either one of the options below:

   **Option 1:**  
   Click **Extensions->Syncfusion Menu** and choose **Essential StudioÂ® for WPF > Add Referencesâ¦** in **Visual Studio**.

    ![Syncfusion Reference Manager via Syncfusion Menu](Syncfusion-Reference-Manger_images/Syncfusion_Menu_AddReference_2019.png)

   N> In Visual Studio 2017 or lower, click Syncfusion Menu and choose Essential StudioÂ® for WPF>Add Referencesâ¦.

   ![Syncfusion Reference Manager via Syncfusion Menu](Syncfusion-Reference-Manger_images/Syncfusion_Menu_AddReference.png)

   **Option 2:**  

   Right-click the selected project file from Solution Explorer, then select **Syncfusion Reference Managerâ¦** from **Context Menu**. The following screenshot shows this option in Visual Studio.   

   ![Syncfusion Reference Manager add-in](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img1.png)

3. The Syncfusion Reference Manager Wizard displays a list of loaded SyncfusionÂ® WPF controls.

   ![Syncfusion Reference Manger Wizard](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img2.png)

   **Platform Selection:** Platform selection option will appear as an option in Syncfusion Reference Manager if opened from a Console/Class Library project. Select the appropriate platform. 

   ![Platform selection option in Syncfusion Reference Manger](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img3.png)

   N> The platform selection option will appear only if Essential StudioÂ® for Enterprise Edition with the platforms WPF and Windows Forms has been installed, or if both Essential StudioÂ® for WPF and WinForms have been installed.

   **Assembly From:** Choose the assembly location, from where the assembly is added to the project.

   ![Assembly location option in Syncfusion Reference Manger](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img4.png)


   N>Â The GAC option will not be available when you select a WPF (.NET Core 3.1, .NET 5.0, .NET 6.0, .NET 7.0, and .NET 8.0) application in Visual Studio 2019 or Visual Studio 2022. 

   **Version:** To add the corresponding version assemblies to the project, select the build version.

   ![Assembly location option in Syncfusion Reference Manger](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger1-img4.png)

   N> WPF (.NET Core 3.1 and .NET 5.0) applications in Visual Studio 2019 are supported from version 18.2.0.44, .NET 6.0 applications in Visual Studio 2022 are supported from 19.4.0.38, .NET 7.0 applications in Visual Studio 2022 are supported from 20.4.0.38, and .NET 8.0 applications in Visual Studio 2022 are supported from 23.2.4. The version combo box is not visible for the NuGet option. 

   **Themes Option:** Choose the necessary themes based on your requirements. To learn more about built-in themes and their available assembly, click the link below.

   [https://help.syncfusion.com/wpf/themes/](https://help.syncfusion.com/wpf/themes/)

   ![Themes selection option in Syncfusion Reference Manger](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img5.png)

   N> Themes option will be enabled only if we selected theme supported controls.

   ![Themes selection option notification in Syncfusion Reference Manger](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img6.png)


4. Select the required controls you want to add to your project. Then click **Done** to add the project's required assemblies for the specified controls. The list of required assemblies for the selected controls to be added is shown in the screenshot below.

   ![Syncfusion Reference Manager new assemblies add information dialog](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img7.png)

5. Click **OK**. The listed Syncfusion assemblies are added to project. Then it notifies âSyncfusion assemblies have been added successfullyâ in Visual Studio status bar.

   ![Syncfusion Reference Manager success status in Visual Studio status bar](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img8.png)

6. Then, SyncfusionÂ® licensing registration required message box will be shown if you installed the trial setup or NuGet packages since SyncfusionÂ® introduced the licensing system from 2018 Volume 2 (v16.2.0.41) Essential StudioÂ® release. Navigate to the [help topic](https://help.syncfusion.com/common/essential-studio/licensing/overview#how-to-generate-syncfusion-license-key), which is shown in the licensing message box to generate and register the SyncfusionÂ® license key to your project. Refer to this [blog](https://www.syncfusion.com/blogs/post/whats-new-in-2018-volume-2.aspx) post for understanding the licensing changes introduced in Essential StudioÂ®.

   ![Syncfusion license registration required information dialog in Syncfusion Reference Manager](Syncfusion-Reference-Manger_images/Syncfusion-Reference-Manger-img9.png)

N>  Reference Manager support is provided by SyncfusionÂ® for select versions of the .NET Framework that are included (as assemblies) in the SyncfusionÂ® Essential StudioÂ® installation. If you try to add Syncfusion assemblies to a project and the project framework isn't compatible with the specified SyncfusionÂ® version assemblies, a dialogue box shows with the message "**Current build v{version} isn't compatible with this framework v{Framework} Version**."






