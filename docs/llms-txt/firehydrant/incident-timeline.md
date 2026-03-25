# Source: https://docs.firehydrant.com/docs/incident-timeline.md

# Incident Timeline

<Image alt="The Incident Timeline in Command Center" align="center" width="650px" src="https://files.readme.io/c9326d0-Screenshot_2023-12-01_at_10.10.56_AM.png">
  The Incident Timeline in Command Center
</Image>

As you work through incidents, a common pain point is tracking what happens and when.

This often means teams will have a "scribe" or "note taker" who follows along and manually notes the events of the incident. Or, more painstakingly, someone must manually comb through chat channels, transcripts, or other documents to cobble together the timeline after the incident.

With FireHydrant, all events that unfold during an incident—such as Runbook steps execution, user actions, task completions, chat messages, and more—are automatically recorded in the timeline.

This feature liberates team members from the stress of manual event tracking, allowing them to focus on resolving the incident.

## Using the Timeline

You don't need to do anything other than set up the initial integrations with your chat provider(s) and use a Runbook step to create an incident channel. FireHydrant will scribe messages from the incident channels it creates.

* **Slack**
  * [Slack Setup](https://docs.firehydrant.com/docs/slack-integration)
  * [Create or rename Incident Slack channel](https://docs.firehydrant.com/docs/runbook-step-create-or-rename-incident-slack-channel)
* **Microsoft Teams**
  * [Microsoft Teams Setup](https://docs.firehydrant.com/docs/microsoft-teams-integration)
  * [Create Microsoft Teams Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-microsoft-teams-incident-channel)

As mentioned above, all events and actions in FireHydrant, including messages, images, and actions from your chat application, are logged automatically.

### Adding other messages to timeline

Any messages in the primary incident channel are automatically tracked, as mentioned above. However, if you have other messages from other channels, you can add them manually via message actions (available in Slack).

Next to any message, click the ellipses and find the action to add the message to the incident. This will open a modal  for you to choose which incident to add the message to, and if there are messages in the thread, also a checkbox to optionally include all the threaded messages too.

<Image alt="Adding a message and/or thread to an incident in Slack" align="center" width="640px" src="https://files.readme.io/c447febdaf877481d51e22d1f015180f78500e9ecd17c1ea702df27a22ff0d58-CleanShot_2025-03-24_at_15.04.132x.png">
  Adding a message and/or thread to an incident in Slack
</Image>

### File uploads

Messages posted into incident channels are automatically scribed to the FireHydrant timeline. This includes numerous file types uploaded:

* **Images**
  * `image/apng`
  * `image/bmp`
  * `image/gif`
  * `image/jpeg`
  * `image/pjpeg`
  * `image/png`
  * `image/svg+xml`
  * `image/tiff`
  * `image/webp`
  * `image/x-icon`
* **Other File Types**
  * `application/zip`
  * `application/pdf`
  * `application/msword`
  * `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
  * `application/vnd.ms-excel`
  * `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
  * `application/vnd.ms-powerpoint`
  * `application/vnd.openxmlformats-officedocument.presentationml.presentation`
  * `application/rtf`
  * `text/csv`
  * `text/plain`

### Filtering the timeline and Saved Views

The timeline can be filtered to specific events. You can also save these filters as **Saved Views**, enabling more accessible selection and filtering when revisiting this incident and other incidents. This also includes setting certain views or filters as default for all of your incidents.

<Image alt="Filtering events and saving custom views/filters" align="center" width="650px" src="https://files.readme.io/895c3c8-CleanShot_2024-08-09_at_15.49.02.png">
  Filtering events and saving custom views/filters
</Image>

Certain types of timeline events, such as messages posted directly in the UI, allow users to edit or copy the message. These action buttons are on the right side next to the star.

<Image alt="Message with copy and edit buttons" align="center" width="650px" src="https://files.readme.io/bda8a92-image.png">
  Message with copy and edit buttons
</Image>

### Starring Events

You can **Star** events from both your chat app and the app UI. Starring an event marks it as "important" and allows you to comment on it, and it also becomes a primary highlight during the [Retrospective phase](https://docs.firehydrant.com/docs/conducting-retrospectives) of an incident.

<Image alt="An example Retrospective page with starred events" align="center" width="650px" src="https://files.readme.io/f13d038-Screenshot_2023-12-01_at_10.16.13_AM.png">
  An example Retrospective page with starred events
</Image>

In Slack, events can be starred by reacting to a message in the incident channel with a Star emoji. The Slack integration settings allow you to change this emoji.

<Image alt="Starring a message in Slack" align="center" width="400px" src="https://files.readme.io/5d16b8c3d947d23f852ca71d67f924f9ae45356951cee655434aed2cd2a49b0b-CleanShot_2024-08-22_at_14.23.57.png">
  Starring a message in Slack
</Image>

In Microsoft Teams, a message can be starred by selecting the contextual action in the dropdown next to each message.

<Image alt="Starring a message in MS Teams" align="center" width="400px" src="https://files.readme.io/c5ad13c8d3cd125ea022265e35b016d3107ffa860b424fcac32036a76344e392-CleanShot_2024-08-22_at_14.27.06.png">
  Starring a message in MS Teams
</Image>

### Exporting the timeline

<Image align="center" width="650px" src="https://files.readme.io/2165e8abf1b2d7c758d65318ac3c4ae14a5871ac9d4df610635d6f6eb734b1c3-CleanShot_2025-01-09_at_11.04.052x.png" />

The timeline can be exported in CSV format from the [The Command Center](https://docs.firehydrant.com/docs/the-command-center). When exporting, all timeline events  will be exported, and the CSV will be organized in the following columns:

| Column          | Description                                                                                                                                                         |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Timestamp**   | ISO 8601 format timestamp of when the timeline event occurred                                                                                                       |
| **Event Type**  | Slug for the type of event. For available values and their definitions, see [List events for an incident](https://docs.firehydrant.com/reference/listincidentevents).                                  |
| **Author Type** | Any one of `patchy`, `firehydrant_user`, or `[integration_slug]` where the slug will vary based on which integration acted (e.g., `pagerduty`, `jira_cloud`, etc.). |
| **Name**        | Usually `FireHydrant`, the name of the user, or the name of the integration                                                                                         |
| **Email**       | Only populated with the user's email address if the **Author Type** is `firehydrant_user`, otherwise empty                                                          |
| **Summary**     | The actual timeline message or summary of the event that occurred                                                                                                   |

## Next Steps

Now that you know everything is tracked automatically by FireHydrant, check out more of what FireHydrant has to offer:

* [Adding Responders](https://docs.firehydrant.com/docs/adding-responders)
* [Posting Updates](https://docs.firehydrant.com/docs/posting-updates)
* [Managing Tasks](https://docs.firehydrant.com/docs/managing-tasks)
* [Slack Responder Guide](https://docs.firehydrant.com/docs/slack-responder-guide)
* [UI Responder Guide](https://docs.firehydrant.com/docs/ui-responder-guide)