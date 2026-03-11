# Source: https://docs.axonius.com/docs/changing-dashboard-access-permissions.md

# Changing Dashboard Access Permissions

You can change the access permissions for dashboards.

Each chart in a dashboard also has associated queries with their own permissions. The permissions for these queries are also updated to the same permissions as the dashboard.

<Callout icon="📘" theme="info">
  Notes

  * A shared dashboard can only be edited by a user in the Global data scope.

  * To move a dashboard to Shared access a user must be in the Global data scope.

  * When you change access permissions, the dashboard is moved to the appropriate folder according to the new permissions.
</Callout>

<Callout icon="📘" theme="info">
  Notes

  When you change the access permissions from *Private* to *Public* by selecting **System Access**, if there are underlying chart queries need to be updated as well, Axonius verifies that you have the required permissions to make this change. If you don't have the necessary permissions, a message is displayed informing you that you need additional permissions.
</Callout>

**To edit access permissions of a dashboard:**

1. On the **Dashboards** page, find the dashboard you want to edit in the folders pane and click the 3-dot menu next to the dashboard name. Then select **Edit**.

<Image align="center" alt="DashboardEditMenu.png" border={false} width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardEditMenu.png" />

The Edit Dashboard dialog opens.

2. In [**Who has access**](/docs/who-has-access), configure the access privileges for the dashboard.
3. Click **Save**. When updating permissions to Shared or Public, if necessary, a message is displayed listing the affected charts, the relevant underlying queries, and where the queries are used. Hover over a chart name to see more detailed information about where the query is used. After verifying the changes, click **Change Permissions to Shared/Public** to update the permissions of the dashboard and all underlying queries.

<Image align="center" alt="DashboardPermissionChanges.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardPermissionChanges.png" />

The dashboard is updated and, if necessary, moved to the appropriate folder according to the access permissions you selected, and displayed on the [Dashboards page](/docs/working-with-dashboard-spaces).

See [Performing Actions on Dashboards](/docs/manage-dashboards#performing-actions-on-dashboards) for more options.