# Source: https://documentation.onesignal.com/docs/en/android-live-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Android live notifications

> Create and update dynamic, real-time notifications on Android devices using OneSignal Live Notifications. Deliver continuously updated content inside a single notification, simulating iOS Live Activities for Android.

OneSignal’s Android Live Notifications let you send real-time updates to a single notification, reducing clutter and improving engagement. These notifications remain persistent and update their content dynamically—ideal for sports scores, download progress, or event tracking.

To receive Live Notifications, Android users must have push notifications enabled.

## Requirements

* Your app must use the latest version of the [OneSignal SDK](./mobile-sdk-setup).
* Android users must have push notification permissions enabled.

***

## Live notifications vs. standard push

Unlike regular push notifications, which send a new notification each time, Live Notifications use a single notification updated over time. Updates are sent via the [Create Message API](/reference/create-message) using the same `collapse_id`.

***

## Configuration

### 1. Implement a Notification Service Extension

Create a `NotificationServiceExtension` class that implements `INotificationServiceExtension`. This class intercepts incoming notifications and can modify or override them.

<Info>
  Refer to [Android Notification Service Extension](./service-extensions#android-notification-service-extension) for more details.
</Info>

```kotlin NotificationServiceExtention.kt theme={null}
package com.onesignal.sample.android

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build
import com.onesignal.notifications.INotificationReceivedEvent
import com.onesignal.notifications.INotificationServiceExtension
import org.json.JSONObject
import java.util.logging.Logger

class NotificationServiceExtension : INotificationServiceExtension {
  override fun onNotificationReceived(event: INotificationReceivedEvent) {
        val context = event.context
        val notificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as? NotificationManager
            ?: run {
                logger.warning("NotificationManager not available.")
                return
            }

        notificationManager.let {
            if (!notificationChannelsCreated) {
                createNotificationChannels(notificationManager)
            }
        }

        // Use `additional_data`to submit the Live Notification payload.
      val additionalData = event.notification.additionalData
        val liveNotificationPayload = additionalData?.optJSONObject("live_notification")
        if (liveNotificationPayload == null) {
            logger.info("No live notification payload found. Showing original notification.")
            return
        }

        event.preventDefault()
        handleLiveNotification(event, liveNotificationPayload, notificationManager, context)
    }
}

```

### 2. Add the extension to the Android Manifest

<CodeGroup>
  ```xml AndroidManifest.xml theme={null}
    <meta-data android:name="com.onesignal.NotificationServiceExtension"
                android:value="com.onesignal.sample.android.NotificationServiceExtension" />
  ```

  ```xml Example AndroidManifest.xml theme={null}
  <?xml version="1.0" encoding="utf-8"?>
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
      xmlns:tools="http://schemas.android.com/tools">

      <application
          android:allowBackup="true"
          android:dataExtractionRules="@xml/data_extraction_rules"
          android:fullBackupContent="@xml/backup_rules"
          android:icon="@mipmap/ic_launcher"
          android:name=".MainApplication"
          android:label="@string/app_name"
          android:roundIcon="@mipmap/ic_launcher_round"
          android:supportsRtl="true"
          android:theme="@style/Theme.OneSignalAndroidSample"
          tools:targetApi="31">
          <meta-data android:name="com.onesignal.NotificationServiceExtension"
              android:value="com.onesignal.sample.android.NotificationServiceExtension" />
          <activity
              android:name=".MainActivity"
              android:exported="true">
              <intent-filter>
                  <action android:name="android.intent.action.MAIN" />

                  <category android:name="android.intent.category.LAUNCHER" />
              </intent-filter>
          </activity>
      </application>

  </manifest>
  ```

</CodeGroup>

### 3. Create Live Notification types

A Live Notification Type indicates which Live Notification to start.

#### Define keys

Live Notifications are referenced by a `key`, which determines how updates are routed.

```kotlin NotificationServiceExtention.kt theme={null}
private const val PROGRESS_LIVE_NOTIFICATION = "progress"
```

#### Create notification channels

Channels define how notifications behave (sound, vibration, appearance). You must create channels for your Live Notification types. We recommend:

* Low Importance for progress notifications
* Disable badges
* Keep sound and vibration to a minimum

See [Android Notification Channel Categories](./android-notification-categories) for more information.

#### Design the Live Notification

When designing a Live Notification, you have the flexibility to create a notification design for each update type. Each design you create must be assigned a specific type, allowing for varied presentations of a Live Notification.

```kotlin NotificationServiceExtention.kt theme={null}
private fun updateProgressNotification(
        liveNotificationUpdates: JSONObject,
        context: Context,
        notificationManager: NotificationManager
    ) {
        val currentProgress = liveNotificationUpdates.optInt("current_progress", 0)

        val builder = NotificationCompat.Builder(context, PROGRESS_CHANNEL_ID)
            .setContentTitle("Progress Live Notifications")
            .setContentText("It's working...")
            .setSmallIcon(android.R.drawable.ic_media_play)
            .setLargeIcon(BitmapFactory.decodeResource(context.resources, android.R.drawable.ic_dialog_info))
            .setOngoing(true)
            .setOnlyAlertOnce(true)
            .setProgress(100, currentProgress, false)
            .setAutoCancel(false) // Prevent auto-dismissal of notification until you set the end event

        notificationManager.notify(keyMap[PROGRESS_LIVE_NOTIFICATION]!!, builder.build())
        logger.info("Updated progress notification with progress: $currentProgress")
    }
```

**Design considerations:**

* Small icon & accent color
* Large icon
* Big picture
* Action buttons

<Info>
  See [Android custom notification layout](https://developer.android.com/develop/ui/views/notifications/custom-notification) for advanced design options.
</Info>

### 4. Extract the Live Notification payload

Live Notifications use the `additional_data` field to pass structured content.

```kotlin NotificationServiceExtention.kt theme={null}
val additionalData = event.notification.additionalData
val liveNotificationPayload = additionalData?.optJSONObject("live_notification")
```

#### Live Notification Schema

| Property           | Required | Description                                                                                                                       |
| ------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `key`              | Yes      | Used to load the correct notification UI.                                                                                         |
| `event`            | Yes      | The action to perform on the Live Notification.                                                                                   |
| `event_attributes` | No       | Static data is used to initialize the Live Notification; a Self-defined schema that defines the data your notification needs.     |
| `event_updates`    | No       | Dynamic content of the Live Notification. Must conform to the ContentState interface defined within your app's Live Notification. |

```json Example Live Notification Payload theme={null}
  {
      "key": "celtics-vs-lakers",
      "event": "start",
      "event_attributes": {
          "homeTeam": "Celtics",
          "awayTeam": "Lakers",
          "game": "Finals Game 1"
      },
      "event_updates": {
          "quarter": 1,
          "homeScore": 0,
          "awayScore": 0,
      }
  }
```

### 5. Handle Live Notification events

Each Live Notification must respond to the following events:

| Event    | Description                                              | Required fields                     |
| -------- | -------------------------------------------------------- | ----------------------------------- |
| `start`  | Begins a Live Notification with static and dynamic data. | `event_attributes`, `event_updates` |
| `update` | Updates the Live Notification with new dynamic data.     | `event_updates`                     |
| `end`    | Ends and removes the Live Notification.                  | None                                |

```kotlin NotificationServiceExtention.kt theme={null}
val liveNotificationEvent = liveNotificationPayload.optString("event", "")
```

***

## Start a Live Notification

When you are ready to start a Live Notification:

* Set `event_attributes` to initialize the static data for the Live Notification. This data will not change during the lifetime of the Live Notification.
* Set `event_updates` data to initialize the dynamic data for the Live Notification. This is the data that can and will change during the lifetime of the Live Notification.
* A [`collapse_id`](./push#collapse-id) to make sure each update overrides the previous. This ID should be unique to the Live Notification to ensure subsequent updates are reflected in the same notification.

```curl curl theme={null}
  curl -X "POST" "https://api.onesignal.com/notifications" \
       -H 'Authorization: key YOUR_REST_API_KEY' \
       -H 'Content-Type: application/json; charset=utf-8' \
       -d $'{
    "app_id": "YOUR_APP_ID",
    "isAndroid": true,
    "collapse_id": "THE_UNIQUE_ID_FOR_THIS_LIVE_NOTIFICATION",
    "data": {
      "live_notification": {
        "key": "progress",
        "event": "start",
        "event_attributes": {},
        "event_updates": {
          "current_progress": 0
        }
      }
    },
    "headings": {
      "en": "Start"
    },
    "contents": {
      "en": "Starting Live Notification"
    },
    "include_aliases": {
      "external_id": ["EID1", "EID2"]
    },
    "target_channel": "push"
  }'
```

***

## Update Live Notification

You can update the Live Notification as many times as you like, so long as it's started first.

* Set `event_updates` data to initialize the dynamic data for the Live Notification. This is the data that can and will change during the lifetime of the Live Notification and informs what to update your Live Notification's content with.

**Example cURL request**

```curl curl theme={null}
  curl -X "POST" "https://api.onesignal.com/notifications" \
       -H 'Authorization: key YOUR_REST_API_KEY' \
       -H 'Content-Type: application/json; charset=utf-8' \
       -d $'{
    "app_id": "YOUR_APP_ID",
    "isAndroid": true,
    "collapse_id": "THE_UNIQUE_ID_FOR_THIS_LIVE_NOTIFICATION",
    "data": {
      "live_notification": {
        "key": "progress",
        "event": "update",
     "event_attributes": {},
        "event_updates": {
          "current_progress": 80
        }
      }
    },
    "headings": {
      "en": "Update"
    },
    "contents": {
      "en": "Updating Live Notification"
    },
    "include_aliases": {
      "external_id": ["EID1", "EID2"]
    },
    "target_channel": "push"
  }'
```

## End Live Notification

**Example cURL request**

```curl curl theme={null}
  curl -X "POST" "https://api.onesignal.com/notifications" \
       -H 'Authorization: key YOUR_REST_API_KEY' \
       -H 'Content-Type: application/json; charset=utf-8' \
       -d $'{
    "app_id": "YOUR_APP_ID",
    "isAndroid": true,
    "collapse_id": "THE_UNIQUE_ID_FOR_THIS_LIVE_NOTIFICATION",
    "data": {
      "live_notification": {
        "key": "progress",
        "event": "dismiss"
      }
    },
    "headings": {
      "en": "Dismissing"
    },
    "contents": {
      "en": "Dismissing Live Notification"
    },
    "include_aliases": {
      "external_id": ["EID1", "EID2"]
    },
    "target_channel": "push"
  }'
```

***

<Check>
  You have successfully created a Live Notification!

  Related docs:

* [Android Notification Service Extension](./service-extensions#android-notification-service-extension)
* [Android SDK Setup](./mobile-sdk-setup)
* [Create Message API](/reference/create-message)
</Check>

***

Built with [Mintlify](https://mintlify.com).
