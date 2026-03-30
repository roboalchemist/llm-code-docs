# Source: https://docs.firehydrant.com/docs/runbook-step-create-microsoft-teams-incident-channel.md

# Create Microsoft Teams Incident Channel

Organizing your communication is critical during an incident. FireHydrant gives you control over if and when a centralized channel is opened for your incident.

> 📘 Note:
>
> * At this time, FireHydrant supports only one primary incident channel per incident.

## Configuring the step

<Image alt="&#x22;Create Microsoft Teams incident channel&#x22; step" align="center" width="650px" src="https://files.readme.io/d6970eb-CleanShot_2024-05-22_at_16.56.38.png">
  "Create Microsoft Teams incident channel" step
</Image>

This Runbook step creates an incident channel in the chosen Team. The **Channel name format** field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables).

This step comes with the following configurable fields:

* **Name** - A configurable name for the step. This shows up in the Runbook details tab for each incident and has no impact on actual execution
* **Channel name format** - The name/format for the channel being created. It supports [Template Variables](https://docs.firehydrant.com/docs/template-variables) and [Markdown](https://docs.firehydrant.com/docs/markdown-support)
  * **Note:** If the channel name format references variables like `severity` or `priority`, changes to these parameters during the incident will also change the name of the channel.

## Channel Naming Conventions

Some examples of channel naming conventions our customers use:

* `incident-{{ number }}` will, for example, become **incident-42**. This is the default
* `-inc-{{ date }}` will become **-inc-2019-10-22**
* `{{ incident.severity }}-incident-{{ name }}-{{ date }}` will become **sev1-incident-bobbys-big-spill-2019-10-22**
* `-inc-{{ date | replace: '-', '' }}` will become **-inc-20191022**