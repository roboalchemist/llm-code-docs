# Source: https://firebase.google.com/docs/reference/swift/firebaseanalyticsswift/api/reference/Extensions/View.md.txt

# FirebaseAnalyticsSwift Framework Reference

# View

    public extension View

- `


  ### [analyticsScreen(name:class:extraParameters:)](https://firebase.google.com/docs/reference/swift/firebaseanalyticsswift/api/reference/Extensions/View#/s:7SwiftUI4ViewP017FirebaseAnalyticsA0E15analyticsScreen4name5class15extraParametersQrSS_SSSDySSypGtF)


  ` Logs `screen_view` events in Google Analytics for Firebase when this view appears on screen.

  #### Declaration

  Swift

      func analyticsScreen(name: String,
                           class: String = "View",
                           extraParameters: [String: Any] = [:]) -> some View

  #### Parameters

  |---|---|
  | ` name ` | Current screen name logged with the `screen_view` event. |
  | ` class ` | Current screen class or struct logged with the `screen_view` event. |
  | ` extraParameters ` | Any additional parameters to be logged. These extra parameters must follow the same rules as described in the `Analytics.logEvent(_:parameters:)` docs. |

  #### Return Value

  A view with a custom `ViewModifier` used to log `screen_view` events when this
  view appears on screen.