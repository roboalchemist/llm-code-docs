# Source: https://docs.axonius.com/docs/ec-overview.md

# Action Center Overview

Use the Action Center to actively control your asset environment. Use it to build and apply policies and create triage and remediation actions. Enforcement actions may be automated via Enforcement Set scheduling or in a Workflow, or run manually.

Enforcement actions help to:

* **Focus your resources** - Automate time-intensive tasks like filing helpdesk tickets, enriching asset data, or updating vulnerability scan coverage.
* **Reduce mean time to compliance** - Automatically close security control gaps as they’re discovered by isolating devices from the network, enabling or disabling users, and deploying software.
* **Maintain IT hygiene** - Continuously check against security policies and automate corrective action for devices, cloud assets, and users. Deploy software, run remote commands, isolate devices from a network, update vulnerability scans, enable or disable users, and much more.
* **Automate policy enforcement** - Create configurable Enforcement Sets to automatically correct noncompliance, notify the proper people of identified threats, enrich data, and respond to, mitigate, or remediate issues.
* **Alert the right teams** - From sending contextualized data to creating an incident response ticket, Axonius can automatically alert the right teams at the right time, via your platform of choice. Set up custom emails or get notifications via Jira, Slack, ServiceNow, Zendesk, and more.
* **Enrich asset data** - Augment asset data with information from third-party data sources such as Shodan, Censys, HaveIBeenPwned, Portnox, and more. Axonius also makes it easy to add or update device data into a Configuration Management Database (CMDB).

You can also view the Action Center run history (i.e., run history of Enforcement Sets and Workflows), test an Enforcement Set before running it, and organize Enforcement Sets and Workflows in folders.

## Action Center Tools

The Action Center includes the following tools:

* Enforcement Actions
* Enforcement Sets
* Enforcement Set management
* Enforcement Set scheduling
* Test run of an Enforcement Set
* Test adapter connections
* Run history
* Workflows
* Workflow management

### Enforcement Actions

Use Enforcement Actions to take direct steps to mitigate vulnerabilities and policy violations on assets returned by the query.
Enforcement Actions can also:

* Create incidents
* Enrich the data in Axonius
* Add and remove tags
* Delete devices or users
* Manage CMDB assets
* Update VA coverage
* Manage AWS services
* Deploy files and run commands
* and much more.

Enforcement Actions can be grouped into sets and run together.

### Enforcement Sets

Enforcement Sets execute Actions on a saved query (which can represent a security policy), and can automatically perform one or more actions on the entities that match the query parameters (policy gaps). Enforcement Actions can mitigate, notify, or create incidents on the identified gaps.
Enforcement Actions in an Enforcement Set can be automated or executed manually, depending on your comfort level. You can also use Enforcement Sets to send notifications about events in the system, for instance, activity log events or fetch history events.

An Enforcement Set can include the following:

* **Main action** - A main Action is executed on all assets returned by the query. The Action may or may not run successfully on each asset. Only one main Action can be configured.
* **Success actions** - One or more Enforcement Actions that run on each asset for which the main Enforcement Action completes successfully.
* **Failure actions** - One or more Enforcement Actions that run on each asset for which the main Enforcement Action does not complete successfully.
* **Post actions** - One or more post Actions that run on all assets matching the query after the main Action has completed.

An execution of an Enforcement Set is called a “run.”

Learn more about [Enforcement Sets](/docs/using-the-ec-page).

### Workflows

Use Workflows to create automations based on events, conditions, and Action Center actions. You can create a single workflow to trigger a series of actions based on data received in incoming events, while supporting multiple scenarios, from user onboarding to incident response.

Axonius provides a canvas, where you can create a workflow using events, conditions, and actions. You configure a workflow with a triggering event, any number of routes and branches to sub-routes, and multiple actions that are executed consecutively or contingent on additional events or actions.

Workflows can be triggered by:

* Third-party based incoming events that notify of changes in external systems.
* Events inside Axonius due to changes in your asset pool - either by a newly created asset in the system or by an existing asset changing its values.
* Actions (scheduled or manually run).

For example, you can create a workflow that is triggered by an incoming event - BambooHR notifying of a user's changed status. The workflow is configured with a series of actions depending on the new status:

* Terminated - Activates Okta suspend, GSuite suspend, and Azure suspend.
* Hired - Creates a user in Okta and adds the 'new hire' tag.

To learn more, refer to [Workflows](/docs/workflows).