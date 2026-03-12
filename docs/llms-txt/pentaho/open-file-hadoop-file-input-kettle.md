# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/open-file-hadoop-file-input-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/open-file-hadoop-file-input-kettle.md

# Open file

When you select **S3** in the **Environment** field, and then select the Ellipsis (…) button in the **File/Folder** field, the Open File dialog box appears. Perform the following steps to open a file.

![Open File dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3849902ec610a1192b94694f26b743d18e5e6ea7%2FPDITransStep_HadoopFileInput_FileTab_OpenFile_Dialog.png?alt=media)

1. In the **Connection** section, fill in the following options.

   | Option               | Description                                                                                                                                                                 |
   | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Access Key**       | Enter the user name needed to access the S3 file system. This option only appears if you select **S3** in the **Source Environment** field in the Hadoop File Input window. |
   | **Secret Key**       | Enter the password needed to access the S3 file system. This option only appears if you select **S3** in the **Source Environment** field in the Hadoop File Input window.  |
   | **Open from Folder** | Indicates the path and name of the directory you want to browse. This directory becomes the active directory.                                                               |
2. In the **Open from Folder** field, navigate to the path and name of the directory you want to browse. This directory becomes the active directory.
3. Use the following options to view and modify the active directory selected in the **Open from Folder** field:

   | Option                 | Description                                                                                                                                                                                            |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Up One Level** icon  | Click this button to display the parent directory of the active directory shown in the **Open from Folder** field.                                                                                     |
   | **Delete** icon        | Click this button to delete a folder from the active directory.                                                                                                                                        |
   | **Create Folder** icon | Click this button to create a new folder in the active directory.                                                                                                                                      |
   | **Name/Type/Modified** | Display the active directory, which is the one that is listed in the **Open from Folder** field. The file type and last modified date display to the right of the folder or file in the **Name** list. |
   | **Filter**             | Apply a filter to the results displayed in the active directory contents.                                                                                                                              |
4. Click **OK** to continue, or **Cancel** to return to the **File** tab without saving your selections.
