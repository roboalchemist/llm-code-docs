# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeDriverLicense


    @interface FIRVisionBarcodeDriverLicense : NSObject

A driver license or ID card data representation.

An ANSI driver license contains more fields than are represented by this class. The
[FIRVisionBarcode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcode.html)s `rawValue` property can be used to access the other fields.
- `
  ``
  ``
  `

  ### [firstName](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)firstName)

  `
  `  
  Holder's first name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *firstName;

- `
  ``
  ``
  `

  ### [middleName](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)middleName)

  `
  `  
  Holder's middle name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *middleName;

- `
  ``
  ``
  `

  ### [lastName](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)lastName)

  `
  `  
  Holder's last name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *lastName;

- `
  ``
  ``
  `

  ### [gender](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)gender)

  `
  `  
  Holder's gender. 1 is male and 2 is female.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *gender;

- `
  ``
  ``
  `

  ### [addressCity](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressCity)

  `
  `  
  Holder's city address.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *addressCity;

- `
  ``
  ``
  `

  ### [addressState](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressState)

  `
  `  
  Holder's state address.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *addressState;

- `
  ``
  ``
  `

  ### [addressStreet](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressStreet)

  `
  `  
  Holder's street address.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *addressStreet;

- `
  ``
  ``
  `

  ### [addressZip](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)addressZip)

  `
  `  
  Holder's address' zipcode.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *addressZip;

- `
  ``
  ``
  `

  ### [birthDate](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)birthDate)

  `
  `  
  Holder's birthday. The date format depends on the issuing country.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *birthDate;

- `
  ``
  ``
  `

  ### [documentType](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)documentType)

  `
  `  
  "DL" for driver licenses, "ID" for ID cards.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *documentType;

- `
  ``
  ``
  `

  ### [licenseNumber](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)licenseNumber)

  `
  `  
  Driver license ID number.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *licenseNumber;

- `
  ``
  ``
  `

  ### [expiryDate](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)expiryDate)

  `
  `  
  Driver license expiration date. The date format depends on the issuing country.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *expiryDate;

- `
  ``
  ``
  `

  ### [issuingDate](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)issuingDate)

  `
  `  
  The date format depends on the issuing country.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *issuingDate;

- `
  ``
  ``
  `

  ### [issuingCountry](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(py)issuingCountry)

  `
  `  
  A country in which DL/ID was issued.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *issuingCountry;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDriverLicense#/c:objc(cs)FIRVisionBarcodeDriverLicense(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;