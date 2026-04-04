# Integrations Guide

::: {.toctree maxdepth="1" hidden="" titlesonly=""}
plugins webhook-integrations slash-commands restful-api
no-code-automation faq
:::

Mattermost provides a variety of methods to integrate with your favorite
tools, automate critical workflows, and extend the capabilities of the
platform. This guide provides a high-level overview of integration
options and the level of technical skills required
`(no-code, low-code, or pro-code) <integrations-guide/faq:what is meant by no-code, low-code, and pro-code?>`{.interpreted-text
role="ref"}, and links to detailed documentation for each.

## Choose Your Path

+-----------------------------------------+----------------------------------------------+-------------------------------+
| Skill Level                             | Best Options                                 | Examples                      |
+=========================================+==============================================+===============================+
| `No-code <no-code>`{.interpreted-text   | - [Pre-built plugins](#pre-built-plugins)    | - Connect Jira, GitHub, Zoom  |
| role="ref"}                             | - [Built-in slash                            | - Command line interactions   |
|                                         |   commands](#built-in-slash-commands)        | - Automate with n8n, Zapier   |
|                                         | - [No-code                                   | - Run incident playbooks      |
|                                         |   automation](#no-code-automation-platforms) |                               |
|                                         | - [Playbooks](#mattermost-playbooks)         |                               |
+-----------------------------------------+----------------------------------------------+-------------------------------+
| `Low-code <low-code>`{.interpreted-text | - [Webhooks](#webhooks)                      | - Send monitoring alerts      |
| role="ref"}                             | - [Custom slash                              | - Trigger actions with        |
|                                         |   commands](#custom-slash-commands)          |   keywords                    |
+-----------------------------------------+----------------------------------------------+-------------------------------+
| `Pro-code <pro-code>`{.interpreted-text | - [REST API](#restful-api)                   | - Build custom apps           |
| role="ref"}                             | - [Custom plugins](#custom-built-plugins)    | - Extend Mattermost core      |
+-----------------------------------------+----------------------------------------------+-------------------------------+

## Integration Options

### Plugins

Learn more about
`Mattermost plugins </integrations-guide/plugins>`{.interpreted-text
role="doc"}.

#### Pre-Built Plugins

**Technical complexity:** `No-code <no-code>`{.interpreted-text
role="ref"}

Mattermost provides a set of
`pre-built plugins </integrations-guide/popular-integrations>`{.interpreted-text
role="doc"} that require no coding to install, configure, and use. These
plugins are installed and managed entirely through the System Console,
where you can enable, configure, and customize settings without any
development work.

![Pre-built plugins available for no-code integration](../images/prebuilt-integrations.png){width="800px"}

#### Custom-Built Plugins

**Technical complexity:** `Pro-code <pro-code>`{.interpreted-text
role="ref"}

`Building custom plugins <integrations-guide/plugins:custom-built plugins>`{.interpreted-text
role="ref"} are the most comprehensive way to add new features and
customization to self-hosted Mattermost deployments. Custom plugins are
ideal for customers wanting to change the behavior of the Mattermost
server, desktop, and web apps without forking the core codebase to suit
their organization's needs.

Building a custom plugin is a **software development** task, using `Go`
for the server-side functionality and optionally `TypeScript/React` for
UI components.

### Webhooks

Learn more about
`Mattermost webhooks </integrations-guide/webhook-integrations>`{.interpreted-text
role="doc"}.

#### Incoming Webhooks

**Technical complexity:** `No-code <no-code>`{.interpreted-text
role="ref"}

`Incoming webhooks </integrations-guide/incoming-webhooks>`{.interpreted-text
role="doc"} allow external applications to post messages into Mattermost
channels and direct messages. They are a simple way to receive
notifications and data from other services in real-time and require only
basic setup.

Additionally, Mattermost webhook payloads are
`fully compatible <integrations-guide/incoming-webhooks:slack compatibility>`{.interpreted-text
role="ref"} with Slack's webhook format to make migration easier.

#### Outgoing Webhooks

**Technical complexity:** `Low-code <low-code>`{.interpreted-text
role="ref"}

`Outgoing webhooks </integrations-guide/outgoing-webhooks>`{.interpreted-text
role="doc"} allow Mattermost to send messages and trigger actions in
external applications when specific keywords are typed in channels. They
are a straightforward way to connect Mattermost conversations to other
services and automate responses. Outgoing webhooks require no coding to
configure in Mattermost. Some light coding is required to parse the
request from the external service and format a JSON response payload.

### Slash Commands

Learn more about
`Mattermost slash commands </integrations-guide/slash-commands>`{.interpreted-text
role="doc"}.

#### Built-In Slash Commands

**Technical complexity:** `No-code <no-code>`{.interpreted-text
role="ref"}

Out-of-the-box
`built-in slash commands </integrations-guide/built-in-slash-commands>`{.interpreted-text
role="doc"} enable command line interaction with users, channels, and
conversations.

#### Custom Slash Commands

**Technical complexity:** `Low-code <low-code>`{.interpreted-text
role="ref"}

You can create
`custom slash commands <integrations-guide/slash-commands:custom slash commands>`{.interpreted-text
role="ref"} that run preconfigured commands that can return a response,
such as plain text, rich message content, interactive buttons or forms,
directly into a channel.

Mattermost\'s slash command format is Slack compatible, so you can
easily migrate your commands from Slack.

### RESTful API

**Technical complexity:** `Pro-code <pro-code>`{.interpreted-text
role="ref"}

With
`Mattermost's RESTful API </integrations-guide/restful-api>`{.interpreted-text
role="doc"}, you have full developer control for automation, bots, and
integrations.

## Build and Automate Workflows

**Technical complexity:** `No-code <no-code>`{.interpreted-text
role="ref"}

In addition to direct tool integrations, Mattermost can be part of
larger automated workflows across your integrated services. Automate
multi-step processes across Mattermost and other systems, often with no
coding required.

### No-code Automation Platforms

Platforms like n8n, Zapier, and Make provide powerful visual editors
that support thousands of connected tools, with triggers and actions
that integrate Mattermost to external services, enabling teams to build
complex workflows without writing code. Admins migrating from tools like
Slack Workflow Builder can recreate familiar automations in Mattermost
using these platforms.

Learn more about additional
`no-code automation options </integrations-guide/no-code-automation>`{.interpreted-text
role="doc"} available in Mattermost.

### Mattermost Playbooks

`Mattermost Playbooks </end-user-guide/workflow-automation>`{.interpreted-text
role="doc"} lets you define and execute repeatable processes without any
coding. Playbooks are often used for incident response, onboarding
checklists, or any workflow that involves multiple steps, owners, and
notifications. Playbooks have integration points you can use to trigger
actions, and they can work in conjunction with plugins, making them a
powerful no-code automation tool for orchestrating both human and system
actions.

Learn more about using
`Playbooks </end-user-guide/workflow-automation>`{.interpreted-text
role="doc"}.

## Frequently Asked Questions

Have questions about coding levels, Slack compatibility, or setup
options? Visit the
`Integrations FAQ </integrations-guide/faq>`{.interpreted-text
role="doc"}.
