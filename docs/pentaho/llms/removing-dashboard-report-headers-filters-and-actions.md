# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/removing-dashboard-report-headers-filters-and-actions.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/removing-dashboard-report-headers-filters-and-actions.md

# Removing headers, filters, and actions for reports in dashboards

You can control the header, filters, and actions available to users viewing an Analyzer report displayed in a dashboard or a standalone report. Independent property settings allow you to disable selected interactive elements of the displayed report, while maintaining the drill-down and keep or exclude capabilities within its charts.

![](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-9254db089dccfe0565fff64a1ef493072fcbaa8f%2FHeader%20options.png?alt=media)

The following table identifies the elements available for controlling viewer access and information in a displayed Analyzer report.

![](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-9254db089dccfe0565fff64a1ef493072fcbaa8f%2FHeader%20options.png?alt=media)

| Item | Name               | Description                                                                                                            |
| ---- | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| 1    | Header bar         | Contains the report title, **Filters** panel and **Actions** menu.                                                     |
| 2    | **Filters** panel  | Displays a filter count and contains a drop-down panel that lists the applied filters.                                 |
| 3    | **Actions** button | Contains a drop-down menu of available user actions, such as exporting the report and changing the visualization type. |
| 4    | Undo/Redo button   | Click to undo or redo a chart drill-down.                                                                              |

You can control Analyzer report elements at the global level using the `analyzer.properties` file, or at the individual dashboard or report level using Javascript APIs or URL parameters.

For global-level control of the header bar, filters, and actions, use the following settings in the `analyzer.properties` file in the `server/pentaho-server/pentaho-solutions/system/analyzer` directory.

| Property                                   | Description                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **report.viewer.edit.disable**             | Disables all filter and field editing operations, such as removing a filter or field. The default value is false.                                                                                                                                                                                                                                        |
| **cv.api.ui.removeHeaderBar.viewer**       | Removes the **header** bar. The refresh indicator continues to appear when the report is refreshed. The default value is false.                                                                                                                                                                                                                          |
| **cv.api.ui.disableFilterPanel.viewer**    | Disables the **Filters** panel. The user will be unable to access the **Filters** drop-down panel and see the applied filters. For example, you may want to disable the **Filters** panel when the dashboard has used prompts to apply filters, so repeating the prompt filters in the **Filters** panel would be redundant. The default value is false. |
| **cv.api.ui.removeReportActions**          | Removes the **Actions** button, and access to the **Actions** menu. The default value is false.                                                                                                                                                                                                                                                          |
| **cv.api.ui.removeUndoButton.viewer=true** | Removes the **Undo** button for the report.                                                                                                                                                                                                                                                                                                              |
| **cv.api.ui.removeRedoButton.viewer=true** | Removes the **Redo** button for the report.                                                                                                                                                                                                                                                                                                              |

**Note:** When you turn off these elements at the global level, setting the URL parameters to `true` does not return them.

For embedded Analyzer, you can remove the header bar, filters, actions, and undo/redo buttons from individual reports using the following Javascript user interface APIs:

* removeHeaderBar(removeFlag)
* removeReportActions(removeFlag)
* disableFilterPanel(removeFlag)
* removeUndoButton(removeFlag)
* removeRedoButton(removeFlag)

**Note:** If you are using 3.0 Viz API, you can remove specific chart types from the **Actions** menu by editing the `pentaho-server/pentaho-solutions/system/karaf/config/web-client/config.js` file. If you are using 2.0 Viz API and earlier, see the article, "How to hide/disable certain chart types in the Analyzer UI" in the [Customer Support](https://support.pentaho.com/hc/en-us/articles/205790979-How-to-hide-disable-certain-chart-types-in-the-Analyzer-UI).

For Analyzer reports produced in a dashboard, you can apply the following URL parameters on the dashboard URL or an individual report URL to control the header bar, filters, and actions.

**Note:** The following URL parameters are only effective when the settings have not been removed or disabled using the `analyzer.properties` file.

* **<http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ASales%20Performance%20(dashboard).xdash/viewer?removeHeaderBar=true>**

  Removes the **header** bar, **Filters** panel, and **Actions** button.
* **<http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ASales%20Performance%20(dashboard).xdash/viewer?removeReportActions=true>**

  Removes the **Actions** button and menu.
* **<http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3ASales%20Performance%20(dashboard).xdash/viewer?disableFilterPanel=true>**

  Disables the **Filters** panel and drop-down.
* **<http://localhost:8080/pentaho/api/repos/%3Apublic%3ASteel%20Wheels%3AWidget%20Library%3AAnalysis%20Views%3AGeomap.xanalyzer/viewer?frameless=true>**

  Removes the report title when the report is opened directly in a browser.

  ![Report title example](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-868cb44dec91b707e1996fcce603172ef1ca87a0%2FPUC_Analyzer_Report_Geomap_Ex_fade.png?alt=media)

  **Note:** When Analyzer reports are used in Pentaho dashboards, the report titles are automatically hidden because Pentaho dashboard content items include their own titles. However, if you use an Analyzer report in your custom dashboard or as a standalone report, then setting this URL parameter may be useful.
