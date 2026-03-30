# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/set-up-a-local-vfs-location-for-schedule-outputs.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/set-up-a-local-vfs-location-for-schedule-outputs.md

# Set up a Local VFS location for schedule outputs

With the VFS connection in the Pentaho User Console, you can use the local physical file system of the machine as the location to store the output of your schedule reports and generated outputs. You must be an administrator to create, edit, or delete the VFS connection, to designate roles that can access the connection, and specify the folder.

**Note:** You must know the full path and folder location where you want to set a local connection because there is no browse function available. You should also know how much storage space is available.

Perform the following steps to create a VFS connection from the User Console to a local file location:

1. Click **Home** and then click **Administration**.

   The Administration perspective opens.
2. Click **VFS Connections** and then click the plus sign to add a connection.

   The New VFS Connection dialog box for general settings opens.

   ![New VFS Connection dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-a7c4582439bd36b1a14ef07d30a2e8b458f86a8f%2FPUC%20New%20VFS%20Connecion%20dialog%20box.png?alt=media)
3. Enter a name for the connection in the **Connection Name** field and optionally add a description for the connection in the **Description** field.
4. Click **Connection Type** and select **Local**.

   See [Set up a VFS location for schedule outputs](https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/setup-a-vfs-location-for-schedule-output) for details about creating other connection types. 
5. In **Access Roles**, click a role or use CtrlClick to select multiple roles from the list to assign permissions for access to the VFS connection and folder.

   The defaults are Administrator and Authenticated.
6. Click **Next**.

   The New VFS Connection dialog box for root folder details opens.
7. Enter the **Root Folder Path** to set the path for your VFS connection output folder. Enter the full path to set a local connection to a specific folder. Optionally, use an empty path to allow access to the root and all its folders.

   The default is to the root and its folders in your local physical file system.
8. Click **Test** to test the connection.

   The test results open.
9. Click **Next**.

   The New VFS Connection summary panel opens with all the information you have entered for the connection including the **Root Folder Path**.
10. If needed, click the **pencil** icon to edit the connection.
11. Click **Finish** to complete the setup.

    The test results display and the New VFS Connection dialog box opens with options to **Create new VFS connection** or **Edit this connection**. If needed, click **Edit this connection** to make changes to the connection.
12. Click **Finish**.

Your new connection is created and listed in the VFS Connections panel.

To edit a VFS connection, select the connection and click the **Edit Connection** icon. To delete the connection, click the **Delete Connection** icon.
