# Source: https://www.courier.com/docs/sdk-libraries/android.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Android SDK

> Add in-app notifications, push notifications, and notification preferences to your Android app with prebuilt UI components and Kotlin APIs.

The Courier Android SDK provides prebuilt UI components and APIs for building notification experiences in Kotlin. It handles authentication, token management, and real-time message delivery so you can focus on your app.

* **[Inbox](#inbox)** — prebuilt notification center for Jetpack Compose and XML layouts
* **[Push Notifications](#push-notifications)** — automatic FCM token syncing and delivery tracking
* **[Preferences](#preferences)** — prebuilt UI for users to manage their notification settings

Available on
<Link href="https://github.com/trycourier/courier-android"><Icon icon="github" iconType="solid" /> GitHub</Link>.

| Requirement     | Value   |
| --------------- | ------- |
| Min Android SDK | 23      |
| Gradle          | 8.4+    |
| Package manager | Jitpack |

## Installation

<Steps>
  <Step title="Add the Jitpack repository">
    In your `settings.gradle` or `settings.gradle.kts`:

    ```gradle  theme={null}
    dependencyResolutionManagement {
        repositories {
            google()
            mavenCentral()
            maven { url 'https://jitpack.io' }
        }
    }
    ```
  </Step>

  <Step title="Add the dependency">
    In your app's `build.gradle`:

    ```gradle  theme={null}
    dependencies {
        implementation 'com.github.trycourier:courier-android:5.2.14'
    }
    ```
  </Step>

  <Step title="Initialize the SDK">
    Call `Courier.initialize()` in your `Application` class before using other SDK features. This gives Courier access to `SharedPreferences` for persisting state across sessions.

    ```kotlin  theme={null}
    class YourApplication : Application() {
        override fun onCreate() {
            super.onCreate()
            Courier.initialize(this)
        }
    }
    ```
  </Step>
</Steps>

<Note>
  If you only plan to use [`CourierClient`](#courierclient) APIs directly, you can skip the `initialize` step.
</Note>

## Authentication

All SDK features (Inbox, Push, Preferences) require a signed-in user. Authentication is JWT-based; your backend generates a token and the SDK manages credentials across app sessions.

<Note>
  For a full walkthrough of JWT generation, see the [Inbox Authentication guide](/platform/inbox/authentication).
</Note>

<Steps>
  <Step title="Generate a JWT on your backend">
    Call the [Issue Token endpoint](/api-reference/authentication/create-a-jwt) from your server:

    ```bash  theme={null}
    curl -X POST https://api.courier.com/auth/issue-token \
      -H "Authorization: Bearer $YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "scope": "user_id:YOUR_USER_ID write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands",
        "expires_in": "2 days"
      }'
    ```
  </Step>

  <Step title="Sign in the user">
    Pass the JWT to the SDK where you manage user state. Credentials persist across app sessions. If the token expires, generate a new one from your backend and call `signIn` again; the SDK does not handle token refresh automatically.

    ```kotlin  theme={null}
    lifecycleScope.launch {
        Courier.shared.signIn(
            accessToken = jwt,
            userId = "your_user_id"
        )
    }
    ```
  </Step>

  <Step title="Sign out when done">
    ```kotlin  theme={null}
    lifecycleScope.launch {
        Courier.shared.signOut()
    }
    ```
  </Step>
</Steps>

You can listen for authentication state changes:

```kotlin  theme={null}
val listener = Courier.shared.addAuthenticationListener { userId ->
    print(userId ?: "No user signed in")
}

listener.remove()
```

## Inbox

Courier Inbox provides a prebuilt notification center UI for Jetpack Compose and XML layouts. It supports theming, custom renderers, and real-time updates.

<Tip>
  Inbox requires the [Courier Inbox provider](https://app.courier.com/channels/courier) to be enabled in your workspace. If using JWT authentication, enable JWT support in the provider settings.

  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/courier-jwt-toggle.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=214922b19e181b120f70ed4850b69b9a" alt="JWT toggle in Courier provider settings" width="385" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/courier-jwt-toggle.png" />
</Tip>

<Note>
  Your app theme must extend `Theme.MaterialComponents` for the prebuilt UI to render correctly. Set this in your `res/values/themes.xml`.
</Note>

<Info>
  For an overview of how Courier Inbox works and how to send messages to it from your backend, see [Get Started with Inbox](/platform/inbox/inbox-overview) and [Send an Inbox Message](/platform/inbox/sending-a-message).
</Info>

### Prebuilt UI

<CodeGroup>
  ```kotlin Jetpack Compose theme={null}
  CourierInbox(
      modifier = Modifier.padding(innerPadding),
      onClickMessageListener = { message, index ->
          if (message.isRead) message.markAsUnread() else message.markAsRead()
      },
      onLongPressMessageListener = { message, index ->
          message.markAsArchived()
      },
      onClickActionListener = { action, message, index ->
          print(message.toString())
      },
      onScrollInboxListener = { offsetInDp ->
          print(offsetInDp.toString())
      }
  )
  ```

  ```kotlin XML Layout theme={null}
  // In your layout XML:
  // <com.courier.android.ui.inbox.CourierInbox
  //     android:id="@+id/courierInbox"
  //     android:layout_width="match_parent"
  //     android:layout_height="match_parent" />

  val inbox: CourierInbox = view.findViewById(R.id.courierInbox)

  inbox.setOnClickMessageListener { message, index ->
      if (message.isRead) message.markAsUnread() else message.markAsRead()
  }

  inbox.setOnLongPressMessageListener { message, index ->
      message.markAsArchived()
  }

  inbox.setOnClickActionListener { action, message, index ->
      Courier.log(action.toString())
  }

  inbox.setOnScrollInboxListener { offsetInDp ->
      Courier.log(offsetInDp.toString())
  }
  ```
</CodeGroup>

### Theming

Pass a `CourierInboxTheme` to customize fonts, colors, unread indicators, swipe actions, and button styles. Both light and dark themes are supported.

```kotlin  theme={null}
CourierInbox(
    modifier = Modifier.padding(innerPadding),
    canSwipePages = true,
    lightTheme = yourLightTheme,
    darkTheme = yourDarkTheme,
    ...
)
```

<Frame caption="Default and styled Inbox on Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-inbox-default.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=86ae9079bb5fdc4143972dc5d3f9b797" alt="Default Inbox" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-inbox-default.png" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-inbox-styled.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=6bc18219d2a66f2dbba56662f338ac01" alt="Styled Inbox" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-inbox-styled.png" />
  </div>
</Frame>

You can also apply branding from [Courier Studio](https://app.courier.com/designer/brands). The SDK supports primary color and footer visibility from your brand settings.

### Custom Inbox UI

For full control over rendering, use `addInboxListener` to receive raw message data and build your own UI:

```kotlin  theme={null}
lifecycleScope.launch {
    val listener = Courier.shared.addInboxListener(
        onLoading = {
            // Show loading state
        },
        onError = { error ->
            // Handle error
        },
        onMessagesChanged = { messages, canPaginate, feed ->
            // Update your custom UI with messages
        },
        onUnreadCountChanged = { count ->
            // Update badge indicators
        },
        onTotalCountChanged = { count, feed ->
            // Track total messages per feed
        },
        onPageAdded = { messages, canPaginate, isFirstPage, feed ->
            // Efficiently append new pages during pagination
        },
        onMessageEvent = { message, index, feed, event ->
            // React to individual events: READ, UNREAD, ARCHIVED, OPENED, ADDED
        }
    )

    // Clean up when done
    listener.remove()
}
```

### Message Actions

```kotlin  theme={null}
lifecycleScope.launch {
    Courier.shared.readMessage(messageId = "...")
    Courier.shared.unreadMessage(messageId = "...")
    Courier.shared.archiveMessage(messageId = "...")
    Courier.shared.readAllInboxMessages()
}

// Or via message object
message.markAsRead()
message.markAsUnread()
message.markAsArchived()
```

## Push Notifications

The SDK simplifies push notification setup with automatic FCM token syncing, delivery tracking, and permission management.

<Note>
  Push notifications require a physical device. Emulators do not reliably support push token registration or notification delivery.
</Note>

### Provider Setup

| Provider                                                      | Token Syncing                    |
| ------------------------------------------------------------- | -------------------------------- |
| [Firebase FCM](https://app.courier.com/channels/firebase-fcm) | Automatic (via `CourierService`) |
| [Expo](https://app.courier.com/channels/expo)                 | Manual                           |
| [OneSignal](https://app.courier.com/channels/onesignal)       | Manual                           |
| [Pusher Beams](https://app.courier.com/channels/pusher-beams) | Manual                           |

<Info>
  For step-by-step provider credential setup, see the [FCM integration guide](/external-integrations/push/firebase-fcm). Initialize the [Firebase SDK](https://firebase.google.com/docs/android/setup) in your project before continuing.
</Info>

### Automatic Token Syncing (FCM)

<Steps>
  <Step title="Create a notification service">
    Create a class that extends `CourierService`. This automatically syncs FCM tokens and tracks delivery.

    ```kotlin  theme={null}
    import com.courier.android.notifications.presentNotification
    import com.courier.android.service.CourierService
    import com.google.firebase.messaging.RemoteMessage

    class YourNotificationService : CourierService() {
        override fun showNotification(message: RemoteMessage) {
            super.showNotification(message)
            message.presentNotification(
                context = this,
                handlingClass = MainActivity::class.java,
                icon = android.R.drawable.ic_dialog_info
            )
        }
    }
    ```
  </Step>

  <Step title="Register the service in AndroidManifest.xml">
    ```xml  theme={null}
    <service
        android:name=".YourNotificationService"
        android:exported="false">
        <intent-filter>
            <action android:name="com.google.firebase.MESSAGING_EVENT" />
        </intent-filter>
    </service>
    ```
  </Step>

  <Step title="Extend CourierActivity for click handling">
    ```kotlin  theme={null}
    class MainActivity : CourierActivity() {
        override fun onPushNotificationClicked(message: RemoteMessage) {
            // Handle notification click
        }

        override fun onPushNotificationDelivered(message: RemoteMessage) {
            // Handle notification delivery
        }
    }
    ```
  </Step>
</Steps>

### Manual Token Syncing

If you don't want to use `CourierService`, sync tokens manually:

```kotlin  theme={null}
lifecycleScope.launch {
    Courier.shared.setToken(
        provider = CourierPushProvider.FIREBASE_FCM,
        token = "your_fcm_token"
    )
}
```

### Requesting Permission

For Android 13+ (API 33), you need to request notification permission at runtime. You can also check the current status without prompting.

```kotlin  theme={null}
Courier.shared.requestNotificationPermission(activity)

val isGranted = Courier.shared.isPushPermissionGranted(context)
```

### Send a Test Notification

Once you've completed the setup above, send a test push using the [Send API](/api-reference/send/send-a-message) with `push` as the routing channel. See the [FCM sending guide](/external-integrations/push/firebase-fcm#sending-messages) for a complete example.

## Preferences

Courier Preferences provides a prebuilt UI for users to manage which notification topics and channels they subscribe to.

<Info>
  Topics and sections are configured in the [Preferences Editor](/platform/preferences/preferences-editor). See [Preferences Overview](/platform/preferences/preferences-overview) for how preference enforcement works at send time.
</Info>

<CodeGroup>
  ```kotlin Jetpack Compose theme={null}
  CourierPreferences(
      mode = CourierPreferences.Mode.Topic,
      onError = { error ->
          print(error.toString())
      }
  )
  ```

  ```kotlin XML Layout theme={null}
  val preferences: CourierPreferences = view.findViewById(R.id.courierPreferences)

  preferences.apply {
      mode = CourierPreferences.Mode.Topic
      onError = { error ->
          print(error)
      }
  }
  ```
</CodeGroup>

### Preference Modes

* **Topic mode** (`Mode.Topic`): shows subscription topics the user can toggle on or off
* **Channels mode** (`Mode.Channels(listOf(PUSH, SMS, EMAIL))`): shows per-channel controls for each topic

### Theming

Pass a `CourierPreferencesTheme` to customize fonts, colors, toggle styles, and section headers. Light and dark themes are both supported, and [Courier Studio branding](https://app.courier.com/designer/brands) is automatically applied when a `brandId` is provided.

<Frame caption="Default and styled Preferences on Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-preferences-default.gif?s=748931e662d547de3a1227d9a18b6a85" alt="Default Preferences" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-preferences-default.gif" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-preferences-styled.gif?s=0ee58d84f4f57937134e5b816543e33a" alt="Styled Preferences" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-preferences-styled.gif" />
  </div>
</Frame>

## CourierClient

For advanced use cases, `CourierClient` provides direct access to the Courier API:

```kotlin  theme={null}
val client = CourierClient(
    jwt = "...",
    userId = "your_user_id"
)

// Token management
client.tokens.putUserToken(token = "...", provider = "firebase-fcm")

// Inbox
val messages = client.inbox.getMessages(paginationLimit = 25)
val unreadCount = client.inbox.getUnreadMessageCount()
client.inbox.read(messageId = "...")
client.inbox.readAll()

// Inbox websocket (real-time updates across devices)
client.inbox.socket.apply {
    receivedMessage = { message -> print(message) }
    receivedMessageEvent = { event -> print(event) } // READ, UNREAD, ARCHIVE, OPENED
    connect()
    sendSubscribe()
}

// Preferences
val prefs = client.preferences.getUserPreferences()
client.preferences.putUserPreferenceTopic(
    topicId = "...",
    status = CourierPreferenceStatus.OPTED_IN,
    hasCustomRouting = true,
    customRouting = listOf(CourierPreferenceChannel.PUSH)
)

// Branding
val brand = client.brands.getBrand(brandId = "...")

// URL tracking (from push payloads or inbox messages)
client.tracking.postTrackingUrl(url = "courier_tracking_url", event = CourierTrackingEvent.DELIVERED)
```

See the full API reference on [GitHub](https://github.com/trycourier/courier-android/blob/master/Docs/Client.md).

<CardGroup cols={2}>
  <Card title="Inbox Overview" href="/platform/inbox/inbox-overview" icon="inbox">
    Learn about Courier Inbox and how to set it up
  </Card>

  <Card title="Push Integrations" href="/external-integrations/push/intro-to-push" icon="mobile">
    Configure FCM and other push providers
  </Card>

  <Card title="Preferences" href="/platform/preferences/preferences-overview" icon="list">
    Set up notification preference topics and channels
  </Card>

  <Card title="GitHub" href="https://github.com/trycourier/courier-android" icon="github">
    Source code, examples, and changelog
  </Card>
</CardGroup>
