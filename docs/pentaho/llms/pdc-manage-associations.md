# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-associations.md

# Manage associations

In Pentaho Data Catalog, you can add, view, and delete associations of business terms with data assets, and business terms with another business term.

## Manage associations of business terms with data assets

In Data Catalog, you can manage the associations of business terms with data assets using the following procedures:

* [Associate business terms with a data asset](#associate-business-terms-with-a-data-asset)
* [View business terms associated with a data asset](#view-business-terms-associated-with-a-data-asset)
* [View data assets associated with a business term](#view-data-assets-associated-with-a-business-term)
* [Remove business term association with the data asset](#remove-business-term-association-with-the-data-asset)

### Associate business terms with a data asset

In Data Catalog, you can associate business terms with a data asset. Perform the following steps to associate a business term with a data asset:

1. Click **Data Canvas** in the left navigation menu.
2. Select the data asset to which you want to add the association.

   The software displays the asset metadata.
3. Click the **Glossary** tab.

   The list of associated business terms opens.
4. Click **Add Terms**.

   The list of **Business Terms** opens in the Add Business Terms dialog box.
5. Select the business term that you want to associate with the data asset.
6. Click **Add**.

You have successfully created the association between the business term and the data asset.

### View business terms associated with a data asset

In Data Catalog, you can view business terms that are associated with a data asset. Perform the following steps to view the list of business terms associated with a data asset in the Data Canvas:

1. Click **Data Canvas** in the left navigation menu.
2. Select the data asset for which you want to view associations.

   The software displays the asset metadata.
3. Click the **Glossary** tab.

   The associated business terms list opens.

   ![Associated term list](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-eedf4d9fcb2b92f429a0a1684a1bec868ce8b4bf%2FPDC%20Data%20Canavas_Associated%20terms%20list.png?alt=media)

   The following table describes the association details.

   <table><thead><tr><th width="151.111083984375">Column name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Business Term</strong></td><td>Specifies the name of the business term associated with the selected data asset.</td></tr><tr><td><strong>Category</strong></td><td>Specifies the name of the category to which the term belongs.</td></tr><tr><td><strong>Glossary</strong></td><td>Specifies the name of the glossary to which the term belongs.</td></tr><tr><td><strong>Definition</strong></td><td>Displays the definition of the term added while creating the term.</td></tr><tr><td><strong>Purpose</strong></td><td>Displays the purpose of the term added while creating the term.</td></tr></tbody></table>

   **Note:** You can use **Show Columns** to customize the display.
4. (Optional) Click **View** to view the term in the Canvas view with a highlighted focus on the Business Glossary page.

### View data assets associated with a business term

In Data Catalog, you can view data assets that are associated with a business term in the Business Glossary page. Perform the following steps to view the list of data assets associated with a business term:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Select the business term for which you want to view associations.
3. Click the **Data Elements** tab.

   The associated data assets list opens. The following table describes the association details:

   <table><thead><tr><th width="141.11114501953125">Column name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Data Source</strong></td><td>Specifies the name of the data source to which the associated data element belongs.</td></tr><tr><td><strong>Item Name</strong></td><td>Specifies the name of the data element associated with the term.</td></tr><tr><td><strong>Item Type</strong></td><td>Specifies the type of the data element associated with the term, like folder, table, schema, and column.</td></tr><tr><td><strong>Parent</strong></td><td>Specifies the parent directory of the data element associated with the term in case of file systems.</td></tr><tr><td><strong>Tags</strong></td><td>Contains the tags linked to the data element associated with the term. Tags will assist in identifying the resource using specific keywords.</td></tr></tbody></table>
4. (Optional) To get detailed information, click the **View Details** button (**<**) next to an item to view the data element in the **Canvas** view with a highlighted focus.

### Remove business term association with the data asset

In Data Catalog, you can delete an association of a business term with the data asset if it is no longer needed. Perform the following steps to delete an association:

1. Click **Data Canvas** in the left navigation menu.
2. Select the data asset for which you want to remove the association.

   The software displays the asset metadata.
3. Click the **Glossary** tab.

   The associated business terms list opens.
4. From the associated business term list, select the **Delete** icon for the business term for which you want to remove the association.

You have successfully removed the association of the business term with the data asset.

## Manage associations between business terms

In Data Catalog, you can manage the associations of one or more business terms to another business term using the following procedure:

* [Associate a business term with another business term](#associate-a-business-term-with-another-business-term)
* [View business terms associated with another business term](#view-business-terms-associated-with-another-business-term)
* [Delete associations among business terms](#delete-associations-among-business-terms)

### Associate a business term with another business term

In Data Catalog, you can associate a business term with another business term and create a relationship that describes the link between two business terms.

Perform the following steps to associate a business term with another business term:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Select the business term for which you want to add the association.
3. Click the **Related** tab.
4. Click **Add Related**.

   The Edit Data source page opens.
5. Select business terms you want to create associations.
6. Click **Select**.

You have successfully added an association between related business terms.

### View business terms associated with another business term

In Data Catalog, you can view the business terms associated with a business term. Perform the following steps to view the list of business terms associated with another business term:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Select the business term for which you want to view the association.
3. Click the **Related** tab.

   The associated business term list opens. The following table describes the column details.

   <table><thead><tr><th width="174.4444580078125">Column Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td>Specifies the business term associated with the selected business term.</td></tr><tr><td><strong>Relationship Type</strong></td><td>Specifies the type of relationship that the selected business term has to the business term shown in the <strong>Name</strong> column.</td></tr><tr><td><strong>Glossary</strong></td><td>Specifies the name of the glossary to which the related business term belongs.</td></tr><tr><td><strong>Category</strong></td><td>Specifies the name of the category to which the associated business term belongs.</td></tr><tr><td><strong>Custodian</strong></td><td>Specifies the owner(s) of the associated business term.</td></tr></tbody></table>
4. (Optional) To get detailed information, click the **View Details** button (**<**) next to an item to view the associated business term in the **Canvas** view with a highlighted focus.

### Delete associations among business terms

In Data Catalog, you can delete an association between business terms if it is no longer needed. Perform the following steps below to delete an association:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Select the business term for which you want to delete the association.
3. Click the **Related** tab.

   The list of associated business terms opens.
4. Select the check box for the association that you want to remove.

   **Note:** You can select multiple associations for removal.
5. Click **Remove**.

You have successfully removed the associations of related business terms.
