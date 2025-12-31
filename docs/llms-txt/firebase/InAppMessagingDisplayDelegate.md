# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplayDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingDisplayDelegate

    protocol InAppMessagingDisplayDelegate : NSObjectProtocol

A protocol defining those callbacks to be triggered by the message display component
under appropriate conditions.
This protocol is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [messageDismissed(_:dismissType:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)messageDismissed:dismissType:)

  `
  `  
  Called when the message is dismissed. Should be called from main thread.  

  #### Declaration

  Swift  

      optional func messageDismissed(_ inAppMessage: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html, dismissType: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingDismissType.html)

  #### Parameters

  |----------------------|--------------------------------------|
  | ` `*inAppMessage*` ` | the message that was dismissed.      |
  | ` `*dismissType*` `  | specifies how the message is closed. |

- `
  ``
  ``
  `

  ### [messageClicked(_:with:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)messageClicked:withAction:)

  `
  `  
  Called when the message's action button is followed by the user.  

  #### Declaration

  Swift  

      optional func messageClicked(_ inAppMessage: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html, with action: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingAction.html)

  #### Parameters

  |----------------------|------------------------------------------------------------|
  | ` `*inAppMessage*` ` | the message that was clicked.                              |
  | ` `*action*` `       | contains the text and URL for the action that was clicked. |

- `
  ``
  ``
  `

  ### [impressionDetected(for:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)impressionDetectedForMessage:)

  `
  `  
  Use this to mark a message as having gone through enough impression so that
  headless component can make appropriate impression tracking for it.

  Calling this is optional.

  When messageDismissedWithType: or messageClicked is
  triggered, the message would be marked as having a valid impression implicitly.
  Use impressionDetected if the UI implementation would like to mark valid
  impression in additional cases. One example is that the message is displayed for
  N seconds and then the app is killed by the user. Neither
  onMessageDismissedWithType or onMessageClicked would be triggered
  in this case. But if the app regards this as a valid impression and does not
  want the user to see the same message again, call impressionDetected to mark
  a valid impression.  

  #### Declaration

  Swift  

      optional func impressionDetected(for inAppMessage: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html)

  #### Parameters

  |----------------------|---------------------------------------------------|
  | ` `*inAppMessage*` ` | the message for which an impression was detected. |

- `
  ``
  ``
  `

  ### [displayError(for:error:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)displayErrorForMessage:error:)

  `
  `  
  Called when the display component could not render the message due to various reason.
  It's essential for display component to call this when error does arise. On seeing
  this, the headless component of fiam would assume that a prior attempt to render a
  message has finished and therefore it's ready to render a new one when conditions are
  met. Missing this callback in failed rendering attempt would make headless
  component think a fiam message is still being rendered and therefore suppress any
  future message rendering.  

  #### Declaration

  Swift  

      optional func displayError(for inAppMessage: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html, error: any Error)

  #### Parameters

  |----------------------|-----------------------------------------------|
  | ` `*inAppMessage*` ` | the message that encountered a display error. |