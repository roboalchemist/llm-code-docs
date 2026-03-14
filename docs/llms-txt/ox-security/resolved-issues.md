# Source: https://docs.ox.security/scan-and-analyze-with-ox/analyzing-scan-results/resolved-issues.md

# Resolved and Removed Issues

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

The [Resolved Issues](#resolved-issues) and [Removed Issues](#removed-issues) pages in the OX Security platform provide auditability, transparency, and insights into the security issues lifecycle.

These pages support teams in reviewing what has been addressed, understanding why issues disappeared, and exporting reports for analysis or compliance.

### Supported Categories

Currently, the resolved/removed Issues views support the following categories (EA stage):

* **Secrets**
* **Static Code Analysis** (referred to internally, not in UI)
* **Git Posture**
* **Cloud CSPM**

> **Note:** Currently third-party issues, such as Snyk and Prisma, are not yet supported in these views.

## Exporting resolved/removed issues

You can export resolved issues as CSV files.

Export is limited by user role. You can define which roles can export issues, for example, define that read-only users can only view.

The following export options are available:

* Exporting all the issues
* Exporting limited by filtering, for example, only high severity, by application, and so on.

## Resolved issues

Resolved Issues are security issues that were identified and later resolved by code fixes, configuration changes, permission updates, dependency removal or updates, and so on.

These issues are no longer active, but are kept in a dedicated view for auditing and reporting.

Monitoring resolved issues provides the following advantages:

* **Accountability**: Teams can track what was fixed and by whom.
* **Learning and Prevention**: Reviewing resolved issues can help prevent similar mistakes in the future.
* **Reporting**: Teams can export a report of resolved issues for compliance or KPI tracking.
* **Verification**: Ensures issues were not accidentally removed without resolution.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c6bf1517b166260f4f8080163ea0baed1dcfbf63%2FResolved_issues%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

| Section                  | Description                                                                                                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Filters Panel**        | Located on the left side, it includes filters such as Resolved Reasons, Severity, Application, Category, Issue Name, CVE, etc., to narrow down the issue list.                                                                                          |
| **MTTR and Trend Graph** | Displays Mean Time To Resolution (MTTR) for various severity levels (e.g., Appoxalypse, High, Medium) and a trend graph of issue resolution over time.                                                                                                  |
| Resolved Issues Table    | <p>Main table displaying resolved issues in which most of the columns are the same as in the Active Issues page, except for the following:<br>- <strong>Resolved Date</strong><br>- <a href="#resolved-reason"><strong>Resolved Reason</strong></a></p> |
| Issue Details Panel      | Appears when selecting a row in the table. Tabs include Summary, App Info, Vulnerabilities, Artifacts, and more, providing complete context for the resolution.                                                                                         |

### Resolved issues use cases

* A developer removed a credential from the code.
* An application admin changes repo settings to fix a misconfiguration.
* Teams want to generate a report of all high-severity issues resolved in the last month.
* A configuration change closed an exposure.

### Resolved Reason

The OX platform assigns a Resolved Reason automatically, which reflects how the issue was resolved, as follows:

* **Configuration fixed**
* **Dependency removed**
* **Outside collaborator status changed**
* **Branch protection configuration changed**
* **Org member repos now private**

These reasons are predefined by OX and may evolve as the platform expands.

## Removed Issues

Removed issues are security issues that that no longer appear in the OX platform. OX Security changes issue status to removed in the following cases:

* OX changes detection logic, for example, updated signatures
* Applications being inactive for extended periods such as 6 months and more
* User-defined exclusions

Monitoring removed issues helps explaining why issues suddenly disappear from the active issues list and prevents confusion about missing issues.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2a97e23404e320e9b6f3d1b64f994a2f05ccb581%2FRemoved%20Issues.png?alt=media" alt=""><figcaption></figcaption></figure>

The Removed issues page contains the same components as the Active Issues page.

Typical use cases are:

* OX changed detection rules, so certain issues are no longer flagged.
* An application hasn’t been active for over six months.
* An exclusion rule removed the issue.
