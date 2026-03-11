# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/issue-change-insights.md

# Change Intelligence

The Change Intelligence page helps you understand how issues evolve between scans by showing what changed, when it changed, and how those changes affect your security posture. It highlights new issues, resolved issues, removed issues, and severity changes so you can track risk trends over time instead of reviewing individual findings in isolation.

By combining trend analysis with detailed scan comparisons, Change Intelligence allows you to identify regressions, validate remediation efforts, and understand the impact of coverage or detection changes across applications and time periods.

Change Intelligence data is also available through the API for automation, reporting, and integration with external systems.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f2bd6497d9938bf628ff8a1e5759375eff588025%2FChange%20Inteligence%20(3).png?alt=media" alt=""><figcaption></figcaption></figure>

## Filters

Filters define the scope of data shown across the entire Change Intelligence view.

The selected filters are applied together and affect the trend graph, Latest Scan Changes, and Historical Changes.

Updating any filter immediately refreshes the data to reflect the selected scan range, application scope, and severity levels.

<table><thead><tr><th width="159.83331298828125">Filter</th><th>Description</th></tr></thead><tbody><tr><td><strong>Time range</strong></td><td><p>Controls two aspects of the data:</p><ul><li>The range of past scans that can be compared against the latest scan</li><li>Extends or limits the time period of historical scans displayed in the trend graph and the Historical Changes view.</li></ul></td></tr><tr><td><strong>Application</strong></td><td>Filters the data to include only issues related to the selected applications. This filter affects the trend graph as well as both the Latest Scan Changes and Historical Changes sections.</td></tr><tr><td><strong>Severity</strong></td><td>Filters the data to include only issues with the selected severity levels. This filter affects the trend graph as well as both the Latest Scan Changes and Historical Changes sections.</td></tr></tbody></table>

## Issues Status Trend Over Time

This section provides a graph that shows the number of issues over time by type of change. You can use the date selector to view data for different periods, such as the last week or month.

<table><thead><tr><th width="248.16668701171875">Change Type</th><th>Description</th></tr></thead><tbody><tr><td><strong>New</strong></td><td>Issues discovered for the first time in the selected period.</td></tr><tr><td><strong>Changed Severity</strong></td><td>Issues whose severity level was updated since the last scan.</td></tr><tr><td><strong>Resolved</strong></td><td>Issues that were fixed and are no longer active.</td></tr><tr><td><strong>Removed</strong></td><td>Issues that were removed because their source or component was removed.</td></tr></tbody></table>

## Latest Scan Changes

This section lists all changes detected between the latest scan and the selected previous scan. It allows you to compare results and identify what has changed since the last run.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-84f0a62687af0805e5e8c4dc0c1d4bd5ac6032f9%2FLatest_Scan_Changes.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Counters at the top of the list summarize totals for each category.

Each record in the list includes key information about the issue and its change type. You can expand an item to see detailed context.

The following examples illustrate common types of issue changes displayed in this view:

| What you see                                                                                                           | What it means                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **114 New** with severity counters                                                                                     | A total of 114 new issues were detected between the latest scan and the selected past scan. The colored counters show how these new issues are distributed by severity.                                                                                                                                                                                        |
| **Repository CTO / ChainProtect – development was created on Sat Feb 07 2026 and first seen in OX on Mon Feb 09 2026** | A repository that was scanned by OX for the first time. All issues listed under this entry are considered new relative to the selected comparison scan.                                                                                                                                                                                                        |
| **Detected by policy – CSPM issue**                                                                                    | Issues that were identified as a result of policy evaluation rather than code, dependency, or image scanning.                                                                                                                                                                                                                                                  |
| **Dependency `webpack@5.101.1` was assigned a new vulnerability (CVE-2025-65438)**                                     | A dependency that was associated with a newly published vulnerability. The discovery date indicates when the vulnerability information became available to OX.                                                                                                                                                                                                 |
| **Clickable issue count or severity badge**                                                                            | Selecting a link navigates you to a filtered issues view. For **New** entries, the link opens the **Active Issues** page showing the newly detected issues. For **Resolved** or **Removed** entries, the link opens the corresponding **Resolved** or **Removed** issues view, allowing you to review issues that were closed or removed in the selected scan. |

### Export

You can export change data directly from the Change Intelligence page.\
Export options include exporting all detected groupings or exporting only the groupings that match the currently applied filters.

### AI Summary

AI Summary provides an automated overview of the issues currently displayed on the page. It summarizes the findings based on the current view, helping you understand what stands out without reviewing every record manually.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4ba5987e058ada55522dfbc2d504a05fdf33f7e7%2FChange_Intelligence_AI_Summary.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

This is useful when you have a large number of issues or frequent scan updates, and you need a quick way to understand the main changes and risks.

AI Summary is optional and disabled by default. This allows organizations to control whether issue data is sent to an AI service, based on internal security and compliance requirements.

When AI Summary is enabled, no issue details, image names, application names, or user data are sent to the AI model. Only library names may be shared for processing in order to generate the summary. Some organizations keep this disabled due to legal or privacy requirements.

Organizations can configure AI Summary to work with their own OpenAI token. In this case, data is sent using the customer-managed token.

**To Enable AI Summary:**

1. Go to **Settings** > **AI Settings**.
2. Enable **AI Summary**.

## Historical Changes

The Historical Changes view shows issue updates from previous scans within the selected date range. It helps identify when issues were introduced, when their severity changed, and how risks evolved over time.\
Each entry reflects the state of the issue at that scan point, including severity changes, resolution, or removal.

Historical results reflect the state of issues at the time of each scan. As coverage, scope, or detection logic changes, issues may later appear as resolved or excluded. For this reason, issue links are available only for the latest scan.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2007c965196dcdc061ced7dd715af3de8b4c2e64%2Fhistorical_change.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

The following examples illustrate how to interpret common entries in the Historical Changes view.

| What you see                                                                                             | What it means                                                                                                                      |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **34 New** with severity counters                                                                        | Thirty-four new issues were detected in this scan. The counters show how these issues are distributed by severity.                 |
| **Development dependencies are now deprecated**                                                          | Issues that were detected because certain dependencies were marked as deprecated during this scan.                                 |
| **Private image `ppa:latest` created was scanned for the first time because it was detected in runtime** | A container image that was scanned for the first time after being detected as running in the environment.                          |
| **45 Removed**                                                                                           | Issues that were removed in this scan, typically due to scope reduction, coverage changes, or components no longer being relevant. |
