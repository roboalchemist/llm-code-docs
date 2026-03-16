# Source: https://docs.rootly.com/integrations/slack/workflows/archive-slack-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive Slack Channel

## Description

This action automatically archives the specified channel. Keep your workspace clean by archiving unused channels will improve your overall Slack experience.

## Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/slack/workflows/archive-slack-channel/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=c6a7d1365f278dabc842a5bdae981f4f" width="899" height="432" data-path="images/integrations/slack/workflows/archive-slack-channel/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Channel

This field specifies which Slack channel to archive.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will archive the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be for sub incidents and it will archive the Slack channel of the parent incident.
* You can also archive static channel (e.g. `#general`, `#alerts`)


Built with [Mintlify](https://mintlify.com).