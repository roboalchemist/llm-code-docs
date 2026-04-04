# Source: https://screenshotone.com/docs/guides/bulk-screenshots/

# How to take screenshots of multiple URLs

ScreenshotOne API supports taking screenshots of multiple URLs in one request—[bulk screenshots](/docs/bulk-screenshots/). But since it is a simple wrapper around the regular screenshot API, you might find it much better to implement your own bulk screenshot solution.

A few tips:

1. Use proxies if needed.
2. Retry failed requests.
3. Use a queue to process the URLs in batches, even internal onces.
4. Respect the concurrency limit. Build your solution based on dynamically calculated quota from [the "get usage" API endpoint](/docs/get-usage/).

Check out working example in the [ScreenshotOne examples](https://github.com/screenshotone/examples) repository—[bulk screenshots example](https://github.com/screenshotone/examples/tree/main/nodejs/bulk-screenshots).

In case you need help, feel free to reach out to support at [support@screenshotone.com](mailto:support@screenshotone.com).