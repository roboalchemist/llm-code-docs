# Source: https://docs.argil.ai/pages/webhook-events/video-generation-failed.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Generation Failed Webhook

> Get notified when an avatar video generation failed

## About the Video Generation Failed Event

The `VIDEO_GENERATION_FAILED` event is triggered when a video generation process fails in Argil. This webhook event provides your service with a payload containing detailed information about the failed generation.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "VIDEO_GENERATION_FAILED",
  "data": {
    "videoId": "<video_id>",
    "videoName": "<video_name>",
    "videoUrl": "<public_url_to_access_video>",
    "extras": "<additional_key-value_data_related_to_the_video>"
  }
}
```

<Note>
  For detailed instructions on setting up this webhook event, visit our [Webhooks API Reference](/pages/api-reference/endpoint/webhooks.create).
</Note>
