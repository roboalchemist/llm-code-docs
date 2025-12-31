# Source: https://firebase.google.com/docs/cloud-messaging/scale-fcm.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/scale-fcm.md.txt

# Best practices when sending FCM messages at scale

<br />

Whether you are growing a nascent app or already running a high-traffic service,
you can benefit from this guide's insights and recommendations on how to scale
smoothly with FCM. These concepts and practices can help you avoid negative
impacts when you need to send large volumes of messages.

## Key terms and concepts

**Message Request**: A FCM message request; used interchangeably with "request",
"message", or "query".

**Requests-per-second (RPS)**: A metric to describe the rate of incoming
requests to FCM; used interchangeably with Queries-per-second (QPS).

**Quota Tokens, Token Buckets, and Refills** : When sending messages against the
FCM HTTP v1 API, each request consumes an allotted *Quota Token* in a given time
window. This window, called a "*Token Bucket* ", *refills* to full at the end of
the time window. For example: the HTTP v1 API allots 600K Quota Tokens for each
1-minute Token Bucket, which refills to full at the end of each 1-minute window.

**Server-side Throttling** : When traffic volume exceeds the FCM service's
capacity, requests beyond serving capacity are rejected to rate-limit ingress
flow. `429` error responses with `retry-after` headers may be returned to indicate
that you should wait a given time period before retrying the request.

**Client-side Throttling** : When clients observe request failures, high latency,
or `429` errors, they should voluntarily rate-limit egress flow to avoid exacerbating
congestion.

**[Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff)**:
When retrying errors, add exponentially increasing time delays. For example: 1s,
2s, 4s, 8s, 16s, 32s, and so forth.

**Jittering**: Avoiding retrying requests at exact intervals. With jittering,
you vary the retry delays through a random process to distribute them uniformly
over time (for example: 0.9s, 2.3s, 4.1s, 8.5s, 17.9s, 34.7s).

**Retry amplification**: When failed requests are retried without exponential
backoff/jittering, they often accumulate and add to ongoing traffic load,
potentially "amplifying" and exacerbating traffic congestion problems.

## The problem: traffic spikes

FCM processes millions of requests per second (RPS). The biggest contributor to
systemic congestion, latency problems, and outages is traffic spikes.

