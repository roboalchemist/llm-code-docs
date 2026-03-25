# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/use-pentaho-repository-access-control.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/use-the-repository-explorer/use-pentaho-repository-access-control.md

# Use Pentaho Repository access control

You can control access to your [repository](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi) by locking files, establishing connection security, and restricting folder permissions.&#x20;

## Lock and unlock jobs and transformations

You can lock or unlock jobs and transformations. Locking and unlocking jobs and transformations protect them from being edited by other users.

### Lock a job or transformation

To lock a job or transformation, complete these steps:

1. In the **Browse** tab in the Repository Explorer window, right-click the job, or transformation and select **Lock**.
2. Enter the notes in the Lock Notes window that appears.
3. Click **OK**.

   The job or transformation icon changes to show a padlock.

   **Note:** The lock status icons are updated on each PDI client only when the Repository Explorer is accessed. If you want to refresh lock status in the Repository Explorer, exit and access it again. Also, to select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations.

   ![Locked status icon](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9d90e42782e4c5108f6c6bdc37d0e89d181841f9%2Flockicon.png?alt=media)

### View lock notes

To view notes that were entered when the job or transformation was locked, do these things:

1. In the **Browse** tab in the Repository Explorer window, right-click the job, or transformation and select **Lock Notes**.

   The lock note appears in a pop-up window.
2. Click **OK** to dismiss the note.

### Unlock a job or transformation

To unlock a job or transformation, complete these steps:

1. In the **Browse** tab in the Repository Explorer window, right-click the job, or transformation,
2. Select **Lock**.

   The icon for the job or transformation returns to normal; the padlock icon disappears.

   **Note:** To select more than one file, hold down the CTRL or the SHIFT key as you select the folders, jobs, or transformations.

## Access connection, security, and cluster information

In addition to managing content such as jobs and transformations, click the **Connections** tab to manage (create, edit, and delete) your database connections in the Pentaho Repository. See [Manage repositories in the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/use-a-pentaho-repository-in-pdi/manage-repositories-in-the-pdi-client) for more information about connecting to a database.

Click the **Security** tab to manage users and roles. Pentaho Data Integration comes with a default security provider. If you do not have an existing security such as LDAP or MSAD, you can use Pentaho Security to define users and roles. You must have administrative privileges to manage security. For more information, see the **Administer Pentaho Data Integration and Analytics** document.

![Security tab, Repository explorer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3265d56448dd5ef7fea2d41fe2d81d691a7bd263%2Fpermissions.png?alt=media)

You can manage your slave servers (Pentaho and Carte instances) by clicking the **Slaves** tab. See [Initialize Slave Servers](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/initialize-slave-servers) for instructions.

Click the **Partitions** and **Cluster** tabs to manage partitions and clusters. See [Create a cluster schema](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/create-a-cluster-schema) for more information.

## Set folder-level permissions

The following table explains the permissions settings for Pentaho Repository content and folders:

| Type                      | Value                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------- |
| **Read**                  | If set, the content of the file or contents of the directory will be accessible. Allows execution. |
| **Manage Access Control** | If set, access controls can be changed for this object.                                            |
| **Write**                 | If set, enables read and write access to the selected content.                                     |
| **Delete**                | If set, the content of the file or directory can be deleted.                                       |

**Note:** You must assign both **Write** and **Manage Access Control** to a directory in order to enable the selected user to create subfolders and save files within the folder.

You can assign any of these permissions to files and folders stored in a Pentaho Repository. Setting permissions manually overrides inherited permissions if the access control flags allow.

Perform the following steps to set folder-level permissions:

1. Open the Repository Explorer (**Tools** > **Repository** > **Explore**).
2. Navigate to the folder to which you want permissions set and click to select it.

   The folder must appear in the right pane before you can set permissions.
3. In the lower pane, under the **Permissions** tab, disable **Inherit security settings from parent**.
4. Click **Add** to open the Select User or Role dialog box.
5. Select a user or role to add to the permission list.
   1. Use the yellow arrows to move the user or role in or out of the permissions list.
   2. Click **OK** when you are done.
6. In the lower pane, under the **Access Control** tab, enable the appropriate **Permissions** granted to your selected user or role.

   If you change your mind, use **Delete** to remove users or roles from the list.
7. Click **Apply** to apply permissions.
