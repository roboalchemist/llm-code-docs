# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Protocols/MessagingDelegate.md.txt

# FirebaseMessaging Framework Reference

# MessagingDelegate

    protocol MessagingDelegate : NSObjectProtocol

A protocol to handle token update or data message delivery from FCM.
- `
  ``
  ``
  `

  ### [messaging(_:didReceiveRegistrationToken:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Protocols/MessagingDelegate#/c:objc(pl)FIRMessagingDelegate(im)messaging:didReceiveRegistrationToken:)

  `
  `  
  This method will be called once a token is available, or has been refreshed. Typically it
  will be called once per app start, but may be called more often, if token is invalidated or
  updated. In this method, you should perform operations such as:
  - Uploading the FCM token to your application server, so targeted notifications can be sent.

  - Subscribing to any topics.

  #### Declaration

  Swift  

      optional func messaging(_ messaging: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging.html, didReceiveRegistrationToken fcmToken: String?)