# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Protocols/FIRMessagingDelegate.md.txt

# FirebaseMessaging Framework Reference

# FIRMessagingDelegate

    @protocol FIRMessagingDelegate <NSObject>

A protocol to handle token update or data message delivery from FCM.
- `
  ``
  ``
  `

  ### [-messaging:didReceiveRegistrationToken:](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Protocols/FIRMessagingDelegate#/c:objc(pl)FIRMessagingDelegate(im)messaging:didReceiveRegistrationToken:)

  `
  `  
  This method will be called once a token is available, or has been refreshed. Typically it
  will be called once per app start, but may be called more often, if token is invalidated or
  updated. In this method, you should perform operations such as:
  - Uploading the FCM token to your application server, so targeted notifications can be sent.

  - Subscribing to any topics.

  #### Declaration

  Objective-C  

      - (void)messaging:(nonnull https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessaging.html *)messaging
          didReceiveRegistrationToken:(nullable NSString *)fcmToken;