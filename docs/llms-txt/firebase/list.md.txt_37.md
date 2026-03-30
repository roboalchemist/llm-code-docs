# Source: https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list.md.txt

# Method: projects.androidApps.deliveryData.list

- [HTTP request](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.request_body)
- [Response body](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.ListAndroidDeliveryDataResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#body.aspect)
- [AndroidDeliveryData](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData.SCHEMA_REPRESENTATION)
- [Date](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Date)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Date.SCHEMA_REPRESENTATION)
- [Data](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data.SCHEMA_REPRESENTATION)
- [MessageOutcomePercents](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageOutcomePercents)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageOutcomePercents.SCHEMA_REPRESENTATION)
- [DeliveryPerformancePercents](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#DeliveryPerformancePercents)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#DeliveryPerformancePercents.SCHEMA_REPRESENTATION)
- [MessageInsightPercents](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageInsightPercents)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageInsightPercents.SCHEMA_REPRESENTATION)
- [ProxyNotificationInsightPercents](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#ProxyNotificationInsightPercents)
  - [JSON representation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#ProxyNotificationInsightPercents.SCHEMA_REPRESENTATION)
- [Try it!](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#try-it)

List aggregate delivery data for the given Android application.

### HTTP request

`GET https://fcmdata.googleapis.com/v1beta1/{parent=projects/*/androidApps/*}/deliveryData`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `parent` | `string` Required. The application for which to list delivery data. Format: `projects/{projectId}/androidApps/{appId}` |

### Query parameters

| Parameters ||
|---|---|
| `pageSize` | `integer` The maximum number of entries to return. The service may return fewer than this value. If unspecified, at most 1,000 entries will be returned. The maximum value is 10,000; values above 10,000 will be capped to 10,000. This default may change over time. |
| `pageToken` | `string` A page token, received from a previous `ListAndroidDeliveryDataRequest` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAndroidDeliveryDataRequest` must match the call that provided the page token. |

### Request body

The request body must be empty.

### Response body

Response message for deliveryData.list.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "androidDeliveryData": [ { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData`) } ], "nextPageToken": string } ``` |

| Fields ||
|---|---|
| `androidDeliveryData[]` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData`)`` The delivery data for the provided app. There will be one entry per combination of app, date, and analytics label. |
| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

## AndroidDeliveryData

Message delivery data for a given date, app, and analytics label combination.

| JSON representation |
|---|
| ``` { "appId": string, "date": { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Date`) }, "analyticsLabel": string, "data": { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data`) } } ``` |

| Fields ||
|---|---|
| `appId` | `string` The app ID to which the messages were sent. |
| `date` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Date`)`` The date represented by this entry. |
| `analyticsLabel` | `string` The analytics label associated with the messages sent. All messages sent without an analytics label will be grouped together in a single entry. |
| `data` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data`)`` The data for the specified `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData.FIELDS.app_id`, `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData.FIELDS.date`, and `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#AndroidDeliveryData.FIELDS.analytics_label`. |

## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

- A full date, with non-zero year, month, and day values.
- A month and day, with a zero year (for example, an anniversary).
- A year on its own, with a zero month and a zero day.
- A year and month, with a zero day (for example, a credit card expiration date).

Related types:

- `google.type.TimeOfDay`
- `google.type.DateTime`
- `https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp`

| JSON representation |
|---|
| ``` { "year": integer, "month": integer, "day": integer } ``` |

| Fields ||
|---|---|
| `year` | `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. |
| `month` | `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. |
| `day` | `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant. |

## Data

Data detailing messaging delivery

| JSON representation |
|---|
| ``` { "countMessagesAccepted": string, "countNotificationsAccepted": string, "messageOutcomePercents": { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageOutcomePercents`) }, "deliveryPerformancePercents": { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#DeliveryPerformancePercents`) }, "messageInsightPercents": { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageInsightPercents`) }, "proxyNotificationInsightPercents": { object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#ProxyNotificationInsightPercents`) } } ``` |

| Fields ||
|---|---|
| `countMessagesAccepted` | `string (https://developers.google.com/discovery/v1/type-format format)` Count of messages accepted by FCM intended for Android devices. The targeted device must have opted in to the collection of usage and diagnostic information. |
| `countNotificationsAccepted` | `string (https://developers.google.com/discovery/v1/type-format format)` Count of notifications accepted by FCM intended for Android devices. The targeted device must have opted in to the collection of usage and diagnostic information. |
| `messageOutcomePercents` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageOutcomePercents`)`` Mutually exclusive breakdown of message delivery outcomes. |
| `deliveryPerformancePercents` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#DeliveryPerformancePercents`)`` Additional information about delivery performance for messages that were successfully delivered. |
| `messageInsightPercents` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#MessageInsightPercents`)`` Additional general insights about message delivery. |
| `proxyNotificationInsightPercents` | ``object (`https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#ProxyNotificationInsightPercents`)`` Additional insights about proxy notification delivery. |

## MessageOutcomePercents

Percentage breakdown of message delivery outcomes. These categories are mutually exclusive. All percentages are calculated with `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data.FIELDS.count_messages_accepted` as the denominator. These categories may not account for all message outcomes.

