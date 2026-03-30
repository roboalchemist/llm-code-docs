# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/pie-donut-and-sunburst-charts.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/pie-donut-and-sunburst-charts.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/pie-donut-and-sunburst-charts.md

# Pie, donut, and sunburst charts

Pie charts are round representations of your data, cut into slices. Each slice represents a piece of data, and the size of the slice is proportionate to the data that it represents. Double-clicking on a slice lets you drill down into your data.

Pie charts are a great way to show numerical or financial data, in other words, what something is worth relative to the whole group.

![Pie chart](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-f4c0e9dd258d4424b2c2e0ed9b3bc56a457fbaaf%2FAnalyzerVisualizationPie.png?alt=media)

Donut charts are a type of pie chart that have a hole in the center, giving it a donut-like appearance. It is used to display data in a circular format, where each segment represents a category. The size of each segment is proportional to the value it represents. Donut charts are useful when you want to show how much each category contributes to the whole, while also showing the relationship between different categories.

You can drill down into your data by double-clicking a data slice. The donut then rearranges itself to show the more detailed information.

![Donut chart](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-21a39a43cb1016a07b07ec1f6757bf5772cb5b3d%2FPAZ%20Donut%20chart.png?alt=media)

Sunburst visualizations organize and display your data in a series of colorful rings. Starting with the center ring, each ring going outward represents more detailed information relating to the inner ring to which it is connected. These outer rings are arranged and colored to indicate their hierarchical relationship with the inner ring. Any fields that contain empty slices can be shown as gaps in the sunburst.

Double-click a data slice to drill down into your data. The sunburst then rearranges itself to show the more detailed information.

Sunburst visualizations are particularly well-suited for numerical analysis of hierarchical data.

![Sunburst chart](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e84de06b1a14f4acf0fe00bcca405b0f86fad340%2FAnalyzerVisualizationSunburst.png?alt=media)

Optional Properties for Pie and Sunburst Charts

| Property                   | Definition                                                                                                                                             | Available In                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| **Data Labels**            | Use this property to label the data features of your report and specify where you want them to appear. You can also choose not to display data labels. | Pie, donut, and sunburst charts |
| **Exploded Slice Radius**  | Use this property to increment the radius of an exploded slice.                                                                                        | Donut charts                    |
| **Slice Inner Radius**     | Use this property to change the inner radius of each slice.                                                                                            | Donut charts                    |
| **Order By**               | Use this property to sort your data on the report.                                                                                                     | Sunburst charts                 |
| **Empty Slices** check box | Select to show Empty Slices as gaps in the report.                                                                                                     | Sunburst charts                 |
