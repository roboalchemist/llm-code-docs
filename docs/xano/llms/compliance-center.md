# Source: https://docs.xano.com/enterprise/enterprise-features/compliance-center.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Compliance Center

<Tip>
  The Compliance Center is included with **Scale** and **Enterprise** plans. Certain plans may not contain all of the available features of the Compliance Center.
</Tip>

## What is the Compliance Center?

The\*\* Compliance Center\*\* provides a comprehensive history of changes made to your workspace objects. This feature allows you to track modifications, understand who made them, when they occurred, and on which Branch.

This detailed tracking offers valuable insights for collaboration, auditing, and understanding the evolution of your project. The Compliance Center records changes to the following workspace elements:

* Database tables and schema

* API groups

* API endpoints

* Addons

* Custom functions

* Background tasks

**Important Note:** Changes to individual records within your database are not tracked by the Compliance Center.

By providing a clear and accessible log of workspace modifications, the Compliance Center enhances team transparency and simplifies the process of understanding project history. This can be particularly useful for:

* **Collaboration:** Easily identify when and by whom specific changes were implemented.

* **Auditing:** Maintain a record of modifications for internal reviews or compliance requirements.

* **Troubleshooting:** Understand recent changes that may have impacted functionality.

* **Onboarding:** Quickly bring new team members up to speed on the project's development.

The Compliance Center is a valuable tool for maintaining a well-documented and understandable development process within your Xano workspaces.

## Using the Compliance Center

To access the Compliance Center navigate to the Settings tab of the workspace, open the menu icon in the top right, and select Compliance.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c77f72e0-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=b8eac020f2ee9b51b66ce7a433f4aef3" width="2280" height="729" data-path="images/c77f72e0-image.jpeg" />
</Frame>

Inside the Compliance Center, you can access various reporting areas for different types of activity in your workspace.

Each change to a workspace object is recorded in the Compliance Center:

* **ID** - the unique ID of a specific change.

* **Object** - the Workspace Object that was changed.

* **Branch** - which Branch the change occurred on.

* **Author** - the team member that made that change.

* **Date** - the time the change occurred.

### Activity Logs

Activity Logs provide an aggregated dashboard of all admin related activity across the workspace.

### Middleware Reporting

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0dae907f-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=01c4bb5b34f5fa51f907506d9f45dda4" width="2031" height="403" data-path="images/0dae907f-image.jpeg" />
</Frame>

Middlware Reporting allows you to audit your APIs, functions, and tasks to ensure that they are all using the expected [middleware](/the-function-stack/building-with-visual-development/middleware). From this view, you can also review when APIs have customized middleware, meaning they have been given different settings than what is applied at the parent object level.

### Version History

Version History is an aggregated dashboard of all schema changes across tables, APIs, functions, addons, and tasks.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c590dd9a-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=4658958c028d036e8f3fc62befa5a949" width="1547" height="452" data-path="images/c590dd9a-image.jpeg" />
</Frame>

You can click on any one of these items and immediately navigate to the item that was changed to review further as necessary.

### Trigger Reporting

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a8b0ba10-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=4fe628ead0da3a201a1a5362b34c2893" width="1579" height="401" data-path="images/a8b0ba10-image.jpeg" />
</Frame>

Similar to Middleware Reporting, Trigger Reporting allows you to audit and verify triggers. You can review both database triggers and workspace triggers.

### Instance Activity

<Frame caption="Instance Activity">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e1aaec81-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=001e034545a364d722dcb8a6cfcae524" width="490" height="554" data-path="images/e1aaec81-image.jpeg" />
</Frame>

<Frame caption="Click on an event for more details">
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0d54f819-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=6a57066d677dee64f8491e64b6a031b8" width="489" height="661" data-path="images/0d54f819-image.jpeg" />
</Frame>

The Compliance Center add-on also includes Instance Activity, available from your instance selection screen. Instance Activity offers administrators history on access to the instance. This includes login events and instance access activity, as well as team member management and permission updates. This includes time and date, user name, their location, IP address, and user agent.To access, click the⚙️ icon that appears to the right side of the instance selector, and on the panel that appears, choose Instance Activity.Instance Activity will report on **login**, **instance connect**, **instance update**, **RBAC update**, **Team update**, **Agency update**, **Image Upload**, **Custom Domain Change**, and **License Requests**.


Built with [Mintlify](https://mintlify.com).