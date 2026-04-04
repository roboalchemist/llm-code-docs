# Source: https://docs.rootly.com/integrations/slack/smart-defaults.md

# Source: https://docs.rootly.com/integrations/pagerduty/smart-defaults.md

# Source: https://docs.rootly.com/integrations/jira/smart-defaults.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Defaults

## Overview

Traditionally, Rootly has strictly relied on [workflow](/integrations/slack/workflows " workflow") configurations to automate Jira actions. While it offered the flexibility required to meet complex incident response procedures, it did require some initial effort to set up. Understanding that not all customers adopt super complex procedures, we've introduced Smart Defaults to our Jira integration to help simplify the configuration process.

New customers on Rootly will have Smart Defaults automatically turned on as soon as they install Jira. They will be able to interact with Jira out-of-box!

Existing customers will have Smart Defaults turned off to avoid interrupting the workflows that have already been set up.

To get started with Jira Smart Defaults, you'll want to first navigate to **Integrations > Jira (Configuration)**.

## Webhook

This URL is used to set up your Jira webhook. Please see [Setting Up Jira Webhook](/integrations/jira/installation) for detailed steps.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/jira/smart-defaults/images-1.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=e06a86812b2560a4e896fe22ac50d9dc" width="1786" height="499" data-path="images/integrations/jira/smart-defaults/images-1.webp" />
</Frame>

## Jira Ticket for Incidents

This section is for configuring the creation of Jira tickets from Rootly.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/jira/smart-defaults/images-2.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=4ef9763dc0efedf39ea0c09bb645e6d0" width="916" height="1029" data-path="images/integrations/jira/smart-defaults/images-2.webp" />
</Frame>

### Create Jira ticket for all new incidents

This flag will allow Rootly to automatically create a Jira ticket into the specified project as soon as an incident is declared on Rootly.

### Project Key

This field allows you to select which project to create the Jira ticket into. If you need to create Jira tickets to different projects, you can disable this and configure through [workflows](/integrations/jira/rootly-to-jira-sync "workflows").

### Issue Type

This field allows you to select an issue type for your Jira ticket. The options are pulled directly from the project you've specified in the previous `Project Key` field.

### Issue Status

This field allows you to select the status to create the ticket into.The options are pulled directly from the project and issue type you've specified in the previous `Project Key` and `Issue Type` fields.

### Title / Summary

This field allows you to define the `Summary` field of your Jira ticket. By default it is set to `{{ incident.title }}` to match the title of your incident. This field supports Liquid syntax.

### Description

This field allows you to define the Description field of your Jira ticket. By default it is set to `{{ incident.summary }}` to match the summary of your incident. This field supports Liquid syntax.

### Default Assignee

This flag allows you to assign the Jira ticket to someone by providing an email address. If no email address is provided, the ticket will be assigned to the creator of the incident. This field supports Liquid syntax.

### Auto-bookmark Jira ticket in Slack

This flag allows you to enable automatic creation of a bookmark to the Jira ticket in the incident Slack channel. Slack’s channel bookmarks let you save and highlight your most important information in a project, letting you quickly find and interact with key information.

### Update Jira ticket when incident is updated

This flag allows you to enable automatic update of the matching Jira ticket whenever an incident is updated. This is a one-way update, meaning only updates from incidents flow into Jira and not the other way around.

## Jira Ticket For Action Items

This section is for configuring the creation of Jira subtasks for action items created on Rootly.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/jira/smart-defaults/images-3.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=59c132abe62b98706c63ee8e1051bf08" width="1742" height="946" data-path="images/integrations/jira/smart-defaults/images-3.webp" />
</Frame>

### Create Jira subtask ticket for action items

This flag will allow Rootly to automatically create a Jira subtask under the parent Jira ticket every time a new action item is created in Rootly.

### Subtask Type

<Warning>
  Please leave this field blank, as Jira subtasks can only be one type. This field will be used in the future to expand task creation to parent ticket-level types.
</Warning>

### Subtask Status

This field allows you to select the status to create the subtask into.The options are pulled directly from the project specified in the previous `Project Key` field.

### Update Jira subtask ticket for action items

This flag allows you to enable automatic update of the matching Jira sub-task whenever an action item is updated. This is a one-way update, meaning only updates from incidents flow into Jira and not the other way around.


Built with [Mintlify](https://mintlify.com).