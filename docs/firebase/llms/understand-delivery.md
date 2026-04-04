# Source: https://firebase.google.com/docs/cloud-messaging/understand-delivery.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery.md.txt

# Understanding message delivery

<br />

For troubleshooting ongoing message delivery failures, use the
**[FCM troubleshooter](https://firebase.google.com/support/troubleshooter/fcm)** and see this
**[blog post](https://firebase.blog/posts/2024/07/understand-fcm-delivery-rates/)**
to understand the different reasons why you may not see your message. You can
also visit the **[FCM status dashboard](https://status.firebase.google.com/cloud-messaging/)**
to identify if there are any ongoing service disruptions affecting FCM.

FCM also provides three sets of tools to help you get insight into broad
evaluation of messaging success and strategy:

- Firebase console message delivery reports
- Aggregated Android SDK delivery metrics from the Firebase Cloud Messaging Data API
- Comprehensive data export to Google BigQuery

[BigQuery data export](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#bigquery-data-export) and the
[Reports](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#message-delivery-reports) tab in the Firebase console require
Google Analytics in order to function. If Google Analytics is not
enabled for your project, you can set it up in the
[integrations](https://console.firebase.google.com/project/_/settings/integrations)
tab of your Firebase project settings. [Aggregated Delivery Data](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#aggregated-delivery-data) does not require Google Analytics to function.

Keep in mind that the reporting of many of the statistics on this page,
are subject to delays up to 24 hours due to batching of analytics data.

## Message delivery reports

In the
[Reports](https://console.firebase.google.com/project/_/messaging/reports)
tab in the Firebase console, you can view the
following data for messages sent to Android or Apple platform FCM SDKs,
including those sent via the Notifications composer and the FCM APIs:

- Sends --- The data message or notification message has been enqueued for delivery or has been successfully passed to a third-party service like APNs for delivery. Note that Sends statistics might lag for a couple of hours. See [lifetime of a message](https://firebase.google.com/docs/cloud-messaging/concept-options#lifetime) for more information.
- Received (available only on Android devices) --- The data message or notification message has been received by the app. This data is available when the receiving Android device has FCM SDK 18.0.1 or higher installed.
- Impressions (available only for notification messages on Android devices) --- The display notification has been displayed on the device while the app is in the background.
- Opens --- The user opened the notification message. Reported only for notifications received when the app is in the background.

This data is available for all messages with a notification payload
and all **labeled**
[data messages](https://firebase.google.com/docs/cloud-messaging/concept-options#data_messages).
To learn more about labels, see
[Adding analytics labels to messages](https://firebase.google.com/docs/cloud-messaging/understand-delivery#adding-analytics-labels-to-messages).

When viewing message reports, you can set a date range for the data displayed,
with the option to export to CSV. You can also filter by these criteria:

- Platform (iOS or Android)
- App
- Custom analytics labels

### Adding analytics labels to messages

Labeling messages is very useful for custom analysis, allowing you to
filter delivery statistics by labels or sets of labels. You can add a
label to any message sent via the HTTP v1 API by setting
the `fcmOptions.analyticsLabel` field in the
[message](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages) object, or in the
platform-specific `AndroidFcmOptions` or `ApnsFcmOptions` fields.
| **Important:** To use this feature, you must include the Analytics SDK in your app and enable [data sharing](https://support.google.com/firebase/answer/6383877) with Firebase. An analytics label is required to display all types of statistics for data messages.

Analytics labels are text strings in the format `^[a-zA-Z0-9-_.~%]{1,50}$`.
Labels can include lower and upper case letters,
numbers, and the following symbols:

- `-`
- `~`
- `%`

Max length is 50 characters. You can specify up to 100 unique labels per day;
messages with labels added beyond that limit are not reported.

In the Firebase console messaging **Reports** tab, you can search a
list of all existing labels and apply them singly or in combination to filter
the statistics displayed.

## Aggregated delivery data using the FCM Data API

The Firebase Cloud Messaging Data API lets you retrieve information that can
help you understand the outcomes of message requests targeted to Android
applications. The API provides aggregated data across all data
collection-enabled Android devices in a project. This includes details on
the percentage of messages delivered
without delay as well as how many messages were delayed or dropped within the
[Android Transport Layer](https://firebase.google.com/docs/cloud-messaging/fcm-architecture).
Evaluating this data can reveal broad trends in message delivery and help you
find effective ways to improve the performance of your send requests. See [Aggregate data timelines](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#aggregate-data-timelines) for information on date range availability in the reports.

The API provides all data available for a given application. See the
[API reference documentation](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData).

### How is the data broken down?

Delivery data is broken down by application, date, and [analytics label](https://firebase.google.com/docs/cloud-messaging/understand-delivery#adding-analytics-labels-to-messages).
A call to the API will return
data for every combination of date, application, and analytics label. For
example, a single `androidDeliveryData` JSON object would look like this:  

     {
      "appId": "1:23456789:android:a93a5mb1234efe56",
      "date": {
        "year": 2021,
        "month": 1,
        "day": 1
      },
      "analyticsLabel": "foo",
      "data": {
        "countMessagesAccepted": "314159",
        "messageOutcomePercents": {
          "delivered": 71,
          "pending": 15
        },
       "deliveryPerformancePercents": {
          "deliveredNoDelay": 45,
          "delayedDeviceOffline": 11
        }
      }

### How to Interpret the Metrics

Delivery data outlines the percentage of messages that fit each of the following
metrics. It is possible that a single message fits multiple metrics.
Due to limitations in how we collect the data and
the level of granularity at which we aggregated the metrics,
**some message outcomes are not represented in the metrics at all,
so the percentages below will not sum to 100%.**

#### Count Messages Accepted

The only count included in the dataset is the count of messages that were
accepted by FCM for delivery to Android devices. All percentages use this value
as the denominator. Keep in mind that this count won't include messages
targeted to users who have
disabled the collection of usage and diagnostic information on
their devices.

#### Message Outcome Percentages

The fields included in the
[`MessageOutcomePercents`](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#messageoutcomepercents)
object provide information on the
outcomes of message requests. The categories are all mutually exclusive. It can
answer questions such as "Are my messages being delivered?" and "What is causing
messages to be dropped?"

For example, a high value for the `droppedTooManyPendingMessages` field could
signal that app instances are receiving volumes of
[non-collapsible messages](https://firebase.google.com/docs/cloud-messaging/concept-options#collapsible_and_non-collapsible_messages)
exceeding FCM's limit of 100 pending messages.
To mitigate this, make sure your app handles calls to
[`onDeletedMessages`](https://firebase.google.com/docs/cloud-messaging/android/receive#override-ondeletedmessages),
and consider sending collapsible messages. Similarly, high percentages for
`droppedDeviceInactive` could be a signal to update registration tokens on your
server, removing stale tokens and unsubscribing them from topics. See
[Manage FCM registration tokens](https://firebase.google.com/docs/cloud-messaging/manage-tokens)
for best practices in this area.

#### Delivery Performance Percents

The fields in the [`DeliveryPerformancePercents`](https://firebase.google.com/docs/reference/fcmdata/rest/v1beta1/projects.androidApps.deliveryData/list#deliveryperformancepercents)
object provide information about messages that were successfully delivered. It
can answer questions such as "Were my messages delayed?" and
"Why are messages delayed?" For example, a high value for
`delayedMessageThrottled` would clearly indicate that you are exceeding
[per-device maximum limits](https://firebase.google.com/docs/cloud-messaging/concept-options#device_throttling),
and should adjust the rate at which you are sending messages.

#### Message Insight Percentagess

This object provides additional information about all message sends. The
`priorityLowered` field expresses the percentage of accepted messages that
had priority lowered from `HIGH` to `NORMAL`. If this value is high, try sending fewer high priority messages or ensure that
you always display a notification when a high priority message is sent. See [our documentation on message priority for more info](https://firebase.google.com/docs/cloud-messaging/android/message-priority)

### How does this data differ from data exported to BigQuery?

The BigQuery export provides individual message logs about message acceptance by
the FCM backend and message delivery in the SDK on the device (Steps 2 and 4 of
the [FCM Architecture](https://firebase.google.com/docs/cloud-messaging/fcm-architecture)). This data is useful for ensuring individual messages were
accepted and delivered. Read more about
[BigQuery data export](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#bigquery-data-export) in the next section.

By contrast, the Firebase Cloud Messaging Data API provides aggregated details
about what happens specifically in the Android Transport Layer (or Step 3 of
the [FCM Architecture](https://firebase.google.com/docs/cloud-messaging/fcm-architecture)).
This data specifically provides insight into the delivery of
messages from FCM backends to the Android SDK. It's particularly useful for
showing trends as to why messages were delayed or dropped during this transport.

In some cases, it is possible that the two data sets might not match precisely
due to the following:

- The aggregated metrics only sample a portion of all messages
- The aggregated metrics are rounded
- We don't present metrics below a privacy threshold
- A portion of message outcomes are missing due to optimizations in how we manage the large volume of traffic.

### Limitations of the API

#### Aggregate Data Timelines

The API will return 7 days of historical data; however, data returned by this API will be delayed by up to 5 days. For example, on
January 20th, the data for January 9th - January 15th would be available, but not for January
16th or later. Additionally, the data is provided at best effort. In the event of
a data outage, FCM will work to fix forward and will not backfill the data after
the issue is fixed. In larger outages, the data could be unavailable for a week
or more.

#### Data Coverage

The metrics provided by the Firebase Cloud Messaging Data API are meant to
provide insight into broad trends of message delivery. However, they do not
provide 100% coverage of all message scenarios. The following scenarios are
known outcomes not reflected in the metrics.

**Expired messages**

If the [Time To Live (TTL)](https://firebase.google.com/docs/cloud-messaging/concept-options#ttl) expires
after the end of the given log date, the message won't be counted as
`droppedTtlExpired` on this date.

**Messages to inactive devices**

Messages sent to inactive devices may or may not show up in the dataset
depending on which data path they take. This can lead to some miscounting in the
`droppedDeviceInactive` and `pending` fields.

**Messages to devices with certain user preferences**

Users who have disabled the collection of usage and diagnostic information on
their devices will not have their messages included in our counting, in keeping
with their preferences.

#### Rounding and Minimums

FCM deliberately rounds and excludes counts where the volumes are not large
enough.

## BigQuery data export

You can export your message data into
[BigQuery](https://bigquery.cloud.google.com/) for further analysis. BigQuery
allows you to analyze the data using BigQuery SQL, export it to another cloud
provider, or use the data for your custom ML models. An export to BigQuery
includes all available data for messages, regardless of
message type or whether the message is sent via the API or
the Notifications composer.

For messages sent to devices with the following FCM SDK minimum
versions, you have the additional option to enable the export of message
delivery data for your app:

- Android 20.1.0 or higher.
- iOS 8.6.0 or higher
- Firebase Web SDK 9.0.0 or higher

See below for details on enabling data export for
[Android](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#enable-message-delivery-data-export-on-android) and
[iOS](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#enable-message-delivery-data-export-on-ios).
| **Note:** Make sure that you have the [required level of access](https://firebase.google.com/docs/projects/bigquery-export#permissions-and-roles) to view or manage settings for data export to BigQuery.

To get started, link your project to BigQuery:

1. Choose one of the following options:

   - Open
     [the Notifications composer](https://console.firebase.google.com/project/_/notification),
     then click **Access BigQuery** at the bottom of the page.

   - From the
     [Integrations](https://console.firebase.google.com/project/_/settings/integrations)
     page in the Firebase console, click **Link** in the **BigQuery**
     card.

     This page displays FCM export options for all
     FCM-enabled apps in the project.
2. Follow the on-screen instructions to enable BigQuery.

Refer to [Link Firebase to BigQuery](https://support.google.com/firebase/answer/6318765)
for more information.

When you enable BigQuery export for Cloud Messaging:

- Firebase [exports your data](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#what-data-exported) to BigQuery. Note
  that the initial propagation of data for export may take up to 48 hours to
  complete.

  - You can [manually schedule data backfills](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer) for up to the past 30 days.
- After the dataset is created, the location
  can't be changed, but you can copy the dataset to a different location
  or manually move (recreate) the dataset in a different location. To learn
  more, see [Change dataset location](https://firebase.google.com/docs/projects/bigquery-export?product=messaging#change-dataset-location).

- Firebase sets up regular syncs of your data from your Firebase project to
  BigQuery. These daily export operations begin at 4:00 AM Pacific Time
  and usually finish in 24 hours.

- By default, all apps in your project are linked to BigQuery and any
  apps that you later add to the project are automatically linked to
  BigQuery. You can
  [manage which apps send data](https://support.google.com/firebase/answer/6318765#manage).

To deactivate BigQuery export,
[unlink your project](https://support.google.com/firebase/answer/6318765#unlink)
in the Firebase console.
| **Note:** There is no charge for exporting data from FCM, and BigQuery provides generous no-cost usage limits. Refer to [BigQuery pricing](https://cloud.google.com/bigquery/pricing) or the [BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox).

### Enable message delivery data export

iOS Android Web  

iOS devices with the FCM SDK 8.6.0 or higher
can enable their app's message delivery data export. FCM
supports data export for both alert and background notifications.
Before enabling these options, you must first create the
FCM-BiqQuery link for your project as described in
[BigQuery data export](https://firebase.google.com/docs/cloud-messaging/doc-revamp/optimize-delivery/understand-delivery#bigquery-data-export).

#### Enable delivery data export for alert notifications

Because only alert notifications can trigger notification service app
extensions, you must add a notification service extension to your app and call
this API inside a service extension to enable display message tracking. See
Apple's documentation on [Modifying Content in Newly Delivered Notifications](https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications?language=objc).

The following call must be made for every notification received:  

### Swift

    // For alert notifications, call the API inside the service extension:
    class NotificationService: UNNotificationServiceExtension {
      override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
      Messaging.extensionHelper()
          .exportDeliveryMetricsToBigQuery(withMessageInfo:request.content.userInfo)
      }
    }

### Objective-C

    // For alert notifications, call the API inside the service extension:
    @implementation NotificationService
    - (void)didReceiveNotificationRequest:(UNNotificationRequest *)request
                       withContentHandler:(void (^)(UNNotificationContent *_Nonnull))contentHandler {
      [[FIRMessaging extensionHelper] exportDeliveryMetricsToBigQueryWithMessageInfo:request.content.userInfo];
    }
    @end

If you are building send requests using the HTTP v1 API, make sure to
specify `mutable-content = 1` in the
[payload object](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsConfig).

#### Enable delivery data export for background notifications

For background messages received when the app is in the foreground or background,
you can call the data export API inside the main app's data message handler.
This call must be made for every notification received:  

### Swift

    // For background notifications, call the API inside the UIApplicationDelegate or NSApplicationDelegate method:
    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any]) {
      Messaging.extensionHelper().exportDeliveryMetricsToBigQuery(withMessageInfo:userInfo)
    }

### Objective-C

    // For background notifications, call the API inside the UIApplicationDelegate or NSApplicationDelegate method:
    @implementation AppDelegate
    - (void)application:(UIApplication *)application
        didReceiveRemoteNotification:(NSDictionary *)userInfo
              fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
      [[FIRMessaging extensionHelper] exportDeliveryMetricsToBigQueryWithMessageInfo:userInfo];
    }
    @end

### What data is exported to BigQuery?

Note that targeting stale tokens or inactive registrations may inflate some of
these statistics.

The schema of the exported table is:

|-----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _PARTITIONTIME  | TIMESTAMP | This pseudo column contains a timestamp for the start of the day (in UTC) in which the data was loaded. For the YYYYMMDD partition, this pseudo column contains the value TIMESTAMP('YYYY-MM-DD').                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| event_timestamp | TIMESTAMP | Event timestamp as recorded by the server                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| project_number  | INTEGER   | The project number identifies the project that sent the message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| message_id      | STRING    | The message ID identifies a message. Generated from the App ID and timestamp, the message ID might, in some cases, not be globally unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| instance_id     | STRING    | The unique id of the app the message is sent to (when available). It can be an instance ID or an Firebase installation ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| message_type    | STRING    | The type of the message. Can be Notification message or Data message. Topic is used to identify the original message for a topic or campaign send; the subsequent messages is either a notification or data message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| sdk_platform    | STRING    | The platform of the recipient app                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| app_name        | STRING    | The package name for Android apps or the bundle id for iOS apps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| collapse_key    | STRING    | The collapse key identifies a group of messages that can be collapsed. When a device is not connected, only the last message with a given collapse key is queued for eventual delivery                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| priority        | INTEGER   | The priority of the message. Valid values are "normal" and "high." On iOS, these correspond to APNs priorities 5 and 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ttl             | INTEGER   | This parameter specifies how long (in seconds) the message should be kept in FCM storage if the device is offline                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| topic           | STRING    | The name of the topic to which a message was sent (when applicable)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| bulk_id         | INTEGER   | The bulk ID identifies a group of related messages, such as a particular send to a topic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| event           | STRING    | The type of the event. Possible values are: - MESSAGE_ACCEPTED: the message was received by the FCM server and the request is valid; - MESSAGE_DELIVERED: the message has been delivered to the app's FCM SDK on the device. By default, this field is not propagated. To enable, follow the instructions provided in [`setDeliveryMetricsExportToBigQuery(boolean)`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#public-void-setdeliverymetricsexporttobigquery-boolean-enable). - MISSING_REGISTRATIONS: the request was rejected due to a missing registration; - UNAUTHORIZED_REGISTRATION: the message was rejected because the sender is not authorized to send to the registration; - MESSAGE_RECEIVED_INTERNAL_ERROR: there was an unspecified error when processing the message request; - MISMATCH_SENDER_ID: the request to send a message was rejected due to a mismatch between the sender id sending the message, and the one declared for the end-point; - QUOTA_EXCEEDED: the request to send a message was rejected due to insufficient quota; - INVALID_REGISTRATION: the request to send a message was rejected due to an invalid registration; - INVALID_PACKAGE_NAME: the request to send a message was rejected due to an invalid package name; - INVALID_APNS_CREDENTIAL: the request to send a message was rejected due to an invalid APNS certificate; - INVALID_PARAMETERS: the request to send a message was rejected due to invalid parameters; - PAYLOAD_TOO_LARGE: the request to send a message was rejected due to a payload larger than the limit; - AUTHENTICATION_ERROR: the request to send a message was rejected due to an authentication error (check the API Key used to send the message); - INVALID_TTL: the request to send a message was rejected due to an invalid TTL. |
| analytics_label | STRING    | With the [HTTP v1 API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages), the analytics label can be set when sending the message, in order to mark the message for analytics purposes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## What can you do with the exported data?

The following sections offer examples of queries that you can run in BigQuery
against your exported FCM data.

### Count sent messages by app

```scdoc
SELECT app_name, COUNT(1)
FROM `<var translate="no">project ID</var>.firebase_messaging.data`
WHERE
  _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
  AND event = 'MESSAGE_ACCEPTED'
  AND message_id != ''
GROUP BY 1;
```

### Count unique app instances targeted by messages

```scdoc
SELECT COUNT(DISTINCT instance_id)
FROM `<var translate="no">project ID</var>.firebase_messaging.data`
WHERE
  _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
  AND event = 'MESSAGE_ACCEPTED';
```

### Count notification messages sent

```scdoc
SELECT COUNT(1)
FROM `<var translate="no">project ID</var>.firebase_messaging.data`
WHERE
  _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
  AND event = 'MESSAGE_ACCEPTED'
  AND message_type = 'DISPLAY_NOTIFICATION';
```

### Count data messages sent

```scdoc
SELECT COUNT(1)
FROM `<var translate="no">project ID</var>.firebase_messaging.data`
WHERE
  _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
  AND event = 'MESSAGE_ACCEPTED'
  AND message_type = 'DATA_MESSAGE';
```

### Count messages sent to a topic or campaign

```scdoc
SELECT COUNT(1)
FROM `<var translate="no">project ID</var>.firebase_messaging.data`
WHERE
  _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
  AND event = 'MESSAGE_ACCEPTED'
  AND bulk_id = your bulk id AND message_id != '';
```

To track events for a message sent to particular topic, modify this query to
replace `AND message_id != ''` with `AND message_id = <your message id>;`.

### Compute fanout duration for a given topic or campaign

The fanout start time is when the original request is received, and the end
time is the time the last individual message targeting a single instance
is created.  

```carbon
SELECT
  TIMESTAMP_DIFF(
    end_timestamp, start_timestamp, MILLISECOND
  ) AS fanout_duration_ms,
  end_timestamp,
  start_timestamp
FROM (
    SELECT MAX(event_timestamp) AS end_timestamp
    FROM `project ID.firebase_messaging.data`
    WHERE
      _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
      AND event = 'MESSAGE_ACCEPTED'
      AND bulk_id = your bulk id
  ) sent
  CROSS JOIN (
    SELECT event_timestamp AS start_timestamp
    FROM `project ID.firebase_messaging.data`
    WHERE
      _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
      AND event = 'MESSAGE_ACCEPTED'
      AND bulk_id = your bulk id
      AND message_type = 'TOPIC'
  ) initial_message;
```

### Count percentage of delivered messages

```googlesql
SELECT
  messages_sent,
  messages_delivered,
  messages_delivered / messages_sent * 100 AS percent_delivered
FROM (
    SELECT COUNT(DISTINCT CONCAT(message_id, instance_id)) AS messages_sent
    FROM `<var translate="no">project ID</var>.firebase_messaging.data`
    WHERE
      _PARTITIONTIME = TIMESTAMP('<var translate="no">date as YYYY-MM-DD</var>')
      AND event = 'MESSAGE_ACCEPTED'
  ) sent
  CROSS JOIN (
    SELECT COUNT(DISTINCT CONCAT(message_id, instance_id)) AS messages_delivered
    FROM `<var translate="no">project ID</var>.firebase_messaging.data`
    WHERE
      _PARTITIONTIME = TIMESTAMP('<var translate="no">date as YYYY-MM-DD</var>')
      AND (event = 'MESSAGE_DELIVERED'
      AND message_id
      IN (
        SELECT message_id FROM `<var translate="no">project ID</var>.firebase_messaging.data`
        WHERE
          _PARTITIONTIME = TIMESTAMP('<var translate="no">date as YYYY-MM-DD</var>')
          AND event = 'MESSAGE_ACCEPTED'
        GROUP BY 1
      )
  ) delivered;
```

### Track all events for a given message id and instance id

```scdoc
SELECT *
FROM `<var translate="no">project ID</var>.firebase_messaging.data`
WHERE
    _PARTITIONTIME = TIMESTAMP('date as YYYY-MM-DD')
    AND message_id = 'your message id'
    AND instance_id = 'your instance id'
ORDER BY event_timestamp;
```

### Compute latency for a given message id and instance id

```googlesql
SELECT
  TIMESTAMP_DIFF(
    MAX(delivered_time), MIN(accepted_time), MILLISECOND
  ) AS latency_ms
FROM (
    SELECT event_timestamp AS accepted_time
    FROM `<var translate="no">project ID</var>.firebase_messaging.data`
    WHERE
      _PARTITIONTIME = TIMESTAMP('<var translate="no">date as YYYY-MM-DD</var>')
      AND message_id = '<var translate="no">your message id</var>'
      AND instance_id = '<var translate="no">your instance id</var>'
      AND event = 'MESSAGE_ACCEPTED'
  ) sent
  CROSS JOIN (
    SELECT event_timestamp AS delivered_time
    FROM `<var translate="no">project ID</var>.firebase_messaging.data`
    WHERE
      _PARTITIONTIME = TIMESTAMP('<var translate="no">date as YYYY-MM-DD</var>') AND
      message_id = '<var translate="no">your message id</var>' AND instance_id = '<var translate="no">your instance id</var>'
      AND (event = 'MESSAGE_DELIVERED'
  ) delivered;
  
```