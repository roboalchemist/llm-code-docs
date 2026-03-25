# Source: https://documentation.onesignal.com/docs/en/live-activities-developer-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Activities developer setup

> Learn how to set up Live Activities on your iOS app with OneSignal to display real-time updates.

Live Activities let your iOS app show real-time updates directly on the lock screen and Dynamic Island. Ideal for delivery tracking, sports scores, or time-sensitive transactional updates, they keep users informed without opening the app.

<Note> Android has a similar feature called [Android Live Notifications](./android-live-notifications). </Note>

## Requirements

* Follow the [iOS SDK setup](./ios-sdk-setup) if using native iOS (Swift/Objective-C).
  * If using a wrapper SDK (React Native, Flutter, Unity, etc.) follow [Mobile SDK setup](./mobile-sdk-setup) and then [Cross-platform Live Activity SDK Setup](./cross-platform-live-activity-setup).
* OneSignal iOS SDK version 5.2.0+ for **push-to-start** support ([see release notes](https://github.com/OneSignal/OneSignal-iOS-SDK/releases/tag/5.2.0)).
* OneSignal iOS SDK version 5.2.15+ for **click tracking** and **Confirmed Delivery**
* iOS 16.1+ and iPadOS 17+
* Use a [.p8 APNs key](./ios-p8-token-based-connection-to-apns). Apple doesn't support p12 certificates with Live Activities.
* Xcode 14 or higher

***

## Setup

These steps walk you through setting up Live Activities quickly. For more details and design customizations, see [Apple's Live Activities Developer docs](https://developer.apple.com/design/human-interface-guidelines/live-activities).

### 1. Add a Widget Extension

In Xcode, go to **File > New > Target... > Widget Extension**.

<Frame caption="Add a new Widget Extension target for your app in Xcode.">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/live-activities/live-activity-widget-extension.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=60a52d6484203c4d6af21bc3a7da5e62" width="2166" height="1488" data-path="images/live-activities/live-activity-widget-extension.png" />
</Frame>

Select and press **Next**.

Configure the Widget Extension by providing a name (example: `OneSignalWidget`) and ensure **Include Live Activity** is selected. Then click **Finish**.

<Frame caption="Widget Extension options for a Live Activity.">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/live-activities/OneSignalWidget.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=47412314963f6fbd58fd2c7d3a529322" width="2166" height="1488" data-path="images/live-activities/OneSignalWidget.png" />
</Frame>

Click **Don't Activate** if prompted to activate the scheme.

<Frame caption="Widget Extension options for a Live Activity.">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/live-activities/la-scheme-activation.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=d3a2207ff2b5988c63c2abd631a72541" width="2166" height="1488" data-path="images/live-activities/la-scheme-activation.png" />
</Frame>

### 2. Update `Info.plist`

In your main target's `Info.plist`, add the key `Supports Live Activities` as **Boolean**, and set it to `YES`.

<Frame caption="Add Supports Live Activities key to Info and set its value to Boolean YES">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/live-activities/info-la-setting.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=e839231401651b71d0ae8d48614ec130" width="2166" height="1488" data-path="images/live-activities/info-la-setting.png" />
</Frame>

If you set it programmatically, it should look like this:

```xml info.plist theme={null}
NSSupportsLiveActivities

```

<Note>
  When updating Live Activities, you have the option to set a "priority" which Apple uses to determine how urgent the update is. Apple has internal thresholds in which they will throttle requests that use the high priority flag too frequently.

  If your use cases for Live Activities relies on more frequent high priority updates, you can add the key `NSSupportsLiveActivitiesFrequentUpdates` to your Info.plist as a Boolean type set to YES as directed in [Apple's Developer Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency). Users will be presented with a dialog when the Live Activity exceeds its push budget, and if they allow the Live Activity to continue, the budget will automatically be increased for a seamless user experience.
</Note>

### 3. Add SDK

<Tabs>
  <Tab title="Package Manager">
    In your Widget Extension target, add the `OneSignalFramework` under **General > Frameworks, Libraries and Embedded Content**:

    <Frame caption="Add the OneSignalFramework to your Widget Extension target">
      <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/live-activities/add-one-signal-framework.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=386781616958e5a80a5cfec5ee143dcb" width="2392" height="1488" data-path="images/live-activities/add-one-signal-framework.png" />
    </Frame>
  </Tab>

  <Tab title="Cocoapods">
    Find the name of your widget extension target in your project's Targets list. Example's name is `OneSignalWidgetExtension`.

    <Frame caption="Find the name of your widget extension target">
      <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/live-activities/cocoapods-la-extension-name.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=850a91387539587802306a66771435eb" width="2166" height="1488" data-path="images/live-activities/cocoapods-la-extension-name.png" />
    </Frame>

    Open your `Podfile` and add the following code. Replace `OneSignalWidgetExtension` with the name of your widget extension target.

    <CodeGroup>
      ```ruby Podfile theme={null}
      target 'OneSignalWidgetExtension' do
        use_frameworks!
        pod 'OneSignal/OneSignal', '>= 5.0.0', '< 6.0'
      end
      ```

      ```ruby Full Podfile example theme={null}
      # Uncomment the next line to define a global platform for your project
      # platform :ios, '9.0'

      target 'Demo Momenta' do
        # Comment the next line if you don't want to use dynamic frameworks
        use_frameworks!
        pod 'OneSignal/OneSignal', '>= 5.0.0', '< 6.0'
        pod 'OneSignal/OneSignalInAppMessages', '>= 5.0.0', '< 6.0'
      end

      target 'OneSignalNotificationServiceExtension' do
        use_frameworks!
        pod 'OneSignal/OneSignal', '>= 5.0.0', '< 6.0'
      end

      target 'OneSignalWidgetExtension' do
        use_frameworks!
        pod 'OneSignal/OneSignal', '>= 5.0.0', '< 6.0'
      end
      ```
    </CodeGroup>

    Close Xcode and run `pod repo update && pod install` to install the `OneSignalLiveActivities` pod.

    If you continue to see the error "No such module 'OneSignalLiveActivities'" after doing this, you can add the dependency manually by going to your **"Widget Extension Target" > General > Frameworks and Libraries > + icon**. Select the `OneSignalLiveActivities` framework:

    <Frame caption="Add dependencies manually">
      <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/427d54ef84e97edaf0a7c3b158b48b3bec7305fb1764db9dd4ef7c340d77bc6c-image.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=f7ba0aa4234ef69ebd7820ef5e50a18b" width="1273" height="881" data-path="images/docs/427d54ef84e97edaf0a7c3b158b48b3bec7305fb1764db9dd4ef7c340d77bc6c-image.png" />
    </Frame>
  </Tab>
</Tabs>

### 4. Define widget attributes and UI

Open the `your-nameLiveActivity.swift` file (example: `OneSignalWidgetLiveActivity.swift`) to define the properties of the struct and to make changes to the widget UI.

* `your-nameAttributes` describes the static content of your Live Activity.
* `ContentState` describes the dynamic content of your Live Activity.

If you are following the example, copy-paste the code below into your `OneSignalWidgetLiveActivity.swift` file.

```swift your-nameLiveActivity.swift theme={null}
import ActivityKit
import WidgetKit
import SwiftUI
// Import the OneSignalLiveActivities module
// If you get an error about the module not being found, return to step 3 and ensure you have added the OneSignalLiveActivities pod correctly.
import OneSignalLiveActivities

// Update to inherit from OneSignalLiveActivityAttributes
// This will be used in your API requests to start a Live Activity
struct OneSignalWidgetAttributes: OneSignalLiveActivityAttributes  {
    // Update to inherit from OneSignalLiveActivityContentState
    public struct ContentState: OneSignalLiveActivityContentState {
        // Dynamic stateful properties about your activity go here!
        var emoji: String
        // Add a reference to OneSignalLiveActivityContentStateData?
        var onesignal: OneSignalLiveActivityContentStateData?
    }
    // Fixed non-changing properties about your activity go here!
    var name: String
    // Add a reference to OneSignalLiveActivityAttributeData
    var onesignal: OneSignalLiveActivityAttributeData
}

struct OneSignalWidgetLiveActivity: Widget {
    var body: some WidgetConfiguration {
      // Update to use `for: the-name-of-your-attributes-struct`
      // This will be used in your API requests to start a Live Activity
        ActivityConfiguration(for: OneSignalWidgetAttributes.self) { context in
            // Lock screen/banner UI goes here
            // Update to show the attributes sent via the payload
            VStack {
                Text("Hello \(context.attributes.name) \(context.state.emoji)")
            }
            .activityBackgroundTint(Color.cyan)
            .activitySystemActionForegroundColor(Color.black)

        } dynamicIsland: { context in
            DynamicIsland {
                // Expanded UI goes here.  Compose the expanded UI through
                // various regions, like leading/trailing/center/bottom
                DynamicIslandExpandedRegion(.leading) {
                    Text("Leading")
                }
                DynamicIslandExpandedRegion(.trailing) {
                    Text("Trailing")
                }
                DynamicIslandExpandedRegion(.bottom) {
                    Text("Bottom \(context.state.emoji)")
                    // more content
                }
            } compactLeading: {
                Text("L")
            } compactTrailing: {
                Text("T \(context.state.emoji)")
            } minimal: {
                Text(context.state.emoji)
            }
            .widgetURL(URL(string: "http://www.apple.com"))
            .keylineTint(Color.red)
        }
    }
}
```

### 5. Allow main target membership

Add your main app target to the **Target Membership** list in the `your-nameLiveActivity.swift` file.

In Xcode, open the Inspector panel on the right side of the screen. Within **Target Membership**, click the **+** button and select your main app target containing the `ContentView` and your OneSignal initialization code.

<Frame caption="Allow main target membership">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/live-activities/target-membership.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=3315253623dfec6c13a56ff30a156772" width="2392" height="1488" data-path="images/live-activities/target-membership.png" />
</Frame>

### 6. Add the setup method to your AppDelegate

Call `OneSignal.LiveActivities.setup` in your `AppDelegate`, after OneSignal SDK initialization.

Replace `OneSignalWidgetAttributes` with the name of your Live Activity attributes struct.

```swift AppDelegate theme={null}
// Import the OneSignalLiveActivities module
import OneSignalLiveActivities

// This should be added after initializing the OneSignal SDK
if #available(iOS 16.1, *) {
 OneSignal.LiveActivities.setup(OneSignalWidgetAttributes.self)
  // If you have multiple Live Activities, you can add them here with the setup method
  // OneSignal.LiveActivities.setup(LiveActivityWidgetAttributes-2.self)
}
```

This manages and reports updates using ActivityKit async sequences.

<Warning>
  If you also consume any of the following sequences directly in your app, it may interfere with OneSignal Live Activity behavior:

* activityStateUpdates
* pushTokenUpdates
* pushToStartTokenUpdates
* activityUpdates
</Warning>

***

## Starting a Live Activity

There are 2 options to start a Live Activity on a device:

<Tabs>
  <Tab title="Push-to-start">
    Send a [Push To Start API request](/reference/start-live-activity). Be sure all names and IDs match your widget's configuration exactly (parameters are case-sensitive). If anything is missing or incorrectly added, you may encounter issues when trying to launch the widget.

    Here is an example request that will work for the example above.

    Replace:

    * `YOUR_APP_ID` with your OneSignal App ID.
    * `YOUR_APP_API_KEY` with your OneSignal API key.
    * `OneSignalWidgetAttributes` with the name of your Widget Attributes struct.

      ```curl curl theme={null}
      curl --location 'https://api.onesignal.com/apps/YOUR_APP_ID/activities/activity/OneSignalWidgetAttributes' \
      --header 'Authorization: key YOUR_APP_API_KEY' \
      --header 'Content-Type: application/json' \
      --data '{
          "event": "start",
          "activity_id": "push-to-start",
          "included_segments": [
              "Subscribed Users"
          ],
          "event_attributes": {
              "name": "World"
          },
          "event_updates": {
              "emoji":"🤩"
          },
          "name": "Live Activities Test",
          "contents": {
              "en": "A push started this Live Activity"
          },
          "headings": {
            "en": "Live Activity Started"
          }
        }'
      ```

    If you are following the example code provided, you should see the Live Activity on your device's lock screen.

    <Frame caption="Live Activity on the lock screen">
      <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/live-activities/live-activity-lock-screen.jpg?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=8abc098ce8772b1c457e5f1effc8c14e" width="900" height="385" data-path="images/live-activities/live-activity-lock-screen.jpg" />
    </Frame>

    <Check>
      You successfully started a Live Activity with push-to-start!

      Users will need to select "Allow" to continue getting updates.
    </Check>
  </Tab>

  <Tab title="Trigger-in-app">
    You can have a user trigger a Live Activity while interacting with your app.

    For example, when a user has an active event going on (they placed an order, a game is in progress, an event is about to start, etc.) and opens your app, you can display a Live Activity automatically.

    In this example we will use a button to start the Live Activity manually.

    ```swift  theme={null}
    import SwiftUI
    import ActivityKit
    import OneSignalFramework
    import OneSignalLiveActivities

    struct ContentView: View {
      @StateObject private var viewModel = LiveActivityViewModel()

      var body: some View {
        VStack {
          Button("Start Live Activity") {
            viewModel.startLiveActivity()
          }
        }
      }
    }

    class LiveActivityViewModel: ObservableObject {

      func startLiveActivity() {
        let osAttributes = OneSignalLiveActivityAttributeData.create(activityId: "click-to-start")
        let attributes = OneSignalWidgetAttributes(name: "OneSignal", onesignal: osAttributes)
        let contentState = OneSignalWidgetAttributes.ContentState(emoji:"🤩", onesignal: nil)
        do {
            let activity = try Activity<OneSignalWidgetAttributes>.request(
                attributes: attributes,
                contentState: contentState,
                pushType: .token)
        } catch {
            print(error.localizedDescription)
        }
      }
    }
    ```

    Upon clicking the button it will launch the Live Activity.
  </Tab>
</Tabs>

***

## Tracking Live Activity Clicks

Track when users tap on your Live Activities and Dynamic Islands by implementing OneSignal's click tracking. This enables you to measure engagement and optionally deep link users to specific content in your app.

### Step 1: Add Click Tracking to Your Widget

Add the `.onesignalWidgetURL()` modifier to any UI component in your Live Activity widget that you want to track clicks on:

```swift  theme={null}
import OneSignalLiveActivities

struct ExampleAppFirstWidget: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: ExampleAppFirstWidgetAttributes.self) { context in
            VStack {
                Spacer()
                Text("Sample Text " + context.attributes.title).font(.headline)
                // Other UI code
            }
            .onesignalWidgetURL(URL(string: "myapp://settings"), context: context)
            // Pass nil if you don't need deep linking: .onesignalWidgetURL(nil, context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    Text("Leading")
                }
                // Other Dynamic Island regions
            } compactLeading: {
                Text("L")
            } compactTrailing: {
                Text("T")
            } minimal: {
                Text("Min")
            }
            .onesignalWidgetURL(URL(string: "myapp://settings"), context: context)
            // Optional: Track Dynamic Island clicks separately
        }
    }
}
```

**Important Considerations:**

* You can pass a URL for deep linking or `nil` if you only want click tracking without navigation
* The view hierarchy **cannot include** Apple's `.widgetURL()` modifier if you're using `.onesignalWidgetURL()`
* Apply the modifier to both the main Live Activity view and Dynamic Island if you want to track clicks on both

### Step 2: Handle URLs in Your App

Add URL handling in your app to track clicks and route users appropriately:

```swift  theme={null}
import OneSignalLiveActivities

// AppDelegate example:
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let originalURL = OneSignal.LiveActivities.trackClickAndReturnOriginal(url)
    
    // Handle the original URL and navigate user
    if let url = originalURL {
        // Your custom URL routing logic
        return handleDeepLink(url)
    }
    return false
}

// SceneDelegate example:
func scene(_ scene: UIScene, openURLContexts URLContexts: Set) {
    guard let url = URLContexts.first?.url else { return }
    
    let originalURL = OneSignal.LiveActivities.trackClickAndReturnOriginal(url)
    
    if let url = originalURL {
        // Your custom URL routing logic
        handleDeepLink(url)
    }
}

// SwiftUI example:
.onOpenURL { url in
    let originalURL = OneSignal.LiveActivities.trackClickAndReturnOriginal(url)
    
    if let url = originalURL {
        // Your custom URL routing logic
        handleDeepLink(url)
    }
}
```

The `trackClickAndReturnOriginal()` method automatically tracks the click with OneSignal and returns the original URL you specified in the widget for your app to handle.

***

## Updating a Live Activity

Use the [Update Live Activity API](/reference/update-live-activity-api) to update active widgets.

Match the `activity_id` used when starting the activity.

This example request will update the push-to-start widget because it has the `activity_id` titled `push-to-start` that we defined.
To update the click-to-start widget, update the request path to use `click-to-start` instead of `push-to-start`.

```curl curl theme={null}
curl --location 'https://api.onesignal.com/apps/YOUR_APP_ID/live_activities/push-to-start/notifications' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: key YOUR_API_KEY' \
--data '{
    "event": "update",
    "event_updates": {
        "emoji": "😎"
    },
    "contents": {
        "en": "A push updated this Live Activity"
    },
    "name": "Live Activity Updated"
}'
```

<Frame caption="Live Activity Updated">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/live-activities/live-activity-updated.jpg?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=729ab3b33c297c15e52617ebd065b293" width="895" height="152" data-path="images/live-activities/live-activity-updated.jpg" />
</Frame>

<Check>
  You successfully updated a Live Activity!

  Checkout the [Update Live Activity API](/reference/update-live-activity-api) for more information on updating a Live Activity.
</Check>

***

## Ending a Live Activity

Using the same [Update Live Activity API](/reference/update-live-activity-api), we can end a Live Activity by setting `"event": "end"`.

```curl curl theme={null}
curl --location 'https://api.onesignal.com/apps/YOUR_APP_ID/live_activities/my_activity_id/notifications' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: key YOUR_API_KEY' \
--data '{
    "event": "end",
    "event_updates": {
        "emoji": "👋"
    },
    "contents": {
        "en": "A push ended this Live Activity"
    },
    "name": "Live Activity Ended"
}'
```

Other ways a Live Activity can end:

* Use our SDK [`exit()` method](./mobile-sdk-reference#exit).
* User manually swipes the Live Activity away.
* User revokes permission for Live Activities in their iOS Settings.

<Frame caption="Live Activity Ended">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/live-activities/live-activity-ended.jpg?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=734a62b67cb2fe989203087a22945448" width="1218" height="200" data-path="images/live-activities/live-activity-ended.jpg" />
</Frame>

<Check>
  You successfully ended the Live Activity and completed the example!
</Check>

***

## Best practices & recommendations

### Design considerations

* Follow Apple's [Live Activities Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/live-activities).
  * Prioritize important information to make it easy to understand at a quick glance.
  * Don't add elements to your app that draw attention to the Dynamic Island.
  * Use margins and maintain space between elements.
  * Use a bold color for the background. Design for both Light and Dark mode.

### Functionality

* Apple requires each [Live Activity presentation](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Review-Live-Activity-presentations) to be supported.
  * [Compact](https://developer.apple.com/design/human-interface-guidelines/live-activities#Compact-presentation)
  * [Minimal](https://developer.apple.com/design/human-interface-guidelines/live-activities#Minimal-presentation)
  * [Expanded](https://developer.apple.com/design/human-interface-guidelines/live-activities#Expanded-presentation)
  * [Lock Screen](https://developer.apple.com/design/human-interface-guidelines/live-activities#The-Lock-Screen)
* Test your [deep links](https://developer.apple.com/design/human-interface-guidelines/live-activities#Offering-interactivity).
* Review Apple's guide on [Displaying Live Data with Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities).
* Avoid displaying sensitive information in a Live Activity.

### Setting a fallback message

* In certain cases where the user is unable to receive an update to their live activity, after one has been started, opening the app should refresh them to continue
  * To account for this, you would set the [stale date](/reference/start-live-activity#body-stale-date) to a date and time in the future, after you know you would have sent your first update to the user, and those who have not received the update would get shown the fallback message.
  * You can listen for this "stale" state in your widget UI to show a fallback message:
  <img src="https://mintcdn.com/onesignal/CKWnlQN-faoVTpm2/images/live-activities/live-activity-refresh.png?fit=max&auto=format&n=CKWnlQN-faoVTpm2&q=85&s=180ef1cc07313ef04361fbd45e2fec24" width="509" height="181" data-path="images/live-activities/live-activity-refresh.png" />

<CodeGroup>
  ```swift swift theme={null}
  struct ptsLiveActivity: Widget {
      var body: some WidgetConfiguration {
          ActivityConfiguration(for: ptsAttributes.self) { context in
              //This will flip to true after the stale date
              let isStale = context.isStale
              if !isStale{
                  VStack {
                      Text("\(context.attributes.name) \(context.state.emoji)")
                          .activityBackgroundTint(Color.cyan)
                          .activitySystemActionForegroundColor(Color.black)
                  }
              }  else {
              //If the message is stale, we request the user clicks the widget to open the app
                  VStack {
                      Text("Something went wrong, please click to refresh")
                  }
              }
          //... Rest of the widget UI
          }
      }
  }
  ```
</CodeGroup>

***

## FAQ

### What is the budget for high-priority updates?

Apple does not provide a fixed limit for high-priority (`priority: 10`) updates, but they do enforce a dynamic system-level budget. Sending too many high-priority updates in a short period may result in throttling, where updates are delayed or dropped.

To reduce the risk of throttling:

* Use a mix of priority levels: Apple recommends using both `priority: 5` (standard) and `priority: 10` (high) for balance.
* Reserve `priority: 10` for time-sensitive or critical updates only (e.g., order status changes, game scores).

If your use case requires frequent updates:

* Add the key `NSSupportsLiveActivitiesFrequentUpdates` to your app's `Info.plist` file, set as a Boolean `YES`.
* When this budget is exceeded, iOS may prompt the user to allow additional updates. If the user agrees, Apple will automatically expand the allowed update limit to maintain a seamless experience.

For more details, refer to [Apple's Developer Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency).

### Can I read Live Activity updates from the main app?

Yes. You can observe updates for debugging or UI sync:

```swift  theme={null}
Task {
    for await content in activity.contentUpdates {
        print("LA activity id: \(activity.id), content update: \(content.state)")
    }
}
// Example output:
// LA activity id: EFE6D54D-F7E1-45EF-9514-4C2598F8DED2, content update: ContentState(message: "My message from payload")
```

Track lifecycle changes:

```swift  theme={null}
Task {
    for await state in activity.activityStateUpdates {
        print("LA state update: \(state)")
        //If you wanted to do something based on the state, you would use this:
       if state != ActivityState.active {
            //Do something here
        }
    }
}

// Example output 1 - LA ended, but still visible
// LA state update: active

/* State can be equal to 4 possible values on the ActivityState enum
active, dismissed, ended, and stale
*/
```

### The API returned a 400 with an error message stating I'm over the subscriber limit. What do I do?

If your push subscriber count is greater than the Push Subscribers for your plan, please upgrade your account to the next plan, or reach out to `support@onesignal.com`. For the latest plan details, [please see here](https://onesignal.com/pricing).

### How do I avoid sending both push and Live Activities?

Your application may already send a series of Push Notifications, where your designed Live Activity replaces the need for these Push Notifications. For example, if you send score updates via Push, you could replace this through a Live Activity.

In order to ensure your users are not getting too many messages, we recommend as your user opts in for a Live Activity, to add a data tag. By adding this data tag, you can exclude users with this data tag from push messages that may contain the same or similar content. Read more on [Data Tags](./add-user-data-tags) and [Segments](./segmentation).

***

## Troubleshooting

### No recipients

In order for your users to be found when trying to start or update a Live Activity, you must ensure that the activity type, widget, and cURL request all have matching values.

1. Check the path parameters in your request to ensure that you are sending a correctly formatted request to the server. The App ID must match your App ID used in the `OneSignal.Initialize` method and the activity type must match that of the type you've defined in your Live Activity file.

2. In the body of the [Push To Start API request](/reference/start-live-activity), you should have the following parameters:

* `event`: `"start"`
* `event_updates`: The dynamic data you have defined in your struct under activity type and that is used in your widget. Ensure the letter casing and variables all match between the request, the type, and the widget.
* `event_attributes`: Static data follows the same logic as Event Updates and must include all variables in use, and must match across all parts of the live activity and the request
* `activity_id`: This will assign an ID to the widget and is what will be used to update the activity after it has been launched on the user's device.
* `name`: The Live Activity Name.
* `contents`: The message content required for sending push.
* `headings`: The message heading required for sending push.
* A targeting parameter like `included_segments`. [Available options](/reference/create-message).

### Activity sent, but not received

1. Ensure that the request is formatted correctly. If any fields that are used in the Widget are omitted, the activity may not launch or update as expected.

2. In your API request, determine the `priority` level you are setting. If you are setting this to `10` (highest priority), try lowering it to `5` and test again. Apple will throttle requests being sent out too frequently per their own internal rate limits.

If your use case relies on more frequent updates, add the key `NSSupportsLiveActivitiesFrequentUpdates` to your Info.plist as a Boolean type set to YES as directed in [Apple's Developer Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency). User will be presented with a dialog when the Live Activity exceeds its push budget, and if they allow the Live Activity to continue, the budget will automatically be increased for a seamless user experience.

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
