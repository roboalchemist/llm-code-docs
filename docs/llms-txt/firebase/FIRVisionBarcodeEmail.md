# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeEmail


    @interface FIRVisionBarcodeEmail : NSObject

An email message from a 'MAILTO:' or similar QR Code type.
- `
  ``
  ``
  `

  ### [address](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail#/c:objc(cs)FIRVisionBarcodeEmail(py)address)

  `
  `  
  Email message address.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *address;

- `
  ``
  ``
  `

  ### [body](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail#/c:objc(cs)FIRVisionBarcodeEmail(py)body)

  `
  `  
  Email message body.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *body;

- `
  ``
  ``
  `

  ### [subject](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail#/c:objc(cs)FIRVisionBarcodeEmail(py)subject)

  `
  `  
  Email message subject.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *subject;

- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail#/c:objc(cs)FIRVisionBarcodeEmail(py)type)

  `
  `  
  Email message type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeEmailType.html type;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeEmail#/c:objc(cs)FIRVisionBarcodeEmail(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;