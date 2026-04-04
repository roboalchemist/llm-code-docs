# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-business-glossary-administer-pdc.md

# Manage business glossary

Pentaho Data Catalog provides a single location for creating, organizing, curating, and identifying business glossary items like glossaries, categories, and terms to help you navigate your vast data environment so you can get the right data efficiently. You can also use the business glossary as a tool with role-based access control to secure and separate valuable data and metadata and prevent such data from reaching unintended audiences.

In Data Catalog, business terms are organized into categories and then into glossaries, representing a hierarchy. Using the business glossaries, you can manage or browse the business glossaries for your data environment.

**Note:** You can perform the following actions based on your permissions in Data Catalog.

## Create a glossary

Perform the following steps to create a glossary:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Click **Actions** and select **Add New Glossary**.

   The Create Glossary dialog box opens.
3. In the **Glossary Name** field, enter a name for the glossary you want to create.
4. Click **Continue**.

   The glossary is created and displayed in the list of glossaries in the Business Glossary navigation tree.
5. In the **Definition** field, click **Edit** to add a definition. Enter the definition and click Save.
6. In the **Purpose** field, click **Edit** to add a purpose. Enter the purpose and click **Save**.
7. (Optional) To change the glossary name, click the pencil icon next to the glossary name.
8. (Optional) In the **Properties**, **Tags**, and **Style** panels, you can click and update the values, which helps identify and define the resource.

   For more information, see the [Business Glossary](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-business-glossary) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

You have successfully created the glossary.

