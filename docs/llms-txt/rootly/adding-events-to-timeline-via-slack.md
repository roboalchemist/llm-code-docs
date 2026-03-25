# Source: https://docs.rootly.com/incidents/incident-timeline/adding-events-to-timeline-via-slack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Events to Timeline via Slack

> Learn how to add timeline events from Slack using the /rootly timeline command, message actions, or emoji reactions.

### Overview

Slack is one of the fastest ways to record timeline events during an incident.\
Rootly supports multiple Slack-based methods so responders can capture actions, observations, and decisions without leaving the incident channel.

You can add events using:

* The `/rootly timeline` slash command
* Message actions (the Slack **hamburger menu**)
* Configurable **pin or emoji reactions**

All Slack-created events appear instantly in the incident timeline.

***

### Methods for Adding Timeline Events

<Steps>
  <Step title="Use the /rootly timeline command">
    In the incident Slack channel, type:

    **`/rootly timeline <event>`**

    This opens the Add Event modal pre-filled with your text, allowing you to set visibility and optional details before submitting.
  </Step>

  <Step title="Use the message action (hamburger menu)">
    You can capture any message directly into the timeline:

    1. Hover over a message
    2. Click the **hamburger icon**
    3. Select **Add event**

    <Frame>
            <img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/adding-events/slack-1.webp?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=9ec67a82fceff0d0999ad744b79bdf65" alt="Adding an event using Slack" width="908" height="353" data-path="images/adding-events/slack-1.webp" />
    </Frame>

    The modal will auto-fill the message content and attach a permalink back to Slack.
  </Step>

  <Step title="Use pin or emoji reactions">
    Rootly can automatically create timeline entries whenever specific reactions are added to a message.

    * **Pin reactions** (📌)
    * **Any custom emoji** your team configures for timeline ingestion

    <Frame>
            <img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/adding-events/slack-2.webp?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=99882bc7946651b783f218194e6de61f" alt="Using the pin emoji to add an event" width="897" height="233" data-path="images/adding-events/slack-2.webp" />
    </Frame>

    You can configure which emoji should create events in **Slack Integration Settings**.
  </Step>
</Steps>

***

### How Slack-Captured Events Behave

* Events created from a command or message action open a modal so you can review details
* Events created from pin/emoji reactions are added automatically — *no modal*
* Reaction-based events use the **original Slack message timestamp** as the event’s `occurred_at` value
* All entries include a Slack permalink and optional user-attribution
* Deduplication prevents duplicate events from repeat reactions

<Info>
  Emoji triggers, follow-up creation, and task creation each use separate emoji lists and **cannot overlap**. Configure them in *Integrations → Slack*.
</Info>

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="The slash command didn’t open the modal">
    Make sure you ran the command **inside the incident channel**.\
    Running it anywhere else will result in a non-incident error.
  </Accordion>

  <Accordion title="My emoji reaction didn’t create a timeline event">
    Verify that:

    * Emoji ingestion is enabled
    * The emoji is included in the **Add to Timeline** emoji list
    * You are in a recognized incident channel
  </Accordion>

  <Accordion title="The event timestamp looks wrong">
    For emoji/pin reactions, occurred\_at is taken from the **Slack message timestamp**, not the moment you reacted.
  </Accordion>

  <Accordion title="A message action option isn’t appearing">
    You may not have permission to update the incident timeline, especially for private incidents.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).