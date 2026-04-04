# Source: https://docs.rootly.com/integrations/slack/workflows/rename-slack-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename Slack Channel

## Description

This action renames the specified channel. This is particularly useful for teams that wish to keep the Slack channel name in-sync with the incident title, issue ticket number, etc.

## Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/slack/workflows/rename-slack-channel/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=3bbcb1aeabcb8609f26098da55d872fb" width="908" height="560" data-path="images/integrations/slack/workflows/rename-slack-channel/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behave.

### Channel

This field specifies which Slack channel to rename.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will rename the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be used for sub incidents and it will rename the Slack channel of the parent incident.

### New Title

Specify a new title for the incident channel. This field accepts [Liquid variables](/liquid/incident-variables) to allow you to dynamically rename the Slack channel.

For example, if this action is taken after the incident title changes; setting the field to `incident-{{ incident.started_at | date: '%Y%m%d' }}-{{ incident.title }}` will rename the Slack channel to match the updated incident title. It will still maintain the `#incident-20231119-<new-incident-title>` format.


Built with [Mintlify](https://mintlify.com).