# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/geo-map-visualization.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/geo-map-visualization.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/geo-map-visualization.md

# Geo map visualization

Geo maps show a geographic summary of your data using size and color. This visualization type plots a pin on a map, based on the location attribute you used. You can add a measure to specify the size of the pinpoints, then use the properties panel to change the color of the pinpoints. Double-clicking on a pinpoint drills-down into your data. If your data model has geographic annotations, then the location information will be retrieved by the geoservice automatically. Geo maps are especially useful for retail or sales data.

You must have a [license](https://developers.google.com/maps/terms?hl=en) from Google if you choose to use Google Maps with any Pentaho software.

![Geo map](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-66350cfc4c810879d2605ddf02cb71b8de6eab82%2FAnalyzerVisualizationGeoMap.png?alt=media)

| Property                     | Definition                                                             | Available In          |
| ---------------------------- | ---------------------------------------------------------------------- | --------------------- |
| **Pattern**                  | Lets you choose from **Gradient**, **3 Step**, or **5 Step** patterns. | Geo map visualization |
| **Color**                    | Choose from different mixes of colors for your report.                 | Geo map visualization |
| **Reverse Colors** check box | Reverses the order of colors in the report.                            | Geo map visualization |
