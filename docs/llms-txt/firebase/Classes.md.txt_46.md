# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes.md.txt

# FirebaseMLVision Framework Reference

# Classes

The following classes are available globally.
- `


  ### [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision)


  ` A Firebase service that supports vision APIs.

  #### Declaration

  Swift

      class Vision : NSObject

- `


  ### [VisionBarcodeAddress](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeAddress)


  ` An address.

  #### Declaration

  Swift

      class VisionBarcodeAddress : NSObject

- `


  ### [VisionBarcodeCalendarEvent](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeCalendarEvent)


  ` A calendar event extracted from a QR code.

  #### Declaration

  Swift

      class VisionBarcodeCalendarEvent : NSObject

- `


  ### [VisionBarcodeDriverLicense](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense)


  ` A driver license or ID card data representation.

  An ANSI driver license contains more fields than are represented by this class. The
  `FIRVisionBarcode`s `rawValue` property can be used to access the other fields.

  #### Declaration

  Swift

      class VisionBarcodeDriverLicense : NSObject

- `


  ### [VisionBarcodeEmail](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeEmail)


  ` An email message from a 'MAILTO:' or similar QR Code type.

  #### Declaration

  Swift

      class VisionBarcodeEmail : NSObject

- `


  ### [VisionBarcodeGeoPoint](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeGeoPoint)


  ` GPS coordinates from a 'GEO:' or similar QR Code type data.

  #### Declaration

  Swift

      class VisionBarcodeGeoPoint : NSObject

- `


  ### [VisionBarcodePersonName](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodePersonName)


  ` A person's name, both formatted and as individual name components.

  #### Declaration

  Swift

      class VisionBarcodePersonName : NSObject

- `


  ### [VisionBarcodePhone](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodePhone)


  ` A phone number from a 'TEL:' or similar QR Code type.

  #### Declaration

  Swift

      class VisionBarcodePhone : NSObject

- `


  ### [VisionBarcodeSMS](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeSMS)


  ` An SMS message from an 'SMS:' or similar QR Code type.

  #### Declaration

  Swift

      class VisionBarcodeSMS : NSObject

- `


  ### [VisionBarcodeURLBookmark](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeURLBookmark)


  ` A URL and title from a 'MEBKM:' or similar QR Code type.

  #### Declaration

  Swift

      class VisionBarcodeURLBookmark : NSObject

- `


  ### [VisionBarcodeWifi](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeWifi)


  ` Wi-Fi network parameters from a 'WIFI:' or similar QR Code type.

  #### Declaration

  Swift

      class VisionBarcodeWifi : NSObject

- `


  ### [VisionBarcodeContactInfo](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo)


  ` A person's or organization's business card. This may come from different underlying formats
  including VCARD and MECARD.

  This object represents a simplified view of possible business cards. If you require lossless
  access to the information in the barcode, you should parse the raw data yourself. To access the
  raw data, use the `FIRVisionBarcode`s `rawValue` property.

  #### Declaration

  Swift

      class VisionBarcodeContactInfo : NSObject

- `


  ### [VisionBarcode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode)


  ` A barcode in an image.

  #### Declaration

  Swift

      class VisionBarcode : NSObject

- `


  ### [VisionBarcodeDetector](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetector)


  ` A barcode detector that detects barcodes in an image.

  #### Declaration

  Swift

      class VisionBarcodeDetector : NSObject

- `


  ### [VisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetectorOptions)


  ` Options for specifying a Barcode detector.

  #### Declaration

  Swift

      class VisionBarcodeDetectorOptions : NSObject

- `


  ### [VisionCloudDetectorOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDetectorOptions)


  ` Generic options of a vision cloud detector.

  #### Declaration

  Swift

      class VisionCloudDetectorOptions : NSObject

- `


  ### [VisionCloudDocumentTextRecognizerOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDocumentTextRecognizerOptions)


  ` Options for a cloud document text recognizer.

  #### Declaration

  Swift

      class VisionCloudDocumentTextRecognizerOptions : NSObject

- `


  ### [VisionCloudImageLabelerOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudImageLabelerOptions)


  ` Options for a cloud image labeler.

  #### Declaration

  Swift

      class VisionCloudImageLabelerOptions : NSObject

- `


  ### [VisionCloudLandmark](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark)


  ` Set of landmark properties identified by a vision cloud detector.

  #### Declaration

  Swift

      class VisionCloudLandmark : NSObject

- `


  ### [VisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmarkDetector)


  ` A landmark detector that detects landmark in an image.

  #### Declaration

  Swift

      class VisionCloudLandmarkDetector : NSObject

- `


  ### [VisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions)


  ` Options for a cloud text recognizer.

  #### Declaration

  Swift

      class VisionCloudTextRecognizerOptions : NSObject

- `


  ### [VisionDocumentText](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentText)


  ` Recognized document text in an image.

  #### Declaration

  Swift

      class VisionDocumentText : NSObject

