# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-dimension-to-a-cube.md

# Add a dimension to a cube

Add a dimension that describes aggregated data in a cube so that the data can be grouped for analysis. You can either create a new cube while adding the dimension or add the dimension to an existing cube.&#x20;

Complete the following steps to add a table or view as a dimension of a cube:&#x20;

1. Log into the **Pentaho User Console** (PUC)**.**&#x20;

2. Open the Semantic Model Editor by taking one of the following actions:

   * If you are using the Modern Design of PUC, in the menu on the left side of the page, click **Semantic Model Editor**.
   * If you are using the Classic Design of PUC, click **File** > **Semantic Model Editor**.&#x20;

   The **Semantic Model Editor** opens.&#x20;

3. Open the semantic model to which you are adding a cube or editing a cube by completing the following sub steps:&#x20;
   1. In the **Semantic Models** list, navigate to the model you want to open by searching or scrolling through the list.&#x20;
   2. Click **Open**. The model opens in the canvas.&#x20;

4. In the **Data Source** tab, navigate to the table or view that you want to use as a dimension.&#x20;

5. (Optional) To preview data in the table or view, click the **Preview** icon next to the table or view. The **Preview Data** panel opens. You can take one or more of the following additional actions while previewing the data:&#x20;

   * Hover over a column header to see metadata information for that column.
   * Click a column header to sort the table by the data in that column.&#x20;
   * Click the **Preview** icon again to close the **Preview Data** panel.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can preview one table or view at a time. By default, the maximum number of rows shown is 100. The administrator can change the maximum value by editing the <code>row-limit</code> property in the <code>application.properties</code> file, located in: <code>\Pentaho\server\pentaho-server\pentaho-solutions\system\semantic-model-editor</code>. The administrator must restart the Server for the new row value maximum to take effect.</p></div>

6. To add a table or view as a dimension, take one of the following actions: &#x20;

   * For an existing cube, drag and hold the table or view over the cube until the **Do you want to:** dialog opens, and then drop the table or view onto the **Use as Dimension** option.&#x20;
   * To create a new cube, drag and hold the table or view over a blank area of the canvas until the **Do you want to:** dialog opens, and then drop the table or view onto the **Use as Dimension** option.  &#x20;

   A dimension is created with one hierarchy that has one level, and the **Dimension Editor** window opens with the top position of the Dimension tree selected.&#x20;

7. Edit options for the dimension by completing the following sub steps:&#x20;
   1. In the **Dimension Name** section, enter a unique **Name** within the cube.&#x20;
   2. (Optional) If the dimension is not linked to a facts table in the cube, in the **Connect to the Facts Table** section, select the **Fact Table Column** that you want to link to the dimension.&#x20;

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> If the cube does not have a facts table defined, you must first add a fact table to cube. For details, see <a href="add-a-fact-table-to-a-cube">Add a fact table to a cube</a>.</p></div>
   3. In the **Dimension Type** section, for the **Type** of dimension you want to use, select one of the following options:&#x20;

      <table><thead><tr><th width="174.22222900390625">Option </th><th>Description </th></tr></thead><tbody><tr><td>StandardDimension </td><td>A dimension used for basic analysis. <strong>StandardDimension</strong> is the default value. </td></tr><tr><td>TimeDimension </td><td>A dimension used for time-based analysis. A time dimension might have annotations like Year, Month, and Week. </td></tr></tbody></table>

8. (Optional) Expand the **Optional Information** section and edit one or more of the following options:

   <table><thead><tr><th width="125.111083984375">Option </th><th>Description </th></tr></thead><tbody><tr><td>Visible </td><td>Value indicating whether the dimension element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Usage Prefix </td><td>String of text added to the beginning of the column name when building collapsed dimension aggregates to disambiguate the dimension usage. Usage prefixes enable the system to accurately recognize and associate columns during aggregate table matching. </td></tr></tbody></table>

