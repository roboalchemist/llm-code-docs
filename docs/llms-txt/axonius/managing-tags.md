# Source: https://docs.axonius.com/docs/managing-tags.md

# Managing Tags

Use **Tags Management** to manage *all*  tags in the system from one central location without viewing the details of a specific asset.
This includes tags added in the following ways:

* From the assets page **Actions** menu, on selected assets, filter results, or query results.
  * [Using the **Tag** action](/docs/working-with-tags#adding-tags-to-assets).
  * [Using the **Enforce** action](/docs/working-with-tags#adding-tags-to-query-or-filter-results-with-a-quick-enforcement-action).
* Using an Action Center action, such as [Axonius - Add Tag to Assets](/docs/add-remove-tag) to add tags to query results.

Only users assigned the **Update system settings** permission (default for admins) can manage tags.

Tags are supported for all asset types.

You can view and manage tags in two views:

* [Table](/docs/managing-tags#managing-tags-from-a-table) - Lists detailed information on all tags in the system.
* [Hierarchical structure](/docs/managing-tags#managing-tags-from-the-tag-hierarchy) - A structure where related tags are grouped together.

## Managing Tags From a Table

**To manage tags from a table**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the **System Settings** page, expand **Data**, and select **Tags Management**. The Tags table opens.

<Callout icon="📘" theme="info">
  Note

  You can click the Management Table icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManagementTableIcon.png) to open the **Tags Management** page directly from the **Tag Hierarchy** page.
</Callout>

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/settings/TagManagement_new.png" />

The **Tags** table shows all tags in the system that match the filter or search criteria, including all tags added to assets in their details page or by Enforcement Actions.

The following information is included for each tag in the table:

* **Tag Name** - The name of the tag.
* **Asset Type** - The asset type to which the tag applies.
* **Affected Assets** - The number of assets tagged with this tag. Click the number of Affected Assets to see a list of assets with their details.
* **Tag Color** - The selected color for the tag. A color can be selected from the color palette. Changes are global and will appear wherever the tag is used.
* **Created On** - The date and time that the tag was created.
* **Last Updated** - The date and time that the tag was last updated.
* **Used In** - Indicates whether or not the tag is used in the Action Center.
  * <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_BW_Icon.png" />

    * Indicates that the tag is used in the Action Center. Hovering over this Action Center icon [opens a table showing where the tag is used in the Action Center](#viewing-the-enforcement-sets-and-workflows-that-use-the-tag).
  * **...** - Indicates that the tag is not used in the Action Center.

<Callout icon="📘" theme="info">
  Note

  It can take a while for the information in the Tags Management table to be updated. You can [refresh the table](#refreshing-the-table) at any time to bring the table up to date, including the Used In table.
</Callout>

### Viewing the Enforcement Sets and Workflows that Use the Tag

For each tag in the Tags Management table (with ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_BW_Icon.png) under the **Used In** column), you can view the Enforcement Sets and/or Workflows that add or remove this tag. It is helpful to know the tag dependencies, for example, which tags would be affected by running Enforcement Sets and Workflows.

**To view the Enforcement Sets and Workflows that use the tag**

1. In the **Tags Management** table, under the **Used In** column, hover over the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_BW_Icon.png) icon. The following table opens:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsedInTable.png)

The table has two columns:

* **Used in** - Displays **Enforcements** - one row per Enforcement Set that uses this tag (add or remove) followed by **Workflows** - one row per Workflow that uses this tag (add or remove).
* **Location** - Enforcement Set or Workflow name link. Clicking the link opens the configuration page of the Enforcement Set or Workflow that uses this tag.

### Refreshing the Table

You can manually update the Tags Management table at any time by clicking the Refresh icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefreshSymbol.png)

<Image alt="TagsRefresh" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagsRefresh.png" />

### Filtering and Searching for Tags

Use the filter bar at the top of the page to select criteria to filter the **Tags** table. The table can be filtered by:

* **Asset Type** - The asset type to which the tag applies.
  * From the **Asset Type** dropdown, select one or more asset types to return the Tags that apply to these asset types. The assets in the dropdown are listed according to asset category (as on the Assets page). In addition, it is possible to type and search to easily locate in the dropdown, the asset type required.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ModulesTagsManagement.png)

You can also search the table according to **Tag Name** and **Asset Type** by entering a search string in the **Search** field.
This list is updated as soon as filter criteria are selected or a search string is entered.

Click the column headers to sort the list.

### Creating a Tag Directly from the Tags List

Click **+ Create Tag** to create a tag without binding it to specific assets. After you choose a name, an asset type an a color for the new tag, it is immediately listed in the table.

