---
---
title: Set Up
description: "Learn how to set up Sentry's Metrics feature using our supported SDKs."
---

  Metrics is currently in Open Beta for non-Enterprise plans running the
  JavaScript or Python SDKs. If you'd like access, please comment with your org
  slug on [this GitHub
  discussion](https://github.com/getsentry/sentry/discussions/102275) or contact
  us at feedback-metrics@sentry.io.

To set up Sentry Metrics, use the links below for supported SDKs. After it's been set up, you'll be able to send counters, gauges, and distributions from your code and view them in Sentry with direct links to related traces.

## Supported SDKs

### JavaScript

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

### Python

- 
- 
- 
- 
- 
- 
- 
- 

### PHP

- 
- 
- 

## Upcoming SDKs

We're actively working on adding Metrics functionality to additional SDKs. Check out these GitHub issues for the latest updates:

- 

- 

- 

- 

- 

- 

- 

- 

- 

If you don't see your platform listed above, please reach out to us on [GitHub](https://github.com/getsentry/sentry/discussions/102275), [Discord](https://discord.gg/sentry) or contact us at [feedback-metrics@sentry.io](mailto:feedback-metrics@sentry.io), we'll get it prioritized!

## Best Practices

### Naming Conventions

Use descriptive, dot-separated names that indicate the metric's purpose:

- **Good**: `checkout.failed`, `email.sent`, `queue.depth`
- **Avoid**: `metric1`, `counter`, `x`

### Attributes

Add attributes for any dimension you want to group or filter by:

```javascript
Sentry.metrics.count("api.request", 1, {
  attributes: {
    endpoint: "/users",
    method: "GET",
    status: "200",
    region: "us-west",
  },
});
```

This allows you to query metrics like:

- `sum(api.request)` grouped by `endpoint`
- `sum(api.request)` where `status:500`
- `sum(api.request)` grouped by `region` where `method:POST`

### Units

Always specify units for clarity:

- Time: `millisecond`, `seconds`
- Size: `byte`, `kilobyte`, `megabyte`

### When to Instrument

Add metrics at key decision points in your code:

- **Before/after critical operations**: Track success and failure rates
- **At service boundaries**: Monitor external API calls, database queries
- **Business logic**: Capture important business events
- **Resource usage**: Track queue depths, connection pools, cache sizes
