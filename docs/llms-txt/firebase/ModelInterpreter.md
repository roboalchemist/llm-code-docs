# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter.md.txt

# FirebaseMLModelInterpreter Framework Reference

# ModelInterpreter

    class ModelInterpreter : NSObject

A Firebase interpreter for a custom model.
- `
  ``
  ``
  `

  ### [isStatsCollectionEnabled](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(py)statsCollectionEnabled)

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

  Swift  

      var isStatsCollectionEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [modelInterpreter(localModel:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(cm)modelInterpreterForLocalModel:)

  `
  `  
  Gets an instance of a custom model interpreter for the given `localModel` and the default
  Firebase app. The default Firebase app instance must be configured before calling this method;
  otherwise, raises `FIRAppNotConfigured` exception. The returned interpreter is thread safe.
  Custom models hosted in non-default Firebase apps are currently not supported.  

  #### Declaration

  Swift  

      class func modelInterpreter(localModel: FIRCustomLocalModel) -> Self

  #### Parameters

  |--------------------|---------------------|
  | ` `*localModel*` ` | Custom local model. |

  #### Return Value

  A custom model interpreter with the given options and the default Firebase app.
- `
  ``
  ``
  `

  ### [modelInterpreter(remoteModel:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(cm)modelInterpreterForRemoteModel:)

  `
  `  
  Gets an instance of a custom model interpreter for the given `remoteModel` and the default
  Firebase app. The default Firebase app instance must be configured before calling this method;
  otherwise, raises `FIRAppNotConfigured` exception. The returned interpreter is thread safe.
  Custom models hosted in non-default Firebase apps are currently not supported.

  It is recommended that the [CustomRemoteModel](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/CustomRemoteModel.html) be downloaded before creating a new
  instance of `ModelInterpreter`. To download the remote model, invoke the `ModelManager`'s
  `download(_:conditions:)` method and monitor the returned `Progress` and/or listen for the
  download notifications defined in `FIRModelDownloadNotifications.h`.  

  #### Declaration

  Swift  

      class func modelInterpreter(remoteModel: FIRCustomRemoteModel) -> Self

  #### Parameters

  |---------------------|----------------------|
  | ` `*remoteModel*` ` | Custom remote model. |

  #### Return Value

  A custom model interpreter with the given options and the default Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [run(inputs:options:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)runWithInputs:options:completion:)

  `
  `  
  Runs model inference with the given inputs and data options asynchronously. Inputs and data
  options should remain unchanged until the model inference completes.  

  #### Declaration

  Swift  

      func run(inputs: FIRModelInputs, options: FIRModelInputOutputOptions, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Type-Definitions.html#/c:FIRModelInterpreter.h@T@FIRModelInterpreterRunCallback)

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*inputs*` `     | Inputs for custom model inference.                                                                                                                                                         |
  | ` `*options*` `    | Data options for the custom model specifiying input and output data types and dimensions.                                                                                                  |
  | ` `*completion*` ` | Handler to call back on the main thread with [ModelOutputs](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelOutputs.html) or error. |

- `
  ``
  ``
  `

  ### [inputIndex(opName:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)inputIndexForOp:completion:)

  `
  `  
  Gets the index of an input op with the given name.  

  #### Declaration

  Swift  

      func inputIndex(opName: String, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Type-Definitions.html#/c:FIRModelInterpreter.h@T@FIRModelInterpreterInputOutputOpIndexCallback)

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------|
  | ` `*opName*` `     | The name of the input op.                                                                      |
  | ` `*completion*` ` | Handler to call back on the main thread with input op index as an `unsignedIntValue` or error. |

- `
  ``
  ``
  `

  ### [outputIndex(opName:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter#/c:objc(cs)FIRModelInterpreter(im)outputIndexForOp:completion:)

  `
  `  
  Gets the index of an output op with the given name.  

  #### Declaration

  Swift  

      func outputIndex(opName: String, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Type-Definitions.html#/c:FIRModelInterpreter.h@T@FIRModelInterpreterInputOutputOpIndexCallback)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------|
  | ` `*opName*` `     | The name of the output op.                                                                      |
  | ` `*completion*` ` | Handler to call back on the main thread with output op index as an `unsignedIntValue` or error. |