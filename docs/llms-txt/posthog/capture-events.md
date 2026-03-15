# Source: https://posthog.com/docs/product-analytics/capture-events.md

# Capturing events - Docs

Once your PostHog instance is up and running, the next step is to start sending events.

## Web

By default, PostHog automatically captures pageviews and pageleaves as well as clicks, change of inputs, and form submissions associated with `a`, `button`, `form`, `input`, `select`, `textarea`, and `label` tags. See our [autocapture docs](/docs/product-analytics/autocapture.md) for more details on this.

If you prefer to disable or filter these, set the appropriate values in your [configuration options](/docs/libraries/js/config.md).

### Custom event capture

You can send custom events using `capture`:

Web

PostHog AI

```javascript
posthog.capture('user_signed_up');
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

> **Tip:** You can define event schemas with typed properties and generate type-safe code using [schema management](/docs/product-analytics/schema-management.md).

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Web

PostHog AI

```javascript
posthog.capture('user_signed_up', {
    login_type: "email",
    is_free_trial: true
})
```

## Node.js

You can send custom events using `capture`:

Node.js

PostHog AI

```javascript
client.capture({
    distinctId: 'distinct_id_of_the_user',
    event: 'user signed up',
})
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Node.js

PostHog AI

```javascript
client.capture({
  distinctId: 'distinct_id_of_the_user',
  event: 'user signed up',
  properties: {
    login_type: 'email',
    is_free_trial: true,
  },
})
```

### Capturing pageviews

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `$pageview` events from your backend like so:

Node.js

PostHog AI

```javascript
client.capture({
  distinctId: 'distinct_id_of_the_user',
  event: '$pageview',
  properties: {
    $current_url: 'https://example.com',
  },
})
```

## Python

You can send custom events using `capture`:

Python

PostHog AI

```python
# Events captured with no context or explicit distinct_id are marked as personless and have an auto-generated distinct_id:
posthog.capture('some-anon-event')
from posthog import identify_context, new_context
# Use contexts to manage user identification across multiple capture calls
with new_context():
    identify_context('distinct_id_of_the_user')
    posthog.capture('user_signed_up')
    posthog.capture('user_logged_in')
    # You can also capture events with a specific distinct_id
    posthog.capture('some-custom-action', distinct_id='distinct_id_of_the_user')
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

> **Tip:** You can define event schemas with typed properties and generate type-safe code using [schema management](/docs/product-analytics/schema-management.md).

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Python

PostHog AI

```python
posthog.capture(
    "user_signed_up",
    distinct_id="distinct_id_of_the_user",
    properties={
        "login_type": "email",
        "is_free_trial": "true"
    }
)
```

### Sending page views

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `pageviews` from your backend like so:

Python

PostHog AI

```python
posthog.capture('$pageview', distinct_id="distinct_id_of_the_user", properties={'$current_url': 'https://example.com'})
```

## PHP

You can send custom events using `capture`:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => 'user_signed_up'
]);
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => 'user_signed_up',
  'properties' => [
    'login_type' => 'email',
    'is_free_trial' => 'true'
  ]
]);
```

### Sending page views

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `pageviews` from your backend like so:

PHP

PostHog AI

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => '$pageview',
  'properties' => [
    '$current_url' => 'https://example.com'
  ]
]);
```

## Ruby

You can send custom events using `capture`:

Ruby

PostHog AI

```ruby
posthog.capture({
    distinct_id: 'distinct_id_of_the_user',
    event: 'user_signed_up'
})
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Ruby

PostHog AI

```ruby
posthog.capture({
    distinct_id: 'distinct_id_of_the_user',
    event: 'user_signed_up',
    properties: {
        login_type: 'email',
        is_free_trial: true
    }
})
```

### Sending pageviews

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `pageviews` from your backend like so:

Ruby

PostHog AI

```ruby
posthog.capture({
    distinct_id: 'distinct_id_of_the_user',
    event: '$pageview',
    properties: {
        '$current_url': 'https://example.com'
    }
})
```

## Go

You can send custom events using `capture`:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_the_user",
  Event: "user_signed_up",
})
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

> **Tip:** You can define event schemas with typed properties and generate type-safe code using [schema management](/docs/product-analytics/schema-management.md).

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id_of_the_user",
    Event:      "user_signed_up",
    Properties: posthog.NewProperties().
      Set("login_type", "email").
      Set("is_free_trial", true),
  })
