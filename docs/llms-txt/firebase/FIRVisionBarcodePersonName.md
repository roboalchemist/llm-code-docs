# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodePersonName


    @interface FIRVisionBarcodePersonName : NSObject

A person's name, both formatted and as individual name components.
- `
  ``
  ``
  `

  ### [formattedName](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)formattedName)

  `
  `  
  Properly formatted name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *formattedName;

- `
  ``
  ``
  `

  ### [first](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)first)

  `
  `  
  First name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *first;

- `
  ``
  ``
  `

  ### [last](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)last)

  `
  `  
  Last name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *last;

- `
  ``
  ``
  `

  ### [middle](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)middle)

  `
  `  
  Middle name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *middle;

- `
  ``
  ``
  `

  ### [prefix](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)prefix)

  `
  `  
  Name prefix.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *prefix;

- `
  ``
  ``
  `

  ### [pronounciation](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)pronounciation)

  `
  `  
  Designates a text string to be set as the kana name in the phonebook.
  Used for Japanese contacts.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *pronounciation;

- `
  ``
  ``
  `

  ### [suffix](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(py)suffix)

  `
  `  
  Name suffix.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *suffix;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodePersonName#/c:objc(cs)FIRVisionBarcodePersonName(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;