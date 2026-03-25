# Source: https://docs.pentaho.com/pdia-data-integration/collaborating-with-pdi.md

# Collaborating with PDI

Use repositories and projects to collaborate in Pentaho Data Integration (PDI).

### In this article

* [Use a Pentaho Repository in PDI](#use-a-pentaho-repository-in-pdi)
  * [Create a connection in the PDI client](#create-a-connection-in-the-pdi-client)
  * [Connect to a Pentaho Repository](#connect-to-a-pentaho-repository)
  * [Manage repositories in the PDI client](#manage-repositories-in-the-pdi-client)
  * [Unsupported repositories](#unsupported-repositories)
  * [Use the Repository Explorer](#use-the-repository-explorer)
  * [Advanced topics](#advanced-topics)
* [Share PDI projects](#share-pdi-projects)
  * [Share a project](#share-a-project)

### Use a Pentaho Repository in PDI

The PDI client (Spoon) supports several storage options. A Pentaho Repository stores content on Pentaho Server.

Use a Pentaho Repository for team collaboration. You get version history, content locking, and enterprise security.

#### Create a connection in the PDI client

To access repository items in Spoon, create a connection first.

1. Verify Pentaho Server is running.
2. Start the PDI client.
3. Click **Connect** in the upper-right corner of the toolbar.

   The **Repository Manager** dialog box opens.

   **Note:** If **Connect** is replaced, you are already connected.
4. Click **Add**.
5. Select a repository type:

   * **Pentaho Repository**. Recommended for production use.
   * **File Repository**. Uses your local file system.
   * **Database Repository**. Uses a relational database.

   **Note:** File and database repositories are not supported for production use.
6. Enter or update **Display Name**.
7. Update the repository URL if needed.
8. (Optional) Enter a **Description**.
9. Click **Save**.

The repository appears in the **Repository Manager** list.

#### Connect to a Pentaho Repository

After you create a repository, connect to it from the **Connect** menu.

1. Select a repository from the **Connect** menu.

   **Note:** If this is your first repository, select it after creation.
2. Enter your **User Name** and **Password**.

   Example: **User Name** = `admin`, **Password** = `password`.
3. Click **Login**.

If login fails, check the repository URL and port.

To show the connection dialog at startup, go to **Tools** > **Options**. Select **Show repository dialog at startup**.

#### Manage repositories in the PDI client

After you create a repository, a menu appears next to **Connect**. Use this menu to switch repositories, open **Repository Manager**, or disconnect.

**Repository Manager**

Use **Repository Manager** to add, edit, or delete repository definitions.

![Repository Manager dialog box](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-0e11da904b1a05a687555fd9d40bacff3565e7ec%2FssPDIRepository_Manager_9.4.png?alt=media)

If you set a default repository at startup, clear it in the same dialog. Select **Launch connection on startup** again to remove the setting.

**Connection details**

Use **Connection Details** to configure a repository connection.

| Setting                          | Description                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------- |
| **Display Name**                 | Identifies the repository within the PDI client.                              |
| **URL**                          | Defines the repository web address. Default: `http://localhost:8080/pentaho`. |
| **Description**                  | Describes the repository, such as its purpose.                                |
| **Launch connection on startup** | Connects automatically when the PDI client starts.                            |

#### Unsupported repositories

You can also create database or file repositories. Use **Other Repositories** in the welcome dialog.

**Note:** File and database repositories are not supported for production use.

**Database repository**

Database repositories store metadata in a relational database.

1. Enter a **Display Name**.
2. Select a **Database Connection**.
3. Create, edit, or delete the database connection.
4. Click **Test** and then click **OK**.
5. Click **Finish** to test the repository connection.

**File repository**

File repositories store metadata on your local file system.

1. Enter a **Display Name**.
2. Set **Location** for the repository.
3. Click **Finish** to test the repository connection.

When you connect, the toolbar shows only the repository display name.

#### Use the Repository Explorer

Use Repository Explorer to manage repository content. Most tasks are in the **Browse** tab.

**Access the Repository Explorer window**

1. Connect to a repository.
2. Select **Tools** > **Repository** > **Explore**.

The Repository Explorer window opens. Your permissions control what you can view and do.

![Repository Explorer window](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-f2cd0270b2d8c01b140f8f6cdddc4a167f3c8461%2FRepositoryExplorerWindow.png?alt=media)

If Repository Explorer is empty with LDAP, update your LDAP settings. See [With LDAP authentication, the PDI Repository Explorer is empty](https://docs.pentaho.com/pdia-data-integration/data-integration-issues/with-ldap-authentication-the-pdi-repository-explorer-is-empty).

**Create a new folder in the repository**

1. In the **Browse** tab, right-click the parent folder.

   Example: right-click `public` to create a subfolder.
2. Select **New Folder**.
3. Enter the folder name.
4. Click **OK**.

**Open a folder, job, or transformation**

1. Right-click the folder, job, or transformation.
2. Select **Open**.

To open multiple files, hold **Ctrl** or **Shift** while selecting.

**Rename a folder, job, or transformation**

1. In the **Browse** tab, right-click the item and select **Rename**.
2. Enter the new name.
3. Click **OK**.
4. Enter a comment when prompted.
5. Click **OK**.

The **Version History** tab records the rename with your comment.

**Move objects**

1. Select the object in the repository.
2. Drag the object to the destination folder.

You can move content into another user’s folder.

To move multiple items, hold **Ctrl** or **Shift** while selecting. Then right-click and select **Move**.

**Delete a folder, job, or transformation**

1. In the **Browse** tab, right-click the item and select **Delete**.
2. Click **Yes** in the warning message.
3. Click **OK**.

To delete multiple items, hold **Ctrl** or **Shift** while selecting.

**Restore objects**

1. Double-click the **Trash** icon.
2. Right-click the object and select **Restore**.

**Controlling access to Pentaho Repository**

You can control repository access with locking and permissions. You can also manage users, roles, connections, and cluster metadata.

**Lock and unlock jobs and transformations**

Locking prevents other users from editing the file.

**Lock a job or transformation**

1. In the **Browse** tab, right-click the job or transformation.
2. Select **Lock**.
3. Enter lock notes.
4. Click **OK**.

The icon shows a padlock.

Lock status refreshes when you reopen Repository Explorer. Exit and reopen the window to refresh icons.

![Locked status icon](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-9d90e42782e4c5108f6c6bdc37d0e89d181841f9%2Flockicon.png?alt=media)

**View lock notes**

1. Right-click the job or transformation.
2. Select **Lock Notes**.
3. Click **OK**.

**Unlock a job or transformation**

1. Right-click the job or transformation.
2. Select **Lock**.

The padlock icon disappears.

**Access connection, security, and cluster information**

Use the **Connections** tab to manage database connections. See [Manage connections for transformations and jobs](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/manage-connections-for-transformations-and-jobs).

Use the **Security** tab to manage users and roles. You need administrative privileges for security tasks.

![Security tab, Repository explorer](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-3265d56448dd5ef7fea2d41fe2d81d691a7bd263%2Fpermissions.png?alt=media)

Use the **Slaves** tab to manage slave servers. See [Initialize Slave Servers](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/carte-clusters-archive/set-up-a-carte-cluster/initialize-slave-servers).

Use the **Partitions** and **Cluster** tabs for partitioning and clusters. See [Create a cluster schema](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/carte-clusters-archive/set-up-a-carte-cluster/create-a-cluster-schema).

**Set folder-level permissions**

These permissions apply to repository files and folders:

* **Read**. View content and execute it.
* **Manage Access Control**. Change permissions.
* **Write**. Read and write the content.
* **Delete**. Delete the content.

**Note:** Assign **Write** and **Manage Access Control** to allow new subfolders.

To set folder permissions:

1. Open Repository Explorer (**Tools** > **Repository** > **Explore**).
2. Select the folder in the right pane.
3. In the lower pane, select **Permissions**.
4. Clear **Inherit security settings from parent**.
5. Click **Add** and select a user or role.
6. In **Access Control**, select the permissions to grant.
7. Click **Apply**.

**Using version history**

Version history lets you compare versions and restore earlier versions. By default, each save creates a new version.

**Use version history**

1. Select **Tools** > **Repository** > **Explore**.
2. In **Browse**, select the folder with the file.
3. Select the file in the upper-right pane.

Versions appear under the **Version History** tab.

![Version History tab, Repository explorer window](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-faff923279154658ca2f5dc63d2e80c68a6cd7ce%2FssPDIRepository_ExplorerVersionHistoryTab.png?alt=media)

**Open a version of a file**

1. Right-click a version under **Version History**.
2. Select **Open**.

The version opens in the PDI client as a separate item. The tab title includes the version number.

**Restore a version of a file**

You need administrative privileges to restore a version.

1. Right-click a version under **Version History**.
2. Select **Restore**.
3. Follow the prompts and click **OK**.

![Restoring a file](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-cb63625056510388872630fd4d87a1ff713903bc%2FssPDIRestoring_a_Previous_Version.png?alt=media)

The restored version becomes the latest version.

![Restoring a file result](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-36c26ec28d09c0cdd73f92284cd73b3daddfe7c0%2FssPDIResults_of_Restoring_a_Previous_Version.png?alt=media)

**Enable or disable tracking of version history and comments**

You can toggle version tracking for all users in this file: `server/pentaho-server/pentaho-solutions/system/repository.spring.properties`

* Set `versioningEnabled=true|false`.
* Set `versionCommentsEnabled=true|false`.

To apply changes:

1. Exit the PDI client.
2. Stop Pentaho Server.
3. Update the properties file.
4. Start Pentaho Server.
5. Start the PDI client.

#### Advanced topics

For advanced repository administration, see the [Administer Pentaho Data Integration and Analytics](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/iFWuQjAZNxh1EoQbRnsT/) documentation.

* [Import and export PDI content](https://app.gitbook.com/s/iFWuQjAZNxh1EoQbRnsT/manage-the-pentaho-system/manage-the-pentaho-repository/import-and-export-pdi-content)
* [Purge transformations, jobs, and shared objects](https://app.gitbook.com/s/iFWuQjAZNxh1EoQbRnsT/manage-the-pentaho-system/manage-the-pentaho-repository/purge-transformations-jobs-and-shared-objects-from-the-pentaho-repository)
* [Backup and restore a Pentaho Repository](https://app.gitbook.com/s/iFWuQjAZNxh1EoQbRnsT/manage-the-pentaho-system/manage-the-pentaho-repository/backup-and-restore-pentaho-repositories)

### Share PDI projects

In Pentaho Data Integration (PDI), you can use a project folder to store ETL workflow files, settings, and related content all in one, self-contained container. You can share that project folder with one or many users that can access it, regardless of the PDI client configuration or project path they use.

#### Share a project

Use one of the following options to share your project with other users:

* Create the project in the Pentaho Repository or a shared VFS.
* Move an existing project into a Pentaho Repository or shared VFS.
* Check the project folder into your organization’s version control system.
* Outside of the PDI client, save the project folder as a ZIP file and share it directly with another user. Projects shared as ZIP files can be opened in the recipient's chosen location. After the recipient saves the project to their chosen location, they can open it and then refresh the project by clicking **Project** > **Refresh Project**.

To learn more about projects and their benefits, see [Organizing ETL with projects](https://docs.pentaho.com/pdia-data-integration/organizing-etl-with-projects).
