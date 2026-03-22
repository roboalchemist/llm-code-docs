# Source: https://docs.rootly.com/incidents/creating-incidents/converting-existing-slack-channels-to-incidents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Converting Existing Slack Channels to Incidents

> A step-by-step guide to converting an existing Slack channel into a Rootly incident channel without losing message history, members, or context.

### Overview

If your team begins investigating an issue in Slack before formally declaring an incident, you can convert that existing conversation into a Rootly incident channel.\
This ensures:

* No message history is lost
* All responders stay in the same channel
* Automated timelines, workflows, and notifications still run
* The incident is created with full context from the existing discussion

The `/incident convert` command transforms any standard Slack channel into a full Rootly incident channel.

### Convert an Existing Slack Channel

<Steps>
  <Step title="Run the Convert Command">
    In the Slack channel you want to convert, type:

    ```
    /incident convert
    ```

    Then press **Enter**.

    This opens the **Convert to Incident** modal.

    <Frame>
            <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/convert-incidents-slack-1.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=024d4e938ea35dd560b3eba0c451073f" alt="Convert Incidents Slack 1 Web" width="897" height="273" data-path="images/incidents/convert-incidents-slack-1.webp" />
    </Frame>

    <Tip>
      You must run the command inside the channel you want to convert — it cannot be used from other channels or DMs.
    </Tip>
  </Step>

  <Step title="Fill Out the Incident Details">
    The modal includes the same configurable fields you see when creating a new incident:

    * **Title**
    * **Summary**
    * **Severity**
    * **Incident Type**
    * **Private Incident (optional)**
    * Any custom fields your workspace has configured

    <Frame>
            <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/convert-incidents-slack-2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=da78d238292082c23bd6bfe34d838f06" alt="Convert Incidents Slack 2 Web" width="893" height="1031" data-path="images/incidents/convert-incidents-slack-2.webp" />
    </Frame>
  </Step>
</Steps>

### What Happens After Conversion

Once submitted, Rootly will:

* Create a new incident in the Rootly platform
* Link the Slack channel to the incident
* Preserve **all** prior messages in the channel
* Generate initial timeline entries
* Trigger any incident-creation workflows
* Assign default roles or responders (if configured)
* Enable Slack commands such as `/rootly status`, `/rootly resolve`, etc.

From here, the channel behaves like any other incident channel created through Slack or the Web UI.

<Check>
  Conversion never deletes or archives the channel — all previous activity remains intact.
</Check>

### When to Use Conversion

Use `/incident convert` when:

* Responders start troubleshooting informally in Slack
* An issue escalates from a conversation into a true incident
* You want to preserve all investigative context without creating a new channel
* You want workflows, timelines, and notifications to begin after discussion has already started

### Troubleshooting

<AccordionGroup>
  <Accordion title="“The command didn’t work.”">
    Ensure:

    * You ran `/incident convert` **inside the Slack channel** to be converted
    * The Rootly Slack app has permission to access that channel
    * You are a user with permission to create incidents
  </Accordion>

  <Accordion title="“A required field is missing.”">
    Your workspace may enforce creation requirements.\
    Open **Configuration → Forms** to confirm what fields must be included.
  </Accordion>

  <Accordion title="“The channel didn’t become an incident channel.”">
    Confirm Slack channel conversions are enabled in your Rootly Slack Integration settings.
  </Accordion>
</AccordionGroup>

### Best Practices

* Convert as soon as a conversation becomes operational or time-sensitive
* Provide a clear incident title and summary to help responders ramp quickly
* Use severity to trigger correct workflows and escalation
* Avoid converting channels that contain unrelated historical content
* Use private incidents when the discussion involves sensitive data


Built with [Mintlify](https://mintlify.com).