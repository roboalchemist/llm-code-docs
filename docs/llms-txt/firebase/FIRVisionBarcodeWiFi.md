# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeWiFi


    @interface FIRVisionBarcodeWiFi : NSObject

Wi-Fi network parameters from a 'WIFI:' or similar QR Code type.
- `
  ``
  ``
  `

  ### [ssid](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi#/c:objc(cs)FIRVisionBarcodeWiFi(py)ssid)

  `
  `  
  A Wi-Fi access point SSID.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *ssid;

- `
  ``
  ``
  `

  ### [password](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi#/c:objc(cs)FIRVisionBarcodeWiFi(py)password)

  `
  `  
  A Wi-Fi access point password.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *password;

- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi#/c:objc(cs)FIRVisionBarcodeWiFi(py)type)

  `
  `  
  A Wi-Fi access point encryption type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeWiFiEncryptionType.html type;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeWiFi#/c:objc(cs)FIRVisionBarcodeWiFi(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;