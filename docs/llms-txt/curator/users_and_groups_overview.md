# Source: https://docs.curator.interworks.com/users_groups/user_management/users_and_groups_overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users and Groups Overview

> Comprehensive guide to user management in Curator covering frontend users, groups, permissions and authentication methods.

## Frontend Users

"Frontend users" (or local Curator users) are responsible for bringing together your various platforms to create
individual frontend experiences. These users are matched based on their usernames, so it's crucial to ensure consistent
naming across your connected systems - if you do not have them matched exactly, see our [Username Mapping guide](/users_groups/user_management/username_mapping).

To view the list of frontend users, go to the backend and navigate to **Settings** > **Users** > **Frontend Users** from
the left-hand menu. Each user who has signed into Curator will have a corresponding record. Clicking on a user record
will display details about that user, including any connected platforms.

You can also get a [preview of the user's navigation](/users_groups/user_security/frontend_user_permissions)
near the top of this page.

## Platform Users

"Platform users" refer to the records maintained by Curator for users synced from your connected systems (e.g., Tableau
users, ThoughtSpot users, etc.). These platform users store synced information from the respective systems, which can be
leveraged by the Frontend User for permissions and platform-specific actions like favoriting or subscribing to a Tableau
Dashboard.

To access the list of platform users, go to the backend and navigate to
**Curator Backend** > **Settings** > ***\[PlatformName]*** > ***\[PlatformName] Users*** from the left-hand menu.
Some systems may have multiple records per user if they have multiple IDs
(e.g., Tableau has a user record with unique IDs ***per site***). Clicking into a user record will provide more details
about that user. You can also [sync a specific platform user](/users_groups/user_management/user_sync_and_membership_sync_overview)
from this page.

## Frontend Groups

Frontend groups are created within Curator and serve functionalities such as
[restricting access](/site_content_design/menus/restrict_access)
to navigation items or [overriding frontend styles based on group membership](/site_content_design/theme/group_overrides).
To access these groups, go to the backend and navigate to **Curator Backend** > **Settings** > **Users** > **Frontend Groups**.

### Creating Frontend Groups

Membership for frontend groups can be established by manually selecting users or by choosing one or more groups from
other platforms. If a group from another platform is chosen, the membership will automatically be reflected in the
frontend group.

For example, let's say you create a group called "Tableau Users" and select the "All Users" group from your Tableau
Server's default site. In this case, any user who logs in and has a Tableau user account from that site will be
automatically added to the "Tableau Users" frontend group.

#### Batch Create

If you want to create multiple Frontend Groups associated with one platform group each, you can use the batch create
functionality instead of repeating the create process:

1. Go to **Curator Backend** > **Settings** > **Users** > **Frontend Groups**.
2. Click the "Batch Create" button.
3. Select the sources from which you want to pull groups. This action doesn't create Frontend Groups; it only pulls in
   a list of available groups from the selected sources.
4. Click "Preview Available Frontend Groups".
5. Check the boxes next to each group you want to create. If you're having trouble finding the desired groups,
   you can sort the table by clicking on the column headers

## User and Membership Syncing

Curator needs to make API calls to your various platforms to keep the platform user information up to date.
This happens when a user logs into Curator to ensure they have the most current information. At the same time,
Curator checks if the user is in any platform groups associated with a frontend group and updates the membership accordingly.

Curator also provides the option to run a scheduled group sync for all frontend groups. You can find the settings for
this at **Curator Backend** > **Integrations** > **Global Settings**. By default, you can keep this set to "Never" as
the membership is updated on login.

Sometimes, the login process can be slow because the platform takes time to respond with the group information. If this
is the case, there is a feature called "Skip User Group Sync on Login" in **Integrations** > **Global Settings**.
Enabling this feature will skip the membership sync on login and only perform the platform user sync, which tends to be
quick across systems. When this feature is enabled, new users will be created during the scheduled group sync to ensure
they are already in their groups when they first log in to Curator.

***Note:*** We recommend **not** disabling the on-login membership sync unless the Curator login process is very slow.
Allowing the sync to happen on login ensures the most current membership for your users.

***Note:*** If you disable the on-login sync, you also **need to ensure a scheduled group sync is configured** to run.
Ideally, you should do this during low usage hours (e.g., midnight) to ensure group membership is fully synced by the
time users log in.
