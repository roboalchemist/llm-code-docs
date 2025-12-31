# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionDocumentTextSymbol


    @interface FIRVisionDocumentTextSymbol : NSObject

A document text symbol recognized in an image.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)text)

  `
  `  
  String representation of the document text symbol that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)frame)

  `
  `  
  The rectangle that contains the document text symbol relative to the image in the default
  coordinate space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)confidence)

  `
  `  
  The confidence of the recognized document text symbol.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull confidence;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text symbol. If no languages are recognized, the
  array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text symbol.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak.html *recognizedBreak;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol#/c:objc(cs)FIRVisionDocumentTextSymbol(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;