![A line chart showing traffic spiking at irregular intervals.](https://firebase.google.com/static/docs/cloud-messaging/doc-revamp/optimize-delivery/images/traffic-spikes.png)

### What is spiky traffic?

There are several different types of traffic spikes.

On-the-hour spikes: FCM receives more than double traffic during the first 30
seconds to 2 minutes of each hour. Similar, albeit lesser, spikes are also
observed at the half-hour and quarter-hour marks (examples: 00:15, 00:30, 00:45)

![A line chart showing semi-hourly and quarter-hourly spiking trends.](https://firebase.google.com/static/docs/cloud-messaging/doc-revamp/optimize-delivery/images/spike-intervals.png)

Retry amplification**:** Retrying failed or timed-out requests without
[Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) can
accumulate into repeating waves of traffic on top of existing traffic crests.

![A line chart showing increasing spike patterns.](https://firebase.google.com/static/docs/cloud-messaging/doc-revamp/optimize-delivery/images/retry-amplification.png)

Abrupt traffic pattern changes: Directing new traffic to FCM or moving traffic
to FCM across regions without smoothing factors such as gradual ramp-up can
cause spikes.

![A line chart showing one abrupt spike.](https://firebase.google.com/static/docs/cloud-messaging/doc-revamp/optimize-delivery/images/abrupt-change.png)

Front-loading quota token usage: Exhausting all quota tokens at the start of
quota windows instead of spreading out the requests evenly across the quota
windows will create on-off oscillations that are difficult and expensive to
load-balance.

![A line chart showing a very sharp spike.](https://firebase.google.com/static/docs/cloud-messaging/doc-revamp/optimize-delivery/images/token-frontload.png)
| **Tip:** Intra-minute volatility can create an apparent confusion where `429` errors are being served while the customer appears to be below quota. This happens because the monitoring and quota enforcement are not time aligned.

Special events: Traffic spikes during holidays (New Year's Eve) or sports events
([FIFA World Cup](https://firebase.blog/posts/2023/05/cloud-messaging-world-cup-scale/)).

![A line chart showing multiple repeated spikes.](https://firebase.google.com/static/docs/cloud-messaging/doc-revamp/optimize-delivery/images/holiday-traffic.png)

## Remedy traffic spikes by "flattening the curve"

This section describes strategies to smooth out traffic spikes where
possible---strategies to "flatten the curve."

### Use FCM only for appropriate use cases

There are some use cases where using FCM to deliver a notification is not
necessary or appropriate.

For example, for calendar event notifications, you can schedule a local task in
your app to display a notification at the appropriate times instead of sending
it from your app server. Limit FCM messages to calendar syncs.

### Avoid spikes

One scaling anti-pattern is to send FCM notifications as quickly as systems will
allow, instead of applying server-side throttling. Consider the following:

- Do all of your customers need to receive the same notification all within a 1 minute window? Would a 5 minute delivery window, for instance, still meet your business needs?
- Can your customers be segmented based on priority to smooth over the spikes?
- Can your notifications be scheduled ahead of time?

*Wherever possible*: avoid strategies that result in immediately exhausting your FCM send quota, only to repeat the pattern as soon as your token bucket refills. This access
pattern creates load-balancing problems for FCM and its dependent
systems. Ramp up traffic as gradually as possible. At minimum, ramp from 0 to
the max RPS across a 60 second time-window. Prefer longer windows for higher
RPS.

### Avoid "on-the-hour" traffic

*Where possible*: avoid sending messages within a 2 minute window of each of
the :00, :15, :30, and :45 minute marks.

### Implement server-side throttling

Implement server-side throttling to monitor and manage the flow of traffic to FCM.
| **Tip:** Monitoring is indispensable for investigating and debugging FCM scaling issues. Your production graphs help Firebase Support contextualize time, correlation, errors, and magnitude (absolute \& relative).

### Handling retries

While FCM strives to be highly available, at times some requests will time out
or fail. While the reasons vary, the following best practices optimize retry
behavior to deliver messages as soon as possible while minimizing impact to
traffic congestion.

#### Timeouts

Set at least a 10 second timeout on send requests before
retrying. Most of FCM's internal Remote Procedure Calls use a 10 second timeout.

#### Errors

- For 400, 401, 403, 404 errors: abort, and do not retry.
- For 429 errors: retry after waiting for the duration set in the retry-after header. If no retry-after header is set, default to 60 seconds.
- For 500 errors: retry with exponential backoff.

#### Exponential backoff

To avoid retry amplification, implement exponential
back-off with jittering for retrying requests. The Firebase Admin SDK, for
example, implements exponential backoff.

Here are some more recommended settings:

- Minimum Interval: Do not immediately retry a failed request with FCM. Wait at least 10 seconds before retrying a failed request.
- Maximum Interval: Set a maximum interval for dropping requests that are no longer timely, instead of retrying indefinitely.

If a request is continually retried with exponential backoff and is still
failing 60 minutes later, it is either miscategorized as a retryable error, or
FCM is experiencing an outage where retries may be inadvertently exacerbating
the situation.
| **Tip:** Implementing a geographically distributed server topology will improve redundancy and improve outcomes for both initial and backoff traffic.

### Create rollout and rollback plans, and make gradual changes

When making large-scale traffic changes, such as increasing traffic to FCM or
shifting traffic across regions or networks, designing a rollout/rollback plan
and implementing gradual changes will protect your users, your service, and FCM.

- A rollout plan aligns expectations for stakeholders. In certain situations (discussed below), you may want to share your rollout plan ahead of time with the FCM team to avoid surprises.
- A rollback plan allows you to account for contingencies and prepare mechanisms to quickly and safely recover from unanticipated failures.
- Making gradual changes has two aspects:
  - "Step-wise" ramp-ups: Steps should be 1% -\> 5% -\> 10% -\> 25% -\> 50% -\> 75% -\> 100% or finer. "[Soak](https://en.wikipedia.org/wiki/Soak_testing)" (observe system behavior under load) each step for 1 day to 1 week. This allows you to spot potential problems before the next "step-up"
  - Gradual traffic ramp-ups: When taking each "step" to ramp up traffic, smooth out the traffic over the span of at least an hour. This allows FCM's load-balancing infrastructure to appropriately scale your new traffic while minimizing the potential for hotspots and congestion.

Here is a hypothetical scenario for migrating 500,000 RPS globally from the
FCM Legacy HTTP API to the FCM HTTP v1 API:

| **Week** |   **Step**   |                          **Gradual Ramp-up Strategy**                           |
|----------|--------------|---------------------------------------------------------------------------------|
| 0        | 1% ramp-up   | Ramp-up smoothly from 0 to 5,000 RPS to FCM HTTP v1 over the course of an hour. |
| 1        | 5% ramp-up   | Ramp-up smoothly from 5,000 to 25,000 RPS over 2 hours.                         |
| 2        | 10% ramp-up  | Ramp-up smoothly from 25,000 to 50,000 RPS over 2 hours                         |
| 3        | 25% ramp-up  | Ramp-up from 50,000 to 125,000 RPS over 3 hours                                 |
| 4        | 50% ramp-up  | Ramp-up from 125,000 to 250,000 RPS over 6 hours                                |
| 5        | 75% ramp-up  | Ramp-up from 250,000 to 375,000 RPS over 6 hours                                |
| 6        | 100% ramp-up | Ramp-up from 375,000 to 500,000 RPS over 6 hours                                |

Hypothetical rollback plan:

- If 95-percentile latency increases to greater than 500 ms or if the error ratio exceeds 1% for more than an hour at any step, use dynamic configuration to roll back to the previous step immediately.
- Continue rollbacks to earlier steps until latency and error ratio return to nominal levels.

## When to reach out to FCM

Contact FCM through [Firebase Support](https://firebase.google.com/support)
if any of the following apply:

- Default quotas no longer meet your use case
- You are changing your sending patterns within a 3 month window at a scale of 100,000 RPS globally or 30,000 RPS continentally.