# Source: https://screenshotone.com/docs/caching/

# Caching

:::note
When you don't use caching (`cache=true`), storage (`store=true`) or similar options, screenshots are rendered on-demand and returned directly to you without being stored anywhere on ScreenshotOne infrastructure. This ensures maximum privacy for your rendered content. Except if you use `response_type=json`, in which case the screenshot is temporarily stored on ScreenshotOne servers to serve the screenshot URL for you.

**During processing**, rendered content may be temporarily stored to pass through internal system components (such as queues, message brokers, or temporary buffers).

Caching is free and available for all plans. However, it is not intended to be used in CDN-like scenarios. It is for you to save costs on rendering.
:::

To use cache, the only option you need to set is `cache=true`:

```
https://api.screenshotone.com/screenshot?url=https://example.com&cache=true
```

[Check out more cache options](/docs/options/#caching).

And the screenshot will be cached for 4 hours by default or if you specify the `cache_ttl` option in seconds, you can prolong the cache time up to one month.

Caching is available for all rendering methods.

## When to use cache

The best usage of cache is to make rendering less expensive and faster, in case if you plan to render a lot of similar websites.

## Cache key

Screenshots are cached by the combination of all specified request options. And the [cache_key](/docs/options/#cache_key) option allows having different cached versions of the same screenshot.

## Impact on rendering quota

Cached screenshots are not counted by quota and are not logged anywhere. They are served directly from the cache. Screenshots are cached in a combination of Cloudflare CDN and R2 storage (like Amazon S3).

However, rarely but cache misses might happen and screenshots might be rendered again and counted towards your quota.

## Cache URL

:::note
Fetching the cache URL doesn't trigger the rendering process. It is a direct link to the cached screenshot.

If you want to regenerate the cache, you need to make a new API request with the same parameters and if the cache is expired, it will be rendered again.
:::

There is a header `x-screenshotone-cache-url` that provides a direct link to the cached image, PDF or video. The file exist as long as it was defined in the [cache_ttl](/docs/options/#cache_key) parameter when API request was performed with `cache=true`.

And if the `response_type` option is specified as `json`, you can find a cache URL in the JSON response too:

```json
{
    "cache_url": "https://cache.screenshotone.com/..."
}
```

What is the benefits of using the cache URL?

1. You don't share API keys and don't complicate your code with [signed links](/docs/signed-requests/).
2. You have full control over when the cache is refreshed—only you can trigger cache regeneration by making a new API request with the same parameters. If you share just the cache URL, others can only access the cached screenshot and cannot cause it to be regenerated after it expires. In contrast, sharing an API request link would allow anyone to trigger a new rendering once the cache expires. **Important!** The link will be unavailable after the cache is expired.

[The screenshot URL](/docs/screenshot-url/) might be different from the cache URL, but it will be likely the same as the cache URL.

## Cache TTL

:::note
For long-term screenshot or video archival, consider [uploading them to any compatible S3-storage](/docs/guides/upload-to-s3/).
:::

The cache TTL is 4 hours by default. You can change it by specifying the `cache_ttl` option in seconds up to one month.

Once the cache TTL is reached, the cached screenshot is deleted and the next request will be rendered again and counted towards your quota.

Cache URL will not be accessible after the cache TTL is reached. It is recommended to avoid using it and always render screenshots and videos with the rendering API request. It will rely on the cache anyway (if specified).

## Support

In case if you have any issues with caching or any ideas on how to improve it and make it better, please contact us at [support@screenshotone.com](mailto:support@screenshotone.com).