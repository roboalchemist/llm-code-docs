# Source: https://docs.pentaho.com/pba-metadata-editor/build-a-business-view.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/build-a-business-view.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/build-a-business-view.md

# Build a business view

The last step in creating a business domain is building your business view. A business view is a collection of business categories that represents the view of your model typically consumed by your end users. Each model can have one and only one business view. Business views are made up of logically (logically relevant to your organization or end-users) organized business categories and business columns.

A business category is like a bucket where you group and re-group your business columns. Business categories can mimic your business table names or be named after your favorite rock stars. Categories do not have metadata associated with them, have no tie back to any business table (although the editor graph gives you the impression this relationship exists; don't be fooled), and have the simple purpose of allowing you to bucket the business columns in your model as intuitively as possibly for your data consumers.

Building a business view consists of creating your categories, then moving your business columns from the business tables into the categories. You can move columns from different business tables into the same category, and even duplicate the same business column into two different categories.

## Create a new category

The editor graph represents the business tables portion of the business model only, so you'll use the navigation pane and the category editor to create a business view.

To create a new category using the navigation pane, first make sure that the model you want to add this category to is selected, and the **Business View** node is visible.

1. In the navigation pane, right-click **Business View**.
2. Select **New Category**.

   The Business Category Properties dialog box appears.
3. Type a name for the category in the **ID** field.
4. Click **OK**.

## Build a business view using Manage Categories

Follow the instructions below to build a business view using the Manage Categories dialog box. Before you begin, make sure that the model whose business view you want to create is selected, and the **Business View** node is visible in the navigation pane.

1. Double-click on **Business View** in the navigation pane. Alternatively, go to **Tools** > **Manage Categories**.

   The Manage Categories dialog box appears.
2. Create categories directly from your business tables by moving columns into categories, add new categories, and remove categories and columns.

   ![Manage Catagories dialog box details](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-723c205fe2fe5eaa3c4c7f6a2ce98b535fa5ede1%2F16_manage_categories.png?alt=media)
3. Click **Close** when you are done.

### Create a new category from a business table

The navigation tree in the Manage Categories dialog box lists all of the business tables in your view. Follow the instructions below to create a new category from a business table in the Manage Categories dialog box:

1. Select the table in the navigation tree on the left.
2. Click the Right Arrow to add categories.

   Notice that your category has the same name as your business table, and all of your business columns were added to the new category by default.
3. Click **Close** when finished.

### Move columns into categories

Follow the instructions below to move columns into categories in the Manage Categories dialog box:

1. Select the table from the list of available business tables.

   To view the columns under a business table, click the Plus Sign to the left of each table name.
2. Select the destination category from the list on the right.
3. Click the Right Arrow to move columns.
4. Click **Close** if you are done.

### Add a new category

Follow the instructions below to add a new category in the Manage Categories dialog box.

1. Click the Plus Sign in the upper-right corner of the **Business View Categories** list.

   The Business Category Properties dialog box appears.
2. Enter an ID (name) for your category, and click **OK**.

   The new category name appears in the Manage Categories dialog box.
3. Click **Close** if you are done.

### Remove categories and columns

Follow the instructions below to remove categories and/or columns in the Manage Categories dialog box:

1. Select the items you want to remove in the **Business View Categories** list on the right.
2. Click the X icon to delete the selected categories or columns.
3. Click **Close** when you are done.

<br>
