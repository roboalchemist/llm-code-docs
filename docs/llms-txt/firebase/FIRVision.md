# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision.md.txt

# FirebaseMLVision Framework Reference

# FIRVision


    @interface FIRVision : NSObject

A Firebase service that supports vision APIs.
- `
  ``
  ``
  `

  ### [statsCollectionEnabled](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(py)statsCollectionEnabled)

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

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isStatsCollectionEnabled) BOOL statsCollectionEnabled;

- `
  ``
  ``
  `

  ### [+vision](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(cm)vision)

  `
  `  
  Gets an instance of Firebase Vision service for the default Firebase app. The default Firebase
  app instance must be configured before calling this method; otherwise, raises FIRAppNotConfigured
  exception.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)vision;

  #### Return Value

  A Firebase Vision service instance, initialized with the default Firebase app.
- `
  ``
  ``
  `

  ### [+visionForApp:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(cm)visionForApp:)

  `
  `  
  Gets an instance of Firebase Vision service for the custom Firebase app.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)visionForApp:(nonnull FIRApp *)app;

  #### Parameters

  |-------------|--------------------------------------------------------------------------------------------------|
  | ` `*app*` ` | The custom Firebase app used for initialization. Raises FIRAppInvalid exception if `app` is nil. |

  #### Return Value

  A Firebase Vision service instance, initialized with the custom Firebase app.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)init)

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

  ### [-barcodeDetectorWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)barcodeDetectorWithOptions:)

  `
  `  
  Gets a barcode detector with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetector.html *)barcodeDetectorWithOptions:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetectorOptions.html *)options;

  #### Parameters

  |-----------------|----------------------------------------------------|
  | ` `*options*` ` | Options containing barcode detector configuration. |

  #### Return Value

  A barcode detector configured with the given options.
- `
  ``
  ``
  `

  ### [-barcodeDetector](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)barcodeDetector)

  `
  `  
  Gets a barcode detector with the default options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetector.html *)barcodeDetector;

  #### Return Value

  A barcode detector configured with the default options.
- `
  ``
  ``
  `

  ### [-faceDetectorWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)faceDetectorWithOptions:)

  `
  `  
  Gets a face detector with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetector.html *)faceDetectorWithOptions:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html *)options;

  #### Parameters

  |-----------------|--------------------------------------------|
  | ` `*options*` ` | Options for configuring the face detector. |

  #### Return Value

  A face detector configured with the given options.
- `
  ``
  ``
  `

  ### [-faceDetector](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)faceDetector)

  `
  `  
  Gets a face detector with the default options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetector.html *)faceDetector;

  #### Return Value

  A face detector configured with the default options.
- `
  ``
  ``
  `

  ### [-onDeviceImageLabelerWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)onDeviceImageLabelerWithOptions:)

  `
  `  
  Gets an on-device image labeler with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler.html *)onDeviceImageLabelerWithOptions:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionOnDeviceImageLabelerOptions.html *)options;

  #### Parameters

  |-----------------|--------------------------------------------|
  | ` `*options*` ` | Options for configuring the image labeler. |

  #### Return Value

  An on-device image labeler configured with the given options.
- `
  ``
  ``
  `

  ### [-onDeviceImageLabeler](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)onDeviceImageLabeler)

  `
  `  
  Gets an on-device image labeler with the default options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler.html *)onDeviceImageLabeler;

  #### Return Value

  An on-device image labeler configured with the default options.
- `
  ``
  ``
  `

  ### [-onDeviceTextRecognizer](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)onDeviceTextRecognizer)

  `
  `  
  Gets an on-device text recognizer.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer.html *)onDeviceTextRecognizer;

  #### Return Value

  A text recognizer.
- `
  ``
  ``
  `

  ### [-cloudTextRecognizerWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudTextRecognizerWithOptions:)

  `
  `  
  Gets a cloud text recognizer configured with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer.html *)cloudTextRecognizerWithOptions:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions.html *)options;

  #### Parameters

  |-----------------|----------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud text recognizer. |

  #### Return Value

  A text recognizer configured with the given options.
- `
  ``
  ``
  `

  ### [-cloudTextRecognizer](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudTextRecognizer)

  `
  `  
  Gets a cloud text recognizer.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer.html *)cloudTextRecognizer;

  #### Return Value

  A text recognizer.
- `
  ``
  ``
  `

  ### [-cloudDocumentTextRecognizerWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudDocumentTextRecognizerWithOptions:)

  `
  `  
  Gets a cloud document text recognizer configured with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextRecognizer.html *)
          cloudDocumentTextRecognizerWithOptions:
              (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDocumentTextRecognizerOptions.html *)options;

  #### Parameters

  |-----------------|-------------------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud document text recognizer. |

  #### Return Value

  A document text recognizer configured with the given options.
- `
  ``
  ``
  `

  ### [-cloudDocumentTextRecognizer](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudDocumentTextRecognizer)

  `
  `  
  Gets a cloud document text recognizer.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextRecognizer.html *)cloudDocumentTextRecognizer;

  #### Return Value

  A document text recognizer.
- `
  ``
  ``
  `

  ### [-cloudLandmarkDetectorWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudLandmarkDetectorWithOptions:)

  `
  `  
  Gets an instance of cloud landmark detector with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmarkDetector.html *)cloudLandmarkDetectorWithOptions:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDetectorOptions.html *)options;

  #### Parameters

  |-----------------|------------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud landmark detector. |

  #### Return Value

  A cloud landmark detector configured with the given options.
- `
  ``
  ``
  `

  ### [-cloudLandmarkDetector](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudLandmarkDetector)

  `
  `  
  Gets an instance of cloud landmark detector with default options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmarkDetector.html *)cloudLandmarkDetector;

  #### Return Value

  A cloud landmark detector configured with default options.
- `
  ``
  ``
  `

  ### [-cloudImageLabelerWithOptions:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudImageLabelerWithOptions:)

  `
  `  
  Gets an instance of cloud image labeler with the given options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler.html *)cloudImageLabelerWithOptions:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudImageLabelerOptions.html *)options;

  #### Parameters

  |-----------------|--------------------------------------------------|
  | ` `*options*` ` | Options for configuring the cloud image labeler. |

  #### Return Value

  A cloud image labeler configured with the given options.
- `
  ``
  ``
  `

  ### [-cloudImageLabeler](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision#/c:objc(cs)FIRVision(im)cloudImageLabeler)

  `
  `  
  Gets an instance of cloud image labeler with default options.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler.html *)cloudImageLabeler;

  #### Return Value

  A cloud image labeler configured with default options.