```

### Capturing pageviews

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `pageviews` from your backend like so:

Go

PostHog AI

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_the_user",
  Event:      "$pageview",
  Properties: posthog.NewProperties().
    Set("$current_url", "https://example.com"),
})
```

## React

By default, PostHog automatically captures pageviews and pageleaves as well as clicks, change of inputs, and form submissions associated with `a`, `button`, `form`, `input`, `select`, `textarea`, and `label` tags. See our [autocapture docs](/docs/product-analytics/autocapture.md) for more details on this.

If you prefer to disable or filter these, set the appropriate values in your [configuration options](/docs/libraries/js/config.md).

## Capturing custom events

After setting up the PostHog provider, you can use the `usePostHog` hook to access all the methods of the `posthog-js` library including `capture` which lets you capture custom events with optional properties.

JavaScript

PostHog AI

```javascript
import { usePostHog } from '@posthog/react'
function App() {
  const posthog = usePostHog()
  const signUpClicked = () => {
    posthog?.capture('clicked_sign_up', {
      signup_method: 'email'
    })
  }
  return (
    <div className="App">
      <button onClick={() => posthog?.capture('button_clicked')}>Click me</button>
      <button onClick={signUpClicked}>Sign up</button>
    </div>
  )
}
export default App
```

## React Native

You can send custom events using `capture`:

React Native

PostHog AI

```jsx
posthog.capture('user_signed_up')
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

React Native

PostHog AI

```jsx
posthog.capture('user_signed_up', {
    login_type: "email",
    is_free_trial: true
})
```

### Capturing screen views

#### With `@react-navigation/native` and autocapture:

When using [@react-navigation/native](https://reactnavigation.org/docs/6.x/getting-started) v6 or lower, screen tracking is automatically captured if the [`autocapture`](/docs/libraries/react-native.md#autocapture) property is used in the `PostHogProvider`:

It is important that the `PostHogProvider` is configured as a child of the `NavigationContainer`:

React Native

PostHog AI

```jsx
// App.(js|ts)
import { PostHogProvider } from 'posthog-react-native'
import { NavigationContainer } from '@react-navigation/native'
export function App() {
    return (
        <NavigationContainer>
            <PostHogProvider apiKey="<ph_project_token>" autocapture>
                {/* Rest of app */}
            </PostHogProvider>
        </NavigationContainer>
    )
}
```

When using [@react-navigation/native](https://reactnavigation.org/docs/7.x/getting-started) v7 or higher, screen tracking has to be manually captured:

React Native

PostHog AI

```jsx
// App.(js|ts)
import { PostHogProvider } from 'posthog-react-native'
import { NavigationContainer } from '@react-navigation/native'
// Using `PostHogProvider` is optional, but needed if you want to capture touch events automatically with the `captureTouches` option.
export function App() {
    return (
        <NavigationContainer>
            <PostHogProvider apiKey="<ph_project_token>" autocapture={{
              captureScreens: false, // Screen events are handled differently for v7 and higher
              captureTouches: true,
            }}>
                {/* Rest of app */}
            </PostHogProvider>
        </NavigationContainer>
    )
}
```

Check out and set it up the official way for [Screen tracking for analytics](https://reactnavigation.org/docs/screen-tracking/).

Then call the `screen` method within the `trackScreenView` method.

React Native

PostHog AI

```jsx
const posthog = usePostHog() // use the usePostHog hook if using the PostHogProvider or your own custom posthog instance
// you can read the params from `getCurrentRoute()`
posthog.screen(currentRouteName, params)
```

#### With `react-native-navigation` and autocapture:

First, simplify the wrapping of your screens with a shared PostHogProvider:

React Native

PostHog AI

```jsx
import PostHog, { PostHogProvider } from 'posthog-react-native'
import { Navigation } from 'react-native-navigation';
export const posthog = new PostHog('<ph_project_token>');
export const SharedPostHogProvider = (props: any) => {
  return (
    <PostHogProvider client={posthog} autocapture={{
      captureScreens: false, // Screen events are handled differently for react-native-navigation
      captureTouches: true,
    }}>
      {props.children}
    </PostHogProvider>
  );
};
```

Then, every screen needs to be wrapped with this provider if you want to capture touches or use the `usePostHog()` hook

React Native

PostHog AI

```jsx
export const MyScreen = () => {
  return (
    <SharedPostHogProvider>
      <View>
        ...
      </View>
    </SharedPostHogProvider>
  );
};
Navigation.registerComponent('Screen', () => MyScreen);
Navigation.events().registerAppLaunchedListener(async () => {
  posthog.initReactNativeNavigation({
    navigation: {
      // (Optional) Set the name based on the route. Defaults to the route name.
      routeToName: (name, properties) => name,
      // (Optional) Tracks all passProps as properties. Defaults to undefined
      routeToProperties: (name, properties) => properties,
    },
    captureScreens: true,
  });
});
```

#### With `expo-router`:

Check out and set it up the official way for [Screen tracking for analytics](https://docs.expo.dev/router/reference/screen-tracking/).

Then call the `screen` method within the `useEffect` callback.

React Native

PostHog AI

```jsx
const posthog = usePostHog() // use the usePostHog hook if using the PostHogProvider or your own custom posthog instance
posthog.screen(pathname, params)
```

#### Manually capturing screen capture events

If you prefer not to use autocapture, you can manually capture screen views by calling `posthog.screen()`. This function requires a `name`. You may also pass in an optional `properties` object.

JavaScript

PostHog AI

```javascript
posthog.screen('dashboard', {
    background: 'blue',
    hero: 'superhog',
})
```

## Android

You can send custom events using `capture`:

Kotlin

PostHog AI

```kotlin
import com.posthog.PostHog
PostHog.capture(event = "user_signed_up")
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Kotlin

