# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-application-performance-monitoring/setup-app-launch.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-app-launch.md

# Setup App Launch

### Cold App Launch

Luciq automatically measures your **cold app launch** latency, which is the time between when your user launches the app from scratch and when it is responsive and accepting touch events.

It starts with the process start time and stops by the end of the first run loop. This interval accounts for any launch blocking logic in your code as well as the time before your app classes are loaded. It includes loading dynamic frameworks and resolving any dynamic references made in the binary.

#### Disabling/Enabling Cold App Launch Tracking

If APM is enabled, our SDK starts collecting data about your cold app launch time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Swift" %}

```swift
// Enable
APM.coldAppLaunchEnabled = true

// Disable
APM.coldAppLaunchEnabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```python
// Enable
LCQAPM.coldAppLaunchEnabled = YES;

// Disable
LCQAPM.coldAppLaunchEnabled = NO;
```

{% endtab %}
{% endtabs %}

***

### Hot App Launch

The Luciq SDK automatically measures the **hot app launch** latency, which is the time between the user launching the app from the background until it's responsive and accepting touch events.

Hot Launch is transitioning the app from the background to the foreground-active state. We capture the Hot Launch event by observing a `UIApplicationWillEnterForegroundNotification` notification which is then followed by `UIApplicationDidBecomeActiveNotification`.

#### Disabling/Enabling Hot App Launch Tracking

If APM is enabled, our SDK starts collecting data about your hot app launch time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Swift" %}

```swift
// Enable
APM.hotAppLaunchEnabled = true

// Disable
APM.hotAppLaunchEnabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
// Enable
LCQAPM.hotAppLaunchEnabled = YES;

// Disable
LCQAPM.hotAppLaunchEnabled = NO;
```

{% endtab %}
{% endtabs %}

***

### End App Launch

In the event that you'd like to define a specific point in time where the app launch can be considered complete, such as when the app is actually interactable, you can use the end app launch API to set that point. You'll then be able to see this data alongside the automatic cold and hot app launches that were captured.

To use the End App Launch API, you'll just need to call the following method:

{% tabs %}
{% tab title="Swift" %}

```swift
APM.endAppLaunch()
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
[IBGAPM endAppLaunch]
```

{% endtab %}
{% endtabs %}
