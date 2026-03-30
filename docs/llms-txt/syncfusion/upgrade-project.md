# Source: https://docs.syncfusion.com/extension/blazor-extension/visual-studio-code/upgrade-project.md

# Source: https://docs.syncfusion.com/extension/blazor-extension/visual-studio/upgrade-project.md

# Upgrading SyncfusionÂ® Blazor application to latest version

The SyncfusionÂ® Blazor migration add-in for Visual Studio allows you to migrate an existing SyncfusionÂ® Blazor application from one version of Essential StudioÂ® to another. This reduces the amount of manual work required during the migration process.

The steps below will assist you to upgrade the SyncfusionÂ® version in the SyncfusionÂ® Blazor application via Visual Studio 2022 or 2026:

N> Before use the SyncfusionÂ® Blazor Project Migration, check whether the SyncfusionÂ® Blazor Template Studio Extension installed or not in Visual Studio Extension Manager by clicking on the Extensions -> Manage Extensions -> Installed. If this extension not installed, install the extension by follow the steps from the [download and installation](download-and-installation) help topic. 

1. Open the SyncfusionÂ® Blazor application that uses the SyncfusionÂ® component in the Visual Studio 2022 or 2026.

2. To open the Migration Wizard, either one of the following options should be followed:

    **Option 1**

    Choose **Extensions -> SyncfusionÂ® -> Essential StudioÂ® for Blazor -> Migrate Projectâ¦** from Visual Studio menu.

    ![MigrationMenu](images/MigrationMenu.PNG)

    **Option 2**

    Right-click the application from the **Solution Explorer** and select the **SyncfusionÂ® Blazor** and choose the **Migrate SyncfusionÂ® Blazor project from another version...**

    ![MigrationAddin](images/MigrationAddin.png)

3. The SyncfusionÂ® Project Migration window will appear. You can choose the required version of SyncfusionÂ® Blazor to migrate.

    N> The versions are loaded from the SyncfusionÂ® Blazor NuGet packages published in [`NuGet.org`](https://www.nuget.org/packages?q=Tags%3A%22blazor%22syncfusion) and it requires internet connectivity.

    ![MigrationWizard](images/Migration.png)

4. Check the **âEnable a backup before migratingâ** checkbox if you want to take the project backup and choose the location.

5. Once the migration process is completed, you will get a successful message window

    ![MigrationSuccessMessage](images/MigrationSuccess.png)

    If you enabled project backup before migrating, the old application was saved in the specified backup path location, as shown below once the migration process completed.

    ![MigrationBackupLocation](images/Backuplocation.png)

6. The SyncfusionÂ® Blazor NuGet packages are updated to the respective selected version in the SyncfusionÂ® Blazor application.

7. If you installed the trial setup or NuGet packages from nuget.org you must register the SyncfusionÂ® license key to your application since SyncfusionÂ® introduced the licensing system from 2018 Volume 2 (v16.2.0.41) Essential StudioÂ® release. Navigate to the [help topic](https://help.syncfusion.com/common/essential-studio/licensing/overview#how-to-generate-syncfusion-license-key) to generate and register the SyncfusionÂ® license key to your application. Refer to this [blog](https://www.syncfusion.com/blogs/post/whats-new-in-2018-volume-2.aspx) post for understanding the licensing changes introduced in Essential StudioÂ®.