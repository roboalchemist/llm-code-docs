# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplay.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingDisplay

    protocol InAppMessagingDisplay

The protocol that a FIAM display component must implement.
This protocol is unavailable on macOS, macOS Catalyst, and watchOS.
- `
  ``
  ``
  `

  ### [displayMessage(_:displayDelegate:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplay#/c:objc(pl)FIRInAppMessagingDisplay(im)displayMessage:displayDelegate:)

  `
  `  
  Method for rendering a specified message on client side. Invoked on a background thread.  

  #### Declaration

  Swift  

      func displayMessage(_ messageForDisplay: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingDisplayMessage.html, displayDelegate: any https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html)

  #### Parameters

  |---------------------------|----------------------------------------------------------------------------------------------------------|
  | ` `*messageForDisplay*` ` | the message object. It would be of one of the three message types at runtime.                            |
  | ` `*displayDelegate*` `   | the callback object used to trigger notifications about certain conditions related to message rendering. |