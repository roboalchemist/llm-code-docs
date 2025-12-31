# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError.md.txt

# FirebaseStorage Framework Reference

# StorageError

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    public enum StorageError : Error, CustomNSError

Firebase Storage errors
- `
  ``
  ``
  `

  ### [unknown(message:serverError:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO7unknownyACSS_SDySSypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case unknown(message: String, serverError: [String : Any])

- `
  ``
  ``
  `

  ### [objectNotFound(object:serverError:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO14objectNotFoundyACSS_SDySSypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case objectNotFound(object: String, serverError: [String : Any])

- `
  ``
  ``
  `

  ### [bucketNotFound(bucket:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO14bucketNotFoundyACSS_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case bucketNotFound(bucket: String)

- `
  ``
  ``
  `

  ### [projectNotFound(project:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO15projectNotFoundyACSS_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case projectNotFound(project: String)

- `
  ``
  ``
  `

  ### [quotaExceeded(bucket:serverError:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO13quotaExceededyACSS_SDySSypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case quotaExceeded(bucket: String, serverError: [String : Any])

- `
  ``
  ``
  `

  ### [unauthenticated(serverError:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO15unauthenticatedyACSDySSypG_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case unauthenticated(serverError: [String : Any])

- `
  ``
  ``
  `

  ### [unauthorized(bucket:object:serverError:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO12unauthorizedyACSS_SSSDySSypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case unauthorized(bucket: String, object: String, serverError: [String : Any])

- `
  ``
  ``
  `

  ### [retryLimitExceeded](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO18retryLimitExceededyA2CmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case retryLimitExceeded

- `
  ``
  ``
  `

  ### [nonMatchingChecksum](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO19nonMatchingChecksumyA2CmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case nonMatchingChecksum

- `
  ``
  ``
  `

  ### [downloadSizeExceeded(total:maxSize:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO20downloadSizeExceededyACs5Int64V_AFtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case downloadSizeExceeded(total: Int64, maxSize: Int64)

- `
  ``
  ``
  `

  ### [cancelled](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO9cancelledyA2CmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case cancelled

- `
  ``
  ``
  `

  ### [invalidArgument(message:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO15invalidArgumentyACSS_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case invalidArgument(message: String)

- `
  ``
  ``
  `

  ### [internalError(message:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO08internalC0yACSS_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case internalError(message: String)

- `
  ``
  ``
  `

  ### [bucketMismatch(message:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO14bucketMismatchyACSS_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case bucketMismatch(message: String)

- `
  ``
  ``
  `

  ### [pathError(message:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO04pathC0yACSS_tcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case pathError(message: String)

[## CustomNSError](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/CustomNSError)

- `
  ``
  ``
  `

  ### [errorDomain](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO11errorDomainSSvpZ)

  `
  `  
  Default domain of the error.  

  #### Declaration

  Swift  

      public static var errorDomain: String { get }

- `
  ``
  ``
  `

  ### [errorCode](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO9errorCodeSivp)

  `
  `  
  The error code within the given domain.  

  #### Declaration

  Swift  

      public var errorCode: Int { get }

- `
  ``
  ``
  `

  ### [errorUserInfo](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Enums/StorageError#/s:15FirebaseStorage0B5ErrorO13errorUserInfoSDySSypGvp)

  `
  `  
  The default user-info dictionary.  

  #### Declaration

  Swift  

      public var errorUserInfo: [String : Any] { get }