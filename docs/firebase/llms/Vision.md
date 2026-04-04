# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.md.txt

# FirebaseMLVision Framework Reference

# Vision

    class Vision : NSObject

A Firebase service that supports vision APIs.
- `
  ``
  ``
  `

  ### [isStatsCollectionEnabled](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(py)statsCollectionEnabled)

  `
  `  
  Enables stats collection in ML Kit vision. The stats include API call counts, errors, API call
  durations, options, etc. No personally identifiable information is logged.

  <br />

  The setting is per `FirebaseApp`, and therefore per `Vision`, and it is persistent across
  launches of the app. It means if the user uninstalls the app or clears all app data, the setting
  will be erased. The best practice is to set the flag in each initialization.

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

  ### [vision()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(cm)vision)

  `
  `  
  Gets an instance of Firebase Vision service for the default Firebase app. The default Firebase
  app instance must be configured before calling this method; otherwise, raises FIRAppNotConfigured
  exception.  

  #### Declaration

  Swift  

      class func vision() -> Self

  #### Return Value

  A Firebase Vision service instance, initialized with the default Firebase app.
- `
  ``
  ``
  `

  ### [vision(app:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(cm)visionForApp:)

  `
  `  
  Gets an instance of Firebase Vision service for the custom Firebase app.  

  #### Declaration

  Swift  

      class func vision(app: FIRApp) -> Self

  #### Parameters

  |-------------|--------------------------------------------------------------------------------------------------|
  | ` `*app*` ` | The custom Firebase app used for initialization. Raises FIRAppInvalid exception if `app` is nil. |

  #### Return Value

  A Firebase Vision service instance, initialized with the custom Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [barcodeDetector(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)barcodeDetectorWithOptions:)

  `
  `  
  Gets a barcode detector with the given options.  

  #### Declaration

  Swift  

      func barcodeDetector(options: FIRVisionBarcodeDetectorOptions) -> FIRVisionBarcodeDetector

  #### Parameters

  |-----------------|----------------------------------------------------|
  | ` `*options*` ` | Options containing barcode detector configuration. |

  #### Return Value

  A barcode detector configured with the given options.
- `
  ``
  ``
  `

  ### [barcodeDetector()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)barcodeDetector)

  `
  `  
  Gets a barcode detector with the default options.  

  #### Declaration

  Swift  

      func barcodeDetector() -> FIRVisionBarcodeDetector

  #### Return Value

  A barcode detector configured with the default options.
- `
  ``
  ``
  `

  ### [faceDetector(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)faceDetectorWithOptions:)

  `
  `  
  Gets a face detector with the given options.  

  #### Declaration

  Swift  

      func faceDetector(options: FIRVisionFaceDetectorOptions) -> FIRVisionFaceDetector

  #### Parameters

  |-----------------|--------------------------------------------|
  | ` `*options*` ` | Options for configuring the face detector. |

  #### Return Value

  A face detector configured with the given options.
- `
  ``
  ``
  `

  ### [faceDetector()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)faceDetector)

  `
  `  
  Gets a face detector with the default options.  

  #### Declaration

  Swift  

      func faceDetector() -> FIRVisionFaceDetector

  #### Return Value

  A face detector configured with the default options.
- `
  ``
  ``
  `

  ### [onDeviceImageLabeler(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)onDeviceImageLabelerWithOptions:)

  `
  `  
  Gets an on-device image labeler with the given options.  

  #### Declaration

  Swift  

      func onDeviceImageLabeler(options: FIRVisionOnDeviceImageLabelerOptions) -> FIRVisionImageLabeler

  #### Parameters

  |-----------------|--------------------------------------------|
  | ` `*options*` ` | Options for configuring the image labeler. |

  #### Return Value

  An on-device image labeler configured with the given options.
