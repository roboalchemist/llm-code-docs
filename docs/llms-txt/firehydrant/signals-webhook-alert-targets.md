# Source: https://docs.firehydrant.com/docs/signals-webhook-alert-targets.md

# Webhook Alert Targets

<Image alt="Webhook Targets" align="center" src="https://files.readme.io/5b74932a857204e78a25b9dc83dcd43826752948bad9f110d423df5a2aa811ed-CleanShot_2024-10-09_at_12.17.432x.png">
  Webhook Targets
</Image>

**Webhook targets** on FireHydrant allow alerts to be sent to external destinations via a webhook. These webhook destinations can then be selected as targets in [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies) and [Page people via Signals](https://docs.firehydrant.com/docs/runbook-step-page-people-via-signals) Runbook steps to notify.

> 📘 Note:
>
> Webhook targets are destinations to send alerts to and should not be confused with [Webhook Event Sources](https://docs.firehydrant.com/docs/generic-webhook-event-source), which is for receiving <Glossary>Event</Glossary>s to FireHydrant.

## Configuration

1. On the Signals page, click on the **Webhook Targets** subpage on the left.
2. Here, click on "+ Add Webhook Target" on the top right to create a new webhook target.
3. The following are available parameters to configure:
   1. **Name (required)** - A descriptive name for this webhook target
   2. **URL (required)** - Single destination URL to send the alert to. Each webhook target sends to one endpoint URL. To send alerts to multiple destinations, create multiple webhook targets.
   3. **Signing Key** - A key or other token that your receiving source can use to verify that the webhook is coming from FireHydrant
4. Once filled, click "Save" to create the webhook target.
5. Once the webhook target is created, it will now be selectable in any Escalation Policies as part of EP steps. When an alert hits this EP, a webhook will be sent to the webhook target with the following JSON layout:

```json Webhook Target JSON Structure
{
  "id": string (UUID),
  "notValidAfter": string (ISO 8601 datetime),
  "notificationPriority": string (HIGH, MEDIUM, LOW),
  "organizationId": string (UUID),
  "rule": {
    "expression": string,
    "id": string (UUID),
    "organizationId": string (UUID),
    "target": {
      "id": string (UUID),
      "organizationId": string (UUID),
      "type": string (ESCALATION_POLICY, ON_CALL_SCHEDULE, USER),
    },
    "teamId": (UUID)
  },
  "signal": ( See Events Data Model ),
  "target": {
    "id": string (UUID),
    "organizationId": string (UUID),
    "type": string (TEAM, ESCALATION_POLICY, ON_CALL_SCHEDULE, USER)
  }
}
```

Note above that you will see **either** `rule` or `target` depending on whether you send an alert manually (`target`) or if an alert was triggered by an inbound event from a source `rule`.

`signal` will always be present in the payload, along with the other parameters. For more information about the `signal` structure, visit [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).