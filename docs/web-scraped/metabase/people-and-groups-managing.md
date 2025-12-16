# Source: https://www.metabase.com/docs/latest/people-and-groups/managing

<div>

1.  [Home](/docs/latest/)
2.  [People and Groups](/docs/latest/people-and-groups/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# People and groups

People can have [accounts](#creating-an-account) in Metabase, and those accounts can be members of [groups](#groups). These groups are used to define [permissions](../permissions/introduction). People can be in multiple groups.

> This page covers accounts people use to log in to *your* Metabase(s). These accounts are distinct from [Metabase *store* accounts](https://store.metabase.com), which are used to manage paid Metabase plans.

## Managing people and groups

To start managing people and groups:

Hit Cmd/Ctrl + K to bring up the command palette and search for "People". Click on the **People** settings result.

Or

Click on the **gear** icon \> **Admin settings** \> **People**. You'll see a list of all the people in your organization.

![Admin menu](images/AdminBar.png)

## Creating an account

Admins can add people to their Metabase. To add a new person manually, click on the gear icon and select **Admin settings**. Under the **People** tab, click **Invite someone** in the upper right corner. You'll be prompted to enter their email, and optionally their first and last names--only the email is required.

Click **Create** to activate an account. An account becomes active once you click **Create**, even if the person never signs into the account. The account remains active until you [deactivate the account](#deactivating-an-account). If you're on a Pro or Enterprise Metabase plan, all active accounts will count toward your user account total. If one person has more than one account, each account will count toward the total (see [how billing works](../cloud/how-billing-works)).

If you've already [configured Metabase to use email](../configuring-metabase/email), Metabase will send the person an email inviting them to log into Metabase. If you haven't yet setup email for your Metabase, Metabase will give you a temporary password that you'll have to manually send to the person.

To create accounts with SSO, check out [authentication options](./start#authentication).

## Editing an account

You can edit someone's name and email address by clicking the three dots icon and choosing **Edit user**.

> Be careful: changing an account's email address *will change the address the person will use to log in to Metabase*.

## Adding a user attribute

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

User attributes is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

To add a user attribute manually:

1.  Go to **Admin settings** \> **People**.
2.  Find the person's account and click the **three dot** (...) menu.
3.  Click **Edit user**.
4.  Click **+ Add an attribute**.
5.  Add the name of the user attribute under "Key". For example, "Department".
6.  Add the value that applies to the specific person. For example, "Engineering".
7.  Optional: [create a group](#creating-a-group) to organize people who will get row and column security.
8.  Add the person to the group.

You can also sync user attributes from your identity provider [via SSO](./start#authentication).

User attributes are required for [row and column security](../permissions/row-and-column-security) permissions.

You can also employ user attributes to specify what database role Metabase should use when that person queries a database. Check out [impersonation access](../permissions/data#impersonated-view-data-permission).

## Deactivating an account

To deactivate someone's account, click on the three dots icon on the right of a person's row and select **Deactivate** from the dropdown. Deactivating an account will mark it as inactive and prevent the user from logging in - but it *won't* delete that person's saved questions or dashboards.

If you're using SSO, you should deactivate the account in Metabase as well as your IdP (that is, deactivation doesn't get applied from Metabase to your IdP, and vice versa).

![Remove a user](images/RemoveUser.png)

To reactivate a deactivated account, click the **Deactivated** radio button at the top of the people list to see the list of deactivated accounts. Click on the icon on the far right to reactivate that account, allowing them to log in to Metabase again.

## Deleting an account

Metabase doesn't explicitly support account deletion. Instead, Metabase deactivates accounts so people can't log in to them, while it preserves any questions, models, dashboards, and other items created by those accounts.

If you want to delete an account because the account information was set up incorrectly, you can deactivate the old account and create a new one instead.

1.  Change the name and email associated with the old account.
2.  [Deactivate](#deactivating-an-account) the old account.
3.  [Create a new account](#creating-an-account) with the person's correct information.

## Checking someone's auth method

Search for a person and look for an icon beside their name.

-   If they log in using Google credentials, Metabase displays a Google icon.
-   If they log in using an email address and password stored in Metabase, no icon is shown.

Note that the type of user is set when the account is first created: if you create a user in Metabase, but that person then logs in via Google or some other form of SSO, the latter's icon will *not* show up next to their name.

## Resetting someone's password

If you've already [configured your email settings](../configuring-metabase/email), people can reset their passwords using the "forgot password" link on the login screen. If you haven't yet configured your email settings, they will see a message telling them to ask an admin to reset their password for them.

To reset a password for someone, just click the three dots icon next to their account and choose **Reset Password**. If you haven't [configured your email settings](../configuring-metabase/email) yet, you'll be given a temporary password that you'll have to share with that person. Otherwise, they'll receive a password reset email.

## Resetting the admin password

If you're using Metabase Cloud, [contact support](/help-premium) to reset your admin password.

If you're a Metabase admin and have access to the server console, you can get Metabase to send you a password reset token:

1.  Stop the running Metabase application.

2.  Restart Metabase with `reset-password email@example.com`, where "email@example.com" is the email associated with the admin account:

    ::: 
    ::: highlight
    ``` highlight
    java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar reset-password email@example.com
    ```
    :::
    :::

3.  Metabase will print out a random token like this:

    ::: 
    ::: highlight
    ``` highlight
    ...
    Resetting password for email@example.com...

    OK [[[1_7db2b600-d538-4aeb-b4f7-0cf5b1970d89]]]
    ```
    :::
    :::

4.  Start Metabase normally again (*without* the `reset-password` option).

5.  Navigate to it in your browser using the path `/auth/reset_password/:token`, where ":token" is the token that was generated from the step above. The full URL should look something like this:

    ::: 
    ::: highlight
    ``` highlight
    https://metabase.example.com/auth/reset_password/1_7db2b600-d538-4aeb-b4f7-0cf5b1970d89
    ```
    :::
    :::

6.  You should now see a page where you can input a new password for the admin account.

## Unsubscribe from all subscriptions and alerts

This action will delete any dashboard subscriptions or alerts the person has created, and remove them as a recipient from any other subscriptions or alerts.

This action doesn't affect email distribution lists that are managed outside of Metabase.

## Default user accounts

Metabase includes default user accounts to handle various tasks. We're documenting these accounts here so you know they're legitimate accounts and not someone trying to spy on your Metabase. Some things to know about them:

-   Customers are not charged for these accounts.
-   No one can log in to these user accounts.
-   Metabase excludes these user accounts from the **Admin settings** \> **People** tab.

### Anonymous user account

-   ID: 0
-   First name: External
-   Last name: User
-   Email: null

Metabase uses this anonymous user account to identify anonymous views, for example views of a [public question or dashboard](../embedding/public-links). This account is a virtual user: the account doesn't exist in the application database. You'll see this account show up in [usage analytics](../usage-and-performance-tools/usage-analytics).

### Metabase internal account

-   ID: 13371338
-   First name: Internal
-   Last name: Metabase
-   Email: internal@metabase.com

Metabase uses this account to load content into Metabase (like the [Usage analytics](../usage-and-performance-tools/usage-analytics) collection). You may see this `internal@metabase.com` account in the logs.

## Groups

To determine [who has access to what](../permissions/start), you'll need to

-   Create one or more groups.
-   Choose which level of access that group has to different databases, collections, and so on.
-   Then add people to those groups.
-   (Optional) promote people to [group managers](#group-managers).

To view and manage your groups, go to the **Admin Panel** \> **People** tab, and then click on **Groups** from the side menu.

![Groups](images/groups.png)

### Special default groups

Every Metabase has two default groups: Administrators and All Users. These are special groups that can't be removed.

#### Administrators

To make someone an admin of Metabase, you just need to add them to the Administrators group. Metabase admins can log into the Admin Panel and make changes there, and they always have unrestricted access to all data that you have in your Metabase instance. So be careful who you add to the Administrator group!

#### All users

The **All Users** group is another special one. Every Metabase user is always a member of this group, though they can also be a member of as many other groups as you want. We recommend using the All Users group as a way to set default access levels for new Metabase users. If you have [Google single sign-on](./google-sign-in) enabled, new users who join that way will be automatically added to the All Users group.

It's important that your All Users group should never have *greater* access for an item than a group for which you're trying to restrict access --- otherwise the more permissive setting will win out. See [Setting permissions](../permissions/start).

## Creating a group

Go to **Admin settings** \> **People** \> **Groups**, and click the **Add a group** button.

We recommend creating groups that correspond to the teams your company or organization has, such as Human Resources, Engineering, Finance, and so on. By default, newly created groups don't have access to anything.

To remove a group, click the X icon to the right of a group in the list to remove it (remember, you can't remove the special default groups).

## Adding people to groups

To add people to that group, click into a group and then click **Add members**.

To remove someone from that group, click on the **X** to the right of the group member.

You can also add or remove people from groups from the **People** list using the dropdown in the **Groups** column.

## Group managers

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Group managers is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (both self-hosted and on Metabase Cloud).

**Group managers** can manage other people within their group.

Group managers can:

-   Add or remove people from their group (that is, people who already have accounts in your Metabase).
-   View all people in the **Admin settings** \> **People** tab.
-   Promote other people to group manager, or demote them from group manager to member.
-   Rename their group.

Group managers are not admins, so their powers are limited. They cannot create new groups or invite new people to your Metabase.

## Promoting/demoting group managers

To promote someone to become a group manager:

1.  At the top right of the screen, click the **gear** icon \> **Admin settings** \> **People** \> **Groups**.
2.  Select the group you want the person to manage. If the person isn't already in the group, you'll need to add that person to the group.
3.  Find the person you want to promote, hover over their member type, and click the up arrow to promote them to group manager. If you want to demote them, click on the down arrow.

## Further reading

-   [Configure Single Sign-On (SSO)](./start#authentication).
-   [Permissions strategies](/learn/metabase-basics/administration/permissions/strategy).
-   [Embedding permissions](../permissions/embedding).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/people-and-groups/managing.md) ]