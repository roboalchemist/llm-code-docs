# Source: https://docs.curator.interworks.com/users_groups/user_security/frontend_user_permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Frontend User Permissions

> Configure and manage user access permissions for different content types and features within Curator.

In order to manage permissions on Curator, there are a few different ways to control access to content - it's largely
dependent upon which content type you're working with.  First, we'll begin with troubleshooting permission to discover
what a user should have access to.  Below that you'll find specific instructions on how to set permissions on specific content-types.

## Preview An Individual User's Access

In order to see what permissions a user has on Curator, you can preview a user's access via the Menu system.

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Settings** > **Users** > **Frontend Users** section from the left-hand menu.
3. Find the user that you would like to preview access for and click on the line containing their username.
4. On the Frontend User page click the "User Menu Access" button to view the a preview of the user's menu.  An icon next
   to each menu-link will show whether or not the user has access, and on hover will provide a reasoning why.

## Manage Permissions to Curator Content

Curator content does not have any inherent permissions - all automatic permissions are inherited from source systems that
Curator is connected to (e.g. Tableau permissions for embedded dashboards).  Creating a page without any embedded
analytic-content will result in global access for all your users.

When it comes to inheritance via the Menu, there is an exception to visible content: **Dropdown Placeholders** will only
display if the user has permissions to at least one item nested beneath the Dropdown.  If the user has access to none
of the items beneath the dropdown, it will not be visible to that user.  However, if you wish to apply permissions to a
specific piece of content, you can create a menu-link for that content and use the Group-based
[Restrict Access](/site_content_design/menus/restrict_access) option.  You
can find the steps below:

1. Navigate to the backend of the system (e.g. `https://www.curatorexample.com/backend`).
2. Navigate to the **Content** > **Navigation** section from the left-hand menu.
3. Click on the "+ New Menu Link" button to create a new menu item.
4. Fill out the form to select the content you'd like to link to, then scroll to the bottom of the page and enable the
   **[Restrict Access](/site_content_design/menus/restrict_access)** toggle.
5. Check the boxes next to the groups you would like to grant permission to.  **NOTE**: If you do not see any groups,
   see our [Groups document](/users_groups/user_management/users_and_groups_overview)
   on how to add new Frontend Groups.
6. Save the menu item to apply permissions.

With that said, if you would like Curator to assume all content is restricted by default, you can enable it globally by
visiting **Settings** > **Security** > **Authentication Settings** > **Customization** section >
**[Restrict Access](/site_content_design/menus/restrict_access) is Always Enabled**
setting.  You will still need to add groups to each piece of content to allow
users to access them.

## Manage Permissions to Analytic Content

When adding content from a source system (e.g. Tableau) Curator will automatically check the Analytic Connection when a
user logs in to determine their access.  If a user has been granted access in the source-system (e.g. Tableau Server),
then they will have access to it in Curator.  You can override these permissions using the steps in the
*Manage Permissions to Curator Content* above.

### Disabling security to preview content

You can expose all links to analytic content in Curator to your users by bypassing the initial security check, but then
expose an "access denied" message when they visit links.  For steps on how to set that up, see
[Preview Security Settings](users_groups/user_security/disabling_link_preview_security).

### Troubleshooting Access

If you believe a user is getting an incorrect permission-denial, visit the Event Logs on the backend and search the logs
for either "403" or the user's username.  Each time a user is denied access to a page Curator logs the reason why under
a 403 error.
