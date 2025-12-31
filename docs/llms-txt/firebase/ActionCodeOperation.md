# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation.md.txt

# FirebaseAuth Framework Reference

# ActionCodeOperation

    @objc(FIRActionCodeOperation)
    public enum ActionCodeOperation : Int, Sendable

Operations which can be performed with action codes.
- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationUnknown)

  `
  `  
  Action code for unknown operation.  

  #### Declaration

  Swift  

      case unknown = 0

- `
  ``
  ``
  `

  ### [passwordReset](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationPasswordReset)

  `
  `  
  Action code for password reset operation.  

  #### Declaration

  Swift  

      case passwordReset = 1

- `
  ``
  ``
  `

  ### [verifyEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationVerifyEmail)

  `
  `  
  Action code for verify email operation.  

  #### Declaration

  Swift  

      case verifyEmail = 2

- `
  ``
  ``
  `

  ### [recoverEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationRecoverEmail)

  `
  `  
  Action code for recover email operation.  

  #### Declaration

  Swift  

      case recoverEmail = 3

- `
  ``
  ``
  `

  ### [emailLink](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationEmailLink)

  `
  `  
  Action code for email link operation.  

  #### Declaration

  Swift  

      case emailLink = 4

- `
  ``
  ``
  `

  ### [verifyAndChangeEmail](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationVerifyAndChangeEmail)

  `
  `  
  Action code for verifying and changing email.  

  #### Declaration

  Swift  

      case verifyAndChangeEmail = 5

- `
  ``
  ``
  `

  ### [revertSecondFactorAddition](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/ActionCodeOperation#/c:@M@FirebaseAuth@E@FIRActionCodeOperation@FIRActionCodeOperationRevertSecondFactorAddition)

  `
  `  
  Action code for reverting second factor addition.  

  #### Declaration

  Swift  

      case revertSecondFactorAddition = 6