9. (Optional) Expand the **Describe Dimension** section and edit one or more of the following options:&#x20;

   <table><thead><tr><th width="124.88885498046875">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the dimension's name. You can use captions to provide a user-friendly label for reports or for localization so that the dimension's name appears in the local language. </td></tr><tr><td>Description </td><td>Description of the dimension. </td></tr></tbody></table>

10. In the Dimension tree, select the hierarchy that was created when you added the dimension.&#x20;

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can add more than one hierarchy to a dimension. </p></div>

11. Edit the options for the hierarchy by completing the following sub steps:&#x20;
    1. In the **Hierarchy Name** section, enter a unique **Name**.

       <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> All hierarchies in a dimension must have a unique name. An empty name is considered unique and can be used only once for a hierarchy in the dimension.</p></div>
    2. In the **Mandatory Data** section, enter information for the following options:

       <table><thead><tr><th width="135.5555419921875">Option </th><th>Description </th></tr></thead><tbody><tr><td>Source Table* </td><td>Table used as the source of data for the hierarchy. </td></tr><tr><td>Alias </td><td>Unique text string used as an alias for the table in queries. You can assign an alias to a table used in multiple hierarchies to ensure that SQL queries work correctly. By default, the table name is used in queries. </td></tr><tr><td>Hierarchy Key </td><td>Column from the hierarchy source table used to connect the hierarchy to the cube’s fact table, enabling accurate joins between dimension data and fact data during query execution. </td></tr><tr><td>Has All* </td><td>Value indicating whether the hierarchy has an “all” member. The "all" member is the parent of all other hierarchy members, representing the total. The default value is <strong>true</strong>. </td></tr></tbody></table>

       &#x20;\*Required
    3. (Optional) Expand the **Optional Information** section and edit one or more of the following options:&#x20;

       <table><thead><tr><th width="121.77783203125">Option</th><th>Description</th></tr></thead><tbody><tr><td>Visible </td><td>Value indicating whether the hierarchy element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>.   </td></tr><tr><td>All Member Name</td><td>Name of the "all" member. The default value is "All <code>Hierarchy Name</code>" , for example: '"All Store" in case the hierarchy name was <strong>Store</strong><em>.</em></td></tr><tr><td>All Member Caption</td><td>String of text that is displayed instead of the All Member's name. You can use captions to provide a user-friendly label for reports or for localization so that the name appears in the local language. </td></tr><tr><td>All Level Name</td><td>Name of the "all" level member. The default value is "<strong>(All)</strong>".</td></tr><tr><td>Default Member</td><td>String value representing the default member of the hierarchy. A valid multidimensional (MDX) identifier is expected, for example: <code>[Time].[1997].[Q1].[1]</code></td></tr><tr><td>Member Reader Class</td><td>String value of the member reader class, in case you want to apply some customized transformation to the original data. The class provided needs to implement the following interface: <code>mondrian.rolap.MemberReader</code></td></tr><tr><td>Origin</td><td>Unsigned Short value that determines the source of the hierarchy according to the following values: 1-identifies levels in a user defined hierarchy; 2-identifies levels in an attribute hierarchy; 4-identifies levels in attribute internal hierarchies, that are not enabled; 8-identifies levels in a key attribute hierarchy. The default value is 1 (user defined), except for Measures that it is 6 (attribute + attribute internal).</td></tr><tr><td>Display Folder</td><td>String value to specify the folder in which to list the hierarchy for users in <strong>Pentaho Analyzer</strong>.</td></tr><tr><td>Unique Key Level Name</td><td>Select one of the existent hierarchy levels. Used to indicate that the given level taken together with all higher levels in the hierarchy acts as a unique alternate key, ensuring that for any unique combination of those level values, there is exactly one combination of values for all levels below it.</td></tr></tbody></table>
    4. (Optional) Expand the **Describe Hierarchy** section and edit one or more of the following options:&#x20;

       <table><thead><tr><th width="116.888916015625">Option</th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the hierarchy’s name. You can use captions to provide a user-friendly label for hierarchies or for localization so that the hierarchy’s name appears in the local language. </td></tr><tr><td>Description </td><td>Description of the hierarchy. </td></tr></tbody></table>

