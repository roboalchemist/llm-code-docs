# Source: https://docs.rootly.com/incidents/managing-incidents/resolving-incidents-via-slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Resolving Incidents via Slack

> Learn how to resolve incidents directly from Slack using Rootly’s /rootly resolve command and status update modal.

### Overview

Slack allows responders to resolve incidents directly from the incident channel—no need to switch to the web interface.\
Using **`/rootly resolve`**, you can mark an incident as fully resolved, provide a short summary of the fix, and trigger any workflows your team has configured for this stage.

All actions performed in Slack are captured in the Timeline, synchronized to the web UI, and used for analytics and retrospectives.

***

### Prerequisites

Before resolving an incident through Slack:

* You must run commands **inside the incident’s Slack channel**.\
  Rootly identifies the incident by the channel ID; commands run in other channels or DMs won’t work.

* You must have permission to update incidents.\
  Organizations may restrict who can transition lifecycle states.

* Slack lifecycle commands are **not supported for scheduled incidents**.\
  Scheduled maintenance must be updated in the web interface.

<Tip>
  If `/rootly resolve` appears unresponsive, you are likely not inside an active incident channel.
</Tip>

***

### Resolving an Incident with `/rootly resolve`

<Steps>
  <Step title="Run the Resolve Command">
    In the incident’s Slack channel, type:

    **`/rootly resolve`**

    Rootly will display a confirmation dialog prompting you to provide a resolution summary and finalize the update.

    <Frame>
            <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/resolving-incidents/slack.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=345e29f2fc6f6d4fb876e24cfd8e5f8e" alt="Resolving an incident using Slack" width="821" height="552" data-path="images/resolving-incidents/slack.webp" />
    </Frame>
  </Step>

  <Step title="Provide a Resolution Summary">
    Enter a concise explanation of the final fix or corrective action.

    This summary becomes part of the permanent Timeline and is often used in:

    * Retrospectives
    * Stakeholder communications
    * Status page updates (if configured)
    * Internal reporting

    <Info>
      Clear and direct resolution notes help responders and stakeholders understand what restored service.
    </Info>
  </Step>

  <Step title="Submit to Complete the Resolution">
    Click **Submit** to finalize.

    Once submitted, Rootly will:

    * Update the incident status to **Resolved**
    * Add a Timeline entry with your resolution note
    * Trigger any configured “on-resolve” workflows
    * Update analytics timestamps
    * Automatically set a mitigation timestamp if one was never recorded
    * Sync the new status back to the web interface and API
  </Step>
</Steps>

***

### Other Ways to Resolve via Slack

If you prefer a modal-based workflow—or need to review available lifecycle states—you can also resolve an incident using the full status picker.

**Using the Status Modal**

Run:

**`/rootly status`**

This opens the incident lifecycle dialog.\
Select **Resolved**, add any optional notes, and submit.

<Info>
  Both methods—`/rootly resolve` and selecting **Resolved** inside `/rootly status`—perform the same lifecycle transition.
</Info>

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="“Nothing happens when I run /rootly resolve.”">
    * You are likely not inside the incident’s Slack channel.
    * Run the command again **inside the correct channel**, where Rootly can match the channel ID to an incident.
  </Accordion>

  <Accordion title="“You are not authorized to update this incident.”">
    You may not have sufficient role or team permissions to modify incident status.\
    Check with your Rootly administrator to confirm your permissions.
  </Accordion>

  <Accordion title="“The transition is blocked.”">
    Your workspace may enforce **required fields** before moving to Resolved.\
    The Slack modal clearly lists any fields that must be completed.
  </Accordion>

  <Accordion title="“Slack commands are disabled for this incident.”">
    Slack lifecycle commands do **not** support scheduled maintenance incidents.\
    Use the web interface to update scheduled incident lifecycle states.
  </Accordion>

  <Accordion title="“PagerDuty did not update when I resolved the incident.”">
    Rootly resolves linked PagerDuty incidents only if:

    * The incident is linked to a PagerDuty incident
    * The PagerDuty integration has **auto-resolve** enabled

    <Warning>
      Resolving an incident directly in PagerDuty does **not** update or resolve the incident in Rootly.
    </Warning>
  </Accordion>
</AccordionGroup>

***

### Best Practices

* **Add informative resolution notes.**\
  These appear in timelines, retrospectives, stakeholder notifications, and status pages.

* **Use Slack to move quickly during active response.**\
  Fast, in-channel updates help keep everyone aligned.

* **Resolve incidents through Rootly—not PagerDuty.**\
  Rootly syncs to PagerDuty, but PagerDuty does not sync back.

* **Automate repetitive actions.**\
  Use workflows to send final updates, publish status page events, initiate retrospectives, or archive Slack channels.

* **Check required fields early.**\
  Completing required information during the incident avoids blockers at resolution time.


Built with [Mintlify](https://mintlify.com).