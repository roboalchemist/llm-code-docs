# Source: https://docs.pentaho.com/pba/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties/use-ordinal-columns.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties/use-ordinal-columns.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp/edit-multidimensional-data-source-models/assign-time-dimension-properties/use-ordinal-columns.md

# Use ordinal columns

Ordinal columns are used to alter the natural order of a level when fetching members from a database.

For example, the natural alphabetical order of the level `month_name` begins with April and ends with September, when represented by a text string. Alternatively, setting the dimension `month_name` so it is sorted by an ordinal column, such as `month_id`, enables you to sort the values in the level `month_name` in chronological order.

Perform the following steps to set ordinal columns:

1. Select the appropriate column to use as the ordinal column, then click **OK**.
2. Choose the appropriate level, then click **Edit** in the **Properties** pane under **Ordinal Column**.

   The **Select Ordinal Column** dialog box appears.
