# Source: https://docs.argil.ai/pages/webhook-events/avatar-training-failed.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Avatar Training Failed Webhook

> Get notified when an avatar training failed

## About the Avatar Training Failed Event

The `AVATAR_GENERATION_FAILED` event is triggered when an avatar training process fails in Argil. This webhook event provides your service with a payload containing detailed information about the failed generation.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "AVATAR_TRAINING_FAILED",
  "data": {
    "avatarId": "<avatar_id>",
    "avatarName": "<avatar_name>",
    "extras": "<additional_key-value_data_related_to_the_avatar>"
  }
}
```

<Note>
  For detailed instructions on setting up this webhook event, visit our [Webhooks API Reference](/pages/api-reference/endpoint/webhooks.create).
</Note>