Repeat steps 1 through 8 to create an additional glossary or see [Create a category](#create-a-category) to create categories.

## Delete a glossary

Deleting a glossary irrevocably removes all its associated categories and terms in Data Catalog.

**CAUTION:** Because you cannot recover this data, use caution when deleting glossaries.

This task assumes you are on the Business Glossary page. Perform the following steps to delete a glossary:

1. In the left navigation tree, select the glossary you want to delete.
2. Click the **More** icon and then click **Delete**.

   A dialog box displays, asking you to confirm the deletion.
3. To confirm the deletion, click **Confirm**.

You have successfully deleted the glossary along with its associated categories and terms.

## Create a category

Perform the following steps to create a category:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Click **Actions** and select **Add New Category** and select **Category**.

   The Create Category dialog box opens.
3. In the **Category Name** field, enter a name for the category you want to create.
4. In the **Parent** field, choose a glossary from the dropdown options under which this new category will be grouped.

   If you selected a glossary from the list before creating a new category, then the selected glossary is automatically pre-selected as the new category's glossary. You can choose a different glossary if necessary.
5. Click **Continue**.

   The category is created and displayed in the list of glossaries in the Business Glossary navigation tree.
6. In the **Definition** field, click **Edit** to add a definition. Enter the definition and click Save.
7. In the **Purpose** field, click **Edit** to add a purpose. Enter the purpose and click **Save**.
8. (Optional) To change the category name, click the pencil icon next to the category name.
9. (Optional) In the **Properties**, **Tags**, and **Style** panels, you can click and update the values, which helps identify and define the resource.

   For more information, see the [Business Glossary](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-business-glossary) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

You have successfully created the category.

Repeat steps 1 through 9 to create additional categories or see [Create a business term](#create-a-business-term) to create a new business term.

## Delete a category

Deleting a category irrevocably removes all its associated terms in Data Catalog.

**CAUTION:** Because you cannot recover this data, use caution when deleting categories.

This task assumes you are on the Business Glossary page. Perform the following steps to delete a category:

1. In the left navigation tree, select the category you want to delete.
2. Click the **More** icon and then click **Delete** from the dropdown menu.

   A dialog box displays, asking you to confirm the deletion.
3. To confirm the deletion, click **Confirm**.

You have successfully deleted the category along with its associated terms.

## Create a business term

Glossaries and categories group terms that data analysts use to label their glossary-specific data. Newly created terms are associated with a glossary and category.

Perform the following steps to create a new term:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Click **Actions** and select **Add New Term**.

   The Create Business Term dialog box opens.
3. In the **Term Name** field, enter a name for the term you want to create.
4. In the **Parent** field, choose a glossary, category, or another term from the dropdown options.

   If you selected a glossary, category, or another term from the list before creating a new term, then the selected glossary item is automatically pre-selected as the new term's parent. You can choose a different glossary item if necessary.

   **Note:** If you don't select any glossary and category, the term is grouped under **Unassigned Terms**.
5. Click **Create**.

   It creates a new term and displays it in the left navigation tree.
6. In the **Definition** field, click **Edit** to add a definition. Enter the definition and click Save.
7. Click **Edit** to add a purpose. Enter the purpose and click **Save**.
8. (Optional) To change the term name, click the pencil icon next to the term.
9. (Optional) If the term can be identified by a general abbreviation, add it to the **Abbreviation** field.
10. (Optional) If the term represents any calculated value that can be arrived at using a mathematical or logical formula, click **Edit** in the **Formula** field, enter the formula, and then click **Save**.
11. (Optional) In the **Properties**, **Tags**, and **Style** panels, you can click and update the values, which helps identify and define the resource.

    For more information, see the [Business Glossary](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-business-glossary) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

You have successfully created a new business term.

## Delete a business term

Deleting a business term irrevocably removes all its associated associations in Data Catalog.

**CAUTION:** Because you cannot recover this data, use caution when deleting business terms.

This task assumes you are on the Business Glossary page. Perform the following steps to delete a business term:

1. In the left navigation tree, select the business term you want to delete.
2. Click the **More** icon and then click **Delete** from the dropdown menu.

   A dialog box displays, asking you to confirm the deletion.
3. To confirm the deletion, click **Confirm**.

You have successfully deleted the business term.

## Edit a glossary, category, or business term

Users with permission can edit the glossary items, like glossary, category, and business term and their features, such as name, definition, and purpose, including tags added to the item.

For example, if both the Finance glossary and the Claims glossary have a term named "expense", then these terms each have an independent identity: the "Finance.expense" and the "Claims.expense".

**Note:** When you have updated a glossary item name, the changes are reflected for all users.

Perform the following steps to edit a glossary item:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Select the glossary item you want to edit, like a glossary, category, or business term.
3. (Optional) In the **Summary** tab, you can click the pencil icon to change the name of the glossary item.

   When finished editing, click outside the box to save the change.
4. (Optional) In the **Summary** tab, click **Edit** to update the glossary definition and purpose.

   When finished editing, click **Save** to save the update.

You have successfully modified the glossary item.

## Import glossary

In Data Catalog, you can import a glossary from a file in one of the following file types:

* JSON Lines (see [https://jsonlines.org/](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fjsonlines.org%2F\&data=05%7C02%7Cmike.dwyer%40hitachivantara.com%7C40e66de83087428a480508dd370afff3%7C18791e1761594f52a8d4de814ca8284a%7C0%7C0%7C638727242553751122%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C\&sdata=hroGNKkzU7vLRdb8j7vS%2FoshJlJ%2B6Bzm%2FcY0K1WxGIU%3D\&reserved=0) for more information)
* Comma Separated Values (text/csv)

Perform the following steps to import a glossary:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Click **Actions** and select **Import**.

   The Import Assets dialog box opens.
3. In the **Label** field, you can drag and drop the file or browse and select the file you want to import and click **Submit**.

You have imported the glossary. You can now see the imported terms in the left glossary item tree.

## Export glossary

In Data Catalog, you can export a glossary into a JavaScript Object Notation (application/json) or Comma Separated Values (text/csv) file. Perform the following steps to export the glossary items:

1. Click **Glossary** in the left navigation menu.

   The Business Glossary page opens.
2. Click **Actions** and select **Export**.

   The **Export Assets** dialog box opens.
3. Select what to export. Select individual glossaries, or choose **Select all** to export every glossary in the list.\
   You can also use **Search** to find items. The counter (for example, **0/11**) shows how many are selected.
4. Select the file type (**CSV** or **JSON**), you want to export the glossary items to and click **Submit**.

   This downloads the file containing the glossary items in the selected format.

You have successfully exported the glossary items into the selected file type.
