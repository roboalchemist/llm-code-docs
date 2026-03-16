# Source: https://docs.rootly.com/integrations/slack/workflows/create-slack-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Slack Channel

## Description

This action creates a designated Slack channel for an incident. Responding to each incident in their designated Slack channel can greatly help teams keep things organized.

## Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/slack/workflows/create-slack-channel/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=531dddca1c1e8691627cbea016d855d4" width="903" height="607" data-path="images/integrations/slack/workflows/create-slack-channel/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Workspace

Select the workspace from the dropdown. The channel will be created into the specified workspace.

### Title

Specify a title for the incident channel. This field accepts [Liquid variables](/liquid/incident-variables) to allow you to dynamically name the Slack channel.

**Example**

Setting the field to `incident-{{ incident.created_at | date: '%Y%m%d' }}-{{ incident.title }}` will create a Slack channel with the name `#incident-20231119-<incident-title>`.

### Private

The value selected in the field will determine whether if the incident channel is created as a public or private channel.

* Selecting `auto` will result in public channels being created for non-private incidents and private channels being created for private incidents.
* Selecting `true` will result in private channels being created for both non-private and private incidents.
* Selecting `false` will result in public channels being created for both non-private and private incidents.


Built with [Mintlify](https://mintlify.com).