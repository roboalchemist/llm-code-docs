# Source: https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow/workflow-conditions.md

# Workflow Conditions

Conditions define whether the workflow should proceed after a trigger. They act as filters that evaluate metadata related to the application, issue, or <mark style="color:yellow;">user.</mark>

Conditions allow you to narrow down automation to specific scenarios, such as triggering actions only for high-severity vulnerabilities in production environments or issues in critical applications.

You can refine workflow execution using conditions. Examples include:

* **Application**: Specify one or more applications.
* **Severity**: Limit to issues with Critical, High, Medium, or Low severity.
* **Business Priority**: Filter by the assigned business impact.

??????If no application is specified, the workflow applies to all applications by default.

| **Condition**          | **Description (if known)**                                                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Application            | Filter by specific application                                                                                                   |
| Application Source     | Filter by source repository or system                                                                                            |
| Application Owner      | Filter by owner entity                                                                                                           |
| Application Owner Name | Filter by specific owner name                                                                                                    |
| Severity               | Current severity of the issue                                                                                                    |
| Original Severity      | Initial severity before any modification                                                                                         |
| Severity Factor        | <p>Multiplier or weight applied to severity<br><mark style="background-color:red;">to find a better definition for SF</mark></p> |
| OSC\&R                 | Mapped to OSC\&R framework category                                                                                              |
| CVE                    | Filter by specific CVE identifier                                                                                                |
| CWE                    | Filter by specific CWE category                                                                                                  |
| Language               | Programming language of the affected component                                                                                   |
| Business Priority      | Application business impact rating                                                                                               |
| App Tag                | Filter by tags assigned to applications                                                                                          |
| Issue Name             | Specific issue identifier or title                                                                                               |
| Vulnerable Library     | Name of the library with the vulnerability                                                                                       |
| PR Type                | Type of Pull Request (e.g., bug fix, feature)                                                                                    |
| Source Tool            | Tool that identified the issue                                                                                                   |
| Registry Name          | Name of the container/image registry                                                                                             |
| Registry Type          | Type of registry (e.g., Docker, GitHub)                                                                                          |
| Artifact Image         | Container image name                                                                                                             |
| Files With Issues      | Number or list of files that include issues                                                                                      |
| CVSS                   | CVSS base score                                                                                                                  |
| EPSS Score             | Exploit Prediction Scoring System score                                                                                          |
| EPSS Percentile        | Percentile ranking of EPSS score                                                                                                 |
| First seen             | Date the issue was first detected                                                                                                |
| Commit Date            | Date of related code commit                                                                                                      |
| Compliance Standard    | Mapped standard (e.g., ISO, NIST)                                                                                                |
| SLA                    | Service level agreement status                                                                                                   |
