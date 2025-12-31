# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionDocumentTextParagraph


    @interface FIRVisionDocumentTextParagraph : NSObject

A document text paragraph recognized in an image that consists of an array of words.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)text)

  `
  `  
  String representation of the document text paragraph that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [words](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)words)

  `
  `  
  An array of words in the document text paragraph.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextWord.html *> *_Nonnull words;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)frame)

  `
  `  
  The rectangle that contains the document text paragraph relative to the image in the default
  coordinate space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)confidence)

  `
  `  
  The confidence of the recognized document text paragraph.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull confidence;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text paragraph. If no languages are recognized,
  the array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text paragraph.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak.html *recognizedBreak;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph#/c:objc(cs)FIRVisionDocumentTextParagraph(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;