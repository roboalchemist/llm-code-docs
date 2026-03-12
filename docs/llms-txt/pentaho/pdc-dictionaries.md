# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-data-identification-methods/pdc-dictionaries.md

# Dictionaries

A dictionary is a list of words that you can use to match column data. Typically, dictionary words are those that you could not write a pattern to match, such as country codes. There are two kinds of dictionaries, system-defined and user-defined. System-defined dictionaries come with Data Catalog and user-defined dictionaries are created by Data Catalog users.

You can add a user-defined dictionary in three ways:

* by importing a CSV file zipped with a JSON file containing the definition of the dictionary.
* by uploading a CSV file and creating the JSON file to define the dictionary by entering information in the UI.
* by selecting a profiled column of data from any JDBC table or file.

  **Note:** If you create a dictionary from a column, this dictionary only works for structured data, and is unavailable for unstructured data.

## Add a dictionary

In addition to importing an existing dictionary into Data Catalog, you can add a dictionary using a CSV file or a profiled column of data.

**Note:** You can only use a profiled column to create a dictionary for structured data. You cannot use a dictionary that was created using a column for unstructured data.

Before beginning this procedure, you must have a CSV file or a profiled column of data with words you want to be in the new dictionary.

Use the following steps to add a dictionary from the Dictionaries page:

**Tip:** You can also add a dictionary from the Data Canvas, by selecting a profiled column and clicking **Actions** > **Create Dictionary**, which opens the Create Dictionary page.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **Dictionaries**.

   The Dictionaries page opens.
3. Click **Add Dictionary**.

   The Create Dictionary page opens. The asterisks next to **Name** and **Category** indicate these are mandatory fields.
4. Enter a name for the dictionary.
5. (Optional) If you do not want to enable the dictionary, toggle the **Dictionary Status** switch to disable it.
6. (Optional) Add a description for the dictionary.
7. In the **Category** field, select a category, or type a category name and click **Add New** to add it as a new category.

   **Note:** This category is not related to categories used by the Business Glossary.
8. In the Apply Values pane, select one of the following methods to add a dictionary:

<table><thead><tr><th width="194.00006103515625">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Upload Dictionary</strong></td><td>Click <strong>Upload Dictionary</strong> to upload a one-column CSV file containing dictionary file definitions and enter a number .00 to 1.0 for the confidence score.</td></tr><tr><td><strong>Select Column</strong></td><td><p>Click <strong>Select Column</strong> to set a profiled column of data to use for the dictionary.</p><ol><li>Click <strong>Add Column</strong> to browse the navigation tree for a column to add for dictionary values.</li><li>Select the column you want to use. <br><strong>Note:</strong> The column you select must already be profiled.</li><li>Click <strong>Update</strong>.</li><li>Enter a number 0.00 to 1.0 for the confidence score.</li></ol></td></tr></tbody></table>

You then have several different options to assign criteria to aid data discovery.

9. (Optional) In the **Column Name Regex** pane, use the following steps to set a regex to match the data column name:
   1. Add a regex as a metadata hint for the column name.
   2. In the **Confidence Score** field for the regex, enter a number 0.00 to 1.0 to set the metadata score for that regex code.
   3. (Optional) If you want to add another regex, click **Add Regex**.
   4. In the **Confidence Score** field for the whole Column Name Regex pane, enter a weightage number 0.00 to 1.0.
10. In the Condition pane, click **Create condition** and select an **Attribute**, **Operator,** and **Value** to set a condition.

    You can click **Add condition** to add another condition. Select **AND** or **OR** to apply multiple conditions to evaluate and match the data.
11. In the **Actions** pane, click **Add Action** to select from the following options:

<table><thead><tr><th width="192.88885498046875">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Assign Tags</strong></td><td>Click <strong>Assign Tags</strong> and enter a tag to assign to the data.</td></tr><tr><td><strong>Assign Table Tags</strong></td><td>Click <strong>Assign Table Tags</strong> and enter a table tag to assign to the data.</td></tr><tr><td><strong>Assign Business Term</strong></td><td>Click <strong>Assign Business Term</strong> to select a business term to assign to the data. 1. Click <strong>Add Term</strong>. 2. Browse the navigation tree for one or more business terms and select the associated check boxes. A number on the <strong>Add</strong> button shows the number of terms you have selected. 3. Click <strong>Add</strong>.</td></tr></tbody></table>

12\. Click **Create dictionary** to add the dictionary.

The new dictionary is added.

