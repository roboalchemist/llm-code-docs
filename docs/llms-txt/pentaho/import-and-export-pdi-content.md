# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-repository/import-and-export-pdi-content.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-repository/import-and-export-pdi-content.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-repository/import-and-export-pdi-content.md

# Import and export PDI content

You can import and export PDI content from and to a repository by using PDI's built-in functions, explained in these subsections.

Among other purposes, these procedures are useful for backing up and restoring content in the solution repository. However, users, roles, permissions, and schedules are not included in import/export operations. If you want to back up these items, you should follow the procedure in [Backup and restore Pentaho repositories](https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-repository/backup-and-restore-pentaho-repositories) instead.

**Note:** If you are on Pentaho version 8.0 or earlier, as a best practice to avoid errors when exporting and importing repository contents, select specific content and not the entire repository. For more information, see [Importing and exporting PDI content with Pentaho 8.0 and earlier](https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-repository-issues/importing-and-exporting-8.0-and-earlier).

## Import content into a repository

Follow the instructions below to import the repository. You must already be logged into the repository in the PDI client before you perform this task.

1. In the PDI client, go to **Tools** > **Repository** > **Import Repository**.
2. Locate the export (XML) file that contains the solution repository contents.
3. Click **Open**.

   The **Directory Selection** dialog box appears.
4. Select the directory in which you want to import the repository.
5. Click **OK**.
6. Enter a comment, if applicable.
7. Wait for the import process to complete.
8. Click **Close**.

The full contents of the repository are now in the directory you specified.

### Import content from the command line

The import script is a command-line utility that pulls content into an enterprise or database repository from an individual `.kjb` or `.ktr` file, or from complete repository export XML files.

You must also declare a rules file that defines certain parameters for the data integration content you are importing. We provide a sample file called `import-rules.xml`, which is included with the standard Data Integration client tool distribution. It contains all the potential rules, along with comments that describe what each rule does. You can either modify the `import-rules.xml` file or copy its contents to another file, and then declare the rules file as a command-line parameter.

The table below defines command-line options for the import script, which are declared using the syntax specific to the operating system type:

* **Linux**

  Options are declared using a dash (-) followed by the option name, then an equals sign (=) and the value, where applicable. For example: `-option=value`
* **Windows**

  Options are declared using a forward slash (/) followed by the option name, then a colon (:) and the value, where applicable. For example: `/option:value`

**Note:** For options requiring no value entry (replace, coe, and version), a dash or slash (depending on your OS) followed by the option is the equivalent of selecting ‘Yes’; otherwise, the option is ignored.

| Options  | Definition / Value                                                                                                          |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |
| rep      | The name of the enterprise or database repository to import into.                                                           |
| user     | The repository username you will use for authentication.                                                                    |
| pass     | The password for the username you specified with **user**.                                                                  |
| dir      | The directory in the repository that you want to copy the content to.                                                       |
| limitdir | Optional. A list of comma-separated source directories to include (excluding those directories not explicitly declared).    |
| file     | The path to the repository export file that you will import from.                                                           |
| rules    | The path to the rules file, as explained above.                                                                             |
| comment  | The comment that will be set for the new revisions of the imported transformations and jobs.                                |
| replace  | Replace existing transformations and jobs in the repository. (The default is: No)                                           |
| coe      | Continue on error, ignoring all validation errors. (The default is: No)                                                     |
| version  | Show the version, revision, and build date of the PDI instance that the import script interfaces with. (The default is: No) |

* **Linux**

  `Import.sh -rep= Archive71 -user=admin -pass=password -coe -replace -dir=/home/admin -file= /Downloads/imagitasDemoEnclosure.ktr -rules=/Downloads/import-rules.xml -comment="New version upload from UAT"`
* **Windows**

  `Import.bat /rep:Archive71 /user:admin /pass:password /coe /replace /dir:\home\admin /file:C:\Downloads\imagitasDemoEnclosure.ktr /rules:C:\Downloads\import-rules.xml /comment:"New version upload from UAT"`

## Export content from the repository

Follow the instructions below to export the repository. You must already be logged into the repository through the PDI client to complete this task.

1. In the PDI client, go to **Tools** > **Repository** > **Export Repository**.
2. In the **Save As** dialog box, browse to the location where you want to save the export file.
3. Type a name for your export file in the **File Name** text box.
4. Click **Save**.

The export file is created in the location you specified. This XML file is a concatenation of all of the data integration content you selected. It is possible to break it up into individual KTR and KJB files by hand or through a transformation.

### Export content from the command line

To export repository objects into XML format, using command-line tools instead of exporting repository configurations from within Spoon, use named parameters and command-line options when calling Kitchen or Pan from a command-line prompt.

The following is an example command-line entry to execute an export job using Kitchen:

```
call kitchen.bat /file:C:\Pentaho_samples\repository\repository_export.kjb
"/param:rep_name=PDI2000" "/param:rep_user=admin" "/param:rep_password=password"
"/param:rep_folder=/public/dev"
"/param:target_filename=C:\Pentaho_samples\repository\export\dev.xml"
```

| Parameter            | Description         |
| -------------------- | ------------------- |
| **rep\_folder**      | Repository Folder   |
| **rep\_name**        | Repository Name     |
| **rep\_password**    | Repository Password |
| **rep\_user**        | Repository Username |
| **target\_filename** | Target Filename     |

It is also possible to use obfuscated passwords with Encr, the command line tool for encrypting strings for storage/use by PDI. The following is an example command-line entry to execute a complete command-line call for the export in addition to checking for errors:

```
@echo off
ECHO This an example of a batch file calling the repository_export.kjb
   
cd C:\Pentaho\pdi-ee-<filepath>--check--</filepath>10.2.0>\data-integration
   
call kitchen.bat /file:C:\Pentaho_samples\repository\repository_export.kjb "/param:rep_name=PDI2000"
"/param:rep_user=admin" "/param:rep_password=password" "/param:rep_folder=/public/dev"
"/param:target_filename=C:\Pentaho_samples\repository\export\dev.xml"
   
if errorlevel 1 goto error
echo Export finished successful.
goto finished
   
:error
echo ERROR: An error occurred during repository export.
:finished
REM Allow the user to read the message when testing, so having a pause
pause
```
