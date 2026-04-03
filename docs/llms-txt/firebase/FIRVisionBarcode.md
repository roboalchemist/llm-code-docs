# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcode


    @interface FIRVisionBarcode : NSObject

A barcode in an image.
- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)frame)

  `
  `  
  The rectangle that holds the discovered relative to the detected image in the view
  coordinate system.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [rawValue](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)rawValue)

  `
  `  
  A barcode value as it was encoded in the barcode. Structured values are not parsed, for example:
  'MEBKM:TITLE:Google;URL:<https://www.google.com;;>'. Does not include the supplemental value.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *rawValue;

- `
  ``
  ``
  `

  ### [rawData](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)rawData)

  `
  `  
  Raw data stored in barcode.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSData *rawData;

- `
  ``
  ``
  `

  ### [displayValue](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)displayValue)

  `
  `  
  A barcode value in a user-friendly format. May omit some of the information encoded in the
  barcode. For example, in the case above the display value might be '<https://www.google.com>'.
  If valueType == .text, this field will be equal to rawValue. This value may be multiline,
  for example, when line breaks are encoded into the original TEXT barcode value. May include
  the supplement value.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *displayValue;

- `
  ``
  ``
  `

  ### [format](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)format)

  `
  `  
  A barcode format; for example, EAN_13. Note that if the format is not in the list,
  VisionBarcodeFormat.unknown would be returned.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeFormat.html format;

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)cornerPoints)

  `
  `  
  The four corner points of the barcode, in clockwise order starting with the top left relative
  to the detected image in the view coordinate system. These are CGPoints boxed in NSValues.
  Due to the possible perspective distortions, this is not necessarily a rectangle.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<NSValue *> *cornerPoints;

- `
  ``
  ``
  `

  ### [valueType](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)valueType)

  `
  `  
  A type of the barcode value. For example, TEXT, PRODUCT, URL, etc. Note that if the type is not
  in the list, .unknown would be returned.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeValueType.html valueType;

- `
  ``
  ``
  `

  ### [email](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)email)

  `
  `  
  An email message from a 'MAILTO:' or similar QR Code type. This property is only set if
  valueType is .email.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail.html *email;

- `
  ``
  ``
  `

  ### [phone](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)phone)

  `
  `  
  A phone number from a 'TEL:' or similar QR Code type. This property is only set if valueType
  is .phone.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePhone.html *phone;

- `
  ``
  ``
  `

  ### [sms](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)sms)

  `
  `  
  An SMS message from an 'SMS:' or similar QR Code type. This property is only set if valueType
  is .sms.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeSMS.html *sms;

- `
  ``
  ``
  `

  ### [URL](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)URL)

  `
  `  
  A URL and title from a 'MEBKM:' or similar QR Code type. This property is only set if
  valueType is .url.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeURLBookmark.html *URL;

- `
  ``
  ``
  `

  ### [wifi](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)wifi)

  `
  `  
  Wi-Fi network parameters from a 'WIFI:' or similar QR Code type. This property is only set
  if valueType is .wifi.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi.html *wifi;

- `
  ``
  ``
  `

  ### [geoPoint](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)geoPoint)

  `
  `  
  GPS coordinates from a 'GEO:' or similar QR Code type. This property is only set if valueType
  is .geo.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeGeoPoint.html *geoPoint;

- `
  ``
  ``
  `

  ### [contactInfo](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)contactInfo)

  `
  `  
  A person's or organization's business card. For example a VCARD. This property is only set
  if valueType is .contactInfo.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo.html *contactInfo;

- `
  ``
  ``
  `

  ### [calendarEvent](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)calendarEvent)

  `
  `  
  A calendar event extracted from a QR Code. This property is only set if valueType is
  .calendarEvent.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeCalendarEvent.html *calendarEvent;

- `
  ``
  ``
  `

  ### [driverLicense](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(py)driverLicense)

  `
  `  
  A driver license or ID card. This property is only set if valueType is .driverLicense.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense.html *driverLicense;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode#/c:objc(cs)FIRVisionBarcode(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;