PostHog AI

```kotlin
import com.posthog.PostHog
PostHog.capture(
    event = "user_signed_up",
    properties = mapOf(
        "login_type" to "email",
        "is_free_trial" to true
    )
)
```

### Autocapture

PostHog autocapture automatically tracks the following events for you:

-   **Application Opened** - when the app is opened from a closed state or when the app comes to the foreground. (e.g. from the app switcher)
-   **Deep Link Opened** - when the app is opened from a deep link.
-   **Application Backgrounded** - when the app is sent to the background by the user.
-   **Application Installed** - when the app is installed.
-   **Application Updated** - when the app is updated.
-   **$screen** - when the user navigates. (if using `android.app.Activity`)
-   **$exception** - when the app throws exceptions.

### Capturing screen views

With [`captureScreenViews = true`](/docs/libraries/android.md#all-configuration-options), PostHog will try to record all screen changes automatically.

The `screenTitle` will be the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)'s `android:label`, if not set it'll fallback to the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element)'s `android:label` or the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)'s `android:name`.

XML

PostHog AI

```xml
<activity
    android:name="com.example.app.ChildActivity"
    android:label="@string/title_child_activity"
    ...
</activity>
```

If you want to manually send a new screen capture event, use the `screen` function.

This function requires a `screenTitle`. You may also pass in an optional `properties` object.

Kotlin

PostHog AI

```kotlin
import com.posthog.PostHog
PostHog.screen(
    screenTitle = "Dashboard",
    properties = mapOf(
        "background" to "blue",
        "hero" to "superhog"
    )
)
```

## iOS

You can send custom events using `capture`:

Swift

PostHog AI

