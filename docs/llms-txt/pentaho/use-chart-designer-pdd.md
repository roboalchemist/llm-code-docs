# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/create-a-chart/use-chart-designer-pdd.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/create-a-chart/use-chart-designer-pdd.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/create-a-chart/use-chart-designer-pdd.md

# Use Chart Designer

After defining the data for the new chart with the Query Editor, you are ready to create the visual layout for the chart using the Chart Designer.

This part of the tutorial assumes you have followed the steps in [Use Query Editor](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/create-a-chart/use-query-editor-pdd) to define the data for the examples shown in the following steps

1. In Chart Designer, under **Data**, click the drop-down arrow to display the data selection menu:

   ![Data panel](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-b9146aac6d88f0cd96c74d4f5ba31d6a5ceae1ea%2FPUC_chart_designer_select_data_for_display.png?alt=media)

   | Data Field          | Description                                                                                                                                                                                                                                                            |
   | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Series Column**   | Series display as the individual columns on a bar chart and as individual lines in a line chart. Area charts display each series as a point.                                                                                                                           |
   | **Category Column** | Categories display as bars or groups of bars on the x-axis (horizontal axis). In line charts, categories are usually associated with time periods. In area charts, the x-axis displays the category labels. If you do not want to display categories, choose **None**. |
   | **Values Column**   | The value determines the height of columns in a bar chart and the height of lines in a line chart. In area charts, the y-axis values determine the heights of the points. The value is always numeric.                                                                 |

   A preview of the chart appears in a box in the upper-right corner of the Chart Designer as you select your options.

   ![Chart designer preview](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-851215f05902f1498ad29e58ce514506f3700fc7%2FPUC_chart_designer_preview.png?alt=media)
2. Under **Chart Type**, click the type of chart applicable for your data. If you are unsure which chart type is best for displaying your data, see [Chart types](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/create-a-chart/chart-types) for more information. In this tutorial, **Bar Chart** is selected.

   By default, pie and dial charts display in animated Flash mode. You can turn animation off by disabling the **Animated** check box in the Chart Designer. Animated charts can highlight key data points. For example, you may want to apply animation if a data point reaches a critical value, such as high or low sales numbers. If you selected a pie or dial chart, see [Pie charts](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Analytics/Pentaho%20Dashboard%20Designer/Pentaho%20Dashboard%20Designer%20cp/Create%20a%20chart/Chart%20types/Pie%20charts=GUID-8BA655E8-2A5E-4725-8E46-C7A91543F666=1=en=.md) or [Dial charts](https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/create-a-chart/chart-types/dial-charts).
3. Under **Theme**, select a theme from the list. In this tutorial, the **Default** theme is selected.

   The theme is applied to your chart.
4. Enter the labels for the **Chart Title**, **X Axis Title** (horizontal axis), and **Y Axis Title** (vertical axis).

   Entries appear in the chart preview.

   ![Chart preview x and y axis](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e2cf32ad94ba7fe347b61568bd671add8094ab7c%2FPUC_chart_designer_preview_axis.png?alt=media)
5. Click **Apply** to see the chart preview.
6. Click **OK** to display your chart in the dashboard panel.

The revised chart now appears in the dashboard.
