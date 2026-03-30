# Source: https://docs.qodo.ai/qodo-documentation/management-portal/users.md

# Users

The **Users** page lists everyone with access to your Qodo account, including their role, team, and status. You can filter by team, search by name or email, and use the actions menu to manage individual users. Available information and actions depend on your plan and role.

#### Who can access this page?

* **Enterprise**
  * Organization admins can view and manage all users.
  * Team owners can view and manage users within their teams.
* **Team and Free plans**
  * Team owners can view and manage users.
  * Team members and standalone users can view only their own information.

<figure><img src="https://2742973941-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnoDWMoicsI0VwDtqoKja%2Fuploads%2Fn7yuSq1TsBBRNqMtrj3T%2FUser%20management%20interface%20with%20blurred%20emails.png?alt=media&#x26;token=cab10524-71a7-466a-9328-2b02d4fdf665" alt=""><figcaption></figcaption></figure>

#### Users table columns

| Column              | Description                                            |
| ------------------- | ------------------------------------------------------ |
| Email               | The user’s login email address.                        |
| User name           | The user’s unique identifier.                          |
| Last login          | The last time the user logged in to Qodo.              |
| Status              | Indicates whether the user has completed registration. |
| Linked Git accounts | Shows whether a Git provider is connected.             |
| Team name           | The team the user belongs to, or **No team**.          |
| Team role           | Team owner or member.                                  |
| Actions             | Available actions based on your permissions.           |

#### Auto-generate user name

{% hint style="info" %}
This setting is available only on Enterprise plans and can be managed by organization admins.
{% endhint %}

Organization admins can control how user names are generated.

When **Auto-generate user name** is enabled, user names are automatically derived from email addresses (for example, `john.smith@company.com` → `john.smith`). User names are used to identify users in third-party systems, such as Git providers.

You can enable or disable this setting using the **Auto-generate user name** toggle at the top of the **Users** page.&#x20;

#### View user details

Selecting **View** from a user’s Actions menu opens a details panel displaying information about the selected user.

#### Export to CSV

From the three-dot menu in the top-right corner of the Users page, select **Export CSV** to download the users list as a CSV file.

#### Invite team members

{% hint style="success" %}
Available to team owners and organization admins.
{% endhint %}

To invite users to a team:

1. Navigate to the **Users** page.
2. In the top-right corner of the page, click **Invite members**.
3. Enter one or more email addresses.
4. (Optional) Upload a file to invite users in bulk.
5. Click **Invite** to send the invitation.

A user can belong to only one team.

#### Remove team members

Removing members is supported only for [**invite-only organizations**.](https://docs.qodo.ai/qodo-documentation/management-portal/invite-only-organizations)

1. Click the **Actions** menu (three vertical dots) next to the user you wish to remove.
2. Select the **Delete** (trash can) icon to remove the member.

#### Edit user roles and assignments

Depending on your role, you can update:

* Organization role (Enterprise only).
* Team assignment
* Team role

A user can belong to only one team.

**To edit a user:**

1. Within the user details page, update any of the editable fields (user name, organization role, team name, or team role).
2. Click **Update** to save your changes.

#### Who can remove users?

Users can be removed from the account based on your permissions.

* Organization admins can remove any user.
* Team owners can remove users from their team.
