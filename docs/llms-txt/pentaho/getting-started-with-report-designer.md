# Source: https://docs.pentaho.com/pdia-try-pdia/getting-started-with-report-designer.md

# Getting started with Report Designer

Use this topic to create and refine a sample report in Report Designer.

You use Pentaho’s sample database in these steps. Sample data is installed by default with Report Designer.

### In this topic

* [About Pentaho Report Designer](#about-pentaho-report-designer)
* [Create a report with Report Designer](#create-a-report-with-report-designer)
* [Design your report](#design-your-report)
* [Refine your report](#refine-your-report)
* [Row banding, data formatting, and alignment](#row-banding-data-formatting-and-alignment)
* [Add a chart to your report](#add-a-chart-to-your-report)
* [Add parameters to your report](#add-parameters-to-your-report)
* [Publish your report](#publish-your-report)

### About Pentaho Report Designer

Pentaho Report Designer is a report creation tool. You can use it standalone or as part of the Pentaho Business Analytics suite.

It helps you build detailed reports from prepared data. You can connect to most data sources.

### Create a report with Report Designer

Perform the steps below to create a report using Report Designer.

1. Start Report Designer. Go to **Start** > **Programs** > **Pentaho Enterprise Edition** > **Design Tools** > **Report Designer**.

   The Report Designer home page appears.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>To change the zoom level, drag the percentage in the upper-left corner. Double-click it to reset to 100%.</p></div>
2. Click **New Report** in the Welcome dialog box.

   The design workspace appears.
3. In the right pane, click the **Data** tab.
4. Right-click **Data Sets** and select **JDBC**.

   You can also click the yellow database icon.
5. Under **Connections**, select **SampleData (Hypersonic)**.
6. Next to **Available Queries**, click the plus sign to add queries.

   ![JDBC Data Source dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d1b71a60a45872623318eae4c21443ed12525d93%2FssPRDJDBCDataSource.png?alt=media)

   Query 1 appears under **Available Queries**.
7. Click the edit icon (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)).

   The SQL Query Designer window opens.
8. Select **PUBLIC** in the **schema filter** menu. Double-click **ORDERFACT** so the table appears in the workspace.

   ![SQL Query Designer](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-9af15ced36e9b4649dee2049f32cb76e14071cd3%2FssPRDSQLQueryDesigner%20-%20SchemaFilter.png?alt=media)
9. In the SQL Query Designer workspace, right-click **ORDERFACT** and select **deselect all**.

   ![Clear all, SQL Query Designer](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d6c90f5ce3d3daf14f1245dffecec90b249b5d09%2FssPRDSQLQueryDesigner%20-%20DeselectAll.png?alt=media)
10. Select the **ORDERNUMBER**, **QUANTITYORDERED**, **PRICEEACH**, and **ORDERDATE** fields.

    ![Orderfact fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1a3668091f81d8b4993261a5f04d8b49a4e6fe83%2FssPRDSQLQueryDesigner%20-%20ORDERFACTFields.png?alt=media)
11. Double-click **PRODUCTS** so the table also appears in the workspace.

    Notice the line joining the **ORDERFACT** and **PRODUCTS** tables.
12. Clear all **PRODUCTS** fields. Then select **PRODUCTNAME** and **PRODUCTLINE**.

    ![Products table](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-dfdfc6cbdcc770069b9a78245a0f4dc0c0f8e19d%2FssPRDSQLQueryDesigner%20-%20PRODUCTSTable.png?alt=media)
13. Click the **Syntax** tab to view the SQL statement.

    Notice that **PRODUCTCODE** joins the tables.

    ![Syntax tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-b0407375a7ef9d0ee3c8d72ee5adab1f2d89b389%2FssPRDSQLQueryDesigner_-_SyntaxTab.png?alt=media)
14. Click **OK** to return to the JDBC Data Source dialog box.

    The SQL statement appears under **Query**.
15. Click **OK** in the JDBC Data Source dialog box.

    ![Query 1 fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-18a9f13c177be7630d806abd6826de28f394a737%2FssPRDDataTabShowingQuery1.png?alt=media)

    The fields now appear under **Query 1**.

Next: [Design your report](#design-your-report).

### Design your report

This exercise walks you through designing your report layout.

1. Under **View**, select **Element Alignment Hints** and **Snap to Elements**.

   These options help align elements.
2. Under **Query 1**, drag **ORDERNUMBER** into the **Details** band.
3. Add **ORDERDATE**, **PRODUCTNAME**, **QUANTITYORDERED**, and **PRICEEACH** to the **Details** band.

   Do not overlap fields.
4. Resize **PRODUCTNAME** larger. Resize **QUANTITYORDERED** smaller.

   ![Resizing](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ef7dbe13d8c74d2d78eaa1723da9e37d871050ab%2Frd_13.png?alt=media)
5. Click **Preview** (![Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-501ad0aec8b3fa954777888b04e2d17b735c10ce%2Fpreview_eye.png?alt=media)).

   ![Report preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2a431a25ca123bb2f7ec505355acab4e5189550a%2FssPRDInitialReportDesign.png?alt=media)
6. Click **Edit** (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)) to return to the workspace.

Next: [Refine your report](#refine-your-report).

### Refine your report

You created a report in the previous exercise. Now add labels, headers, and row banding.

1. Drag a label (![Label](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-f952ae1a87a67130c08d8d6e5df5c2a409833d04%2Frd_35.png?alt=media)) to the **Page Header** band.

   The **Structure** tab updates.

   ![Structure tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-03721f7235725c36663164292add6ca4e6ad0eeb%2Frd_15.png?alt=media)
2. Click inside the label and type `Order Report`.
3. Select the label text. Set the font size to 18. Apply bold.

   ![Font resizing](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5165a7f7928326eca83f5f7bee7843205045fe06%2Frd_16.png?alt=media)
4. With the label selected, set a font color.

   The page header appears on every page.
5. Create column headers. Click **Details Header** under the **Structure** tab.

   The **Style** and **Attributes** tabs appear.
6. Under **common** in **Attributes**, set **hide-on-canvas** to **False**.

   The **Details Header** band appears.
7. Click the **Select Objects** icon (![Select objects](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-75d16c81c01f61ce83aebfef6cf3d9ea0578702a%2Fselect_objects_icon.png?alt=media)).
8. Select all column objects in the **Details** pane.

   ![Selected objects](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-003a0d129a45ba7019aa51b6b43795badd424b69%2Fselect_objects.png?alt=media)
9. Press Ctrl+C to copy. Press Ctrl+V to paste into the **Details Header** pane.
10. Select **Format** > **Morph** > **label**.

    The objects change to labels.
11. Type the header labels: `Order No.`, `Order Date`, `Product Name`, `Quan.`, and `Price Each`.
12. Click **Preview** (![Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-501ad0aec8b3fa954777888b04e2d17b735c10ce%2Fpreview_eye.png?alt=media)).

    ![Report example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-688d663e1122f8b16d656853748ff3d7b4c2d197%2FssPRDReportWithHeadingLabels.png?alt=media)
13. Select **Format** > **Row Banding**.
14. In the Row Banding dialog box, select **Yellow** for **Visible Color**. Click **OK**.
15. Click **Preview**.

    ![Report with row banding](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-4201c67cb9c92ebe1721386fe571bc6fd13523ac%2FssPRDReportWithRowBanding.png?alt=media)
16. Select **File** > **Save**. Save to `.../report-designer/samples`. Use `Orders` as the file name.

Next: [Row banding, data formatting, and alignment](#row-banding-data-formatting-and-alignment).

### Row banding, data formatting, and alignment

#### Row banding

Create a row band element to control which fields show banding. You can name the row band element anything.

In this example, the row band element is named **row-band-element**.

![Row Banding dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-aa798a428b075c114bfb6e372b783e9fa4ebc66f%2FssPrdRowBand.png?alt=media)

After you create the element, select the fields to band. In **Attributes**, type `row-band-element` in the **name** field.

![Name field, Attributes](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0afa73f11ea2a7dde92d3d4ce84cde0105c4e40b%2FssPrdAllColumnsSelected.png?alt=media)

#### Data formatting

Report Designer uses default formats for dates and numbers. You can change formats under **Attributes**.

Select a field. Then select a value for **format**.

In this example, **Order Date** uses `MM-dd-yy`.

![Format field, Attributes](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-6e8c48dcfb730211d7738bb2bc6cf66b9484efcb%2FssPrdDataFormat.png?alt=media)

Preview the report to confirm the results.

![Order Date formatting applied](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-11377ab81449d287a4a5689807471bf06360f431%2FssPrdOrderDateClean.png?alt=media)

{% hint style="info" %}
You can also type a custom format string. Use the JavaScript date and number format syntax.
{% endhint %}

#### Alignment

To align multiple objects, select them first. Then choose an alignment option under **Format**.

To multi-select, press Shift and click each object. You can also use **Select Objects** (![Select Objects](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-75d16c81c01f61ce83aebfef6cf3d9ea0578702a%2Fselect_objects_icon.png?alt=media)) and drag to select.

![Alignment selection, Format menu](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c48a77edb7a039f2077e95f2d4be57479d171f07%2FssPrdAlignHeaders.png?alt=media)

Next: [Add a chart to your report](#add-a-chart-to-your-report).

### Add a chart to your report

In this exercise, you add a chart to your report.

1. Select **File** > **Open**. Open the report you saved earlier.
2. In the **Palette**, drag a Chart icon (![Chart](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-38ee5d74b5834c1c460abd2aed454513dc9fac8c%2Frd_chart.png?alt=media)) into the **Report Footer** band.
3. Resize and center the chart.

   ![Chart resizing handles](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5152344111a904ce3c66e136031d958befbb9146%2Frd_24.png?alt=media)
4. Double-click the sample chart.
5. Select the **pie chart** icon.

   Chart properties are listed on the left. Data properties are listed on the right.
6. Under **Title**, set **chart-title** to `Product Pie Chart`.
7. Under **Common** in **Primary DataSource**, set **value-column**. Click the ellipsis to open the Select Field dialog box.
8. Select **QUANTITYORDERED** and click **OK**.
9. Under **Series**, click the ellipsis next to **series-by-field**.

   The Edit Array dialog box opens.
10. Click the **Add** icon (![Add](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5fda46e3255983f47487ad27f06e7f8a20ee00ad%2Fadd.png?alt=media)).
11. Select **PRODUCTLINE** and click **OK**.
12. Click **OK** to close the Edit Chart dialog box.
13. Click **Preview** (![Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-501ad0aec8b3fa954777888b04e2d17b735c10ce%2Fpreview_eye.png?alt=media)).
14. Scroll to the last page.

    ![Displayed report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0abdff8b62ff222c4923cb44cabc9ab80c9999c1%2Frd_27.png?alt=media)
15. Save your report.

{% hint style="info" %}
To use a bar or line chart, change the chart type. Add **series-by-value** entries for `SALES` and `COST`.
{% endhint %}

Next: [Add parameters to your report](#add-parameters-to-your-report).

### Add parameters to your report

Now make your report interactive by setting parameters. Users get prompted for values when they run the report.

1. In Report Designer, open your Orders report.
2. Select **Data** > **Add Parameter**.

   You can also select **Master Report Parameter** (![Master report parameter](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-cc7624a3679de5abfb1daa93eed0f47f90e041eb%2Frd_add_parameter.png?alt=media)) under the **Data** tab.

   The Add Parameter dialog box appears.
3. In **Name**, enter `enter_prodline`.
4. In **Label**, enter `Select Line`.
5. For **Display Type**, select **Drop Down**.
6. Under **DataSources**, select **JDBC (SampleData (Hypersonic)**. Click the **Edit** icon (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)).

   The JDBC Data Source dialog box appears.
7. Under **Connections**, select **SampleData (Memory)**.
8. Next to **Available Queries**, click **Add** (![Add](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5fda46e3255983f47487ad27f06e7f8a20ee00ad%2Fadd.png?alt=media)).

   Query 2 is added.
9. In **Query Name**, enter `prodlineList`.
10. In **Query**, enter the following SQL:

    ```sql
    SELECT DISTINCT
         "PRODUCTS"."PRODUCTLINE"
    FROM
         "PRODUCTS"
    ```

    You can also build the query in SQL Query Designer.
11. Click **OK** to close the Data Source dialog box.
12. In the Add Parameter dialog box, under **DataSources**, select **prodlineList**.
13. For **Value Type**, select **String**.
14. Optional: Set a default value, such as `Motorcycles`.

    ![Add Parameter dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d8b51d365198804d3db91167781b4243703f8294%2FssPRDAddParameter.png?alt=media)
15. Click **OK** to close the Add Parameter dialog box.
16. Map the parameter back to Query 1. Under **Data**, double-click **Query 1**.
17. Click the **Edit** icon (![Edit](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-155f015433752130f7340b11ca96303843194c36%2Fedit.png?alt=media)) to open SQL Query Designer. Right-click **PRODUCTLINE** and select **add where condition**.
18. In the condition editor, enter `${enter_prodline}`. Click **OK**.

    ![Condition.edit dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-95cd10972f49d0c02ebf3211a7f9601ca6e840b4%2Frd_condition_edit.png?alt=media)
19. Click **OK** to close SQL Query Designer.
20. Click **OK** to close the Data Source dialog box.
21. Click **Preview**.

    ![Product line menu](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-07962c842428094e839a87810bf5d8005ff2b1b2%2FssPRDProductLineParameterInReport.png?alt=media)
22. Save and close the report.

Next: [Publish your report](#publish-your-report).

### Publish your report

Now publish the report to a Pentaho server.

1. In Report Designer, open the report you created.
2. Select **File** > **Publish**.

   You can also select **Publishes the report on a Pentaho server** (![Publish](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-39fd703669f0982b5f50c4b42c17c35e20f5d300%2Frd_publish.png?alt=media)).
3. In the Login dialog box, confirm the server URL is `http://localhost:8080/pentaho/`.

   ![Login dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1b90efe4ae3bad75b38eb8ff08bc12e26e29de8b%2FssPRDServerLogin.png?alt=media)
4. Click **OK**.

   The Publish to Server dialog box appears.
5. Enter a report title and description.
6. Under **Location**, save to `...public/Steel Wheels`.
7. Set **Output Type** to **html** and click **OK**.

   A success message appears.
8. Click **Yes** to open the User Console and view the report.

   To view it later, go to `http://localhost:8080/pentaho/`. Then browse to the `Reporting Examples` directory.
9. Log in as `Admin`.

   The default password is `password`.
10. Select a product line parameter value. Keep the default **Output Type**.

Your report is now available to users.
