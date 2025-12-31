# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentText.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionDocumentText


    @interface FIRVisionDocumentText : NSObject

Recognized document text in an image.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentText#/c:objc(cs)FIRVisionDocumentText(py)text)

  `
  `  
  String representation of the recognized document text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [blocks](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentText#/c:objc(cs)FIRVisionDocumentText(py)blocks)

  `
  `  
  An array of blocks recognized in the document text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextBlock.html *> *_Nonnull blocks;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentText#/c:objc(cs)FIRVisionDocumentText(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;