- `


  ### [VisionDocumentTextBlock](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock)


  ` A document text block recognized in an image that consists of an array of paragraphs.

  #### Declaration

  Swift

      class VisionDocumentTextBlock : NSObject

- `


  ### [VisionDocumentTextParagraph](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph)


  ` A document text paragraph recognized in an image that consists of an array of words.

  #### Declaration

  Swift

      class VisionDocumentTextParagraph : NSObject

- `


  ### [VisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextRecognizer)


  ` A cloud document text recognizer that recognizes text in an image.

  #### Declaration

  Swift

      class VisionDocumentTextRecognizer : NSObject

- `


  ### [VisionDocumentTextSymbol](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol)


  ` A document text symbol recognized in an image.

  #### Declaration

  Swift

      class VisionDocumentTextSymbol : NSObject

- `


  ### [VisionDocumentTextWord](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord)


  ` A document text word recognized in an image that consists of an array of symbols.

  #### Declaration

  Swift

      class VisionDocumentTextWord : NSObject

- `


  ### [VisionFace](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace)


  ` A human face detected in an image.

  #### Declaration

  Swift

      class VisionFace : NSObject

- `


  ### [VisionFaceContour](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceContour)


  ` A contour on a human face detected in an image.

  #### Declaration

  Swift

      class VisionFaceContour : NSObject

- `


  ### [VisionFaceDetector](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetector)


  ` A face detector that detects faces in an image.

  #### Declaration

  Swift

      class VisionFaceDetector : NSObject

- `


  ### [VisionFaceDetectorOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions)


  ` Options for specifying a face detector.

  #### Declaration

  Swift

      class VisionFaceDetectorOptions : NSObject

- `


  ### [VisionFaceLandmark](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceLandmark)


  ` A landmark on a human face detected in an image.

  #### Declaration

  Swift

      class VisionFaceLandmark : NSObject

- `


  ### [VisionImage](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage)


  ` An image or image buffer used in vision detection, with optional metadata.

  #### Declaration

  Swift

      class VisionImage : NSObject

- `


  ### [VisionImageLabel](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabel)


  ` Represents a label for an image.

  #### Declaration

  Swift

      class VisionImageLabel : NSObject

- `


  ### [VisionImageLabeler](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabeler)


  ` An on-device or cloud image labeler for labeling images.

  #### Declaration

  Swift

      class VisionImageLabeler : NSObject

- `


  ### [VisionImageMetadata](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageMetadata)


  ` Metadata of an image used in feature detection.

  #### Declaration

  Swift

      class VisionImageMetadata : NSObject

- `


  ### [VisionLatitudeLongitude](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionLatitudeLongitude)


  ` An object representing a latitude/longitude pair. This is expressed as a pair of doubles
  representing degrees latitude and degrees longitude. Unless specified otherwise, this must
  conform to the [WGS84
  standard](http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf). Values must be within normalized ranges.

  #### Declaration

  Swift

      class VisionLatitudeLongitude : NSObject

- `


  ### [VisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionOnDeviceImageLabelerOptions)


  ` Options for an on-device image labeler.

  #### Declaration

  Swift

      class VisionOnDeviceImageLabelerOptions : NSObject

- `


  ### [VisionPoint](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionPoint)


  ` A 2D or 3D point in the image. A valid point must have both x and y coordinates. The point's
  coordinates are in the same scale as the original image.

  #### Declaration

  Swift

      class VisionPoint : NSObject

- `


  ### [VisionText](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionText)


  ` Recognized text in an image.

  #### Declaration

  Swift

      class VisionText : NSObject

- `


  ### [VisionTextBlock](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock)


  ` A text block recognized in an image that consists of an array of text lines.

  #### Declaration

  Swift

      class VisionTextBlock : NSObject

- `


  ### [VisionTextElement](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement)


  ` A text element recognized in an image. A text element is roughly equivalent to a space-separated
  word in most Latin-script languages.

  #### Declaration

  Swift

      class VisionTextElement : NSObject

- `


  ### [VisionTextLine](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine)


  ` A text line recognized in an image that consists of an array of elements.

  #### Declaration

  Swift

      class VisionTextLine : NSObject

- `


  ### [VisionTextRecognizedBreak](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizedBreak)


  ` Detected break from text recognition.

  #### Declaration

  Swift

      class VisionTextRecognizedBreak : NSObject

- `


  ### [VisionTextRecognizedLanguage](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizedLanguage)


  ` Detected language from text recognition.

  #### Declaration

  Swift

      class VisionTextRecognizedLanguage : NSObject

- `


  ### [VisionTextRecognizer](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizer)


  ` An on-device or cloud text recognizer that recognizes text in an image.

  #### Declaration

  Swift

      class VisionTextRecognizer : NSObject