# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.md.txt

# FirebaseMLVision Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRVisionBarcodeDetectionCallback](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionBarcodeDetector.h@T@FIRVisionBarcodeDetectionCallback)


  ` A block containing an array of barcodes or `nil` if there's an error.

  #### Declaration

  Objective-C

      typedef void (^FIRVisionBarcodeDetectionCallback)(
          NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode *> *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` barcodes ` | Array of barcodes detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [FIRVisionCloudLandmarkDetectionCompletion](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionCloudLandmarkDetector.h@T@FIRVisionCloudLandmarkDetectionCompletion)


  ` A block containing an array of landmark or `nil` if there's an error.

  #### Declaration

  Objective-C

      typedef void (^FIRVisionCloudLandmarkDetectionCompletion)(
          NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark *> *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` landmarks ` | Array of landmark detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [FIRVisionDocumentTextRecognitionCallback](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionDocumentTextRecognizer.h@T@FIRVisionDocumentTextRecognitionCallback)


  ` The callback to invoke when the document text recognition completes.

  #### Declaration

  Objective-C

      typedef void (^FIRVisionDocumentTextRecognitionCallback)(
          https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentText *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` text ` | Recognized document text in the image or `nil` if there was an error or no text was detected. |
  | ` error ` | The error or `nil`. |

- `


  ### [FIRFaceContourType](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionFaceContour.h@T@FIRFaceContourType)


  ` Facial contour types.

  #### Declaration

  Objective-C

      typedef NSString *FIRFaceContourType

- `


  ### [FIRVisionFaceDetectionCallback](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionFaceDetector.h@T@FIRVisionFaceDetectionCallback)


  ` A block containing an array of faces or `nil` if there's an error.

  #### Declaration

  Objective-C

      typedef void (^FIRVisionFaceDetectionCallback)(
          NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace *> *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` faces ` | Array of faces detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [FIRFaceLandmarkType](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionFaceLandmark.h@T@FIRFaceLandmarkType)


  ` Type of all facial landmarks.

  #### Declaration

  Objective-C

      typedef NSString *FIRFaceLandmarkType

- `


  ### [FIRVisionImageLabelerCallback](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionImageLabeler.h@T@FIRVisionImageLabelerCallback)


  ` A block containing an array of labels or `nil` if there's an error.

  #### Declaration

  Objective-C

      typedef void (^FIRVisionImageLabelerCallback)(
          NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel *> *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` labels ` | Array of labels detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [FIRVisionTextRecognitionCallback](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionTextRecognizer.h@T@FIRVisionTextRecognitionCallback)


  ` The callback to invoke when the text recognition completes.

  #### Declaration

  Objective-C

      typedef void (^FIRVisionTextRecognitionCallback)(https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionText *_Nullable,
                                                       NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` text ` | Recognized text in the image or `nil` if there was an error or no text was detected. |
  | ` error ` | The error or `nil`. |