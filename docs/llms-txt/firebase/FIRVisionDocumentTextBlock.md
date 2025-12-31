# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionDocumentTextBlock


    @interface FIRVisionDocumentTextBlock : NSObject

A document text block recognized in an image that consists of an array of paragraphs.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)type)

  `
  `  
  The detected block type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionDocumentTextBlockType.html type;

- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)text)

  `
  `  
  String representation of the document text block that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [paragraphs](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)paragraphs)

  `
  `  
  An array of paragraphs in the block if the type is `VisionDocumentTextBlockType.text`. Otherwise,
  the array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextParagraph.html *> *_Nonnull paragraphs;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)frame)

  `
  `  
  The rectangle that contains the document text block relative to the image in the default
  coordinate space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)confidence)

  `
  `  
  The confidence of the recognized document text block.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull confidence;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the document text block. If no languages are recognized, the
  array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [recognizedBreak](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(py)recognizedBreak)

  `
  `  
  The recognized start or end of the document text block.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak.html *recognizedBreak;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock#/c:objc(cs)FIRVisionDocumentTextBlock(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;