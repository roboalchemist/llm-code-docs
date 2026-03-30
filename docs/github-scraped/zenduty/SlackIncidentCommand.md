---
id: SlackIncidentCommand
title: Slack - Incident Command Integration
---

The Slack Incident Command integration lets you send real-time incident alerts to a Slack channel. To integrate Slack Webhook Outgoing with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Slack Incident Command integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Outgoing Integrations" and then "Add New Integration". Give it a name and select the application "Slack Incident Command" from the dropdown menu.

4. Go to "Configure" under your integrations and click on the **Connect with Slack** button. Authenticate your Slack account. You will be redirected back to your Zenduty integrations page.

5. To setup your incident command, you have two options - Single Channel or Multichannel.

6. In the single channel configuration, you can select an existing channel and all incidents and updates will be sent that channel.

7. In the multichannel configuration, Zenduty will create a new channel for every incident that is created. Enter the **Channel Name Prefix** value. For example, if you choose the prefex as "incident_", then an incident with number 123 will create a Slack channel named #incident_123. In the **Archive channel when incident is resolved?** section, you can say **yes** or **no** if you'd like to archive the channel after the incident is resolved. Whenever a new incident channel is created, all the on-call engineers, responders, roles and task addignees will be automatically added to the channel.

8. Click on **Save** to save the integration.

Your Slack Incident Command integration is now setup!
