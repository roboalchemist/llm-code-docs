# Source: https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager.md.txt

# FirebaseMLCommon Framework Reference

# ModelManager

    class ModelManager : NSObject

Manages models that are used by MLKit features.
- `
  ``
  ``
  `

  ### [modelManager()](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(cm)modelManager)

  `
  `  
  Returns the `ModelManager` instance for the default Firebase app. The default Firebase app
  instance must be configured before calling this method; otherwise, raises `FIRAppNotConfigured`
  exception.  

  #### Declaration

  Swift  

      class func modelManager() -> Self

  #### Return Value

  The `ModelManager` instance for the default Firebase app.
- `
  ``
  ``
  `

  ### [modelManager(app:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(cm)modelManagerForApp:)

  `
  `  
  Returns the `ModelManager` instance for the given custom Firebase app. The custom Firebase app
  instance must be configured before calling this method; otherwise, raises `FIRAppNotConfigured`
  exception.  

  #### Declaration

  Swift  

      class func modelManager(app: FIRApp) -> Self

  #### Parameters

  |-------------|-----------------------------------|
  | ` `*app*` ` | The custom Firebase app instance. |

  #### Return Value

  The `ModelManager` instance for the given custom Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(im)init)

  `
  `  
  Unavailable. Use the [modelManager()](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager.html#/c:objc(cs)FIRModelManager(cm)modelManager) or [modelManager(app:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager.html#/c:objc(cs)FIRModelManager(cm)modelManagerForApp:) class methods.
- `
  ``
  ``
  `

  ### [isModelDownloaded(_:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(im)isModelDownloaded:)

  `
  `  
  Checks whether the given model has been downloaded.  

  #### Declaration

  Swift  

      func isModelDownloaded(_ remoteModel: FIRRemoteModel) -> Bool

  #### Parameters

  |---------------------|---------------------------------------------|
  | ` `*remoteModel*` ` | The model to check the download status for. |

  #### Return Value

  Whether the given model has been downloaded.
- `
  ``
  ``
  `

  ### [download(_:conditions:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(im)downloadModel:conditions:)

  `
  `  
  Downloads the given model from the server to a local directory on the device. Use
  [isModelDownloaded(_:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager.html#/c:objc(cs)FIRModelManager(im)isModelDownloaded:) to check the download status for the model. If this method is invoked and
  the model has already been downloaded, a request is made to check if a newer version of the model
  is available for download. If available, the new version of the model is downloaded.

  To be notified when a model download request completes, observe the
  [.firebaseMLModelDownloadDidSucceed](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants.html#/c:@FIRModelDownloadDidSucceedNotification) (indicating model is ready to use) and
  [.firebaseMLModelDownloadDidFail](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants.html#/c:@FIRModelDownloadDidFailNotification) notifications defined in
  `FIRModelDownloadNotifications.h`. If the latest model is already downloaded, completes
  without additional work and posts a [.firebaseMLModelDownloadDidSucceed](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants.html#/c:@FIRModelDownloadDidSucceedNotification) notification,
  indicating that the model is ready to use.  

  #### Declaration

  Swift  

      func download(_ remoteModel: FIRRemoteModel, conditions: FIRModelDownloadConditions) -> Progress

  #### Parameters

  |---------------------|-------------------------------------------|
  | ` `*remoteModel*` ` | The model to download.                    |
  | ` `*conditions*` `  | The conditions for downloading the model. |

  #### Return Value

  Progress for downloading the model.
- `
  ``
  ``
  `

  ### [deleteDownloadedModel(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(im)deleteDownloadedModel:completion:)

  `
  `  
  Deletes the downloaded model from the device.  

  #### Declaration

  Swift  

      func deleteDownloadedModel(_ remoteModel: FIRRemoteModel, completion: @escaping (Error?) -> Void)

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*remoteModel*` ` | The downloaded model to delete.                                                                                                                                                                                                                              |
  | ` `*completion*` `  | Handler to call back on the main queue when the model deletion completed successfully or failed with the given [error](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants.html#/c:@FIRModelDownloadUserInfoKeyError). |

- `
  ``
  ``
  `

  ### [getLatestModelFilePath(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelManager#/c:objc(cs)FIRModelManager(im)getLatestModelFilePath:completion:)

  `
  `  
  Gets the absolute file path on the device for the last downloaded model. Please do not use this
  API if you intend to use this model through `ModelInterpreter`.  

  #### Declaration

  Swift  

      func getLatestModelFilePath(_ remoteModel: FIRRemoteModel, completion: @escaping (String?, Error?) -> Void)

  #### Parameters

  |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*remoteModel*` ` | The downloaded model.                                                                                                                                                                                                                                                                                                                                                          |
  | ` `*completion*` `  | Handler to call back returning the absolute file path of the downloaded model. This will return `nil` and will fail with the given [error](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants.html#/c:@FIRModelDownloadUserInfoKeyError) if the model is not yet downloaded on the device or valid custom remote model is not provided. |