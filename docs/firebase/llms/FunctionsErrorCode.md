# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode.md.txt

# FirebaseFunctions Framework Reference

# FunctionsErrorCode

    @objc(FIRFunctionsErrorCode)
    public enum FunctionsErrorCode : Int, Sendable

The set of error status codes that can be returned from a Callable HTTPS trigger. These are the
canonical error codes for Google APIs, as documented here:
<https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto#L26>
- `
  ``
  ``
  `

  ### [OK](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeOK)

  `
  `  
  The operation completed successfully.  

  #### Declaration

  Swift  

      case OK = 0

- `
  ``
  ``
  `

  ### [cancelled](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeCancelled)

  `
  `  
  The operation was cancelled (typically by the caller).  

  #### Declaration

  Swift  

      case cancelled = 1

- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnknown)

  `
  `  
  Unknown error or an error from a different error domain.  

  #### Declaration

  Swift  

      case unknown = 2

- `
  ``
  ``
  `

  ### [invalidArgument](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeInvalidArgument)

  `
  `  
  Client specified an invalid argument. Note that this differs from `FailedPrecondition`.
  `InvalidArgument` indicates arguments that are problematic regardless of the state of the
  system (e.g., an invalid field name).  

  #### Declaration

  Swift  

      case invalidArgument = 3

- `
  ``
  ``
  `

  ### [deadlineExceeded](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeDeadlineExceeded)

  `
  `  
  Deadline expired before operation could complete. For operations that change the state of the
  system, this error may be returned even if the operation has completed successfully. For
  example, a successful response from a server could have been delayed long enough for the
  deadline to expire.  

  #### Declaration

  Swift  

      case deadlineExceeded = 4

- `
  ``
  ``
  `

  ### [notFound](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeNotFound)

  `
  `  
  Some requested document was not found.  

  #### Declaration

  Swift  

      case notFound = 5

- `
  ``
  ``
  `

  ### [alreadyExists](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeAlreadyExists)

  `
  `  
  Some document that we attempted to create already exists.  

  #### Declaration

  Swift  

      case alreadyExists = 6

- `
  ``
  ``
  `

  ### [permissionDenied](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodePermissionDenied)

  `
  `  
  The caller does not have permission to execute the specified operation.  

  #### Declaration

  Swift  

      case permissionDenied = 7

- `
  ``
  ``
  `

  ### [resourceExhausted](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeResourceExhausted)

  `
  `  
  Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system
  is out of space.  

  #### Declaration

  Swift  

      case resourceExhausted = 8

- `
  ``
  ``
  `

  ### [failedPrecondition](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeFailedPrecondition)

  `
  `  
  Operation was rejected because the system is not in a state required for the operation's
  execution.  

  #### Declaration

  Swift  

      case failedPrecondition = 9

- `
  ``
  ``
  `

  ### [aborted](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeAborted)

  `
  `  
  The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.  

  #### Declaration

  Swift  

      case aborted = 10

- `
  ``
  ``
  `

  ### [outOfRange](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeOutOfRange)

  `
  `  
  Operation was attempted past the valid range.  

  #### Declaration

  Swift  

      case outOfRange = 11

- `
  ``
  ``
  `

  ### [unimplemented](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnimplemented)

  `
  `  
  Operation is not implemented or not supported/enabled.  

  #### Declaration

  Swift  

      case unimplemented = 12

- `
  ``
  ``
  `

  ### [internal](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeInternal)

  `
  `  
  Internal errors. Means some invariant expected by underlying system has been broken. If you
  see one of these errors, something is very broken.  

  #### Declaration

  Swift  

      case `internal` = 13

- `
  ``
  ``
  `

  ### [unavailable](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnavailable)

  `
  `  
  The service is currently unavailable. This is a most likely a transient condition and may be
  corrected by retrying with a backoff.  

  #### Declaration

  Swift  

      case unavailable = 14

- `
  ``
  ``
  `

  ### [dataLoss](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeDataLoss)

  `
  `  
  Unrecoverable data loss or corruption.  

  #### Declaration

  Swift  

      case dataLoss = 15

- `
  ``
  ``
  `

  ### [unauthenticated](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Enums/FunctionsErrorCode#/c:@M@FirebaseFunctions@E@FIRFunctionsErrorCode@FIRFunctionsErrorCodeUnauthenticated)

  `
  `  
  The request does not have valid authentication credentials for the operation.  

  #### Declaration

  Swift  

      case unauthenticated = 16