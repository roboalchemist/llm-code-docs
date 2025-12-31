# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode.md.txt

# FirebaseMLVision Framework Reference

# VisionBarcode

    class VisionBarcode : NSObject

A barcode in an image.
- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)frame)

  `
  `  
  The rectangle that holds the discovered relative to the detected image in the view
  coordinate system.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [rawValue](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)rawValue)

  `
  `  
  A barcode value as it was encoded in the barcode. Structured values are not parsed, for example:
  'MEBKM:TITLE:Google;URL:<https://www.google.com;;>'. Does not include the supplemental value.  

  #### Declaration

  Swift  

      var rawValue: String? { get }

- `
  ``
  ``
  `

  ### [rawData](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)rawData)

  `
  `  
  Raw data stored in barcode.  

  #### Declaration

  Swift  

      var rawData: Data? { get }

- `
  ``
  ``
  `

  ### [displayValue](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)displayValue)

  `
  `  
  A barcode value in a user-friendly format. May omit some of the information encoded in the
  barcode. For example, in the case above the display value might be '<https://www.google.com>'.
  If valueType == .text, this field will be equal to rawValue. This value may be multiline,
  for example, when line breaks are encoded into the original TEXT barcode value. May include
  the supplement value.  

  #### Declaration

  Swift  

      var displayValue: String? { get }

- `
  ``
  ``
  `

  ### [format](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)format)

  `
  `  
  A barcode format; for example, EAN_13. Note that if the format is not in the list,
  VisionBarcodeFormat.unknown would be returned.  

  #### Declaration

  Swift  

      var format: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeFormat.html { get }

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)cornerPoints)

  `
  `  
  The four corner points of the barcode, in clockwise order starting with the top left relative
  to the detected image in the view coordinate system. These are CGPoints boxed in NSValues.
  Due to the possible perspective distortions, this is not necessarily a rectangle.  

  #### Declaration

  Swift  

      var cornerPoints: [NSValue]? { get }

- `
  ``
  ``
  `

  ### [valueType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)valueType)

  `
  `  
  A type of the barcode value. For example, TEXT, PRODUCT, URL, etc. Note that if the type is not
  in the list, .unknown would be returned.  

  #### Declaration

  Swift  

      var valueType: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionBarcodeValueType.html { get }

- `
  ``
  ``
  `

  ### [email](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)email)

  `
  `  
  An email message from a 'MAILTO:' or similar QR Code type. This property is only set if
  valueType is .email.  

  #### Declaration

  Swift  

      var email: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeEmail.html? { get }

- `
  ``
  ``
  `

  ### [phone](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)phone)

  `
  `  
  A phone number from a 'TEL:' or similar QR Code type. This property is only set if valueType
  is .phone.  

  #### Declaration

  Swift  

      var phone: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodePhone.html? { get }

- `
  ``
  ``
  `

  ### [sms](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)sms)

  `
  `  
  An SMS message from an 'SMS:' or similar QR Code type. This property is only set if valueType
  is .sms.  

  #### Declaration

  Swift  

      var sms: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeSMS.html? { get }

- `
  ``
  ``
  `

  ### [url](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)URL)

  `
  `  
  A URL and title from a 'MEBKM:' or similar QR Code type. This property is only set if
  valueType is .url.  

  #### Declaration

  Swift  

      var url: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeURLBookmark.html? { get }

- `
  ``
  ``
  `

  ### [wifi](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)wifi)

  `
  `  
  Wi-Fi network parameters from a 'WIFI:' or similar QR Code type. This property is only set
  if valueType is .wifi.  

  #### Declaration

  Swift  

      var wifi: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeWifi.html? { get }

- `
  ``
  ``
  `

  ### [geoPoint](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)geoPoint)

  `
  `  
  GPS coordinates from a 'GEO:' or similar QR Code type. This property is only set if valueType
  is .geo.  

  #### Declaration

  Swift  

      var geoPoint: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeGeoPoint.html? { get }

- `
  ``
  ``
  `

  ### [contactInfo](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)contactInfo)

  `
  `  
  A person's or organization's business card. For example a VCARD. This property is only set
  if valueType is .contactInfo.  

  #### Declaration

  Swift  

      var contactInfo: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeContactInfo.html? { get }

- `
  ``
  ``
  `

  ### [calendarEvent](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)calendarEvent)

  `
  `  
  A calendar event extracted from a QR Code. This property is only set if valueType is
  .calendarEvent.  

  #### Declaration

  Swift  

      var calendarEvent: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeCalendarEvent.html? { get }

- `
  ``
  ``
  `

  ### [driverLicense](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(py)driverLicense)

  `
  `  
  A driver license or ID card. This property is only set if valueType is .driverLicense.  

  #### Declaration

  Swift  

      var driverLicense: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDriverLicense.html? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode#/c:objc(cs)FIRVisionBarcode(im)init)

  `
  `  
  Unavailable.