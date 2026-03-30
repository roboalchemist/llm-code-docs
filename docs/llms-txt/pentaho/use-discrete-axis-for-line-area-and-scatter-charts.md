# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/customize-pdi-data-explorer/use-discrete-axis-for-line-area-and-scatter-charts.md

# Use discrete axis for line, area, and scatter charts

By default, the PDI Data Explorer provides time and number dimensions in line, area, and scatter [visualizations](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/inspect-your-data/use-visualizations/visualization-types) on a continuous scale axis. The continuous axis is helpful for identifying trends that occur over a period of time, such as financial growth, real estate sales, or test scores.

Prior to Pentaho version 8.1, line and area visualizations used a discrete axis, where the data points display evenly spaced across the axis. Additionally, the scatter visualization only accepted measures in its X-axis and Y-axis zones. However, if you prefer the Time and Number dimensions in Line and Area visualizations on a discrete axis, and to disable the Time and Number dimensions in Scatter visualizations, perform either or both of the following procedures to edit the global mapping configurations:
