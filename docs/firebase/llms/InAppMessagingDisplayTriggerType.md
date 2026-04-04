# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayTriggerType.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingDisplayTriggerType

    enum InAppMessagingDisplayTriggerType : Int, @unchecked Sendable

Represents how an in-app message should be triggered to appear. This enum is unavailable on
macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [onAppForeground](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayTriggerType#/c:@E@FIRInAppMessagingDisplayTriggerType@FIRInAppMessagingDisplayTriggerTypeOnAppForeground)

  `
  `  
  Triggered on app foreground.  

  #### Declaration

  Swift  

      case onAppForeground = 0

- `
  ``
  ``
  `

  ### [onAnalyticsEvent](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDisplayTriggerType#/c:@E@FIRInAppMessagingDisplayTriggerType@FIRInAppMessagingDisplayTriggerTypeOnAnalyticsEvent)

  `
  `  
  Triggered from an analytics event being fired.  

  #### Declaration

  Swift  

      case onAnalyticsEvent = 1