```swift
PostHogSDK.shared.capture("user_signed_up")
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Swift

PostHog AI

```swift
PostHogSDK.shared.capture("user_signed_up", properties: ["login_type": "email"], userProperties: ["is_free_trial": true])
```

## Autocapture

PostHog autocapture automatically tracks the following events for you:

-   **Application Opened** - when the app is opened from a closed state or when the app comes to the foreground (e.g. from the app switcher)
-   **Application Backgrounded** - when the app is sent to the background by the user
-   **Application Installed** - when the app is installed
-   **Application Updated** - when the app is updated
-   **$screen** - when the user navigates (if using `UIViewController`)
-   **$autocapture** - when the user interacts with elements in a screen (if using `UIKit`)

> 🚧 **Note:** `$autocapture` captures interactions with UIKit elements. Some SwiftUI views use UIKit under the hood (e.g., `TextField` → `UITextField`, `Toggle` → `UISwitch`) and will also be autocaptured.

### Capturing screen views

With [`configuration.captureScreenViews`](/docs/libraries/ios/configuration.md#all-configuration-options) set as `true`, PostHog will try to record all screen changes automatically.

If you want to manually send a new screen capture event, use the `screen` function.

Swift

PostHog AI

```swift
PostHogSDK.shared.screen("Dashboard", properties: ["fromIcon": "bottom"])
```

> **Important:** While `captureScreenViews` works with both `UIKit` and `SwiftUI`, the screen names captured in `SwiftUI` may not be very meaningful as they are based on internal SwiftUI view identifiers. For `SwiftUI` applications, we recommend turning this option off and instead using the `.postHogScreenView()` view modifier (see next section) to capture screen views with meaningful names.

> **Note:** You can use the `BeforeSendBlock` to filter or drop any undesired screen events, giving you control over which screen views are sent to PostHog. See [Amending, dropping or sampling events](/docs/libraries/ios.md#amending-dropping-or-sampling-events) for implementation examples.

### Capturing screen views in SwiftUI

To track a screen view in `SwiftUI`, apply the `postHogScreenView` modifier to your full-screen views. PostHog will send a `$screen` event when the `onAppear` action is executed and will infer a screen name based on the view’s type. You can provide a custom name and event properties if needed.

HomeView.swift

PostHog AI

```swift
// This will trigger a screen view event with $screen_name: "HomeViewContent"
struct HomeView: View {
    var body: some View {
        HomeViewContent()
            .postHogScreenView()
    }
}
// This will trigger a screen view event with $screen_name: "My Home View" and an additional event property from_button: "start"
struct HomeView: View {
    var body: some View {
        HomeViewContent()
            .postHogScreenView("My Home View", ["from_button": "start"])
    }
}
```

In SwiftUI, views can range from entire screens to small UI components. Unlike UIKit, SwiftUI doesn’t clearly distinguish between these levels, which makes automatic tracking of full-screen views harder.

### Adding a custom label on autocaptured elements

PostHog automatically captures interactions with various UI elements in your app, but these interactions are often identified by element type names (e.g., UIButton, UITextField, UILabel).

While this provides basic tracking, it can be challenging to pinpoint specific interactions with particular elements in your analytics. To make your data more meaningful and actionable, you can assign custom labels to any autocaptured element. These labels act as descriptive identifiers, making it easier to identify, filter, and analyze events in your reports.

**Adding a custom label in UIKit**

To assign a custom label to a UIView, use the `postHogLabel` property:

Swift

PostHog AI

```swift
let view = UIView()
view.postHogLabel = "usernameTextField"
```

In this example, interactions with the UITextField will be captured with an additional identifier "usernameTextField".

**Adding a custom label in SwiftUI**

In SwiftUI, use the `.postHogLabel(_:)` modifier instead:

Swift

PostHog AI

```swift
var body: some View {
    ...
    TextField("username", text: $username)
        .postHogLabel("usernameTextField")
}
```

Since SwiftUI's `TextField` uses `UITextField` under the hood, interactions with it will be autocaptured with the additional identifier "usernameTextField".

**Example of generated analytics data**

The generated analytics element in the examples above will have the following form:

Swift

PostHog AI

```swift
<UITextField id="usernameTextField">text value</UITextField>
```

**Filtering for labeled autocaptured elements in reports**

To locate and filter interactions with specific elements in PostHog reports, you can use Autocapture element filters, such as:

-   Tag Name (`UITextField` in this example)
-   Text (`text value` in this example)
-   CSS Selector (the generated `id` attribute in this example)

In the examples above, we can filter for the specific text field using the CSS Selector `#usernameTextField`

### Interaction autocapture

Interaction autocapture records when users interact with UI elements in your app. This includes:

-   User interactions like `touch`, `swipe`, `pan`, `pinch`, `rotation`, `long_press`, `scroll`
-   Control types `value_changed`, `submit`, `toggle`, `primary_action`, `menu_action`, `change`

Interaction autocapture is **not enabled by default**. You can enable it by setting `captureElementInteractions` to `true` in the config.

Swift

PostHog AI

```swift
let config = PostHogConfig(apiKey: <ph_project_token>, host: https://us.i.posthog.com)
config.captureElementInteractions = true // Disabled by default
PostHogSDK.shared.setup(config)
```

### Autocapture configuration