You can assign the new tag to the required assets from the relevant Asset page, as explained in [Working with Tags](https://docs.axonius.com/axonius-help-docs/docs/working-with-tags).

### Editing Tags from the Tags List

You can edit tags from the Tags list.

<Callout icon="📘" theme="info">
  Note

  When editing tags, once you click to execute the change, the edit window closes and, if necessary, the process continues in the background.
</Callout>

#### Changing the Tag Color

From the **Tags Management** table, you can change the color of a tag. The tag's color changes on all assets where it is used.

**To change the tag color**

1. In the row of a tag, under **Tag Color**, select the down arrow adjacent to the color, and from the choice of colors that opens, click the new color.

<Image alt="ChangeTagColor" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeTagColor.png" />

#### Exporting the List of Tags to CSV

The list of tags can be exported to a CSV file. Only the currently listed items are exported.

**To export the list of tags**

1. On the top right above the **Tags Management** table, click **Export CSV**. The file is generated and downloaded to the local computer.

#### Renaming a Tag

From the Tags Management table, you can rename a single tag and repeat for each tag

that you want to rename. Once renamed, the new tag name replaces the old tag name on all assets. For example, when TagA is renamed to TagAA, all assets that had TagA now have TagAA.

<Callout icon="📘" theme="info">
  Note

  Renaming tags does not trigger any migrations, such as query migrations. For example, if a Query is created to search for devices with TagA and some time after TagA is renamed to TagAA, the Query is not updated automatically to search for devices with TagAA. In this case, you have to manually [edit the Query](/docs/managing-queries#viewing-and-editing-query-details) to search for TagAA.
</Callout>

**To rename a tag**

1. In the **Tags Management** table, hover over one tag, or select one or more tags.
2. Select **Rename**.
3. In the **Rename Tag** dialog that opens, enter a new name for the tag.
4. Click **Save Changes**. To see the changes, you may need to click the Refresh Data ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefreshIcon.png) icon.

#### Deleting Tags

You can delete one or more selected tags from the **Tags Management** table. When you do so, only the selected tags are removed permanently from all affected assets. The remaining tags are ungrouped, if relevant (i.e., if the deleted tag is a parent tag). Learn more about [grouped tags in a hierarchical structure](/docs/managing-tags#managing-tags-from-the-tag-hierarchy). This action may take some time to complete.

**To delete a tag**

1. In the **Tags Management** table, hover over one tag, or select one or more tags.
2. Select Delete. If required confirm the deletion in the dialog box that opens. The tags are deleted permanently from all assets. This might take some time.
3. Click **Refresh** to refresh the table to see the updated data. The **Total** records is reduced by the number of deleted tags.

   <Callout icon="📘" theme="info">
     **Note**

     Tags whose assets are removed from the system are **not** automatically deleted. They remain in the **Tags Management** table even though they are not bound to any specific asset. To delete such a tag, hover over it and select Delete.
   </Callout>

## Managing Tags From the Tag Hierarchy

Tags can be nested to create hierarchies where assets with children tags also inherit the parent tag. In the **Tag Hierarchy** page, you can view nested tags and move tags from one tag group to another. You can also move one group of tags to another group of tags.\
For example, you can have a first-level **North America** tag with several country tags under it, including **USA** (second-level). Under the **USA** tag, you can have state tags (third-level), including **Virginia**, **Washington**, **Maryland**, **Florida**, and more.

You can then [search for assets with these tags and child tags using Queries](/docs/working-with-tags#creating-queries).

**To manage tags from the tag hierarchy**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the **System Settings** page, expand **Data**, and select **Tags Management**. The Tags table opens.
3. Click the Tag Hierarchy icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagHierarchyIcon.png)

<Callout icon="📘" theme="info">
  Note

  You can click the Tag Hierarchy icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagHierarchyIcon.png) to open the **Tag Hierarchy** directly from the **Tags Management** table.
</Callout>

<Image alt="TagHierarchy" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagHierarchy.png" />

The **Tag Hierarchy** shows all tags and their relation to other tags in the system.
If a tag is nested, the level of the tag is indicated.

<Image alt="TagLevels" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagLevels.png" />

The following information is included for each tag in the hierarchical structure:

* **Tag Name** - The name of the tag.
* **Level** - The level of the tag in the hierarchy.
* **Asset Type** - The asset type to which the tag applies.
* **Actions menu** - For grouped tags, includes the following actions: **Rename**, **Move**, **Change color**, **Rename tag level**, and **Delete**. For ungrouped tags, includes the same actions with the exception of **Rename tag level**.

### Refreshing the Hierarchy View

To manually update the hierarchy view, click Refresh ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefreshSymbol.png)

