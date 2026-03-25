# Source: https://docs.logrocket.com/docs/data-collected.md

# Data Collected

LogRocket automatically captures user behavior, network, performance, and log data with a single code snippet.

> 📘 Privacy concerns?
>
> All data captured can be sanitized for user privacy. See [Privacy](https://docs.logrocket.com/docs/privacy) for more information on sanitization.

## DOM video replay and user events (click, scroll, etc)

<Image align="center" src="https://files.readme.io/76829f8-Screenshot_2024-05-02_at_9.34.31_AM.png" />

LogRocket leverages the [MutationObserver API](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver) to capture session replays: "videos" of how users engage with your app. Replaying these videos allows you to understand user behavior and contextualize and diagnose bugs and errors.

## Network request and responses

<Image align="center" src="https://files.readme.io/5c895d9-Screenshot_2024-05-02_at_10.24.51_AM.png" />

LogRocket instruments the `XMLHttpRequest` and `fetch` APIs to capture request and response data from your app, including status codes, headers, and bodies.

## Performance data

<Image align="center" src="https://files.readme.io/0e25206-Screenshot_2024-05-02_at_10.15.07_AM.png" />

LogRocket captures detailed performance data, including CPU and memory usage; page load timelines - first input delay, time to first byte, largest contentful paint, and DOM complete; long tasks; average network speed; cumulative layout shift; and crashes.

On mobile apps, LogRocket captures CPU and memory usage, app start times, device and app throughput, frozen frames, and crashes.

For full details on our capabilities regarding performance data, see [Performance Monitoring](https://docs.logrocket.com/docs/performance-monitoring).

## Console and redux logs

<Image align="center" width="80%" src="https://files.readme.io/f946bb6-Screenshot_2024-05-02_at_10.23.02_AM.png" />

LogRocket automatically captures console logs, Redux actions and Redux state from your app.