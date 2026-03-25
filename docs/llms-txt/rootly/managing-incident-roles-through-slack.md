# Source: https://docs.rootly.com/incidents/incident-roles/managing-incident-roles-through-slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Incident Roles Through Slack

> Learn how to assign, update, and manage incident roles—such as Incident Commander or Communications Lead—directly from Slack using Rootly’s role assignment dialog and commands.

### Overview

Slack is often where incident response actually happens, so Rootly lets you assign and manage incident roles **directly inside the incident channel**, without switching back to the web interface.

This includes:

* Assigning yourself to a role
* Assigning or removing other responders
* Editing all incident roles in one modal
* Adding roles that aren't yet part of this incident
* Managing multi-user and single-user roles
* Enforcing permission checks for private incidents

To use these Slack capabilities, make sure the [Slack integration is installed](/integrations/slack).

<Info>
  Role management in Slack only works inside an **incident channel** and requires permission to assign incident roles.\
  For private incidents, users must also have update permission for private incidents.
</Info>

***

### Manage Roles via Slack

<Steps>
  <Step title="Open the Incident Channel">
    Navigate to the Slack channel for the incident.\
    Slack commands and buttons rely on the channel’s mapping to an active incident.
  </Step>

  <Step title="Open the Role Assignment Modal">
    You can open the Assign Roles modal in two ways:

    **Option A: Use the Assign Roles button**

    When an incident is created, the pinned incident summary includes an **:firefighter: Assign Roles** button.

    <Frame caption="Assign Roles button in the Slack incident summary">
            <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/roles-slack/1.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=fc76ca83b40d172f0760498b5b4f6260" alt="Assign roles from the incident summary" width="899" height="489" data-path="images/roles-slack/1.webp" />
    </Frame>

    **Option B: Use the slash command**

    Run the command inside the incident channel:

    ```
    /rootly assign
    ```

    You may also use the aliases:

    * `/rootly role`
    * `/rootly roles`

    <Frame caption="Using /rootly assign to open the modal">
            <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/roles-slack/2.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=cbee32c71f6c311ea7d6f8e96867fcfc" alt="/rootly assign" width="894" height="258" data-path="images/roles-slack/2.webp" />
    </Frame>
  </Step>

  <Step title="Assign or Remove Incident Roles">
    The modal displays every role available for this incident.\
    Each role has an associated menu or selector depending on how it was configured.

    Common actions include:

    * **Assign Myself**\
      Quickly take ownership of a role.

    * **Edit Assigned Users**\
      Add or remove specific responders.

    * **Remove Myself**\
      Step out of a role you previously held.

    <Frame caption="Editing assigned users in the Slack modal">
            <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/roles-slack/3.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=c77e4194b2070517362ce0b8172d65ed" alt="Editing roles in Slack" width="903" height="644" data-path="images/roles-slack/3.webp" />
    </Frame>

    <Info>
      If the role supports multiple assignees, you’ll see a **multi-select**.\
      If the role only allows one assignee, you’ll see a **single-select** dropdown.
    </Info>

    <Warning>
      Some roles may display a notice like:\
      **“Only users with an Incident Response seat can be assigned.”**\
      This appears when your organization enforces seat restrictions.
    </Warning>
  </Step>

  <Step title="Add Missing Roles (Optional)">
    If your team has defined incident roles that are **not yet added to this specific incident**, you’ll see an **Add Roles** banner.

    These roles must be added before responders can be assigned to them.
  </Step>

  <Step title="Save Your Changes">
    Click **Update** to apply all role assignments.\
    Rootly updates the incident immediately and posts relevant timeline entries.
  </Step>
</Steps>

***

### Best Practices

* **Assign roles early in the incident**\
  Clear ownership improves coordination and communication.

* **Use multi-assignee roles intentionally**\
  For example, an “On-call Engineer” role may allow multiple users, while “Incident Commander” should be single-assignee.

* **Review roles during major status transitions**\
  As the incident escalates, mitigation begins, or communications ramp up, ensure the right responders are assigned.

* **Use role automation where appropriate**\
  Workflows can auto-assign on-call responders, service owners, or leadership roles when an incident begins or severity increases.

* **Keep roles aligned with your process**\
  Customize roles in the web UI to match how your incident response team operates.

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="The /rootly assign command didn’t work">
    Make sure you’re running it **inside an incident channel**.\
    Running the command in DMs or non-incident channels will fail.
  </Accordion>

  <Accordion title="I can’t see the Assign Roles button">
    You may not have permission to assign incident roles.\
    Check your incident role or RBAC configuration.
  </Accordion>

  <Accordion title="Some roles don’t allow multiple people">
    Roles are configured by your team.\
    If a role only allows one user, Slack will display a single-select field.
  </Accordion>

  <Accordion title="I see a message about Incident Response seats">
    Your organization enforces seat restrictions for role holders.\
    Only users with an available seat can be assigned.
  </Accordion>

  <Accordion title="A role is missing from the Slack modal">
    The role may not be added to this incident yet.\
    Use the “Add Roles” option if available.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).