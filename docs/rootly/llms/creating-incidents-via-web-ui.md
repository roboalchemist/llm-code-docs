# Source: https://docs.rootly.com/incidents/creating-incidents/creating-incidents-via-web-ui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Incidents via Web Interface

> A step-by-step guide to creating incidents using the Rootly web interface, including how to complete the incident form, customize fields, and configure assignment and automation behavior.

### Overview

The Rootly web interface provides the most complete and structured way to create an incident. It supports rich field configuration, required-field validation, access controls, and the full power of automations and workflows.

Use the web interface when you need clarity, accuracy, and full control over the incident creation experience.

<Tip>
  The Web UI is the most reliable way to create high-quality incidents. It enforces all required fields, validations, and permissions set by your workspace.
</Tip>

### Create a New Incident in the Web App

<Steps>
  <Step title="Open the New Incident Form">
    You can initiate a new incident from several locations:

    * **Dashboard → Create Incident** (top-right)
    * **Incidents → Create Incident** (top-right)

    **Global Action Menu → Create Incident** (bottom-left)

    This opens the full New Incident form.

        <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/createincidentweb1.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=dc37a1003a4c46b09a0ea2cbe190d7cc" alt="images/createincidentweb1.jpg" width="982" height="284" data-path="images/incidents/createincidentweb1.webp" />
  </Step>

  <Step title="Fill in the Incident Details">
    The New Incident form captures all core information needed to begin coordinated response and trigger automation.

    Most fields are customizable under **Configuration → Forms**.

    **Default fields include:**

    | Field               | Description                                                         |
    | :------------------ | :------------------------------------------------------------------ |
    | **Title**           | Name of the incident; also used to generate the Slack channel name. |
    | **Summary**         | Short description of what’s happening.                              |
    | **Severity**        | Defaults from SEV3 → SEV0.                                          |
    | **Type**            | Defaults: Cloud, Security, Customer-Facing, Default.                |
    | **Mark as Private** | Restricts visibility to permitted users.                            |

        <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/newincidentformweb2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=94d97d70fc8b1a4f49c354b6996f3149" alt="images/newincidentformweb2.jpg" width="588" height="630" data-path="images/incidents/newincidentformweb2.webp" />

    **Additional Notes**

    * Required fields are marked with a **\***
    * Leaving **Title** blank activates the **Automatic Incident Title Generator**
    * Only owners, admins, or privileged users can create/view private incidents
    * Private incidents are recommended for security-, privacy-, or customer-sensitive issues

    <Info>
      If your team uses **Mark as In Triage**, selecting this checkbox starts the incident in **Triage** instead of **Started**. See the *Incident Lifecycle* page for details on how these statuses differ.
    </Info>
  </Step>

  <Step title="Review Required Fields (If Applicable)">
    Your workspace may enforce:

    * Required fields on incident **creation**
    * Required fields for **specific lifecycle transitions**
    * Required fields based on **severity**, **incident type**, or **team**

    If you miss a required field, the Web UI will block submission and highlight the missing values.

    <Tip>
      Completing required metadata during creation prevents blockers later when moving the incident from Started → Mitigated → Resolved.
    </Tip>
  </Step>

  <Step title="(Optional) Add Additional Context">
    Depending on how your team configures the form, you may see optional sections such as:

    * Services
    * Functionalities
    * Environments
    * Groups
    * Incident Types
    * Labels
    * Notify Emails
    * Custom form fields
    * Test Incident checkbox (if enabled)

    Adding contextual metadata improves:

    * Automated routing
    * Workflow execution
    * Analytics and dashboards
    * Retrospective quality
  </Step>

  <Step title="Create the Incident">
    Click **Create Incident**.

    Upon creation, Rootly will automatically:

    * Create the incident record
    * Capture lifecycle timestamps (e.g., started\_at)
    * Trigger your incident-creation workflows
    * Create a Slack incident channel (if enabled)
    * Assign default responders or roles
    * Add initial timeline entries
    * Redirect you to the newly created incident page

    <Tip>
      Most teams automate channel creation, role assignment, and stakeholder notifications to reduce manual overhead and speed up initial response.**Customize the New Incident form in the Web app**
    </Tip>
  </Step>
</Steps>

### After the Incident Is Created

Once the incident is open, you can:

* Update lifecycle status (Triage → Started → Mitigated → Resolved → Closed)
* Assign roles and add responders
* Add timeline entries
* Attach or review alerts
* Trigger or monitor workflows
* Publish stakeholder updates
* Track action items and tasks
* Join the Slack channel associated with the incident

All changes are tracked automatically and appear in the Timeline for retrospective analysis.

### Customizing the New Incident Form

<Steps>
  <Step title="Open Form Configuration">
    Navigate to:

    **Configuration → Forms → New Incident → Configure**

    Then select the **Web** tab.

        <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/newincidentwebeditform.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=b0eede159e4c0615e04a5944115e1925" alt="images/newincidentwebeditform.jpg" width="1213" height="741" data-path="images/incidents/newincidentwebeditform.webp" />

    You can optionally copy the structure from the Slack form using:

    **Copy fields from Slack form**

    * Left panel: current form structure
    * Right panel: real-time preview
  </Step>

  <Step title="Edit and Manage Fields">
    You can customize:

    * Field order
    * Field visibility
    * Required fields
    * Custom field types (dropdowns, multi-selects, relations, etc.)

    Use:

    * **Drag handle (six dots)** → reorder fields
    * **Pencil icon** → edit a field
    * **Minus icon** → remove a field
    * **Add Fields** → add new fields

    Changes save automatically.

    <Tip>
      We recommend keeping Slack and Web forms aligned so responders have a consistent experience regardless of where incidents are created.
    </Tip>
  </Step>
</Steps>

### Troubleshooting

<AccordionGroup>
  <Accordion title="“I can’t create an incident.”">
    Check for:

    * Missing required fields
    * Missing permissions
    * Private incident restrictions
  </Accordion>

  <Accordion title="“My workflows didn’t run.”">
    Confirm that workflow conditions match:

    * Severity
    * Type
    * Services
    * Environments
    * Groups
  </Accordion>

  <Accordion title="“Why is the form blocking me?”">
    Required-fields enforcement or conditional visibility rules may be preventing submission.
  </Accordion>

  <Accordion title="“Slack channel wasn’t created.”">
    Verify:

    * Slack integration is enabled
    * Auto-channel creation is turned on
    * The incident wasn’t created as private (depending on workspace rules)
  </Accordion>
</AccordionGroup>

### Best Practices

* Use structured fields (Severity, Services, Environments) for clarity & analytics
* Keep required fields minimal but meaningful
* Use Private mode for security or privacy-sensitive incidents
* Align Slack and Web forms for consistency
* Automate repetitive creation steps with workflows
* Provide descriptive titles and actionable summaries

High-quality incident creation dramatically accelerates response and improves clarity for everyone involved.


Built with [Mintlify](https://mintlify.com).