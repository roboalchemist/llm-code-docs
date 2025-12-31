# Source: https://docs.crewai.com/en/enterprise/guides/onedrive-trigger.md

# OneDrive Trigger

> Automate responses to OneDrive file activity

## Overview

Start automations when files change inside OneDrive. You can generate audit summaries, notify security teams about external sharing, or update downstream line-of-business systems with new document metadata.

<Tip>
  Connect OneDrive in **Tools & Integrations** and toggle the trigger on for your deployment.
</Tip>

## Enabling the OneDrive Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **OneDrive** and switch the toggle to enable

<Frame caption="Microsoft OneDrive trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=55774f3aee2c024ee81e8d543d9391be" alt="Enable or disable triggers with toggle" data-og-width="2166" width="2166" data-og-height="478" height="478" data-path="images/enterprise/onedrive-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=82cf038f92dfd9771c87ff44d364c42b 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=d79a78258619bcc517c9bcbf0e1b42f4 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6e5fc33aaebcffe573195b7b7a85986e 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bbd2f96f33f12988c8c52f36e178e553 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ef16d274ea3fe359655c8ac163b3c97a 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=0efecea63f338e2cdf7372a627993bac 2500w" />
</Frame>

## Example: Audit file permissions

```python  theme={null}
from onedrive_file_crew import OneDriveFileTrigger

crew = OneDriveFileTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": onedrive_payload,
})
```

The crew inspects file metadata, user activity, and permission changes to produce a compliance-friendly summary.

## Testing Locally

Test your OneDrive trigger integration locally using the CrewAI CLI:

```bash  theme={null}
# View all available triggers
crewai triggers list

# Simulate a OneDrive trigger with realistic payload
crewai triggers run microsoft_onedrive/file_changed
```

The `crewai triggers run` command will execute your crew with a complete OneDrive payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_onedrive/file_changed` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>

## Troubleshooting

* Ensure the connected account has permission to read the file metadata included in the webhook
* Test locally with `crewai triggers run microsoft_onedrive/file_changed` to see the exact payload structure
* If the trigger fires but the payload is missing `permissions`, confirm the site-level sharing settings allow Graph to return this field
* For large tenants, filter notifications upstream so the crew only runs on relevant directories
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution
