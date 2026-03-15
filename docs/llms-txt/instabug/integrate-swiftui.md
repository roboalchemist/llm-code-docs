# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/integrate-luciq-on-ios/integrate-swiftui.md

# Integrate SwiftUI

This guide provides instructions on how to integrate Luciq's Bug Reporting, Crash Reporting, and App Performance Monitoring features in your SwiftUI application. Following these steps, you can capture and report bugs and crashes from your SwiftUI application.

### Define SwiftUI Screens

In order to track and identify screens in your SwiftUI app, you‘ll need to use the `LuciqTraceView` function.

This will allow the SDK to [measure the loading time](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-loading) of your SwiftUI views and allow you to define screen names for your SwiftUI views. The screen name will correspond to the current view in your app, and Luciq will use the latest UI component to update screens.

{% hint style="warning" %}
Only the wrapper approach (Approach 1) Will allow the SDK to measure Screen Loading time of your SwiftUI Views
{% endhint %}

#### Approach 1: Wrapping Luciq on your views

Wrap Luciq around each view you have in your app by using the following:

```swift
var body: some View {
      LuciqTracedView(name: "View Name") {
        VStack {
          Text("Hello, World!")
      }
  }
}
```

#### Approach 2: Appending Luciq Modifier to your views

If you don’t use App Performance Monitoring, or don’t want to track your screen loading times, you can also define screen names by doing the following:

1. Call an API on the view that you want to make the root view.
2. Using the API below, it will create you a new view and wrap the user view with a traced view.

**Example:**

```swift
var body: some View {
    VStack {
        Text("Hello, World!")
    }
    .luciqTracedView(name: "View Name")
}
```

***

### Private Views

You can easily mark any SwiftUI view that might contain sensitive information, like payment details, as private. Any private view will automatically appear with a black overlay covering it in any screenshot.

To make a view private, you can use one of the following methods:

* Method 1:

```swift
LuciqPrivateView {
  Text("Hello, World") 
}
```

* Method 2:

```swift
Text("Hello, World")
     .Luciq_privateView()
```

***

### User Interactions - Manual Approach

To manually log user interactions on SwiftUI screens, you need to use the below API. The logged interactions will be reflected in the Repro Steps and User Steps components.

```swift
UserStep(event: .tap)  
            .setMessage("Hello, World")  
            .setViewType(.text)  
            .logUserStep()
```

Properties in the API:

* Event: User action on the screen (Ex. Tap, scroll..)
* Message: A brief message to help in identifying the UI element (Ex. Sign in)
* View Type: the type of the Ui element (Ex. Button, dropdown, text..)
