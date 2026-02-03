# Source: https://docs.datadoghq.com/incident_response/incident_management/investigate/timeline.md

---
title: Timeline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Investigate Incidents >
  Timeline
---

# Timeline

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/investigate/timeline/timeline_tab.fc192408f75c29e2bec10f5a32c79c7c.png?auto=format"
   alt="Example incident showing the Timeline tab" /%}

The Incident Timeline is the primary source of information for the work done during an incident. As actions are performed, new cells are added to the timeline in chronological order to capture the changes made, the person who made the change, and the time the changes were made.

By default, timeline cells are sorted in `oldest first` order, but you can change it to `newest first` using the button at the top of the timeline.

## Content types{% #content-types %}

Each cell has its own content type that indicates the kind of information the cell contains:

| Content type       | Description                                                                                                                                                                                                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Responder note     | A note manually written by an incident responder. Responder notes have the following sub-types:- *Graph*: The responder note contains one or more Datadog graphs- *Link*: The responder note contains a hyperlink- *Code*: The responder note contains text wrapped in Markdown syntax for code blocks |
| Incident update    | Any changes made to an incident's properties (including status and severity) or its impact.                                                                                                                                                                                                            |
| Integration update | Any changes made through the Incident Management product's [integrations](https://docs.datadoghq.com/incident_response/incident_management/#integrations).                                                                                                                                             |
| Task               | Any changes made to incident tasks in the Remediation section of the Incident Details page.                                                                                                                                                                                                            |
| Notification sent  | An update when a manual notification is sent by an incident responder.                                                                                                                                                                                                                                 |

### Responder notes{% #responder-notes %}

Add responder notes directly to the timeline using the text box underneath the section tabs of the Incident Details page. You can also add responder notes [to the timeline from Slack](https://docs.datadoghq.com/integrations/slack/?tab=slackapplicationus#using-datadog-incidents). You can customize the timestamp of the responder note at creation time to capture important information that was relevant at an earlier point in time in the chronological order of the timeline.

For responder notes you author, you can edit the content or timestamp, or delete the note entirely. You can also copy a link to a specific cell to share with teammates.

### Graph cells{% #graph-cells %}

Graph definitions are stored using share URLs for graphs if enabled in your [Organization Settings](https://app.datadoghq.com/organization-settings/public-sharing/settings). For 24 hours after a graph cell is added to the timeline, it has the same full interactive hover states found in Dashboards, Notebooks, and other pages. After 24 hours in the timeline, the graph is replaced with static images capturing what the graph was displaying. This is to ensure that graphs with data that has short retention have backups you can view after the live data for the graphs expires.

### Images{% #images %}

To upload an image to be hosted by Datadog, drop an image file into the text box field above the timeline. This adds the image as an individual cell in the timeline.

You can also add an image to an existing cell:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/investigate/timeline/timeline_cell_add_image.924c22e8ea72705400c5e84acc3039a9.png?auto=format"
   alt="Your image description" /%}



1. Click the pencil icon to edit a cell.
1. Click the image icon and locate the image in your file directory.
1. You can use any of the following options to upload an image to be hosted by Datadog:
   - Drop an image file into the upload area.
   - Click **Choose File** and locate the image in your file directory.
   - Paste a publicly accessible URL for the image.

## Further reading{% #further-reading %}

- [Investigate incidents](https://docs.datadoghq.com/incident_response/incident_management/investigate/)
