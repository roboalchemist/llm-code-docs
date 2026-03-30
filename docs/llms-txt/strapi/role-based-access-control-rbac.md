# Role-Based Access Control (RBAC)

The Role-Based Access Control (RBAC) feature allows the management of the administrators, who are the users of the admin panel. More specifically, RBAC manages the administrators' accounts and roles.

</IdentityCard>

</Tabs>

4. Click on the **Save** button on the top right corner.

:::tip
To create admin permissions for your custom plugin, please refer to our [dedicated guide](/cms/plugins-development/guides/admin-permissions-for-plugins).
:::

#### Setting custom conditions for permissions

For each permission of each category, a 

## Usage

**Path to use the feature:**  *Settings > Administration panel > Users*

The *Users* interface displays a table listing all the administrators of your Strapi application. More specifically, for each administrator listed in the table, their main account information are displayed, including name, email and attributed role. The status of their account is also indicated: active or inactive, depending on whether the administrator has already logged in to activate the account or not.

From this interface, it is possible to:

- make a textual search  to find specific administrators,
- set filters  to find specific administrators,
- create a new administrator account (see [Creating a new account](#creating-a-new-account)) ,
- delete an administrator account  (see [Deleting an account](#deleting-an-account)),
- or access information regarding an administrator account, and edit it  (see [Editing an account](#editing-an-account)).

:::tip
Sorting can be enabled for most fields displayed in the table. Click on a field name, in the header of the table, to sort on that field.
:::

### Creating a new account

1. Click on the  **Invite new user** button.
2. In the *Invite new user* window, fill in the Details information about the new administrator:

  | User information | Instructions                                                                 |
  | ---------------- | ---------------------------------------------------------------------------- |
  | First name       | (mandatory) Write the administrator's first name in the textbox.             |
  | Last name        | (mandatory) Write the administrator's last name in the textbox.              |
  | Email            | (mandatory) Write the administrator's complete email address in the textbox. |

3. Fill in the Login settings about the new administrator:

  | Setting          | Instructions                                                                                                    |
  | ---------------- | --------------------------------------------------------------------------------------------------------------- |
  | User's roles     | (mandatory) Choose from the drop-down list the role to attribute to the new administrator.                      |
  | Connect with SSO | (optional) Click **TRUE** or **FALSE** to connect the new administrator account with SSO.                       |

4. Click on the **Invite user** button in the bottom right corner of the *Add new user* window.
5. A URL appears at the top of the window: it is the URL to send the new administrator for them to log in for the first time to your Strapi application. Click the copy button  to copy the URL.
6. Click on the **Finish** button in the bottom right corner to finish the new administrator account creation. The new administrator should now be listed in the table.

:::note
The administrator invitation URL is accessible from the administrator's account until it has been activated.
:::

### Deleting an account

It is possible to delete one or several administrator accounts at the same time.

1. Click on the delete button  on the right side of the account's record, or select one or more accounts by ticking the boxes on the left side of the accounts' records then click on the  **Delete** button above the table.
2. In the deletion window, click on the **Confirm** button to confirm the deletion.

### Editing an account

1. Click on the name of the administrator whose account you want to edit.
2. In the *Details* area, edit your chosen account details:

| User information      | Instructions  |
| --------------------- | ----------------------- |
| First name            | Write the administrator's first name in the textbox.                                        |
| Last name             | Write the administrator's last name in the textbox.                                         |
| Email                 | Write the administrator's complete email address in the textbox.                            |
| Username              | Write the administrator's username in the textbox.                                          |
| Password              | Write the new administrator account's password in the textbox.                              |
| Confirm password      | Write the new password in the textbox for confirmation.                                     |
| Active                | Click on **TRUE** to activate the administrator's account.                                  |

3. (optional) In the *Roles* area, edit the role of the administrator:
  - Click on the drop-down list to choose a new role, and/or add it to the already attributed one.
  - Click on the delete button  to delete an already attributed role.
4. Click on the **Save** button in the top right corner.