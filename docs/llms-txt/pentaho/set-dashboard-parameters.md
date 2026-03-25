# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/set-dashboard-parameters.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/set-dashboard-parameters.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/set-dashboard-parameters.md

# Set dashboard parameters

If you are placing a file, such as an `.xaction` or `.prpt`, inside a dashboard panel, it is possible that the author of the file defined meaningful parameters for the content. If previously defined, the parameters and their associated default values, appear under **Parameters** in the edit pane of the dashboard.

In the example in this article, when the chart initially rendered, it displayed a parameter called *chart\_type* with a default value called bar. A user can change the value of the parameter to see the content rendered as a pie, line, or area chart.

Parameter names are hard-coded in the file, which means they cannot be changed. Neither can you change the number of parameters associated with a file. When you create a chart using the Chart Designer, embed a URL into a dashboard, or create a data table, you can change both the name and value of a parameter.

**Note:** In Windows, the URL parameters have a maximum limit of 2,048 characters, minus the number of characters in the actual path.
