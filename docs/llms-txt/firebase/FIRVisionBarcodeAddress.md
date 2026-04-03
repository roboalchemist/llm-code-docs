# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeAddress.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeAddress


    @interface FIRVisionBarcodeAddress : NSObject

An address.
- `
  ``
  ``
  `

  ### [addressLines](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeAddress#/c:objc(cs)FIRVisionBarcodeAddress(py)addressLines)

  `
  `  
  Formatted address, containing multiple lines when appropriate.

  The parsing of address formats is quite limited. Typically all address information will appear
  on the first address line. To handle addresses better, it is recommended to parse the raw data.
  The raw data is available in [FIRVisionBarcode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode.html)'s `rawValue` property.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<NSString *> *addressLines;

- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeAddress#/c:objc(cs)FIRVisionBarcodeAddress(py)type)

  `
  `  
  Address type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeAddressType.html type;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeAddress#/c:objc(cs)FIRVisionBarcodeAddress(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;