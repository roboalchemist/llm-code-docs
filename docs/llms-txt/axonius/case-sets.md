# Source: https://docs.axonius.com/docs/case-sets.md

# Case Sets

**Case Sets** integrate Axonius's internal Case management with external ticketing systems. This feature simplifies issue tracking and resolution by connecting Axonius Cases (internal tickets) to external tickets (from third-party systems like Jira or ServiceNow), alongside capabilities for recurring cases and automated core follow-up actions.

## Why Case Sets are Needed

Axonius users, such as Security, IT Operations, Compliance, and Platform Admins, often create [**Cases**](/docs/case-management-overview) within Axonius. These Cases allow them to directly manage and resolve issues identified by the platform, significantly reducing the need to rely on external ticketing systems for daily operations. This process involves identifying an issue, creating a Case (potentially based on an Axonius Query or Finding), assigning it, setting a due date, monitoring progress, and ultimately resolving it - all without switching to third-party ticketing systems like Jira or ServiceNow.

However, not all personnel within an organization (for example, a finance manager who only needs summary reports) have direct access to Axonius. To involve these individuals in issue management, Axonius users frequently create tickets in external systems. This ensures everyone can participate in resolving issues identified by Axonius, even without direct access to the platform. External ticketing systems also provide a formal way for Axonius users to document their work and progress.

The primary challenge arises from the lack of correlation between issues identified in Axonius and their corresponding external tickets. For instance, if an Axonius user creates an external ticket to resolve a vulnerability, the status in Axonius remains disconnected from the external ticket's status. This means resolving the vulnerability in Axonius doesn't automatically close the external ticket. Conversely, if an external ticket wasn't created via Axonius, closing it won't be reflected in Axonius.

## How Case Sets Solve the Problem

**Case Sets** directly address this lack of correlation by enabling a direct link between Axonius Cases and external tickets. Through the **Case Set wizard**, you can:

* Create one-time or recurring Cases for identified issues.
* Simultaneously create and link external tickets to their corresponding Cases. You can link a new external ticket to a Case.
* Define automated actions based on event updates, such as asset resolution or ticket status changes.

Once linked, the Axonius Case receives updates from the associated external ticket (e.g., status, description, owner), facilitating coordination. This feature enhances Case Management by automating the creation of both Axonius Cases and linked external tickets. It also enables recurring case generation to continuously address gaps and supports automated follow-up actions.

This feature benefits:

* Security Operations, IT Operations, and any team that needs to coordinate remediation efforts involving users both inside and outside of Axonius.
* Teams aiming for automated and actionable remediation workflows across diverse toolsets.
* Organizations with diverse toolsets and access levels.

## Key Benefits of Case Sets

The following are key benefits of the Case Sets feature:

* **Automated case and ticket Creation** - Use the wizard to set up recurring, automatic generation of Cases with linked external tickets for known issues.
* **Event-driven actions** - Trigger automatic follow-up actions based on asset resolution or ticket status updates.
* **Centralized actionability** - Manage and monitor all related external tickets from Axonius for each Case.

## Use Cases for Case Sets

Case Sets have many uses, including:

* **Vulnerability remediation** - Create recurring Cases for critical CVEs, link them to Jira tickets for patching, and automatically close Cases when tickets are resolved and assets are remediated.
* **Privileged access cleanup** - Identify overprovisioned or dormant privileged accounts and coordinate cleanup efforts across security and IT operations teams.
* **Asset hygiene and compliance** - Generate Cases for noncompliant assets (e.g., those without EDR installed), link them to external queues, and ensure issues are addressed and auditable.
* **Agent management** - Address missing or misconfigured agents on devices.
* **Exposure management** - Proactively manage and mitigate Security Findings and exposures.
* **Shadow IT handling** - Handle unapproved software and SaaS applications.