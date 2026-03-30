# Source: https://docs.curator.interworks.com/site_content_design/menus/restrict_access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Restrict Access

> Control menu visibility and access permissions based on user groups and roles to secure content appropriately.

When you add a Dashboard or other content brought in from connected integrations like Tableau, Curator will inherit the
security settings from those integrations. However, you may want to override those source-systems or you may want to prevent
users from seeing content that exists solely within Curator - for example, restricting access to a specific
[page](/site_content_design/pages/pages_overview).  With **Restrict Access**
you can override inherited security settings when necessary, offering you maximum flexibility over the visibility of content.

## Enabling Restrict Access

1. On the backend of Curator, navigate to the **Content** > **Reorder Navigation** section from the left-hand menu.
2. Find the menu link you'd like to restrict access to and click the pencil/edit icon - or click the "New Menu Link"
   button to create a new menu item.
3. Toggle the Restrict Access to ON to display a list of [groups](/users_groups/user_management/users_and_groups_overview)
4. Select the groups you'd like to grant access to
5. Save the menu item

You can then confirm the restrict access is enabled on the Reorder Navigation page by hovering over the lock icon and
seeing the phrase "Restricted Access based on Group Membership"

**Tableau admins** automatically have access to all Tableau-connected content in Curator.  Restrict access overrides
these permissions, so admins will need to be in one of the selected groups to see the content within the menu.