12. In the Dimension tree, select the level of the hierarchy that was created when you added the dimension. For example, the default level is named “Level1”.

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> You can add more than one level to a hierarchy. </p></div>

13. Edit the options for the level by completing the following sub steps:&#x20;

    1. In the **Level Name** section, enter a unique **Name**.

       <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> All levels in a hierarchy must have a unique name. An empty name is considered unique and can be used only once for a level in the hierarchy.</p></div>
    2. In the **Level Source** section, which presents the **Source Table** previously chosen for the hierarchy, select a value for the following option:&#x20;

    <table><thead><tr><th width="123.5555419921875">Option </th><th>Description </th></tr></thead><tbody><tr><td>Column </td><td>Column of the source table that you want to use for the level.  If a column is not selected, a <code>KeyExpression</code> must be defined in the Advanced mode instead or an error occurs when you try to save the model. For details, see <a href="../../advanced-mode">Advanced mode</a>.</td></tr></tbody></table>

14. In the **Relevant Information** section, edit one or more of the following options:&#x20;

    <table><thead><tr><th width="142.22222900390625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Name Column </td><td><p>Column of the source table that contains the user identifier of the level., i.e., the value the user sees in each row of the reports representing each member of the level. </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Instead of selecting a specific column, you can define a <code>NameExpression</code> in the <code>Level</code> element of a SQL expression to use as the user identifier. For details, see <a href="../../advanced-mode">Advanced mode</a>.</p></div></td></tr><tr><td>Ordinal Column </td><td><p>Column of the source table that contains the member ordinals for the level. </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> If the Ordinal Column is not specified, the key column is used for ordering. Instead of selecting a specific column, you can define an <code>OrdinalExpression</code> in the <code>Level</code> element of a SQL expression to use for ordering. For details, see <a href="../../advanced-mode">Advanced mode</a>.</p></div></td></tr></tbody></table>

