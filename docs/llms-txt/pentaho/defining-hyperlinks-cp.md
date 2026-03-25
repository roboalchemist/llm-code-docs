# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp.md

# Defining hyperlinks

Manage the amount of information displayed in a report by hyperlinking from one report to other related reports, charts, dashboards, and URLs. For example, you can present basic information in an easy-to-comprehend report with hyperlinks to reports that contain details.

For charts, hyperlinks take precedence over the [drill-down chart](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/set-analyzer-report-options/turn-on-drill-through-links) feature. For example, when readers click a bar in a chart, it displays data related to the hyperlink you define, not the drill-down chart.

For reports, you can define a hyperlink on any row label or column header. When you define a hyperlink, the link is applied to all members within the row or column. In this source report, hyperlinks have been defined for the Positions row level and the Region column level. Notice how each of the row and column members have a blue underlined hyperlink.

![Source report](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e068d95e1ba817734a9a8b78dbed17c26e8fa019%2FssAnalyzerScreenSourceReport.png?alt=media)

When defining hyperlinks to a destination report that has [parameters](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/add-query-parameters-to-analyzer-reports-task-article), you can map the row and column levels in the source report to parameters in the destination report. With this function, you can constrain the hyperlink result to display only data for the mapped parameters. If you do not restrain the results, then no filter applies and all the data appears.

**Note:** If you have renamed a Level in the report, Analyzer continues to display the Level caption or name in the header.

For example, you can create a hyperlink in the source report for all the members in the **Position** row labels, and constrain the displayed data to only that related to each position and its department. To do this, you map the **Department** and **Positions** row levels in the source report to the **Business Unit** and **Job Title** parameters in this destination report.

![Target report](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-eb5977cb862fc20788059cc33d31638f87f69849%2FssAnalyzerScreenTargetReport.png?alt=media)

When the reader clicks on the **Administrative Assistant** position within the **Finance** department in the source report, it looks like the example below:

![Administrative report results](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-b5a99357b46aed7a742481e973c702f7cec307a3%2FssAnalyzerScreenAdminResults.png?alt=media)

Each parameter added to the mapping further constrains the data. You can map any row levels that appear to the left, and column levels that appear above the member data.

**Note:** If you did not constrain the data with parameters, readers would see data for all **Administrative Assistant** positions in all departments.
