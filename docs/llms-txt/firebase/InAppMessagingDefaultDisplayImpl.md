# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDefaultDisplayImpl.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# InAppMessagingDefaultDisplayImpl

    class InAppMessagingDefaultDisplayImpl : NSObject, https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplay.html

Public class for displaying fiam messages. Most apps should not use it since its instance
would be instantiated upon SDK start-up automatically. It's exposed in public interface
to help UI Testing app access the UI layer directly.
- `
  ``
  ``
  `

  ### [displayMessage(_:displayDelegate:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDefaultDisplayImpl#/c:objc(cs)FIRIAMDefaultDisplayImpl(im)displayMessage:displayDelegate:)

  `
  `  
  Conforms to display delegate for rendering of in-app messages.  

  #### Declaration

  Swift  

      func displayMessage(_ messageForDisplay: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage.html, displayDelegate: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplayDelegate.html)