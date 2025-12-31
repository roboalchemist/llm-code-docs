# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode.md.txt

# FirebaseStorage Framework Reference

# StorageErrorCode

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageErrorCode)
    public enum StorageErrorCode : Int, Swift.Error

Adds wrappers for common Firebase Storage errors (including creating errors from GCS errors).
For more information on unwrapping GCS errors, see the GCS errors docs:
<https://cloud.google.com/storage/docs/json_api/v1/status-codes>
This is never publicly exposed to end developers (as they will simply see an NSError).
- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeUnknown)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case unknown = -13000

- `
  ``
  ``
  `

  ### [objectNotFound](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeObjectNotFound)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case objectNotFound = -13010

- `
  ``
  ``
  `

  ### [bucketNotFound](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeBucketNotFound)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case bucketNotFound = -13011

- `
  ``
  ``
  `

  ### [projectNotFound](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeProjectNotFound)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case projectNotFound = -13012

- `
  ``
  ``
  `

  ### [quotaExceeded](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeQuotaExceeded)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case quotaExceeded = -13013

- `
  ``
  ``
  `

  ### [unauthenticated](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeUnauthenticated)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case unauthenticated = -13020

- `
  ``
  ``
  `

  ### [unauthorized](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeUnauthorized)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case unauthorized = -13021

- `
  ``
  ``
  `

  ### [retryLimitExceeded](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeRetryLimitExceeded)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case retryLimitExceeded = -13030

- `
  ``
  ``
  `

  ### [nonMatchingChecksum](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeNonMatchingChecksum)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case nonMatchingChecksum = -13031

- `
  ``
  ``
  `

  ### [downloadSizeExceeded](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeDownloadSizeExceeded)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case downloadSizeExceeded = -13032

- `
  ``
  ``
  `

  ### [cancelled](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeCancelled)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case cancelled = -13040

- `
  ``
  ``
  `

  ### [invalidArgument](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeInvalidArgument)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case invalidArgument = -13050

- `
  ``
  ``
  `

  ### [bucketMismatch](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeBucketMismatch)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case bucketMismatch = -13051

- `
  ``
  ``
  `

  ### [internalError](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodeInternalError)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case internalError = -13052

- `
  ``
  ``
  `

  ### [pathError](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageErrorCode#/c:@M@FirebaseStorage@E@FIRStorageErrorCode@FIRStorageErrorCodePathError)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case pathError = -13053