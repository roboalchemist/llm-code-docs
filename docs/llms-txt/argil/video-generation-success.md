# Source: https://docs.argil.ai/pages/webhook-events/video-generation-success.md

# Video Generation Success Webhook

> Get notified when an avatar video generation completed successfully

## About the Video Generation Success Event

The `VIDEO_GENERATION_SUCCESS` event is triggered when a video generation process completes successfully in Argil. This webhook event provides your service with a payload containing detailed information about the successful video generation.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "VIDEO_GENERATION_SUCCESS",
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
