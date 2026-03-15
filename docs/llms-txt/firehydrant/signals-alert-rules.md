# Source: https://docs.firehydrant.com/docs/signals-alert-rules.md

# Alerts & Alert Rules

<Image align="center" alt="Diagram of how an inbound Event becomes an Alert on FireHydrant" border={false} caption="Diagram of how an inbound Event becomes an Alert on FireHydrant" src="https://files.readme.io/8d6138c-image.png" width="650px" />

As mentioned in [Introduction to Signals](https://docs.firehydrant.com/docs/signals-introduction), your infrastructure and observability tools will generate <Glossary>Event</Glossary>s. Teams configure Alert Rules (see next section) to describe which events should alert and whom, and when a Rule matches, the Event is turned into an Alert and routed to the relevant party via [Escalation Policies](https://docs.firehydrant.com/docs/escalation-policies) and [On-Call Schedules](https://docs.firehydrant.com/docs/on-call-schedules).

You can also send Alerts directly to specific entities like teams, escalation policies, schedules, or users by [bypassing rules](#bypassing-rules), and finally, users can manually page out during incidents via chat applications, the web app, or the mobile app.

## Creating an Alert Rule

<Image align="center" alt="Adding rules helps filter incoming events to create alerts that matter to your team." border={false} caption="Adding rules helps filter incoming events to create alerts that matter to your team." src="https://files.readme.io/658222d-alert-rule.jpg" width="650px" />

Teams own all Alert Rules, so you can create a new rule for a team when looking at that team’s page (Teams > Team Name).

1. From the team’s page, click the “Rules” tab.
2. On the Rules page, click the “New Rule” button.
3. First, you're going to create a filter expression to turn incoming events into Alerts. You'll be presented with some dropdown to help you get started with building your filter: Level, Summary, Body, Annotations, and Tags.
   1. The filters will dynamically pull in data from the last 100 incoming events, and you can explore any of the 100 most recent events by clicking on the events in the list below your filter.
   2. Once you've added some filters to the input, you can directly edit the CEL Expression to add more complex logic. Learn more about [Using CEL](https://docs.firehydrant.com/docs/signals-using-cel).
4. After creating your filter, the next step is to select a target to notify when events match your rule. This can be an escalation policy, an on-call schedule or a user. Notably, these targets will be limited to the team that owns the current rule.
5. Finally, you can add a name for your rule. Additionally, you can choose an incident type to use when an incident is opened from a resulting alert. This allows you to pre-fill some fields like team or service-related data.
6. Click “Create Rule” to create your new rule.

### Overriding Priorities

<Image align="center" alt="Overriding the determined priority" border={false} caption="Overriding the determined priority" src="https://files.readme.io/cf05461-CleanShot_2024-06-28_at_11.05.48.png" width="650px" />

FireHydrant allows categorizing notifications as `HIGH`, `MEDIUM`, and `LOW` priority. The Transposers offered out-of-box will categorize an inbound Event according to sane defaults. However, when defining a Rule, you can override these assigned priorities at any time by setting the Notification Priority value.

This, in conjunction with [Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences), allows responders to strategically decide how they would like to be notified, and for which Alerts.

## Bypassing Rules

If you already have monitoring rules or routing configured externally and want to notify specific entities, you can send webhooks directly to:

* A team (**Note**: routing directly to a team will notify that team's ***default*** escalation policy)
* An escalation policy
* An on-call schedule
* A user

You can find these URLs by navigating to **Teams** > \***\* >** \* > **Alert Triggers**. The top-most section of this tab will allow you to select a dropdown to change the target and copy the webhook that routes directly to that target.

<Image align="center" alt="Retrieving webhooks that route directly to entities" border={false} caption="Retrieving webhooks that route directly to entities" src="https://files.readme.io/868cd1c-CleanShot_2024-04-23_at_17.41.31.png" />

## Permissions

Users with <Glossary>Member</Glossary> permissions can configure and update alert trigger rules within any teams they are members of. Users with <Glossary>Owner</Glossary> permission can edit the same for all teams regardless of their membership or lack thereof.

For more information, visit [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls).

## Next Steps

* Ensure you have configured your [Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences) so that you can receive your alerts when paged