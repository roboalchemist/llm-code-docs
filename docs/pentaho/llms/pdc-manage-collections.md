# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-collections.md

# Manage collections

In Pentaho Data Catalog, you can structure and manage your data assets by creating **Collections**, which include two types: Datasets, used to group homogeneous tables or files with identical schemas, and Data Collections, used to logically organize heterogeneous data assets that may vary in format or structure. These assets are structured within a hierarchy of components: **Category**, **Group**, **Dataset**, **Data Collection**, and **Data Product**. To learn more about these components, see the **Collections** section in the Use Pentaho Data Catalog document.

The **Manage Collections** section provides step-by-step guidance for organizing and maintaining your data assets within Data Catalog. You can create and organize Categories and Groups, which serve as containers for Datasets and Data Collections. Additionally, you can also customize and maintain this structure by editing or deleting existing items as needed. Once your data is organized and enriched, you can publish it as a **Data Product** to make it available across the organization.

## Create a category

A **Category** in Collections helps Data Catalog users by providing a logical and organized structure for managing data assets. It serves as the top-level container that groups related **Groups**, **Datasets**, and **Data Collections** under a common business context, such as a department, project, or domain.

Perform the following steps to create a new category for collections in Data Catalog:

1. In the left navigation menu, click **Data Canvas** and then click **Collections**.

   The list of existing collections appears in the **Collections** panel.
2. At the bottom of the **Collections** panel, click **Create New Category**.

   The **Create New Category** dialog box opens.

   You can also access this option from any of the views, **Browse Collections**, **My Collections**, or **Shared with Me**.
3. In the **Create New Category** dialog box, in the **Category Name** box, enter a name for the category that you want to create.
4. In the **Description** box, enter a meaningful description and then click **Create**.

   **Tip:** A clear and concise description helps other users understand the purpose of the category and improves discoverability across the catalog.

You have successfully created a new category, and it is visible in the **Collections** panel.

