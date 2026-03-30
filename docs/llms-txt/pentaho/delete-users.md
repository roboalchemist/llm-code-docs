# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc/delete-users.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc/delete-users.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc/delete-users.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/manage-users-and-roles/manage-users-and-roles-in-the-pdi-client/delete-users.md

# Delete users

**Note:** We recommend that you disable a user or role instead of deleting it.

1. Select **Users**, then highlight the user to be deleted in the **Available** list.
2. Next to **Available**, click the **X** icon.

   A security message appears.
3. Click **Yes** to remove the user.

   The specified user is deleted.

If a user or role is deleted in the Pentaho Repository, content that refers to the deleted user, either by way of owning the content or having an ACL that mentions the user or role, is left unchanged. This situation makes it possible to create a new user or role using an identical name. In this scenario, content ownership and access control entries referring to the deleted user or role now apply to the new user or role. To avoid this problem, disable a user or role to prevent the creation of a user or role with an identical name. Use these alternatives rather than deleting the user or role.

| If...                    | Then...                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| You are disabling a role | Unassign all current members associated with the role.                                                          |
| You are disabling a user | Reset the password to a password that is so cryptic that it is impossible to guess and is unknown to any users. |
