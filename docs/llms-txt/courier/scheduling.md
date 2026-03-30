# Source: https://www.courier.com/docs/platform/automations/scheduling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduling

> Courier Automations support scheduled triggers via one-time, recurring, or cron-based scheduling. Set schedules in UTC-0, accounting for a 12-minute delay, without needing external API calls.

* **One-time:** Set the specific time and date to invoke the automation.
* **Recurrence:** Identify a repeat schedule for the automation to be invoked. This is similar to scheduling a repeat event in a calendar application.
* **Cron:** Similar to Recurrence but with more specificity using [crontab expressions](https://crontab.guru/).

Because scheduling is a part of Automations, it can be used across channels (eg. email, SMS, chat, in-app inbox, push) and providers (eg. Twilio, Sendgrid, email SMTP, Slack, MS Teams, WeChat).

## Setup Scheduling

To setup a scheduled automation, drag over the Schedule trigger from the triggers section onto the canvas. Publishing an automation template is sufficient to allow the trigger to invoke the automation on the provided schedule. You do not need to make a separate API call to invoke.

<Warning>
  The date picker uses your browser's timezone by default. You can change it using the timezone dropdown. After configuration, the displayed date remains relative to your browser timezone.
</Warning>

<Note>
  The schedule trigger is accurate to within \~12 minutes of the selected time.
</Note>

<Frame caption="Automation Schedule Trigger">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/automation-schedule.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=210f34e6e19a69a338ee2da1b2684887" alt="Schedule Trigger" width="2614" height="1612" data-path="assets/platform/automations/automation-schedule.png" />
</Frame>

## Related Resources

<CardGroup cols={2}>
  <Card title="Automation Designer" href="/platform/automations/designer" icon="pen-ruler">
    Build workflows visually
  </Card>

  <Card title="Segment Integration" href="/platform/automations/segment" icon="chart-line">
    Trigger automations from Segment events
  </Card>
</CardGroup>