After creating a Category, create a group to organize your pre-defined dataset or collections. For more information, see [Create a group](#create-a-group).

## Create a group

A **Group** in Collections helps Data Catalog users to organize Datasets and Data Collections within a category based on specific topics, data sources, or use cases. It adds an intermediate layer of structure, making collections easier to manage, access, and govern.

Perform the following steps to create a new group for collections in Data Catalog:

1. In the left navigation menu, click **Data Canvas** and then click **Collections**.

   The list of existing collections appears in the **Collections** panel.
2. At the bottom of the **Collections** panel, click the **Create New Category** drop-down, select **Create Group**.

   The **Create New Group** dialog box opens.

   You can also access this option from any of the views, **Browse Collections**, **My Collections**, or **Shared with Me**.
3. In the **Create New Group** dialog box, from the Parent Category drop-down menu, select an existing category or group (as a nested item), that you want to use for creating a new group.
4. In the **Group Name**box, enter a name for the group that you want to create.
5. In the **Description** box, enter a meaningful description and then click **Create**.

   **Tip:** A clear and concise description helps other users understand the purpose of the category and improves discoverability across the catalog.

You have successfully created a new group, and it is now visible in the **Collections** panel under the selected category.

After creating a category and group, you can create a dataset or data collection. For more information, see [Create a dataset](#create-a-dataset) or [Create a data collection](#create-a-data-collection).

## Create a dataset

In Data Catalog, you can create datasets by grouping related data elements that share a common structure. This helps organize data in a meaningful way, making it easier to apply metadata, perform profiling, assign business terms, and enable efficient data discovery and governance.

Perform the following steps to create a new dataset for collections in Data Catalog:

1. In the left navigation menu, click **Data Canvas**.

   The **Data Canvas** opens, showing a list of available data sources and their respective data assets.
2. From the Data Sources panel, select data tables that share a similar structure, such as those with the same columns or schema (homogeneous data), and click **Add to Cart** located below the panel. You can also use the [**Details** tab](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#details-tab) to filter and select the data tables, and click the **Add to Cart** option on the tab.

   The selected tables appear in the **Data Cart**.
3. In the **Data Cart**, review the selected assets and click **Save as Collection**.

   The **Create New Collection** dialog box opens.
4. In the **Parent Group** drop-down menu, select an existing group where you want to create a dataset.
5. In the **Collection Name** box, enter a name for the dataset.
6. In the **Description** box, enter a meaningful description.

   **Tip:** A clear and concise description helps other users understand the purpose of the category and improves discoverability across the catalog.
7. Under **Select Type**, select **Dataset**.

   **Note:** Select the **Collection** option if you want to create a Data Collection instead. For more information, see [Create a data collection](#create-a-data-collection).
8. To run profiling and aggregation jobs on the dataset, choose one or both of the following options:

   1. **Profile Job**: Profiles the dataset and runs data aggregation.
   2. **Aggregation Job**: Runs only the aggregation job if the dataset is already profiled.

   For more details about these jobs, see **Processing Collections** in the **Use Pentaho Data Catalog** document.
9. Review the information you entered and click **Create**.

   It creates the dataset and initiates the selected job. You can track job progress in the **Workers** page.

You have successfully created a **Dataset**, and it appears in the **Collection** hierarchy under the selected group.

Once the profiling or aggregation job is complete, you can view the results on the **Summary** tab. You can then proceed to assign **Business Terms**, **Applications**, and explore other available tabs. For more information, see [**Content pane**](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#content-pane) under the [**Data Canvas**](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data) section in [**Use Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

## Create a data collection

In Data Catalog, you can create a data collection to group together multiple data assets that may have different structures. With data collections, you can organize diverse data assets under a single logical entity for easier management, discovery, and collaboration. Data collections help in categorizing related information, sharing curated groups of data assets with other users, and streamlining metadata management tasks across heterogeneous data.

Perform the following steps to create a new data collection under a group in Data Catalog:

1. In the left navigation menu, click **Data Canvas**.

   The **Data Canvas** opens, showing a list of available data sources and their respective data assets.
2. From the Data Sources panel, select data assets with different formats (heterogeneous data), and click **Add to Cart** located below the panel. You can also use the [**Details** tab](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#details-tab) to filter and select the data tables, and then click the Add to Cart option on the tab.

   The selected data assets appear in the **Data Cart**.
3. In the Data Cart, review the selected assets and click **Save as Collection**.

   The **Create New Collection** dialog box opens.
4. In the **Parent Group** drop-down menu, select an existing group where you want to create a data collection.
5. In the **Collection Name** box, enter a name for the data collection.
6. In the **Description** box, enter a meaningful description.

   **Tip:** A clear and concise description helps other users understand the purpose of the category and improves discoverability across the catalog.
7. Under **Select Type**, select **Data Collection**.

   **Note:**

   * Select the **Dataset** option if you want to create a dataset using homogeneous data assets, such as tables with the same schema. For more information, see [Create a dataset](#create-a-dataset).
   * Unlike datasets, data collections do not support profiling or aggregation jobs
8. Review the information you entered and click **Create**.

You have successfully created a **Data Collection**, and it appears in the **Collection** hierarchy under the selected group.

You can then proceed to assign **Business Terms**, **Applications**, and explore other available tabs. For more information, see [**Content pane**](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#content-pane) under the [**Data Canvas**](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data) section in [**Use Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

## Create a duplicate of a collection

In Data Catalog, you can duplicate a Dataset or Data Collection to create a new version that includes the original content, metadata, and relationships. With this feature, you can reuse or extend an existing collection without modifying the source.

{% hint style="info" %}
A collection can be duplicated only once. Once duplicated, the original collection can’t be modified.
{% endhint %}

Perform the following steps to create a duplicate of a collection:

1. In the left navigation menu, click **Data Canvas**, and then click **Collections**.
2. In the **Collections** panel, expand the respective category and group, and then click the Dataset or Data Collection you want to duplicate.\
   The **Summary** page of the selected collection appears.
3. Click the **Actions** drop-down menu and then click **Duplicate**.\
   The **Duplicate Collection** dialog box appears.
   \
   **Note**: If the collection is already duplicated, you can’t see the duplicate option. For more information, see [Duplicate or versioning of a collection](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-collections).

   <figure><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2FOtTei4sMqt10404ZEeU5%2Fimage.png?alt=media&#x26;token=d25d308c-4e82-40d8-bc0b-50aba0b6bcc5" alt=""><figcaption></figcaption></figure>
4. In the **Collection Name** field, enter a new, unique name for the duplicate collection.\
   A default name is suggested. You can edit it as needed. The name must be unique within the selected group.
5. From the **Parent Group** dropdown, select the category and group where you want to place the duplicate collection.
6. Click **Duplicate** to complete the duplication.\
   A new collection is created in the selected group, and a Duplicate banner briefly appears to notify you, including the option to undo and delete the duplicate collection.

You have successfully created a duplicate collection. The new collection includes all metadata, business terms, properties, and data assets from the original collection. System-generated values, such as profiling results and generated columns, are not copied. The duplicated collection also includes a reference link to the original, visible on the [Properties](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#properties-panel) tab.\
\
Next, you can [edit (add or remove assets)](#add-assets-to-a-collection), [update (add or remove properties)](#edit-or-update-a-category-group-dataset-data-collection-or-data-product), or process the collection.

## Publish a collection as a data product

In Data Catalog, you can publish a collection as a data product, which helps you package curated datasets or data collections into shareable, reusable, and well-documented entities. As data products are visible to all users, they enhance data discoverability, promote trust through clear ownership and descriptions, and support data-as-a-service initiatives across teams. Publishing a collection as a data product helps other users easily access, understand, and consume high-quality, business-ready data for analytics, reporting, or integration.

Perform the following steps to publish a collection as a data product under a group in Data Catalog:

1. In the left navigation menu, click **Data Canvas** and then click **Collections**.

   The list of existing collections appears in the **Collections** panel.
2. Select a collection that you want to publish as a data product.
3. Verify that the **Sensitivity** level is defined, as it is mandatory for publishing. You should also review and, if applicable, define additional metrics such as **Trust Score**, **Data Quality**, and other relevant attributes to enhance the product’s credibility. If these values are not specified, go to the [**Summary** tab](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#summary-tab), configure the required properties, and click **Save**.
4. Click **Actions**, then select **Publish as Data Product**. \
   In the **Publish Data Product** dialog box, review the **Sensitivity** property, which is mandatory, and ensure it is properly configured.&#x20;
5. You now have two options:

   * Click **Start Publishing** to publish the collection with all required and recommended properties set.
   * Click **Publish Anyway** if you want to proceed, even if some recommended properties (other than Sensitivity) don’t meet the suggested thresholds.

   **Note:** If the collection doesn’t have properties defined, you get an error message, and publishing cannot proceed.

You have successfully published the collection as a data product. The component now displays the updated data product icon and appears as a data product in the **Collections** hierarchy. It is visible to all users in Data Catalog.

After publishing a collection as a data product, you can view and manage its metadata, including the description, owner, and assigned domain. You can also share the data product with other users or teams to promote collaboration and reuse.

## Share collections

In Data Catalog, you can share a dataset, data collection, or data product with other users to enable collaboration and controlled access. Sharing allows other users to view, update, or run the component based on the permission you assign. It supports collaboration, ensures alignment across departments, and enables secure access to curated data assets for business and analytical use cases.

Perform the following steps to share a collection component in Data Catalog:

1. In the left navigation menu, click **Data Canvas**, and then click **Collections**.

   The **Collections** panel displays the hierarchy of components.
2. Select the dataset, data collection, or data product you want to share.

   The **Summary** tab opens.
3. In the upper-right corner, click **Share**.

   The **Share** dialog box opens.
4. In the **Type a member** box, enter the name or email address of the user you want to share with.
5. From the **Permission** drop-down menu, choose one of the following:
   * **View**: The user can only view the component.
   * **Update**: The user can edit the component.
   * **Run**: The user can execute supported actions such as profiling or publishing.\
     **Note:** With **Permissions**, you can control what actions others can perform on the shared component.
6. (Optional) In the **Message** box, enter a message for the user.
7. Click **Share**.

   The selected user is granted access with the specified permission level.

The dataset, data collection, or data product is now shared with the selected user. The component will appear in their **Shared with me** view when they log in to Data Catalog.

## Add assets to a collection

In Data Catalog, you can add selected data assets, such as tables or files, to an existing Dataset or Data Collection. With this, you can enhance existing collections or create a duplicate version before adding new assets, depending on your needs.

{% hint style="info" %}
The target collection must match the type of selected assets. For example, homogeneous tables can be added to a Dataset, while heterogeneous assets can be added to a Data Collection.
{% endhint %}

Perform the following steps to add data assets to a collection:

1. In the left navigation menu, click **Data Canvas**.
2. In the **Data Sources** panel, navigate to and select the data assets (tables or files) you want to add.\
   You can select multiple assets from different schemas or folders as needed.
3. Click **Add to Cart**.\
   The selected items appear in the **Data Cart** on the right panel.
4. In the Data Cart, click the drop-down next to **Save as Collection**, and then click **Add to Collection**.\
   The **Add to Collection** dialog box appears with two options:
   * [Add assets to an existing collection](#option_1-_add)\
     Select this option to append the selected data assets to an existing Dataset or Data Collection. The original collection is updated with the new items, and its version remains unchanged. This option is useful when extending an already curated collection.
   * [Duplicate collection and add items](#option-2-duplicate-collection-and-add-assets)\
     Choose this option to create a new copy of an existing collection and add the selected assets to it. This approach avoids modifying the original collection and helps you to manage and enrich the duplicate version independently.

### Option 1: Add assets to an existing collection <a href="#option_1-_add" id="option_1-_add"></a>

Perform the following steps to add assets to an existing collection:

<figure><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2F96HEVg8oMzZMawKfLLzf%2Fimage.png?alt=media&#x26;token=d024081a-d0a6-4399-8d28-156cd60c5667" alt=""><figcaption></figcaption></figure>

1. In the **Add to Collection** dialog box, select **Add to Existing Collection**.
2. Browse through the available categories and groups to locate the target collection. You can also use the search bar to locate a collection.\
   **Note**: Only compatible collections (Dataset or Data Collection) are enabled for selection based on the type of selected assets.
3. Select the collection you want to add the assets to.
4. Click **Add to Collection**.\
   The assets are appended to the selected collection.

The selected data assets are successfully added to the existing collection. A banner briefly appears to notify you about the added assets, including an option to delete them.

### Option 2: Duplicate collection and add assets

Perform the following procedure if you want to avoid modifying the original collection and instead duplicate it, adding the assets to the new copy.

<figure><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2FKoydcugugDJ3XhRPsC85%2Fimage.png?alt=media&#x26;token=b62c8659-4896-47f5-a1a0-b1d700a42a78" alt=""><figcaption></figcaption></figure>

1. In the **Add to Collection** dialog box, select **Duplicate Collection and Add Items**.
2. Browse through the available categories and groups to locate the source collection. You can also use the search bar to locate the source collection.\
   **Note**: Only compatible collections (Dataset or Data Collection) are enabled for selection based on the type of selected assets.
3. Select the source collection you want to duplicate and add the assets to.
4. In the **Collection Name** field, enter a unique name for the new collection.\
   A name is required and must be unique within the selected group.
5. In the **Parent Group** dropdown, select the group where the new duplicate collection will be created.
6. Click **Duplicate and Add**.

A new collection is created in the selected group, and the selected assets are added to it. A Duplicate banner briefly appears to notify you, including the option View Original Collection.

## Remove assets from a collection

In Data Catalog, you can remove individual assets, such as tables or files, from an existing Dataset or Data Collection. With this, you can maintain collections that are relevant, clean, and aligned with your business requirements.

{% hint style="info" %}
Removing an asset from a collection does not delete the original data asset from the Data Canvas. Only the association within the selected collection is removed.
{% endhint %}

Perform the following steps to remove assets from a collection:

1. In the left navigation menu, click **Data Canvas** and then **Collections**.
2. In the **Collections** panel, expand the respective category and group and then click the Dataset or Data Collection from which you want to remove assets.\
   The **Summary** page of the selected collection appears.
3. Click the **Details** tab.\
   A list of assets included in the collection appears.
4. Locate the asset you want to remove and click the **Delete** icon next to it.
5. In the confirmation dialog box, click **Remove** to confirm.\
   The asset is removed from the collection.

The selected asset is successfully removed from the collection. It no longer appears in the **Details** tab of the collection, but the source asset remains available in Data Canvas for future use.

## Edit or update a category, group, dataset, data collection, or data product

In Data Catalog, each collection component, such as category, group, dataset, data collection, or data product, includes editable metadata, including name, description, purpose, key metrics, and properties. You can edit or update this information on the **Summary** tab, and manage associated metadata on other tabs such as **Terms**, **Applications**, or **Policies**, depending on the component type.

{% hint style="info" %}
You can edit a category, group, dataset, data collection, or data product only if you are the owner or if the component has been shared with you with edit permissions. If you do not see the edit options, contact the owner or your administrator to request the appropriate access.
{% endhint %}

Perform the following steps to edit a collection component in Data Catalog:

1. In the left navigation menu, click **Data Canvas**, and then click **Collections**.

   The **Collections** panel displays a hierarchy of categories, groups, datasets, data collections, and data products.
2. Select the component (category, group, dataset, data collection, or data product) you want to edit.

   The **Summary** tab opens by default.
3. To edit text fields such as **Name**, **Description**, or **Purpose**, click the **Edit** icon next to the respective field, update the value, and click **Save** to apply the changes.
4. Update key metrics, such as **Sensitivity**, **Trust Score**, or **Data Quality**, in the Key Metrics section as required.

   These metrics help validate readiness for publishing as a data product.
5. To update properties such as **Domain** or **Status**, click the **Edit** icon next to the field under the **Properties** section, make the necessary changes, and click **Save**.
6. Go to other tabs, such as **Terms**, **Applications**, or **Policies**, to add or remove relevant metadata.

   **Note:** The available tabs vary based on the type of collection component selected.
7. After completing your updates, ensure that all required fields are defined and properly saved.

You have successfully updated the selected collection component. The changes are saved immediately and are visible to other users based on their assigned access rights.

## Edit or provide an alternate column name in dataset

In Data catalog, you can now provide an alternate name to the column under the dataset you created. However, it doesn't change the original column name in the Data Canvas (source).

Perform the following steps to edit or provide an alternative column name:

1. In the left navigation menu, click **Data Canvas** and select the required assets and create a **Dataset**.
2. Go to **Collections** and open the dataset you created.
3. In the dataset view, hover over the column you want to rename and click the **Edit** icon next to the column name.
4. Enter the new (alternate) column name, and then press **Enter** or click **Save**.

The column name is updated with the alternate name you provided. The original column name remains unchanged in the **Data Canvas.**

<figure><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2F9CFJuSFgrLkCt4hFP6UA%2Fimage.png?alt=media&#x26;token=478d1621-6fe3-4f36-a781-ae556c704922" alt=""><figcaption></figcaption></figure>

## Delete a category, group, dataset, data collection, or data product

In Data Catalog, you can delete any collection component, such as a category, group, dataset, data collection, or data product, when it is no longer needed. Deleting unused or obsolete components helps maintain a clean and organized catalog, reduces clutter, and ensures users can easily navigate and find relevant data assets.

{% hint style="info" %}
Only the owner of the collection component can delete it. If you do not see the Delete option, it is possible that you do not have the required permissions.
{% endhint %}

Perform the following steps to delete a collection component in Data Catalog:

1. In the left navigation menu, click **Data Canvas**, and then click **Collections**.

   The Collections panel displays a hierarchy of existing components, including categories, groups, datasets, data collections, and data products.
2. In the **Collections** panel, click the **More options** icon next to the component name (such as a dataset or data collection) that you want to delete.
3. Click **Delete** from the menu.

   A confirmation prompt appears.
4. Click **Confirm** to confirm the deletion.

   The component is permanently removed from the catalog.

You have successfully deleted the selected collection component. It no longer appears in the Collections hierarchy and is no longer accessible to users.

## View data patterns and sample data for a dataset

In Data Catalog, you can view the data patterns and sample data for any column in the dataset created or directly from **Data Canvas**. For more information, see [Data Canvas #Data Patterns](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#data-patterns "mention") and [Data Canvas #Sample Data](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data#sample-data "mention")in [Data Canvas](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data "mention") section in [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ "mention") guide.

Perform the following steps to view the data patterns and sample data:

1. In the left navigation menu, click **Data Canvas** or **Collections.**
2. On **Data Canvas**, go to the data source or on **Collections,** go to the data set, and locate the column for which you want to view the details.
3. Select the column to open its **Details** panel.
4. In the **Data Patterns and Sample Data** section.\
   The section displays detected data patterns and a few sample records for the selected column.

The **Data Patterns** **and Sample Data** sections display profiling insights for the selected column in both **Data Canvas** and **Collections** views.
