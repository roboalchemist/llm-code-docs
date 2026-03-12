# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/gauge-chart-analytics-analyzer-visualizations.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/gauge-chart-analytics-analyzer-visualizations.md

# Gauge chart

A gauge chart is a type of chart used to display the progress or status of a specific metric or goal. It typically consists of a circular scale with needles or markers that move to indicate the current value or position. Gauge charts are often used in business and industry to track key performance indicators (KPIs), such as production levels, inventory levels, or customer satisfaction ratings. This chart shows a clear and concise visual representation of progress for quickly identifying trends and making data-driven decisions. You can drill down into the data by double-clicking on any dial in the chart. Gauge charts are implemented using Apache Echarts and do not support exporting to PDF.

![Gauge Chart](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-71e9467619497a1d0107a758f995bef75a7d5af1%2FPAZ%20Gauge%20chart.png?alt=media)

Optional Properties for Gauge Charts

| Property                     | Definition                                                                                                                                  | Available In |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Show Measure Color Bands** | Use this property to divide the circular scale into discrete colored partitions.                                                            | Gauge charts |
| **Pattern**                  | If the **Show Measure Color Bands** property is selected, use this property to choose from **Gradient**, **3 Step**, or 5**Step** patterns. | Gauge charts |
| **Color**                    | If the **Show Measure Color Bands** property is selected, use this property to choose from different mixes of colors for your report.       | Gauge charts |
| **Reverse Colors**           | If the **Show Measure Color Bands** property is selected, use this property to reverse the order of colors in the report.                   | Gauge charts |
