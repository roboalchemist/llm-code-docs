# Source: https://docs.logrocket.com/reference/ios-redact-view.md

# Sanitize View Data

Redact individual views or disable capture altogether

Redacting a view prevents that portion of the application view from being recorded

## Redact individual views in SwiftUI

To redact individual views in SwiftUI, see our [SwiftUI Documentation.](https://docs.logrocket.com/reference/swiftui-about)

## Redact individual views in UIKit

To redact a view, assign that view an accessibility identifier, either through the storyboard or manually by setting View\.accessibilityIdentifier. Next, add that accessibility identifier to the **redactionTags** SDK configuration option. The view will be hidden during the capture process so that it does not show up in the final recording.

### Redacts views with accessibility identifiers that match these tags

```swift redactionTags
redactionTags: Set<String> = []

SDK.initialize(configuration: Configuration(
  ...
  redactionTags: redactionTags
))
```

## Allow individual views in UIKit

Individual subviews of a redacted view can be allowed for view capture, also by assigning their accessibility identifiers. Add these values to the **allowTags** SDK configuration option.

### Capture views with accessibility identifiers that match these tags

```swift allowTags
allowTags: Set<String> = []

SDK.initialize(configuration: Configuration(
  ...
  allowTags: allowTags
))
```

## Prevent capturing touch events on redacted views

In order to prevent touches on redacted views from appearing in session replay, the following configuration must be provided. An example of when this would be useful is if your app redacts a PIN pad.

```swift captureRedactedViewTouches
SDK.initialize(configuration: Configuration(
  ...
  captureRedactedViewTouches: false
))
```

## Disable touch tracking

If you wish to prevent capturing touch events entirely, set this option to false.

```swift disable touch tracking
SDK.initialize(configuration: Configuration(  
  ...  
  registerTouchHandlers: false  
))
```

## Disable automatic view capture entirely

By default, the SDK will capture views automatically.  To block recording of all views, set this option to false.

### Enable (default) or disable automatic view capture

```swift Enable or Disable View Capture
SDK.initialize(configuration: Configuration(
  ...
  viewScanningEnabled: true
))
```

## Pause View Capture

To completely disable the view capture system call `SDK.pauseViewCapture()`. If a capture is already in progress it will not be stopped, but no view captures will be created until the system is resumed with `SDK.unpauseViewCapture()`.

## Directly Redact / Allow Individual Views

In situations where using accessibility identifiers is not practical (such as if they are procedurally generated) you can individually allow and redact views using the `SDK.redactView(UIView)` and `SDK.allowView(UIView)` functions.

```swift Directly Redact / Allow Individual Views
@IBOutlet weak var redactedButton: UIButton!
@IBOutlet weak var allowButton: UIButton!

override func viewDidLoad() {
    ...
    SDK.redactView(redactedButton)
    SDK.allowView(allowButton)
  }
```