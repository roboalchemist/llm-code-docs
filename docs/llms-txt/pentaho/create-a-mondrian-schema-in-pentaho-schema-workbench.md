# Source: https://docs.pentaho.com/pba-schema-workbench/work-with-mondrian-schema/create-a-mondrian-schema-in-pentaho-schema-workbench.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/work-with-mondrian-schema/create-a-mondrian-schema-in-pentaho-schema-workbench.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/work-with-mondrian-schema/create-a-mondrian-schema-in-pentaho-schema-workbench.md

# Create a Mondrian schema

In order to complete this process, you should have already connected to your data source in Schema Workbench.

This section explains the basic procedure for creating a barebones Mondrian schema using Schema Workbench.

1. To create a new Mondrian schema, click the **New** button, or go to the **File** > **New** > **Schema**.

   A new schema sub-window will appear. Resize it to fit your preference.
2. It's easier to visualize your physical data model if you have it in front of you. Turn on the JDBC Explorer from the **New** section of the **File** menu and position it according to your preference. If you have a third-party database visualization tool that you are more familiar with, use that instead.

   The JDBC Explorer is not interactive; it only shows the table structure of your data source so that you can see at a glance what the names of the columns and rows in it.
3. Typically your first action when creating a schema is to add a cube. Right-click the **Schema** icon in the schema window, then select **Add cube** from the context menu. Alternatively you can click the **New Cube** button in the toolbar.

   A new default cube will show up in your schema.
4. Give your cube a name.
5. Add a table by clicking the **New Table** button, or by right-clicking your cube, then selecting **Add Table**. This will be your fact table. Alternatively, you can select **View** or **Inline Table** if these are the data types you need for your fact table.
6. Click the **Table** entry in the **name** field of your new table, and select or type in the name of the table in your physical model that you want to use for this cube's fact table.
7. Add a dimension by right-clicking the cube, then selecting **Add Dimension**, or by clicking the **New Dimension** button.

   When you add a dimension, a new hierarchy is automatically created for it.
8. Type in a friendly name for this dimension in the **name** field.
9. Select a foreign key for this dimension from the **foreignKey** drop-down box, or just type it into the field.
10. To configure the hierarchy, expand the dimension by clicking the lever icon on the left side of the dimension's tree entry, then click on **New Hierarchy 0**. Choose a **primaryKey** or **primaryKey Table**.
11. Add a table to the hierarchy by right-clicking the hierarchy, then selecting **Add Table** from the context menu.
12. Choose a column for the name attribute.
13. Add a level to the hierarchy by right-clicking the hierarchy, then selecting **Add Level** from the context menu.
14. Give the level a name and choose a column for it.
15. Add a member proeperty to the level by right-clicking the level, then selecting **Add Property** from the context menu.
16. Give the property a name and choose a column for it.
17. Add a measure to the cube by right-clicking the cube and selecting **Add Measure** from the context menu.
18. Choose a column that you want to provide values for, then select an aggregator to determine how the values should be calculated.

These instructions have shown you how to use Schema Workbench's interface to add and configure basic Mondrian schema elements.

When your schema is finished, you should test it with a basic MDX query such as:

```
select {[Dim1].[All Dim1s]} on rows, {[Measures].[Meas1]} on columns from [CubeName]
```

In order to use your schema as a data source in any Pentaho Business Analytics client tools, you must publish it to the Pentaho Server. To do this, select **Publish** from the **File** menu, then enter in your Pentaho Server connection information and credentials when requested.
