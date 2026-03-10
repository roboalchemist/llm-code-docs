# Source: https://screenshotone.com/docs/screenshot-url/

# Screenshot URL

:::danger
The URL is temporary and will be available for a limited time—**4 hours maximum**. Do not rely on it for long-term storage of screenshots.

Except, when you use [caching](/docs/caching/), and the cache TTL is set to more than 4 hours.
:::

:::note
For long-term screenshot or video archival, consider [uploading them to any compatible S3-storage](/docs/guides/upload-to-s3/).
:::


When you set `response_type=json` for both [animated/scrolling screenshots](/docs/animated-screenshots/) or [regular screenshots](/docs/options/), you will get a screenshot URL in the response:

```json
{
    "screenshot_url": "..."
}
```

The URL is always a fresh URL where the screenshot is stored, it is not a cached URL unless you use [caching](/docs/caching/).

Also, when [using webhooks](/docs/async-and-webhooks/) and if you do not upload the screenshot to any S3-compatible storage, you will get the URL in the webhook request body,too.