| JSON representation |
|---|
| ``` { "delivered": number, "pending": number, "collapsed": number, "droppedTooManyPendingMessages": number, "droppedAppForceStopped": number, "droppedDeviceInactive": number, "droppedTtlExpired": number } ``` |

| Fields ||
|---|---|
| `delivered` | `number` The percentage of all accepted messages that were successfully delivered to the device. |
| `pending` | `number` The percentage of messages accepted on this day that were not dropped and not delivered, due to the device being disconnected (as of the end of the America/Los_Angeles day when the message was sent to FCM). A portion of these messages will be delivered the next day when the device connects but others may be destined to devices that ultimately never reconnect. |
| `collapsed` | `number` The percentage of accepted messages that were [collapsed](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages) by another message. |
| `droppedTooManyPendingMessages` | `number` The percentage of accepted messages that were dropped due to [too many undelivered non-collapsible messages](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages). Specifically, each app instance can only have 100 pending messages stored on our servers for a device which is disconnected. When that device reconnects, those messages are delivered. When there are more than the maximum pending messages, we call [OnDeletedMessages()](https://firebase.google.com/docs/cloud-messaging/android/receive#override-ondeletedmessages) in our SDK instead of delivering the messages. |
| `droppedAppForceStopped` | `number` The percentage of accepted messages that were dropped because the application was force stopped on the device at the time of delivery and retries were unsuccessful. |
| `droppedDeviceInactive` | `number` The percentage of accepted messages that were dropped because the target device is inactive. FCM will drop messages if the target device is deemed inactive by our servers. If a device does reconnect, we call [OnDeletedMessages()](https://firebase.google.com/docs/cloud-messaging/android/receive#override-ondeletedmessages) in our SDK instead of delivering the messages. |
| `droppedTtlExpired` | `number` The percentage of accepted messages that expired because [Time To Live (TTL)](https://firebase.google.com/docs/cloud-messaging/concept-options#ttl) elapsed before the target device reconnected. |

## DeliveryPerformancePercents

Overview of delivery performance for messages that were successfully delivered. All percentages are calculated with `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data.FIELDS.count_messages_accepted` as the denominator. These categories are not mutually exclusive; a message can be delayed for multiple reasons.

| JSON representation |
|---|
| ``` { "deliveredNoDelay": number, "delayedDeviceOffline": number, "delayedDeviceDoze": number, "delayedMessageThrottled": number, "delayedUserStopped": number } ``` |

| Fields ||
|---|---|
| `deliveredNoDelay` | `number` The percentage of accepted messages that were delivered to the device without delay from the FCM system. |
| `delayedDeviceOffline` | `number` The percentage of accepted messages that were delayed because the target device was not connected at the time of sending. These messages were eventually delivered when the device reconnected. |
| `delayedDeviceDoze` | `number` The percentage of accepted messages that were delayed because the device was in doze mode. Only [normal priority messages](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) should be delayed due to doze mode. |
| `delayedMessageThrottled` | `number` The percentage of accepted messages that were delayed due to message throttling, such as [collapsible message throttling](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_throttling) or [maximum message rate throttling](https://firebase.google.com/docs/cloud-messaging/concept-options#device_throttling). |
| `delayedUserStopped` | `number` The percentage of accepted messages that were delayed because the intended device user-profile was [stopped](https://firebase.google.com/docs/cloud-messaging/android/receive#handling_messages) on the target device at the time of the send. The messages were eventually delivered when the user-profile was started again. |

## MessageInsightPercents

Additional information about message delivery. All percentages are calculated with `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data.FIELDS.count_messages_accepted` as the denominator.

| JSON representation |
|---|
| ``` { "priorityLowered": number } ``` |

| Fields ||
|---|---|
| `priorityLowered` | `number` The percentage of accepted messages that had their priority lowered from high to normal. See [documentation for setting message priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority). |

## ProxyNotificationInsightPercents

Additional information about [proxy notification](https://firebase.google.com/docs/cloud-messaging/android/message-priority#proxy) delivery. All percentages are calculated with `https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#Data.FIELDS.count_notifications_accepted` as the denominator.

| JSON representation |
|---|
| ``` { "proxied": number, "failed": number, "skippedUnsupported": number, "skippedNotThrottled": number, "skippedUnconfigured": number, "skippedOptedOut": number } ``` |

| Fields ||
|---|---|
| `proxied` | `number` The percentage of accepted notifications that were successfully proxied by [Google Play services](https://developers.google.com/android/guides/overview). |
| `failed` | `number` The percentage of accepted notifications that failed to be proxied. This is usually caused by exceptions that occurred while calling [notifyAsPackage](https://developer.android.com/reference/android/app/NotificationManager#notifyAsPackage%28java.lang.String,%20java.lang.String,%20int,%20android.app.Notification%29). |
| `skippedUnsupported` | `number` The percentage of accepted notifications that were skipped because proxy notification is unsupported for the recipient. |
| `skippedNotThrottled` | `number` The percentage of accepted notifications that were skipped because the messages were not throttled. |
| `skippedUnconfigured` | `number` The percentage of accepted notifications that were skipped because configurations required for notifications to be proxied were missing. |
| `skippedOptedOut` | `number` The percentage of accepted notifications that were skipped because the app disallowed these messages to be proxied. |