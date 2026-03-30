# Source: https://firebase.google.com/docs/cloud-messaging/throttling-and-quotas.md.txt

Our goal is to always deliver every message sent using FCM. However, delivering
every message sometimes results in a poor overall user experience. In other
cases, we need to provide boundaries to ensure that FCM provides a scalable
service for all senders. The types of limits and quotas described in this
section help us balance these important factors.

> [!NOTE]
> **Note:** The limits discussed in this section are subject to change.

## Downstream message throttling

The HTTP v1 API introduced per-project, per-minute quotas for downstream
messaging. The default quota of 600k messages per minute covers over 99% of
FCM developers while protecting the stability of the system and
minimizing the impact of spiky projects.

[Spiky traffic patterns](https://firebase.google.com/docs/cloud-messaging/scale-fcm#problem:-traffic) can
result in quota exceeded errors. In an over quota scenario, the system serves
HTTP status code `429 RESOURCE_EXHAUSTED` ("QUOTA_EXCEEDED") until the quota is
refilled in the following minute. 429 responses may also be returned in overload
situations, so you are strongly encouraged to handle 429s according to
[published
recommendations](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode).

Keep in mind:

- The downstream quota measures messages, not requests.
- Client errors (HTTP status code 400-499) are counted (excluding 429s).
- Quotas are per-minute, but these minutes are not aligned to the clock.

### Monitoring quota

You can view quota, usage, and errors on the Google Cloud Console using the following:

1. Go to the [Google Cloud console](https://console.cloud.google.com/).
2. Select **APIs \& services**.
3. From the table list, select **Firebase Cloud Messaging API**.
4. Select **QUOTA \& SYSTEM LIMITS**.

> [!NOTE]
> **Note:** These graphs are not precisely time aligned with quota minutes, meaning 429s may be served when traffic appears to be under quota.

### Request a quota increase

Before requesting a quota increase, ensure that:

- Your usage is regularly ≥ 80% of quota for at least 5 consecutive minutes per day.
- You have \< 5% client error ratio, especially during peak traffic.
- You adhere to the best practices for sending [messages at
  scale](https://firebase.google.com/docs/cloud-messaging/scale-fcm).

If you meet these criteria, you can submit a [quota increase
request](https://firebase.google.com/support/troubleshooter/contact) for up to
+25% and FCM will make every practical effort to fulfill the request
(no increase can be guaranteed).

If you need more downstream messaging quota due to an impending launch or
temporary event, request your quota at least 15 days in advance to allow
sufficient time to handle the request. For large requests (\>18M messages per
minute), at least 30 days of notice is required. We can only approve 2 temp
quota events per year. The total duration of temp quota across the year must not
exceed 30 days. Launches and special event requests are still subject to the
client error ratio and best practices requirements.

To learn more, see [FCM quotas](https://firebase.google.com/support/faq#fcm-quotas).

### Topic message limits and fanout throttling

See [Topic messaging quotas and
limits](https://firebase.google.com/docs/cloud-messaging/topic-messaging#quotas-and-limits) for more
details.

### Collapsible message throttling

As described in [Collapsible
messages](https://firebase.google.com/docs/cloud-messaging/customize-messages/collapsible-message-types),
collapsible messages are content-free notifications designed to collapse on top
of each other. In the event that a developer is repeating the same message to an
app too frequently, we delay messages to reduce the impact on a
user's battery.

For example, if you send large numbers of new email sync requests to a single
device, we might delay the next email sync request a few minutes so that the
device can sync at a lower average rate. This throttling is done strictly to
limit the battery impact experienced by the user.

If your use case requires high burst send patterns, then non-collapsible
messages may be the right choice. For such messages, make sure to include the
content in such messages in order to reduce the battery cost.

We limit collapsible messages to a burst of 20 messages per app per device, with
a refill of 1 message every 3 minutes.

### Maximum message rate to a single device

For Android, you can send up to 240 messages per minute and 5,000 messages per
hour to a single device. This high threshold is meant to allow for short term
bursts of traffic, such as when users are interacting rapidly over chat. This
limit prevents errors in sending logic from inadvertently draining the battery
on a device.

For iOS, we return an error when the rate exceeds APNs limits.

> [!CAUTION]
> **Caution:** Don't routinely send messages near this maximum rate. This could waste end users' resources, and your app may be marked as abusive.