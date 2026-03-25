# Source: https://www.courier.com/docs/sdk-libraries/ios.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier iOS SDK

> Add in-app notifications, push notifications, and notification preferences to your iOS app with prebuilt UI components and Swift APIs.

The Courier iOS SDK provides prebuilt UI components and APIs for building notification experiences in Swift. It handles authentication, token management, and real-time message delivery so you can focus on your app.

* **[Inbox](#inbox)** — prebuilt notification center with theming and custom rendering
* **[Push Notifications](#push-notifications)** — automatic token syncing and delivery tracking for APNS and FCM
* **[Preferences](#preferences)** — prebuilt UI for users to manage their notification settings

Available on
<Link href="https://github.com/trycourier/courier-ios"><Icon icon="github" iconType="solid" /> GitHub</Link>.

| Requirement      | Value                            |
| ---------------- | -------------------------------- |
| Min iOS version  | 13.0                             |
| Package managers | Swift Package Manager, CocoaPods |

## Installation

<CodeGroup>
  ```text Swift Package Manager theme={null}
  1. In Xcode, go to File > Add Packages
  2. Paste: https://github.com/trycourier/courier-ios
  3. Select the version and add to your target
  ```

  ```ruby CocoaPods theme={null}
  platform :ios, '13.0'

  target 'YourApp' do
    pod 'Courier_iOS'
  end
  ```
</CodeGroup>

If using CocoaPods, run `pod install` from your project's `ios/` directory after updating the Podfile.

## Authentication

All SDK features (Inbox, Push, Preferences) require a signed-in user. Authentication is JWT-based; your backend generates a token and the SDK manages credentials across app sessions.

<Note>
  For a full walkthrough of JWT generation, see the [Inbox Authentication guide](/platform/inbox/authentication).
</Note>

<Steps>
  <Step title="Generate a JWT on your backend">
    Call the [Issue Token endpoint](/api-reference/authentication/create-a-jwt) from your server with the scopes your app needs:

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

    ```swift  theme={null}
    Task {
        await Courier.shared.signIn(
            userId: "your_user_id",
            accessToken: jwt
        )
    }
    ```
  </Step>

  <Step title="Sign out when done">
    ```swift  theme={null}
    Task {
        await Courier.shared.signOut()
    }
    ```
  </Step>
</Steps>

You can listen for authentication state changes:

```swift  theme={null}
let listener = await Courier.shared.addAuthenticationListener { userId in
    print(userId ?? "No user signed in")
}

listener.remove()
```

## Inbox

Courier Inbox provides a prebuilt notification center UI for SwiftUI and UIKit. It supports theming, custom renderers, and real-time updates.

<Tip>
  Inbox requires the [Courier Inbox provider](https://app.courier.com/channels/courier) to be enabled in your workspace. If using JWT authentication, enable JWT support in the provider settings.

  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/courier-jwt-toggle.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=214922b19e181b120f70ed4850b69b9a" alt="JWT toggle in Courier provider settings" width="385" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/courier-jwt-toggle.png" />
</Tip>

<Info>
  For an overview of how Courier Inbox works and how to send messages to it from your backend, see [Get Started with Inbox](/platform/inbox/inbox-overview) and [Send an Inbox Message](/platform/inbox/sending-a-message).
</Info>

### Prebuilt UI

<CodeGroup>
  ```swift SwiftUI theme={null}
  import Courier_iOS

  CourierInboxView(
      didClickInboxMessageAtIndex: { message, index in
          message.isRead ? message.markAsUnread() : message.markAsRead()
      },
      didLongPressInboxMessageAtIndex: { message, index in
          message.markAsArchived()
      },
      didClickInboxActionForMessageAtIndex: { action, message, index in
          print(action, message, index)
      },
      didScrollInbox: { scrollView in
          print(scrollView.contentOffset.y)
      }
  )
  ```

  ```swift UIKit theme={null}
  import Courier_iOS

  let courierInbox = CourierInbox(
      didClickInboxMessageAtIndex: { message, index in
          message.isRead ? message.markAsUnread() : message.markAsRead()
      },
      didLongPressInboxMessageAtIndex: { message, index in
          message.markAsArchived()
      },
      didClickInboxActionForMessageAtIndex: { action, message, index in
          print(action, message, index)
      },
      didScrollInbox: { scrollView in
          print(scrollView.contentOffset.y)
      }
  )

  view.addSubview(courierInbox)
  ```
</CodeGroup>

### Theming

Pass a `CourierInboxTheme` to customize fonts, colors, unread indicators, swipe actions, and button styles. Both light and dark themes are supported.

```swift  theme={null}
CourierInboxView(
    canSwipePages: true,
    lightTheme: yourLightTheme,
    darkTheme: yourDarkTheme,
    ...
)
```

<Frame caption="Default and styled Inbox on iOS">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-inbox-default.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=e6844e7c3baf6cc83508000c6cc04dbb" alt="Default Inbox" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-inbox-default.png" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-inbox-styled.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=03b368e1ad9ad77ef2ab85dd92814abd" alt="Styled Inbox" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-inbox-styled.png" />
  </div>
</Frame>

You can also apply branding from [Courier Studio](https://app.courier.com/designer/brands). The SDK supports primary color and footer visibility from your brand settings.

### Custom Inbox UI

For full control over rendering, use `addInboxListener` to receive raw message data and build your own UI:

```swift  theme={null}
let listener = await Courier.shared.addInboxListener(
    onLoading: { isRefresh in
        // Show loading state
    },
    onError: { error in
        // Handle error
    },
    onMessagesChanged: { messages, canPaginate, feed in
        // Update your custom UI with messages
    },
    onUnreadCountChanged: { count in
        // Update badge indicators
    },
    onTotalCountChanged: { count, feed in
        // Track total messages per feed
    },
    onPageAdded: { messages, canPaginate, isFirstPage, feed in
        // Efficiently append new pages during pagination
    },
    onMessageEvent: { message, index, feed, event in
        // React to individual events: .read, .unread, .archived, .opened, .added
    }
)

// Clean up
listener.remove()
```

### Message Actions

```swift  theme={null}
try await Courier.shared.readMessage("messageId")
try await Courier.shared.unreadMessage("messageId")
try await Courier.shared.archiveMessage("messageId")
try await Courier.shared.readAllInboxMessages()

// Or via message object
message.markAsRead()
message.markAsUnread()
message.markAsArchived()
```

## Push Notifications

The SDK simplifies push notification setup with automatic token syncing, delivery tracking, and permission management.

<Note>
  Push notifications require a physical device. Simulators do not reliably support push token registration or notification delivery.
</Note>

### Provider Setup

| Provider                                                      | Token Syncing                     |
| ------------------------------------------------------------- | --------------------------------- |
| [APNS](https://app.courier.com/channels/apn)                  | Automatic (via `CourierDelegate`) |
| [Firebase FCM](https://app.courier.com/channels/firebase-fcm) | Manual                            |
| [Expo](https://app.courier.com/channels/expo)                 | Manual                            |
| [OneSignal](https://app.courier.com/channels/onesignal)       | Manual                            |
| [Pusher Beams](https://app.courier.com/channels/pusher-beams) | Manual                            |

<Info>
  For step-by-step provider credential setup, see the [APNS integration guide](/external-integrations/push/apple-push-notification) or [FCM integration guide](/external-integrations/push/firebase-fcm).
</Info>

### Automatic Token Syncing (APNS)

Extend `CourierDelegate` in your `AppDelegate` to automatically sync APNS tokens and handle notification events:

```swift  theme={null}
import Courier_iOS

@main
class AppDelegate: CourierDelegate {

    override func pushNotificationDeliveredInForeground(
        message: [AnyHashable: Any]
    ) -> UNNotificationPresentationOptions {
        return [.sound, .list, .banner, .badge]
    }

    override func pushNotificationClicked(message: [AnyHashable: Any]) {
        print("Notification clicked: \(message)")
    }
}
```

### Manual Token Syncing

For FCM or other providers, sync tokens manually:

```swift  theme={null}
Task {
    // APNS token
    try await Courier.shared.setAPNSToken(deviceToken)

    // FCM or other provider
    try await Courier.shared.setToken(for: .firebaseFcm, token: fcmToken)
}
```

### Notification Service Extension

To track notification delivery when the app is not running, add a Notification Service Extension:

<Steps>
  <Step title="Download the template">
    Download [`CourierNotificationServiceTemplate.zip`](https://github.com/trycourier/courier-notification-service-extension-template/archive/refs/heads/main.zip) and run `sh make_template.sh`. Watch the [video walkthrough on GitHub](https://github.com/trycourier/courier-ios/blob/master/Docs/3_PushNotifications.md#4-add-the-notification-service-extension-optional-but-recommended) for a step-by-step guide.
  </Step>

  <Step title="Add the extension target">
    In Xcode: File > New > Target > select "Courier Service" > Finish.
  </Step>

  <Step title="Link the Courier SDK">
    Add the Courier package to the new target via SPM or CocoaPods.
  </Step>
</Steps>

### Requesting Permission

Prompt the user to allow notifications. iOS shows a system dialog the first time; if the user denies, they must enable notifications from device Settings.

```swift  theme={null}
let status = try await Courier.requestNotificationPermission()
```

### Send a Test Notification

Once you've completed the setup above, send a test push using the [Send API](/api-reference/send/send-a-message) with `push` as the routing channel. See the [APNS sending guide](/external-integrations/push/apple-push-notification#sending-messages) or [FCM sending guide](/external-integrations/push/firebase-fcm#sending-messages) for complete examples.

## Preferences

Courier Preferences provides a prebuilt UI for users to manage which notification topics and channels they subscribe to.

<Info>
  Topics and sections are configured in the [Preferences Editor](/platform/preferences/preferences-editor). See [Preferences Overview](/platform/preferences/preferences-overview) for how preference enforcement works at send time.
</Info>

<CodeGroup>
  ```swift SwiftUI theme={null}
  import Courier_iOS

  CourierPreferencesView(
      mode: .topic,
      onError: { error in
          print(error.localizedDescription)
      }
  )
  ```

  ```swift UIKit theme={null}
  import Courier_iOS

  let preferences = CourierPreferences(
      mode: .topic,
      onError: { error in
          print(error.localizedDescription)
      }
  )

  view.addSubview(preferences)
  ```
</CodeGroup>

### Preference Modes

* **Topic mode** (`.topic`): shows subscription topics the user can toggle on or off
* **Channels mode** (`.channels([.push, .sms, .email])`): shows per-channel controls for each topic

### Theming

Pass a `CourierPreferencesTheme` to customize fonts, colors, toggle styles, and section headers. Light and dark themes are both supported, and [Courier Studio branding](https://app.courier.com/designer/brands) is automatically applied when a `brandId` is provided.

<Frame caption="Default and styled Preferences on iOS">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-preferences-default.gif?s=7ccc1f70a8ab6c51bf9627a9b7a3281c" alt="Default Preferences" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-preferences-default.gif" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-preferences-styled.gif?s=e740a619288899725cfcbad1f07ed5cd" alt="Styled Preferences" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-preferences-styled.gif" />
  </div>
</Frame>

## CourierClient

For advanced use cases, `CourierClient` provides direct access to the Courier API:

```swift  theme={null}
let client = CourierClient(
    jwt: "...",
    userId: "your_user_id"
)

// Token management
try await client.tokens.putUserToken(token: "...", provider: "apns")

// Inbox
let messages = try await client.inbox.getMessages(paginationLimit: 25)
let unreadCount = try await client.inbox.getUnreadMessageCount()
try await client.inbox.read(messageId: "...")
try await client.inbox.readAll()

// Inbox websocket (real-time updates across devices)
let socket = client.inbox.socket
socket.receivedMessage = { message in print(message) }
socket.receivedMessageEvent = { event in print(event) } // .read, .unread, .archive, .opened
try await socket.connect()
try await socket.sendSubscribe()

// Preferences
let prefs = try await client.preferences.getUserPreferences()
try await client.preferences.putUserPreferenceTopic(
    topicId: "...",
    status: .optedIn,
    hasCustomRouting: true,
    customRouting: [.push]
)

// Branding
let brand = try await client.brands.getBrand(brandId: "...")

// URL tracking (from push payloads or inbox messages)
try await client.tracking.postTrackingUrl(url: "courier_tracking_url", event: .delivered)
```

See the full API reference on [GitHub](https://github.com/trycourier/courier-ios/blob/master/Docs/5_Client.md).

<CardGroup cols={2}>
  <Card title="Inbox Overview" href="/platform/inbox/inbox-overview" icon="inbox">
    Learn about Courier Inbox and how to set it up
  </Card>

  <Card title="Push Integrations" href="/external-integrations/push/intro-to-push" icon="mobile">
    Configure APNS, FCM, and other push providers
  </Card>

  <Card title="Preferences" href="/platform/preferences/preferences-overview" icon="list">
    Set up notification preference topics and channels
  </Card>

  <Card title="GitHub" href="https://github.com/trycourier/courier-ios" icon="github">
    Source code, examples, and changelog
  </Card>
</CardGroup>
