# Source: https://www.courier.com/docs/platform/automations/segment.md

# Source: https://www.courier.com/docs/external-integrations/cdp/segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment

> Connect Segment to Courier to send identify, track, and group events into Courier automations, and send Courier message events back to Segment for analytics.

## Segment to Courier

Courier's Destination for Segment provides a straightforward way to send data from web or mobile applications into Courier to improve notification delivery and management.

These events are visible on the [Segment integration page](https://app.courier.com/channels/segment) inside Courier Studio, where you can map them to trigger notification workflows. For example, you can trigger an automation that welcomes a new user when an `analytics.identify` event is received from Segment.

**Supported Segment Events:**

* `analytics.group`
* `analytics.identify`
* `analytics.track`

### Connecting Segment

1. Log into the Segment app and navigate to the [Destinations](https://segment.com/docs/connections/destinations) catalog page.
2. Click **Add Destination**.
3. Search for Courier in the Destinations Catalog and select the Courier destination.
4. Choose the Source that should send data to the Courier destination.
5. In the [Courier Integrations Page](https://app.courier.com/integrations), search for Segment and click on it to access the Courier API Key. If you don't see a key here, go to the [Courier Settings Page](https://app.courier.com/settings) and copy the Auth Token from the API Keys section.
6. Enter the Courier API Key or Auth Token in the API Key field of the Courier destination settings in Segment.
7. To validate the setup, navigate to the destination's "Event Tester" in Segment and click "Send Event" at the bottom of the page. In Courier Studio, refresh the page or wait a few seconds. If the destination setup was successful, the test event will appear in the list.

### Identify Calls

Segment Identify calls allow you to connect a user to their actions (Segment events) and record traits about them.
The user can be identified by their User ID and can hold additional traits such as their name and email.
These traits can be used to update Courier recipient profiles over time. See the [Segment Identify spec](https://segment.com/docs/connections/spec/identify/) and [Courier Profiles API](/api-reference/user-profiles/get-a-profile) for details.

Example Payload

```json  theme={null}
{
  "messageId": "segment-test-message-iskh4123",
  "timestamp": "2024-05-21T18:00:18.913Z",
  "type": "identify",
  "email": "test@example.org",
  "traits": {
    "trait1": 2,
    "email": "test@example.org"
  },
  "userId": "rod-test"
}
```

### Track Calls

Segment Track calls allow you to record actions performed by your users, including any properties associated with their actions. See the [Segment Track spec](https://segment.com/docs/connections/spec/track/) for details.

Track events appear with a prefix of `track/` in Courier. Courier gathers data from the track's `properties` object. To send notifications based on a Segment event, these track events must be mapped to Courier Automations.

Here's an example Segment API call:

```jsx  theme={null}
analytics.track('Login Button Clicked', {
  messageId: "segment-test-message-a8rmf",
  timestamp: "2021-12-07T08:41:59.410Z",
  type: "track",
  email: "test@example.org",
  projectId: "4GgKeBoVJkT9EZL4vAmduv",
  properties: {
    property1: 1,
    property2: "test",
    property3: true
  },
  userId: "test-user-cqw3gr",
  event: "Segment Test Event Name"
})
```

The associated JSON from the Segment API call will be sent to Courier as a track event:

```json  theme={null}
{
  "messageId": "segment-test-message-a8rmf",
  "timestamp": "2021-12-07T08:41:59.410Z",
  "type": "track",
  "email": "test@example.org",
  "projectId": "4GgKeBoVJkT9EZL4vAmduv",
  "properties": {
    "property1": 1,
    "property2": "test",
    "property3": true
  },
  "userId": "test-user-cqw3gr",
  "event": "Segment Test Event Name"
}
```

The above JSON object is mapped into the Courier data object as follows:

```json  theme={null}
{
  "data": {
    "property1": 1,
    "property2": "test",
    "property3": true
  }
}
```

### Troubleshooting

If you continue to see the "No Segment events received yet." message in Courier, it could mean that Segment was unable to successfully set up your Courier workspace as a destination. To ensure that the test event sent by Segment is successfully received by Courier:

1. Double-check that your API Key was copied accurately into Segment.
2. Check where the `email` property is placed within the test JSON object in Segment. If it is at the top level of an identify call, move it within the `traits` object and resend the test event.
3. If you are still experiencing issues, please reach out to Courier Support.

***

## Courier to Segment

You can also configure Courier as a Segment Source so that Courier message and audience events flow back into Segment for analytics.

### Setting Up Courier as a Segment Source

1. In Segment, navigate to the *Sources* page (under "Connections").
2. Select your framework of choice (e.g., Node.js).
3. Obtain a write key. After adding Node.js as a source, you'll see a page with instructions on how to add Segment to your Node.js codebase.
   Copy the write key from this page.
4. In Courier's Segment configuration, paste your [Segment Write Key](https://segment.com/docs/connections/find-writekey/) in the *Segment write key* input field.

After adding your Segment write key, Courier will send updates to Segment. Update events include messages being sent, opened, clicked, delivered, unroutable, and undeliverable.

### Courier Events Sent to Segment

When Courier is set up as a Segment source, the following events can be tracked in Segment:

#### Message Events

* `Message Clicked`
* `Message Delivered`
* `Message Opened`
* `Message Sent`
* `Message Undeliverable`
* `Message Unroutable`

#### Audience Events

* `Audience User Matched`
* `Audience User Unmatched`
