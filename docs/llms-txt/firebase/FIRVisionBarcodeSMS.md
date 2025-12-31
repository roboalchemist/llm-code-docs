# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeSMS.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeSMS


    @interface FIRVisionBarcodeSMS : NSObject

An SMS message from an 'SMS:' or similar QR Code type.
- `
  ``
  ``
  `

  ### [message](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeSMS#/c:objc(cs)FIRVisionBarcodeSMS(py)message)

  `
  `  
  An SMS message body.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *message;

- `
  ``
  ``
  `

  ### [phoneNumber](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeSMS#/c:objc(cs)FIRVisionBarcodeSMS(py)phoneNumber)

  `
  `  
  An SMS message phone number.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *phoneNumber;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeSMS#/c:objc(cs)FIRVisionBarcodeSMS(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;