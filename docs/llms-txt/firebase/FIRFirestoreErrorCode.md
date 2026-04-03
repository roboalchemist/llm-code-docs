# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode.md.txt

# FirebaseFirestore Framework Reference

# FIRFirestoreErrorCode

    enum FIRFirestoreErrorCode : NSInteger {}

Error codes used by Cloud Firestore.
- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeOK](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeOK)

  `
  `  
  The operation completed successfully. `NSError` objects will never have a code with this
  value.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeOK = 0

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeCancelled](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeCancelled)

  `
  `  
  The operation was cancelled (typically by the caller).  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeCancelled = 1

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeUnknown](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnknown)

  `
  `  
  Unknown error or an error from a different error domain.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeUnknown = 2

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeInvalidArgument](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeInvalidArgument)

  `
  `  
  Client specified an invalid argument. Note that this differs from FailedPrecondition.
  InvalidArgument indicates arguments that are problematic regardless of the state of the
  system (e.g., an invalid field name).  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeInvalidArgument = 3

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeDeadlineExceeded](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeDeadlineExceeded)

  `
  `  
  Deadline expired before operation could complete. For operations that change the state of the
  system, this error may be returned even if the operation has completed successfully. For
  example, a successful response from a server could have been delayed long enough for the
  deadline to expire.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeDeadlineExceeded = 4

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeNotFound](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeNotFound)

  `
  `  
  Some requested document was not found.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeNotFound = 5

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeAlreadyExists](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeAlreadyExists)

  `
  `  
  Some document that we attempted to create already exists.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeAlreadyExists = 6

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodePermissionDenied](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodePermissionDenied)

  `
  `  
  The caller does not have permission to execute the specified operation.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodePermissionDenied = 7

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeResourceExhausted](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeResourceExhausted)

  `
  `  
  Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system
  is out of space.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeResourceExhausted = 8

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeFailedPrecondition](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeFailedPrecondition)

  `
  `  
  Operation was rejected because the system is not in a state required for the operation's
  execution.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeFailedPrecondition = 9

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeAborted](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeAborted)

  `
  `  
  The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeAborted = 10

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeOutOfRange](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeOutOfRange)

  `
  `  
  Operation was attempted past the valid range.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeOutOfRange = 11

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeUnimplemented](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnimplemented)

  `
  `  
  Operation is not implemented or not supported/enabled.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeUnimplemented = 12

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeInternal](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeInternal)

  `
  `  
  Internal errors. Means some invariants expected by underlying system has been broken. If you
  see one of these errors, something is very broken.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeInternal = 13

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeUnavailable](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnavailable)

  `
  `  
  The service is currently unavailable. This is a most likely a transient condition and may be
  corrected by retrying with a backoff.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeUnavailable = 14

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeDataLoss](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeDataLoss)

  `
  `  
  Unrecoverable data loss or corruption.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeDataLoss = 15

- `
  ``
  ``
  `

  ### [FIRFirestoreErrorCodeUnauthenticated](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreErrorCode#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnauthenticated)

  `
  `  
  The request does not have valid authentication credentials for the operation.  

  #### Declaration

  Objective-C  

      FIRFirestoreErrorCodeUnauthenticated = 16