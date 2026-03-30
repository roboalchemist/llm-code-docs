# Source: https://docs.pentaho.com/pba-aggregation-designer/work-with-aggregate-tables.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/9.3-aggregation-designer/work-with-aggregate-tables.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/work-with-aggregate-tables.md

# Work with aggregate tables

To work with aggregate tables, following instructions in the following sections:&#x20;

* [Select a model](#select-a-model)
* [Use Aggregate Advisor](#use-aggregate-advisor)
* [Add aggregates](#add-aggregates)
* [Customize aggregates](#customize-aggregates)
* [Delete aggregates](#delete-aggregates)
* [Export aggregates](#export-aggregates)

## Select a model

After defining your data source, you must select the cube you want to use for defining and building aggregate tables.

To select a model:

1. In the Connect to Data Source dialog box, under **OLAP Model**, select **Mondrian Schema File**.
2. Click the Ellipsis (...) to display a file dialog box.
3. Browse to locate and select your Mondrian schema file, which would be `SteelWheels.mondrian.xml` if using sample data, then click **OK**.
4. Click **Apply**.

   The Cube list is populated with a list of cubes defined in your schema.
5. Select the Mondrian cube you want to optimize, then click **Connect**.

When the Pentaho Aggregation Designer establishes a connection, it runs several validation tests to ensure that your database structure is ready to support aggregate tables. A validation summary dialog box appears with a list of test results. If you see an error message, contact your database administrator.

## Use Aggregate Advisor

If you are unfamiliar with aggregate table design and need help creating aggregates to optimize a cube, you can rely on the Aggregate Advisor to provide you with a list of recommendations. The Pentaho Aggregation Designer uses your schema file and the data in your database to create aggregate definitions.

![](https://2790200156-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMLn7wj5kT2VbUHEUieXY%2Fuploads%2Fgit-blob-2da136566df32213f550c627116f5320d927e91f%2FPAD_advisor_1.png?alt=media)

To display recommended aggregates, perform the following steps.

1. In the Pentaho Aggregation Designer toolbar, click **Advisor**.
2. Specify your **Advisor Input Parameters**.
   * **Max Aggregates**

     Allows you to specify the maximum number of aggregates you want the Advisor to recommend.
   * **Max Time to Run**

     Allows you to specify the maximum amount of time (in seconds) you want the Advisor to run before making recommendations.

     **Note:** Allowing the Advisor to run for longer periods of time allows for more potential recommendations to be evaluated and results in more accurate recommendations.
3. Click **Recommend**.

   The Advisor runs for a few seconds before it displays an initial list of recommended aggregates. The Advisor is designed to keep running until it finds an optimal solution. If you stop the Advisor prematurely, the Advisor returns the best set of recommendations it has found up to the point when it was stopped.

## Add aggregates

To add an aggregate, perform the following steps:

1. In the right pane of the Pentaho Aggregation Designer, click **Add**.
2. In the left pane, enter a **Name** and **Description** for your new aggregate.
3. Under **Level**, click the down arrows to define the hierarchy and levels associated with the aggregate you are creating.
4. Click **Apply**. Your aggregate is added to the aggregate list.

## Customize aggregates

To customize an aggregate, perform the following steps:

1. In the Pentaho Aggregation Designer, click on an aggregate in the proposed aggregate list to select it.

   **Note:** When you modify an aggregate created using the Advisor, the aggregate becomes a **Custom** aggregate as indicated by the **Type** column in the proposed aggregate list.
2. (Optional) In the left pane, you can modify the **Name** and **Description** for your custom aggregate.
3. In the **Aggregation Levels** tab, click the down arrows to make changes to the hierarchy and levels associated with the aggregate definition you are customizing.
4. Click **Apply**.

   The Pentaho Aggregation Designer updates the proposed aggregate list, cost/benefit chart, and impact summary.

## Delete aggregates

To delete an aggregate, perform the following steps:

1. Select the aggregate you want to delete from the proposed aggregate list.
2. Click **Remove**.

## Export aggregates

The Pentaho Aggregation Designer allows you to preview the DDL, DML, and schema (for relational databases) outputs before you build aggregate tables. You can also save the outputs and edit them later. If you are using OLAP, DML is the only available output.

To preview the DDL and DML outputs, perform the following steps:

1. Select the aggregates that have DML/DDL output you want to preview.
2. In the Pentaho Aggregation Designer toolbar, click **Export**.
3. In the Execute and Publish dialog box, click **Preview**.

   ![Preview](https://2790200156-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMLn7wj5kT2VbUHEUieXY%2Fuploads%2Fgit-blob-266a9b4636a38b34548b2e19b1c99b37be048eea%2FPAD_preview.png?alt=media)
4. Click **Copy to Clipboard** or **Save** to retain the output.
5. If you examine the DDL/DML outputs and are satisfied with the results, you can allow the Pentaho Aggregation Designer to build (Execute/Publish) the aggregate tables. Follow the instructions for publishing and exporting included in the Execute and Publish dialog box.

   ![Execute and Publish](https://2790200156-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMLn7wj5kT2VbUHEUieXY%2Fuploads%2Fgit-blob-bfa868860f31305dc307b1b831ddaf0bdfce83a7%2FPAD_execute_and_publish.png?alt=media)
