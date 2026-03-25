# Source: https://docs.axonius.com/docs/importing-and-exporting-dashboards.md

# Importing and Exporting Dashboards

You can import and export Dashboards to and from Axonius. Dashboards are exported from Axonius in JSON file format. An exported Dashboard can be imported. This makes it easy to move Dashboards from one Axonius environment to another.

All charts and their settings, including queries, are exported. Access permissions are NOT exported with dashboards. When importing, you can set the access level.

* A Dashboard can only be imported to the same major version (first two numbers of the version number) of Axonius as it was exported. For example, a dashboard exported from version 6.0.x cannot be imported to version 6.1.x.
* Dashboards with all access permissions, including custom or Private, can be imported and exported.
* To import a dashboard to Shared access, import to Public or Private first and then edit the dashboard and set the access to Shared.
* System dashboards, including **My Dashboard**, cannot be exported.

For more information about Data Scopes, see [Data Scope Management](/docs/data-scope-management).

## Required Permissions

The user's role must have the following permissions to import or export dashboards.

* To export dashboards, roles must be unrestricted and have the following permissions:
  * Export dashboard
* To import dashboards, roles must have the following permissions:
  * Import Dashboard
  * View Dashboards
  * Add Dashboards
  * Add charts
  * Delete charts
  * View entity - Must have this permission for all the entity types included in the imported dashboards.
  * Add saved queries - Must have this permission for all the entity types included in the imported dashboards.
  * Edit saved queries - Must have this permission for all the entity types included in the imported dashboards.

## Exporting Dashboards

**To export dashboards:**

1. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardIconSmall.png) on the left navigation panel to open the **Dashboard** page.
2. From the three-dot menu next to the Dashboard name in the **Dashboard List** or above the upper right corner of the Dashboard, select **Export Dashboard**. The Dashboard is downloaded to your local computer as a JSON file.

## Importing Dashboards

<Callout icon="📘" theme="info">
  **Notes:**

  * When importing multiple dashboards at the same time, the selected access settings are applied to them all. Dashboards cannot be assigned Shared access during the import.
  * Only users in the Global data scope can assign Shared access. To do this, import the dashboard to Public or Private and then edit the dashboard to have Shared access.
</Callout>

**To import dashboards:**

1. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardIconSmall.png) on the left navigation panel to open the **Dashboard** page.
2. From the **Add Dashboard** dropdown, select **Import Dashboard**.
3. Navigate to the location of the dashboard JSON file and select it.
4. Click **Upload**.
5. In **Dashboard name**, enter a descriptive name for the Dashboard.
6. Under **Who has access**, select specific roles you want to have access to the Dashboard. See [Who Has Access](https://docs.axonius.com/axonius-help-docs/docs/who-has-access) for more information.
7. Select **Admin Access Only** to give access only to users with the **Admin** role.
8. In the **Import Dashboard** dialog, select what to do if a dashboard or one of the underlying queries with the same name as that being imported already exists.
   * Click **Overwrite** to import the dashboards and overwrite the previously existing dashboards with the same name.
   * Click **Create a Copy** to import the dashboards using the same name as the existing ones. The existing dashboards are still available.
9. Click **Save**. The Dashboards are imported and added to the Dashboard List according to the access permissions you selected.