15. (Optional) Expand the **Optional Information** section and edit one or more of the following options:

    <table><thead><tr><th width="204.44439697265625">Option </th><th>Description </th></tr></thead><tbody><tr><td>Visible  </td><td>Value indicating whether the level element is visible in the <strong>Pentaho Analyzer</strong> design environment. Elements that are not visible cannot be accessed directly in <strong>Pentaho Analyzer</strong> to use in reports. However, hidden elements can still be used to build expressions and conditions that are internally evaluated by the Mondrian engine for reporting. The default value is <strong>true</strong>. </td></tr><tr><td>Approximate Row Count  </td><td>Estimated number of members in the level. Setting an approximate row count can improve performance of running reports that use the cube. </td></tr><tr><td>Null Parent Value  </td><td>Value that identifies null parents in a parent-child hierarchy. Typical values are NULL and 0. </td></tr><tr><td>Key Column Type  </td><td><p>The type of data in the key column for the level. Types of data include STRING, NUMERIC, INTEGER, BOOLEAN, DATE, TIME, and TIMESTAMP. </p><p> </p><p>When generating SQL statements, Mondrian encloses values for String columns in quotation marks but leaves values for Integer and Numeric columns un-quoted. Date, Time, and Timestamp values are quoted according to the SQL dialect. For an SQL-compliant dialect, the values appear prefixed by their type name, for example, DATE '2006-06-01'. </p></td></tr><tr><td>Internal Type  </td><td><p>The Java type that Mondrian uses to store the level's key column. Types include INT, LONG, OBJECT, and STRING.  </p><p> </p><p>The Internal Type value also determines the JDBC method that Mondrian calls to retrieve the column. For example, if the Java type is INT, Mondrian calls <code>ResultSet.getInt(int)</code>. </p><p> </p><p>Usually, the Internal Type attribute is not needed, because Mondrian chooses a type based on the type of database column. </p></td></tr><tr><td>Unique Members  </td><td>Value that indicates whether members are unique across all parents in the level. For example, zip codes are unique across all states. Members of the first level are always unique. The default value is <strong>false</strong>. </td></tr><tr><td>Level Type  </td><td>Value that indicates whether the level is a regular or a time-related level. The level type is important for time-related functions such as YTD (year-to-date). The available values are conditioned by the Dimension Type. When the Dimension Type is <strong>StandardDimension</strong>, then the only possible value for the Level Type is <strong>Regular</strong>. When the Dimension Type is <strong>TimeDimension</strong> , then you can choose as Level Type one of: <strong>TimeUndefined</strong>, <strong>TimeYears</strong>, <strong>TimeHalfYears</strong>, <strong>TimeQuarters</strong>, <strong>TimeMonths</strong>, <strong>TimeWeeks</strong>, <strong>TimeDays</strong>, <strong>TimeHours</strong>, <strong>TimeMinutes</strong>, <strong>TimeSeconds</strong>.</td></tr><tr><td>Hide Member If  </td><td><p>Value that indicates when a member of the level is hidden.  </p><ul><li><strong>Never</strong>: Member is never hidden. </li><li><strong>IfBlankName</strong>: Member is hidden if its name is null or empty. </li><li><strong>IfParentsName</strong>: Member is hidden if its name matches the parent’s name. </li></ul><p>The default value is <strong>Never</strong>. </p></td></tr><tr><td>Formatter Class  </td><td><p></p><div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>Important:</strong> This attribute is deprecated and might be removed in a future release. To ensure compatibility, instead of using this attribute, use a nested <strong>MemberFormatter</strong> inside the <strong>Level</strong> element in Advanced mode. For details, see <a href="../../advanced-mode">Advanced mode</a>.</p></div><p>Formatter class name for the member labels displayed. The class must implement the <code>mondrian.olap.MemberFormatter</code> interface. </p><p></p><p> A formatter class is a user-defined Java class for customizing how values are displayed so that you can format data beyond default settings, such as applying custom date formats, currency symbols, or localized labels. </p></td></tr><tr><td>Caption Column  </td><td><p>The name of the column in the source table that holds the caption for members. Captions are a string of text that is displayed instead of the member's name. </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Instead of selecting a specific column, you can define a <code>CaptionExpression</code> in the <code>Level</code> element of a SQL expression to use as the caption. For details, see <a href="../../advanced-mode">Advanced mode</a>.</p></div></td></tr><tr><td>Parent Column  </td><td><p>The name of the column in the source table that references the parent member in a parent-child hierarchy. </p><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> Instead of selecting a specific column, you can define a <code>ParentExpression</code> in the <code>Level</code> element of a SQL expression to use as the parent. For details, see <a href="../../advanced-mode">Advanced mode</a>.</p></div></td></tr></tbody></table>

16. (Optional) Expand the **Describe Level** section and edit one or more of the following options:

17. <table><thead><tr><th width="133.111083984375">Option </th><th>Description </th></tr></thead><tbody><tr><td>Caption </td><td>String of text that is displayed instead of the level's name. You can use captions to provide a user-friendly label for reports or for localization so that the level's name appears in the local language. </td></tr><tr><td>Description </td><td>Description of the level. </td></tr></tbody></table>

18. Click **Apply**. The dimension is created and added as a new node of the cube in the semantic model.&#x20;

19. (Optional) If you created a new cube, change the name of the cube by clicking the name to make it editable and then enter a new, unique name for the cube.

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Note:</strong> The default name of a cube is “Cube” plus a number that represents the order in which the cube was created (example: Cube 3).  </p></div>

20. Click **Save** to save changes to the model.&#x20;