You can enable or disable autocapture through the `PostHogConfig` object. Find more details about autocapture configuration in the [configuration page](/docs/libraries/ios/configuration.md#autocapture-configuration).

## Java

You can send custom events using `capture`:

Java

PostHog AI

```java
posthog.capture("distinct_id_of_the_user", "user_signed_up");
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Java

PostHog AI

```java
posthog.capture(
    "distinct_id_of_the_user",
    "user_signed_up",
    PostHogCaptureOptions
        .builder()
        .property("login_type", "email")
        .property("is_free_trial", true)
        .build());
```

## Rust

You can send custom events using `capture`:

Rust

PostHog AI

```rust
let mut event = Event::new("user_signed_up", "distinct_id_of_the_user");
client.capture(event).unwrap();
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Rust

PostHog AI

```rust
let mut event = Event::new("user_signed_up", "distinct_id_of_the_user");
event.insert_prop("login_type", "email").unwrap();
event.insert_prop("is_free_trial", true).unwrap();
client.capture(event).unwrap();
```

### Batching events

To capture multiple events at once, use `batch()`:

Rust

PostHog AI

```rust
let event1 = posthog_rs::Event::new("event 1", "distinct_id_of_user_A");
let event2 = posthog_rs::Event::new("event 2", "distinct_id_of_user_B");
client.capture_batch(vec![event1, event2]).unwrap();
```

## Elixir

To capture an event, use `PostHog.capture/2`:

Elixir

PostHog AI

```elixir
PostHog.capture("user_signed_up", %{distinct_id: "distinct_id_of_the_user"})
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Elixir

PostHog AI

```elixir
PostHog.capture("user_signed_up", %{
  distinct_id: "distinct_id_of_the_user",
  login_type: "email",
  is_free_trial: true
})
```

### Context

Carrying `distinct_id` around all the time might not be the most convenient approach, so PostHog lets you store it and other properties in a context.

The context is stored in the `Logger` metadata and PostHog automatically attaches these properties to any events you capture with `PostHog.capture/2`, as long as they happen in the same process.

Elixir

PostHog AI

```elixir
PostHog.set_context(%{distinct_id: "distinct_id_of_the_user"})
PostHog.capture("page_opened")
```

You can also scope the context to a specific event name:

Elixir

PostHog AI

```elixir
PostHog.set_event_context("sensitive_event", %{"$process_person_profile": false})
```

### Batching events

Events are automatically batched and sent to PostHog via a background job.

### Special events

`PostHog.capture/2` is very powerful and enables you to send events that have special meaning.

In other libraries you'll usually find helpers for these special events, but they must be explicitly sent in Elixir.

For example:

#### Create alias

Elixir

PostHog AI

```elixir
PostHog.capture("$create_alias", %{distinct_id: "frontend_id", alias: "backend_id"})
```

#### Group analytics

Elixir

PostHog AI

```elixir
PostHog.capture("$groupidentify", %{
  distinct_id: "static_string_used_for_all_group_events",
  "$group_type": "company",
  "$group_key": "company_id_in_your_db"
})
```

## Flutter

You can send custom events using `capture`:

Dart

PostHog AI

```dart
await Posthog().capture(
  eventName: 'user_signed_up',
);
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Dart

PostHog AI

```dart
await Posthog().capture(
  eventName: 'user_signed_up',
  properties: {
    'login_type': 'email',
    'is_free_trial': true
  }
);
```

### Autocapture

PostHog autocapture automatically tracks the following events for you:

-   **Application Opened** - when the app is opened from a closed state or when the app comes to the foreground (e.g. from the app switcher)
-   **Application Backgrounded** - when the app is sent to the background by the user
-   **Application Installed** - when the app is installed.
-   **Application Updated** - when the app is updated.
-   **$screen** - when the user navigates (if using [navigatorObservers](https://docs.flutter.dev/ui/navigation) or [go\_router](https://pub.dev/packages/go_router). You'd need to set up the `PosthogObserver` manually.)
-   **$exception** - when the app throws exceptions.

### Capturing screen views

> Note: Your routes should be named. Otherwise, they won't be recorded.

#### Using `navigatorObservers`

Add the `PosthogObserver` to record screen views automatically:

Dart

PostHog AI

```dart
import 'package:flutter/material.dart';
import 'package:posthog_flutter/posthog_flutter.dart';
void main() => runApp(MyApp());
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // If you're using session replay, `PostHogWidget` has to be the root, and `MaterialApp` must be the child.
    return MaterialApp(
      navigatorObservers: [
        // The PosthogObserver records screen views automatically
        PosthogObserver(),
      ],
      ...
    );
  }
}
```

Name your routes:

Dart

PostHog AI

```dart
...
MaterialPageRoute(builder: (context) => const HomeScreenRoute(),
  settings: const RouteSettings(name: 'Home Screen'),
),
...
```

#### Using `go_router`

Add the `PosthogObserver` to record screen views automatically:

Dart

PostHog AI

```dart
import 'package:flutter/material.dart';
import 'package:posthog_flutter/posthog_flutter.dart';
import 'package:go_router/go_router.dart';
// GoRouter configuration
final _router = GoRouter(
  routes: [
    ...
  ],
  // The PosthogObserver records screen views automatically
  observers: [PosthogObserver()],
);
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // If you're using session replay, `PostHogWidget` has to be the root, and `MaterialApp` must be the child.
    return MaterialApp.router(
      routerConfig: _router,
    );
  }
}
```

Name your routes:

Dart

PostHog AI

```dart
...
GoRoute(
  name: 'Home Screen',
  ...
),
...
```

## .NET

You can send custom events using `capture`:

C#

PostHog AI

```csharp
posthog.Capture("distinct_id_of_the_user", "user_signed_up");
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

C#

PostHog AI

```csharp
posthog.Capture(
    "distinct_id_of_the_user",
    "user_signed_up",
    properties: new() {
        ["login_type"] = "email",
        ["is_free_trial"] = "true"
    }
);
```

### Sending page views

If you're aiming for a backend-only implementation of PostHog and won't be capturing events from your frontend, you can send `$pageview` events from your backend like so:

C#

PostHog AI

```csharp
using PostHog;
using Microsoft.AspNetCore.Http.Extensions;
posthog.CapturePageView(
    "distinct_id_of_the_user",
    HttpContext.Request.GetDisplayUrl());
```

## API

You can send custom events using `capture`:

Terminal

PostHog AI

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_the_user",
    "event": "user_signed_up"
}' https://us.i.posthog.com/i/v0/e/
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Terminal

PostHog AI

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "properties": {
        "login_type": "email",
        "is_free_trial": "true"
    },
    "distinct_id": "distinct_id_of_the_user",
    "event": "user_signed_up"
}' https://us.i.posthog.com/i/v0/e/
```

### Batching events

Events can be sent together in a batch. There is no limit on the number of events you can send in a batch, but the entire request body must be less than `20MB` by default.

Terminal

PostHog AI

```shell
POST https://us.i.posthog.com/batch/
Content-Type: application/json
Body:
{
    "api_key": "<ph_project_token>",
    "batch": [
        {
            "event": "event_name",
            "properties": {
                "distinct_id": "distinct_id_of_the_user",
                "key1": "value1",
                "key2": "value2"
            },
        },
        ...
    ]
}
```

## Event ingestion

It's a priority for us that events are fully processed and saved as soon as possible. Typically, events will be usable in queries within a few minutes.

## Advanced: Anonymous vs identified events

PostHog captures two types of events: [**anonymous** and **identified**](/docs/data/anonymous-vs-identified-events.md)

**Identified events** enable you to attribute events to specific users, and attach [person properties](/docs/product-analytics/person-properties.md). They're best suited for logged-in users.

Scenarios where you want to capture identified events are:

-   Tracking logged-in users in B2B and B2C SaaS apps
-   Doing user segmented product analysis
-   Growth and marketing teams wanting to analyze the *complete* conversion lifecycle

**Anonymous events** are events without individually identifiable data. They're best suited for [web analytics](/docs/web-analytics.md) or apps where users aren't logged in.

Scenarios where you want to capture anonymous events are:

-   Tracking a marketing website
-   Content-focused sites
-   B2C apps where users don't sign up or log in

Under the hood, the key difference between identified and anonymous events is that for identified events we create a [person profile](/docs/data/persons.md) for the user, whereas for anonymous events we do not.

> **Important:** Due to the reduced cost of processing them, anonymous events can be up to 4x cheaper than identified ones, so we recommended you only capture identified events when needed.

### How to capture anonymous events

## Web

The JavaScript Web SDK captures anonymous events by default. However, this may change depending on your [`person_profiles` config](/docs/libraries/js/config.md) when initializing PostHog:

1.  `person_profiles: 'identified_only'` *(recommended)* *(default)* - Anonymous events are captured by default. PostHog only captures identified events for users where [person profiles](/docs/data/persons.md) have already been created.

2.  `person_profiles: 'always'` - Capture identified events for all events.

For example:

Web

PostHog AI

```javascript
posthog.init('<ph_project_token>', {
    api_host: 'https://us.i.posthog.com',
    defaults: '2026-01-30',
    person_profiles: 'always'
})
```

## Backend

PostHog's backend SDKs and API capture identified events by default. To capture anonymous events, set the `$process_person_profile` property to `false`:

PostHog AI

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id_of_the_user',
    event: 'your_event_name',
    properties: {
        $process_person_profile: false,
    },
})
```

### Python

```python
posthog.capture(
    "distinct_id_of_the_user",
    "your_event_name",
    {
        "$process_person_profile": false
    }
)
```

### PHP

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => 'your_event_name',
  'properties' => [
    '$process_person_profile' => false
  ]
]);
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id_of_the_user',
    event: 'your_event_name',
    properties: {
        $process_person_profile: false
    }
})
```

### Go

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id_of_the_user",
    Event:      "your_event_name",
    Properties: posthog.NewProperties().
      Set("$process_person_profile", false),
})
```

### Java

```java
posthog.capture("distinct_id_of_the_user", "your_event_name", new HashMap<String, Object>() {
  {
    put("$process_person_profile", false);
  }
});
```

### Rust

```rust
let mut event = Event::new("your_event_name", "distinct_id_of_the_user");
event.insert_prop("$process_person_profile", false).unwrap();
client.capture(event).unwrap();
```

### Elixir

```elixir
PostHog.capture("your_event_name", %{
  distinct_id: "distinct_id_of_the_user",
  "$process_person_profile": false
})
```

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "properties": {
        "$process_person_profile": false
    },
    "distinct_id": "distinct_id_of_the_user",
    "event": "your_event_name"
}' https://us.i.posthog.com/i/v0/e/
```

