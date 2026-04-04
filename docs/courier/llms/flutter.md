# Source: https://www.courier.com/docs/sdk-libraries/flutter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier Flutter SDK

> Add in-app notifications, push notifications, and notification preferences to your Flutter app with prebuilt widgets and Dart APIs.

The Courier Flutter SDK provides prebuilt widgets and APIs for building notification experiences in Dart. It handles authentication, token management, and real-time message delivery across iOS and Android from a single codebase.

* **[Inbox](#inbox)** — prebuilt notification center widget with theming and custom rendering
* **[Push Notifications](#push-notifications)** — automatic token syncing and delivery tracking for APNS and FCM
* **[Preferences](#preferences)** — prebuilt widget for users to manage their notification settings

Available on
<Link href="https://github.com/trycourier/courier-flutter"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://pub.dev/packages/courier_flutter"><Icon icon="box" iconType="solid" /> pub.dev</Link>.

| Requirement     | Value |
| --------------- | ----- |
| Min iOS version | 15.0  |
| Min Android SDK | 23    |
| Gradle          | 8.4+  |

## Installation

```bash  theme={null}
flutter pub add courier_flutter
```

### iOS Setup

Update your deployment target to iOS 15+, then install the CocoaPod:

```bash  theme={null}
cd ios && pod install
```

### Android Setup

<Steps>
  <Step title="Add the Jitpack repository">
    In your `android/build.gradle`:

    ```gradle  theme={null}
    allprojects {
        repositories {
            google()
            mavenCentral()
            maven { url 'https://jitpack.io' }
        }
    }
    ```
  </Step>

  <Step title="Set minimum SDK version">
    In your `app/build.gradle`:

    ```gradle  theme={null}
    minSdkVersion 23
    targetSdkVersion 33
    compileSdkVersion 33
    ```
  </Step>

  <Step title="Gradle sync">
    Your app must support at least Gradle 8.4.
  </Step>
</Steps>

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

    ```dart  theme={null}
    await Courier.shared.signIn(
        userId: "your_user_id",
        accessToken: jwt,
    );
    ```
  </Step>

  <Step title="Sign out when done">
    ```dart  theme={null}
    await Courier.shared.signOut();
    ```
  </Step>
</Steps>

You can listen for authentication state changes:

```dart  theme={null}
final listener = await Courier.shared.addAuthenticationListener((userId) {
    print(userId ?? "No user signed in");
});

await listener.remove();
```

## Inbox

Courier Inbox provides a prebuilt notification center widget. It supports theming, custom renderers, and real-time updates. The widget automatically adapts to your app's Flutter `Theme` unless you provide a custom `CourierInboxTheme`.

<Tip>
  Inbox requires the [Courier Inbox provider](https://app.courier.com/channels/courier) to be enabled in your workspace. If using JWT authentication, enable JWT support in the provider settings.

  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/courier-jwt-toggle.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=214922b19e181b120f70ed4850b69b9a" alt="JWT toggle in Courier provider settings" width="385" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/courier-jwt-toggle.png" />
</Tip>

<Info>
  For an overview of how Courier Inbox works and how to send messages to it from your backend, see [Get Started with Inbox](/platform/inbox/inbox-overview) and [Send an Inbox Message](/platform/inbox/sending-a-message).
</Info>

### Prebuilt Widget

<Frame caption="Default Inbox on iOS and Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-inbox-default-ios.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=d034503fc2476be86a06363b5ebd588e" alt="Default Inbox on iOS" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-inbox-default-ios.png" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-inbox-default-android.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=b6e2f493d2534b71669b4a20cccac050" alt="Default Inbox on Android" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-inbox-default-android.png" />
  </div>
</Frame>

```dart  theme={null}
CourierInbox(
  onMessageClick: (message, index) {
    message.isRead ? message.markAsUnread() : message.markAsRead();
  },
  onActionClick: (action, message, index) {
    print(action);
  },
)
```

The widget automatically picks up your app's Flutter theme:

* Button style from `Theme.of(context).elevatedButtonTheme.style`
* Loading/unread indicator color from `Theme.of(context).primaryColor`
* Text styles from `Theme.of(context).textTheme`

### Theming

Pass a `CourierInboxTheme` to override the default styles. This controls fonts, colors, unread indicators, swipe actions, tab styles, and button styles.

```dart  theme={null}
final theme = CourierInboxTheme(
    loadingIndicatorColor: Color(0xFF9747FF),
    tabIndicatorColor: Color(0xFF9747FF),
    unreadIndicatorStyle: CourierInboxUnreadIndicatorStyle(
        indicator: CourierInboxUnreadIndicator.dot,
        color: Color(0xFF9747FF),
    ),
    // ... additional style properties
);

CourierInbox(
  canSwipePages: true,
  lightTheme: theme,
  darkTheme: theme,
  onMessageClick: (message, index) { ... },
)
```

<Frame caption="Styled Inbox on iOS and Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-inbox-styled-ios.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=94352a699443b790fb4243b35924ea93" alt="Styled Inbox on iOS" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-inbox-styled-ios.png" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-inbox-styled-android.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=476b38f80ec3aaf146a517c07e6e1cad" alt="Styled Inbox on Android" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-inbox-styled-android.png" />
  </div>
</Frame>

You can also apply branding from [Courier Studio](https://app.courier.com/designer/brands). The SDK supports primary color and footer visibility from your brand settings.

### Custom Inbox UI

For full control over rendering, use `addInboxListener` to receive raw message data and build your own UI:

```dart  theme={null}
final listener = await Courier.shared.addInboxListener(
  onLoading: (isRefresh) {
    // Show loading state
  },
  onError: (error) {
    // Handle error
  },
  onMessagesChanged: (messages, canPaginate, feed) {
    // Update your custom UI with messages
  },
  onUnreadCountChanged: (unreadCount) {
    // Update badge indicators
  },
  onTotalCountChanged: (feed, totalCount) {
    // Track total messages per feed
  },
  onPageAdded: (messages, canPaginate, isFirstPage, feed) {
    // Efficiently append new pages during pagination
  },
  onMessageEvent: (message, index, feed, event) {
    // React to individual events: read, unread, archived, opened, added
  },
);

// Clean up
await listener.remove();
```

<Frame caption="Custom Inbox list item rendering">
  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-inbox-custom.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=6765d1ffac0e413d3a35aa1bed23f7d5" alt="Custom Inbox list item rendering" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-inbox-custom.png" />
</Frame>

### Message Actions

```dart  theme={null}
await Courier.shared.readMessage(messageId: messageId);
await Courier.shared.unreadMessage(messageId: messageId);
await Courier.shared.archiveMessage(messageId: messageId);
await Courier.shared.readAllInboxMessages();

// Or via message object
await message.markAsRead();
await message.markAsUnread();
await message.markAsArchived();
```

## Push Notifications

The SDK simplifies push notification setup with automatic token syncing and delivery tracking for both APNS (iOS) and FCM (Android).

<Note>
  Push notifications require a physical device. Simulators and emulators do not reliably support push token registration or notification delivery.
</Note>

| Feature                    | iOS | Android |
| -------------------------- | --- | ------- |
| Automatic token management | Yes | Yes     |
| Notification tracking      | Yes | Yes     |
| Permission requests        | Yes | No      |

### Provider Setup

Configure your push provider in the [Courier dashboard](https://app.courier.com/channels):

* **iOS**: [APNS](https://app.courier.com/channels/apn) (recommended) or [FCM](https://app.courier.com/channels/firebase-fcm)
* **Android**: [FCM](https://app.courier.com/channels/firebase-fcm) (recommended)

<Info>
  For step-by-step provider credential setup, see the [APNS integration guide](/external-integrations/push/apple-push-notification) or [FCM integration guide](/external-integrations/push/firebase-fcm).
</Info>

### iOS Push Setup

<Steps>
  <Step title="Enable Push Notifications capability">
    In Xcode: select your target > Signing & Capabilities > add Push Notifications. Watch the [video walkthrough on GitHub](https://github.com/trycourier/courier-flutter/blob/master/Docs/3_PushNotifications.md#automatically-sync-tokens-ios) for a step-by-step guide.
  </Step>

  <Step title="Add a Notification Service Extension">
    Follow the [iOS SDK Notification Service Extension setup](/sdk-libraries/ios#notification-service-extension) or add the extension manually. This enables delivery tracking when the app is not running.
  </Step>
</Steps>

### Android Push Setup

<Steps>
  <Step title="Set up Firebase">
    Follow the [Firebase Android setup guide](https://firebase.google.com/docs/android/setup) and add the `google-services.json` to your app.
  </Step>

  <Step title="Create a notification service">
    Add a class extending `CourierService` and register it in `AndroidManifest.xml`. See the [Android SDK push setup](/sdk-libraries/android#automatic-token-syncing-fcm) for the full steps. Watch the [video walkthrough on GitHub](https://github.com/trycourier/courier-flutter/blob/master/Docs/3_PushNotifications.md#automatically-sync-tokens-android) for a step-by-step guide.
  </Step>
</Steps>

### Token Syncing and Permissions

Request notification permission (iOS shows a system dialog; safe to call on Android where it's a no-op below API 33) and manually sync tokens if you're not using automatic syncing.

```dart  theme={null}
final status = await Courier.shared.requestNotificationPermission();

// Manual token sync (if not using automatic syncing)
await Courier.shared.setToken(provider: "firebase-fcm", token: fcmToken);
```

### Handling Push Events

Register a listener to respond when notifications are delivered or tapped. This is useful for deep linking, analytics, or showing in-app alerts.

```dart  theme={null}
// Listen for push notification events
final listener = await Courier.shared.addPushNotificationListener(
  onPushNotificationDelivered: (push) {
    print("Delivered: ${push.body}");
  },
  onPushNotificationClicked: (push) {
    print("Clicked: ${push.body}");
  },
);

listener.remove();
```

### Send a Test Notification

Once you've completed the setup above, send a test push using the [Send API](/api-reference/send/send-a-message) with `push` as the routing channel. See the [APNS sending guide](/external-integrations/push/apple-push-notification#sending-messages) or [FCM sending guide](/external-integrations/push/firebase-fcm#sending-messages) for complete examples.

## Preferences

Courier Preferences provides a prebuilt widget for users to manage which notification topics and channels they subscribe to.

<Info>
  Topics and sections are configured in the [Preferences Editor](/platform/preferences/preferences-editor). See [Preferences Overview](/platform/preferences/preferences-overview) for how preference enforcement works at send time.
</Info>

<Frame caption="Default Preferences on Flutter">
  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-preferences-default.gif?s=8394a00f01c109c5064f5ebbcf036b37" alt="Default Preferences on Flutter" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-preferences-default.gif" />
</Frame>

```dart  theme={null}
import 'package:courier_flutter/ui/preferences/courier_preferences.dart';

CourierPreferences(
  mode: TopicMode(),
)
```

### Preference Modes

* **Topic mode** (`TopicMode()`): shows subscription topics the user can toggle on or off
* **Channels mode** (`ChannelsMode(channels: [push, sms, email])`): shows per-channel controls for each topic

### Theming

Pass a `CourierPreferencesTheme` to customize fonts, colors, toggle styles, and section headers. Light and dark themes are both supported, and [Courier Studio branding](https://app.courier.com/designer/brands) is automatically applied when a `brandId` is provided.

```dart  theme={null}
final theme = CourierPreferencesTheme(
    brandId: "YOUR_BRAND_ID",
    sectionTitleStyle: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
    topicTitleStyle: TextStyle(fontSize: 18),
    // ... additional style properties
);

CourierPreferences(
  mode: TopicMode(),
  lightTheme: theme,
  darkTheme: theme,
)
```

<Frame caption="Styled Preferences on Flutter">
  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/flutter-preferences-styled.gif?s=795cde4e2558cfdd51fc6f29386f07e9" alt="Styled Preferences on Flutter" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/flutter-preferences-styled.gif" />
</Frame>

## CourierClient

For advanced use cases, `CourierClient` provides direct access to the Courier API:

```dart  theme={null}
final client = CourierClient(
    jwt: "...",
    userId: "your_user_id",
);

// Token management
await client.tokens.putUserToken(token: "...", provider: "apns");       // iOS
await client.tokens.putUserToken(token: "...", provider: "firebase-fcm"); // Android

// Inbox
final messages = await client.inbox.getMessages(paginationLimit: 25);
final unreadCount = await client.inbox.getUnreadMessageCount();
await client.inbox.read(messageId: "...");
await client.inbox.readAll();

// Preferences
final prefs = await client.preferences.getUserPreferences();
await client.preferences.putUserPreferenceTopic(
    topicId: "...",
    status: CourierUserPreferencesStatus.optedIn,
    hasCustomRouting: true,
    customRouting: [CourierUserPreferencesChannel.push],
);

// Branding
final brand = await client.brands.getBrand(brandId: "...");

// URL tracking (from push payloads or inbox messages)
await client.tracking.postTrackingUrl(url: trackingUrl, event: CourierTrackingEvent.delivered);
```

See the full API reference on [GitHub](https://github.com/trycourier/courier-flutter/blob/master/Docs/5_Client.md).

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

  <Card title="GitHub" href="https://github.com/trycourier/courier-flutter" icon="github">
    Source code, examples, and changelog
  </Card>
</CardGroup>
