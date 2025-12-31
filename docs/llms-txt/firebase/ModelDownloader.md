# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Classes/ModelDownloader.md.txt

# FirebaseMLModelDownloader Framework Reference

# ModelDownloader

    public class ModelDownloader

Downloader to manage custom model downloads.
- `
  ``
  ``
  `

  ### [modelDownloader()](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Classes/ModelDownloader#/s:25FirebaseMLModelDownloader05ModelC0C05modelC0ACyFZ)

  `
  `  
  Model downloader with default app.  

  #### Declaration

  Swift  

      public static func modelDownloader() -> ModelDownloader

- `
  ``
  ``
  `

  ### [modelDownloader(app:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Classes/ModelDownloader#/s:25FirebaseMLModelDownloader05ModelC0C05modelC03appACSo6FIRAppC_tFZ)

  `
  `  
  Model Downloader with custom app.  

  #### Declaration

  Swift  

      public static func modelDownloader(app: FirebaseApp) -> ModelDownloader

- `
  ``
  ``
  `

  ### [getModel(name:downloadType:conditions:progressHandler:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Classes/ModelDownloader#/s:25FirebaseMLModelDownloader05ModelC0C03getD04name12downloadType10conditions15progressHandler10completionySS_AA0d8DownloadH0OAA0dM10ConditionsVySfcSgys6ResultOyAA06CustomD0VAA0M5ErrorOGctF)

  `
  `  
  Downloads a custom model to device or gets a custom model already on device, with an optional handler for progress.  

  #### Declaration

  Swift  

      public func getModel(name modelName: String,
                           downloadType: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/ModelDownloadType.html,
                           conditions: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/ModelDownloadConditions.html,
                           progressHandler: ((Float) -> Void)? = nil,
                           completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel.html, https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError.html>) -> Void)

  #### Parameters

  |-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `       | The name of the model, matching Firebase console.                                                                                                                                                                                                                                                                                                 |
  | ` `*downloadType*` `    | ModelDownloadType used to get the model.                                                                                                                                                                                                                                                                                                          |
  | ` `*conditions*` `      | Conditions needed to perform a model download.                                                                                                                                                                                                                                                                                                    |
  | ` `*progressHandler*` ` | Optional. Returns a float in \[0.0, 1.0\] that can be used to monitor model download progress.                                                                                                                                                                                                                                                    |
  | ` `*completion*` `      | Returns either a [CustomModel](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel.html) on success, or a [DownloadError](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadError.html) on failure, at the end of a model download. |

- `
  ``
  ``
  `

  ### [listDownloadedModels(completion:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Classes/ModelDownloader#/s:25FirebaseMLModelDownloader05ModelC0C20listDownloadedModels10completionyys6ResultOyShyAA06CustomD0VGAA0fD5ErrorOGc_tF)

  `
  `  
  Gets the set of all downloaded models saved on device.  

  #### Declaration

  Swift  

      public func listDownloadedModels(completion: @escaping (Result<Set<https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel.html>,
        https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError.html>) -> Void)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | Returns either a set of [CustomModel](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel.html) models on success, or a [DownloadedModelError](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError.html) on failure. |

- `
  ``
  ``
  `

  ### [deleteDownloadedModel(name:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Classes/ModelDownloader#/s:25FirebaseMLModelDownloader05ModelC0C016deleteDownloadedD04name10completionySS_ys6ResultOyytAA0fD5ErrorOGctF)

  `
  `  
  Deletes a custom model file from device as well as corresponding model information saved in UserDefaults.  

  #### Declaration

  Swift  

      public func deleteDownloadedModel(name modelName: String,
                                        completion: @escaping (Result<Void, https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError.html>)
                                          -> Void)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `  | The name of the model, matching Firebase console and already downloaded to device.                                                                                     |
  | ` `*completion*` ` | Returns a [DownloadedModelError](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Enums/DownloadedModelError.html) on failure. |