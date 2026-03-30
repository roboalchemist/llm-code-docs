# Source: https://docs.axonius.com/docs/managing-queries-folders.md

# Managing Queries

Once you start working with Axonius, you might find yourself creating a large number of queries. The folder pane on the left side of the Queries page allows you to easily manage your queries.

<Image alt="QueriesFolders.png" width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueriesFolders.png" />

Click the left arrow next to **Search Folders** to collapse the folder pane. This is only visible when you hover over the pane.
![QueryFolderPaneCollapse.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryFolderPaneCollapse.png)

Click the right arrow to expand the folder pane.

![QueryFolderPaneExpand.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryFolderPaneExpand.png)

Queries are arranged into folders. Folders with subfolders can be expanded and collapsed by clicking the arrows next to the folder name. Queries in a subfolder also appear in the parent folder.

![QueriesFolderExpandCollapse.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueriesFolderExpandCollapse.png)

### Default Folders

Axonius provides a number of query folders by default.

* **All Queries** - Automatically lists all queries that you're authorized to see including all public, private, and predefined queries. Asset Scope queries are also listed here.  Every query must be saved to a folder. Note that you cannot save a query directly to the **All Queries** folder, only to a subfolder.
* **Public** - (Current Data Scope) Lists all queries accessible to all users in your Data Scope. The name of the folder is the name of the current Data Scope. Folders you create are available only to this Data Scope.
* **Shared Queries** - Only lists queries accessible to all Data Scopes and predefined queries. You can save queries available to all Data Scopes here and create new folders, up to 5 levels, under this folder.
  * **Predefined Queries** - The system comes with a set of predefined queries in the **Predefined Queries** folder that cannot be edited or deleted. This folder can only contain predefined queries.
* **My Private Queries** - You can save queries here and create new folders in this folder. The **My Private Queries** folder contains queries that are accessible by you only and is set as a default folder when you save a new query. You can create up to 5 levels of folders.
* **Asset Scope Queries** - Queries used to create Data Scopes. See [Data Scope Management](/docs/data-scope-management) for more information about Data Scopes.
* **Archive** - For Archived queries. Learn more in [Archiving Saved Queries](/docs/managing-queries-folders#archiving-saved-queries)

Folders can be expanded and collapsed by clicking the arrows next to the folder name. If a folder does not contain a subfolder, no arrow is shown.

![Queries-FolderExpandColapse.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Queries-FolderExpandColapse.png)

## Creating a New Folder

You can create folders only in the **Public Queries**, **My Private Queries**, **Asset Scope Queries**, or **Archive** folders or their subfolders.

**To create a new folder**

1. Hover over a folder.
2. Click on the 3-dot menu. The **Folder** menu opens.

<Image alt="Queries-New-Folder.png" width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Queries-New-Folder.png" />

4. Select **New Folder**. A new folder called 'untitled folder' is created inside the folder you selected.
5. Enter a name for the new folder or click on the Folder menu again, and select **Rename** to give a more appropriate name.

## Renaming Folders

Any folder you created can be renamed.

**To rename a folder**

1. Hover over a folder.
2. Click on the 3-dot menu. The Folder menu opens.
3. Click select **Rename** and give a new name to the folder.

## Moving Folders

You can move folders by drag and drop. If a private folder is moved into a public folder, all the queries in the private folder will become public.

**To move a folder or a subfolder from one folder to another**

Click and drag the folder or subfolder to a different folder. Note that if you move a  folder/subfolder from a private folder to a public folder, then the subfolder and all the queries in it become public. You can't move a public folder into a private folder.

## Deleting Folders

You can delete any folders that you have created. System folders cannot be deleted.

**To delete a folder**

1. Hover over a folder.
2. Click on the 3-dot menu. The Folder menu opens.
3. Click **Delete**.

<Callout icon="📘" theme="info">
  IMPORTANT

  Deleting a folder **does delete** all Queries in the folder. This cannot be undone. To delete the folder but keep the Queries, move them to another folder and then delete the folder you don't want.
</Callout>

## Moving Queries to Another Folder

You can move queries from one folder to another. Moving a query to another folder may change the access permissions of the query. You will be asked to confirm the change before the query is moved.

<Callout icon="📘" theme="info">
  Notes

  * You can only move queries which you have permissions to edit.

  * If you move a private query to a public folder, the query becomes public.

  * You can only move a query to a folder with the same permissions as the query itself (either public or private).

  * You can't move queries to the **Predefined Queries** folder.

  * Public queries cannot be moved to a private folder.
</Callout>

**To move a query to a different folder**

1. On the **Queries** page, select one or more queries. When at least one query is selected, the **Actions** button is displayed above the **Saved Queries** table.
2. Click the **Actions** menu.
3. From the **Actions** menu, select **Move To Folder** to move one or more queries to  a different folder. A Folder List dropdown opens.

![MoveQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MoveQuery.png)

3. Use the vertical and horizontal scrollbars to find the folders you want and click **Move**. The queries are moved to the appropriate folder. A confirmation message is displayed in some cases.

## Archiving Saved Queries

You might have a large number of saved queries. Use the Archive feature to move saved queries to an Archive folder. Once a query is in the Archive  folder, users will no longer be able to choose it when they create new charts, enforcement actions, reports or other queries. However, the query will continue to work correctly in existing chart, actions, reports and other queries.

**To move queries to the archive folder**

1. Select one or more queries.
2. From the **Actions** menu choose **Move to Folder**.

![ArchiveQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ArchiveQuery.png)

3. From the menu that opens select **Archive**.
4. Choose **Move**.
5. A message is displayed telling you that once you move a query to the archive folder you will not be able to choose it in any new Chart, Enforcement Action, Report or other Query. Confirm the action.

The query is moved. The word (Archived) now appears before the query name.

* You can also drag and drop a folder to the Archive folder.
* You can move a query from the archive folder to another folder

If you change your mind, you can remove items from the Archive folder. They can only be moved back to folders with the same permissions as they had before (e.g. Private/public)

When you move a saved query to the Archive folder it retains any permissions that it previously had, that is,  private queries remain private and public queries remain public. You can move a query out of the Archive folder, according to the Query’s existing permissions, If a query was public, you can only move it to the public folder, if it was private and you want to move it to the public folder the system asks if you want to move it to the public folder.