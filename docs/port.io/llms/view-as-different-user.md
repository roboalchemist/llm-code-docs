# Source: https://docs.port.io/sso-rbac/users-and-teams/view-as-different-user.md

# View as a different user

Port's "View as" feature enables administrators to validate and troubleshoot user permissions without switching accounts or requesting credentials. This capability is essential when implementing dynamic filters, permission rules, or role-based access controls that depend on the logged-in user's context.

Each "View as" session is bound to a specific browser tab, allowing you to maintain multiple views simultaneously, one as your admin user to modify configurations, and another as a member user to see the immediate impact of your changes.

Using this feature, you can verify exactly what a specific user can see and do within the portal, including:

* Accessible pages and catalog views
* Entity creation and deletion permissions
* Self-service actions available for execution or approval
* Applied dynamic filters and data visibility

## Access the feature[â](#access-the-feature "Direct link to Access the feature")

There are two ways to access the "View as" feature:

**Option 1: From the navigation bar**

1. Navigate to your [Port portal](https://app.getport.io).
2. Click on the ![](/img/icons/show-icon.svg)![](/img/icons/show-icon-dark.svg) button in the top right corner of the page.
3. Choose the user type you want to view as from the dropdown list.
4. Click `View`.

**Option 2: From a user entity**

1. Navigate to the [Users page](https://app.getport.io/_users) in your catalog.
2. Choose the user you want to view as
3. Click the actions menu `...` on the user entity.
4. Select **View as**.

## Limitations[â](#limitations "Direct link to Limitations")

* This feature is available only for admin users.
* You cannot view as disabled users.
* You cannot edit or delete your original user in a view as session.
* Some sensitive routes (rotate secrets, generate api token, etc.) are blocked and cannot be used in a view as session.

Session lifecycle

When you are viewing Port as a different user, this session is bound to your current browser tab. This is useful for maintaining two different tabs - one as your own user where you can modify your environment configuration (dynamic filters, permissions, etc.) and one as a member user to see the impact of those changes.

## Audit logs[â](#audit-logs "Direct link to Audit logs")

Data modification

When you are in a "view as" session, you can still perform updates or deletes on your data.

Any update or delete operation you perform when viewing as a different user will be recorded in the audit log under your own user, with clear attribution showing that the action was performed during a "view as" session.

The audit log entry will show your username followed by the user you were viewing as.<br /><!-- -->For example: **John Cena** *as Jane Villanueva*
