# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingDisplay

    @protocol FIRInAppMessagingDisplay

The protocol that a FIAM display component must implement.
- `


  ### [-displayMessage:displayDelegate:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplay#/c:objc(pl)FIRInAppMessagingDisplay(im)displayMessage:displayDelegate:)


  ` Method for rendering a specified message on client side. It's called from main thread.

  #### Declaration

  Objective-C

      - (void)displayMessage:
                  (nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingDisplayMessage.html *)messageForDisplay
             displayDelegate:
                 (nonnull id<https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Protocols/FIRInAppMessagingDisplayDelegate.html>)displayDelegate;

  #### Parameters

  |---|---|
  | ` messageForDisplay ` | the message object. It would be of one of the three message types at runtime. |
  | ` displayDelegate ` | the callback object used to trigger notifications about certain conditions related to message rendering. |