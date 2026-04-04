# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types.md.txt

# FirebaseFirestore Framework Reference

# _ErrorType

    typealias FirestoreErrorCode.Code._ErrorType = FirestoreErrorCode

Error codes used by Cloud Firestore.
- `


  ### [OK](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeOK)


  ` The operation completed successfully. `NSError` objects will never have a code with this
  value.

  #### Declaration

  Swift

      static var OK: FirestoreErrorCode.Code { get }

- `


  ### [cancelled](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeCancelled)


  ` The operation was cancelled (typically by the caller).

  #### Declaration

  Swift

      static var cancelled: FirestoreErrorCode.Code { get }

- `


  ### [unknown](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnknown)


  ` Unknown error or an error from a different error domain.

  #### Declaration

  Swift

      static var unknown: FirestoreErrorCode.Code { get }

- `


  ### [invalidArgument](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeInvalidArgument)


  ` Client specified an invalid argument. Note that this differs from FailedPrecondition.
  InvalidArgument indicates arguments that are problematic regardless of the state of the
  system (e.g., an invalid field name).

  #### Declaration

  Swift

      static var invalidArgument: FirestoreErrorCode.Code { get }

- `


  ### [deadlineExceeded](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeDeadlineExceeded)


  ` Deadline expired before operation could complete. For operations that change the state of the
  system, this error may be returned even if the operation has completed successfully. For
  example, a successful response from a server could have been delayed long enough for the
  deadline to expire.

  #### Declaration

  Swift

      static var deadlineExceeded: FirestoreErrorCode.Code { get }

- `


  ### [notFound](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeNotFound)


  ` Some requested document was not found.

  #### Declaration

  Swift

      static var notFound: FirestoreErrorCode.Code { get }

- `


  ### [alreadyExists](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeAlreadyExists)


  ` Some document that we attempted to create already exists.

  #### Declaration

  Swift

      static var alreadyExists: FirestoreErrorCode.Code { get }

- `


  ### [permissionDenied](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodePermissionDenied)


  ` The caller does not have permission to execute the specified operation.

  #### Declaration

  Swift

      static var permissionDenied: FirestoreErrorCode.Code { get }

- `


  ### [resourceExhausted](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeResourceExhausted)


  ` Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system
  is out of space.

  #### Declaration

  Swift

      static var resourceExhausted: FirestoreErrorCode.Code { get }

- `


  ### [failedPrecondition](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeFailedPrecondition)


  ` Operation was rejected because the system is not in a state required for the operation's
  execution.

  #### Declaration

  Swift

      static var failedPrecondition: FirestoreErrorCode.Code { get }

- `


  ### [aborted](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeAborted)


  ` The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.

  #### Declaration

  Swift

      static var aborted: FirestoreErrorCode.Code { get }

- `


  ### [outOfRange](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeOutOfRange)


  ` Operation was attempted past the valid range.

  #### Declaration

  Swift

      static var outOfRange: FirestoreErrorCode.Code { get }

- `


  ### [unimplemented](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnimplemented)


  ` Operation is not implemented or not supported/enabled.

  #### Declaration

  Swift

      static var unimplemented: FirestoreErrorCode.Code { get }

- `


  ### [internal](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeInternal)


  ` Internal errors. Means some invariants expected by underlying system has been broken. If you
  see one of these errors, something is very broken.

  #### Declaration

  Swift

      static var `internal`: FirestoreErrorCode.Code { get }

- `


  ### [unavailable](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnavailable)


  ` The service is currently unavailable. This is a most likely a transient condition and may be
  corrected by retrying with a backoff.

  #### Declaration

  Swift

      static var unavailable: FirestoreErrorCode.Code { get }

- `


  ### [dataLoss](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeDataLoss)


  ` Unrecoverable data loss or corruption.

  #### Declaration

  Swift

      static var dataLoss: FirestoreErrorCode.Code { get }

- `


  ### [unauthenticated](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types#/c:@E@FIRFirestoreErrorCode@FIRFirestoreErrorCodeUnauthenticated)


  ` The request does not have valid authentication credentials for the operation.

  #### Declaration

  Swift

      static var unauthenticated: FirestoreErrorCode.Code { get }