# Source: https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID.md.txt

# FirebaseInstanceID Framework Reference

# InstanceID

    class InstanceID : NSObject

Firebase Instance ID is deprecated. Please use Firebase Installations instead.

Instance ID provides a unique identifier for each app instance and a mechanism
to authenticate and authorize actions (for example, sending an FCM message).

Once an InstanceID is generated, the library periodically sends information about the
application and the device where it's running to the Firebase backend. To stop this. see
`[FIRInstanceID deleteIDWithHandler:]`.

Instance ID is long lived but, may be reset if the device is not used for
a long time or the Instance ID service detects a problem.
If Instance ID is reset, the app will be notified via
`kFIRInstanceIDTokenRefreshNotification`.

If the Instance ID has become invalid, the app can request a new one and
send it to the app server.
To prove ownership of Instance ID and to allow servers to access data or
services associated with the app, call
`[FIRInstanceID tokenWithAuthorizedEntity:scope:options:handler]`.
- `
  ``
  ``
  `

  ### [instanceID()](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(cm)instanceID)

  `
  `  
  FIRInstanceID.  

  #### Declaration

  Swift  

      class func instanceID() -> Self

  #### Return Value

  A shared instance of FIRInstanceID.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(im)init)

  `
  `  
Unavailable. Use +instanceID instead.  
[## Tokens](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/Tokens)

- `
  ``
  ``
  `

  ### [instanceID(handler:)](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(im)instanceIDWithHandler:)

  `
  `  
  Returns a result of app instance identifier InstanceID and a Firebase Messaging scoped token.
  param handler The callback handler invoked when an app instanceID and a default token
  are generated and returned. If instanceID and token fetching fail for some
  reason the callback is invoked with nil `result` and the appropriate error.  

  #### Declaration

  Swift  

      func instanceID(handler: @escaping https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions.html#/c:FIRInstanceID.h@T@FIRInstanceIDResultHandler)

- `
  ``
  ``
  `

  ### [token(withAuthorizedEntity:scope:options:handler:)](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(im)tokenWithAuthorizedEntity:scope:options:handler:)

  `
  `  
  Returns a token that authorizes an Entity (example: cloud service) to perform
  an action on behalf of the application identified by Instance ID.

  This is similar to an OAuth2 token except, it applies to the
  application instance instead of a user.

  This is an asynchronous call. If the token fetching fails for some reason
  we invoke the completion callback with nil `token` and the appropriate
  error.

  This generates an Instance ID if it does not exist yet, which starts periodically sending
  information to the Firebase backend (see `[FIRInstanceID getIDWithHandler:]`).

  Note, you can only have one `token` or `deleteToken` call for a given
  authorizedEntity and scope at any point of time. Making another such call with the
  same authorizedEntity and scope before the last one finishes will result in an
  error with code `OperationInProgress`.  
  See

  FIRInstanceID deleteTokenWithAuthorizedEntity:scope:handler:  

  #### Declaration

  Swift  

      func token(withAuthorizedEntity authorizedEntity: String, scope: String, options: [AnyHashable : Any]? = nil, handler: @escaping https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions.html#/c:FIRInstanceID.h@T@FIRInstanceIDTokenHandler)

  #### Parameters

  |--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*authorizedEntity*` ` | Entity authorized by the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | ` `*scope*` `            | Action authorized for authorizedEntity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | ` `*options*` `          | The extra options to be sent with your token request. The value for the `apns_token` should be the NSData object passed to the UIApplicationDelegate's `didRegisterForRemoteNotificationsWithDeviceToken` method. The value for `apns_sandbox` should be a boolean (or an NSNumber representing a BOOL in Objective-C) set to true if your app is a debug build, which means that the APNs device token is for the sandbox environment. It should be set to false otherwise. If the `apns_sandbox` key is not provided, an automatically-detected value shall be used. |
  | ` `*handler*` `          | The callback handler which is invoked when the token is successfully fetched. In case of success a valid `token` and `nil` error are returned. In case of any error the `token` is nil and a valid `error` is returned. The valid error codes have been documented above.                                                                                                                                                                                                                                                                                              |

- `
  ``
  ``
  `

  ### [deleteToken(withAuthorizedEntity:scope:handler:)](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(im)deleteTokenWithAuthorizedEntity:scope:handler:)

  `
  `  
  Revokes access to a scope (action) for an entity previously
  authorized by `[FIRInstanceID tokenWithAuthorizedEntity:scope:options:handler]`.

  This is an asynchronous call. Call this on the main thread since InstanceID lib
  is not thread safe. In case token deletion fails for some reason we invoke the
  `handler` callback passed in with the appropriate error code.

  Note, you can only have one `token` or `deleteToken` call for a given
  authorizedEntity and scope at a point of time. Making another such call with the
  same authorizedEntity and scope before the last one finishes will result in an error
  with code `OperationInProgress`.  

  #### Declaration

  Swift  

      func deleteToken(withAuthorizedEntity authorizedEntity: String, scope: String, handler: @escaping https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions.html#/c:FIRInstanceID.h@T@FIRInstanceIDDeleteTokenHandler)

  #### Parameters

  |--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*authorizedEntity*` ` | Entity that must no longer have access.                                                                                                 |
  | ` `*scope*` `            | Action that entity is no longer authorized to perform.                                                                                  |
  | ` `*handler*` `          | The handler that is invoked once the unsubscribe call ends. In case of error an appropriate error object is returned else error is nil. |

[## Identity](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/Identity)

- `
  ``
  ``
  `

  ### [getID(handler:)](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(im)getIDWithHandler:)

  `
  `  
  Asynchronously fetch a stable identifier that uniquely identifies the app
  instance. If the identifier has been revoked or has expired, this method will
  return a new identifier.

  Once an InstanceID is generated, the library periodically sends information about the
  application and the device where it's running to the Firebase backend. To stop this. see
  `[FIRInstanceID deleteIDWithHandler:]`.  

  #### Declaration

  Swift  

      func getID(handler: @escaping https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions.html#/c:FIRInstanceID.h@T@FIRInstanceIDHandler)

  #### Parameters

  |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*handler*` ` | The handler to invoke once the identifier has been fetched. In case of error an appropriate error object is returned else a valid identifier is returned and a valid identifier for the application instance. |

- `
  ``
  ``
  `

  ### [deleteID(handler:)](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID#/c:objc(cs)FIRInstanceID(im)deleteIDWithHandler:)

  `
  `  
  Resets Instance ID and revokes all tokens.

  This method also triggers a request to fetch a new Instance ID and Firebase Messaging scope
  token. Please listen to kFIRInstanceIDTokenRefreshNotification when the new ID and token are
  ready.

  This stops the periodic sending of data to the Firebase backend that began when the Instance ID
  was generated. No more data is sent until another library calls Instance ID internally again
  (like FCM, RemoteConfig or Analytics) or user explicitly calls Instance ID APIs to get an
  Instance ID and token again.  

  #### Declaration

  Swift  

      func deleteID(handler: @escaping https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions.html#/c:FIRInstanceID.h@T@FIRInstanceIDDeleteHandler)