# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeContactInfo


    @interface FIRVisionBarcodeContactInfo : NSObject

A person's or organization's business card. This may come from different underlying formats
including VCARD and MECARD.

This object represents a simplified view of possible business cards. If you require lossless
access to the information in the barcode, you should parse the raw data yourself. To access the
raw data, use the [FIRVisionBarcode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode.html)s `rawValue` property.
- `
  ``
  ``
  `

  ### [addresses](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)addresses)

  `
  `  
  Person's or organization's addresses.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeAddress.html *> *addresses;

- `
  ``
  ``
  `

  ### [emails](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)emails)

  `
  `  
  Contact emails.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail.html *> *emails;

- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)name)

  `
  `  
  A person's name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName.html *name;

- `
  ``
  ``
  `

  ### [phones](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)phones)

  `
  `  
  Contact phone numbers.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePhone.html *> *phones;

- `
  ``
  ``
  `

  ### [urls](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)urls)

  `
  `  
  Contact URLs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<NSString *> *urls;

- `
  ``
  ``
  `

  ### [jobTitle](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)jobTitle)

  `
  `  
  A job title.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *jobTitle;

- `
  ``
  ``
  `

  ### [organization](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(py)organization)

  `
  `  
  A business organization.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *organization;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeContactInfo#/c:objc(cs)FIRVisionBarcodeContactInfo(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;