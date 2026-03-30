# Source: https://documentation.onesignal.com/docs/en/segmentation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Segments

> Create and manage dynamic user segments in OneSignal to target personalized messaging based on activity, location, tags, and more.

A segment is a dynamic audience that groups [Subscriptions](./subscriptions) or [Users](./users) based on filters like activity, country, [Tags](./add-user-data-tags), message activity, and more. Segments help you send personalized, timely, and relevant messages.

Once created, segments update automatically as users interact with your app or site—no extra tracking required.

<Warning>
  Segment counts only reflect *opted-in* Push, SMS, and Email [subscriptions](./subscriptions).

  When used in Journeys or In-App Messages, segments include [users](./users) and opted-out subscriptions.

  To analyze unsubscribed subscriptions, use the [Export CSV of Players](/reference/csv-export) API.
</Warning>

***

## Segment types

The OneSignal platform supports two main categories of segments:

#### Subscription-based Segments

Subscription-based segments are built using filters on subscription attributes, such as device type, language, or app version, etc.
Historically, all segments created on the OneSignal platform have been subscription-based.

#### User-based Segments

User-based segments are built using filters on user-level attributes rather than individual subscriptions.
Currently, these segments support filters on message events and custom events. Examples include:

* When a user last opened an email, SMS, or push notification sent via OneSignal.
* Specific custom events tracked in your app or website.

A user-based segment includes all users who meet the criteria and automatically make all of their subscriptions eligible to be targeted, enabling richer audience definitions that can reach any of the user’s devices.

***

## Creating segments

You can create segments in three ways:

* From the **Dashboard**
* Via the [Create Segment API](/reference/create-segments)
* By uploading a CSV. See our [Import](./import) guide for details.

### Create a segment in the dashboard

1. Go to **Audience > Segments**
2. Click **New Segment**
3. Add filters, name the segment, and click **Create Segment**

<Frame caption="New Segment creation interface">
  <img src="https://mintcdn.com/onesignal/anhp0o--bcksJgNR/images/segments/segments-tab.png?fit=max&auto=format&n=anhp0o--bcksJgNR&q=85&s=1838cce365a48e51d1fd738a2a0fb52c" width="2536" height="1646" data-path="images/segments/segments-tab.png" />
</Frame>

### Exclude segments

Exclude a segment to prevent its members from receiving a message or entering a Journey.

Common use cases:

* Avoid sending duplicate or conflicting messages
* Respect user messaging preferences (e.g., "opted out of promo")
* Prioritize transactional messages over campaigns

You can exclude segments when:

* Sending a message
* Building a Journey
* Using the **Exclude Segment** option in segment settings

***

## Filters

Filters define which subscriptions belong to a segment. You can combine multiple filters using **AND** or **OR** logic.

