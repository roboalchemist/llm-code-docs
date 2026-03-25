# Source: https://docs.firehydrant.com/docs/runbook-step-create-or-rename-incident-slack-channel.md

# Create or rename Incident Slack channel

<Image align="center" alt="Example incident channel created for an incident" border={false} caption="Example incident channel created for an incident" src="https://files.readme.io/e092e67-image.png" width="650px" />

Organizing your communication is critical during an incident. FireHydrant gives you control over if and when a centralized channel is opened for your incident.

> 📘 Note:
>
> * At this time, FireHydrant supports only one primary incident channel created and tracked in the timeline per incident.

<Image align="center" alt="Slack &#x22;Create or Rename Incident Channel&#x22; step" border={false} caption="Slack &#x22;Create or Rename Incident Channel&#x22; step" src="https://files.readme.io/5811004-image.png" width="650px" />

This Runbook step creates or renames the incident channel in Slack. The behavior is as follows:

* **If the channel does not exist**, this step will create a new incident channel per your configurations.
* **If the channel exists because another Runbook step executed it elsewhere**, subsequent runs of this step will rename the channel if there are changes to the naming convention from the original.
* **If the channel exists because it was created outside of FireHydrant**, then FireHydrant cannot delete or rename that existing channel and will create a new one. This new channel will be named according to your specified conventions, and a dynamically calculated hash will be appended to the end because Slack requires channel name uniqueness.

The available fields to configure are:

* **Channel name format** - Name format of the channel. FireHydrant sees organizations using a variety of identifiers here, including the name or number of the incident, severity, and sometimes even external ticketing identifiers.
  * Slack limits channel names to only alphanumerics, dashes, and underscores, with 80 characters as the maximum length. If the name ends up being longer than 80 character, FireHydrant will truncate it to 80 characters.
  * This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables)
* **Channel visibility** - Set the Slack channel as public or private. Note that subsequent runs of this Runbook cannot change an existing channel's privacy, even if the settings are different. The reason is that changing a channel's privacy requires elevated permissions that FireHydrant has opted not to request from users.
* **Create a communications channel?** - This option is available for organizations that want to spin up multiple channels - one for primary incident response and another just for comms.
  * **Only** milestone updates made to the incident will be posted in both channels. Any chat messages or other activity within the comms channel will **not** be included in the comms channel timeline.
  * This use case is recommended for organizations that want a separate channel where people can chat, ask questions, etc., but without polluting the primary responders' channel and incident timeline.

## Channel Naming Conventions

Some examples of channel naming conventions our customers use:

* `incident-{{ number }}` will become **incident-42**. This is the default
* `-inc-{{ date }}` will become **-inc-2019-10-22**
* `{{ incident.severity }}-incident-{{ name }}-{{ date }}` will become **sev1-incident-bobbys-big-spill-2019-10-22**
* `-inc-{{ date | replace: '-', '' }}` will become **-inc-20191022**