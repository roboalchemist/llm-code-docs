# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType.md.txt

# FirebaseMLModelDownloader Framework Reference

# ModelDownloadType

    public enum ModelDownloadType

Possible ways to get a custom model.
- `
  ``
  ``
  `

  ### [localModel](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType#/s:25FirebaseMLModelDownloader17ModelDownloadTypeO05localD0yA2CmF)

  `
  `  
  Get local model stored on device if available. If no local model on device, this is the same as [latestModel](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType.html#/s:25FirebaseMLModelDownloader17ModelDownloadTypeO06latestD0yA2CmF).  

  #### Declaration

  Swift  

      case localModel

- `
  ``
  ``
  `

  ### [localModelUpdateInBackground](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType#/s:25FirebaseMLModelDownloader17ModelDownloadTypeO05localD18UpdateInBackgroundyA2CmF)

  `
  `  
  Get local model on device if available and update to latest model from server in the background. If no local model on device, this is the same as [latestModel](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType.html#/s:25FirebaseMLModelDownloader17ModelDownloadTypeO06latestD0yA2CmF).  

  #### Declaration

  Swift  

      case localModelUpdateInBackground

- `
  ``
  ``
  `

  ### [latestModel](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType#/s:25FirebaseMLModelDownloader17ModelDownloadTypeO06latestD0yA2CmF)

  `
  `  
  Get latest model from server. Does not make a network call for model file download if local model matches the latest version on server.  

  #### Declaration

  Swift  

      case latestModel