You can also see an [example of creating a dictionary](#example-of-creating-a-dictionary).

### Example of creating a dictionary

If the data you want to identify doesn't follow any particular pattern, you can create a dictionary to identify the data. This example shows the process of creating a dictionary to find first names, using an uploaded CSV file.

The formula for calculating a confidence score for a dictionary is as follows:

Confidence score = (Similarity \* weightage) + (Metadata hint score \* weightage)

* Similarity is derived from comparing the data to the information in the uploaded CSV file.
* The Metadata hint score is derived from the Column Name Regex pane.
* The Similarity value and Column Name Regex should add up to 1.

To create a dictionary, in the left navigation menu, click **Data Operations** and on the Data Identification Methods card, click **Dictionaries**. Then, on the Dictionaries page, click **Add Dictionary**.

Add basic information for the dictionary as shown in the following screen. In this example, the dictionary is called `Firstname Dict`, and the categories `Sensitive` and `Firstname Dict` are assigned. The category **Firstname Dict** is added as a new category.

![Adding name, description, and category](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-0629422767a9c9acd33142170a318a3b357de9c3%2FPDC%20Add%20Dict%20example%20screen1%20\(Create%20Dict\).png?alt=media)

Then you must set the input for calculating the confidence score. The confidence score for the Apply Values pane and the Column Name Regex panes are used to create the **Condition**.

In the **Apply Values** pane, you must add a single column CSV file with a word list to use to create the dictionary. In this example, the file `chinook_firstnames_list.csv` has been added, and the overall weightage is set to `0.6`.

![Uploading a CSV file](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-086fa581318315c7b45397b95ea0a0f5620f9912%2FPDC%20Add%20Dict%20example%20screen2%20\(Apply%20Values\).png?alt=media)

Data Catalog compares this list in the dictionary to the column data, and based on that, it generates a similarity score.

In the Column Name Regex pane, you must add one or more regular expressions to match the data. Data that matches provides a metadata score. The screen below shows the regex `[Ff]irst[Nn]ame` being added with the confidence score `0.7`, and the regex `[Nn]ame` being added with the confidence score `0.3`, with the overall weightage for the column name regex as `0.4`.

![Adding a column name regular expression](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-9ac176fb5f67f4069da164df1a899d75690e9fdc%2FPDC%20Add%20Dict%20example%20screen3%20\(Column%20Name%20Regex\).png?alt=media)

You need to create one or more conditions to match the data. The screen below shows a condition that will match data if the attribute **Confidence Score** is **Greater than** `0.5` OR the attribute **Metadata Score** is **Greater than** `0.5`.

![Adding a condition](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-b11df1d165e3ae927c5de793ba2d6b3914a020a1%2FPDC%20Add%20Dict%20example%20screen4%20\(Condition\).png?alt=media)

Once the conditions are met, an action is applied to the data that is matched. The Actions pane in the example below indicates that the tags **Firstname** and **Sensitive** are applied to matching data.

![Setting an action](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-cb9bc25169ccff9e91ef439ce1677e310be6c2ba%2FPDC%20Add%20Dict%20example%20screen5%20\(Action\).png?alt=media)

Now the dictionary can be added by clicking **Create Dictionary**.

## View dictionaries

In Data Catalog, perform the following steps to view the available dictionaries:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **View Methods** or **Dictionaries**.

   You can view the list of dictionaries under the **Dictionaries** tab.
3. Locate the dictionaries you want to view in the table and select the More options icon (![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media)) at the end of its row, then select **View**.

   For **Dictionaries**, to view the JSON file details, click the **Rules** tab.

   It provides insight into logic for the dictionary to apply tags mentioned in the JSON file, such as conditions and confidence scores. Based on these data factors, you can apply dictionaries to datasets.

   For example, in the following JSON file the dictionary rule specifies that the type is "Dictionary". The confidence score is calculated based on the weighted sum of "similarity" and "metadataScore" with conditions set to apply when the confidence score is greater than or equal to 0.7 and the column cardinality is greater than or equal to 1. If these conditions are met, the action is to apply the tag "General" to the dataset. This demonstrates how the provided logic guides the application of tags to datasets based on specified criteria.

   ```
   [ 
       { 
           "__typename": "dictionariesRules", 
           "type": "Dictionary", 
           "minSamples": 200, 
           "confidenceScore": { 
               "+": [ 
                   { 
                       "*": [ 
                           { 
                               "var": "similarity" 
                           }, 
                           0.9 
                       ] 
                   }, 
                   { 
                       "*": [ 
                           { 
                               "var": "metadataScore" 
                           }, 
                           0.1 
                       ] 
                   } 
               ] 
           }, 
           "condition": { 
               "and": [ 
                   { 
                       ">=": [ 
                           { 
                               "var": "confidenceScore" 
                           }, 
                           "0.7" 
                       ] 
                   }, 
                   { 
                       ">=": [ 
                           { 
                               "var": "columnCardinality" 
                           }, 
                           "1" 
                       ] 
                   } 
               ] 
           }, 
           "actions": [ 
               { 
                   "applyTags": [ 
                       { 
                           "k": "General" 
                       } 
                   ] 
               } 
           ] 
       } 
   ] 
   ```

## Edit dictionaries

In Data Catalog, you can edit dictionaries to modify, update, or expand existing dictionaries to accommodate changes in business requirements, improve data accuracy, and address discrepancies. Whether you are correcting errors, adding new values, or aligning with evolving organizational standards, by updating dictionaries, you can ensure that data profiling and classification remain relevant and accurate.

Perform the following steps to edit an existing dictionary in Data Catalog:

**Note:** The default dictionaries in Data Catalog cannot be edited. However, you can modify custom dictionaries that are created.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **View Methods** or **Dictionaries**.

   You can view the list of dictionaries under the **Dictionaries** tab.
3. Locate the dictionaries you want to view in the table and select the More options icon (![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media)) at the end of its row, then select **Edit**.
4. You can update the dictionary's name and description, and toggle the **Dictionary Status** switch to disable or enable as needed.
5. In the **Category** field, select a category or type a category name and click **Add New** to add it as a new category. You can also remove an existing category.

   **Note:** This category is not related to the categories used in the Business Glossary.
6. In the **Apply Values** pane, select one of the following methods to update a dictionary:

<table><thead><tr><th width="175.111083984375">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Upload Dictionary</strong></td><td>Click <strong>Upload Dictionary</strong> to upload a one-column CSV file containing dictionary file definitions and enter a number 0.00 to 1.0 for the confidence score.</td></tr><tr><td><strong>Select Column</strong></td><td><p>Click <strong>Select Column</strong> to set a profiled column of data to use for the dictionary.</p><ol><li>Click <strong>Add Column</strong> to browse the navigation tree for a column to add for dictionary values. </li><li>2. Select the column you want to use. <br><strong>Note:</strong> The column you select must already be profiled.</li><li>Click <strong>Update</strong>.</li><li>Enter a number 0.00 to 1.0 for the confidence score.</li></ol></td></tr></tbody></table>

You then have several different options to assign criteria to aid data discovery.

7. (Optional) In the **Column Name Regex** pane, you can click the **Delete** icon to remove the existing regex or click **Add Regex** and use the following steps to set an additional regex to match the data column name:
   1. Add a regex as a metadata hint for the column name.
   2. In the **Confidence Score** field for the regex, enter a number 0.00 to 1.0 to set the metadata score for that regex code.
8. In the **Condition** pane, you can click the **Delete** icon and remove the existing condition or click **Add Condition** and select an **Attribute**, **Operator**, and **Value** to set an additional condition. Select either **AND** or **OR** to apply multiple conditions to evaluate and match the data.
9. In the **Actions** pane, you can click the **Delete** icon and remove existing action, or to add additional actions, click **Add Action** to select from the following options:

<table><thead><tr><th width="207.3333740234375">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Assign Tags</strong></td><td>Click <strong>Assign Tags</strong> and enter a tag to assign to the data.</td></tr><tr><td><strong>Assign Table Tags</strong></td><td>Click <strong>Assign Table Tags</strong> and enter a table tag to assign to the data.</td></tr><tr><td><strong>Assign Business Term</strong></td><td><p>Click <strong>Assign Business Term</strong> to select a business term to assign to the data. </p><ol><li>Click <strong>Add Term</strong>. </li><li>Browse the navigation tree for one or more business terms and select the associated checkboxes. <br>A number on the <strong>Add</strong> button shows the number of terms you have selected. </li><li>Click <strong>Add</strong>.</li></ol></td></tr></tbody></table>

10\. Click **Save dictionary** to update the dictionary.

You have successfully updated the existing dictionary in Data Catalog.

## Import dictionaries

In Data Catalog, you can import dictionaries by uploading a ZIP file that contains details of dictionaries in CSV or JSON formats and minimize the risk of errors due to manual input.

Perform the following steps to import custom dictionaries in Data Catalog.

Ensure you have a ZIP file that contains all details of dictionaries in the CSV or JSON formats. If you are migrating from different Data Catalog instances, you can export dictionaries in the ZIP file containing CSV and JSON files. For more information, see [Export dictionaries](#export-dictionaries).

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **Dictionaries**.

   The **Dictionaries** page opens.
3. Click **Import**.

   The **Import Dictionary** dialog box opens.
4. Upload the ZIP file, which contains the details of dictionaries in CSV and JSON files, and click **Continue**.

   It starts uploading and adding dictionaries into Data Catalog. You can click **View Workers** and monitor the process. For more information about tracking the progress, see [Manage worker processes](https://docs.pentaho.com/pdc-admin/manage-worker-processes-cp).

   Sample JSON and the CSV files:\
   ![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2FiyTRKmP3aICnW3a2yIat%2Fimage.png?alt=media\&token=4fc8448b-78ba-4f53-aaf0-ba949793fa03)\
   \
   ![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2FqmSiDynTYZWBYuE4cIEe%2Fimage.png?alt=media\&token=d9f462fd-26b6-4826-af1f-334296ca2dd5)

You have successfully imported the dictionaries into Data Catalog.

You can also export dictionaries from Data Catalog. See [Export dictionaries](#export-dictionaries) for more information.

## Export dictionaries

In Data Catalog, you can export dictionaries to create a backup of all dictionaries and use them to migrate connections from one instance to another, ensuring consistency and reducing manual errors.

Perform the following steps to export dictionaries in Data Catalog:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **Dictionaries**.

   The **Dictionaries** page opens.
3. Click **Export**.

   This downloads a ZIP file containing details of dictionaries in CSV and JSON formats.

You have successfully exported dictionaries available in Data Catalog.

You can also import the dictionaries into Data Catalog. See [Import dictionaries](#import-dictionaries) for more information.
