# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessaging

    class InAppMessaging : NSObject

The root object for in-app messaging iOS SDK.

Note: Firebase In-App Messaging depends on using a Firebase Installation ID and token pair to be
able to retrieve messages defined for the current app instance. By default, the Firebase In-App
Messaging SDK will obtain the ID and token pair on app/SDK startup. In its default configuration
the in-app messaging SDK will send some device and client data (linked to the installation ID)
to the Firebase backend periodically.

The app can tune the default data collection behavior via certain controls. They are listed in
descending order below. If a higher-priority setting exists, lower level settings are ignored.

1. Dynamically turning on or off data collection behavior by setting the `automaticDataCollectionEnabled` property on the `InAppMessaging` instance to true or false.
2. Setting `FirebaseInAppMessagingAutomaticDataCollectionEnabled` to false in the app's plist file.
3. Disabling data collection via the global Firebase data collection setting.

This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [inAppMessaging()](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(cm)inAppMessaging)

  `
  `  
  @fn inAppMessaging
  @brief Gets the singleton InAppMessaging object constructed from the default Firebase app
  settings.  

  #### Declaration

  Swift  

      class func inAppMessaging() -> InAppMessaging

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(im)init)

  `
  `  
  Unavailable

  Use +inAppMessaging instead.  
  Unavailable. Use +inAppMessaging instead.
- `
  ``
  ``
  `

  ### [messageDisplaySuppressed](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(py)messageDisplaySuppressed)

  `
  `  
  A boolean flag that can be used to suppress messaging display at runtime,
  initialized to false at app startup. Once set to true, the in-app messaging SDK will stop
  rendering any new messages until this flag is set back to false.  

  #### Declaration

  Swift  

      var messageDisplaySuppressed: Bool { get set }

- `
  ``
  ``
  `

  ### [automaticDataCollectionEnabled](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(py)automaticDataCollectionEnabled)

  `
  `  
  A boolean flag that can be set at runtime to allow or disallow
  collecting user data on app startup. This property is persisted across app
  restarts and has higher priority over the `FirebaseInAppMessagingAutomaticDataCollectionEnabled`
  flag (if present) in your app's `Info.plist` file.  

  #### Declaration

  Swift  

      var automaticDataCollectionEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [messageDisplayComponent](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(py)messageDisplayComponent)

  `
  `  
  This is the display component that will be used by InAppMessaging to render messages.
  If it's `nil`, InAppMessaging will only perform other non-rendering flows (fetching messages for
  example). Any custom implementations of [InAppMessagingDisplay](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplay.html) require setting this property in
  order to take effect.  

  #### Declaration

  Swift  

      var messageDisplayComponent: any https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplay.html { get set }

- `
  ``
  ``
  `

  ### [triggerEvent(_:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(im)triggerEvent:)

  `
  `  
  Directly requests an in-app message with the given trigger to be shown.  

  #### Declaration

  Swift  

      func triggerEvent(_ eventName: String)

- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessaging#/c:objc(cs)FIRInAppMessaging(py)delegate)

  `
  `  
  This delegate should be set on the app side to receive message lifecycle events.  

  #### Declaration

  Swift  

      weak var delegate: (any https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html)? { get set }