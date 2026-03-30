# Source: https://docs.pentaho.com/pba/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties.md

# Assign time dimension properties

Typically, you might sort your data by year or month. However, by designating a time dimension in the Data Source Model Editor, you can filter on a variety of date ranges and relative date options, such as previous periods, before \[a user-defined period], after \[a user-defined period], current period, or next period.

Analyzer supports many types of relative date filters. To apply them to a level of a time hierarchy, you need to define the time-specific properties for that level. This is because each data warehouse implementation may have a different date format and set of time hierarchy levels.

These steps show you how to assign a time property to a dimension in a multidimensional model.

1. Within the Data Source Model Editor, click the **Analysis** tab.
2. Select the dimension you want to assign as a time dimension.
3. Within the **Properties** pane on the right, click the **Time Dimension** box to assign the dimension as a time dimension.
4. Expand the dimension to display its hierarchy, then expand the hierarchy to display its levels. Choose the level for which you want to assign time dimension properties.

   The properties of the level display in the **Properties** pane.

   The options for **Time Level Type** and **Source Column Format** do not display for a child-level if the time dimension property is not set for its parent-dimension.
5. Set the **Time Level Type** and **Source Column Format** to match the format of your data. The **Time Level Type** and **Source Column Format** must match the format of the data stored in your data source for relative date filtering to work properly in Analyzer. This does not affect how your values display. For more information regarding the time level types and formats, see **Pentaho Schema Workbench** for details.
