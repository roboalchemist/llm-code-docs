# Source: https://docs.pentaho.com/pba/pentaho-user-console/modern-design/browse-files.md

# Browse Files

The Browse Files component of the Modern Design interface helps you keep your files and folders organized, making them easier to find and use. The available folders, files, and actions in the Browse Files component depend on your role and permissions.

**Note:** The Browse Files component is required to use the [Scheduler](https://docs.pentaho.com/pba/pentaho-user-console/modern-design/scheduler).

## Find files or folders to manage

To find files or folder to manage in the Browse Files component, complete the following steps:

1. Log into the Pentaho User Console (PUC).
2. Open the **Browse Files** component by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click Browse Files.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to Modern Design**, and then select **Browse Files**.&#x20;

   The **Browse Files** component opens.
3. To display the list of files or folders that contains the one you want to manage, take one of the following actions:&#x20;

   * In the left sidebar navigation menu, select one of the following options:

     <table><thead><tr><th width="176.00006103515625">Menu option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Browse Files</strong></td><td>Displays a list files and folders in the Home folder of your repository. </td></tr><tr><td><strong>Recently opened</strong></td><td>Displays a list of recently opened files.</td></tr><tr><td><strong>Favorites</strong></td><td>Displays a list of files that you have marked as favorites.</td></tr><tr><td><strong>Trash</strong></td><td>Displays a list of files and folders that you sent to the trash.</td></tr></tbody></table>
   * In the **Folders** pane, expand folders to find the one that contains the file or folder you want to manage and then select that folder.

   The list of files and folders is displayed in a table on the main pane of the Browse Files component.

## Manage files and folders in repository

You can take one of the following actions for a file or folder in the repository: open, schedule, download, move, duplicate, send to trash, info, or rename.

Before you can manage a specific file or folder, you must find the folder that contains it. For details, see [Find files or folders to manage](#find-files-or-folders-to-manage).

To manage a specific file or folder, complete the following steps:&#x20;

1. In the list of files and folders containing the one you want to manage, browse or search for the specific file or folder you want by name.&#x20;
2. Manage the file or folder by taking one of the following actions:
   1. To open the file or folder, click **Open**. Folders open to display their contents in the main pane of the Browse files component. Files open in the Classic Design of PUC.
   2. To manage the file or folder, in the rightmost side of its row, click the **More Actions** icon, and then select one of the following options:

      <table><thead><tr><th width="243.55548095703125">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Schedule</strong></td><td>Opens the <strong>Create Schedule</strong> window, where you can configure a transformation or job to run once or on a recurring schedule, according to settings you specify. The <strong>Schedule</strong> option is available only for transformation (.ktr) and job (.kjb) files. For detailed instructions on creating a schedule, see <a href="scheduler/schedule-a-transformation-or-job">Schedule a transformation or job</a>.</td></tr><tr><td><strong>Download</strong></td><td>Downloads the file or folder to your default download folder. Folders and their contents are downloaded as zip files. </td></tr><tr><td><strong>Move</strong></td><td>Opens the <strong>Move to</strong> window. In the <strong>Move to</strong> window, you can navigate to a different folder or create a new folder and click <strong>Move here</strong> to move the file or folder to that folder.</td></tr><tr><td><strong>Duplicate</strong></td><td>Opens the <strong>Duplicate to</strong> window. In the <strong>Duplicate to</strong> window, you can navigate to a different folder or create a new folder and click <strong>Paste here</strong> to create a duplicate of the file or folder in that folder.</td></tr><tr><td><strong>Send to trash</strong></td><td>Opens the <strong>Send to trash?</strong> dialog box. You can click <strong>Yes</strong> to move the file or folder into the trash.</td></tr><tr><td><strong>Info</strong></td><td>Opens a window that displays information about the file or folder. You can also copy the file path from the <strong>Info</strong> window by clicking <strong>Copy source</strong>. </td></tr><tr><td><strong>Rename</strong></td><td><p><strong>Important</strong>: After you rename a transformation or job, any dashboards, schedules, or favorites linked to it become inactive and stop functioning.</p><p></p><p>Makes the transformation or job name editable in the table. After you enter a new name, you must click <strong>OK</strong> to rename the transformation or job.</p></td></tr></tbody></table>

## Manage files and folders in trash

You can restore or permanently delete files and folders that you have moved into the trash.

[Find the file or folder](#find-a-file-or-folder) you want to manage in the Trash and then do one of the following:

1. Log into the Pentaho User Console (PUC).
2. Open the **Browse Files** component by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click Browse Files.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to Modern Design**, and then select **Browse Files**.&#x20;

   The **Browse Files** component opens.
3. In the left sidebar navigation menu, select **Trash.** The list of files and folders that you sent to the trash is displayed in a table on the main pane of the Browse Files component.
4. To manage the file or folder in the trash, take one of the following actions:
   * To restore the file or folder from the Trash, click **Restore**.
   * To permanently delete a single file or folder in the Trash, click the **More Actions** icon, and then select **Permanently delete**.
   * To permanently delete all files and folders in the Trash, click **Delete all permanently**.

## Create a new folder

You can use the Browse Files component to create a new folder in your repository.

To create a new folder, complete the following steps:

1. Log into the Pentaho User Console (PUC).
2. Open the **Browse Files** component by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click Browse Files.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to Modern Design**, and then select **Browse Files**.&#x20;

   The **Browse Files** component opens.
3. In the **Folders** pane, expand folders to find the one where you want to create a new folder.
4. Click **+ New folder**. In the main pane of the Browse Files component, at the top of the table, a new row is added, and the **Name** field is made editable.
5. Enter a **Name** for the new folder and click the **Ok** icon (a green checkmark). The new folder is added to the table and assigned to you as the owner.

## Upload files and folders

In the Browse Files component, you can upload one or more files or a folder and its contents to your repository. Folders must be in a zip file format to upload.

To upload files or a folder and its contents, complete the following steps:

1. Log into the Pentaho User Console (PUC).
2. Open the **Browse Files** component by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click Browse Files.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to Modern Design**, and then select **Browse Files**.&#x20;

   The **Browse Files** component opens.
3. In the **Folders** pane, expand folders to find the repository folder where you want to upload your file or folder.&#x20;
4. Click **Upload**.&#x20;
5. In the window that opens, find the **Drop file here** box, and then drop one or more or more files or folder zip files in the box.
6. (Optional) To set logging preferences for the upload and manage file permissions for the uploaded files, turn on the **Advanced options** toggle, and then edit the following options:

   <table><thead><tr><th width="160.8887939453125">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Replace files</strong></td><td>Specifies that if a file with the same name already exists in the folder, the uploaded file replaces it. </td></tr><tr><td><strong>Don't upload</strong></td><td>Specifies that a file is not uploaded when it has the same name as a file already in the folder.</td></tr><tr><td><strong>File permissions</strong></td><td><p>Specifies how to handle permissions for an uploaded file that was previously stored on Pentaho Platform and has existing metadata.</p><p></p><p>Use the following options to specify how you want files handled if metadata is detected:</p><ul><li>Do not change permissions</li><li><p>Retain permissions</p><ul><li>Set owner based on uploaded file</li><li>Do not change owner</li></ul></li></ul></td></tr><tr><td><strong>Logging</strong></td><td>Specifies whether the system displays logging details for your upload request. Turn on the <strong>Logging</strong> option to view logging details for the upload.</td></tr></tbody></table>
7. Click **Upload**. The files are uploaded and displayed in the main pane of the Browse Files component.
