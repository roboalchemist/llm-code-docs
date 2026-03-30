# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/assign-permissions-to-use-or-manage-database-connections.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/assign-permissions-to-use-or-manage-database-connections.md

# Assign permissions to use or manage database connections

You may have several connections to your data that you do not want to share with all of your users. When connected to the Pentaho Server, the PDI client (also known as Spoon) gives you the ability to make your data visible to only those users and roles that you specify. You can assign permission to allow users and roles to read, write, or delete the connection. Connection definitions are stored in the Pentaho Repository. The PDI client Repository Explorer enables you to browse the available connections and select the one for which you want to assign permissions.

1. From within the PDI client, click on **Tools** > **Repository** > **Explore**.

   The Repository Explorer appears.
2. Select the **Connections** tab.
3. Select the connection for which you want to assign permissions.
4. From the **User/Role** area, select the user or role for which you want to assign permissions.
5. Check the permissions you want to assign to the selected user or role.

   | Selection                 | Selection Result                                                                                                                                                                                                                                                                          |
   | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Read**                  | For this user or role, the connection appears in the connection list and can be selected for use. If users or roles have permission to read a transformation or job but not to a referenced database connection, they cannot open the transformation or job and an error message appears. |
   | **Write**                 | This user or role can edit the connection definition.                                                                                                                                                                                                                                     |
   | **Delete**                | This user or role can permanently remove the connection definition from the list..                                                                                                                                                                                                        |
   | **Manage Access Control** | This user or role can assign read, write, and delete permissions to other users or roles.                                                                                                                                                                                                 |
6. Click **Apply**.
7. Click **Close** to exit the dialog box.

You can also delegate the ability to assign these permissions to another user or role. For more information on managing users and roles, see [With the PDI client](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/manage-users-and-roles-in-the-pdi-client).
