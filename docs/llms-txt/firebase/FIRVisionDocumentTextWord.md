# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionDocumentTextWord


    @interface FIRVisionDocumentTextWord : NSObject

A document text word recognized in an image that consists of an array of symbols.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)text)

  `
  `  
  String representation of the document text word that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [symbols](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)symbols)

  `
  `  
  An array of symbols in the document text word.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextSymbol.html *> *_Nonnull symbols;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)frame)

  `
  `  
  The rectangle that contains the document text word relative to the image in the default
  coordinate space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)confidence)

  `
  `  
  The confidence of the recognized document text word.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull confidence;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text word. If no languages are recognized, the
  array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text word.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak.html *recognizedBreak;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord#/c:objc(cs)FIRVisionDocumentTextWord(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;