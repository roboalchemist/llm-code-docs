# Source: https://docs.axonius.com/docs/setting-page-columns-display.md

# Setting Page Columns Display

Your system includes predefined columns for each Assets table, as well as the **Adapter Connections** and **Adapter Fetch History** pages. You can change those default displays and customize which columns appear on each page in which order. When you export tables to CSV files, the column order in the exported file matches the table display order.

Each Assets page maintains its own column configuration, displaying only columns relevant to that specific asset type.

You can save columns in sets of Views that you can load as required. See [Saved Views](/docs/setting-page-columns-display#saved-views) for more information.

<Image alt="EditTbleMenu2.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditTbleMenu2.png" />

## Setting Page Columns Display

<Callout icon="📘" theme="info">
  Note

  Applies to Assets tables,  Adapter Connections page and Adapters Fetch History page.
</Callout>

You can set the columns displayed on the page, change their order, or freeze specific columns so that they are not scrolled.

**To change the displayed columns:**

1. Click **Edit Table**, then select **Edit Columns** from the dropdown menu.

<Image alt="EditColumnsNEw2.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditColumnsNEw2.png" />

2. In the **Available Columns** pane, select an adapter from the dropdown menu to view its available columns. (This step applies to Assets pages only.)
   ![AdapterDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ColumAdapter.png)

3. To add columns to the page, select the required columns in the **Available Columns** list and then click **Add**. Columns available depend on the adapter you select. Note that **Custom Data** is also an option in the adapter list.

<Callout icon="📘" theme="info">
  Note

  It is not recommended  to add more than 50 columns to a table, as this may affect optimal table behavior.
</Callout>

4. To remove columns from the page, select the required columns in the **Displayed Columns** list and click **Remove**.
5. To change the order in which the columns appear, move them up or down in the **Displayed Columns** pane.
6. To cancel any changes that you made to the column display and return to the default view, click **Reset**.
7. Click **Save** when you finish your configuration. To save a view as your default view, see [Saved Views](/docs/setting-page-columns-display#saved-views).

To return to your default column view and clear all filters, click **Reset** above the search bar.

<Callout icon="📘" theme="info">
  Note

  On Assets pages, you can save queries with the columns in the **Displayed Columns** pane even when no query expression has been defined. Then, you can load these saved queries and use them as a template for building new saved queries that include the predefined columns and column filters.
</Callout>

### Changing the Order Columns are Displayed

You can change the order of columns in tables in the system directly from the table.
Drag and drop columns on the table to arrange them in the order you want. Use **Edit Columns** to save your changes.

### Freezing the Columns Displayed

By freezing the columns displayed, you can scroll horizontally while the frozen columns are always visible.
A frozen column has a lock icon in its header; an unfrozen column has an unlock icon.
By default, on Assets pages the **Adapter Connections** column is always displayed (frozen) when you scroll horizontally.

**To freeze columns from an Assets/Adapter Connections/Fetch History page:**

1. Hover over a column heading.

<Image alt="LockIcon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LockIcon.png" />

2. Click the unlock icon on the column. All the columns up to and including the selected column are frozen (closed lock icon).

You can also freeze the column display using the **Edit Columns** dialog.
Any frozen columns are displayed at the top of the Displayed Columns pane, in a shaded area.

1. Click **Edit Table**, then select **Edit Columns** from the dropdown menu.

2. Drag the field that you want to set to lock near to the top of the **Displayed Column** pane.

3. Hover over the column name to see the lock/unlock icon.

4. Click the icon to set the column name to be locked. This column and all columns above it are then frozen.

5. Click **Apply**.

On Assets pages, the system informs you if you choose too many columns to properly display the Assets table, the system informs. In that case, either change your screen resolution or select fewer columns.

<Image alt="ColumnsEditLock2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ColumnsEditLock2.png" />

To unfreeze a column, drag the column header out of the frozen (shaded) area, or click the unlock icon to unfreeze this column and all columns below it.

## Saved Views

<Callout icon="📘" theme="info">
  Note

  Applies to Assets tables, Adapter Connections page and Adapters Fetch History page.
</Callout>

Views are column arrangements displayed in tables. Use **Saved Views** to create views tailored to specific use cases or your workflow preferences.

Use **Views** to define and save column arrangements. You can:

* Create a collection of **Saved Views** for Assets table and Adapter table columns and switch between them according to your needs.
* Display fields most relevant to your current task.
* Define different view sets for each asset type or Adapter Connection/Fetch History page.

Each user can create their own set of Views, however, users cannot share a view.

### Creating a View

**To create a view**:

1. Select **Edit Table**.

2. From **Saved Views**, select **+ New View**.
   ![SavedViewsNewView](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/new%20view.png)

3. The **New View** dialog opens. Enter a name for your view. You can only save the view after naming it.
   ![NewViewDialog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewViewDialog-NewUI.png)

4. Select columns from the **Available Columns** pane, then click **Add** to move them to the **Displayed Columns** pane.

<Callout icon="📘" theme="info">
  Note

  It is not recommended to add more than 50 columns to a table, as this may affect optimal table behavior.
</Callout>

5. To remove columns from the **Displayed Columns** pane, select them and click **Remove**. Note that the columns available change according to the adapter you select. For more information, see [Setting Page Column Display](/docs/setting-page-columns-display#setting-page-columns-display).
6. To change the column display order, drag the columns up and down to change. To make this the default view, enable **Set as Default**.
7. Under **Expand Assets by**, select whether to expand rows in the view by a complex field. See [Expanding Assets by a Complex Field](/docs/expanding-assets-by-a-complex-field) for more information.
8. Under **Access**, define which user roles can access this view. See [Sharing a Saved View](#sharing-a-saved-view)  for more information.
9. Save the View.

After you save the view, the system notifies you and loads the new view.
On each Assets page, you can select a view and set it as default.

<Callout icon="📘" theme="info">
  Note

  The view is only saved to the Asset Type/Adapter table it was created from.
</Callout>

### Loading a View

1. From  **Edit Table**, hover over **Saved Views**. All available views for this asset/adapter table are listed.
   ![SavedViewsList](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/new%20view.png)

2. Select the view you want to load.

The **System View** contains the default columns that Axonius provides for each asset type. You can set any view as your personal default. Once set, your default view loads automatically each time you open that specific table.

### Editing a View

1. From  **Edit Table**, hover over **Saved Views**.

2. Hover over the relevant view. A popup displaying the view's details appears. Click **Edit**.

   <Image alt="SavedViewEditPopup" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/saved%20view%20popup.png" />

3. Edit the view as required, then click **Save** to load the edited view.

#### Editing the System View (Admins Only)

Admins can also edit the default System View (but not rename it). This creates a new **System View** for all users.

### Sharing a Saved View

You can share a saved view by managing access to selected roles.
See [Managing Roles](/docs/manage-roles) for more information about assigning permissions to roles at the system level.

<Callout icon="📘" theme="info">
  Notes

  * Only users with the *Manage saved views* permission can share views. This section is not available to users without this permission.

  * Users with the *Manage saved views* permission who are **not** admins can share views but cannot modify role permissions. Only admins can edit role permissions.
</Callout>

When you hover over a view, you can see an indication whether it is shared by your admin or shared by you with others. Unshared views are listed as **Private**.

<Image alt="SharedView" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-SVQPWCLX.png" />

**To share a saved view:**

1. Hover over the relevant view and click **Edit**.
2. Scroll to the bottom of the **Edit View** dialog and expand **Who has access**.
3. Under [**Who has access**](/docs/who-has-access), configure the access privileges for the saved view.
4. Save your changes.

### Deleting a View

<Callout icon="📘" theme="info">
  **Note**

  You can only delete private views. You can't delete views shared by your admin.
</Callout>

Hover over the relevant view and click **Delete**. The system asks you to confirm before deleting the view.

* If you delete your default view, the System View becomes the new default for that Assets page. The System View cannot be deleted.
* After deleting a view, the current column view continues to be displayed, but this arrangement is no longer saved as a view.

### Making a View the Default View

The system includes a default System View for each table. You can set any view as your personal default. That default view displays automatically when you open an asset/adapter table, and you can set different defaults for each table type.

To set a view as default, hover over the relevant view and click **Set Default**. You can also do this from the **Edit View** dialog.

<Image align="center" alt="SetViewAsDefault" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/set%20view%20as%20default.png" />

### Additional Predefined Views

Axonius supplies various column arrangements for search for specific parameters for Assets pages. These include:

* System search (Host Name) (Default)
* System search (Last Used Users) (Default)
* System search (IP Address) (Default)
* System search (Installed Software Name) (Default)

See **System Search Default** to set the columns to be displayed in system searches. For more information, see [Free Text Search in Table](/docs/query-wizard-and-query-filter#free-text-search-in-table).

## Refining the Data Displayed in Table Columns and Rows

<Callout icon="📘" theme="info">
  Note

  For Assets tables only.
</Callout>

Use complex expressions to refine the display in Assets table so you can zoom in on the information that interests you the most. The following types of data refinement are available:

* Refine display by field value
* Refine field values by adapter connection
* Refine asset entities by field value
* Refine asset entities by adapter connection

Data refinement does not impact the 'count' of the results, only the results that are displayed.

To open the **Refine Data Display** dialog, click the ![RefineDataFilterIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Filtericon\(2\).png) icon on the right of each column title.

<Image alt="Refine1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine1.png" />

Configuring data refinement does the following:

* Sets the columns and rows displayed in the queries that you create.

* Sets the display of CSV exports, including reports or Enforcement Actions that export data as CSV files.

### Refining Display by Field Value

Use complex expressions to create sophisticated filters to:

* Refine the display.
* Search for specific values to be displayed in each table column on the page, including multi-field columns.

Open the **Refine display by field value pane**, which acts as a sophisticated column filter.

<Image align="center" alt="Refine2" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine2.png" />

Each row in the  **Field values - refine by condition** pane is a filter expression that consists of the following elements:

1. AND / OR switch

2. NOT Flag

3. Field dropdown

4. Operator dropdown

5. Value field

6. Parentheses controls

See [Creating Queries with the Query Wizard](/docs/query-wizard-and-query-filter) for more information on each element and how to define it.

The **Field Name** drop-down shows the column on which you are filtering. The options available depend on the field type: if this is a complex field, all values that are part of the complex field are displayed and you can select the field to filter by.

For example, If you filter on the **Installed Software** complex field, the field dropdown contains the following range of possible values to filter by:

<Image align="center" alt="Refine3" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine3.png" />

Axonius displays only values that match the complete filter.

### Refining Field Values by Adapter Connection

Configure the system to hide or show values from specific adapter connections in a selected column. Only values from the included adapters will be displayed in that column.

1. Open the **Refine field values by adapter connection** pane.
2. From the dropdown menu, select whether to include or exclude values.
3. In the adapters list, start typing to search for a specific adapter or connection name, then select the adapter or connection that you want to exclude or include values from.

<Image align="center" alt="Refine4" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-VA28S6A5.png" />

4. Mark the adapter to select all its connections or specific connections, or click **Select All** to select all adapters and connections.
5. To undo your selections, click **Clear All**.

### Refining Asset Entities by Field Value

Use **Refine asset entities by field value** to refine the contents of the asset entity that are displayed according to the rows.

For example, you can hide a row, an asset entity, which contains a Software Version with a specific value.

1. Open the **Refine asset entities by field value** pane.

<Image align="center" alt="Refine5" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine5.png" />

2. Create a filter as explained in [Refining Display by Field Value](/docs/setting-page-columns-display#refining-display-by-field-value).

### Refining Asset Entities by Adapter Connection

Use **Refine asset entities by adapter connection** to hide or show asset entities from specific adapter connections. You can hide or show a row (an asset entity) if it comes from a specific adapter or adapter connection. An asset without any asset entities might be completely hidden or shown.

1. Open the **Refine asset entities by adapter connection** pane.
2. Create a filter as explained in [Refining Field Values by Adapter Connection](/docs/setting-page-columns-display#refining-field-values-by-adapter-connection).

<Image alt="Refine6" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-DXJW6L7M.png" />

### Refining Data for the Entire Table

Instead of refining data for each field separately, you can manage data refinement for all table columns in a single dialog.

1. Click **Refine Data** (next to **Edit Table** button).

<Image alt="Refine7a" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine7a.png" />

2. If no fields to be refined were selected yet, select a field. You can only select fields that are currently included in the table. Next, click **Add**.

<Image align="center" alt="Refine8" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine8.png" />

3. Select a data refinement method and set the required filters, as explained in previous sections.
4. To refine data for another field, click `+` and select a field. It appears as a new tab in the Refine Data Display dialog.

<Image align="center" alt="Refine9" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine9.png" />

5. Select **Apply** to save your changes.
6. Click **X** next to the field's tab to remove it.

<Image alt="Refine10" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine10.png" />

You can open the general Refine Data dialog at any time to see all the refinements defined for this table.

<br />