# Source: https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-conditions.md

# Pipeline Conditions

Conditions define the context in which a workflow runs.\
They refine triggers by applying filters, such as severity, branch, or business priority.

| Condition Name         | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| Application            | Filters by the application where the issue was found.                                  |
| Application Owner      | Filters by the assigned application owner.                                             |
| Application Owner Name | Filters by the name of the application owner.                                          |
| Severity               | Filters by the current severity level of the issue.                                    |
| Original Severity      | Filters by the severity level assigned before changes or overrides.                    |
| Severity Factor        | Filters by factors that influence severity, such as exposure or exploitability.        |
| OSC\&R                 | Filters by Open Software Control & Risk (OSC\&R) framework category.                   |
| CVE                    | Filters by a specific Common Vulnerabilities and Exposures (CVE) identifier.           |
| CWE                    | Filters by a Common Weakness Enumeration (CWE) category.                               |
| Language               | Filters by programming language.                                                       |
| Business Priority      | Filters by the business priority assigned to an application.                           |
| App Tag                | Filters by application tags defined in the system.                                     |
| Issue Name             | Filters by the specific name of an issue.                                              |
| Vulnerable Library     | Filters by the library where the vulnerability was found.                              |
| PR Type                | Filters by the type of pull request (for example, minor change or major refactor).     |
| Source Tool            | Filters by the tool that reported the issue (for example, SAST or container scan).     |
| Files With Issues      | Filters by the number of files that contain issues.                                    |
| CVSS                   | Filters by Common Vulnerability Scoring System (CVSS) score.                           |
| EPSS Score             | Filters by Exploit Prediction Scoring System (EPSS) score.                             |
| EPSS Percentile        | Filters by EPSS percentile to prioritize issues likely to be exploited.                |
| Job Triggered By       | Filters by the event that triggered the CI/CD job (for example, push or pull request). |
| Job Id                 | Filters by the unique identifier of a CI/CD job.                                       |
| Scanned Branch         | Filters by the branch that was scanned.                                                |
| Target Branch          | Filters by the branch targeted in a merge or pull request.                             |
| Event Type             | Filters by the event type, such as pipeline run, scheduled job, or webhook event.      |
| Issue Actions          | Filters by the action taken on an issue (for example, created, reopened, or closed).   |
