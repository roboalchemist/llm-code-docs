# Source: https://docs.axonius.com/docs/report-content.md

# Report Content

Axonius Reports generates a pre-defined executive report, in a PDF format, which includes all Axonius Dashboard charts, a selected list of saved queries for devices or users, or combination of both, as well as [Data Analytics Reports](/docs/analyzing-query-data) reports. The report also includes links to the relevant Axonius page to see additional details. If you have set email configuration, the report is sent by email when it is generated.

You can download the last generated report.

<Callout icon="📘" theme="info">
  Note

  The sections included in the report depend on the report configuration. See [Configuring Reports](/docs/report-configuration-screen).
</Callout>

The Report PDF file can include some or all of the following sections:

1. [Cover page](#cover-page)
2. [Table of Contents](#contents)
3. [Axonius Dashboard](#axonius-dashboard)
4. [Dashboard Charts](#dashboard-charts)
5. [Devices - Saved Queries](#devices--saved-queries)
6. [User - Saved Queries](#users--saved-queries)
7. [Data Analytic Reports](#data-analytic-reports)

## Cover Page

Includes the report name and the time and date the report was generated.

<Image align="center" alt="ReportsCoverPAget.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ReportsCoverPAget.png" />

## Table of Contents

A list of the report sections, according to the report configuration. Each section starts on a new page.

## Axonius Dashboard

Includes all Axonius [Default Charts](/docs/default-panels).

The report structure is 4 columns and two rows on each page, i.e. when a chart is one column  4 charts will be displayed per page. The pie charts and the Matrix table  are always 2 columns.

To open the Axonius dashboard charts in Axonius, click **View in Axonius** next to the title.

<Image align="center" alt="ReportChart1.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ReportChart1.png" />

## Dashboard Charts

Includes all custom charts and the following Axonius dashboard default charts:

* Device Discovery
* Adapter Connections Status

Those default charts and any other custom pie charts include a legend that describes what data each of the chart slices represents.

For details about the different charts, see [Default Charts](/docs/default-panels) and [Custom Charts](/docs/working-with-custom-panels).

To view the full charts, click the 'View in Axonius' link next to the title.

<Image alt="TestREport2.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TestREport2.png" />

## Assets - Saved Queries

Includes the Devices/Users/Security Findings/Software saved queries listed in the report configuration, ordered according to the saved query name sorted alphabetically.
Each saved query consists of the following information:

* **Query Name** - The name of the query
* **Description** - The description of the query that the user entered when they created the report.
* **Asset Count** – the number of assets discovered in that query
* **View all results** - Link to the full query results on the Devices page.

If no results are found for a specific query, the asset number is shown as 0.

For details, see [Saved Queries](/docs/saved-queries-devices).

<Image alt="Devices_savedQueries.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Devices_savedQueries.png" />

## Data Analytic Reports

Includes the selected data analytic reports created using the [Data Analytics](/docs/analyzing-query-data) page.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataAnalytics-Reports.png)