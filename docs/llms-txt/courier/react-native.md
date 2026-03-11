# Source: https://www.courier.com/docs/sdk-libraries/react-native.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Courier React Native SDK

> Add in-app notifications, push notifications, and notification preferences to your React Native app with prebuilt components and TypeScript APIs.

The Courier React Native SDK provides prebuilt components and APIs for building notification experiences in React Native. It handles authentication, token management, and real-time message delivery across iOS and Android from a single codebase.

* **[Inbox](#inbox)** — prebuilt notification center with theming and custom rendering
* **[Push Notifications](#push-notifications)** — automatic token syncing and delivery tracking for APNS and FCM
* **[Preferences](#preferences)** — prebuilt UI for users to manage their notification settings

Available on
<Link href="https://github.com/trycourier/courier-react-native"><Icon icon="github" iconType="solid" /> GitHub</Link>
and <Link href="https://www.npmjs.com/package/@trycourier/courier-react-native"><Icon icon="npm" iconType="solid" /> npm</Link>.

| Requirement     | Value |
| --------------- | ----- |
| Min iOS version | 15.0  |
| Min Android SDK | 23    |
| Gradle          | 8.4+  |

## Installation

<CodeGroup>
  ```bash npm theme={null}
  npm install @trycourier/courier-react-native
  ```

  ```bash yarn theme={null}
  yarn add @trycourier/courier-react-native
  ```
</CodeGroup>

### iOS Setup

<Steps>
  <Step title="Set iOS deployment target to 15.0+">
    Update your Podfile:

    ```ruby  theme={null}
    platform :ios, '15.0'
    ```
  </Step>

  <Step title="Install CocoaPods">
    ```bash  theme={null}
    cd ios && pod install
    ```
  </Step>
</Steps>

### Android Setup

<Steps>
  <Step title="Add the Jitpack repository">
    In your `android/build.gradle`:

    ```gradle  theme={null}
    allprojects {
        repositories {
            google()
            mavenCentral()
            maven { url 'https://www.jitpack.io' }
        }
    }
    ```
  </Step>

  <Step title="Set minimum SDK version">
    In your `android/build.gradle`:

    ```gradle  theme={null}
    ext {
        minSdkVersion = 23
        compileSdkVersion = 33
        targetSdkVersion = 33
    }
    ```
  </Step>

  <Step title="Extend CourierReactNativeActivity">
    Update your `MainActivity` to extend `CourierReactNativeActivity`. This allows the SDK to manage user state across app sessions.

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      import com.courierreactnative.CourierReactNativeActivity

      class MainActivity : CourierReactNativeActivity() {
          // ...
      }
      ```

      ```java Java theme={null}
      import com.courierreactnative.CourierReactNativeActivity;

      public class MainActivity extends CourierReactNativeActivity {
          // ...
      }
      ```
    </CodeGroup>
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

    ```typescript  theme={null}
    import Courier from "@trycourier/courier-react-native";

    await Courier.shared.signIn({
        userId: "your_user_id",
        accessToken: jwt,
    });
    ```
  </Step>

  <Step title="Sign out when done">
    ```typescript  theme={null}
    await Courier.shared.signOut();
    ```
  </Step>
</Steps>

You can listen for authentication state changes:

```typescript  theme={null}
const listener = Courier.shared.addAuthenticationListener({
    onUserChanged: (userId) => {
        console.log("User changed:", userId);
    },
});

listener.remove();
```

## Inbox

Courier Inbox provides a prebuilt notification center component. It supports theming and real-time updates on both iOS and Android.

<Tip>
  Inbox requires the [Courier Inbox provider](https://app.courier.com/channels/courier) to be enabled in your workspace. If using JWT authentication, enable JWT support in the provider settings.

  <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/courier-jwt-toggle.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=214922b19e181b120f70ed4850b69b9a" alt="JWT toggle in Courier provider settings" width="385" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/courier-jwt-toggle.png" />
</Tip>

<Note>
  On Android, your app theme must extend `Theme.MaterialComponents` for the prebuilt UI to render correctly. Set this in your `res/values/styles.xml`.
</Note>

<Info>
  For an overview of how Courier Inbox works and how to send messages to it from your backend, see [Get Started with Inbox](/platform/inbox/inbox-overview) and [Send an Inbox Message](/platform/inbox/sending-a-message).
</Info>

### Prebuilt Component

<Frame caption="Default Inbox on iOS and Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-inbox-default.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=e6844e7c3baf6cc83508000c6cc04dbb" alt="Default Inbox on iOS" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-inbox-default.png" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-inbox-default.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=86ae9079bb5fdc4143972dc5d3f9b797" alt="Default Inbox on Android" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-inbox-default.png" />
  </div>
</Frame>

```jsx  theme={null}
import { CourierInboxView } from "@trycourier/courier-react-native";

<CourierInboxView
  onClickInboxMessageAtIndex={(message, index) => {
    message.read
      ? Courier.shared.unreadMessage({ messageId: message.messageId })
      : Courier.shared.readMessage({ messageId: message.messageId });
  }}
  onClickInboxActionForMessageAtIndex={(action, message, index) => {
    console.log(action);
  }}
  style={{ flex: 1 }}
/>
```

### Theming

Pass a theme object to customize the inbox appearance. The theme supports separate iOS and Android style properties, custom fonts, colors, and button styles.

```typescript  theme={null}
<CourierInboxView
  lightTheme={{
    iOS: {
      unreadIndicatorStyle: { indicator: "dot", color: "#9747FF" },
      titleStyle: { unread: { font: { family: "Avenir", size: 18 } } },
      // ... additional iOS styles
    },
    android: {
      unreadIndicatorStyle: { indicator: "dot", color: "#9747FF" },
      titleStyle: { unread: { font: { family: "fonts/poppins.otf", size: 18 } } },
      // ... additional Android styles
    },
  }}
/>
```

<Frame caption="Styled Inbox on iOS and Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-inbox-styled.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=03b368e1ad9ad77ef2ab85dd92814abd" alt="Styled Inbox on iOS" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-inbox-styled.png" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-inbox-styled.png?fit=max&auto=format&n=iZIqSLNN7hLm8RQn&q=85&s=6bc18219d2a66f2dbba56662f338ac01" alt="Styled Inbox on Android" width="300" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-inbox-styled.png" />
  </div>
</Frame>

You can also apply branding from [Courier Studio](https://app.courier.com/designer/brands). The SDK supports primary color and footer visibility from your brand settings.

### Custom Inbox UI

For full control over rendering, use `addInboxListener` to receive raw message data and build your own UI:

```typescript  theme={null}
const listener = await Courier.shared.addInboxListener({
    onLoading: (isRefresh) => {
        // Show loading state
    },
    onError: (error) => {
        // Handle error
    },
    onMessagesChanged: (messages, canPaginate, feed) => {
        // Update your custom UI with messages
    },
    onUnreadCountChanged: (unreadCount) => {
        // Update badge indicators
    },
    onTotalCountChanged: (totalCount, feed) => {
        // Track total messages per feed
    },
    onPageAdded: (messages, canPaginate, isFirstPage, feed) => {
        // Efficiently append new pages during pagination
    },
    onMessageEvent: (message, index, feed, eventName) => {
        // React to individual events: read, unread, archived, opened, added
    },
});

// Clean up
listener.remove();
```

### Message Actions

```typescript  theme={null}
await Courier.shared.readMessage({ messageId: "..." });
await Courier.shared.unreadMessage({ messageId: "..." });
await Courier.shared.archiveMessage({ messageId: "..." });
await Courier.shared.readAllInboxMessages();
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
| Permission requests        | Yes | Yes     |

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
    In Xcode: select your target > Signing & Capabilities > add Push Notifications. Watch the [video walkthrough on GitHub](https://github.com/trycourier/courier-react-native/blob/master/Docs/3_PushNotifications.md#1-enable-the-push-notifications-capability) for a step-by-step guide.
  </Step>

  <Step title="Add a Notification Service Extension">
    This enables delivery tracking when the app is not running. See the [iOS SDK push setup](/sdk-libraries/ios#notification-service-extension) for the full steps.
  </Step>
</Steps>

### Android Push Setup

<Steps>
  <Step title="Set up Firebase">
    Follow the [Firebase Android setup guide](https://firebase.google.com/docs/android/setup) and add `google-services.json` to your app. Watch the [video walkthrough on GitHub](https://github.com/trycourier/courier-react-native/blob/master/Docs/3_PushNotifications.md#1-add-firebase) for a step-by-step guide.
  </Step>

  <Step title="Create a notification service">
    Add a class extending `CourierService` and register it in `AndroidManifest.xml`. See the [Android SDK push setup](/sdk-libraries/android#automatic-token-syncing-fcm) for the full steps.
  </Step>
</Steps>

### Handling Push Events

Register a listener to respond when notifications are delivered or tapped. This is useful for deep linking, analytics, or showing in-app alerts.

```typescript  theme={null}
const listener = await Courier.shared.addPushNotificationListener({
    onPushNotificationDelivered: (push) => {
        console.log("Delivered:", push);
    },
    onPushNotificationClicked: (push) => {
        console.log("Clicked:", push);
    },
});

listener.remove();
```

### Requesting Permission

Prompt the user to allow notifications (iOS shows a system dialog; Android 13+ requires runtime permission). You can also check the current permission status without prompting.

```typescript  theme={null}
const status = await Courier.shared.requestNotificationPermission();
const isGranted = await Courier.shared.getNotificationPermissionStatus();
```

### Send a Test Notification

Once you've completed the setup above, send a test push using the [Send API](/api-reference/send/send-a-message) with `push` as the routing channel. See the [APNS sending guide](/external-integrations/push/apple-push-notification#sending-messages) or [FCM sending guide](/external-integrations/push/firebase-fcm#sending-messages) for complete examples.

## Preferences

Courier Preferences provides a prebuilt component for users to manage which notification topics and channels they subscribe to.

<Info>
  Topics and sections are configured in the [Preferences Editor](/platform/preferences/preferences-editor). See [Preferences Overview](/platform/preferences/preferences-overview) for how preference enforcement works at send time.
</Info>

<Frame caption="Default Preferences on iOS and Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-preferences-default.gif?s=7ccc1f70a8ab6c51bf9627a9b7a3281c" alt="Default Preferences on iOS" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-preferences-default.gif" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-preferences-default.gif?s=748931e662d547de3a1227d9a18b6a85" alt="Default Preferences on Android" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-preferences-default.gif" />
  </div>
</Frame>

```jsx  theme={null}
import { CourierPreferencesView } from "@trycourier/courier-react-native";

<CourierPreferencesView
  mode={{ type: "topic" }}
  style={{ flex: 1 }}
/>
```

### Preference Modes

* **Topic mode** (`{ type: "topic" }`): shows subscription topics the user can toggle on or off
* **Channels mode** (`{ type: "channels", channels: ["push", "sms", "email"] }`): shows per-channel controls for each topic

### Theming

Pass a theme object with platform-specific style properties to customize fonts, colors, and toggle styles.

<Frame caption="Styled Preferences on iOS and Android">
  <div style={{ display: "flex", gap: "16px", justifyContent: "center" }}>
    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/ios-preferences-styled.gif?s=e740a619288899725cfcbad1f07ed5cd" alt="Styled Preferences on iOS" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/ios-preferences-styled.gif" />

    <img src="https://mintcdn.com/courier-4f1f25dc/iZIqSLNN7hLm8RQn/assets/sdks/mobile/android-preferences-styled.gif?s=0ee58d84f4f57937134e5b816543e33a" alt="Styled Preferences on Android" width="250" style={{ borderRadius: "8px" }} data-path="assets/sdks/mobile/android-preferences-styled.gif" />
  </div>
</Frame>

## Expo

If you are using Expo, additional setup is required for push notification token syncing. You'll need to update your `AppDelegate` (iOS) and `MainActivity` (Android) with Courier-specific code since Expo manages these files differently.

See the full [Expo setup guide on GitHub](https://github.com/trycourier/courier-react-native/blob/master/Docs/6_Expo.md) for step-by-step instructions for both platforms.

## CourierClient

For advanced use cases, `CourierClient` provides direct access to the Courier API:

```typescript  theme={null}
const client = new CourierClient({
    jwt: "...",
    userId: "your_user_id",
});

// Token management
await client.tokens.putUserToken({ token: "...", provider: "apns" });        // iOS
await client.tokens.putUserToken({ token: "...", provider: "firebase-fcm" }); // Android

// Inbox
const messages = await client.inbox.getMessages({ paginationLimit: 25 });
const unreadCount = await client.inbox.getUnreadMessageCount();
await client.inbox.read({ messageId: "..." });
await client.inbox.readAll();

// Preferences
const prefs = await client.preferences.getUserPreferences();
await client.preferences.putUserPreferenceTopic({
    topicId: "...",
    status: CourierUserPreferencesStatus.OptedIn,
    hasCustomRouting: true,
    customRouting: [CourierUserPreferencesChannel.Push],
});

// Branding
const brand = await client.brands.getBrand({ brandId: "..." });

// URL tracking (from push payloads or inbox messages)
await client.tracking.postTrackingUrl({
    url: "courier_tracking_url",
    event: CourierTrackingEvent.Delivered,
});

// Clean up
client.remove();
```

See the full API reference on [GitHub](https://github.com/trycourier/courier-react-native/blob/master/Docs/5_Client.md).

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

  <Card title="GitHub" href="https://github.com/trycourier/courier-react-native" icon="github">
    Source code, examples, and changelog
  </Card>
</CardGroup>
