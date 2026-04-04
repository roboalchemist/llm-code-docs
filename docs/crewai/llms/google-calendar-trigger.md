# Source: https://docs.crewai.com/en/enterprise/guides/google-calendar-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Calendar Trigger

> Kick off crews when Google Calendar events are created, updated, or cancelled

## Overview

Use the Google Calendar trigger to launch automations whenever calendar events change. Common use cases include briefing a team before a meeting, notifying stakeholders when a critical event is cancelled, or summarizing daily schedules.

<Tip>
  Make sure Google Calendar is connected in **Tools & Integrations** and enabled
  for the deployment you want to automate.
</Tip>

## Enabling the Google Calendar Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Google Calendar** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e6594f439112ba76a399585e3e69e166" alt="Enable or disable triggers with toggle" data-og-width="2228" width="2228" data-og-height="1000" height="1000" data-path="images/enterprise/calendar-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=fa2e4f7da20c86c5ad7a6b7e2ab96116 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c3f8a6638774eadefa5a5924328d5787 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a2b8c83efc9a11a156877a8f061ca39c 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c772c71eda91c64d2db474c2ecb74159 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=35c5f5fe2de12a82aa0f1f798380def1 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1fefaff8a0a2cf8e9d7d4c11203ed0eb 2500w" />
</Frame>

## Example: Summarize meeting details

The snippet below mirrors the `calendar-event-crew.py` example in the trigger repository. It parses the payload, analyses the attendees and timing, and produces a meeting brief for downstream tools.

```python  theme={null}
from calendar_event_crew import GoogleCalendarEventTrigger

crew = GoogleCalendarEventTrigger().crew()
result = crew.kickoff({
    "crewai_trigger_payload": calendar_payload,
})
print(result.raw)
```

Use `crewai_trigger_payload` exactly as it is delivered by the trigger so the crew can extract the proper fields.

## Testing Locally

Test your Google Calendar trigger integration locally using the CrewAI CLI:

```bash  theme={null}
# View all available triggers
crewai triggers list

# Simulate a Google Calendar trigger with realistic payload
crewai triggers run google_calendar/event_changed
```

The `crewai triggers run` command will execute your crew with a complete Calendar payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run google_calendar/event_changed` (not `crewai run`) to
  simulate trigger execution during development. After deployment, your crew
  will automatically receive the trigger payload.
</Warning>

## Monitoring Executions

The **Executions** list in the deployment dashboard tracks every triggered run and surfaces payload metadata, output summaries, and errors.

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>

## Troubleshooting

* Ensure the correct Google account is connected and the trigger is enabled
* Test locally with `crewai triggers run google_calendar/event_changed` to see the exact payload structure
* Confirm your workflow handles all-day events (payloads use `start.date` and `end.date` instead of timestamps)
* Check execution logs if reminders or attendee arrays are missing—calendar permissions can limit fields in the payload
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution
