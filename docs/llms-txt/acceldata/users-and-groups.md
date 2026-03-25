# Source: https://docs.acceldata.io/documentation/users-and-groups.md

# Users and Groups

ADOC provides comprehensive tools for managing users and organizing them into groups for streamlined access control.
 With **Users & Groups**, administrators can:

- Add and manage individual user accounts
- Organize users into logical groups
- Assign roles and permissions to entire groups instead of individuals
- Monitor account activity and quickly manage user access

By leveraging groups, organizations can simplify administration, improve security, and ensure consistency in permissions across teams.

## 1. User Management

The User Management page provides a complete view of all users in your ADOC account. It allows administrators to manage users, invite new ones, assign roles and groups, and monitor their activity.

Accessing User Management

1. Click **Settings** from the left navigation pane.
2. Select **User Management**.

The Users table in the User Management section provides key details about each user in your ADOC account. It displays the user's full name and email ID under **Name & User ID**, along with their **Status** indicating whether they are active or inactive. The **Tenant Roles** column shows roles assigned at the tenant level, such as **Admin**, **Owner**, **Viewer**, or any custom-defined roles. The **Groups** column lists the group(s) the user belongs to, and the **Last Login** column captures the most recent timestamp when the user accessed the system.

When you click the ellipsis (⋮) menu on the far-right side of a user row, two actions appear:

- **Active Toggle**: This switch allows an admin to quickly activate or deactivate a user. If a user is set to **Inactive**, they will not be able to access the platform.
- **Edit**: Selecting **Edit** opens the **Edit User** page, where admins can update user details like first name, last name, status, roles, groups, or send a password reset email.

### Inviting Users

Admins can add users to the platform by sending them an invitation email. The Invite User button is located at the top right of the Users tab.

Steps to Invite Users:

1. Click the **Invite User** button.
2. Enter one or more email addresses, separated by commas.
3. Select the roles and groups to assign to the invited users.
4. Click **Review** to verify the entered details.
5. Click **Send Invites**.

Note If an email is invalid or the user already exists in the system, an error message will be displayed.

Once a user accepts the invitation and signs up, they will appear in the Users table with their assigned roles and groups. You can also **search for users using the search bar** at the top of the page to quickly locate specific accounts.

## 2. Groups

Groups are a way to organize users and manage their access collectively. Instead of assigning roles to individual users one by one, you can add users to a group and apply roles at the group level—making role and permission management easier, especially as teams scale.

The Groups tab displays a list of all existing user groups along with key details such as the **group name** (e.g., DefaultGroup, Report Group, dom_ug), the **number of roles and users assigned to each group** (e.g., Roles: 1, Users: 1), **who created the group**, and **who last updated it along with the timestamp**. This information helps admins track changes and manage group access efficiently.

You can also use the search bar to quickly locate groups by name.

### Creating a User Group

To create a new group:

1. Navigate to the **Groups** tab under **User Management**.
2. Click **Create User Group** (blue button on the right).
3. Enter a unique group name (e.g., data-team-west).
4. Select users to include and assign one or more roles to the group.
5. (Optional) Add a description to clarify the group’s purpose.
6. Click **Save**.

Once created, the group will appear in the Groups table, showing the number of users and roles it contains.

### Group Detail View

Clicking on a group opens a **detailed panel** on the right-hand side. This panel provides a complete overview of the group’s configuration:

- **Tenant Roles**: Displays how many global (tenant-level) roles are associated with this group.
- **Users**: Lists the users added to the group. You’ll see the usernames or email addresses of assigned members.
- **Domain Role Mappings**: Allows you to assign roles for specific domains, giving you more granular control.
- **Activity**: 

Shows metadata such as:

- **Created By / On**: Who created the group and when.
- **Last Updated By / On**: Who made the most recent changes and the timestamp — useful for audits and tracking.

You can also **Edit** or **Delete** the group from this view.

**Why Use Groups?**

- **Access Control**: Assign permissions to multiple users in one action.
- **Collaboration**: Structure teams logically (e.g., Analytics Team, DevOps, QA) with appropriate access.
- **Scalability**: As teams grow, simply add new users to the right groups.
- **RBAC-Aligned**: Consistent with role-based access control principles, making permissions easy to audit.

---

## Best Practices

- Assign at least one role to every user. Without a role, the user cannot access platform features.
- Use group-based role assignments. Add users to groups and assign roles at the group level to reduce repetitive work.
- Organize groups logically. Base them on teams, functions, or projects for easier management.
- Document group purposes. Add clear descriptions to help with audits and onboarding.
- Deactivate instead of deleting. Preserve history while preventing access.
- Review regularly. Remove unused groups or inactive accounts to keep the system clean.

---

## FAQs

**What happens if I deactivate a user?**

They immediately lose access, but their roles and groups are preserved for reactivation.

**Can a user be in multiple groups?** 

Yes. Permissions from all groups are combined. 

**If I change a group’s roles, does it affect all members?**

Yes. All members inherit the updated roles instantly.

**Can I remove a user from a group without deleting their account?**

Yes. Removing them only changes their group-based access.

**How can I track who changed a group?**

Open the group’s detail view and check the Activity section for audit history.