# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionText.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionText


    @interface FIRVisionText : NSObject

Recognized text in an image.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionText#/c:objc(cs)FIRVisionText(py)text)

  `
  `  
  String representation of the recognized text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [blocks](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionText#/c:objc(cs)FIRVisionText(py)blocks)

  `
  `  
  An array of blocks recognized in the text.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock.html *> *_Nonnull blocks;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionText#/c:objc(cs)FIRVisionText(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;