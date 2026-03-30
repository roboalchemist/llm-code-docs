# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-repository/upload-and-download-from-the-pentaho-repository.md

# Upload and download from the Pentaho Repository

You can upload and download from the Pentaho Repository with the Pentaho User Console (PUC) or the command line interface. The ability to upload and download assumes that you have already created a data source, that data content exists to be pushed, and defines permissions for the repository.

For uploading, any starting location can be selected. Permission settings are inherited through the folder structure if the destination location has existing permission settings. It is advisable to keep existing security settings as defaults for the upload.

For downloading, you are able to select the destination location for the downloaded file or folder. The download process always creates a ZIP file that includes a manifest file along with the downloaded content. The manifest file contains the collection of permissions settings for the downloaded files and folders and is found in the root directory of the ZIP file.

| Supported File Types                                                                                                                                                                                                                              | Hidden File Types                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The following file types and artifacts are supported for uploading and downloading from the Pentaho Repository.                                                                                                                                   | The following file types are hidden by default in the Pentaho Repository.                                                                                                                                                                           |
| <ul><li>Reporting (<code>.prpt</code>, <code>.prpti</code>; <code>.xml</code>)</li><li>Analyzer (<code>.xanalyzer</code>)</li><li>Dashboards (<code>.xdash</code>)</li><li>Solution Files (<code>.xaction</code>; <code>.locale</code>)</li></ul> | <ul><li>Web (<code>.html</code>; <code>.htm</code>)</li><li>Reporting (<code>.xml</code>)</li><li>Solution Files (<code>.properties</code>)</li><li>Graphics (<code>.png</code>; <code>.jpg</code>, <code>.gif</code>; <code>.svg</code>)</li></ul> |

## Upload folders and files

The User Console can be used to upload files and folders to the Pentaho Repository. To upload files, a user must have a role with the Publish Content operation permission and Write permission for the target folder (**Browse Files** > **Properties** > **Share** > **Users and Roles** > **Permissions**), where permissions can be held through a user name or a role that the user holds (Power User for example). See the **Pentaho Business Analytics** document for details on publish and write permissions.

For **Retain permission on upload file**, the file permission contained in the uploaded ZIP (`exportManifest.xml`) will be the permission applied the repository. If the file doesn't have an entry in the `exportManifest.xml` for the permission, then it will use the default permission, which is inherit. This is equivalent to the command line switch: `--permission=true`

For **Set Owner based on uploaded file**, the owner found in the uploaded ZIP (`exportManifest.xml`) will be the owner of the file in the repository. If the file does not have an entry in the `exportManifest.xml` for the `Owner`, then it will set the `Owner` to the user who is uploading the zip. This equivalent to the command line switch: `--retainOwnership=true`

Complete the following steps to upload one or more files to the repository with the User Console.

1. From the User Console Home, click **Browse Files**.

   The Browse Files page appears.
2. From the **Browse** pane on the left, click to choose the destination folder for the upload.
3. With the destination folder highlighted, click **Upload** in the **Folder Actions** pane on the right.

   The Upload dialog box appears.
4. Browse to the files or zipped folders to be uploaded by clicking **Browse**.
5. Select one or more files or zipped folders to upload.
6. Click **OK** to begin upload using the default settings.
7. Choose preferences for the upload by clicking to expand the **Advanced Options** menu.
   1. Choose **Replace the Existing File** or **Do Not Upload** from the first menu.
   2. Choose **File Permissions** from the second menu.

      The choices are **Do Not Change Permissions** or **RetainPermissions on the Uploaded File**.
   3. If you selected **Retain Permissions on the Uploaded File**, choose **File Ownership** by selecting **Do Not Change Owner** or **Set Owner Based on Uploaded File** from the third menu.
   4. Choose **None**, **Short**, or **Verbose** from the **Logging** menu.
8. Click **OK**.

The upload runs and the files or folders are uploaded to the repository. If the upload fails, an error log window opens with specific information.

### Upload from the command line

1. Open the command line interface by clicking **Start** and typing `cmd`. Press Enter.
2. From the command line interface, go to the location where you have a local copy of the Pentaho Server installed, such as: `C:/dev/pentaho/pentaho-server`
3. Enter a space, then type the arguments for upload into the command line interface. A completed upload argument would look something like this:

   `import-export.bat --import --url=http://localhost:8080/pentaho --username=dvader --password=password --charset=UTF-8 --path=/public --file-path=C:/Users/dvader/Downloads/pentaho-solutions.zip --overwrite=true --permission=true --retainOwnership=true`
