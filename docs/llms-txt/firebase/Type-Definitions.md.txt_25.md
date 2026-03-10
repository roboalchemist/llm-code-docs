# Source: https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions.md.txt

# FirebaseInstanceID Framework Reference

# Type Definitions


Firebase Instance ID is deprecated. Please use Firebase Installations instead.

The following type definitions are available globally.
- `


  ### [InstanceIDTokenHandler](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions#/c:FIRInstanceID.h@T@FIRInstanceIDTokenHandler)


  ` @related FIRInstanceID

  The completion handler invoked when the InstanceID token returns. If
  the call fails we return the appropriate `error code` as described below.

  #### Declaration

  Swift

      typealias InstanceIDTokenHandler = (String?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` token ` | The valid token as returned by InstanceID backend. |
  | ` error ` | The error describing why generating a new token failed. See the error codes below for a more detailed description. |

- `


  ### [InstanceIDDeleteTokenHandler](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions#/c:FIRInstanceID.h@T@FIRInstanceIDDeleteTokenHandler)


  ` @related FIRInstanceID

  The completion handler invoked when the InstanceID `deleteToken` returns. If
  the call fails we return the appropriate `error code` as described below

  #### Declaration

  Swift

      typealias InstanceIDDeleteTokenHandler = (Error) -> Void

  #### Parameters

  |---|---|
  | ` error ` | The error describing why deleting the token failed. See the error codes below for a more detailed description. |

- `


  ### [InstanceIDHandler](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions#/c:FIRInstanceID.h@T@FIRInstanceIDHandler)


  ` @related FIRInstanceID

  The completion handler invoked when the app identity is created. If the
  identity wasn't created for some reason we return the appropriate error code.

  #### Declaration

  Swift

      typealias InstanceIDHandler = (String?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` identity ` | A valid identity for the app instance, nil if there was an error while creating an identity. |
  | ` error ` | The error if fetching the identity fails else nil. |

- `


  ### [InstanceIDDeleteHandler](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions#/c:FIRInstanceID.h@T@FIRInstanceIDDeleteHandler)


  ` @related FIRInstanceID

  The completion handler invoked when the app identity and all the tokens associated
  with it are deleted. Returns a valid error object in case of failure else nil.

  #### Declaration

  Swift

      typealias InstanceIDDeleteHandler = (Error?) -> Void

  #### Parameters

  |---|---|
  | ` error ` | The error if deleting the identity and all the tokens associated with it fails else nil. |

- `


  ### [InstanceIDResultHandler](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Type-Definitions#/c:FIRInstanceID.h@T@FIRInstanceIDResultHandler)


  ` @related FIRInstanceID

  The completion handler invoked when the app identity and token are fetched. If the
  identity wasn't created for some reason we return the appropriate error code.

  #### Declaration

  Swift

      typealias InstanceIDResultHandler = (https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceIDResult?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` result ` | The result containing an identity for the app instance and a valid token, nil if there was an error while creating the result. |
  | ` error ` | The error if fetching the identity or token fails else nil. |