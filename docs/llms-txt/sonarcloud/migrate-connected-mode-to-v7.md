# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/migrate-connected-mode-to-v7.md

# Migrate connected mode to v7

SonarQube for Visual Studio 7.0+ no longer stores the connected mode settings files in a location that could be under source control, and no longer modifies C# and VB.NET project files to configure the analysis rules.

This makes binding a solution for the first time much simpler because no source-controlled files will be modified. However, any solutions that were bound using the old configuration model will need to have their configuration settings migrated to the new model.

#### Migration is required for connected mode <a href="#migration-is-required-for-connected-mode" id="migration-is-required-for-connected-mode"></a>

Any features that require a connection to the Sonar server will not be available until you have migrated to the new model, including the following:

* issues suppressed on the server will not be suppressed in the IDE
* changes to Quality Profiles will not be synchronized to the IDE
* taint issues reported on the server will not be shown in the IDE

Analyses will still be performed using the old-style analysis configuration that is part of the solution (but without suppressions).

### Automating the migration process <a href="#automating-the-migration-process" id="automating-the-migration-process"></a>

To help automate the migration process, SonarLint for Visual Studio 7.0 provides a migration wizard.

* If you did not customize your binding settings in earlier versions, the wizard should be able to complete the migration without error.
* If you did customize your binding settings, you might need to manually undo your changes.
* If you are upgrading from a legacy version of Sonarlint (version 3.10 or earlier), please skip directly to the **Migrating from a legacy version** header below for instructions.

It is recommended to first run the wizard; once completed, SonarLint will announce whether or not the migration was successful. Please check the instructions below about what to do with the wizard logs if there is an error.

### Using the migration wizard <a href="#using-the-migration-wizard" id="using-the-migration-wizard"></a>

When you open a solution that is bound using the old model, SonarQube for Visual Studio will display a notification in Visual Studio and offer an option to open a wizard to help with migration.

Before starting the wizard, it is ***highly recommended*** that you begin in a clean state. For example, you should have no unsaved files and no uncommitted changes to files under source control before starting the migration.

<div align="left"><figure><img src="https://1613591589-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5CSDwdOaYoOAGYNiRqgl%2Fuploads%2Fgit-blob-f5b0997cdd715071c2387f99cf2e0486117b66ee%2F9fc619721686f082dc464edc00a64af43352ce61.png?alt=media" alt="SonarQube for Visual Studio will provide you with a gold bar to explain that some features are not available."><figcaption></figcaption></figure></div>

Select **Migrate configuration** to start the connected mode migration wizard. The wizard will do the following:

* Delete the existing .sonarlint settings folder.
  * Note: this may cause source control changes.
* Write the settings files in the new location.

In addition, ***for C# and VB.NET projects only***, the migration wizard will attempt to do the following:

* Remove any entries that point to the SonarQube for Visual Studio-generated SonarLint.xml file.
* Remove any MSBuild properties that point to the SonarLint-generated ruleset.

SonarQube for Visual Studio will attempt to remove these settings from the project files themselves, and also from any .props or .targets files it finds.

SonarQube for Visual Studio will announce whether or not the migration was successful. If SonarLint cannot remove all of the settings automatically, it will do its best to identify any changes that must be made manually.

If your code is under source control, you can review the diff after the wizard has finished and see what was changed. Once complete, commiting the change to source control will complete the migration process.

#### If the wizard cannot make changes automatically <a href="#if-the-wizard-cannot-make-changes-automatically" id="if-the-wizard-cannot-make-changes-automatically"></a>

If the wizard cannot make changes automatically, use the logs to identify what was missed. Then, manually locate and remove the setting.

To manually remove the setting, you will need to:

1. delete the .sonarlint folder, and
2. remove the relevant settings from C# and VB.NET project files. See this page for more information about the settings that need to be removed.

Once complete, commit the change to source control to complete the process.

If you have problems with the migration, please open a thread in the [SonarQube for Visual Studio Community Forum](https://community.sonarsource.com/tags/c/sl/visual-studio/35/connected_mode) and tag it with the tags `connected_mode` and `migration`.

### Migrating from a legacy version <a href="#migrating-from-a-legacy-version" id="migrating-from-a-legacy-version"></a>

If you are upgrading from a legacy version of Sonarlint for Visual Studio (version 3.10 or earlier), the migration must be done manually. In addition to the deletion of all SonarLint-related folders, as described above in the **If the wizard cannot make changes automatically** article, you must delete the SonarQube folder from the project before binding again to SonarQube (Server, Cloud) or SonarQube Community Build.

### Notes for Tfvc users <a href="#notes-for-tfvc-users" id="notes-for-tfvc-users"></a>

If you are using Team Foundation Version Control **and** have C# or VB.NET projects in your solution, it’s possible that you will see some additional dialogs from Tfvc appearing when the migration finishes. If your solution does not contain C# or VB.NET projects or you are migrating to SonarQube for Visual Studio version 8.28 or newer, you will probably not see this warning and can disregard the rest of this section.

As described above, the settings files are no longer written to a source-controlled location. Instead, they are written under the per-user roaming folder (`%APPDATA%\SonarLint for Visual Studio`). However, the projects still need to reference the settings files that configure the Roslyn-based Sonar C# and VB.NET rules.

Tfvc will detect that these files are being referenced and may pop up one or more dialogs like the one below warning that files outside the workspace are being referenced and asking for confirmation that this is ok. Select **Add the item** to dismiss the dialog.

<div align="left"><figure><img src="https://1613591589-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5CSDwdOaYoOAGYNiRqgl%2Fuploads%2Fgit-blob-75fa3001137cf66df793d3efc0c86828f1b05726%2F07ee8c5b9dca9d5f1f4d8ef76d1c072214762086.png?alt=media" alt="To complete the migration for Tfvc users, SonarQube for Visual Studio needs to add the items that are outside of source control." width="503"><figcaption></figcaption></figure></div>

It is possible that multiple Visual Studio dialogs will appear, or that they will appear behind the migration wizard dialog. In that case, you might need to dismiss the wizard dialog before the Visual Studio dialogs can be closed. The wizard dialog can be closed by selecting Enter or Escape on your keyboard, or by using the mouse.

<div align="left"><figure><img src="https://1613591589-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5CSDwdOaYoOAGYNiRqgl%2Fuploads%2Fgit-blob-c40e9485939aedc481e8f0b4b0ede1a85d96ca7d%2Fb33a75cb8e29437848188bb6a13144f3d31a2f24.png?alt=media" alt="When you dismiss the Tfvs dialogs, they should no longer appear."><figcaption></figcaption></figure></div>

Once you have dismissed the Tfvc dialogs they should not appear again.