- `
  ``
  ``
  `

  ### [onDeviceImageLabeler()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)onDeviceImageLabeler)

  `
  `  
  Gets an on-device image labeler with the default options.  

  #### Declaration

  Swift  

      func onDeviceImageLabeler() -> FIRVisionImageLabeler

  #### Return Value

  An on-device image labeler configured with the default options.
- `
  ``
  ``
  `

  ### [onDeviceTextRecognizer()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)onDeviceTextRecognizer)

  `
  `  
  Gets an on-device text recognizer.  

  #### Declaration

  Swift  

      func onDeviceTextRecognizer() -> FIRVisionTextRecognizer

  #### Return Value

  A text recognizer.
- `
  ``
  ``
  `

  ### [cloudTextRecognizer(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudTextRecognizerWithOptions:)

  `
  `  
  Gets a cloud text recognizer configured with the given options.  

  #### Declaration

  Swift  

      func cloudTextRecognizer(options: FIRVisionCloudTextRecognizerOptions) -> FIRVisionTextRecognizer

  #### Parameters

  |-----------------|----------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud text recognizer. |

  #### Return Value

  A text recognizer configured with the given options.
- `
  ``
  ``
  `

  ### [cloudTextRecognizer()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudTextRecognizer)

  `
  `  
  Gets a cloud text recognizer.  

  #### Declaration

  Swift  

      func cloudTextRecognizer() -> FIRVisionTextRecognizer

  #### Return Value

  A text recognizer.
- `
  ``
  ``
  `

  ### [cloudDocumentTextRecognizer(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudDocumentTextRecognizerWithOptions:)

  `
  `  
  Gets a cloud document text recognizer configured with the given options.  

  #### Declaration

  Swift  

      func cloudDocumentTextRecognizer(options: FIRVisionCloudDocumentTextRecognizerOptions) -> FIRVisionDocumentTextRecognizer

  #### Parameters

  |-----------------|-------------------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud document text recognizer. |

  #### Return Value

  A document text recognizer configured with the given options.
- `
  ``
  ``
  `

  ### [cloudDocumentTextRecognizer()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudDocumentTextRecognizer)

  `
  `  
  Gets a cloud document text recognizer.  

  #### Declaration

  Swift  

      func cloudDocumentTextRecognizer() -> FIRVisionDocumentTextRecognizer

  #### Return Value

  A document text recognizer.
- `
  ``
  ``
  `

  ### [cloudLandmarkDetector(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudLandmarkDetectorWithOptions:)

  `
  `  
  Gets an instance of cloud landmark detector with the given options.  

  #### Declaration

  Swift  

      func cloudLandmarkDetector(options: FIRVisionCloudDetectorOptions) -> FIRVisionCloudLandmarkDetector

  #### Parameters

  |-----------------|------------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud landmark detector. |

  #### Return Value

  A cloud landmark detector configured with the given options.
- `
  ``
  ``
  `

  ### [cloudLandmarkDetector()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudLandmarkDetector)

  `
  `  
  Gets an instance of cloud landmark detector with default options.  

  #### Declaration

  Swift  

      func cloudLandmarkDetector() -> FIRVisionCloudLandmarkDetector

  #### Return Value

  A cloud landmark detector configured with default options.
- `
  ``
  ``
  `

  ### [cloudImageLabeler(options:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudImageLabelerWithOptions:)

  `
  `  
  Gets an instance of cloud image labeler with the given options.  

  #### Declaration

  Swift  

      func cloudImageLabeler(options: FIRVisionCloudImageLabelerOptions) -> FIRVisionImageLabeler

  #### Parameters

  |-----------------|--------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud image labeler. |

  #### Return Value

  A cloud image labeler configured with the given options.
- `
  ``
  ``
  `

  ### [cloudImageLabeler()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision#/c:objc(cs)FIRVision(im)cloudImageLabeler)

  `
  `  
  Gets an instance of cloud image labeler with default options.  

  #### Declaration

  Swift  

      func cloudImageLabeler() -> FIRVisionImageLabeler

  #### Return Value

  A cloud image labeler configured with default options.