4. Press Enter after the arguments are typed.

The upload process runs and the results are displayed in the command interface. If an argument is required for successful upload and has not been provided, the missing requirement is displayed in the command interface. The [Command line arguments reference](#command-line-arguments-reference) has a list of available command line arguments for uploading.

## Download folders and files

Downloading folders and files can be done through the User Console or through the command line interface. The download process always creates a ZIP file that includes a manifest file along with the downloaded content. The manifest file is a collection of the permissions settings for the downloaded files and folders and is found in the root directory of the ZIP file.

### Download action permissions

Only the Administrator role has downloading permissions, by default. The roles that have download action permissions are defined in the in the `pentaho.xml` configuration file. To add downloading permissions for a user, add that user to a role that has download permissions as shown below:

**CAUTION:** Providing the download action permissions to non-admin users can expose sensitive data.

1. Stop the Pentaho Server.
2. Navigate to the `pentaho.xml` file, located at: `/server/pentaho-server/pentaho-solutions/system/pentaho.xml`
3. Open the file with any text editor and locate the `download-roles` node in the file.
4. Add additional roles as needed.

   To create a Power User, type:

   ```
   <download-roles>Administrator,Power User</download-roles>
   ```

   **Note:** Use a comma between roles; not spaces.
5. Save and close the `pentaho.xml` file.
6. Restart the Pentaho Server.
7. Restart the User Console. Log on as a user with that role.

   You will now see the **Download** option in the **File Actions** pane in the Browse Files perspective of the User Console.

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

### Download a folder

1. From the User Console Home, click **Browse Files**.

   The Browse Files page appears.
2. From the **Browse** pane on the left, browse to the location of the folder to be downloaded.
3. With the folder highlighted, click **Download** in the **Folder Actions** pane on the right.
4. Choose **Save File** in the window that appears, and click **OK**.

The folder is saved as a ZIP file with the manifest located in the top level of the file.

### Download a file

1. From the User Console Home, click **Browse Files**.

   The Browse Files page appears.
2. Browse to the location of the file by clicking through the folders in the **Browse** pane on the left.

   The **Files** pane in the center populates with a list of reports.
3. Click to select the file in the **Files** pane and choose **Download** in the **Folder Actions** pane on the right.
4. Choose **Save File** in the window that appears, and click **OK**.

The file is saved as a ZIP file with the manifest located in the top level of the file.

### Download from the command line

1. Open the command line interface by clicking **Start** and typing `cmd`. Press Enter.
2. From the command line interface, go to the location where you have a local copy of the Pentaho Server installed, such as: `C:/dev/pentaho/pentaho-server`
3. Enter a space, then type the arguments for download into the command line interface

   A completed download argument would look something like this: `import-export.bat --export --url=http://localhost:8080/pentaho --username=dvader --password=password --charset=UTF-8 --path=/public --file-path=C:/Users/dvader/Downloads/pentaho-solutions.zip --overwrite=true --permission=true --retainOwnership=true`
4. Press Enter after typing the arguments.

The download process runs and the results are displayed in the command interface. The file is saved as a ZIP file with the download manifest located in the top level of the file. If an argument is required for successful download and has not been provided, the missing requirement is displayed in the command interface. The [Command line arguments reference](#command-line-arguments-reference) has a list of available command line arguments for downloading.

## Response code definitions

Here is a list of response codes for the `import-export.bat` script:

| Response Code | Definition                                                                             |
| ------------- | -------------------------------------------------------------------------------------- |
| 1             | `Publish to server failed.`                                                            |
| 2             | `General publish error.`                                                               |
| 3             | `Publish successful.`                                                                  |
| 5             | `Authentication to the publish server failed. Username or password is incorrect.`      |
| 6             | `Datasource publish failed.`                                                           |
| 7             | `XMLA catalog already exists.`                                                         |
| 8             | `Schema already exists.`                                                               |
| 9             | `Content about to be published already exists.`                                        |
| 10            | `Error publishing to the server due to prohibited symbols in the name of the content.` |

## Command line arguments reference

You can use the command line to manage the Pentaho Repository. The following tables list the command arguments, descriptions, values, and whether a specific argument is required.

### Upload

The following arguments are for uploading to the Pentaho Repository:

| Command                    | Description                                                                                                 | Values                             | Required |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------- |
| `-i`, `--import`           | Upload Command                                                                                              | n/a                                | Yes      |
| `-x`, `--source <arg>`     | External system type                                                                                        | legacy-db or file-system (default) | Yes      |
| `-o`, `--overwrite <arg>`  | Overwrites file(s) on upload. Default value is: True                                                        | Boolean                            | No       |
| `-m`, `--permission <arg>` | Applies ACL using manifest file. Default value is: True                                                     | Boolean                            | No       |
| `-r`, `--retainOwnership`  | Replaces the file ownership upon upload with the ownership of the original download. Default value is: True | Boolean                            | No       |
| `-t`, `--type <arg>`       | The type of content being uploaded- files (default), metadata.                                              | File type                          | No       |

### Download

The following arguments are for downloading from the Pentaho Repository:

| Command                      | Description                                                                         | Values    | Required |
| ---------------------------- | ----------------------------------------------------------------------------------- | --------- | -------- |
| `-e`, `--export`             | Download command                                                                    | n/a       | Yes      |
| `-fp`, `--filepath <arg>`    | Location that the ZIP file is downloaded to                                         | File path | Yes      |
| `-w`, `--withManifest <arg>` | If true, includes `Manifest.xml` inside ZIP. If false, download excludes this file. | Boolean   | No       |

### Backup and restore

The following arguments are for backing up or restoring the Pentaho Repository:

| Command                   | Description                                                              | Values       | Required |
| ------------------------- | ------------------------------------------------------------------------ | ------------ | -------- |
| `--backup`                | Backup command                                                           | n/a          | Yes      |
| `--restore`               | Restore command                                                          | n/a          | Yes      |
| `-a`, `--url <arg>`       | URL of Pentaho Repository (for example: <http://localhost:8080/pentaho>) | URL          | Yes      |
| `-u`, `--username <arg>`  | Pentaho Repository username                                              | Alphanumeric | Yes      |
| `-p`, `--password <arg>`  | Pentaho Repository password                                              | Alphanumeric | Yes      |
| `-fp`, `--filepath <arg>` | Location that the ZIP file is downloaded to                              | File path    | Yes      |
| `-o`, `--overwrite <arg>` | Overwrites file(s) on upload. Default value is: True                     | Boolean      | No       |
| `--logfile`               | Specifies the location for writing the log file.                         | File path    | No       |

### Common arguments

The following arguments apply to uploading, downloading, backing up and restoring the Pentaho Repository:

| Command                                | Description                                                                                        | Values          | Required |
| -------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------- | -------- |
| `-a`, `--url <arg>`                    | URL of Pentaho Repository (for example: <http://localhost:8080/pentaho>)                           | URL             | Yes      |
| `-c`, `--charset <arg>`                | Charset to use for the repository. Characters from external systems are converted to this charset. | UTF-8 (default) | No       |
| `-h`, `--help`                         | Prints this message.                                                                               | n/a             | No       |
| `-f`, `--path <arg>`                   | Pentaho Repository path to which the uploaded files are added (for example: `/public`)             | File path       | Yes      |
| `-p`, `--password <arg>`               | Pentaho Repository password                                                                        | Alphanumeric    | Yes      |
| `-u`, `--username <arg>`               | Pentaho Repository username                                                                        | Alphanumeric    | Yes      |
| `-l`, `--logfile <arg>`                | Path to local file system with name of file to write                                               | File path       | No       |
| `-a_ds`, `--analysis-datasource <arg>` | Analysis datasource type.                                                                          | Alphanumeric    | No       |
| `-a_xmla`, `--xmla-enabled <arg>`      | Analysis XMLA enabled flag.                                                                        | Boolean         | No       |
| `-cat`, `--catalog <arg>`              | Catalog description.                                                                               | Alphanumeric    | No       |
| `-ds`, `--datasource-type <arg>`       | Datasource type.                                                                                   | Alphanumeric    | No       |
| `-m_id`, `--metadata-domain-id <arg>`  | Metadata domain ID.                                                                                | Alphanumeric    | No       |
| `-params`, `--params <arg>`            | Parameters to pass to `REST` service call.                                                         | Alphanumeric    | No       |
| `-res`, `--resource-type <arg>`        | Import/Export resource type.                                                                       | Alphanumeric    | No       |
| `-rest`, `--rest`                      | Use the REST (default) version (not local to the Pentaho Server).                                  | Alphanumeric    | No       |
| `-v`, `--service <arg>`                | This is the REST Service call, for example: ACL, children, properties                              | URL             | No       |
