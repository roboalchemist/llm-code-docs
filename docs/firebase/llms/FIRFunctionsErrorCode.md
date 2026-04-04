# Source: https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode.md.txt

# FirebaseFunctions Framework Reference

# FIRFunctionsErrorCode

    enum FIRFunctionsErrorCode : NSInteger {}

The set of error status codes that can be returned from a Callable HTTPS tigger. These are the
canonical error codes for Google APIs, as documented here:
<https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto#L26>
- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeOK](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeOK)

  `
  `  
  The operation completed successfully.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeOK = 0

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeCancelled](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeCancelled)

  `
  `  
  The operation was cancelled (typically by the caller).  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeCancelled = 1

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeUnknown](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnknown)

  `
  `  
  Unknown error or an error from a different error domain.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeUnknown = 2

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeInvalidArgument](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeInvalidArgument)

  `
  `  
  Client specified an invalid argument. Note that this differs from `FailedPrecondition`.
  `InvalidArgument` indicates arguments that are problematic regardless of the state of the
  system (e.g., an invalid field name).  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeInvalidArgument = 3

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeDeadlineExceeded](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeDeadlineExceeded)

  `
  `  
  Deadline expired before operation could complete. For operations that change the state of the
  system, this error may be returned even if the operation has completed successfully. For
  example, a successful response from a server could have been delayed long enough for the
  deadline to expire.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeDeadlineExceeded = 4

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeNotFound](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeNotFound)

  `
  `  
  Some requested document was not found.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeNotFound = 5

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeAlreadyExists](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeAlreadyExists)

  `
  `  
  Some document that we attempted to create already exists.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeAlreadyExists = 6

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodePermissionDenied](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodePermissionDenied)

  `
  `  
  The caller does not have permission to execute the specified operation.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodePermissionDenied = 7

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeResourceExhausted](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeResourceExhausted)

  `
  `  
  Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system
  is out of space.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeResourceExhausted = 8

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeFailedPrecondition](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeFailedPrecondition)

  `
  `  
  Operation was rejected because the system is not in a state required for the operation's
  execution.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeFailedPrecondition = 9

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeAborted](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeAborted)

  `
  `  
  The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeAborted = 10

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeOutOfRange](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeOutOfRange)

  `
  `  
  Operation was attempted past the valid range.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeOutOfRange = 11

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeUnimplemented](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnimplemented)

  `
  `  
  Operation is not implemented or not supported/enabled.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeUnimplemented = 12

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeInternal](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeInternal)

  `
  `  
  Internal errors. Means some invariant expected by underlying system has been broken. If you
  see one of these errors, something is very broken.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeInternal = 13

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeUnavailable](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnavailable)

  `
  `  
  The service is currently unavailable. This is a most likely a transient condition and may be
  corrected by retrying with a backoff.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeUnavailable = 14

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeDataLoss](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeDataLoss)

  `
  `  
  Unrecoverable data loss or corruption.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeDataLoss = 15

- `
  ``
  ``
  `

  ### [FIRFunctionsErrorCodeUnauthenticated](https://firebase.google.com/docs/reference/ios/firebasefunctions/api/reference/Enums/FIRFunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnauthenticated)

  `
  `  
  The request does not have valid authentication credentials for the operation.  

  #### Declaration

  Objective-C  

      FIRFunctionsErrorCodeUnauthenticated = 16