| Filter             | Description                                                                                                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First session**  | Date/time of user creation.                                                                                                                                                                                                                                    |
| **Last session**   | Last time Subscription opened the app or site.                                                                                                                                                                                                                 |
| **Session count**  | Number of times Subscription opened the app or visited the site.                                                                                                                                                                                               |
| **Usage duration** | Total seconds the Subscription had your app/site open.                                                                                                                                                                                                         |
| **Language**       | User's preferred language (based on device/browser). See [multi-language support](./multi-language-messaging).                                                                                                                                                 |
| **App version**    | Pulled from Android `versionCode` or iOS `CFBundleShortVersionString`. <br />- Combine with **Device type** to filter by different app versions for each platform. <br />- See [Target outdated app versions tutorial](./app-version-update) for more details. |
| **Device type**    | iOS, Android, Web Push (browser), Email, etc.                                                                                                                                                                                                                  |
| **User tag**       | Custom tags you set via the SDK or API. See [Add User Tags](./add-user-data-tags).                                                                                                                                                                             |
| **Location**       | Filter by radius from coordinates (lat/long). Requires at least 1 meter and up to 2 decimal places of precision. See [location permission](./mobile-sdk-reference#location).                                                                                   |
| **Country**        | Based on last IP geolocation (ISO 3166-2 code).                                                                                                                                                                                                                |
| **Test users**     | Users marked as [Test Users](./users).                                                                                                                                                                                                                         |
| **Rooted**         | Android only — whether device is rooted.                                                                                                                                                                                                                       |
| **Message Event**  | Filter by message event (e.g., "clicked", "delivered", "failed"). See [Message event filters](#message-event-filters).                                                                                                                                         |
| **Custom Event**   | Filter by custom event (e.g., "purchase", "user login"). See [Custom event filters](#custom-event-filters).                                                                                                                                                    |

<Frame caption="Segment filters configuration screen">
  <img src="https://mintcdn.com/onesignal/anhp0o--bcksJgNR/images/segments/segment-editor.png?fit=max&auto=format&n=anhp0o--bcksJgNR&q=85&s=a7681afc862e8c3b7f848c8e26731c02" width="1418" height="694" data-path="images/segments/segment-editor.png" />
</Frame>

### Message event filters

Message event filters allow you to filter users based on their interaction with one of your messaging channels within a certain window.

<Frame caption="Message event filters">
  <img src="https://mintcdn.com/onesignal/anhp0o--bcksJgNR/images/segments/message_event_filters.png?fit=max&auto=format&n=anhp0o--bcksJgNR&q=85&s=acb0fc98a44ef1a5392e3781d8ae66c8" width="1418" height="950" data-path="images/segments/message_event_filters.png" />
</Frame>

First select the messaging channel you want to filter on, then specify the action that you want to track for that channel and whether the user has or has not performed that action.

You can specify a minimum, maximum, or exact number of time the user must have performed the action in order to qualify, as well as a time window ranging from the last 24 hour to the last 90 days in which they must have performed or not performed the action.

You can also specify a custom time window by using the `between` option, which allows you to define a start and end range (in days ago) for when the event may have occurred.

See below for a list of available trackable interactions for each channel:

| Channel |                              Trackable Interactions                             |
| :-----: | :-----------------------------------------------------------------------------: |
|   Push  |                         Sent, Received, Clicked, Failed                         |
|   SMS   |                             Sent, Delivered, Failed                             |
|  Email  | Sent, Delivered, Opened, Clicked, Bounced, Failed, Suppressed, Reported as spam |
|  In-App |                                Received, Clicked                                |

<Warning>
  Segments created with message event filters are user-based. Because of this, they cannot be combined with subscription-based segments (those that don’t use message event filters) for inclusion or exclusion when sending messages outside of Journeys.

  However, within [Journeys](./journeys-overview) which is user-based, you can combine event-based segments with subscription-based segments. This allows for more flexible targeting in automated messaging flows.
</Warning>

### Custom event filters

[Custom event](./custom-events) filters let you target users based on meaningful actions they have taken in your app, website, or external systems.

<Note>
  Custom events filters are currently in **Early Access**.

  To request access, contact `support@onesignal.com` with:

* your company name
* your OneSignal Organization ID
* your OneSignal App ID(s) that you want to use the feature on
</Note>

<Frame caption="Custom event filters">
  <img src="https://mintcdn.com/onesignal/F6bmHbMOfl8CCgqr/images/segments/custom_event_filters.png?fit=max&auto=format&n=F6bmHbMOfl8CCgqr&q=85&s=02889ac9e9edc4ef01a740e962814f89" width="1852" height="1318" data-path="images/segments/custom_event_filters.png" />
</Frame>

#### How They Work

Start by selecting the event type you want to filter on. Then specify:

* The action that you want to track.
* Whether the user `has` or `has not` performed that action.

You can also set conditions such as:

* Minimum, maximum, or exact number of times the action must be performed.
* A time window during which the action must (or must not) occur. You can either choose a preset range or define a custom window using the `between` option, which lets you specify a start and end range (in days ago).

#### Event Properties

After selecting an event type, you can optionally filter on event properties. You can include filters on multiple custom event properties,

* Choose `all`, applies an AND condition across properties.
* Choose `at least one`, applies an OR condition.

Custom events are represented as [JSON Objects](https://www.w3schools.com/js/js_json.asp). [See the full structure here](./custom-events#what-is-a-custom-event%3F).

Nested event properties can be referenced using `dot notation`.

**Example**

Given the following custom event structure,

```
{
  "signup": {
    "method": "google",
    "experiment_group": "control_group",
    "referral_code": "SAVE15",
    "location": {
      "timezone": "Europe/Paris",
      "country": "CA"
    },
    metadata: {
      "labels": ["red", "green", "blue"]
    }
  },
  "user_id": "user_804f7e88"
}
```

You can filter by:

* `signup.referral_code` → to target users with referral code `SAVE15`.
* `signup.location.country` → to target users in `Canada`.
* `metadata.labels.0` → to target users with label `red`.

<Warning>
  Segments created with custom event filters are in Early Access. Because of this,

* a custom event segment can only contain custom event filter, and cannot be combined with other segments for inclusion or exclusion when sending messages.
</Warning>

<Warning>
  Segments created with custom event filters are user-based.
</Warning>

### Segment logic: AND vs OR

Use **AND** to combine filters that *all* must match. Use **OR** to match *any* of multiple conditions.

#### AND filter example

Create a segment of users who:

* Have not returned in more than 7 days
* Will be removed after 11 days

<Frame caption="Inactive segment filter setup">
  <img src="https://mintcdn.com/onesignal/anhp0o--bcksJgNR/images/segments/and-filter-example.png?fit=max&auto=format&n=anhp0o--bcksJgNR&q=85&s=605ba0427b200b9b04ec8fd54ce115f1" width="1418" height="792" data-path="images/segments/and-filter-example.png" />
</Frame>

#### OR filter example

Create a segment of users who:

* Have not returned in more than 7 days
* Have new Subscriptions created in the last 3 days

<Frame caption="OR clause segment configuration">
  <img src="https://mintcdn.com/onesignal/anhp0o--bcksJgNR/images/segments/or-filter-example.png?fit=max&auto=format&n=anhp0o--bcksJgNR&q=85&s=519088174843b2edbac2a2b2d0073cab" width="1418" height="958" data-path="images/segments/or-filter-example.png" />
</Frame>

***

## Managing segments

### View users

Click **Options > View Users** to see which [subscriptions](./subscriptions) are in the segment.

### Edit

Click the segment name or **Options > Edit** to change filters.

### Pause / Resume

If you're near your segment limit (based on [your plan](https://onesignal.com/pricing)), you can pause segments. Targeting a paused segment will fail.

### Set as default

Set a default segment to be auto-selected when sending a new message. This helps reduce targeting mistakes and save time.

### Duplicate

Copy a segment's filters to create a new one.

***

## Deleting segments

<Warning>
  Deleting a segment cannot be undone and does **not** delete the users inside it.
</Warning>

### In the dashboard

1. Go to **Audience > Segments**
2. Click the three-dot menu next to a segment
3. Select **Delete**

<Frame caption="Segment options menu">
  <img src="https://mintcdn.com/onesignal/anhp0o--bcksJgNR/images/segments/segment-menu.png?fit=max&auto=format&n=anhp0o--bcksJgNR&q=85&s=e2a74b94e0acdd572faf9ac398d7b267" width="1788" height="782" data-path="images/segments/segment-menu.png" />
</Frame>

***

### Using the API

Use the [Delete Segment API](/reference/delete-segments). Only removes the segment definition.

To delete users in the segment, use the [Delete Users](./delete-users) API.

```json  theme={null}
{
  "name": "Segment 2",
  "filters": [
    { "field": "session_count", "relation": ">", "value": "1" },
    { "operator": "AND" },
    { "field": "tag", "relation": "!=", "key": "tag_key", "value": "1" },
    { "operator": "OR" },
    { "field": "last_session", "relation": "<", "hours_ago": "30" }
  ]
}
```

***

## FAQ

### How do I add myself to a segment?

1. Find your Subscriptions using your [External ID](./users).
2. Either:

* Set yourself as a [Test user](./find-set-test-subscriptions)
* Add a custom [Tag](./add-user-data-tags)

1. Create a segment using the **Test Users** filter or the tag.

### Do segment counts include opted-out users?

* Visible counts only include opted-in subscriptions.
* Segments used in Journeys and in-app messages include both subscribed and unsubscribed subscriptions.
* To see unsubscribed subscriptions, use the [Export CSV of Players](/reference/csv-export) API.

### Are segment counts always accurate?

Segments larger than 80,000 total users may have an estimated size, instead of a precise count, in order to calculate them quickly. To get the most accurate numbers, see the message report stats after sending the message.

### What types of in-app purchases are tracked?

* Tracked: Consumable purchases made while the OneSignal SDK is active.
* Not tracked: Subscription purchases.
* To import historical purchase data, use the Update User API with the purchases parameter.

***

Built with [Mintlify](https://mintlify.com).
