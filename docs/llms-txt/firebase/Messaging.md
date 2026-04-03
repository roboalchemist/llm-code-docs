# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging.md.txt

# FirebaseMessaging Framework Reference

# Messaging

    class Messaging : NSObject

Firebase Messaging lets you reliably deliver messages.

To send or receive messages, the app must get a
registration token. This token authorizes an
app server to send messages to an app instance.

In order to handle incoming Messaging messages, set the
`UNUserNotificationCenter`'s `delegate` property
and implement the appropriate methods.
- `
  ``
  ``
  `

  ### [delegate](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(py)delegate)

  `
  `  
  Delegate to handle FCM token refreshes, and remote data messages received via FCM direct channel.  

  #### Declaration

  Swift  

      weak var delegate: (any https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Protocols/MessagingDelegate.html)? { get set }

- `
  ``
  ``
  `

  ### [messaging()](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(cm)messaging)

  `
  `  
  FIRMessaging  

  #### Declaration

  Swift  

      class func messaging() -> Self

  #### Return Value

  An instance of Messaging.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)init)

  `
  `  
  Unavailable

  Use +messaging instead.  
Unavailable. Use +messaging instead.  
[## APNs](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/APNs)

- `
  ``
  ``
  `

  ### [apnsToken](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(py)APNSToken)

  `
  `  
  This property is used to set the APNs Token received by the application delegate.

  Messaging uses method swizzling to ensure that the APNs token is set
  automatically. However, if you have disabled swizzling by setting
  `FirebaseAppDelegateProxyEnabled` to `NO` in your app's
  Info.plist, you should manually set the APNs token in your application
  delegate's `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`
  method.

  If you would like to set the type of the APNs token, rather than relying on
  automatic detection, see [setAPNSToken(_:type:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging.html#/c:objc(cs)FIRMessaging(im)setAPNSToken:type:).  

  #### Declaration

  Swift  

      var apnsToken: Data? { get set }

- `
  ``
  ``
  `

  ### [setAPNSToken(_:type:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)setAPNSToken:type:)

  `
  `  
  Set the APNs token for the application. This token will be used to register
  with Firebase Messaging, and will be associated with the app's installation ID
  in the form of an FCM token.  

  #### Declaration

  Swift  

      func setAPNSToken(_ apnsToken: Data, type: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingAPNSTokenType.html)

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*apnsToken*` ` | The APNs token for the application.                                                                                                                                                                                        |
  | ` `*type*` `      | The type of APNs token. Debug builds should use `MessagingAPNSTokenTypeSandbox`. Alternatively, you can supply `MessagingAPNSTokenTypeUnknown` to have the type automatically detected based on your provisioning profile. |

[## FCM Tokens](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/FCM-Tokens)

- `
  ``
  ``
  `

  ### [isAutoInitEnabled](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(py)autoInitEnabled)

  `
  `  
  Is Firebase Messaging token auto generation enabled? If this flag is disabled, Firebase
  Messaging will not generate an FCM token automatically for message delivery.

  If this flag is disabled, Firebase Messaging does not generate new tokens automatically for
  message delivery. If this flag is enabled, FCM generates a registration token on application
  start when there is no existing valid token and periodically refreshes the token and sends
  data to the Firebase backend.

  This setting is persisted, and is applied on future invocations of your application. Once
  explicitly set, it overrides any settings in your Info.plist.

  By default, FCM automatic initialization is enabled. If you need to change the
  default (for example, because you want to prompt the user before getting a token),
  set `FirebaseMessagingAutoInitEnabled` to NO in your application's Info.plist.  

  #### Declaration

  Swift  

      var isAutoInitEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [fcmToken](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(py)FCMToken)

  `
  `  
  The FCM registration token is used to identify this device so that FCM can send notifications to
  it. It is associated with your APNs token when the APNs token is supplied, so messages sent to
  the FCM token will be delivered over APNs.

  The FCM registration token is sometimes refreshed automatically. In your Messaging delegate,
  the delegate method `messaging(_:didReceiveRegistrationToken:)` will be called once a token is
  available, or has been refreshed. Typically it should be called once per app start, but
  may be called more often if the token is invalidated or updated.

  Once you have an FCM registration token, you should send it to your application server, where
  it can be used to send notifications to your device.  

  #### Declaration

  Swift  

      var fcmToken: String? { get }

- `
  ``
  ``
  `

  ### [token()](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)tokenWithCompletion:)

  `
  `  
  Asynchronously gets the default FCM registration token.

  This creates a Firebase Installations ID, if one does not exist, and sends information about the
  application and the device to the Firebase backend. A network connection is required for the
  method to succeed. To stop this, see [Messaging.isAutoInitEnabled](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging.html#/c:objc(cs)FIRMessaging(py)autoInitEnabled),
  `Messaging.delete(completion:)` and `Installations.delete(completion:)`.  

  #### Declaration

  Swift  

      func token() async throws -> String

  #### Parameters

  |--------------------|-----------------------------------------------------|
  | ` `*completion*` ` | The completion handler to handle the token request. |

- `
  ``
  ``
  `

  ### [deleteToken()](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)deleteTokenWithCompletion:)

  `
  `  
  Asynchronously deletes the default FCM registration token.

  This does not delete all tokens for non-default sender IDs, See `Messaging.delete(completion:)`
  for deleting all of them. To prevent token auto generation, see [Messaging.isAutoInitEnabled](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging.html#/c:objc(cs)FIRMessaging(py)autoInitEnabled).  

  #### Declaration

  Swift  

      func deleteToken() async throws

  #### Parameters

  |--------------------|------------------------------------------------------|
  | ` `*completion*` ` | The completion handler to handle the token deletion. |

- `
  ``
  ``
  `

  ### [retrieveFCMToken(forSenderID:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)retrieveFCMTokenForSenderID:completion:)

  `
  `  
  Retrieves an FCM registration token for a particular Sender ID. This can be used to allow
  multiple senders to send notifications to the same device. By providing a different Sender
  ID than your default when fetching a token, you can create a new FCM token which you can
  give to a different sender. Both tokens will deliver notifications to your device, and you
  can revoke a token when you need to.

  This registration token is not cached by FIRMessaging. FIRMessaging should have an APNs
  token set before calling this to ensure that notifications can be delivered via APNs using
  this FCM token. You may re-retrieve the FCM token once you have the APNs token set, to
  associate it with the FCM token. The default FCM token is automatically associated with
  the APNs token, if the APNs token data is available.

  This creates a Firebase Installations ID, if one does not exist, and sends information
  about the application and the device to the Firebase backend.  

  #### Declaration

  Swift  

      func retrieveFCMToken(forSenderID senderID: String) async throws -> String

  #### Parameters

  |--------------------|-----------------------------------------------------|
  | ` `*senderID*` `   | The Sender ID for a particular Firebase project.    |
  | ` `*completion*` ` | The completion handler to handle the token request. |

- `
  ``
  ``
  `

  ### [deleteFCMToken(forSenderID:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)deleteFCMTokenForSenderID:completion:)

  `
  `  
  Invalidates an FCM token for a particular Sender ID. That Sender ID cannot no longer send
  notifications to that FCM token. This does not delete the Firebase Installations ID that may have
  been created when generating the token. See `Installations.delete(completion:)`.  

  #### Declaration

  Swift  

      func deleteFCMToken(forSenderID senderID: String) async throws

  #### Parameters

  |--------------------|------------------------------------------------------|
  | ` `*senderID*` `   | The senderID for a particular Firebase project.      |
  | ` `*completion*` ` | The completion handler to handle the token deletion. |

[## Topics](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/Topics)

- `
  ``
  ``
  `

  ### [subscribe(toTopic:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)subscribeToTopic:)

  `
  `  
  Asynchronously subscribes to a topic. This uses the default FCM registration token to identify
  the app instance and periodically sends data to the Firebase backend. To stop this, see
  `Messaging.delete(completion:)` and `Installations.delete(completion:)`.  

  #### Declaration

  Swift  

      func subscribe(toTopic topic: String)

  #### Parameters

  |---------------|------------------------------------------------|
  | ` `*topic*` ` | The name of the topic, for example, @"sports". |

- `
  ``
  ``
  `

  ### [subscribe(toTopic:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)subscribeToTopic:completion:)

  `
  `  
  Asynchronously subscribe to the provided topic, retrying on failure. This uses the default FCM
  registration token to identify the app instance and periodically sends data to the Firebase
  backend. To stop this, see `Messaging.delete(completion:)` and
  `Installations.delete(completion:)`.  

  #### Declaration

  Swift  

      func subscribe(toTopic topic: String) async throws

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*topic*` `      | The topic name to subscribe to, for example, @"sports".                                                                                                           |
  | ` `*completion*` ` | The completion that is invoked once the subscribe call ends. On success, the error parameter is always `nil`. Otherwise, an appropriate error object is returned. |

- `
  ``
  ``
  `

  ### [unsubscribe(fromTopic:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)unsubscribeFromTopic:)

  `
  `  
  Asynchronously unsubscribe from a topic. This uses a FCM Token
  to identify the app instance and periodically sends data to the Firebase backend. To stop this,
  see `Messaging.delete(completion:)` and `Installations.delete(completion:)`.  

  #### Declaration

  Swift  

      func unsubscribe(fromTopic topic: String)

  #### Parameters

  |---------------|-----------------------------------------------|
  | ` `*topic*` ` | The name of the topic, for example @"sports". |

- `
  ``
  ``
  `

  ### [unsubscribe(fromTopic:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)unsubscribeFromTopic:completion:)

  `
  `  
  Asynchronously unsubscribe from the provided topic, retrying on failure. This uses a FCM Token
  to identify the app instance and periodically sends data to the Firebase backend. To stop this,
  see `Messaging.delete(completion:)` and `Installations.delete(completion:)`.  

  #### Declaration

  Swift  

      func unsubscribe(fromTopic topic: String) async throws

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*topic*` `      | The topic name to unsubscribe from, for example @"sports".                                                                                                    |
  | ` `*completion*` ` | The completion that is invoked once the unsubscribe call ends. In case of success, nil error is returned. Otherwise, an appropriate error object is returned. |

[## Analytics](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/Analytics)

- `
  ``
  ``
  `

  ### [appDidReceiveMessage(_:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)appDidReceiveMessage:)

  `
  `  
  Use this to track message delivery and analytics for messages, typically
  when you receive a notification in `application:didReceiveRemoteNotification:`.
  However, you only need to call this if you set the `FirebaseAppDelegateProxyEnabled`
  flag to `NO` in your Info.plist. If `FirebaseAppDelegateProxyEnabled` is either missing
  or set to `YES` in your Info.plist, the library will call this automatically.  

  #### Declaration

  Swift  

      func appDidReceiveMessage(_ message: [AnyHashable : Any]) -> https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/MessagingMessageInfo.html

  #### Parameters

  |-----------------|-----------------------------------------------------|
  | ` `*message*` ` | The downstream message received by the application. |

  #### Return Value

Information about the downstream message.  
[## GDPR](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/GDPR)

- `
  ``
  ``
  `

  ### [deleteData()](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)deleteDataWithCompletion:)

  `
  `  
  Deletes all the tokens and checkin data of the Firebase project and related data on the server
  side. A network connection is required for the method to succeed.

  This does not delete the Firebase Installations ID. See `Installations.delete(completion:)`.
  To prevent token auto generation, see [Messaging.isAutoInitEnabled](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging.html#/c:objc(cs)FIRMessaging(py)autoInitEnabled).  

  #### Declaration

  Swift  

      func deleteData() async throws

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A completion handler which is invoked when the operation completes. `error == nil` indicates success. |