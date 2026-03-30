# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-data-identification-methods/pdc-data-patterns.md

# Data patterns

Data patterns are also used to identify data, by discovering patterns in the data that match a regular expression.

## Add a data pattern

In addition to importing an existing data pattern into Data Catalog, you can create a new data pattern to identify data or assign a business term to data.

Use the following steps to add a data pattern from the Data Patterns page:

**Tip:** You can also add a pattern from the Data Canvas by selecting a profiled column and clicking **Actions** > **Create Pattern**, which opens the Create Pattern page. Any pattern that appears on the Data Canvas for the profiled column with a frequency of more than 10% is brought into the Create Pattern page.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **Data Patterns**.

   The Data Patterns page opens.
3. Click **Add Pattern**.

   The Create Pattern page opens.
4. Enter a name for the pattern.
5. (Optional) If you do not want to enable the pattern, toggle the **Pattern Status** switch to disable it.
6. (Optional) Add a description for the pattern.
7. In the **Category** field, select a category, or type a category name and click **Add New** to add it as a new category.

   **Note:** This category is not related to categories used by the Business Glossary.

   You have several different options to assign criteria to aid data discovery.
8. (Optional) In the Column Name Regex pane, use the following steps to set a regex to match the data column name:
   1. Add a regex as a metadata hint for the column name.

      **Note:** The column you select must already be profiled.
   2. In the **Confidence Score** field for the regex, enter a number .00 to 1.0 for each regex snippet to set the metadata score for that regex code.
   3. (Optional) If you want to add another regex, click **Add Regex**.
   4. In the **Confidence Score** field for the whole Column Name Regex pane, enter a weightage number .00 to 1.0.
9. (Optional) In the Content Patterns pane, use the following steps to set a pattern the data content should match:
   1. In the **Pattern Equals** field, enter a pattern for the data.
   2. (Optional) If you want to add another pattern, click **Add Pattern**.
   3. In the **Confidence Score** field for the whole Content Patterns pane, enter a weightage number .00 to 1.0.
10. (Optional) In the Content Regex pane, use the following steps to set a regex the data content should match:

    1. In the **Content Equals** field, enter a regex to match the data content.
    2. (Optional) If you want to add another regex, click **Add Regex**.
    3. In the **Confidence Score** field for the whole Content Regex pane, enter a weightage number .00 to 1.0.

    **Note:** The numbers in the **Confidence Score** fields for the Column Name Regex, Content Patterns, and Content Regex panes need to add up to 1.
11. In the Condition pane, click **Add condition** to add a new condition.

    You can enter **AND** or **OR** statements to evaluate and match the data.
12. In the Actions pane, click **Add Action** to select from the following options:

<table><thead><tr><th width="200.6666259765625">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Assign Tags</strong></td><td>Click <strong>Assign Tags</strong> and enter a tag to assign to the data.</td></tr><tr><td><strong>Assign Table Tags</strong></td><td>Click <strong>Assign Table Tags</strong> and enter a table tag to assign to the data.</td></tr><tr><td><strong>Assign Business Term</strong></td><td><p>Click <strong>Assign Business Term</strong> to select a business term to assign to the data. </p><ol><li>Click <strong>Add Term</strong>. </li><li>Browse the navigation tree for one or more business terms and select the associated checkboxes. <br>A number on the <strong>Add</strong> button shows the number of terms you have selected.</li><li>Click <strong>Add</strong>.</li></ol></td></tr></tbody></table>

13\. Click **Create Pattern** to add the pattern.

The new pattern is added.

