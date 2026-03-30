# Source: https://firebase.google.com/docs/cloud-messaging/topic-messaging.md.txt

[Video](https://www.youtube.com/watch?v=pP044hR6zNQ)

FCM topic messaging lets you to send a message to multiple devices
that have opted in to a particular topic. You compose topic messages as needed,
and FCM handles routing and delivering the message reliably to the
right devices.

Key points about topic messaging:

- Best suited for publicly available information like weather alerts.
- Topic messages are optimized for throughput rather than latency. For fast, secure delivery to single devices or small groups, [target messages](https://firebase.google.com/docs/cloud-messaging/send/v1-api#send-messages-to-specific-devices) to registration tokens instead of topics.

## Quotas and limits

Topic messaging supports unlimited subscriptions for each topic. However,
FCM enforces limits in these areas:

- One app instance can be subscribed to no more than 2000 topics.
- If you are using [batch subscription](https://developers.google.com/instance-id/reference/server#manage_relationship_maps_for_multiple_app_instances) to subscribe app instances, each request is limited to 1000 app instances.

### Subscription throttling

The rate for adding or removing topic subscriptions is limited to 3,000 QPS per
project.

The frequency of new subscriptions is rate-limited per project. If you send too
many subscription requests in a short period of time, FCM
servers will respond with a `429 RESOURCE_EXHAUSTED` ("QUOTA_EXCEEDED")
response. Retry with exponential backoff.

### Fanout throttling

Message fanout is the process of sending a message to multiple devices, such as
when you target topics and groups, or when you use the
[Notifications composer](https://console.firebase.google.com/project/_/notification)
to target audiences or user segments.

Message fanout is not instantaneous and so occasionally you have multiple
fanouts in progress concurrently. We limit the number of concurrent message
fanouts per project to 1,000. After that, we may reject additional fanout
requests or defer the fanout of the requests until some of the already in
progress fanouts complete.

The actual achievable fanout rate is influenced by the number of projects
requesting fanouts at the same time. A fanout rate of 10,000 QPS for an
individual project is not uncommon, but that number is not a guarantee and is a
result of the total load on the system. It is important to note that the
available fanout capacity is divided among projects and not across fanout
requests. So, if your project has two fanouts in progress, then each fanout will
only see half of the available fanout rate. The recommended way to maximize your
fanout speed is to only have one active fanout in progress at a time.

> [!NOTE]
> **Note:** This fanout rate quota is not adjustable.

## Next Steps

- Learn how to [Manage Topic Subscriptions](https://firebase.google.com/docs/cloud-messaging/manage-topic-subscriptions) using the Admin SDK or from your client app.
- Learn how to [Send Messages to Topics](https://firebase.google.com/docs/cloud-messaging/send-topic-messages) using the Admin SDK or the FCM v1 HTTP API.