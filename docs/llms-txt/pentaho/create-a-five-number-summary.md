# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/boxplot-chart/create-a-five-number-summary.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/boxplot-chart/create-a-five-number-summary.md

# Create a five-number summary

Perform the following steps to create a five-number summary of data points for a Boxplot chart:

1. Create a new or open an existing Analyzer report and select **Boxplot** from the chart dropdown.
2. Right-click any **Measures** field and choose **User Defined Measure**> **Create Calculated Measure**.

   The **Calculated Measure** dialog box displays. See [Creating a calculated measure in a report](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/creating-a-calculated-measure-in-a-report).
3. Create a calculated measure that returns the median value.

   1. Enter the following MDX query In the **Create Calculated Measure** formula panel: `Median(<Set>, <Numeric Expression>)`
   2. Enter an appropriate name and click **OK** to create the median calculated measure.

   You can return a set of descendants of a set member at a specified level, optionally including or excluding descendants in other levels with the following code: `Descendants(<Member>, <Level>)`

   See [Mondrian documentation](https://mondrian.pentaho.com/documentation/mdx.php).
4. Create a calculated measure that returns the lower quartile value.
   1. Enter the following MDX query In the **Create Calculated Measure** formula panel: `FirstQ(<Set>, <Numeric Expression>)`.
   2. Enter an appropriate name and click **OK** to create the lower calculated measure.
5. Create a calculated measure that returns the upper quartile value.
   1. Enter the following MDX query In the **Create Calculated Measure** formula panel: `ThirdQ(<Set>, <Numeric Expression>)`.
   2. Enter an appropriate name and click **OK** to create the upper quartile calculated measure.
6. Create a calculated measure that returns the minimum value.
   1. Enter the following MDX query In the **Create Calculated Measure** formula panel: `Min(<Set>, <Numeric Expression>)`.
   2. Enter an appropriate name and click **OK** to create the minimum calculated measure.
7. Create a calculated measure that returns the maximum value.
   1. Enter the following MDX query In the **Create Calculated Measure** formula panel: `Max(<Set>, <Numeric Expression>)`.
   2. Enter an appropriate name and click **OK** to create the maximum calculated measure.
