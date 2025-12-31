# Source: https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager.md.txt

# FirebaseMLCommon Framework Reference

# FIRModelManager


    @interface FIRModelManager : NSObject

Manages models that are used by MLKit features.
- `
  ``
  ``
  `

  ### [+modelManager](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(cm)modelManager)

  `
  `  
  Returns the `ModelManager` instance for the default Firebase app. The default Firebase app
  instance must be configured before calling this method; otherwise, raises `FIRAppNotConfigured`
  exception.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)modelManager;

  #### Return Value

  The `ModelManager` instance for the default Firebase app.
- `
  ``
  ``
  `

  ### [+modelManagerForApp:](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(cm)modelManagerForApp:)

  `
  `  
  Returns the `ModelManager` instance for the given custom Firebase app. The custom Firebase app
  instance must be configured before calling this method; otherwise, raises `FIRAppNotConfigured`
  exception.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)modelManagerForApp:(nonnull FIRApp *)app;

  #### Parameters

  |-------------|-----------------------------------|
  | ` `*app*` ` | The custom Firebase app instance. |

  #### Return Value

  The `ModelManager` instance for the given custom Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(im)init)

  `
  `  
  Unavailable. Use the `modelManager()` or `modelManager(app:)` class methods.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-isModelDownloaded:](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(im)isModelDownloaded:)

  `
  `  
  Checks whether the given model has been downloaded.  

  #### Declaration

  Objective-C  

      - (BOOL)isModelDownloaded:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRRemoteModel.html *)remoteModel;

  #### Parameters

  |---------------------|---------------------------------------------|
  | ` `*remoteModel*` ` | The model to check the download status for. |

  #### Return Value

  Whether the given model has been downloaded.
- `
  ``
  ``
  `

  ### [-downloadModel:conditions:](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(im)downloadModel:conditions:)

  `
  `  
  Downloads the given model from the server to a local directory on the device. Use
  `isModelDownloaded(_:)` to check the download status for the model. If this method is invoked and
  the model has already been downloaded, a request is made to check if a newer version of the model
  is available for download. If available, the new version of the model is downloaded.

  To be notified when a model download request completes, observe the
  `.firebaseMLModelDownloadDidSucceed` (indicating model is ready to use) and
  `.firebaseMLModelDownloadDidFail` notifications defined in
  `FIRModelDownloadNotifications.h`. If the latest model is already downloaded, completes
  without additional work and posts a `.firebaseMLModelDownloadDidSucceed` notification,
  indicating that the model is ready to use.  

  #### Declaration

  Objective-C  

      - (nonnull NSProgress *)downloadModel:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRRemoteModel.html *)remoteModel
                                 conditions:
                                     (nonnull https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelDownloadConditions.html *)conditions;

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

  ### [-deleteDownloadedModel:completion:](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(im)deleteDownloadedModel:completion:)

  `
  `  
  Deletes the downloaded model from the device.  

  #### Declaration

  Objective-C  

      - (void)deleteDownloadedModel:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRRemoteModel.html *)remoteModel
                         completion:(nonnull void (^)(NSError *_Nullable))completion;

  #### Parameters

  |---------------------|-------------------------------------------------------------------------------------------------------------------------|
  | ` `*remoteModel*` ` | The downloaded model to delete.                                                                                         |
  | ` `*completion*` `  | Handler to call back on the main queue when the model deletion completed successfully or failed with the given `error`. |

- `
  ``
  ``
  `

  ### [-getLatestModelFilePath:completion:](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelManager#/c:objc(cs)FIRModelManager(im)getLatestModelFilePath:completion:)

  `
  `  
  Gets the absolute file path on the device for the last downloaded model. Please do not use this
  API if you intend to use this model through `ModelInterpreter`.  

  #### Declaration

  Objective-C  

      - (void)getLatestModelFilePath:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRRemoteModel.html *)remoteModel
                          completion:(nonnull void (^)(NSString *_Nullable,
                                                       NSError *_Nullable))completion;

  #### Parameters

  |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*remoteModel*` ` | The downloaded model.                                                                                                                                                                                                                     |
  | ` `*completion*` `  | Handler to call back returning the absolute file path of the downloaded model. This will return `nil` and will fail with the given `error` if the model is not yet downloaded on the device or valid custom remote model is not provided. |