# Source: https://docs.axonius.com/docs/workflows-overview.md

# Workflows - Overview

Use Workflows to define a chain of events and actions.

* Each Workflow begins with a trigger - an Event or an Action.
* Events can come from inside Axonius, such as when a query returns more or less results from one Discovery Cycle to the next (Asset added or removed), or they can come from an external third-party source, such as Slack, BambooHR, Okta New User, Zendesk ticket updated.
* Actions are enforcement actions that perform actions internally in the Axonius system or in an external third-party system.

Workflows help you do the following:

* Create a single chain of events to support multiple scenarios, including onboarding/offboarding employees, granting new access to systems, revoking access, and incident response.
* Trigger a series of actions based on data received from incoming events or actions.
* Create sequential and conditional automations based on Events, Conditions, and Actions.

The Workflows page provides:

* A table with summarized information on each Workflow defined in the system.
* A canvas to create a Workflow using Events, Actions, Conditions, and Delays.
* A Run History page where you can see information on all runs of all Workflows or of a specific Workflow.

A Workflow begins running as follows:

* A Workflow with an Event trigger begins running when the event occurs.
* A Workflow with a Scheduled Action trigger begins running automatically according to a configured schedule.
* A Workflow with a Manual Action trigger begins running when you manually run the Enforcement Action trigger.

After the Workflow trigger completes running, it continues running and automatically performs configured actions consecutively or contingent on additional events, the results of previous actions, and delays.

A Workflow runs on one asset at a time. This means that if a query returns 10 assets, the Workflow will run ten times.

## Use Cases for Workflows

The following include common use cases for Workflows:

* **Automated Patch Orchestration** - Workflows automates the full patch lifecycle by connecting asset, vulnerability, ticketing, and software tools. It triggers remediation based on severity, updates tickets, validates fixes, and tracks compliance, reducing delays and minimizing exposure.

* **Alert Enrichment & Automated Triage** - Workflows pulls context from HR, identity, endpoint, and CMDB systems to enrich alerts in real time. This enables faster, more accurate triage, cutting false positives and analyst fatigue.

* **Identity Lifecycle Automation (in Identities)** - Workflows coordinates access provisioning and revocation across HR, ITSM, and IAM during joiner, mover, and leaver events. It enforces policy-aligned access automatically, boosting compliance and reducing risk from overprovisioning.

* **Asset Compliance Flows** - Workflows monitors asset posture and triggers remediation when systems drift out of compliance. From missing EDR to OS version gaps, it opens tickets, notifies owners, and initiates fixes, ensuring continuous policy enforcement.

## Use Case Examples

* User Termination Workflow - Upon receiving an incoming event notifying of an employee status change in Bamboo to “terminated,” the Workflow runs a series of actions based on the change.
  * If terminated, suspends them from Google Workspace, Slack, and SalesForce.
  * If not terminated, adds a tag.

![UserTerminationWorkflow(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UserTerminationWorkflow\(1\).png)

* New Hire Workflow - Upon receiving an event from Workday about a newly hired employee, the Workflow checks if the employee is temporary.
  * If Temporary, sends an email to the employee and creates a User in SAP.
  * If Permanent, creates a ticket in Zendesk, creates a user in Okta, and sends a Slack message to the channel.

![NewHireWF](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewHireWF.png)

* Alert received Workflow - When an alert is received from Rapid7, the Workflow opens a ticket in Jira with alert details, and sends an email to the Security Operations Center (SOC) manager.

![AlertReceivedWF](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AlertReceivedWF.png)

* Review need for subscription - The Workflow sends a Slack message to managers of users with access to a costly yearly subscription to confirm their need for this subscription, and based on the response, the Workflow does nothing or revokes access.