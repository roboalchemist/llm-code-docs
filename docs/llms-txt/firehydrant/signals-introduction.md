# Source: https://docs.firehydrant.com/docs/signals-introduction.md

# Introduction to Signals

<Image alt="An overview of the Signal lifecycle" align="center" width="800px" src="https://files.readme.io/94fd099-event-rule-alert-incident.jpg">
  An overview of Signals
</Image>

With Signals, you can manage the entire incident management lifecycle in a single platform. Signals offers a complete alerting solution with on-call schedules, escalation policies, and multi-platform notifications to help your team better respond to incidents.

## Signals lifecycle

<Image alt="Diagram of how an inbound Event becomes an Alert on FireHydrant" align="center" width="650px" src="https://files.readme.io/8d6138c-image.png">
  Diagram of how an inbound Event becomes an Alert on FireHydrant
</Image>

### It starts with an event

<Image alt="Example logs in the Event Log" align="center" width="650px" src="https://files.readme.io/213702b1050c6bebf97b193a54f580335e811177c26349e460e8d843e167dfbf-CleanShot_2025-03-26_at_18.07.37.png">
  Example logs in the Event Log
</Image>

All alerts in FireHydrant begin with an incoming event. An <Glossary>Event</Glossary> is created when your monitoring tools (called [Event Sources](https://docs.firehydrant.com/docs/signals-configuring-event-sources)) send a webhook to FireHydrant.

FireHydrant offers multiple out-of-box event sources that translate between proprietary webhook formats into the universal format FireHydrant understands.

You can also configure [Custom Event Sources](https://docs.firehydrant.com/docs/custom-event-source) for any additional tool support FireHydrant doesn't already offer or to modify existing behavior.

Any events that are successfully received by FireHydrant, regardless of whether they actually alert anyone, will be included in the **[Event Log](https://app.firehydrant.io/signals/logs)**. If an error has occurred, then you may find it in the Errors tab of Event Logs.

<Image alt="Example errors in the Error Log" align="center" width="650px" src="https://files.readme.io/b9340904910fdc924ae4f2aa2b0b7001a7988d2498e0f820070daaef13addf93-image.png">
  Example errors in the Error Log
</Image>

### Match rules or directly target

<Image alt="Example alerts on the Alerts page" align="center" width="650px" src="https://files.readme.io/c346f133cb2d0cfe51e3b58161076eb47df6cdea176db3a6a5d15e8c496894f7-CleanShot_2025-03-26_at_18.09.02.png">
  Example alerts on the Alerts page
</Image>

Only when an alert is created does it show up on the **[Alerts page](https://app.firehydrant.io/signals/alerts)**.

Payloads from the events sent to FireHydrant are evaluated against [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) created by your teams. When an event payload matches a rule, an **Alert** is created and routed to a destination/target.

The rule specifies which target should be notified and may include one of [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies), [On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules), or [Users](https://docs.firehydrant.com/docs/user-administration). This provides strategic flexibility to your teams to only subscribe to and be notified by important Events without being fatigued by too much noise.

Escalation policies can also notify [webhook endpoints](https://docs.firehydrant.com/docs/signals-webhook-alert-targets) and [round robin](https://docs.firehydrant.com/docs/round-robin) targets within steps, on top of schedules and users.

**Alternatively, you can bypass Alert Rules and directly target an entity** (e.g., a team, escalation policy, schedule, user, etc.). In this scenario, the alert will always open against the intended target.

<Image alt="Directly routing Events to specific targets and always creating an Alert" align="center" width="650px" src="https://files.readme.io/a52abfa-CleanShot_2024-06-28_at_11.01.57.png">
  Directly routing Events to specific targets and always creating an Alert
</Image>

### Set notification preferences

Users can set their preferences for [where and how they receive alerts](https://docs.firehydrant.com/docs/signals-notification-preferences). For instance, a user may ask to have text messages and an email sent when an Alert is fired off.

FireHydrant supports all major communications methods (SMS, Voice, Push/App, Email, Slack, WhatsApp) for receiving alerts/pages.

### Respond to alerts

No matter where they receive an alert, responders can quickly take action and respond. They can:

* **Acknowledge** the alert to stop any additional alerts being sent to the next step of the escalation policy.
* **Escalate** the alert to send it to the next step of the escalation policy. This is helpful when a responder needs to pass off an alert based on time constraints or context.
* **Open an Incident** from the alert to kick off your team’s incident management workflow. FireHydrant will pull in key data from the alert to help the team make progress on resolving the incident.
* **Dismiss** the alert when they’ve determined it’s not an incident or should just be ignored.
* **Resolve** the alert or formally mark it as being "handled." An alert can be resolved at any point in the lifecycle unless dismissed or expired. When an alert is connected to an incident, the alert will be automatically resolved when the incident is resolved. The alert will also be automatically resolved when a second Event arrives with a “Close” status.
* **No action**. If no action is taken within the time specified in the Escalation Policy, it will automatically escalate to the next target or hand off to another team if specified.
* **Mark as Noise** if the alert is not useful and is just noise. This doesn't modify the alert's state; it only flags this alert for noise analytics. For more information, see [Noisy Alerts](https://docs.firehydrant.com/docs/noisy-alerts).

If an alert fully exhausts the chain of targets in escalation policies and handoffs, it will enter an "expired" state. The Expired state is still open but no longer actively notifying or escalating, and it can remain in this state indefinitely. From here, users can choose to ACK, Resolve, Dismiss, or open an incident from the alert just as they can with an Open alert.

<Image alt="Visualizing the alert lifecycle" align="center" width="650px" src="https://files.readme.io/786a81e-image.png">
  Visualizing the alert lifecycle
</Image>

## Alerts and Incident Management

A crucial part of responding to incidents is gathering context about what’s disrupting your services and applications. Alerts often contain substantial information, such as links and charts from your monitoring services. Having your alerting tool embedded in your incident management process means that your team can more quickly connect the dots between the data linked to your alerts and the root causes of your incidents.

Once a responder decides to create an incident from an alert, they transition from Signals over to the Incident Management portion of the platform. To read more about promoting alerts into incidents, see [Promoting Alerts into Incidents](https://docs.firehydrant.com/docs/signals-promoting-alerts-into-incidents).

## Next Steps

Now that you have an overview of how Signals works on FireHydrant, it's time to dive in to setup.

1. Configure **[Event Sources](https://docs.firehydrant.com/docs/signals-configuring-event-sources)** to send key events to FireHydrant
2. Designate **[On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules)** to designate who should be on-call, and when
3. Set up **[Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies)** to set up safety nets and escalations in case any responders aren't available when paged
4. Create **[Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules)** to decide when inbound events should trigger alerts
5. Modify **[Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences)** to decide how you would like to be notified when you are paged
6. Learn more about **[Promoting Alerts into Incidents](https://docs.firehydrant.com/docs/signals-promoting-alerts-into-incidents)** and incident management on FireHydrant