# Source: https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter.md.txt

# FirebaseMLModelInterpreter Framework Reference

# FIRModelInterpreter


    @interface FIRModelInterpreter : NSObject

A Firebase interpreter for a custom model.
- `
  ``
  ``
  `

  ### [statsCollectionEnabled](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(py)statsCollectionEnabled)

  `
  `  
  Enables stats collection in ML Kit model interpreter. The stats include API call counts, errors,
  API call durations, options, etc. No personally identifiable information is logged.

  <br />

  The setting is per `FirebaseApp`, and therefore per `ModelInterpreter`, and it is persistent
  across launches of the app. It means if the user uninstalls the app or clears all app data, the
  setting will be erased. The best practice is to set the flag in each initialization.

  <br />

  By default the logging is enabled. You have to specifically set it to false to disable
  logging.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isStatsCollectionEnabled) BOOL statsCollectionEnabled;

- `
  ``
  ``
  `

  ### [+modelInterpreterForLocalModel:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(cm)modelInterpreterForLocalModel:)

  `
  `  
  Gets an instance of a custom model interpreter for the given `localModel` and the default
  Firebase app. The default Firebase app instance must be configured before calling this method;
  otherwise, raises `FIRAppNotConfigured` exception. The returned interpreter is thread safe.
  Custom models hosted in non-default Firebase apps are currently not supported.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)modelInterpreterForLocalModel:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomLocalModel.html *)localModel;

  #### Parameters

  |--------------------|---------------------|
  | ` `*localModel*` ` | Custom local model. |

  #### Return Value

  A custom model interpreter with the given options and the default Firebase app.
- `
  ``
  ``
  `

  ### [+modelInterpreterForRemoteModel:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(cm)modelInterpreterForRemoteModel:)

  `
  `  
  Gets an instance of a custom model interpreter for the given `remoteModel` and the default
  Firebase app. The default Firebase app instance must be configured before calling this method;
  otherwise, raises `FIRAppNotConfigured` exception. The returned interpreter is thread safe.
  Custom models hosted in non-default Firebase apps are currently not supported.

  It is recommended that the `CustomRemoteModel` be downloaded before creating a new
  instance of `ModelInterpreter`. To download the remote model, invoke the `ModelManager`'s
  `download(_:conditions:)` method and monitor the returned `Progress` and/or listen for the
  download notifications defined in `FIRModelDownloadNotifications.h`.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)modelInterpreterForRemoteModel:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomRemoteModel.html *)remoteModel;

  #### Parameters

  |---------------------|----------------------|
  | ` `*remoteModel*` ` | Custom remote model. |

  #### Return Value

  A custom model interpreter with the given options and the default Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-runWithInputs:options:completion:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)runWithInputs:options:completion:)

  `
  `  
  Runs model inference with the given inputs and data options asynchronously. Inputs and data
  options should remain unchanged until the model inference completes.  

  #### Declaration

  Objective-C  

      - (void)runWithInputs:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInputs.html *)inputs
                    options:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInputOutputOptions.html *)options
                 completion:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Type-Definitions.html#/c:FIRModelInterpreter.h@T@FIRModelInterpreterRunCallback)completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------|
  | ` `*inputs*` `     | Inputs for custom model inference.                                                        |
  | ` `*options*` `    | Data options for the custom model specifiying input and output data types and dimensions. |
  | ` `*completion*` ` | Handler to call back on the main thread with `ModelOutputs` or error.                     |

- `
  ``
  ``
  `

  ### [-inputIndexForOp:completion:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)inputIndexForOp:completion:)

  `
  `  
  Gets the index of an input op with the given name.  

  #### Declaration

  Objective-C  

      - (void)inputIndexForOp:(nonnull NSString *)opName
                   completion:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Type-Definitions.html#/c:FIRModelInterpreter.h@T@FIRModelInterpreterInputOutputOpIndexCallback)
                                  completion;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------|
  | ` `*opName*` `     | The name of the input op.                                                                      |
  | ` `*completion*` ` | Handler to call back on the main thread with input op index as an `unsignedIntValue` or error. |

- `
  ``
  ``
  `

  ### [-outputIndexForOp:completion:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)outputIndexForOp:completion:)

  `
  `  
  Gets the index of an output op with the given name.  

  #### Declaration

  Objective-C  

      - (void)outputIndexForOp:(nonnull NSString *)opName
                    completion:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Type-Definitions.html#/c:FIRModelInterpreter.h@T@FIRModelInterpreterInputOutputOpIndexCallback)
                                   completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------|
  | ` `*opName*` `     | The name of the output op.                                                                      |
  | ` `*completion*` ` | Handler to call back on the main thread with output op index as an `unsignedIntValue` or error. |