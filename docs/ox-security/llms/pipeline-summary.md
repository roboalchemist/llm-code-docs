# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary.md

# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/understanding-pipeline-scan-results/pipeline-summary.md

# Pipeline Summary

The Pipeline Summary page provides a high-level view of all pipeline scans across your organization and lets you drill into specific jobs.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f3b08c4a0217f2c4e4e85957ace2a13128b89b8c%2FPipeline%20summary.png?alt=media" alt=""><figcaption></figcaption></figure>

### KPI Cards & Trend Charts

| Widget                                                          | Description                                                   | How to read it                                                                                                    |
| --------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Pipeline Protected Repos** (donut)                            | Distribution of repositories protected by pipeline workflows. | Segments show the count per state (for example, **Passed**, **Monitor**, **Blocked**) with a total in the header. |
| **Pipeline Scan Status Trend** (line)                           | Trend of pipeline scan outcomes over time.                    | Lines track counts per status (Passed/Monitor/Blocked) by date.                                                   |
| **Pipeline Scan Trends (Grouped by Issue Severity)** (area/bar) | New issues found in pipeline scans, grouped by severity.      | Use it to spot spikes in **Critical**/**High** findings after recent changes.                                     |
| **Pipeline Duration Trend** (line)                              | Average or median runtime of pipeline scans over time.        | Use to monitor performance regressions in scan duration.                                                          |

### Filters Panel

Use the left panel to narrow results. You can combine multiple filters, save them under My Filters, and clear them at any time.

| Filter                     | What it narrows                               | Examples / Notes                                                               |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------ |
| **Result**                 | Overall pipeline scan outcome.                | Passed, Monitor, Blocked.                                                      |
| **Application**            | Specific app/repository.                      | Filters all widgets and the grid to the selected app(s).                       |
| **Severity**               | Findings severity considered in results.      | Critical, High, Medium, Low.                                                   |
| **Event Type**             | Source-control event that triggered the scan. | Push, Pull/Merge Request.                                                      |
| **CI/CD Type**             | The CI/CD system used.                        | GitHub Actions, GitLab CI, Bitbucket Pipelines, Jenkins, Azure Pipelines, etc. |
| **Scanned Branch**         | Branch name or pattern.                       | `main`, `release/*`, feature branches.                                         |
| **App Tag**                | Application labels/tags.                      | Use tags for teams, services, or risk groups.                                  |
| **Job Triggered By**       | Who initiated the job.                        | Username/service account.                                                      |
| **Job ID**                 | Specific pipeline job identifier.             | Paste or select a known ID to jump to that job.                                |
| **Scan Completion Status** | Technical execution status.                   | Completed, Timed out, Error.                                                   |
| **Scan Type**              | What was scanned.                             | Code, Container image, etc.                                                    |
| **Artifact**               | Artifact identifier/name (if applicable).     | Image digest/name, package, etc.                                               |
| **Artifact Tag**           | Artifact tag or label.                        | For example, `v1.2.3`, `latest`.                                               |

### Results Grid

The table lists each pipeline scan. Most cells link to details.

| Column             | What it shows                                      | Interactions / Notes                                                                                                 |
| ------------------ | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Job ID**         | Unique identifier for the pipeline scan job.       | Click to open the job’s details page (summary, issues, logs).                                                        |
| **Scanned Branch** | Branch that triggered the scan.                    | Helps correlate findings to code paths/releases.                                                                     |
| **App Name**       | The application (repository) scanned.              | Click to open the app overview (depending on permissions).                                                           |
| **Scan Type**      | The kind of scan that ran.                         | Indicates whether the scan was for Source Code or a Docker Image.                                                    |
| **Triggered By**   | User or system that started the scan.              | Shows avatar/name when available.                                                                                    |
| **Issues**         | Whether issues were detected.                      | A check (✓) means no issues of interest. A number indicates count of issues that met your workflow conditions.       |
| **Blocking**       | Whether the workflow triggered a **block** action. | ✓ means not blocked. You may also see a ratio such as **0 out of 1** (blocked rules matched / total blocking rules). |
| **Date**           | When the scan completed.                           | Uses your selected time range.                                                                                       |

### Common Tasks

* **Check organization health:** Use the Pipeline Protected Repos donut and Status Trend chart to see protection coverage and outcome trends.
* **Investigate recent spikes:** Look at Pipeline Scan Trends (Grouped by Issue Severity) to spot increases in Critical/High findings; filter by Application or Scanned Branch to localize.
* **Review slow scans:** Use Pipeline Duration Trend and filter by CI/CD Type or Application to find regressions and tune performance.
* **Drill into a specific job:** Find the row by Job ID or apply filters, then click Job ID to open details, such as issues, policy matches, and actions taken.
