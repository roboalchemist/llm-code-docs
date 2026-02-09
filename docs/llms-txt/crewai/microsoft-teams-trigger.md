# Source: https://docs.crewai.com/en/enterprise/guides/microsoft-teams-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams Trigger

> Kick off crews from Microsoft Teams chat activity

## Overview

Use the Microsoft Teams trigger to start automations whenever a new chat is created. Common patterns include summarizing inbound requests, routing urgent messages to support teams, or creating follow-up tasks in other systems.

<Tip>
  Confirm Microsoft Teams is connected under **Tools & Integrations** and
  enabled in the **Triggers** tab for your deployment.
</Tip>

## Enabling the Microsoft Teams Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Microsoft Teams** and switch the toggle to enable

<Frame caption="Microsoft Teams trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=21eced4a8a635d17e32dccbeaf4ac217" alt="Enable or disable triggers with toggle" data-og-width="2192" width="2192" data-og-height="492" height="492" data-path="images/enterprise/msteams-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=3acc624c7b67651b5cd41df314902c41 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=1270b8fb54dc348f6cd242d2f3fd6480 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=76c96b3b169dd164c31e7bf88d4fdd8c 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=04b9e72848e035c107a0857ae708a0f3 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bee29617f472e6d4709d74c764d201c8 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c73be9f59015ab22173857ce635a2be9 2500w" />
</Frame>

## Example: Summarize a new chat thread

```python  theme={null}
from teams_chat_created_crew import MicrosoftTeamsChatTrigger

crew = MicrosoftTeamsChatTrigger().crew()
result = crew.kickoff({
    "crewai_trigger_payload": teams_payload,
})
print(result.raw)
```

The crew parses thread metadata (subject, created time, roster) and generates an action plan for the receiving team.

## Testing Locally

Test your Microsoft Teams trigger integration locally using the CrewAI CLI:

```bash  theme={null}
# View all available triggers
crewai triggers list

# Simulate a Microsoft Teams trigger with realistic payload
crewai triggers run microsoft_teams/teams_message_created
```

The `crewai triggers run` command will execute your crew with a complete Teams payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_teams/teams_message_created` (not `crewai
    run`) to simulate trigger execution during development. After deployment, your
  crew will automatically receive the trigger payload.
</Warning>

## Troubleshooting

* Ensure the Teams connection is active; it must be refreshed if the tenant revokes permissions
* Test locally with `crewai triggers run microsoft_teams/teams_message_created` to see the exact payload structure
* Confirm the webhook subscription in Microsoft 365 is still valid if payloads stop arriving
* Review execution logs for payload shape mismatches—Graph notifications may omit fields when a chat is private or restricted
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution
