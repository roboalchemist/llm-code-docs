# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.md.txt

# FirebaseMLVision Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [VisionBarcodeDetectionCallback](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionBarcodeDetector.h@T@FIRVisionBarcodeDetectionCallback)


  ` A block containing an array of barcodes or `nil` if there's an error.

  #### Declaration

  Swift

      typealias VisionBarcodeDetectionCallback = ([FIRVisionBarcode]?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` barcodes ` | Array of barcodes detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [VisionCloudLandmarkDetectionCompletion](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionCloudLandmarkDetector.h@T@FIRVisionCloudLandmarkDetectionCompletion)


  ` A block containing an array of landmark or `nil` if there's an error.

  #### Declaration

  Swift

      typealias VisionCloudLandmarkDetectionCompletion = ([FIRVisionCloudLandmark]?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` landmarks ` | Array of landmark detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [VisionDocumentTextRecognitionCallback](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionDocumentTextRecognizer.h@T@FIRVisionDocumentTextRecognitionCallback)


  ` The callback to invoke when the document text recognition completes.

  #### Declaration

  Swift

      typealias VisionDocumentTextRecognitionCallback = (FIRVisionDocumentText?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` text ` | Recognized document text in the image or `nil` if there was an error or no text was detected. |
  | ` error ` | The error or `nil`. |

- `


  ### [FaceContourType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionFaceContour.h@T@FIRFaceContourType)


  ` Facial contour types.

  #### Declaration

  Swift

      struct FaceContourType : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [VisionFaceDetectionCallback](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionFaceDetector.h@T@FIRVisionFaceDetectionCallback)


  ` A block containing an array of faces or `nil` if there's an error.

  #### Declaration

  Swift

      typealias VisionFaceDetectionCallback = ([FIRVisionFace]?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` faces ` | Array of faces detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [FaceLandmarkType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionFaceLandmark.h@T@FIRFaceLandmarkType)


  ` Type of all facial landmarks.

  #### Declaration

  Swift

      struct FaceLandmarkType : _ObjectiveCBridgeable, Hashable, Equatable, _SwiftNewtypeWrapper, RawRepresentable

- `


  ### [VisionImageLabelerCallback](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionImageLabeler.h@T@FIRVisionImageLabelerCallback)


  ` A block containing an array of labels or `nil` if there's an error.

  #### Declaration

  Swift

      typealias VisionImageLabelerCallback = ([FIRVisionImageLabel]?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` labels ` | Array of labels detected in the image or `nil` if there was an error. |
  | ` error ` | The error or `nil`. |

- `


  ### [VisionTextRecognitionCallback](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions#/c:FIRVisionTextRecognizer.h@T@FIRVisionTextRecognitionCallback)


  ` The callback to invoke when the text recognition completes.

  #### Declaration

  Swift

      typealias VisionTextRecognitionCallback = (FIRVisionText?, Error?) -> Void

  #### Parameters

  |---|---|
  | ` text ` | Recognized text in the image or `nil` if there was an error or no text was detected. |
  | ` error ` | The error or `nil`. |