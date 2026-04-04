# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRIAMDefaultDisplayImpl.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRIAMDefaultDisplayImpl


    @interface FIRIAMDefaultDisplayImpl : NSObject <https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplay.html>

Public class for displaying fiam messages. Most apps should not use it since its instance
would be instantiated upon SDK start-up automatically. It's exposed in public interface
to help UI Testing app access the UI layer directly.
- `
  ``
  ``
  `

  ### [-displayMessage:displayDelegate:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRIAMDefaultDisplayImpl#/c:objc(cs)FIRIAMDefaultDisplayImpl(im)displayMessage:displayDelegate:)

  `
  `  
  Conforms to display delegate for rendering of in-app messages.  

  #### Declaration

  Objective-C  

      - (void)displayMessage:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.html *)messageForDisplay
             displayDelegate:
                 (nonnull id<https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplayDelegate.html>)displayDelegate;