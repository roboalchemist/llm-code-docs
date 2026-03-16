# Source: https://docs.rootly.com/integrations/slack/workflows/update-slack-channel-topic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Slack Channel Topic

# Description

This action updates the topic field of Slack channels. Channel topic is a great way to display important information upfront, so users can see them without having to scroll through the channel or look at pinned and bookmarked messages.

# Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/slack/workflows/update-slack-channel-topic/images-1.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=e533805445b1c6cb0b2033cdba4424f7" width="894" height="570" data-path="images/integrations/slack/workflows/update-slack-channel-topic/images-1.webp" />
</Frame>

## Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

## Channels

This field specifies which Slack channels to update the topic for.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will update topic for the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be used for sub incidents and it will update the topic for the Slack channel of the parent incident.
* You can also update topics for static channel (e.g. #general, #alerts)

## Topic

This field defines what the topic will be. [Incident variables](/configuration/incident-types), [Liquid syntax](https://shopify.github.io/liquid/ "Liquid syntax"), and [Slack markdown](https://api.slack.com/reference/surfaces/formatting "Slack markdown") are all supported in this field.


Built with [Mintlify](https://mintlify.com).