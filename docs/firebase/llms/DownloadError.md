# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError.md.txt

# FirebaseMLModelDownloader Framework Reference

# DownloadError

    public enum DownloadError : Error, Equatable

Possible errors with model downloading.
- `
  ``
  ``
  `

  ### [notFound](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO8notFoundyA2CmF)

  `
  `  
  No model with this name exists on server.  

  #### Declaration

  Swift  

      case notFound

- `
  ``
  ``
  `

  ### [permissionDenied](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO16permissionDeniedyA2CmF)

  `
  `  
  Invalid, incomplete, or missing permissions for model download.  

  #### Declaration

  Swift  

      case permissionDenied

- `
  ``
  ``
  `

  ### [failedPrecondition](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO18failedPreconditionyA2CmF)

  `
  `  
  Conditions not met to perform download.  

  #### Declaration

  Swift  

      case failedPrecondition

- `
  ``
  ``
  `

  ### [resourceExhausted](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO17resourceExhaustedyA2CmF)

  `
  `  
  Requests quota exhausted.  

  #### Declaration

  Swift  

      case resourceExhausted

- `
  ``
  ``
  `

  ### [notEnoughSpace](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO14notEnoughSpaceyA2CmF)

  `
  `  
  Not enough space for model on device.  

  #### Declaration

  Swift  

      case notEnoughSpace

- `
  ``
  ``
  `

  ### [invalidArgument](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO15invalidArgumentyA2CmF)

  `
  `  
  Malformed model name or Firebase app options.  

  #### Declaration

  Swift  

      case invalidArgument

- `
  ``
  ``
  `

  ### [emptyModelName](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO14emptyModelNameyA2CmF)

  `
  `  
  Model name is empty.  

  #### Declaration

  Swift  

      case emptyModelName

- `
  ``
  ``
  `

  ### [internalError(description:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError#/s:25FirebaseMLModelDownloader13DownloadErrorO08internalE0yACSS_tcACmF)

  `
  `  
  Other errors with description.  

  #### Declaration

  Swift  

      case internalError(description: String)