# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/jira/jira-permissions.md

# Jira Permissions

* **Permission name:** May differ, depending on your version of Jira. For on-premises Jira the permissions interface is similar to Jira Cloud, but the might look slightly different.
* **Project permissions:** Are configured in the project administration page and may differ, depending on their project permission scheme.
* **Cloud Jira:** Has specific team-managed projects, where permissions are defined for roles and then roles are assigned to users. Role permissions are similar to project level permissions defined in the permission scheme.\
  **Settings > Projects > Target Projects > Project Settings > Access > Manage Users/Roles**
* **Default permission scheme:** Grants access to add-on for all the members of administrators and developers groups. No additional configuration is required in this case.

## Project Level Permissions

To change, go to **Settings > Projects > Target Projects > Project Settings > Permissions**.

| **Permission Name** | **Code**            | **Purpose / Required For**                                                                   |
| ------------------- | ------------------- | -------------------------------------------------------------------------------------------- |
| **Browse Projects** | `BROWSE_PROJECTS`   | <p>- Viewing project information<br>- Searching projects<br>- Accessing project settings</p> |
| **Create Issues**   | `CREATE_ISSUES`     | <p>- Creating new issues<br>- Bulk issue creation</p>                                        |
| **Edit Issues**     | `EDIT_ISSUES`       | <p>- Updating existing issues<br>- Transitioning issues</p>                                  |
| **Comment Issues**  | `ADD_COMMENTS`      | - Adding comments to issues                                                                  |
| **Close Issues**    | `TRANSITION_ISSUES` | <p>- Closing/resolving issues<br>- Changing issue status</p>                                 |
| **Assign Issues**   | `ASSIGN_ISSUES`     | <p>- Changing issue assignees<br>- Assigning during issue creation</p>                       |

## Global Permissions

To change, go to **Settings > System > Global Permissions**.

| **Permission Name** | **Code**       | **Purpose / Required For**                             |
| ------------------- | -------------- | ------------------------------------------------------ |
| **Browse Users**    | `BROWSE_USERS` | <p>- Searching users<br>- Viewing user information</p> |

## Additional Jira Cloud Requirements

To ensure a successful integration with Jira Cloud, the user whose credentials are used during the connector integration process, must have the **User** role for the relevant Jira product.

Most Jira projects are associated with either Jira Software or Jira Service Management. To prevent integration issues, assign the **User** role to the user for both products. This role provides the necessary permissions to make API calls.

**To check your user role:**

1. Sign in to Jira Cloud as an administrator.\
   Make sure you have the required permissions to manage users.
2. Go to **Settings** > **User Management**.
3. Search for the user whose credentials are used in the connectors.
4. Select the username to open their profile.
5. Under **Product Access**, confirm that the user has access to the relevant Jira product.
6. Verify that the user role is set to **User** for the applicable product.
