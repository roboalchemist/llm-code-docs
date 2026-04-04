# Source: https://docs.ox.security/generate-reports/built-in-reports/executive-reports.md

# Executive Reports

The Executive Report provides a high-level summary of your organization’s security posture over a selected time period. It highlights key trends, risk areas, and performance indicators across business units and their associated applications.

You can export the report as a PDF as follows:

* **Summary version:** Includes only the high-level information shown in the left section of the Executive Reports page.
* **Full version:** Includes the detailed data from the right section, based on the selected item on the left.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fe10c4e7c12db030e48ac6b4c3b0ab1ee9975319%2FExecutive_report.png?alt=media" alt=""><figcaption></figcaption></figure>

The report provides the following information:

* Organizational-wide metrics on active issues and SLA performance
* Severity breakdowns and trend indicators
* Grouped summaries by business units
* Optional filtering by severity, category, and scan type

## Before you begin

Before filtering data or generating a report, decide what information you want the report to include:

* [How to group your organization into business units to focus on specific security areas](#creating-business-units)
* [Whether to include SLA data in the report](#enabling-sla-data-in-executive-reports)
* [Which applications to exclude for a faster and more targeted report generation](#excluding-applications-from-the-report)

### Creating business units

A business unit in the OX platform is a way to group applications based on your organizational structure by team, department, product area, or similar criteria.

Creating business units and sub-units helps you focus on specific parts of the organization and understand how each group is performing. Each unit in the report shows how well that group is handling security issues and meeting SLA targets.

The grouping is based on application tags assigned to OX applications. You can define units and sub-units to achieve the level of detail that fits your needs.

**To create a new business unit:**

1. In the **Executive Report** page, select **Executive report settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b4c36d540e6b596fc3de4cb66b4e85aaa86c7f78%2Fbusiness%20units.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In the **Executive Reports Settings** dialog, select **+ New business unit** and define the following:
   1. **Business unit name:** Add a clear and meaningful name.
   2. **Tags:** To determine which data appears in the report and help generate more focused security insights, select tags that help to characterize the best the type of information you are willing to display in the report.
2. To add a sub-unit, select **+ Add Sub-unit**, add the name and the tags.
3. Select **SAVE**. The new business units appear in the **Executive Reports** page, and the number of sub-units nested under the business unit appears in the upper right corner of the unit.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5b9fdf604cf2c4515d382642e1920c79a0072dd3%2Fbusiness%20units%20section.png?alt=media" alt=""><figcaption></figcaption></figure>

1. To display a specific unit with nested sub-units, select the nested units number. The selected business unit and all its nested levels appear.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e8af0ac0b53f340260ccba6b23297698ed786025%2Fsub-units.png?alt=media" alt=""><figcaption></figcaption></figure>

### Enabling SLA data in Executive Reports

You can decide whether you want to display SLA trends and data in the report. By default, SLA data is not displayed, but you can enable this option at any time.

**To enable displaying SLA data in the report:**

1. In the **Executive Report** page, select **Executive report settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f3d604fd8b75a29070674e9d0a22013ece6239ff%2FSLA_enable_in_ER.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

> **Note:**\
> Before enabling SLA data display in the Executive Report, make sure the SLA capability is enabled in the OX platform. Go to **Settings > SLA**.

1. In the **Executive Reports Settings** dialog, enable **Add SLA to Executive Report** and select **SAVE**.

### Excluding applications from the report

You can exclude from the report specific applications that do not contribute to your understanding of the security posture.

**To exclude applications:**

1. In the **Executive Report** page, select **Executive report settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-860017947f1bc8409f1344d3c01e296eed727170%2Fexclude_apps_from_ER.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Specify application you want to exclude using application tags and select **SAVE**.

## Working with Executive Reports

Executive Report dashboard is divided into the following sections:

* [Filters](#filtering-report-information)
* [Your Organization](#your-organization)
* [Breakdown by Business Units](#breakdown-by-business-units)
* [Detailed view](#detailed-view)

## Filtering report information

The filtering options let you customize the report to focus on the data that matters most. You can filter by:

<table><thead><tr><th width="183">Filter Type</th><th>Description</th></tr></thead><tbody><tr><td><strong>Severity</strong></td><td>Show only issues of selected severity levels, such as Critical, High and so on.</td></tr><tr><td><strong>Category</strong></td><td>Include only specific security categories, such as Container Security, SBOM, or Code Security.</td></tr><tr><td><strong>Date Range</strong></td><td></td></tr></tbody></table>

## Your Organization

This section summarizes security and SLA trends across your entire organization, including the number of business units, applications, issue severity breakdowns, and recent changes.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-77af0e30aace1ca46f0d125702fc75e24b80e209%2Fyour_org_section.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| **Parameter**        | **Description**                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **AppSec org**       | Name of the organization being analyzed.                                                       |
| **2 Business units** | Number of business units under the organization.                                               |
| **14 Applications**  | Total applications managed within the organization.                                            |
| **10 Developers**    | Number of developers linked to the organization: currently 10.                                 |
| **Last Change**      | Days since the last change to code or security configuration.                                  |
| **Issues Trend**     | Indicates whether the number of issues increased or decreased compared to the previous period. |
| **SLA Trend**        | Indicates whether SLA adherence improved or declined compared to the previous period.          |
| **Appoxalypse**      | Number of Appoxalypse-class issues (most critical).                                            |
| **Critical**         | Number of critical severity issues.                                                            |
| **High**             | Number of high severity issues.                                                                |
| **Medium**           | Number of medium severity issues.                                                              |

## Breakdown by Business Units

This section provides a summary for each [business unit within](#creating-business-units) the organization, including application count, issue trends, SLA performance, and issue severity levels. It also highlights application tags to help classify assets.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d1ab6930d39aa547249e7a39ac0dbd74cf5dcba1%2Fbusiness%20units%20section.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| **Parameter**         | **Description**                                                                        |
| --------------------- | -------------------------------------------------------------------------------------- |
| **\[Business Unit]**  | Name of the business unit (e.g., Backend dev, Frontend dev).                           |
| **\[N] Applications** | Number of applications in this unit.                                                   |
| **Last Change**       | Days since the last update affecting this business unit.                               |
| **Issues Trend**      | Indicates whether issue volume increased or decreased compared to the previous period. |
| **SLA Trend**         | Indicates whether SLA adherence improved or declined compared to the previous period.  |
| **Appoxalypse**       | Number of Appoxalypse-class issues in this unit.                                       |
| **Critical**          | Number of critical severity issues.                                                    |
| **High**              | Number of high severity issues.                                                        |
| **Medium**            | Number of medium severity issues.                                                      |
| **App Tags**          | Labels describing app characteristics (e.g., PII, Cloud, Login, etc.).                 |

## Detailed view

Each section in the Executive Report summary on the left has a corresponding detailed view on the right.

This view gives you a deeper breakdown of your organization’s security data, including SLA tracking, issue distribution, and application grouping.

It's designed to help you analyze trends, track progress, and focus remediation efforts where they matter most.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dc64076889f20e36deabc9884bda6ec54b16fa54%2Fdetailed%20view.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

| Section              | Description                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| Total Open Issues    | The total number of unresolved issues in the selected scope.                                           |
| Active Issues        | Count of currently active issues by severity: Appoxalypse, Critical, High, Medium.                     |
| Last Change          | Shows when the last code and security changes were detected.                                           |
| Issue Trend          | Graph showing issue volume by severity across the selected date range compared to the previous period. |
| SLA                  | SLA tracking table showing how many issues are overdue, approaching due, or on track by severity.      |
| Issues by Severity   | Count of issues broken down by severity level.                                                         |
| Issues by Category   | Count of issues grouped by scan category (e.g., SBOM, Git Posture, CI/CD).                             |
| Application Overview | Lists how applications are grouped under business, security, and development teams.                    |
| App Tags             | Tags assigned to applications (not shown in detail if no tags exist).                                  |
| Staff                | Number of developers linked to the selected organization or unit.                                      |
