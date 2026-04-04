# Source: https://docs.curator.interworks.com/users_groups/user_management/user_sync_and_membership_sync_overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Sync and Membership Sync Overview 

> Overview of user synchronization and membership sync processes between Curator and external authentication systems.

There are two different sync process that run in Curator: the user sync and the group membership sync. There used to be
one sync that did both, but we found bringing over every user and group resulted in very slow syncs and a lot of
redundancy. Separating the one sync into two has led to much greater efficiency but some confusion. This doc aims to
answer frequently asked questions about these syncs and will be updated as new questions are asked.

First, a quick primer on both syncs:

1. **User Sync**:
   * **What is it?**
     The user sync brings user details from your analytic platforms to Curator. This includes full display name, email
     address, user roles, etc. This does not include group membership.
   * **When does it happen?**
     The user sync always happens on login. You can also manually sync a specific user's details from the Curator
     backend > Settings > Users > Frontend Users > select a specific user and use the buttons in the "Platform Users"
     section to sync the details.
     *Note: If the user doesn't exist on Curator the user sync will create it. This results in having a lean user base of
     only the true Curator users.*
     *Note: You cannot disable the on-login user sync.*
2. **Group Membership Sync**:
   * **What is it?**
     The group membership sync builds Curator Frontend Group membership from a user's platform group membership. For
     instance, you can create an "Admins" Frontend Group in Curator and, instead of manually selecting numerous users, you
     can select the "Admins" group from one of your platform connections and Curator will automatically put those users in
     the Curator Frontend Group. This does not include user details.
     *Note: This is only relevant if you use Curator Frontend Groups for restricting access in the navigation or for
     Frontend Group Overrides. If you don't use these features then group membership is irrelevant to Curator.*
   * **When does it happen?**
     The group membership sync will happen on login by default. Some platforms can have slow response times when Curator
     requests the relevant membership, so you can disable the on-login membership sync to speed up the login. If you
     disable the on-login membership sync you can enable a sync to occur on a scheduled cadence to ensure users are in
     their groups by the time they login.
     *Note: If you disable the on-login membership sync, the scheduled membership sync will create users if they don't
     already exist on Curator. This is to preemptively ensure the user has their groups before logging in, which requires a
     Curator user. This is the **only scenario** where the group membership sync also syncs user details.*

**Where are my Users?**
You can find your Frontend Users at the Curator Backend > Settings > Users > Frontend Users. This page will also show the
associated platform-specific users.

**Where are my Groups?**
You can find your Frontend Groups at the Curator Backend > Settings > Users > Frontend Groups. You can trigger syncs and
change sync settings from this page.

**Why would I create groups?**
The primary features that leverage Curator Frontend Groups are:

1. **[Restrict Access](/site_content_design/menus/restrict_access)**
   You can deny permission to see content in Curator by restricting access in the navigation based on group membership. This
   is especially helpful for content created in Curator that doesn't have permissions to pull from an analytic platform (i.e.
   Pages, Files, external URL's, etc.). This can also be useful if your navigation has many items and the permission checks
   add copious load time by restricting access to a high-level menu item, which automatically denies access to all of the
   item's children.
2. **Frontend Group Overrides**
   Overrides are useful if you have groups of users who require a different look-and-feel in the Curator frontend. This is
   common if you have groups/departments or multiple tenants who use different logos, colors, etc. You can also present
   entirely different navigation structures and homepages to your various groups.

**How do I create groups?**
You can create a Frontend Group at Curator Backend > Settings > Users > Frontend Groups by using the "New Frontend Group"
button. You can build membership by either manually selecting uses from the "Group Membership" section or by using a group
from one of your connected analytic platforms. For instance, you can create an "Finance" group that uses a Tableau Group
and ThoughtSpot Group instead of manually selected every use who needs to see finance content.

**Curator used to automatically create Frontend Groups that were in Tableau, but not anymore. Why not?**
If your Curator instance doesn't leverage restricted access by group or Frontend Group Overrides then Tableau Groups are
irrelevant to Curator and syncing them is unnecessary. Even if you do use a couple Tableau Groups for Curator Frontend
Groups you don't need all of them. Now Curator's membership syncs are much leaner and more efficient, resulting in the
same functionality with much better performance.

**I created a user in Tableau, but it doesn’t show they are synced in Curator. How do I get Curator to sync a user?**
The user will be synced to Curator as soon as they log in. Users are always synced during login.
*Caveat: Tableau uses unique user records for each Site they are a member of. To avoid long login times, Curator only
syncs the Tableau User from the Site you've specified in the REST connection (Curator backend > Integrations >
Connections). The other Site users will be synced on a daily cadence.*
*Caveat to the caveat: If you've enabled the Tableau Repository connection every Site user will be synced on login.
Repository queries are much faster than REST API calls so the login time isn't as affected.*
