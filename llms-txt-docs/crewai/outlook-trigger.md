# Source: https://docs.crewai.com/en/enterprise/guides/outlook-trigger.md

# Outlook Trigger

> Launch automations from Outlook emails and calendar updates

## Overview

Automate responses when Outlook delivers a new message or when an event is removed from the calendar. Teams commonly route escalations, file tickets, or alert attendees of cancellations.

<Tip>
  Connect Outlook in **Tools & Integrations** and ensure the trigger is enabled for your deployment.
</Tip>

## Enabling the Outlook Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Outlook** and switch the toggle to enable

<Frame caption="Microsoft Outlook trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f8a739ad0963ccddafeed60f21366628" alt="Enable or disable triggers with toggle" data-og-width="2186" width="2186" data-og-height="508" height="508" data-path="images/enterprise/outlook-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=03b5121587c619936c87f05e15992f08 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=651d2efd933f7109b216d343e6d6a6ce 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a7a27424bf507c739280376fd57ea80d 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=481164952ea35f62566b09d392a0910b 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f4d3db361e699578e9ce44bde1e683fd 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=aaabf7a26259291cf3b8545a4c3a996d 2500w" />
</Frame>

## Example: Summarize a new email

```python  theme={null}
from outlook_message_crew import OutlookMessageTrigger

crew = OutlookMessageTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": outlook_payload,
})
```

The crew extracts sender details, subject, body preview, and attachments before generating a structured response.

## Testing Locally

Test your Outlook trigger integration locally using the CrewAI CLI:

```bash  theme={null}
# View all available triggers
crewai triggers list

# Simulate an Outlook trigger with realistic payload
crewai triggers run microsoft_outlook/email_received
```

The `crewai triggers run` command will execute your crew with a complete Outlook payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_outlook/email_received` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>

## Troubleshooting

* Verify the Outlook connector is still authorized; the subscription must be renewed periodically
* Test locally with `crewai triggers run microsoft_outlook/email_received` to see the exact payload structure
* If attachments are missing, confirm the webhook subscription includes the `includeResourceData` flag
* Review execution logs when events fail to match—cancellation payloads lack attendee lists by design and the crew should account for that
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution
