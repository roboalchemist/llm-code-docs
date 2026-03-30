# Source: https://www.courier.com/docs/platform/journeys/nodes/throttle.md

# Source: https://www.courier.com/docs/platform/automations/throttle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Throttle Node

> Throttle Nodes limit the number of automation-triggered messages per user or group within a set timeframe, preventing over-notification. Configure by user, global, or dynamic scope in Automations.

The throttle node limits how many automation-triggered messages a user or group receives within a set timeframe. Events that exceed the configured limit are dropped and do not pass to the next node.

Because Throttle is a part of Automations, it can apply across channels (eg. email, SMS, chat, in-app inbox, push) and providers (eg. Twilio, Sendgrid, email SMTP, Slack, MS Teams, WeChat).

## Throttle Node Example Use Cases

**Alert Notifications**

When sending alert notifications, you may want to limit the number of notifications sent to a user in a given period to avoid bombarding them with too many alerts.

**Email Campaigns**

If you are running an email campaign, you may want to limit the number of emails sent to a customer within a specific timeframe to avoid overwhelming them with too many messages.

In general, a Throttle step can be useful in any situation where you need to control the flow of data or limit the frequency of an action.

Courier will allow you to specify what next steps should be taken when the throttle is triggered, and what steps should be taken when the throttle is not triggered.

## Creating A Throttle Step

To create a Throttle, use the "Throttle" action, then fill out details in the step node.

Specify maximum number of events to allow through the throttle, and the time period to throttle by.

You have the options to throttle by:

| Scope     | Usage                                                                                                       |
| :-------- | :---------------------------------------------------------------------------------------------------------- |
| `user_id` | Apply throttling by using `user_id` coming from `data`                                                      |
| `GLOBAL`  | Let Courier decide the throttle parameter.                                                                  |
| `Dynamic` | You can use arbitrary value available in your `run_context` by referencing it like `refs.data.throttle_key` |

Below is an example of a throttle step that allows 2 events to pass through for a given user in a 24-hour period before throttling.

In this example, the throttle is set to be applied by `user_id`. You have to supply `user_id` in the following manner to throttle the user.

```bash  theme={null}
curl --request POST \
  --url https://api.courier.com/automations/<automation_template_id>/invoke \
  --header 'Authorization: Bearer <replace_with_api_key>' \
  --header 'Content-Type: application/json' \
  --data '{
  "data": {
		"user_id": "<user_id>"
  }
}
```

<Frame caption="Creating Throttle Step">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/digests-batching-throttling/throttle-step.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=3e3b2d6437d95176a283ed5a3eb3975f" alt="Creating throttle step" width="1976" height="960" data-path="assets/platform/automations/digests-batching-throttling/throttle-step.png" />
</Frame>

## Related Resources

<CardGroup cols={2}>
  <Card title="Batching" href="/platform/automations/batching" icon="layer-group">
    Group multiple events into a single notification
  </Card>

  <Card title="Send Limits" href="/platform/sending/send-limits" icon="gauge">
    Cap message volume by user, topic, or tenant
  </Card>
</CardGroup>
