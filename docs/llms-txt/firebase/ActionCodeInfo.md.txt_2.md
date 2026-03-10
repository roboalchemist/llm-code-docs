# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo.md.txt

# FirebaseAuth Framework Reference

# ActionCodeInfo

    @objc(FIRActionCodeInfo)
    open class ActionCodeInfo : NSObject, @unchecked Sendable

Manages information regarding action codes.
- `


  ### [operation](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeInfo(py)operation)


  ` The operation being performed.

  #### Declaration

  Swift

      @objc
      public let operation: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation.html

- `


  ### [email](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeInfo(py)email)


  ` The email address to which the code was sent. The new email address in the case of
  `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation.html#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationRecoverEmail`.

  #### Declaration

  Swift

      @objc
      public let email: String

- `


  ### [previousEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeInfo#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeInfo(py)previousEmail)


  ` The email that is being recovered in the case of `https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation.html#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationRecoverEmail`.

  #### Declaration

  Swift

      @objc
      public let previousEmail: String?