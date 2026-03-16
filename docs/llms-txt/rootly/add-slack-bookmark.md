# Source: https://docs.rootly.com/integrations/slack/workflows/add-slack-bookmark.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Slack Bookmark

## Description

This action adds a bookmark to a specified Slack channel. Bookmarks are particularly useful for keeping track of important links. Links that are bookmarked will appear at the top of your channels.

## Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/slack/workflows/add-slack-bookmark/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=dc019812863898089cc72483722a87b1" width="1411" height="1316" data-path="images/integrations/slack/workflows/add-slack-bookmark/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Channel

This field specifies which Slack channel to add the bookmark in.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will set the bookmark in the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be used for sub incidents and it will set the bookmark in the Slack channel of the parent incident.
* You can also set the bookmark in other static channel (e.g. `#general`, `#alerts`)

### Playbook

Selecting a playbook in this field will attach the link to the playbook as a bookmark in the specified channel.

### Title

This field will be the text that gets displayed in the bookmarkbar of the Slack channel.

### Link

Use this field to specify the URL for the bookmark. You can either input a hardcoded link or use Liquid variables to dynamically set a link.

Some common examples:

* `{{ incident.url }}`
* `{{ incident.jira_issue_url }}`
* `{{ incident.pagerduty_incident_url }}`

<Tip>
  TIP: You can use the [Incident Variable Explorer](https://rootly.com/account/help/liquid-explorer) to test out what value each liquid variable returns.
</Tip>

### Emoji

An emoji can be attached to each bookmark to help with visual identification.

All Slack emojis are supported. You can view a complete list of them [here](https://www.webfx.com/tools/emoji-cheat-sheet/).


Built with [Mintlify](https://mintlify.com).