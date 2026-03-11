# Source: https://docs.axonius.com/docs/workspaces.md

# Workspaces

Workspaces provide custom, use-case-driven views of the Axonius platform. They act as tailored environments, allowing different users to easily navigate within Axonius and quickly realize value for specific objectives. Upon login, users are presented with a focused interface relevant to their role or the specific use case.

Each workspace includes:

* A custom [left navigation bar](/docs/getting-to-know-the-axonius-interface) featuring the assets and functions most relevant to that specific use case.
* A Home page that is the default landing page for each workspace (except for the Axonius Platform). The Home page displays a dashboard that gives immediate insights on your data, including KPIs and insights on common use cases in the context of the workspace. Each workspace had a default Home page dashboard that is managed by Axonius and cannot be edited or deleted. Admin users can set a different dashboard as the workspace Home page.
* A focused navigation menu that highlights relevant assets and modules to help users focus only on the workspace use cases. While a workspace is a focused environment, all Axonius modules and functionality are available from the More menu at the bottom the the navigation menu.
* A focused asset view on the assets page shows the assets most relevant to the workspace use case.
* Default custom table views of specific assets in some workspaces.

See [Getting to Know the Axonius Interface](/docs/getting-to-know-the-axonius-interface) to learn about the tools available in the top pane of each workspace.

Each workspace has a use-case-focused navigation menu on the left. The main assets and tools related to the workspace each have an icon, and you can navigate directly to their asset pages.

![LeftNavCutout-MoreMenu.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LeftNavCutout-MoreMenu.png)

Once displayed, you may need to scroll to see all the options.

## Accessing a Workspace

You access workspaces from the Workspaces list.

**To access a workspace:**

1. Above the left navigation menu, click **Workspaces** (or the name of the currently selected workspace).

<Image align="center" alt="IdentitiesWorkspaceSelector.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IdentitiesWorkspaceSelector.png" />

2. In the workspace selection box, choose the workspace you want and click **Select**.

<Image align="center" alt="WorkspaceSelectorBox.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WorkspaceSelectorBox.png" />

3. The Home page of the selected workspace is displayed.

<Image align="center" alt="WorkspacesGeneral-1.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workspaces/WorkspacesGeneral-1.png" />

## Changing the Workspace Home Page

Each workspace has a Home page that displays a default dashboard with use-case relevant charts. These dashboards are managed by Axonius and cannot be edited or deleted. However, Admin users can select another dashboard as the Home page dashboard provided that dashboard has "Shared" access privileges. Shared dashboards are listed under the "Shared" folder of the Dashboards page.

### Required Permissions

Admins with the following permissions can change a workspace Home page dashboard:

* In the admin user's role configuration: **Manage Workspaces**
* Under Settings > User and Role Management > Special Permissions: **Object Sharing Settings**

### Changing a Workspace Home Page

**To change the Home page dashboard:**

1. Go to the Dashboard Manager page and locate the dashboard you want.
2. Select a dashboard and from the 3-dot more menu, select Set as Homepage for and then select a workspace.
3. The dashboard is set as the workspace Home page.

<Image align="center" alt="HomePageDashboardSelect.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HomePageDashboardSelect.png" />

When a workspace is disabled in the list, the selected dashboard is already set as the Home page of that workspace.

## Set a Dashboard to Shared Access

To be used as the Home page of a workspace, a dashboard must have Shared access.

<Callout icon="💡" theme="default">
  **Important**

  When changing a dashboard to Shared access, **all** queries used by the charts in the dashboard are also changed to Shared access and will be available to all users with the selected roles across all data scopes. Before changing access permissions, verify that you want to make this change.
</Callout>

**To set a dashboard to Shared:**

1. Go to the Dashboard page and, in the folders pane, locate the dashboard you want to use as a Home page. Alternatively, go to the Dashboard Manager page and locate the dashboard you want.
2. From the 3-dot more menu, select **Edit**.

<Image align="center" alt="ChangeDashboardPermissionsEdit.png" width="350px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeDashboardPermissionsEdit.png" />

3. Under **Who has access**, from the **General access** list, select **Shared**. Note that the folder selected in the **Folder** section is changed to "Shared".

<Image align="center" alt="ChangeDashboardPermissionsbox.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/a6e244e5d14d180728a7af36e48d12c6385b6e0f/Images/ChangeDashboardPermissionsbox.png" />

4. Click **Save**.