# Source: https://docs.pentaho.com/pba-report-designer/report-designer-and-reporting-engine-issues-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/report-designer-and-reporting-engine-issues-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/report-designer-and-reporting-engine-issues-cp.md

# Report Designer and Reporting engine issues

Follow the suggestions in the following sections to help resolve common issues with Pentaho Report Designer and the Pentaho Reporting engine:

* [Report elements with dynamic heights overlap other elements](#report-elements-with-dynamic-heights-overlap-other-elements)
* [Microsoft Excel report takes a long time to generate](#microsoft-excel-report-takes-a-long-time-to-generate)
* [Columns unexpectedly merge when exporting to Excel](#columns-unexpectedly-merge-when-exporting-to-excel)

## Report elements with dynamic heights overlap other elements

If you have overlapping elements in your report when using the **dynamic-height** style property, use the following directions to create a two-row details band:

1. In the **Structure** pane, select your **Details** band and then go to the **Style** pane and change the value of **layout** to **'block'**.
2. Right-click the **Details** band, then select **band** from the **Add Element** context menu.
3. Move or add the elements for the first row into your created band.
4. Add another band, then move or copy all elements for the second row into the second band.

When your first row elements expand, your second row elements will be pushed down. Repeat this process as necessary for multiple rows.

## Microsoft Excel report takes a long time to generate

If you export content from Report Designer to Microsoft Excel and the report takes a long time to generate or the process runs out of memory, you might be generating a report with more than 60,000 records.

For better performance, if you have a report that generates an Excel worksheet with more than 60,000 records, you must export to the XLSX format instead of the XLS format. Starting with Report Designer v10.2, Microsoft Excel XLSX is the only supported worksheet format.

## Columns unexpectedly merge when exporting to Excel

If you export content from Report Designer to Excel and end up with unexpectedly merged columns in the output, you probably have a horizontal alignment problem with your column header or footer labels. If a label spans two columns, then the Pentaho Reporting engine will force the two columns to merge in the output.

Check your horizontal elements for overlapping column. If you need more information on this topic, refer to the section: [Align elements](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-report-elements-in-report-designer-cp).
