# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-simple-measures-in-bulk-to-a-cube.md

# Add simple measures in bulk to a cube

When a cube’s fact table has many fact columns, and you need to create one or more simple measures for each column, you can create simple measures in bulk by defining criteria to select columns and apply an aggregation function to those columns.&#x20;

Complete the following steps to add simple measures to a cube, in bulk:&#x20;

1. Log into the **Pentaho User Console** (PUC). &#x20;
2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens. &#x20;
3. Open the semantic model that contains the cube to which you want to add measures to in bulk by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;
4. Select the cube you want to edit, and then click the **Add a Measure** icon. The **Add a Measure** dialog opens.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> If the <strong>Add a Measure</strong> icon is not visible, click the <strong>More Actions</strong> icon, and then select <strong>Add a Measure</strong>.</p></div>
5. Select **Add Simple Measure**, and then click **Confirm**. The **Add Measure** dialog opens.&#x20;
6. Select **Bulk Measures**. The **Add Measure** window opens with the **Condition** section displayed.&#x20;
7. (Optional) To ensure that measure names are unique inside each cube, in the **Name the Measures** subsection, turn on the **Use Custom Name** toggle to display the **Measure Name** fields and then enter a prefix or suffix or both.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Notes:</strong>  </p><ul><li>By default, measure names are assigned the same name as the related column name.</li><li>If measure names are repeated during bulk creation, the system displays a warning and appends a number to each measure name so that it is unique. The appended number represents the order in which the measure was created (example: Measure (1)). </li><li>When using physical column names to name measures, underscores are replaced with spaces and each word in the column name is capitalized (example: birth_date is changed to Birth Date). </li></ul></div>
8. In the **Select the Criteria** subsection, select the **Subject** that the system should use as criteria when selecting columns during bulk measure creation. Subjects include:&#x20;
   * **All Columns**: Considers all columns of the table.
   * **Column Key**: Selects among the table’s key columns (defined physically as Primary or Foreign Keys in the database) .&#x20;
   * **Column Type**: Matches columns by the column type. &#x20;
   * **Column Name**: Matches columns by using physical names (contains, starts with, ends with).&#x20;
9. (Optional) If you selected a **Subject** that displays an additional option to configure in the **Select the Criteria** subsection, enter the information for that option:&#x20;

   <table><thead><tr><th width="142.22222900390625">Subject </th><th width="132.44439697265625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Column Key </td><td>Key Type* </td><td><p>The type of key that the system looks for when selecting columns during bulk measure creation. Key types include the following options: </p><ul><li>All </li><li>Primary Key </li><li>Foreign Key </li></ul></td></tr><tr><td>Column Type </td><td>Column Type* </td><td>The type of column that the system looks for when selecting columns during bulk measure creation. Types available to choose from are determined by the information in the cube’s fact table. </td></tr><tr><td>Column Name </td><td>Filter* </td><td><p>Filter option and text that the system uses to filter the columns by their name during bulk measure creation. Filter includes the following options: </p><ul><li>Contains </li><li>Ends With </li><li>Starts With </li></ul></td></tr></tbody></table>

   \* Required field&#x20;
10. In the **Define Aggregation** subsection, edit or change the following options:&#x20;

    <table><thead><tr><th width="174.22222900390625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Aggregation</td><td><p>Method used in reports for grouping and calculating data for each one of the new measures that will get created. Aggregation options include:  </p><ul><li>Average </li><li>Count </li><li>Distinct Count </li><li>Maximum </li><li>Minimum </li><li>Sum (default value)</li></ul></td></tr><tr><td>Excluding Columns</td><td>List with the columns that you want the system to exclude from the bulk measure creation process. This list is populated with the fact table columns that matched the criteria previously defined for the bulk measure creation. Leave empty in case you don't want the system to exclude any.</td></tr></tbody></table>
11. Click **Create**. The measures are created and added to the **Measures** node inside the cube.&#x20;
12. Click **Save** to save changes to the model.&#x20;
