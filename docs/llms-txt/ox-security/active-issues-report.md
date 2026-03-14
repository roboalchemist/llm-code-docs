# Source: https://docs.ox.security/generate-reports/built-in-reports/active-issues-report.md

# Active Issues Reports

The Active Issues report provides a real-time view and an overtime view of all unresolved security issues in your organization.\
It helps teams track the volume, severity, and type of active issues, enabling data-driven prioritization and remediation.

You can filter and export the report data.

Use the Active Issues report to:

* Monitor the trend of unresolved security issues over time.
* Identify categories with the highest concentration of open issues.
* Focus on the most critical and high-impact vulnerabilities first.
* Track ownership and accountability for issue resolution.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b8b818d237b87ea7b753a9f90ce2b526535af007%2FActive_Issues_report.png?alt=media" alt=""><figcaption></figcaption></figure>

### Report Sections

| Section                                 | Description                                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Active Issues Over Time**             | Displays a stacked area chart showing how the number of active issues changes over the selected date range.                                       |
| **Current Active Issues by Severity**   | Shows a severity distribution chart for all currently active issues.                                                                              |
| **Active Issues According to Category** | Shows a category-based distribution chart for all currently active issues.                                                                        |
| **Top Issues**                          | Lists the most severe active issues with details such as category, vulnerability description, first seen date, occurrence count, and issue owner. |

### Filters

| Filter            | Description                                                                                                                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Category**      | Displays issues according to security category, such as SBOM, Container Security, and Open Source Security.                                                                                     |
| **Application**   | Select specific applications to include in the report.                                                                                                                                          |
| **Severity**      | Filter active issues by severity level.                                                                                                                                                         |
| **App Tag**       | Filter results using application tags.                                                                                                                                                          |
| **Business Unit** | Narrow the results to specific business units. You can create new [business units in the Executive Reports page](https://docs.ox.security/generate-reports/built-in-reports/executive-reports). |

## Exporting Active Issues report data

The following export options are available in the active issues report:

| Option            | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| **Export as PDF** | Generate a PDF file of the report, including charts and tables.  |
| **Export as CSV** | Generate a CSV file containing issues data for further analysis. |

> **Note:** By default, the exported report includes all columns from the Top Issues table. If you hide any columns in your custom view, the export will reflect those changes.
