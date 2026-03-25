# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/inspect-your-data/use-visualizations.md

# Use visualizations

Data visualizations have two modes: **Stream View** and **Model View**. You can switch between these modes to inspect data and shape visualizations based on the sampled set. **Stream View** generates SQL queries used in entity-relational modeling and executed in a relational database. **Model View** builds upon the same tables as **Stream View**, laying a dimensional model on top of them, and allowing for multidimensional queries, supported in the background by MDX queries to a Mondrian engine.

The first view provided during data inspection is a **Stream View** of your step data in a flat table on the canvas. To reduce the number of data fields selected, click anywhere on the field name in the available fields panel. The blue disc icon to the left of the name disappears, indicating that the field is no longer selected. To change the visualization type, use the **visualization selector**. If you select a visualization that requires a model, the mode will automatically switch to **Model View**. Otherwise, it remains in **Stream View**, and if available **Model View** can be manually selected.

Drag the fields you want to visualize from the available fields panel and drop them into the drop zones of the **Layout** panel. The drop zones and the data they accept are determined by the **visualization type**. To explore your data with additional visualization types, **create additional tabs**.

You can further customize your visualization by keeping or excluding fields, by drilling down into data points in the visualization including the legend or axis labels of a chart, and by other filtering options. When you filter, the filtering action is applied to the data and the **Filters** panel and visualization automatically updates, based on the selected filter. For more information, see the **Filters** article.

Once you are satisfied with your step data and model, you can make the content available for collaboration by **publishing a data source**.
