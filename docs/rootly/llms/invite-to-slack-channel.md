# Source: https://docs.rootly.com/integrations/slack/workflows/invite-to-slack-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Invite To Slack Channel

## Description

This action invites Slack users and user groups into the specified Slack channel.

## Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/slack/workflows/invite-to-slack-channel/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=4145028990f8959b7c83d3d7bb116af2" width="893" height="594" data-path="images/integrations/slack/workflows/invite-to-slack-channel/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Channel

This field specifies which Slack channel to invite the user(s)/user group(s) to.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will invite the user(s)/user group(s) to the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be used for sub incidents and it will invite the user(s)/user group(s) to the Slack channel of the parent incident.
* You can also invite user(s)/user group(s) to static channel (e.g. `#general`, `#alerts`)

### Slack Users

This field sets the user(s) you wish to invite to the specified channel. User(s) can either be hard-coded to specific persons within your team or set dynamically via Liquid variables. For example, you can use the syntax `{{ incident.creator }}` to invite the person who originally declared the incident.

Slack User Groups

This field sets the Slack user group(s) you wish to invite to the specified channel. All users part of the specified user group will be invited. You can read more about Slack user groups [here](https://slack.com/help/articles/212906697-Create-a-user-group).


Built with [Mintlify](https://mintlify.com).