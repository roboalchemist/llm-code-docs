# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplayDelegate.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Protocols/FIRInAppMessagingDisplayDelegate.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingDisplayDelegate

    @protocol FIRInAppMessagingDisplayDelegate <NSObject>

A protocol defining those callbacks to be triggered by the message display component
under appropriate conditions.
This protocol is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [-messageDismissed:dismissType:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Protocols/FIRInAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)messageDismissed:dismissType:)

  `
  `  
  Called when the message is dismissed. Should be called from main thread.  

  #### Declaration

  Objective-C  

      - (void)messageDismissed:(nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html *)inAppMessage
                   dismissType:(https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Enums/FIRInAppMessagingDismissType.html)dismissType;

  #### Parameters

  |----------------------|--------------------------------------|
  | ` `*inAppMessage*` ` | the message that was dismissed.      |
  | ` `*dismissType*` `  | specifies how the message is closed. |

- `
  ``
  ``
  `

  ### [-messageClicked:withAction:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Protocols/FIRInAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)messageClicked:withAction:)

  `
  `  
  Called when the message's action button is followed by the user.  

  #### Declaration

  Objective-C  

      - (void)messageClicked:(nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html *)inAppMessage
                  withAction:(nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingAction.html *)action;

  #### Parameters

  |----------------------|------------------------------------------------------------|
  | ` `*inAppMessage*` ` | the message that was clicked.                              |
  | ` `*action*` `       | contains the text and URL for the action that was clicked. |

- `
  ``
  ``
  `

  ### [-impressionDetectedForMessage:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Protocols/FIRInAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)impressionDetectedForMessage:)

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

  Objective-C  

      - (void)impressionDetectedForMessage:
          (nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html *)inAppMessage;

  #### Parameters

  |----------------------|---------------------------------------------------|
  | ` `*inAppMessage*` ` | the message for which an impression was detected. |

- `
  ``
  ``
  `

  ### [-displayErrorForMessage:error:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Protocols/FIRInAppMessagingDisplayDelegate#/c:objc(pl)FIRInAppMessagingDisplayDelegate(im)displayErrorForMessage:error:)

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

  Objective-C  

      - (void)displayErrorForMessage:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html *)inAppMessage
                               error:(nonnull NSError *)error;

  #### Parameters

  |----------------------|-----------------------------------------------|
  | ` `*inAppMessage*` ` | the message that encountered a display error. |