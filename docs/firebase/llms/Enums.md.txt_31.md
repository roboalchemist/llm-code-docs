# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums.md.txt

# FirebaseMLVision Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [VisionBarcodeValueType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeValueType)


  ` @enum VisionBarcodeValueType
  Barcode's value format. For example, TEXT, PRODUCT, URL, etc.

  #### Declaration

  Swift

      enum VisionBarcodeValueType : Int

- `


  ### [VisionBarcodeAddressType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeAddressType)


  ` @enum VisionBarcodeAddressType
  Address type.

  #### Declaration

  Swift

      enum VisionBarcodeAddressType : Int

- `


  ### [VisionBarcodeEmailType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeEmailType)


  ` @enum VisionBarcodeEmailType
  Email type for VisionBarcodeEmail.

  #### Declaration

  Swift

      enum VisionBarcodeEmailType : Int

- `


  ### [VisionBarcodePhoneType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodePhoneType)


  ` @enum VisionBarcodePhoneType
  Phone type for VisionBarcodePhone.

  #### Declaration

  Swift

      enum VisionBarcodePhoneType : Int

- `


  ### [VisionBarcodeWiFiEncryptionType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeWiFiEncryptionType)


  ` @enum VisionBarcodeWiFiEncryptionType
  Wi-Fi encryption type for VisionBarcodeWiFi.

  #### Declaration

  Swift

      enum VisionBarcodeWiFiEncryptionType : Int

- `


  ### [VisionBarcodeFormat](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeFormat)


  ` @options VisionBarcodeFormat
  This option specifies the barcode formats that the library should detect.

  #### Declaration

  Swift

      struct VisionBarcodeFormat : OptionSet

- `


  ### [VisionCloudModelType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudModelType)


  ` @enum VisionCloudModelType
  Type of model to use in vision cloud detection API.

  #### Declaration

  Swift

      enum VisionCloudModelType : UInt

- `


  ### [VisionCloudTextModelType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudTextModelType)


  ` @enum VisionCloudTextModelType
  An enum of model types for cloud text recognition.

  #### Declaration

  Swift

      enum VisionCloudTextModelType : UInt

- `


  ### [VisionDocumentTextBlockType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDocumentTextBlockType)


  ` @enum VisionDocumentTextBlockType
  An enum of document text block types.

  #### Declaration

  Swift

      enum VisionDocumentTextBlockType : Int

- `


  ### [VisionFaceDetectorClassificationMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorClassificationMode)


  ` @enum VisionFaceDetectorClassificationMode
  Classification mode for face detection.

  #### Declaration

  Swift

      enum VisionFaceDetectorClassificationMode : UInt

- `


  ### [VisionFaceDetectorPerformanceMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorPerformanceMode)


  ` @enum VisionFaceDetectorPerformanceMode
  Performance preference for accuracy or speed of face detection.

  #### Declaration

  Swift

      enum VisionFaceDetectorPerformanceMode : UInt

- `


  ### [VisionFaceDetectorLandmarkMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorLandmarkMode)


  ` @enum VisionFaceDetectorLandmarkMode
  Landmark detection mode for face detection.

  #### Declaration

  Swift

      enum VisionFaceDetectorLandmarkMode : UInt

- `


  ### [VisionFaceDetectorContourMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorContourMode)


  ` @enum VisionFaceDetectorContourMode
  Contour detection mode for face detection.

  #### Declaration

  Swift

      enum VisionFaceDetectorContourMode : UInt

- `


  ### [VisionImageLabelerType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionImageLabelerType)


  ` @enum VisionImageLabelerType
  An enum of image labeler types.

  #### Declaration

  Swift

      enum VisionImageLabelerType : UInt

- `


  ### [VisionDetectorImageOrientation](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation)


  ` @enum VisionDetectorImageOrientation
  This enum specifies where the origin (0,0) of the image is located. The constant has the same
  value as defined by EXIF specifications.

  #### Declaration

  Swift

      enum VisionDetectorImageOrientation : UInt

- `


  ### [VisionTextRecognizedBreakType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionTextRecognizedBreakType)


  ` @enum VisionTextRecognizedBreakType
  An enum of recognized text break types.

  #### Declaration

  Swift

      enum VisionTextRecognizedBreakType : Int

- `


  ### [VisionTextRecognizerType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionTextRecognizerType)


  ` @enum VisionTextRecognizerType
  An enum of text recognizer types.

  #### Declaration

  Swift

      enum VisionTextRecognizerType : Int