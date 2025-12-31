# Source: https://docs.crewai.com/en/enterprise/guides/google-drive-trigger.md

# Google Drive Trigger

> Respond to Google Drive file events with automated crews

## Overview

Trigger your automations when files are created, updated, or removed in Google Drive. Typical workflows include summarizing newly uploaded content, enforcing sharing policies, or notifying owners when critical files change.

<Tip>
  Connect Google Drive in **Tools & Integrations** and confirm the trigger is enabled for the automation you want to monitor.
</Tip>

## Enabling the Google Drive Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Google Drive** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=caef65990821bbc38454b46ca8f7bc46" alt="Enable or disable triggers with toggle" data-og-width="2208" width="2208" data-og-height="1540" height="1540" data-path="images/enterprise/gdrive-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=26fc4c3542735f7ff2f8723a7bec0265 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=67b08f32c76c711734916902a4df35a3 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=5d0695c5d0f5ebd51d6413c0334a0ce6 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6b2600ca253c042e06f2108c68d5cff3 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=62541a717c8dee05cee7310561882f58 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ac92f2d61bf065c81a2ce6f02cac5d9d 2500w" />
</Frame>

## Example: Summarize file activity

The drive example crews parse the payload to extract file metadata, evaluate permissions, and publish a summary.

```python  theme={null}
from drive_file_crew import GoogleDriveFileTrigger

crew = GoogleDriveFileTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": drive_payload,
})
```

## Testing Locally

Test your Google Drive trigger integration locally using the CrewAI CLI:

```bash  theme={null}
# View all available triggers
crewai triggers list

# Simulate a Google Drive trigger with realistic payload
crewai triggers run google_drive/file_changed
```

The `crewai triggers run` command will execute your crew with a complete Drive payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run google_drive/file_changed` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>

## Monitoring Executions

Track history and performance of triggered runs with the **Executions** list in the deployment dashboard.

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>

## Troubleshooting

* Verify Google Drive is connected and the trigger toggle is enabled
* Test locally with `crewai triggers run google_drive/file_changed` to see the exact payload structure
* If a payload is missing permission data, ensure the connected account has access to the file or folder
* The trigger sends file IDs only; use the Drive API if you need to fetch binary content during the crew run
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution
