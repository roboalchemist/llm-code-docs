# Source: https://docs.jit.io/docs/managing-users.md

# Users and Permissions

Users & Permissions has the following tabs:

* Users, where you can invite new users, edit roles, force logout or delete users.
* Audit Logs, which displays audit logs which can also be downloaded.
* API Tokens, which displays API token metadata and also allows you to generate new API tokens that can be used to access Jit APIs, for example from CLI scripts.

## User roles and permissions

[block:parameters]
{
  "data": {
    "h-0": "Role",
    "h-1": "Permissions",
    "0-0": "Admin",
    "0-1": "Invite members  \nChange users roles. For example, from Member to Admin  \nCreate API tokens and define where they are used  \nPerform all options and actions on the Jit platform",
    "1-0": "Engineering Manager",
    "1-1": "Activate teams and view their My Teams data",
    "2-0": "Member",
    "2-1": "All options and actions on the Jit platform apart from inviting members and creating tokens",
    "3-0": "Developer",
    "3-1": "View specific pages via links"
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]

## Accessing Users & Permissions

Go to the left menu, scroll to **Settings** and then to **Users and Permissions**.

![](https://files.readme.io/d49e97f-image.png)

| Field       | Description                        |
| :---------- | :--------------------------------- |
| Invite User | Invite a user with Jit permissions |
| User        | User with Jit permissions          |
| Roles       | See Roles & Permissions above      |
| Joined      | Date and time of the first login   |
| Last seen   | Date and time of last login        |

### Inviting new users

1. Click **Invite User**.

   ![](https://files.readme.io/3190d95-image.png)

2. Click **Copy Invite Link**.

3. Optional: Click **Edit**, select a new expiration date and then click **Save**.

   ![](https://files.readme.io/8bf14d4-image.png)

4. Copy the **invite** and send the link to the new user. We recommend sending the link via Slack.

5. Optional: To deactivate a link after it has been sent, repeat steps 1 to 3 above and then click **Deactivate link**.

### Displaying User management audit logs

1. Go to **User Management**  and select **Audit Logs**.

   ![](https://files.readme.io/436f6be-image.png)
2. Click **Download** to download an Audit Log data.

### Generating API tokens

1. Go to **Users & Permissions**and  select **API Tokens**.

   ![](https://files.readme.io/7f8fed0-image.png)
2. Click **Generate Token**.

   ![](https://files.readme.io/a8fe4e1-image.png)
3. Complete the **Description** field, select a **role** and then click **Create**.

   ![](https://files.readme.io/27155c9-image.png)
4. Copy the **Client ID** and **Secret Key**.
5. We recommend using GitHub secrets when using Jit APIs.  Go to **GitHub**,  and in the repo running **GitHub Actions secrets and variables**, click **New repository secret** and paste the **secret**.

   ![](https://files.readme.io/0c42426-image.png)