## Android

The Android SDK captures anonymous events by default. However, this may change depending on your `personProfiles` [config](/docs/libraries/android.md#all-configuration-options) when initializing PostHog:

1.  `personProfiles = PersonProfiles.IDENTIFIED_ONLY` *(recommended)* *(default)* - Anonymous events are captured by default. PostHog only captures identified events for users where [person profiles](/docs/data/persons.md) have already been created.

2.  `personProfiles = PersonProfiles.ALWAYS` - Capture identified events for all events.

3.  `personProfiles = PersonProfiles.NEVER` - Capture anonymous events for all events.

For example:

Kotlin

PostHog AI

```kotlin
val config = PostHogAndroidConfig(
   apiKey = POSTHOG_API_KEY,
   host = POSTHOG_HOST,
).apply {
   personProfiles = PersonProfiles.IDENTIFIED_ONLY
}
```

## iOS

The iOS SDK captures anonymous events by default. However, this may change depending on your `personProfiles` [config](/docs/libraries/ios/configuration.md#all-configuration-options) when initializing PostHog:

1.  `personProfiles: .identifiedOnly` *(recommended)* *(default)* - Anonymous events are captured by default. PostHog only captures identified events for users where [person profiles](/docs/data/persons.md) have already been created.

2.  `personProfiles: .always` - Capture identified events for all events.

3.  `personProfiles: .never` - Capture anonymous events for all events.

For example:

iOS

PostHog AI

```swift
let config = PostHogConfig(
    apiKey: POSTHOG_API_KEY,
    host: POSTHOG_HOST
)
config.personProfiles = .identifiedOnly
PostHogSDK.shared.setup(config)
```

## Flutter

The Flutter SDK captures anonymous events by default. However, this may change depending on your `personProfiles` [config](/docs/libraries/flutter.md#person-profiles-anonymous-vs-identified-persons) when initializing PostHog:

1.  `personProfiles: PostHogPersonProfiles.identifiedOnly` *(recommended)* *(default)* - Anonymous events are captured by default. PostHog only captures identified events for users where [person profiles](/docs/data/persons.md) have already been created.

2.  `personProfiles: PostHogPersonProfiles.always` - Capture identified events for all events.

3.  `personProfiles: PostHogPersonProfiles.never` - Capture anonymous events for all events.

For example:

Dart

PostHog AI

```dart
final config = PostHogConfig('<ph_project_token>');
config.host = POSTHOG_HOST;
config.personProfiles = PostHogPersonProfiles.identifiedOnly;
```

### How to capture identified events

## Web

If you've set the [`personProfiles` config](/docs/libraries/js/config.md) to `IDENTIFIED_ONLY` (the default option), anonymous events are captured by default. To capture identified events, call any of the following functions:

-   [`identify()`](/docs/product-analytics/identify.md)
-   [`alias()`](/docs/product-analytics/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user)
-   [`group()`](/docs/product-analytics/group-analytics.md)
-   [`setPersonProperties()`](/docs/product-analytics/person-properties.md)
-   [`setPersonPropertiesForFlags()`](/docs/libraries/js/features.md#overriding-server-properties)
-   [`setGroupPropertiesForFlags()`](/docs/libraries/js/features.md#overriding-server-properties)

When you call any of these functions, it creates a [person profile](/docs/data/persons.md) for the user. Once this profile is created, all subsequent events for this user will be captured as identified events.

Alternatively, you can set `personProfiles` to `ALWAYS` to capture identified events by default.

## Backend

PostHog's backend SDKs and API capture identified events by default.

PostHog AI

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id_of_the_user',
    event: 'your_event_name',
})
```

### Python

```python
posthog.capture(
    "distinct_id_of_the_user",
    "your_event_name",
)
```

### PHP

```php
PostHog::capture([
  'distinctId' => 'distinct_id_of_the_user',
  'event' => 'your_event_name',
]);
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id_of_the_user',
    event: 'your_event_name',
})
```

### Go

```go
client.Enqueue(posthog.Capture{
    DistinctId: "distinct_id_of_the_user",
    Event:      "your_event_name",
})
```

### Java

```java
posthog.capture("distinct_id_of_the_user", "your_event_name", new HashMap<String, Object>() {});
```

### Rust

```rust
let mut event = Event::new("your_event_name", "distinct_id_of_the_user");
client.capture(event).unwrap();
```

### Elixir

```elixir
PostHog.capture("your_event_name", %{
  distinct_id: "distinct_id_of_the_user"
})
```

### api

```api
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "distinct_id": "distinct_id_of_the_user",
    "event": "your_event_name"
}' https://us.i.posthog.com/i/v0/e/
```

## Android

If you've set the [`personProfiles` config](/docs/libraries/android.md#all-configuration-options) to `IDENTIFIED_ONLY` (the default option), anonymous events are captured by default. Then, to capture identified events, call any of the following functions:

-   [`identify()`](/docs/product-analytics/identify.md)
-   [`alias()`](/docs/product-analytics/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user)
-   [`group()`](/docs/product-analytics/group-analytics.md)

When you call any of these functions, it creates a [person profile](/docs/data/persons.md) for the user. Once this profile is created, all subsequent events for this user will be captured as identified events.

Alternatively, you can set `personProfiles` to `ALWAYS` to capture identified events by default.

## iOS

If you've set the [`personProfiles` config](/docs/libraries/ios/configuration.md#all-configuration-options) to `IDENTIFIED_ONLY` (the default option), anonymous events are captured by default. Then, to capture identified events, call any of the following functions:

-   [`identify()`](/docs/product-analytics/identify.md)
-   [`alias()`](/docs/product-analytics/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user)
-   [`group()`](/docs/product-analytics/group-analytics.md)

When you call any of these functions, it creates a [person profile](/docs/data/persons.md) for the user. Once this profile is created, all subsequent events for this user will be captured as identified events.

Alternatively, you can set `personProfiles` to `ALWAYS` to capture identified events by default.

## Flutter

If you've set the [`personProfiles` config](/docs/libraries/flutter.md#person-profiles-anonymous-vs-identified-persons) to `IDENTIFIED_ONLY` (the default option), anonymous events are captured by default. Then, to capture identified events, call any of the following functions:

-   [`identify()`](/docs/product-analytics/identify.md)
-   [`alias()`](/docs/product-analytics/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user)
-   [`group()`](/docs/product-analytics/group-analytics.md)

When you call any of these functions, it creates a [person profile](/docs/data/persons.md) for the user. Once this profile is created, all subsequent events for this user will be captured as identified events.

Alternatively, you can set `personProfiles` to `ALWAYS` to capture identified events by default.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better