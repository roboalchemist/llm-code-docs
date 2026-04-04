# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/boxplot-chart/boxplot-chart-example.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/boxplot-chart/boxplot-chart-example.md

# Boxplot chart example

The Boxplot chart example shown in this article was created using the following steps:

1. Choose **File** > **New** > **Analysis Report**.

   The **Select Data Source** dialog box opens.
2. Select **SteelWheelsSales** and click **OK**.

   The new report displays.
3. Select **Boxplot** in the chart list.
4. Add the **Territory** market to the **Category** layout and add the **Years** time to the **Series** layout.
5. In the **Available fields** list, right-click any field in **Measures** and choose **Create Calculated Measure**.
6. Enter **Median** as the **Display Name** and calculate the median of the set by entering the following MDX query in the **Create Calculated Measure**formula panel and clicking **OK**: `Median(Descendants([Product].CurrentMember,[Product].[Line]), [Measures].[Quantity])`

   ![Create Calculated Measure dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-2347a651057ef3437a98b428bd107ca02d28a1f9%2FPAZ%20Create%20Calculated%20Measure%20dialog%20box.png?alt=media)
7. Create a **Lower Quartile** calculated measure set by entering the following MDX query in the **Create Calculated Measure** formula panel and clicking **OK**: `FirstQ(Descendants([Product].CurrentMember,[Product].[Line]), [Measures].[Quantity])`
8. Create an **Upper Quartile** calculated measure set by entering the following MDX query in the **Create Calculated Measure** formula panel and clicking OK: `ThirdQ(Descendants([Product].CurrentMember,[Product].[Line]), [Measures].[Quantity])`
9. Create a **Minimum** calculated measure set by entering the following MDX query in the **Create Calculated Measure** formula panel and clicking OK: `Min(Descendants([Product].CurrentMember,[Product].[Line]), [Measures].[Quantity])`
10. Create a **Maximum** calculated measure set by entering the following MDX query in the **Create Calculated Measure** formula panel and clicking OK: `Max(Descendants([Product].CurrentMember,[Product].[Line]), [Measures].[Quantity])`
11. Right-click each of the five measures you have created and choose **Add to Report**.

Your Boxplot chart will display as shown in this article.
