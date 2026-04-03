# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError.md.txt

# FirebaseMLModelDownloader Framework Reference

# DownloadedModelError

    public enum DownloadedModelError : Error

Possible errors with locating a model file on device.
- `
  ``
  ``
  `

  ### [notFound](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError#/s:25FirebaseMLModelDownloader20DownloadedModelErrorO8notFoundyA2CmF)

  `
  `  
  No model with this name exists on device.  

  #### Declaration

  Swift  

      case notFound

- `
  ``
  ``
  `

  ### [fileIOError(description:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError#/s:25FirebaseMLModelDownloader20DownloadedModelErrorO11fileIOErroryACSS_tcACmF)

  `
  `  
  File system error.  

  #### Declaration

  Swift  

      case fileIOError(description: String)

- `
  ``
  ``
  `

  ### [internalError(description:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError#/s:25FirebaseMLModelDownloader20DownloadedModelErrorO08internalF0yACSS_tcACmF)

  `
  `  
  Other errors with description.  

  #### Declaration

  Swift  

      case internalError(description: String)