You can also see an [example of adding a data pattern](#example-of-adding-a-data-pattern).

### Example of adding a data pattern

If the data you want to identify follows a particular pattern that can be expressed with a regular expression (regex), you can create a data pattern to identify the data. Some common examples are phone numbers, email IDs, or IP addresses. This example shows the process of creating a data pattern to find email addresses.

The formula for calculating a confidence score for a pattern is as follows:

Confidence score = (Metadata Hint score \* weightage) + (Pattern score \* weightage) + (Regex score \* weightage)

* The Metadata hint score is derived from the Column Name Regex pane.
* The Pattern score is derived from the Content Patterns pane.
* The Regex score is derived from the Content Regex pane, which is not shown in this example, since it is optional.

To create a data pattern, in the left navigation menu, click **Data Operations** and on the Data Identification Methods card, click **Data Patterns**. Then, on the Data Patterns page, click **Add Pattern**.

Add basic information for the pattern as shown in the following screen. In this example, the pattern is called `Email pattern`, and the category `eMail` is assigned.

![Adding name, description and category](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-2333fce203631d170fee739ec363a9f48d21fdfe%2FPDC%20Add%20Pattern%20example%20screen1%20\(Create%20Pat\).png?alt=media)

Then you add the regex to match the column name. In the example below, the regex `[Ee]mail` has the confidence score `0.8`, and the regex `[Ee]mailID` has the confidence score `0.2`. The overall weightage of the **Column Name Regex** is `0.5`.

![Adding a column name regular expression](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-51e48101ed02e16e4bfc6dc2c43fdc7485eec934%2FPDC%20Add%20Pattern%20example%20screen2%20\(Column%20Name%20regex\).png?alt=media)

Then you can enter either a content pattern or content regex. In this example, content regex is added that will match any email ID, and the weightage `0.5` is assigned.

![Adding a content regular expression](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-699a3e9837fd5c8c91a62fbf69632ef529ad3509%2FPDC%20Add%20Pattern%20example%20screen3%20\(Content%20Regex\).png?alt=media)

You need to add a condition. Here, the example is looking for data with a metadata score greater than `0.5` and a confidence score greater than `0.3`.

![Add a condition](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-d2a96f2c121973e0e02e4a1fef09d49c280226cc%2FPDC%20Add%20Pattern%20example%20screen4%20\(Condition\).png?alt=media)

Then you set the action to be taken when the data is matched. In this example, the tags `eMail` and `Sensitive` are applied.

![Setting an action](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-46a15875bb7abf6fe5a243e04735336ebe453315%2FPDC%20Add%20Pattern%20example%20screen5%20\(Action\).png?alt=media)

Now the pattern can be added by clicking **Create Pattern**.

## View data patterns

In Data Catalog, perform the following steps to view the available data patterns.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **View Methods** or **Data Patterns**.

   You can view the list of data patterns under the **Patterns** tab.
3. Locate the data patterns you want to view in the table and select the More options icon (<img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media" alt="" data-size="line">) at the end of its row, then select **View**.

   You can view the Pattern details in JSON format.

## Edit data patterns

In Data Catalog, you can edit data patterns to modify existing or create new regular expressions to improve the accuracy and relevance of pattern matching. By updating data patterns, you can address evolving data formats, refine existing patterns, and ensure proper identification of data elements across datasets.

Perform the following steps to edit an existing data pattern in Data Catalog:

**Note:** The default data patterns in Data Catalog cannot be edited. However, you can modify custom data patterns that are created.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **View Methods** or **Data Patterns**.

   You can view the list of data patterns under the **Patterns** tab.
3. Locate the data patterns you want to view in the table and select the More options icon (![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media)) at the end of its row, then select **Edit**.
4. You can update the data pattern's name and description, and toggle the **Pattern Status** switch to disable or enable as needed.
5. In the **Category** field, select a category or type a category name and click **Add New** to add it as a new category. You can also remove an existing category.

   **Note:** This category is not related to categories used by the Business Glossary.

   You have several different options to assign criteria to aid data discovery.
6. (Optional) In the Column Name Regex pane, you can click the **Delete** icon to remove the exiting regex or use the following steps to set an additional regex to match the data column name:
   1. Add a regex as a metadata hint for the column name.

      **Note:** The column you select must already be profiled.
   2. In the **Confidence Score** field for the regex, enter a number 0.00 to 1.0 for each regex snippet to set the metadata score for that regex code.
7. (Optional) In the Content Patterns pane, you can click the **Delete** icon to remove the existing pattern or use the following steps to set an additional pattern the data content should match:
   1. Click **Add Pettern**, and then in the **Pattern Equals** field, enter a pattern for the data.
   2. In the **Confidence Score** field for the whole Content Patterns pane, enter a weightage number 0.00 to 1.0.
8. (Optional) In the Content Regex pane, can click the **Delete** icon to remove the existing regex or use the following steps to set an additional regex the data content should match:

   1. click **Add Regex**, and then in the **Content Equals** field, enter a regex to match the data content.
   2. In the **Confidence Score** field for the whole Content Regex pane, enter a weightage number 0.00 to 1.0.

   **Note:** The numbers in the **Confidence Score** fields for the Column Name Regex, Content Patterns, and Content Regex panes need to add up to 1.
9. In the **Condition** pane, you can click the **Delete** icon and remove the existing condition or click **Add Condition** to add a new condition. You can enter either **AND** or **OR** statements to evaluate and match the data.
10. In the Actions pane, you can click the **Delete** icon and remove existing actions, or to add additional actions, click **Add Action** to select from the following options:

<table><thead><tr><th width="206.22222900390625">Option</th><th>Description</th></tr></thead><tbody><tr><td><strong>Assign Tags</strong></td><td>Click <strong>Assign Tags</strong> and enter a tag to assign to the data.</td></tr><tr><td><strong>Assign Table Tags</strong></td><td>Click <strong>Assign Table Tags</strong> and enter a table tag to assign to the data.</td></tr><tr><td><strong>Assign Business Term</strong></td><td><p>Click <strong>Assign Business Term</strong> to select a business term to assign to the data.</p><ol><li>Click <strong>Add Term</strong>. </li><li>Browse the navigation tree for one or more business terms and select the associated checkboxes. <br>A number on the <strong>Add</strong> button shows the number of terms you have selected.</li><li>Click <strong>Add</strong>.</li></ol></td></tr></tbody></table>

11\. Click **Save Pattern** to save the data pattern.

You have successfully updated the existing pattern in Data Catalog.

## Import data patterns

In Data Catalog, you can import data patterns by uploading a JSON or ZIP file, which contains details of patterns and minimizes the risk of errors due to manual input.

Perform the following steps to import data patterns in Data Catalog.

Ensure you have a JSON or ZIP file that contains all details of patterns. If you are migrating from different Data Catalog instances, you can export patterns in the ZIP file containing JSON files. For more information, see [Export data patterns](#export-data-patterns).

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click Patterns.

   The Data Patterns page opens.
3. Click **Import**.

   The **Import Pattern** dialog box opens.
4. Upload the JSON or ZIP file, which contains the details of data patterns, and click **Continue**.

   It starts uploading the connections and configuring the data source connections. You can click **View Workers** and monitor the process. For more information about tracking the progress, see [Manage worker processes](https://docs.pentaho.com/pdc-admin/manage-worker-processes-cp).

   A sample JSON file:

   ![Data patterns JSON file](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-942dcb42d282c0f37b793c3bbeffc0072e6cf33e%2FData_Identification_Patterns_JSON_file.png?alt=media)

You have successfully imported the data patterns into Data Catalog.

You can also export data patterns from Data Catalog. See [Export data patterns](#export-data-patterns) for more information.

## Export data patterns

In Data Catalog, you can export data patterns to create a backup of all details of data patterns and use them to migrate connections from one instance to another, ensuring consistency and reducing manual errors.

Perform the following steps to export data patterns in Data Catalog:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Data Identification Methods** card, click **Data Patterns**.

   The **Data Patterns** page opens.
3. Click **Export**.

   This downloads a ZIP file that contains details of data patterns in JSON formats.

You have successfully exported data patterns available in Data Catalog.

You can also import the data patterns into Data Catalog. See [Import data patterns](#import-data-patterns) for more information.