<Image alt="TagsRefresh" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagsRefresh.png" />

### Filtering and Searching the Tags Hierarchy

Use the filter bar at the top of the page to select criteria to filter the **Tags** hierarchy. The hierarchy can be filtered by:

* **Asset Type** - The asset type to which the tag applies. Learn more [how to filter the tags by asset type](#filtering-and-searching-for-tags).
* **Hierarchy Level** - The level of the tag in the hierarchy.

You can also search the hierarchical structure according to the **Tag Name** by entering a search string in the **Search** field.
This hierarchical structure is updated as soon as filter criteria are selected or a search string is entered.

### Editing Tags in the Tag Hierarchy

#### Moving Tags

You can move tags of the same asset type by dragging and dropping or by using the **Move** command. You can move a tag to be a child of another tag or to be a lone tag without child tags. When you move a tag, its child tags move together with it.
You cannot move a tag to be a parent of another tag.
You cannot create hierarchies between asset types. For example, you cannot move **tag2** (Users) below **central part** (Devices).

<Callout icon="📘" theme="info">
  Note

  It is not possible to drag and drop when the **Tag Hierarchy** view is filtered by **Hierarchy Level**. In this case, a notification pops up: 'Drag and drop is not supported in hierarchy level filtered view.'
</Callout>

**To move a tag using the Move action**

1. Click the 3-dot **Open Actions Menu** of the tag that you want to move, and click **Move**.
2. In the hierarchy that opens, click the tag under which you want to move the selected tag, and then click **Move**.

**To move a tag to be a child of another tag using Drag and Drop**

1. Click the tag to move and drag it to the parent tag until a purple rectangle encloses both tags. In the screen below, the **central part** tag is being dragged to below the **manhattan** tag.

<Image alt="Dragscreen1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dragscreen1.png" />

2. Release the mouse to drop it in place. In the screen below, **central part** is now a child tag of **manhattan**.

<Image alt="Dropscreen1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dropscreen1.png" />

**To move a child tag to be a lone tag using Drag and Drop**

1. Click the tag and drag it to overlap the purple line that appears below the parent tag. In the screen below, the **manhattan** tag is being dragged to a level on its own.

<Image alt="Dragscreen2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dragscreen2.png" />

2. Release the mouse to drop it in place. In the screen below, **manhattan** is now a parent tag and was moved together with its child tag **central part**.

<Image alt="Dropscreen2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dropscreen2.png" />

#### Renaming a Tag in the Tag Hierarchy

You can rename a tag. The name change is global. View the note in [Renaming a Tag from the Tags Table](#renaming-a-tag-from-the-tags-table).

**To rename a tag**

1. Click the 3-dot **Open Actions Menu** of the tag that you want to rename, and click **Rename**.
2. In the **Rename Tag** dialog that opens, type a new name for the tag and then click **Save Changes**. To see the changes, you may need to click the Refresh Data ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefreshIcon.png) icon.

#### Changing the Tag Color

You can change the color of a tag using **Change color** . The tag's color changes on all assets where it is used.

**To change the tag color**

1. Click the 3-dot **Open Actions Menu** of the tag whose color you want to change, and click **Change color**.
2. In the **Change color** dialog that opens, click the Down arrow to open a selection of colors, and click the new color.

<Image alt="ChangeColordialogopen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeColordialogopen.png" />

3. Click **Save**. To see the changes, you may need to click Refresh.

#### Renaming the Level

You can rename the hierarchy level of a tag. This changes the level name throughout the system. For example, if you change the hierarchy level name from '1st level' to 'First level', all tags at the 1st level will now have the new level name 'First level'. This does not change the location of the tag in the hierarchy structure.

**To rename the hierarchy level**

1. Click the 3-dot **Open Actions Menu** of the tag whose hierarchy level you want to rename, and click **Rename tag level**.
2. In the **Rename Hierarchy Level** dialog that opens, type the name of the new level. The hierarchy level name must be different than the original name.

<Image alt="RenameHierarchyLevel" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RenameHierarchyLevel.png" />

3. Click **Save Changes**. To see the changes, you may need to click Refresh.

<Image alt="RenamedLevel" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RenamedLevel.png" />

#### Deleting a Tag

You can delete a tag from the **Tag Hierarchy**. When you do so, the selected tag and all its child tags are removed permanently from all relevant assets. This action may take some time to complete.

**To delete a tag**

1. Click the 3-dot **Open Actions Menu** of the tag that you want to delete, and click **Delete**.
2. Click **Delete Tags** to confirm the deletion. It may take a little while to complete.
3. To see the changes, you may need to click Refresh.