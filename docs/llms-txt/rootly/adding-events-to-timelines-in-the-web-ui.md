# Source: https://docs.rootly.com/incidents/incident-timeline/adding-events-to-timelines-in-the-web-ui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Events to Timeline via Web Interface

> Learn how to add timeline events directly from the Rootly web interface with markdown support for event descriptions.

### Overview

The Web interface provides the most structured and controlled way to add timeline events to an incident. It supports rich text formatting, attachments, timestamps, and granular visibility settings—making it ideal for adding clear, polished, retrospective-ready updates.

Events added through the Web UI are treated the same as those created via Slack, email, or API, and appear immediately in the incident’s chronological timeline.

***

### Adding a Timeline Event in the Web UI

<Steps>
  <Step title="Open the Incident">
    Navigate to the incident you want to update and scroll to the **Timeline** section.
  </Step>

  <Step title="Click “Add event”">
    Click the **Add event** button at the top of the timeline to open the event creation modal.

    <Frame>
            <img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/adding-events/web.webp?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=606c4b1b586e64fedb8511166667b5a0" alt="Adding an event to a timeline" width="894" height="303" data-path="images/adding-events/web.webp" />
    </Frame>
  </Step>

  <Step title="Write Your Event Description">
    Enter the text you want recorded as a timeline event.

    Your description supports **Markdown formatting**, allowing you to add emphasis, structure, and links.\
    This is especially helpful when summarizing findings, outlining hypotheses, or highlighting important decisions.

    [Markdown](https://www.markdownguide.org/) syntax is supported in your event description.
  </Step>

  <Step title="Configure Optional Details">
    You can optionally customize:

    * **Occurred At** — set an exact timestamp or backfill earlier events
    * **Attachments** — upload logs, screenshots, or supporting documents

    These fields help maintain an accurate and high-quality incident timeline.
  </Step>

  <Step title="Save the Event">
    Click **Create event** to publish your entry to the timeline.\
    It will appear in chronological order based on the timestamp you provided.
  </Step>
</Steps>

***

### Tips for Creating Useful Timeline Entries

* Use Markdown to structure your updates for readability
* Write concise, factual observations and decisions
* Attach files instead of pasting long logs
* Record the *why* behind actions when possible
* Use accurate timestamps when reconstructing events

<Info>
  Well-written timeline entries significantly accelerate retrospective creation and help future responders understand what happened.
</Info>

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="My event is appearing in the wrong order">
    Check the **Occurred At** field.\
    If left blank, Rootly uses the time you created the event.
  </Accordion>

  <Accordion title="My event isn’t showing on the public/external timeline">
    Make sure visibility is set to **External**, not Internal.
  </Accordion>

  <Accordion title="I can’t see the Add event button">
    You may not have permissions to update incidents or timeline entries.
  </Accordion>

  <Accordion title="Attachments won’t upload">
    Ensure the file type and size comply with your workspace’s attachment rules.
  </Accordion>
</AccordionGroup>

***

### Best Practices

* Keep entries focused and easy to scan
* Include decisions, not just actions
* Backdate events thoughtfully to maintain timeline accuracy
* Use Markdown headings, lists, and code formatting where helpful
* Add context such as impacted services or related systems


Built with [Mintlify](https://mintlify.com).