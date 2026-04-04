# Source: https://docs.pentaho.com/pdc-admin/manage-reference-data-sets.md

# Manage reference data sets

Reference data sets contain relatively static, unchanging data values that are commonly used by an organization. In Pentaho Data Catalog, you can create reference data sets that contain valid data values for your organization to reference.

Some examples of common reference data sets include:

* Branch Numbers
* Country codes
* Currencies
* Exchange codes
* Language codes
* Measurement units
* Postal codes
* Product codes
* Regions
* Transaction codes

## Add a category for reference data

Add categories to organize reference data sets into groups, enhancing the management and navigation of reference data sets.

**Note:** You must create at least one category before you can create a reference date set.

Perform the following steps to create a new category for reference data sets:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the Reference Data menu, click **Actions** > **Add New Category**.
3. In the Create Category dialog box, enter a **Category Name** and click **Create**.

The new category is added to the **Reference Data** menu.

Add one or more reference data sets to the new category.

## Add a reference data set

Add reference data sets to Data Catalog to facilitate the classification and categorization of data across the organization.

To add a reference data set to Data Catalog, complete the following tasks, in order:

1. [Create a reference data set](#create-a-reference-data-set)
2. [Add schema to a reference data set](#add-schema-to-a-reference-data-set)
3. [Add values to a reference data set](#add-values-to-a-reference-data-set)

### Create a reference data set

Create a reference data set to categorize enterprise data and maintain organizational consistency.

If you need a new category to contain the reference data set, you must create the category before creating the reference data set. For instructions about creating a new category, see [Add a category for reference data](#add-a-category-for-reference-data).

Perform the following steps to create a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, click **Actions** > **Add New DataSet**.

   The Create DataSet dialog box opens.
3. In the **DataSet Name** box, Enter a **DataSet Name**.
4. In the **Parent** list, select the category or reference data set that you want to be the parent of the new reference data set.

   **Note:** Select a reference data set as a parent only for organizational purposes. Reference data sets do not inherit any properties or information from parent reference data sets.
5. Click **Create**.

   A new, empty reference data set is created and the **Summary** tab for the new reference data set opens.
6. In the **Description** box, enter a description for the reference data set.
7. In the **Purpose** box, enter an explanation of the purpose for the reference data set.
8. (Optional) In the **Properties** box, update one or more of the following properties:

<table><thead><tr><th width="130.6666259765625">Property</th><th>Value options</th></tr></thead><tbody><tr><td>Sensitivity</td><td><ul><li>Unknown (default)</li><li>Low</li><li>Medium</li><li>High</li></ul></td></tr><tr><td>Status</td><td><ul><li>Info (default)</li><li>Valid</li><li>Warning</li><li>Expired</li></ul></td></tr><tr><td>Version</td><td>1.0 (default)<br><strong>Note:</strong> The version number can only be increased.</td></tr></tbody></table>

9\. Click **Save**.

The reference data set is created.

Add a schema to define and control the type of information contained in the reference data set.

### Add schema to a reference data set

Add schema for a reference data set so that you can maintain data quality by standardizing and controlling what data values can be entered in the reference data set.

For example, you can add schema to specify that the value for a type of information is selected from a pre-defined list, and then specify the list of valid values.

**CAUTION:** A schema can be added that has the same values in all columns as an existing schema, but has a unique identifier assigned to it in the system. If the duplicate schema are used in different parts of an organization and one schema is updated, then the reference data values that the schema is meant to control might no longer be consistent across the organization. Verify that a schema with all the same values does not already exist before adding a new schema.

**Tip:** You can also import reference data schema and values in a CSV file or from a Data Catalog table by clicking **Import** to open the Import Reference Data wizard.

Perform the following steps to add schema to a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Click the **Schema** tab.
4. In the **Reference Data Schema** table, click **+ Add Row**.
5. In the new table row, update the following fields:

<table><thead><tr><th width="155.111083984375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Column Name</strong></td><td>A column name that represents the type of data that the schema controls.</td></tr><tr><td><strong>Data Type</strong></td><td><p>The type of data that can be entered as a value. <strong>Data Type</strong> options include:</p><ul><li><strong>Text</strong></li><li><strong>String</strong></li><li><strong>Integer</strong></li><li><strong>Float</strong></li><li><strong>Binary</strong></li></ul></td></tr><tr><td><strong>Length</strong></td><td>The number of characters that can be entered for the value.</td></tr><tr><td><strong>Input Type</strong></td><td><p>The input method that can be used to enter a value. <strong>Input Type</strong> options include:</p><ul><li><strong>Pre-defined</strong></li><li><strong>Free text</strong></li></ul></td></tr><tr><td><strong>Valid Value</strong></td><td>A comma-separated list of values that are valid as input. You must update the <strong>Valid Value</strong> field when the schema <strong>Input Type</strong> is <strong>Pre-defined</strong>.For example, to create a list of colors that a user can select from, you might enter the following list of valid values: <code>red, yellow, blue</code>.</td></tr><tr><td><strong>Editable</strong></td><td>A switch that can be toggled to specify whether the schema can be edited. <strong>Editable</strong> options are <strong>no</strong> and <strong>yes.</strong><br>You must have the Admin user role to specify whether a schema can be edited.</td></tr></tbody></table>

6\. On the right side of the new table row, click **Save**.

The new schema is saved to the **Reference Data Schema** table and is added as a column to the **Reference Data Values** table on the **Data Values** tab.

### Add values to a reference data set

Populate a reference data set with values to serve as authoritative lookup references for fields that are governed by the reference data set.

**CAUTION:** A reference data value can be added that has the same values in all columns as an existing reference data value, but has a unique identifier assigned to it in the system. If the duplicate values are used in different parts of an organization and one value is updated, then the reference data is no longer consistent across the organization. Verify that a reference data value with all the same values does not already exist before adding a new reference data value.

**Tip:** You can also import reference data schema and values in a CSV file or from a Data Catalog table by clicking **Import** to open the Import Reference Data wizard.

Perform the following steps to add values to a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Click the **Data Values** tab.
4. Click **+ Add Row**.

   **Note:** If the value already exists in a row that is disabled, you can re-enable that row by toggling the **Status** switch to the **Enabled** position.

   A row is added to the **Reference Data Values** table. Columns in the table correspond to the schemas that are defined on the **Schema** tab.
5. Update the new table row with values that adhere to the schema that controls each column.
6. On the right side of the new table row, click **Save**.

The new values are saved to the **Reference Data Values** table.

If you made multiple modifications to the **Reference Data Values** table, consider committing a new version of the reference data set.

## Update a reference data set

Update a reference data set to add or remove information, modify properties, or commit a new version of the reference data set.

You can update a reference data set by completing one or more of the following tasks:

* [Add a business term to a reference data set](#add-a-business-term-to-a-reference-data-set)
* [Update properties of a reference data set](#update-properties-of-a-reference-data-set)
* [Commit a new version of a reference data set](#commit-a-new-version-of-a-reference-data-set)
* [#delete-a-schema-from-a-reference-data-set](#delete-a-schema-from-a-reference-data-set "mention")
* [Remove values from a reference data set](#remove-values-from-a-reference-data-set)

### Add a business term to a reference data set

Add a business term to a reference data set to clarify the context for using the data and to enhance organizational understanding of the data.

Perform the following steps to add a business term to a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Click the **Business Terms** tab.
4. In the **Business Terms** tab, click **Add Terms**.

   The Add Business Terms dialog box opens.
5. Navigate to the business term that you want to add to the reference data set and select it.
6. Click **Add**.

The business term is added to the reference data set and appears in the **Business Terms** table.

### Update properties of a reference data set

Update the properties of a reference data set to reflect changes in data sensitivity and data status or to increment the version number.

Perform the following steps to update the properties of a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Update one or more of the following properties by clicking the pencil icon next to the property:

<table><thead><tr><th width="115.111083984375">Property</th><th>Value options</th></tr></thead><tbody><tr><td>Sensitivity</td><td><ul><li>Unknown (default)</li><li>Low</li><li>Medium</li><li>High</li></ul></td></tr><tr><td>Status</td><td><ul><li>Info (default)</li><li>Valid</li><li>Warning</li><li>Expire</li></ul></td></tr><tr><td>Version</td><td>1.0 (default)<strong>Note:</strong> The version number can only be increased.</td></tr></tbody></table>

4\. Click **Save**.

The updates to the properties of the reference data set are saved.

### Commit a new version of a reference data set

Consider committing a new version of a reference data set after you make multiple modifications to the reference data set.

**Note:** You can also increase the version number in the **Properties** pane of the **Summary** tab.

Perform the following steps to commit a new version of a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Click the **Data Values** tab.
4. Click **Commit**.

   The Please Confirm dialog box opens.
5. Confirm that you want to commit a new version of the reference data set by completing one of the following actions:
   * Keep the version number that is automatically generated by Data Catalog. The automatically generated version number increments the minor version number by 1. For example, for the version number 1.0, the automatically generated number is 1.1.
   * Enter a new version number.
6. Click **Confirm**.

The new version of the reference data set is committed.

You can verify that the version number changed in the Data Set pane at the top of the page.

### Delete a schema from a reference data set

Delete a schema that you do not want your organization to use in the reference data set.

**Important:** Deleted schema cannot be restored.

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to delete, and then select the reference data set.
3. Click the **Schema** tab.
4. Navigate to the schema that you want to delete from the **Reference Data Schema** table.
5. On the right side of the table row with the schema, click the trash can icon.

   The Confirm Deletiondialog box opens.
6. Click **Confirm**.

The schema is deleted from the reference data set and cannot be restored.

### Remove values from a reference data set

Remove values from a reference data set that you do not want your organization to use for the type of data defined in the reference data set.

**Important:** Deleted values cannot be restored.

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Click the **Data Values** tab.
4. Navigate to the value that you want to remove from the **Reference Data Values** table.
5. Remove the value by completing one of the following actions on the right side of the table row with the value:
   * To disable the value, click the pencil icon, and then toggle the **Status** switch to the **Disabled** position.
   * To delete the value, click the trash can icon.

The value is removed from the reference data set.

## Comment on a reference data set

Comment on a reference set so that you can collaborate on the contents or structure of the reference data set with other members of your organization.

Perform the following steps to comment on a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to update, and then select the reference data set.
3. Click the **Comments** tab.
4. (Optional) If the comment box is not visible, scroll to the bottom of the page.
5. In the comment box, enter a comment.
6. (Optional) Edit the comment by using one or more of the following options in the comment box toolbar:
   * Format the comment text by using text formatting options.
   * Attach a picture, video, or link by clicking the associated icon.
   * Apply a code tag to text by selecting the text and clicking the code icon.
7. Click **Submit**.

   The comment is posted to the top of the **Comments** tab.
8. (Optional) To create a Jira Issue related to the comment, click **+ Create Jira Issue**.
9. (Optional) To edit the comment, click the pencil icon.
10. (Optional) To delete the comment, click the trash can icon.

## View activity for a reference data set

View activity to monitor changes to a reference data set, including the timing of the updates, the details of the modifications, and the systems or individuals involved in making the changes.

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to review, and then select the reference data set.
3. Click the **Activity** tab.
4. In the **Activity Status** table, navigate to the activity that you want to review.

   **Tip:** You can use the search and filter functions to find a specific activity.
5. On the right side of the table row with the activity, click **View**.

   The Details window opens with information about modifications to the reference data set.

## Export a reference data set

Export a reference data set for external use, analysis, or archiving.

For example, you might import the reference data set into other systems for downstream comparisons. You can also edit the reference data in a spreadsheet and import the edited data back into Data Catalog.

Perform the following steps to export a reference data set:

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to export, and then select the reference data set.
3. In the **Data Set** pane, click **Actions** > **Export**.

   The reference data set is exported as a CSV file and downloaded to your default download directory.

## Delete a reference data set

Delete a reference data set to permanently remove it from Data Catalog.

**Important:** Deleted reference data sets cannot be restored.

Perform the following steps to delete a reference data set:

You must have the Admin user role to delete a reference data set.

1. Click **Reference Data** in the left navigation menu.

   The Reference Data page opens.
2. In the **Reference Data** menu, navigate to the reference data set that you want to delete.
3. Click the trash can icon next to the reference data set.

   The **Confirm Deletion** dialog box opens.
4. Click **Confirm**.

The reference data set is deleted and cannot be restored.
