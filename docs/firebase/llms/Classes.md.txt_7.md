# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes.md.txt

# FirebaseMLVision Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRVision](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVision)


  ` A Firebase service that supports vision APIs.

  #### Declaration

  Objective-C


      @interface FIRVision : NSObject

- `


  ### [FIRVisionBarcodeAddress](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeAddress)


  ` An address.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeAddress : NSObject

- `


  ### [FIRVisionBarcodeCalendarEvent](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent)


  ` A calendar event extracted from a QR code.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeCalendarEvent : NSObject

- `


  ### [FIRVisionBarcodeDriverLicense](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense)


  ` A driver license or ID card data representation.

  An ANSI driver license contains more fields than are represented by this class. The
  `https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode`s `rawValue` property can be used to access the other fields.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeDriverLicense : NSObject

- `


  ### [FIRVisionBarcodeEmail](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail)


  ` An email message from a 'MAILTO:' or similar QR Code type.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeEmail : NSObject

- `


  ### [FIRVisionBarcodeGeoPoint](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeGeoPoint)


  ` GPS coordinates from a 'GEO:' or similar QR Code type data.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeGeoPoint : NSObject

- `


  ### [FIRVisionBarcodePersonName](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName)


  ` A person's name, both formatted and as individual name components.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodePersonName : NSObject

- `


  ### [FIRVisionBarcodePhone](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePhone)


  ` A phone number from a 'TEL:' or similar QR Code type.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodePhone : NSObject

- `


  ### [FIRVisionBarcodeSMS](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeSMS)


  ` An SMS message from an 'SMS:' or similar QR Code type.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeSMS : NSObject

- `


  ### [FIRVisionBarcodeURLBookmark](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeURLBookmark)


  ` A URL and title from a 'MEBKM:' or similar QR Code type.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeURLBookmark : NSObject

- `


  ### [FIRVisionBarcodeWiFi](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi)


  ` Wi-Fi network parameters from a 'WIFI:' or similar QR Code type.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeWiFi : NSObject

- `


  ### [FIRVisionBarcodeContactInfo](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo)


  ` A person's or organization's business card. This may come from different underlying formats
  including VCARD and MECARD.

  This object represents a simplified view of possible business cards. If you require lossless
  access to the information in the barcode, you should parse the raw data yourself. To access the
  raw data, use the `https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode`s `rawValue` property.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeContactInfo : NSObject

- `


  ### [FIRVisionBarcode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode)


  ` A barcode in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcode : NSObject

- `


  ### [FIRVisionBarcodeDetector](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetector)


  ` A barcode detector that detects barcodes in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeDetector : NSObject

- `


  ### [FIRVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetectorOptions)


  ` Options for specifying a Barcode detector.

  #### Declaration

  Objective-C


      @interface FIRVisionBarcodeDetectorOptions : NSObject

- `


  ### [FIRVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDetectorOptions)


  ` Generic options of a vision cloud detector.

  #### Declaration

  Objective-C


      @interface FIRVisionCloudDetectorOptions : NSObject

- `


  ### [FIRVisionCloudDocumentTextRecognizerOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDocumentTextRecognizerOptions)


  ` Options for a cloud document text recognizer.

  #### Declaration

  Objective-C


      @interface FIRVisionCloudDocumentTextRecognizerOptions : NSObject

- `


  ### [FIRVisionCloudImageLabelerOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudImageLabelerOptions)


  ` Options for a cloud image labeler.

  #### Declaration

  Objective-C


      @interface FIRVisionCloudImageLabelerOptions : NSObject

- `


  ### [FIRVisionCloudLandmark](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmark)


  ` Set of landmark properties identified by a vision cloud detector.

  #### Declaration

  Objective-C


      @interface FIRVisionCloudLandmark : NSObject

- `


  ### [FIRVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmarkDetector)


  ` A landmark detector that detects landmark in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionCloudLandmarkDetector : NSObject

- `


  ### [FIRVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions)


  ` Options for a cloud text recognizer.

  #### Declaration

  Objective-C


      @interface FIRVisionCloudTextRecognizerOptions : NSObject

- `


  ### [FIRVisionDocumentText](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentText)


  ` Recognized document text in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionDocumentText : NSObject

- `


  ### [FIRVisionDocumentTextBlock](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock)


  ` A document text block recognized in an image that consists of an array of paragraphs.

  #### Declaration

  Objective-C


      @interface FIRVisionDocumentTextBlock : NSObject

- `


  ### [FIRVisionDocumentTextParagraph](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph)


  ` A document text paragraph recognized in an image that consists of an array of words.

  #### Declaration

  Objective-C


      @interface FIRVisionDocumentTextParagraph : NSObject

- `


  ### [FIRVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextRecognizer)


  ` A cloud document text recognizer that recognizes text in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionDocumentTextRecognizer : NSObject

- `


  ### [FIRVisionDocumentTextSymbol](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol)


  ` A document text symbol recognized in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionDocumentTextSymbol : NSObject

- `


  ### [FIRVisionDocumentTextWord](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord)


  ` A document text word recognized in an image that consists of an array of symbols.

  #### Declaration

  Objective-C


      @interface FIRVisionDocumentTextWord : NSObject

- `


  ### [FIRVisionFace](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace)


  ` A human face detected in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionFace : NSObject

- `


  ### [FIRVisionFaceContour](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceContour)


  ` A contour on a human face detected in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionFaceContour : NSObject

- `


  ### [FIRVisionFaceDetector](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetector)


  ` A face detector that detects faces in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionFaceDetector : NSObject

- `


  ### [FIRVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions)


  ` Options for specifying a face detector.

  #### Declaration

  Objective-C


      @interface FIRVisionFaceDetectorOptions : NSObject

- `


  ### [FIRVisionFaceLandmark](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceLandmark)


  ` A landmark on a human face detected in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionFaceLandmark : NSObject

- `


  ### [FIRVisionImage](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage)


  ` An image or image buffer used in vision detection, with optional metadata.

  #### Declaration

  Objective-C


      @interface FIRVisionImage : NSObject

- `


  ### [FIRVisionImageLabel](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabel)


  ` Represents a label for an image.

  #### Declaration

  Objective-C


      @interface FIRVisionImageLabel : NSObject

- `


  ### [FIRVisionImageLabeler](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler)


  ` An on-device or cloud image labeler for labeling images.

  #### Declaration

  Objective-C


      @interface FIRVisionImageLabeler : NSObject

- `


  ### [FIRVisionImageMetadata](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageMetadata)


  ` Metadata of an image used in feature detection.

  #### Declaration

  Objective-C


      @interface FIRVisionImageMetadata : NSObject

- `


  ### [FIRVisionLatitudeLongitude](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionLatitudeLongitude)


  ` An object representing a latitude/longitude pair. This is expressed as a pair of doubles
  representing degrees latitude and degrees longitude. Unless specified otherwise, this must
  conform to the [WGS84
  standard](http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf). Values must be within normalized ranges.

  #### Declaration

  Objective-C


      @interface FIRVisionLatitudeLongitude : NSObject

- `


  ### [FIRVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionOnDeviceImageLabelerOptions)


  ` Options for an on-device image labeler.

  #### Declaration

  Objective-C


      @interface FIRVisionOnDeviceImageLabelerOptions : NSObject

- `


  ### [FIRVisionPoint](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint)


  ` A 2D or 3D point in the image. A valid point must have both x and y coordinates. The point's
  coordinates are in the same scale as the original image.

  #### Declaration

  Objective-C


      @interface FIRVisionPoint : NSObject

- `


  ### [FIRVisionText](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionText)


  ` Recognized text in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionText : NSObject

- `


  ### [FIRVisionTextBlock](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock)


  ` A text block recognized in an image that consists of an array of text lines.

  #### Declaration

  Objective-C


      @interface FIRVisionTextBlock : NSObject

- `


  ### [FIRVisionTextElement](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement)


  ` A text element recognized in an image. A text element is roughly equivalent to a space-separated
  word in most Latin-script languages.

  #### Declaration

  Objective-C


      @interface FIRVisionTextElement : NSObject

- `


  ### [FIRVisionTextLine](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine)


  ` A text line recognized in an image that consists of an array of elements.

  #### Declaration

  Objective-C


      @interface FIRVisionTextLine : NSObject

- `


  ### [FIRVisionTextRecognizedBreak](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak)


  ` Detected break from text recognition.

  #### Declaration

  Objective-C


      @interface FIRVisionTextRecognizedBreak : NSObject

- `


  ### [FIRVisionTextRecognizedLanguage](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage)


  ` Detected language from text recognition.

  #### Declaration

  Objective-C


      @interface FIRVisionTextRecognizedLanguage : NSObject

- `


  ### [FIRVisionTextRecognizer](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer)


  ` An on-device or cloud text recognizer that recognizes text in an image.

  #### Declaration

  Objective-C


      @interface FIRVisionTextRecognizer : NSObject