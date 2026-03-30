# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/user-security/pentaho-server-security/hiding-user-folders-in-puc-and-pdi-cp.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/user-security/pentaho-server-security/hiding-user-folders-in-puc-and-pdi-cp.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/user-security/pentaho-server-security/hiding-user-folders-in-puc-and-pdi-cp.md

# Hiding user folders in PUC and PDI

One way you can centralize and secure content created by users is to hide individual users' Home folders in the Pentaho User Console (PUC) or in the PDI client. For example, if your organization implements multi-tenancy, you may want to prevent individual users from viewing their Home folders for security reasons.

You can configure your server to hide the Home folders by default for both PUC and PDI. When you create new users in your system, their Home folders will be hidden. If a user needs to create, edit, or save content, you can provide the Write permission in a folder that is visible to that user. Those users can then view the folder and access the content. You can add the Write permission in PUC and in the PDI client.

These tasks assume you are a Pentaho Administrator.

To centralize and secure content created by users, you can hide users' Home folders in PUC and in the PDI client.

Perform the following steps to edit the `system.properties` file so that when you create new users, their Home folders will be hidden by default.

1. Stop the Pentaho Server.

   See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.
2. Navigate to `/Pentaho/server/pentaho-server/pentaho-solutions/system` and open the `system.properties` file with the text editor of your choice.
3. Locate the **hideUserHomeFolderOnCreate** property. By default, this property is set to `false.`
4. Change the setting to `true` as shown here:

   **hideUserHomeFolderOnCreate=true**
5. Save and close the `system.properties` file.
6. Start the Pentaho Server.

   See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

Now when you add a new user in either PUC or the PDI client, that user's Home folder is hidden by default. Later, you may need to perform one of the following actions:

* To override this setting for a specific user, see [Override the hidden Home folder for a user](#override-the-hidden-home-folder-for-a-user).
* To stop hiding Home folders by default when you create new users, see [Stop hiding the Home folder for new users](#stop-hiding-the-home-folder-for-new-users).
* If a user whose Home folder is hidden needs to create, edit, or save any content, you must provide the Write permission in a folder that is visible to the user in PUC and in the PDI client. See the instructions for assigning Write permission in the following section, [Assign the Write permission to a user folder](#assign-the-write-permission-to-a-user-folder).

## Override the hidden Home folder for a user

Follow these steps to override the hidden Home folder for a specific user.

1. Log in to PUC with your Pentaho Administrator credentials.
2. Navigate to the **Browse Files** perspective.
3. Select the user’s **Home** folder.
4. In the **Properties** dialog box, clear the **Hidden** option.

The user's home folder is now visible.

## Stop hiding the Home folder for new users

Follow these steps to stop creating users with their Home folders hidden by default.

1. Stop the Pentaho Server.
2. Navigate to `/Pentaho/server/pentaho-server/pentaho-solutions/system` and open the `system.properties` file with the text editor of your choice.
3. Locate the **hideUserHomeFolderOnCreate** property.
4. Change the setting to `false` as shown here:

   **hideUserHomeFolderOnCreate=false**
5. Save and close the `system.properties` file.
6. Start the Pentaho Server.

When you add a new user in either PUC or the PDI client, that user's Home folder is now visible.

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

## Assign the Write permission to a user folder

{% tabs %}
{% tab title="Assign permission in PUC" %}
In PUC you can assign Write permission in a public folder to a user whose **Home** folder is hidden. When this permission is granted, the user can save and edit content they create using PUC.

1. Log in to PUC with your Pentaho Administrator credentials.
2. Select the **Public** folder, and then select or create the folder you want the user to access.
3. Assign the **Write** permission to the user's folder:
   1. Click the **Properties** > **Share** tab and clear the **Inherits folder permissions** option.
   2. Click **Add** and select the user.
   3. Select the **Write** permissions for the user.
   4. Click **OK** to save your changes.

The user can now save their content in the assigned folder.
{% endtab %}

{% tab title="Assign permission in PDI client" %}
In the PDI client you can assign the Write permission in a public folder to a user whose **Home** folder is hidden. When this permission is granted, the user can save and edit content they create using the PDI client.

1. Start the PDI client

   See the **Pentaho Data Integration** document for instructions on starting the PDI client.
2. Connect to a Pentaho Repository with your Pentaho administrator credentials. If needed, create a connection.
3. Open the Repository Explorer by clicking **Tools** > **Repository** > **Explore**.
4. On the **Browse** tab, select the **Public** folder, and then select or create the folder you want the user to access.
5. Select the newly created folder and grant **Write** permission to the new user by performing the following steps:
   1. On the Access Control panel, clear the **Inherit access control from parent** option.
   2. Click the **Plus Sign** to add a user.
   3. From the list of users that displays, select the name of the user you want and click the Right Arrow to move the name to the **Selected** list. Click **OK**.
   4. Select the user's name in the **User/Role** list and select the **Write** permission.
   5. Click **Apply** to save your changes, then click **OK** to close the dialog box.
6. Close the **Repository Explorer**.

The user can now save their content in the assigned folder.
{% endtab %}
{% endtabs %}
