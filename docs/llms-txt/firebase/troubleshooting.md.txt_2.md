# Source: https://firebase.google.com/docs/cloud-messaging/troubleshooting.md.txt

This page provides troubleshooting help and answers to frequently asked
questions about Cloud Messaging.

<br />

### What's the
difference between the the Notifications composer and FCM?

<br />

Firebase Cloud Messaging provides a complete set of messaging
capabilities through its client SDKs and HTTP server
protocol. For deployments with more complex messaging requirements,
FCM is the right choice.

The Notifications composer is a lightweight, serverless messaging
solution built on Firebase Cloud Messaging. With a user-friendly
graphical console and reduced coding requirements,
the Notifications composer lets users send messages to
re-engage and retain users, foster app growth, and support marketing
campaigns.

<br />

| **Capabilities** |   | **Notifications composer** | **Cloud Messaging** |
|---|---|---|---|
| **Target** | Single device | Yes | Yes |
|   | Clients subscribed to topics (i. e. weather) | Yes | Yes |
|   | Clients in predefined user segment (app, version, language) | Yes | No |
|   | Clients in specified analytics audiences | Yes | No |
|   | Clients in device groups | No | Yes |
|   | Upstream from client to server | No | Yes |
| **Message Type** | Notifications up to 2kb | Yes | Yes |
|   | Data messages up to 4kb | No | Yes |
| **Delivery** | Immediate | Yes | Yes |
|   | Future client device local time | Yes | No |
| **Analytics** | Built-in Notifications analytics collection and funnel analytics | Yes | No |

<br />

<br />

<br />

<br />

### Do I need to use other
Firebase services in order to use FCM?

<br />

You can use Firebase Cloud Messaging as a standalone component, without using
other Firebase services.

<br />

<br />

<br />

### Why do my targeted devices
apparently fail to receive messages?

<br />

When it looks like devices haven't successfully received messages, check first
for these two potential causes:

**Foreground message handling for notification messages.** Client apps need to
add message handling logic to handle notification messages when the app is in
the foreground on the device. See the details for
[iOS](https://firebase.google.com/docs/cloud-messaging/downstream#receive_downstream_messages) and
[Android](https://firebase.google.com/docs/cloud-messaging/downstream#sample-receive).

**Network firewall restrictions.** If your organization has a firewall that
restricts the traffic to or from the Internet, you need to configure it to allow
connectivity with FCM in order for your Firebase Cloud Messaging client
apps to receive messages. The ports to open are:

- 5228
- 5229
- 5230

FCM usually uses 5228, but it sometimes uses 5229 and 5230.
FCM doesn't provide specific IPs, so you should allow your firewall to
accept outgoing connections to all IP addresses contained in the IP blocks
listed in Google's [ASN of 15169](https://bgp.he.net/AS15169#_prefixes).

<br />

<br />

<br />

### Why
isn't `onMessageReceived` being called in my Android app?

<br />

When your app is in the background, [notification
messages](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type)
are displayed in the system tray, and `onMessageReceived` is not called. For
notification messages with a data payload, the notification message is displayed
in the system tray, and the data that was included with the notification message
can be retrieved from the intent launched when the user taps on the
notification.

For more information, see [Receive and handle messages](https://firebase.google.com/docs/cloud-messaging/downstream#sample-receive).

<br />

<br />

<br />

### Why do I get 404
error when I send messages to an active app instance restored from a backup?

<br />

FID (Firebase Installation ID) is the identifier of an app instance. By default,
Firebase Installation data is backed up and restored. So in the restoration
case, the restored app instance and the original app instance share the same
FID. Since FCM only stores one token per FID, if both the original app instance
and the restored app instance are in use, then when one app instance registers
with FCM, the other app instance's token is removed, which causes 404
errors.

We recommend developers to do the following in their app:

- [Exclude](https://developer.android.com/identity/data/autobackup#xml-include-exclude) Firebase installation data in backup. The Firebase installation data is stored in a `PersistedInstallation....json` file. The filename is a constant for an app. For example, `<exclude domain="file" path="PersistedInstallation.W0R...GQ.json"
  />`

<br />

<br />

<br />

### Apple
announced they're deprecating the legacy binary protocol for APNs. Do I need to
do anything?

<br />

No. Firebase Cloud Messaging switched to the HTTP/2-based APNs protocol in 2017.
If you're using FCM to send notifications to iOS devices, there should
be no action required on your part.

<br />

<br />

## FCM quotas and limits

<br />

### How do I notify a large customer
base within 2 minutes?

<br />

This use case cannot be supported. You must spread your traffic out over 5
minutes.

<br />

<br />

<br />

### My app notifies users of
events, and these messages must be delivered immediately to support my business
model. Can I get more quota?

<br />

Unfortunately, we cannot grant quota increases for this reason. You must spread
your traffic out over 5 minutes to [avoid spiky
traffic](https://firebase.google.com/docs/cloud-messaging/scale-fcm#avoid-spikes).

<br />

<br />

<br />

### My messages are about
scheduled events. How can I send all traffic at the top of the hour?

<br />

We recommend that you start sending the notifications at least 5 minutes prior
to the event. Alternatively, send [data
messages](https://firebase.google.com/docs/cloud-messaging/cloud-messaging/customize-messages/set-message-type#data-messages)
and implement your platform's analog of `onMessageReceived` handler to schedule
local notifications ahead of time.

<br />

<br />

<br />

### How can I monitor my quota usage?

<br />

See Google Cloud guidance on how to [chart and monitor quota metrics](https://cloud.google.com/monitoring/alerts/using-quota-metrics).

<br />

<br />

<br />

### 429 errors are hard
for me and my business to handle. Can I get an exemption or more quota to avoid
getting 429s?

<br />

While we understand that quota limits can be challenging, quotas are vital to
keeping the service reliable and we can't grant exemptions. Use retries to
properly [handle 429 errors](https://firebase.google.com/docs/cloud-messaging/scale-fcm#handling-retries).

<br />

<br />

<br />

### How long will it
take for my quota increase request to be fulfilled?

<br />

Your [quota increase
request](https://firebase.google.com/docs/functions/quotas#when_you_reach_a_quota_limit) depends on your
use of FCM. In any case, you can expect an answer in a few business
days. In some cases, there may be some back-and-forth regarding your usage of
FCM and various circumstances, which can prolong the process. If all
requirements are met, most requests will be handled within 2 weeks.

<br />

<br />

<br />

### Can I get more quota for a
temporary event?

<br />

You can request additional quota to support an event lasting up to 1 month.
File the request at least 1 month in advance of the event and with clear details
on when the event starts and ends, and FCM will make every practical
effort to fulfill the request. If granted, these quota increases will be
reverted after the event's end date.

<br />

<br />

<br />

### Is my current quota subject
to change?

<br />

While Google won't do so lightly, quotas may be changed as needed to protect the
integrity of the system. When possible, Google will notify you in advance of
such changes. Keep your [Cloud MSA
contacts](https://cloud.google.com/docs/cloud-msa) updated to increase the
chances of receiving service announcements.

<br />

<br />