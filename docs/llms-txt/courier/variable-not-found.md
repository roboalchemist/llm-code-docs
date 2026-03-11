# Source: https://www.courier.com/docs/platform/content/template-settings/variable-not-found.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Throw on Variable Not Found

> Prevent messages from sending when required variables are missing. Checks only rendered blocks and shows errors in previews, logs, and observability integrations.

**Throw on Variable Not Found** prevents a channel from sending when a variable in the rendered template can't be resolved. Toggle it on in the notification template's **Settings > Advanced** section.

For example, if your email template includes `Hello {profile.first_name},` but `first_name` isn't in the user profile or the Send API `profile` object, Courier throws a render error for that channel. Errors are visible in the template preview and in message logs:

**Preview**

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/Bx2CvzFGBAIqaAxK/assets/platform/content/variable-not-found-on-preview.png?fit=max&auto=format&n=Bx2CvzFGBAIqaAxK&q=85&s=7dc9878fb1d6f8254077a42eb5cd3c99" alt="Screenshot of Variable Not Found on Preview" width="940" height="576" data-path="assets/platform/content/variable-not-found-on-preview.png" />
</Frame>

**Logs**

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/Bx2CvzFGBAIqaAxK/assets/platform/content/variable-not-found-on-logs.png?fit=max&auto=format&n=Bx2CvzFGBAIqaAxK&q=85&s=77c9ffb212d9902ab3d42ef5642bb186" alt="Screenshot of Variable Not Found on Logs" width="1005" height="622" data-path="assets/platform/content/variable-not-found-on-logs.png" />
</Frame>

## Conditional Blocks

The check runs after all conditionals are evaluated and only inspects blocks that will actually be sent. If a block is hidden by a condition, its variables aren't checked.

For example:

1. You add a conditional on `profile.first_name` to a text block.
2. The block uses `{profile.first_name}`.
3. The profile has no `first_name`, so the block is hidden by the condition.
4. Throw on Variable Not Found does not trigger, and the message sends successfully.

<Frame caption="A conditional block that hides when profile.first_name is missing">
  <img src="https://mintcdn.com/courier-4f1f25dc/qUk1Kbn04YYvlcHw/assets/platform/content/hide-conditional.png?fit=max&auto=format&n=qUk1Kbn04YYvlcHw&q=85&s=060e2f65db3cdea28986be49d3b0a826" alt="Screenshot of a Conditional Block" width="938" height="357" data-path="assets/platform/content/hide-conditional.png" />
</Frame>

## Multiple Channels

Each channel is checked independently. If `{profile.first_name}` appears in your email template but not in your Inbox template, only the email channel fails; Inbox renders and sends successfully.

## Observability

Render errors from this feature appear in [Outbound Webhooks](/platform/workspaces/outbound-webhooks) and [Observability integrations](/external-integrations/observability/intro-to-observability) under channel update events.

## Related

<CardGroup cols={2}>
  <Card title="Variables" href="/platform/content/variables/inserting-variables" icon="brackets-curly">
    Insert dynamic values from data, profile, tenant, and brand objects.
  </Card>

  <Card title="Send Conditions" href="/platform/content/template-settings/send-conditions" icon="filter">
    Control when notifications and channels send using conditional logic.
  </Card>
</CardGroup>
