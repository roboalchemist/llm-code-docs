# Source: https://docs.firehydrant.com/docs/create-microsoft-teams-group-chat.md

# Create Microsoft Teams Group Chat

Organize your incident communication using Microsoft Teams group chats. Using our Runbook Step, you can automatically create a new Teams group chat, based on any conditions you have set.. This feature offers key advantages over traditional Teams channels by providing greater flexibility in managing incident participants. Group chats allow you to quickly add or remove team members as the incident evolves, streamlining your response process. If your organization needs faster collaboration setup, wants to reduce channel clutter, or requires dynamic participant management, group chats are an excellent alternative.

## Configuring the step

<Image alt="&#x22;Create Microsoft Teams incident group chat&#x22; step" align="center" width="650px" src="https://files.readme.io/7ebdaf40339384348a58b3c126817eaf33810415d5417d05d638782dcdedc4f4-CleanShot_2025-01-22_at_14.21.412x.png">
  "Create Microsoft Teams incident group chat" step
</Image>

This step comes with the following configurable fields:

* **Name** - A configurable name for the step. This shows up in the Runbook details tab for each incident and has no impact on actual execution
* **Group chat name format** - The name/format for the group chat being created. It supports [Template Variables](https://docs.firehydrant.com/docs/template-variables) and [Markdown](https://docs.firehydrant.com/docs/markdown-support).
  * **Note:** If the chat name references variables like `severity` or `priority`, changes to these parameters during the incident will also change the name of the chat.
* **Invite users** - Comma-delimited list of user email addresses to invite to the group chat. Supports [Template Variables](https://docs.firehydrant.com/docs/template-variables) and [Markdown](https://docs.firehydrant.com/docs/markdown-support)

## Group chat naming conventions

Some examples of group chat naming conventions our customers use:

* `incident-{{ number }}` will, for example, become **incident-42**. This is the default
* `-inc-{{ date }}` will become **-inc-2019-10-22**
* `{{ incident.severity }}-incident-{{ name }}-{{ date }}` will become **sev1-incident-bobbys-big-spill-2019-10-22**
* `-inc-{{ date | replace: '-', '' }}` will become **-inc-20191022**