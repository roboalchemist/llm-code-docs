# Source: https://docs.rootly.com/incidents/incident-operations/slack-creating-a-sub-incident.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Sub-Incidents via Slack

> Learn how to create sub-incidents directly from Slack incident channels using the /rootly sub command and interactive dialog.

### Overview

Create sub-incidents directly from an incident’s Slack channel using Rootly slash commands.\
Sub-incidents help teams split large or cross-functional incidents into focused workstreams while keeping everything tied back to the parent incident.

***

### Restrictions

Sub-incident creation is only available when:

* You run the command **inside an incident channel**
* The incident is **not already a sub-incident**
* You have **permission to create incidents**
* The incident has no restrictions (e.g., cannot split a sub-incident)

If these conditions are not met, Slack will show an appropriate error.

***

### How to Create a Sub-Incident in Slack

#### 1. Run the sub-incident command

In the parent incident channel, type **any** of the following:

```
/rootly sub
/rootly split
/rootly fork
/rootly swimlane
```

These commands all trigger the **Create Sub-Incident** dialog.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/creating-sub-incident/slack-1.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=6147f9d0e1dc06c61a10396c120a70d0" alt="Sub-incident Slack dialog" width="907" height="1094" data-path="images/creating-sub-incident/slack-1.webp" />
</Frame>

***

#### 2. Complete the creation dialog

Fill in the incident fields as you normally would.\
Rootly automatically links the new incident as a **sub-incident** of the channel you ran the command from.

After submitting, Slack will confirm that the sub-incident has been created:

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/creating-sub-incident/slack-2.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=066ba94a7375cbcbf43a732aacbf60d1" alt="Sub-incident created confirmation" width="898" height="438" data-path="images/creating-sub-incident/slack-2.webp" />
</Frame>

You’ll then see a reference to the new sub-incident in the parent incident’s summary, Slack channel, and web interface.

***

### What Happens Behind the Scenes

Rootly automatically:

* Sets the new incident’s **parent\_incident\_id**
* Assigns a sub-incident kind (e.g., `normal_sub`, `scheduled_sub`)
* Attributes the creation to **Slack**
* Optionally creates a **Slack channel** for the sub-incident (team settings apply)
* Triggers any workflows conditioned on\
  `Kind → is one of → normal_sub / scheduled_sub / test_sub`

<Info>
  Sub-incidents created via Slack behave exactly the same as those created in the Web UI.\
  They inherit parent properties depending on your workspace configuration and feature flags.
</Info>

***

### Demo

<iframe width="100%" height="420" src="https://www.loom.com/embed/29cda58cf37646b1a5cea28d3b8901d7" frameborder="0" allowfullscreen />

***

### Best Practices

* **Use sub-incidents to divide ownership** across SRE, Security, Networking, or other teams.
* **Keep the parent incident customer-facing** while sub-incidents track internal or deep-dive workstreams.
* **Use workflows to automate structure**, such as creating roles or tasks for each new sub-incident.
* **Name sub-incidents clearly** to reflect their specific investigative track.
* Avoid splitting unless the scope is meaningfully distinct—small tasks are usually better captured as action items.

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="“This command can only be used in an incident channel”">
    Slack restricts `/rootly sub` to **incident channels only**.\
    Run the command inside the relevant incident channel.
  </Accordion>

  <Accordion title="“Cannot split a sub-incident”">
    Sub-incidents cannot be split further.\
    Create sub-incidents **from parent incidents only**.
  </Accordion>

  <Accordion title="“Not authorized to create incidents”">
    Your role does not have permission to create incidents.\
    Contact your Rootly admin to update your permissions.
  </Accordion>

  <Accordion title="Nothing happens after submitting the dialog">
    This may occur if:

    * Required fields were left blank
    * Your Slack integration is temporarily disconnected
    * Your team has restricted sub-incident creation via feature flags
  </Accordion>

  <Accordion title="The sub-incident doesn’t show in the parent incident UI">
    Ensure that:

    * The originating channel was the correct **parent incident channel**
    * The parent incident is not archived or cancelled
    * The sub-incident was created successfully (Slack will show a confirmation)
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).