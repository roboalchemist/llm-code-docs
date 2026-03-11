# Source: https://docs.axonius.com/docs/case-management-overview.md

# Case Management

**Case Management** in Axonius provides an in-house ticketing and remediation system designed to track, assign, and automatically measure the progress of specific issues identified within your asset inventory.

Essentially, Cases function as internal tickets, eliminating the need for manual data exports or managing remediation in a separate, third-party ticketing system. Cases link the identified problems directly to the necessary actions and monitor the resolution in real-time from within Axonius.

A Case serves as the central control point by linking:

* The problem: Defined by a **Query** or **Finding Rule** (e.g., "Devices missing security agent").
* The responsible party: An assigned User or team.
* The action: The potential remediation task and due date.
* The tracking: Real-time progress monitoring as assets meet compliance.

Cases can be created based on the following:

* **Queries** (asset remediation) - From the **Case Management** page, you create Cases based on simple queries to manage remediation for a dynamic list of assets that match specific criteria.
  * You can use Axonius queries to identify system issues or anomalies that require attention and correction. For example, 'Devices that have not been seen in the last 30 days' or 'Running GCP Instances Not Covered by an Endpoint Protection Tool (AX)'.
  * When you identify problematic assets using a Query, you can [create a **Case** in Axonius](/docs/creating-a-new-case) to address the issue, assign it to a relevant User, and track its progress until all assets with the issue are resolved.
  * You can link a Case to any type of asset query in a many-to-many asset-case relation. You cannot link a case to an internal module query, such as Adapters Fetch History.

* **Finding Rules** (security/compliance issues) - Cases created from the Findings Center focus on resolving specific security or compliance risks identified by your Finding Rules.
  * You create the Case either from an Alert triggered by a rule (in the Alerts table) or directly from a Finding Rule (in the Rule Management table).

You can manage, monitor, and update all active Cases in the system from one central location - the [**Case Management** page](/docs/case-management-page).

## Case Management Use Cases

Cases eliminate the dependency for external ticketing systems in routine asset and risk remediation, and offer a highly contextualized alternative.

### Asset Management: Enforcing Compliance

This shows how Cases track real-time compliance improvements.

* **Case Title:** Install Tanium on all devices
* **Query:** Devices without Tanium installed
* **Assignee:** IT expert
* **Due date:** February 18th, 2024

#### Problem Space

A query running in Axonius indicates that many devices do not have Tanium installed, which poses a security risk. The IT expert in your organization has been assigned to remediate this issue by the end of the week.

#### Solution

Create a Case, link it to the query, assign it to an IT expert, and set a due date to complete the task. You can link additional queries or Enforcement Sets to the Case, and notify users via email about the new Case assigned to them. Once saved, the Case tracks progress automatically. As the IT expert installs Tanium on a device, that device no longer matches the query, and the Case's green progress bar advances.

#### Benefits

Provides real-time visibility into asset remediation progress, eliminating the need for manual updates and external ticketing.

### Risk Management: Tracking Patching Efforts

This shows how to link identified risk to automated or assigned remediation efforts.

* **Case Title:** Remediate Java 10 exploit
* **Query:** Devices with Security Findings (vulnerabilities) CVE-123, CVE-124, CVE-125
* **Assignee:** Jane Smith
* **Due date:** April 6th, 2024
* **Linked remediation:** Update Java version to 12 (via Enforcement Set)

#### Problem Space

A query running in Axonius shows many devices with critical Security Findings, including CVE-123, CVE-124, and CVE-125. Jane Smith, an employee in your organization, is assigned to remove these Security Findings from these devices by the end of the week.

#### Solution

Create a Case, link it to this query, assign the Case to Jane Smith, and set a due date to complete the task. You can also link an Enforcement Set designed to upgrade Java in devices to version 12, to reduce the Security Finding count. Once the Case is saved, it tracks progress as devices fall out of the high-risk query.

#### Benefits

The Case centralizes Security Finding management, eliminating the need for third-party ticketing. It measures the success of the remediation (manual or automated via Enforcement Set) by showing how many devices no longer match the high-risk query criteria.