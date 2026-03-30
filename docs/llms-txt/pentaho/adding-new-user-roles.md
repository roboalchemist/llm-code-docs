# Source: https://docs.pentaho.com/pentaho-data-mastering/setting-up-users-and-roles/adding-user-roles/adding-new-user-roles.md

# Adding new user roles

Add a new user role with specified permissions so that you can control which actions a user with that role can perform in the Pentaho Data Mastering.

You must have admin privileges to add user roles.

Perform the following steps to add a user role:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. In the **Users** card, click **Roles**.

   The Roles page opens.
3. Click **Add Role**.
4. Click **Create New**.

   The Create Role page opens.
5. Specify the following information:

| Field             | Description                                                                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name\***        | Name of the new user role. **Tip:** In your identity management tool, the user role name is appended with the prefix, `MDM`. For example, the admin role is `MDM_Admin` in the Keycloak IAM server.                                      |
| **Description**   | Description of the user role.                                                                                                                                                                                                            |
| **PERMISSIONS\*** | <p>Permissions that you want to assign to the user role. <strong>CAUTION:</strong></p><p>By default, all permissions are listed in the PERMISSIONS box. You must remove permissions that you do not want to assign to the user role.</p> |

\* *Mandatory Field*

6. Click **Create Role** to create the new role.

   A confirmation message appears in the top-right corner of the page.

   **Tip:** To add multiple user roles at one time, see [Adding user roles in bulk](https://docs.pentaho.com/pentaho-data-mastering/setting-up-users-and-roles/adding-user-roles/adding-new-user-roles/adding-user-roles-in-bulk).
